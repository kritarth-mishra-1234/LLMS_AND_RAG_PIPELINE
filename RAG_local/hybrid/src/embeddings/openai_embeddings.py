# src/embeddings/openai_embeddings.py
from openai import OpenAI
from config.config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def embed_texts(texts):
    """Generate embeddings for a list of texts."""
    embeddings = []
    for text in texts:
        response = client.embeddings.create(
            model="text-embedding-ada-002",
            input=text
        )
        embeddings.append(response.data[0].embedding)
    return embeddings

def embed_query(text):
    """Generate embedding for a single query text."""
    response = client.embeddings.create(
        model="text-embedding-ada-002",
        input=text
    )
    return response.data[0].embedding