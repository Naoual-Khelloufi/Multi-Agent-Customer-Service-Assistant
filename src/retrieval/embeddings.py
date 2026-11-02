from sentence_transformers import SentenceTransformer
from src.config import EMBEDDING_MODEL_NAME


# Load the embedding model once
model = SentenceTransformer(EMBEDDING_MODEL_NAME)


def create_embeddings(texts):
    # E5 requires the "passage:" prefix for documents
    texts = [f"passage: {text}" for text in texts]

    embeddings = model.encode(
        texts,
        normalize_embeddings=True,
        show_progress_bar=False
    )

    return embeddings.tolist()


def create_query_embedding(query):
    # E5 requires the "query:" prefix for questions
    embedding = model.encode(
        f"query: {query}",
        normalize_embeddings=True
    )

    return embedding.tolist()