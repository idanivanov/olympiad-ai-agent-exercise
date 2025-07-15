from typing import Annotated, Any, Iterator

from langchain.chat_models import init_chat_model
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, StateGraph
from langgraph.graph.state import CompiledStateGraph
from langgraph.prebuilt import ToolNode, tools_condition
from pydantic import BaseModel, ConfigDict, Field, model_validator

from olympiad_ai_agent_exercise.nodes import ChatNode
from olympiad_ai_agent_exercise.settings import Settings
from olympiad_ai_agent_exercise.state import State
from olympiad_ai_agent_exercise.tools import tools


class Agent(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    model_name: Annotated[str, Field(default_factory=lambda: Settings().MODEL_NAME)]

    _llm: ChatOpenAI
    _graph: CompiledStateGraph

    @model_validator(mode="after")
    def _build_graph(self) -> "Agent":
        # Initialize the LLM with tools
        self._llm = init_chat_model(f"openai:{self.model_name}").bind_tools(tools)

        # Build the graph
        graph_builder = StateGraph(State)

        # Define the nodes
        graph_builder.add_node("chat", ChatNode(llm=self._llm))
        graph_builder.add_node("tools", ToolNode(tools=tools))

        # Define the edges
        graph_builder.add_edge(START, "chat")
        graph_builder.add_conditional_edges("chat", tools_condition)
        # Any time a tool is called, we return to the chatbot to decide the next step
        graph_builder.add_edge("tools", "chat")

        self._graph = graph_builder.compile(checkpointer=MemorySaver())
        return self

    def stream(self, user_input: str) -> Iterator[dict[str, Any] | Any]:
        yield from self._graph.stream(
            {
                "messages": [
                    {
                        "role": "user",
                        "content": user_input
                    }
                ]
            },
            config={"configurable": {"thread_id": "1"}}
        )

    def save_graph_to_png(self, file_path: str = "assets/graph.png") -> None:
        with open(file_path, "wb") as file_descr:
            file_descr.write(self._graph.get_graph().draw_mermaid_png())
