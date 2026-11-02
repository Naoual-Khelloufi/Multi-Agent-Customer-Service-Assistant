from src.agents.retrieval_agent import retrieval_agent


state = {
    "question": "How should an agent handle an angry customer?"
}

result = retrieval_agent(state)

print("\nRetrieved context:")
print(result["context"])

print("\nSources:")
for source in result["sources"]:
    print("-", source)