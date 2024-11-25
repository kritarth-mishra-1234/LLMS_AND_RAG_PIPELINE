import os
from dotenv import load_dotenv

load_dotenv()

# Configuration variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_ENV = os.getenv("PINECONE_ENV")
EMBEDDING_MODEL = "text-embedding-ada-002"  # OpenAI embedding model
DIMENSION = 1536  # OpenAI embedding dimension
INDEX_NAME = "mishra3"
    