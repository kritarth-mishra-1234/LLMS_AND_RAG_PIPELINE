import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
# PINECONE_ENVIRONMENT = os.getenv("PINECONE_ENVIRONMENT")
# PINECONE_INDEX_NAME = "wine-index"

#extra after removing langchain
EMBEDDING_MODEL = "text-embedding-ada-002"  # OpenAI's embedding model