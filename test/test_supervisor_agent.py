from src.agents.supervisor_agent import supervisor_agent

state = {
    "question": "How should an agent handle an angry customer?"
}

result = supervisor_agent(state)

print("Supervisor result:")
print(result)
