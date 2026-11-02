from src.ingestion.document_loader import load_documents
from src.ingestion.document_processor import process_documents
from src.retrieval.vector_store import add_documents, search_documents


# Load and process documents
documents = load_documents()
chunks = process_documents(documents)

# Store documents in ChromaDB
add_documents(chunks)

# Test semantic search
query = "How should an agent handle an angry customer?"

results = search_documents(query)

print("\nVector Store Test Results:")
print(f"Query: {query}")
print(f"Results found: {len(results)}")

for i, document in enumerate(results, start=1):
    print(f"\nResult {i}:")
    print(document.page_content)
    print("Source:", document.metadata.get("source"))
    print("Distance:", document.metadata.get("distance"))