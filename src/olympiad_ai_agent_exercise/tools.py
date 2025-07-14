from langchain_tavily import TavilySearch


web_search_tool = TavilySearch(max_results=2)


tools = [
    web_search_tool
]
