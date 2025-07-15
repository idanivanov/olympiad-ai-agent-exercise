from langchain_core.messages import SystemMessage
from langchain_openai import ChatOpenAI

from olympiad_ai_agent_exercise.state import State


class ChatNode:
    llm: ChatOpenAI

    def __init__(self, llm: ChatOpenAI) -> None:
        self.llm = llm

    def __call__(self, state: State) -> State:
        return {"messages": [self.llm.invoke(state["messages"])]}


class PlanningNode:
    llm: ChatOpenAI

    def __init__(self, llm: ChatOpenAI) -> None:
        self.llm = llm

    def __call__(self, state: State) -> State:
        # Prepend a planning prompt and ask the LLM to generate a concise action plan
        planning_prompt = state["messages"] + [
            {
                "role": "system",
                "content": (
                    "You are the planning module for an autonomous AI agent. "
                    "Given the last user message, think step-by-step and output a concise bullet-point plan "
                    "(3-6 bullets) describing the actions the agent should take next. "
                    "Do NOT execute any tools or provide final answers – only produce the plan."
                ),
            }
        ]

        plan_message = self.llm.invoke(planning_prompt)

        # Store the plan back into the conversation as a system message for later reference
        plan_message = SystemMessage(content=plan_message.content, name="plan")
        return {"messages": [plan_message]}
