"""Assert Relay credentials stay in headers and direct SerpAPI auth still works."""
import runpy
import sys
from pathlib import Path
from types import ModuleType, SimpleNamespace

import pytest
import requests


@pytest.fixture
def component(monkeypatch):
    base = ModuleType("xai_components.base")
    class Port:
        def __class_getitem__(cls, item):
            return cls
    base.InArg = base.InCompArg = base.OutArg = Port
    base.Component = object
    base.secret = str
    base.xai_component = lambda cls: cls
    monkeypatch.setitem(sys.modules, "xai_components", ModuleType("xai_components"))
    monkeypatch.setitem(sys.modules, "xai_components.base", base)
    module = runpy.run_path(str(Path(__file__).resolve().parents[1] / "serp_components.py"))
    component = module["SerpApiAuthorize"]()
    component.from_env = SimpleNamespace(value=False)
    component.api_key = SimpleNamespace(value=None)
    component.client = SimpleNamespace(value=None)
    return component


@pytest.mark.parametrize("credential", [None, "", "   "])
def test_relay_never_falls_back_to_vector_credentials(component, monkeypatch, credential):
    monkeypatch.setenv("VECTO_API_KEY", "vector-key")
    if credential is None:
        monkeypatch.delenv("XPRESSAI_RELAY_TOKEN", raising=False)
    else:
        monkeypatch.setenv("XPRESSAI_RELAY_TOKEN", credential)
    with pytest.raises(ValueError, match="XPRESSAI_RELAY_TOKEN"):
        component.execute({})
    assert component.client.value is None


def test_relay_authentication_is_in_header_not_query(component, monkeypatch):
    monkeypatch.setenv("XPRESSAI_RELAY_TOKEN", "relay-credential")
    component.execute({})
    captured = []
    def send(request, **kwargs):
        captured.append(request)
        response = requests.Response()
        response.status_code = 200
        response._content = b'{}'
        return response
    monkeypatch.setattr(component.client.value.session, "send", send)
    component.client.value.request("GET", "/search.json", {"q": "test"})
    assert captured[0].headers["Authorization"] == "Bearer relay-credential"
    assert "relay-credential" not in captured[0].url
    assert "api_key" not in captured[0].url


@pytest.mark.parametrize("from_env", [False, True])
def test_direct_serpapi_auth_is_preserved(component, monkeypatch, from_env):
    component.from_env.value = from_env
    component.api_key.value = "explicit-serp-key"
    monkeypatch.setenv("SERP_API_KEY", "environment-serp-key")
    monkeypatch.delenv("XPRESSAI_RELAY_TOKEN", raising=False)
    component.execute({})
    assert component.client.value.api_key == ("environment-serp-key" if from_env else "explicit-serp-key")
    assert "Authorization" not in component.client.value.session.headers
