<p align="center">
  <a href="https://github.com/XpressAI/xircuits/tree/master/xai_components#xircuits-component-library-list">Component Libraries</a> •
  <a href="https://github.com/XpressAI/xircuits/tree/master/project-templates#xircuits-project-templates-list">Project Templates</a>
  <br>
  <a href="https://xircuits.io/">Docs</a> •
  <a href="https://xircuits.io/docs/Installation">Install</a> •
  <a href="https://xircuits.io/docs/category/tutorials">Tutorials</a> •
  <a href="https://xircuits.io/docs/category/developer-guide">Developer Guides</a> •
  <a href="https://github.com/XpressAI/xircuits/blob/master/CONTRIBUTING.md">Contribute</a> •
  <a href="https://www.xpress.ai/blog/">Blog</a> •
  <a href="https://discord.com/invite/vgEg2ZtxCw">Discord</a>
</p>

<p align="center"><i>Xircuits Component Library for SerpAPI! Seamlessly integrate web search capabilities into your workflows.</i></p>

---

## Xircuits Component Library for SerpAPI

This library allows Xircuits to interact with SerpAPI, enabling web searches across various search engines like Google, Bing, and Yahoo. It provides components for authentication and performing searches directly within Xircuits workflows.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Main Xircuits Components](#main-xircuits-components)
- [Try the Examples](#try-the-examples)
- [Installation](#installation)


## Prerequisites

Before you begin, you will need the following:

1. Python3.9+.
2. Xircuits.
3. A SerpAPI API Key (obtainable from [SerpAPI](https://serpapi.com/)).

## Main Xircuits Components

### SerpApiAuthorize Component:  
Authenticates and initializes the SerpAPI client.  

<img src="https://github.com/user-attachments/assets/bb017eb5-e7ef-42b5-99ee-e598417b6075" alt="Image" width="200" height="100" />

### SerpApiSearch Component:  
Performs a web search using SerpAPI, retrieving results from search engines like Google, Bing, and Yahoo.  

<img src="https://github.com/user-attachments/assets/aeb09eeb-1b1e-4a13-954c-fb8352ada9f4" alt="Image" width="200" height="150" />

## Try The Examples

We have provided an example workflow to help you get started with the SerpAPI component library. Give it a try and see how you can create custom SerpAPI workflows for your applications.

### SerpAPI Example
This example demonstrates how to authenticate with SerpAPI, perform a search, and process the retrieved results.

## Installation

To use this component library, ensure that you have an existing [Xircuits setup](https://xircuits.io/docs/main/Installation). You can then install the SerpAPI library using the [component library interface](https://xircuits.io/docs/component-library/installation#installation-using-the-xircuits-library-interface), or through the CLI using:

```
xircuits install serpapi
```
You can also do it manually by cloning and installing it:
```
# base Xircuits directory
git clone https://github.com/XpressAI/xai-serpapi xai_components/xai_serpapi
pip install -r xai_components/xai_serpapi/requirements.txt
```

