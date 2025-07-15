from langchain_community.agent_toolkits import FileManagementToolkit
from langchain_tavily import TavilySearch

from olympiad_ai_agent_exercise.settings import Settings

web_search_tool = TavilySearch(max_results=2)

file_system_tools = FileManagementToolkit(
    root_dir=Settings().DATA_DIR,
    selected_tools=["read_file", "write_file", "list_directory"],
).get_tools()


tools = [
    web_search_tool,
    *file_system_tools,
]
