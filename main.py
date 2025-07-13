from langchain_openai import ChatOpenAI

from olympiad_ai_agent_exercise.settings import Settings

settings = Settings()

llm = ChatOpenAI(
    model="gpt-4o-mini",
)
response = llm.invoke("TEST!")
print(response)
