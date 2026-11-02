
from pathlib import Path
from docx import Document as WordDocument
from langchain_core.documents import Document
from src.config import RAW_DATA_DIR


def load_documents():
    documents = []

    # Get all Word files from data/raw
    files = list(RAW_DATA_DIR.glob("*.docx"))

    if not files:
        print("No Word documents found.")
        return documents

    for file_path in files:

        word_file = WordDocument(file_path)
        text = []

        # Extract paragraphs
        for paragraph in word_file.paragraphs:
            if paragraph.text.strip():
                text.append(paragraph.text.strip())

        # Extract tables
        for table in word_file.tables:
            for row in table.rows:
                row_text = " | ".join(
                    cell.text.strip() for cell in row.cells
                )

                if row_text.strip():
                    text.append(row_text)

        # Combine all extracted text
        full_text = "\n".join(text)

        if full_text.strip():

            documents.append(
                Document(
                    page_content=full_text,
                    metadata={
                        "source": file_path.name,
                        "document_id": file_path.stem
                    }
                )
            )

        print(f"Loaded: {file_path.name}")

    print(f"\nTotal documents loaded: {len(documents)}")

    return documents
