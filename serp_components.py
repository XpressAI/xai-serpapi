from xai_components.base import InArg, InCompArg, OutArg, Component, xai_component, secret
import os
import serpapi


@xai_component
class SerpApiAuthorize(Component):
    """A component to authorize and initialize a SerpAPI client.

    ##### inPorts:
    - api_key (secret): The SerpAPI key.
    - from_env (bool): Use API key from environment variable if True.

    ##### outPorts:
    - client (object): The initialized SerpAPI client.
    """
    api_key: InArg[secret]
    from_env: InCompArg[bool]

    client: OutArg[object]

    def execute(self, ctx) -> None:
        if self.from_env.value:
            client = serpapi.Client(api_key=os.getenv('SERP_API_KEY', None))
        else:
            # Initialize the SerpApi client with the provided API key
            client = serpapi.Client(api_key=self.api_key.value)

        ctx['serp_client'] = client
        self.client.value = client


@xai_component
class SerpApiSearch(Component):
    """A component to search the web using SerpAPI.

    ##### inPorts:
    - query (str): The search query.
    - engine (str): The search engine to use (e.g., 'google', 'bing', 'yahoo', etc.).
    - client (str): Optional SerpAPI Client.

    ##### outPorts:
    - results (dict): The search results returned from SerpAPI.
    """
    query: InCompArg[str]
    engine: InCompArg[str]
    client: InArg[object]
    results: OutArg[dict]

    def execute(self, ctx) -> None:
        if self.client.value is not None:
            # Initialize the SerpApi client with the provided API key
            client = self.client.value
        else:
            client = ctx['serp_client']

        # Perform the search
        search_results = client.search({
            'engine': self.engine.value,
            'q': self.query.value
        })

        # Set the results to the output port
        self.results.value = dict(search_results)
