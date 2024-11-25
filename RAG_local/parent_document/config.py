import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

CHUNK_SIZE = 400
PARENT_CHUNK_SIZE = 2000
INDEX_NAME = os.getenv("PINECONE_INDEX_NAME")
