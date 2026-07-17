from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun


# Initialize the search tool
search = DuckDuckGoSearchRun()


@tool
def web_search_tool(query: str) -> str:
    """
    Searches the web and returns relevant information.
    """
    return search.run(query)


# Example usage
query = "Latest advancements in Artificial Intelligence"

result = web_search_tool.invoke(query)

print(result)