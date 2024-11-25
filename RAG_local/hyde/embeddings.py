import openai
import numpy as np
from typing import List
import config

openai.api_key = config.OPENAI_API_KEY

def get_embeddings(texts: List[str]) -> np.ndarray:
    """
    Get embeddings for a list of texts using OpenAI's embedding model.
    
    Args:
        texts: List of strings to get embeddings for
        
    Returns:
        numpy array of embeddings
    """
    try:
        response = openai.Embedding.create(
            input=texts,
            model=config.EMBEDDING_MODEL
        )
        return np.array([embedding.embedding for embedding in response['data']])
    except Exception as e:
        print(f"Error getting embeddings: {e}")
        raise
