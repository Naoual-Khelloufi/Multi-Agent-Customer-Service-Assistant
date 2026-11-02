
from pathlib import Path
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# LLM configuration
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
LLM_MODEL_NAME = "openai/gpt-oss-20b"

# Project directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Data directories
RAW_DATA_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DATA_DIR = BASE_DIR / "data" / "processed"

# Vector database directory
VECTORSTORE_DIR = BASE_DIR / "vectorstore"

# Embedding model
EMBEDDING_MODEL_NAME = "intfloat/multilingual-e5-small"


# Retrieval
TOP_K = 4

# Chunking
CHUNK_SIZE = 600
CHUNK_OVERLAP = 100
