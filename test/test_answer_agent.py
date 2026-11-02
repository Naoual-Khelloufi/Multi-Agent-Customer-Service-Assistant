from src.agents.retrieval_agent import retrieval_agent
from src.agents.answer_agent import answer_agent


# User question
question = "How should an agent handle an angry customer?"

# Initial state
state = {
    "question": question
}

# Retrieve relevant documents
retrieval_result = retrieval_agent(state)

# Update state with retrieved context
state.update(retrieval_result)

# Generate answer
answer_result = answer_agent(state)

# Display results
print("\nQuestion:")
print(question)

print("\nGenerated answer:")
print(answer_result["answer"])

print("\nGeneration status:")
print(answer_result["generation_status"])

print("\nSources:")
for source in state["sources"]:
    print("-", source)