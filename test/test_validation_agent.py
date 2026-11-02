from src.agents.validation_agent import validation_agent

# Using a mock state to test validation logic without consuming API quota.
state = {
    "question": "How should an agent handle an angry customer?",
    "context": "The agent should listen actively and remain calm.",
    "sources": ["DOC-03_Complaint_and_Conflict_Management.docx"],
    "answer": "The agent should listen actively and remain calm.",
    "generation_status": "success"
}

result = validation_agent(state)

print("Validation result:")
print(result)
