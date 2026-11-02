from src.graph.workflow import customer_service_app

question = "How should an agent handle an angry customer?"

result = customer_service_app.invoke({
    "question": question
})

print("\nQuestion:")
print(question)

print("\nGenerated answer:")
print(result.get("answer"))

print("\nSources:")
for source in result.get("sources", []):
    print("-", source)

print("\nValidation:")
print(result.get("validation_status"))
print(result.get("validation_message"))