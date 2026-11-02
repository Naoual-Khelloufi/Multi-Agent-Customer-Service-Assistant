import chromadb
from langchain_core.documents import Document
from src.config import VECTORSTORE_DIR, TOP_K
from src.retrieval.embeddings import (
    create_embeddings,
    create_query_embedding
)


# Initialize ChromaDB
client = chromadb.PersistentClient(
    path=str(VECTORSTORE_DIR)
)

collection = client.get_or_create_collection(
    name="customer_service",
    metadata={"hnsw:space": "cosine"}
)


def add_documents(chunks):

    texts = [chunk.page_content for chunk in chunks]
    metadatas = [chunk.metadata for chunk in chunks]

    # Create unique IDs for each chunk
    ids = [f"chunk_{i}" for i in range(len(chunks))]

    # Generate embeddings
    embeddings = create_embeddings(texts)

    # Store everything in ChromaDB
    collection.upsert(
        ids=ids,
        documents=texts,
        metadatas=metadatas,
        embeddings=embeddings
    )

    print(f"{len(chunks)} chunks stored in ChromaDB.")


def search_documents(query, top_k=TOP_K):

    query_embedding = create_query_embedding(query)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=min(top_k, collection.count())
    )

    documents = []

    if results["documents"] and results["documents"][0]:

        for i, text in enumerate(results["documents"][0]):

            documents.append(
                Document(
                    page_content=text,
                    metadata={
                        **results["metadatas"][0][i],
                        "distance": results["distances"][0][i]
                    }
                )
            )

    return documents