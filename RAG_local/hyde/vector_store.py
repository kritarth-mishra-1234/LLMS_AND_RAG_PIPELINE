import pinecone
from typing import List, Dict, Any
import config
from pinecone import Pinecone, ServerlessSpec
import numpy as np
PINECONE_INDEX_NAME = config.INDEX_NAME
pc=Pinecone(api_key=config.PINECONE_API_KEY)
def init_pinecone():
    if PINECONE_INDEX_NAME not in pc.list_indexes().names():
        pc.create_index(
            name=PINECONE_INDEX_NAME, 
            dimension=1536, 
            metric='cosine',
            spec=ServerlessSpec(
                cloud='aws',
                region='us-east-1'
            )
        )
    return pc.Index(PINECONE_INDEX_NAME)

def upsert_to_pinecone(
    index: pinecone.Index,
    texts: List[str],
    embeddings: np.ndarray,
    metadata: List[Dict] = None
) -> None:
    """
    Upsert texts and their embeddings to Pinecone.
    
    Args:
        index: Pinecone index
        texts: List of texts
        embeddings: numpy array of embeddings
        metadata: List of metadata dictionaries
    """
    if metadata is None:
        metadata = [{} for _ in texts]
    
    vectors = [
        (str(i), emb.tolist(), {"text": text, **meta})
        for i, (emb, text, meta) in enumerate(zip(embeddings, texts, metadata))
    ]
    
    index.upsert(vectors=vectors)

def query_pinecone(
    index: pinecone.Index,
    query_embedding: np.ndarray,
    top_k: int = 5
) -> List[Dict[str, Any]]:
    """
    Query Pinecone for similar vectors.
    
    Args:
        index: Pinecone index
        query_embedding: Query embedding vector
        top_k: Number of results to return
        
    Returns:
        List of similar items with scores and metadata
    """
    results = index.query(
        vector=query_embedding.tolist(),
        top_k=top_k,
        include_metadata=True
    )
    
    return [{
        'score': match.score,
        'text': match.metadata.get('text', ''),
        'metadata': match.metadata
    } for match in results.matches]
