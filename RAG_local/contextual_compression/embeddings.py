# embeddings.py
from typing import List
import openai
from config import OPENAI_API_KEY, EMBEDDING_MODEL

# Initialize OpenAI
openai.api_key = OPENAI_API_KEY

def embed_documents(texts: List[str]) -> List[List[float]]:
    """Generate embeddings for a list of documents."""
    # OpenAI recommends replacing newlines with spaces for best results
    texts = [text.replace("\n", " ") for text in texts]
    
    try:
        response = openai.Embedding.create(
            input=texts,
            model=EMBEDDING_MODEL
        )
        return [data.embedding for data in response.data]
    except Exception as e:
        print(f"Error generating embeddings: {e}")
        raise

def embed_query(text: str) -> List[float]:
    """Generate embeddings for a single query."""
    # OpenAI recommends replacing newlines with spaces for best results
    text = text.replace("\n", " ")
    
    try:
        response = openai.Embedding.create(
            input=[text],
            model=EMBEDDING_MODEL
        )
        return response.data[0].embedding
    except Exception as e:
        print(f"Error generating embedding for query: {e}")
        raise