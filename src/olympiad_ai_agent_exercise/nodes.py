from langchain_openai import ChatOpenAI

from olympiad_ai_agent_exercise.state import State


class ChatNode:
    llm: ChatOpenAI

    def __init__(self, llm: ChatOpenAI) -> None:
        self.llm = llm

    def __call__(self, state: State) -> State:
        return {"messages": [self.llm.invoke(state["messages"])]}
