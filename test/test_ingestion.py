from src.ingestion.document_loader import load_documents
from src.ingestion.document_processor import process_documents


# Load Word documents
documents = load_documents()

# Split documents into chunks
chunks = process_documents(documents)

# Display results
print("\nIngestion Test Results:")
print(f"Documents loaded: {len(documents)}")
print(f"Chunks generated: {len(chunks)}")

if chunks:
    print("\nFirst chunk:")
    print(chunks[0].page_content)

    print("\nMetadata:")
    print(chunks[0].metadata)
else:
    print("No chunks generated.")