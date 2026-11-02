
from langchain_text_splitters import RecursiveCharacterTextSplitter

from src.config import CHUNK_SIZE, CHUNK_OVERLAP


def process_documents(documents):
    # Create the text splitter
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )

    # Split documents into chunks
    chunks = text_splitter.split_documents(documents)

    print(f"Documents received: {len(documents)}")
    print(f"Chunks generated: {len(chunks)}")

    return chunks
