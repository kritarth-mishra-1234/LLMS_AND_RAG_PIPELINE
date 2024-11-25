import openai
from typing import List
import numpy as np
from config import OPENAI_API_KEY

client = openai.OpenAI(api_key=OPENAI_API_KEY)

def get_embeddings(texts: List[str]) -> List[List[float]]:
    """Generate embeddings using OpenAI API."""
    try:
        response = client.embeddings.create(
            input=texts,
            model="text-embedding-ada-002"
        )
        return [r.embedding for r in response.data]
    except Exception as e:
        print(f"Error generating embeddings: {str(e)}")
        return []