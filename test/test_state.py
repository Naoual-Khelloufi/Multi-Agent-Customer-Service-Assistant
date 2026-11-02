from src.graph.state import CustomerServiceState

# Mock state to test the shared state structure without API calls
state: CustomerServiceState = {
    "question": "How should an agent handle an angry customer?",
    "next_step": "retrieve",
    "supervisor_message": "Question accepted.",
    "context": "",
    "sources": [],
    "retrieved_documents": [],
    "answer": "",
    "generation_status": "",
    "validation_status": "",
    "validation_message": ""
}

print("State initialized successfully:")
print(state)