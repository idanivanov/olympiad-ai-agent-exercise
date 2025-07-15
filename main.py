from olympiad_ai_agent_exercise.agent import Agent
from olympiad_ai_agent_exercise.state import State
from olympiad_ai_agent_exercise.settings import Settings

settings = Settings()

agent = Agent()

agent.save_graph_to_png()

while True:
    user_input = input("User: ")
    if user_input.lower() in ["quit", "exit", "q"]:
        print("Goodbye!")
        break
    for event in agent.stream(user_input):
        for value in event.values():
            print("\n")
            value["messages"][-1].pretty_print()
            print("\n================================================================================\n")
