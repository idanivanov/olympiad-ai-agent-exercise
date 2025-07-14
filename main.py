from olympiad_ai_agent_exercise.agent import Agent
from olympiad_ai_agent_exercise.settings import Settings

settings = Settings()

agent = Agent()

agent.save_graph_to_png()

while True:
    try:
        user_input = input("User: ")
        if user_input.lower() in ["quit", "exit", "q"]:
            print("Goodbye!")
            break
        for event in agent.stream(user_input):
            for value in event.values():
                print("Assistant:", value)
    except Exception as e:  # pylint: disable=broad-exception-caught
        # fallback if input() is not available
        user_input = "What do you know about LangGraph?"
        print("User: " + user_input)
        for event in agent.stream(user_input):
            for value in event.values():
                print("Assistant:", value)
        break
