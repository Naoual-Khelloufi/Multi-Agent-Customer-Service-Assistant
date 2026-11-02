from src.retrieval.vector_store import search_documents


def retrieval_agent(state):

    question = state["question"]

    # Retrieve relevant documents
    retrieved_documents = search_documents(question)

    # Extract text and sources
    context = "\n\n".join(
        document.page_content
        for document in retrieved_documents
    )

    sources = list(set(
        document.metadata["source"]
        for document in retrieved_documents
    ))

    return {
        "context": context,
        "sources": sources,
        "retrieved_documents": retrieved_documents
    }