# config.py
import os
from dotenv import load_dotenv

load_dotenv()

# API Keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

# OpenAI Configuration
EMBEDDING_MODEL = "text-embedding-ada-002"
EMBEDDING_DIMENSION = 1536  # Dimension for text-embedding-ada-002

# Text Splitting Configuration
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

# Vector Search Configuration
SIMILARITY_THRESHOLD = 0.76
TOP_K = 4

# Pinecone Configuration
INDEX_NAME = "mishra2"