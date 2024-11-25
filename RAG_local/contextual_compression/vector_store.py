# vector_store.py
import pinecone
from pinecone import Pinecone, ServerlessSpec
from typing import List, Dict, Any, Tuple
from config import (
    PINECONE_API_KEY,
    INDEX_NAME,
    EMBEDDING_DIMENSION,
    SIMILARITY_THRESHOLD,
    TOP_K
)
my_index_name = INDEX_NAME
pc = Pinecone(api_key=PINECONE_API_KEY)
def get_pinecone_index():
    if my_index_name not in pc.list_indexes().names():
        pc.create_index(
            name=my_index_name, 
            dimension=1536, 
            metric='cosine',
            spec=ServerlessSpec(
                cloud='aws',
                region='us-east-1'
            )
        )
    return pc.Index(my_index_name)

def add_documents(index: pinecone.Index,
                 documents: List[Tuple[str, Dict[str, Any]]],
                 embeddings: List[List[float]],
                 batch_size: int = 100) -> None:
    """Add documents to Pinecone index in batches."""
    for i in range(0, len(documents), batch_size):
        batch_docs = documents[i:i + batch_size]
        batch_embeddings = embeddings[i:i + batch_size]
        
        vectors = []
        for j, ((text, metadata), embedding) in enumerate(zip(batch_docs, batch_embeddings)):
            vectors.append({
                'id': f'doc_{i+j}',
                'values': embedding,
                'metadata': {
                    'text': text,
                    **metadata
                }
            })
        
        index.upsert(vectors=vectors)

def similarity_search(index: pinecone.Index,
                     query_embedding: List[float],
                     top_k: int = TOP_K) -> List[Tuple[str, Dict[str, Any]]]:
    """Search for similar documents in Pinecone index."""
    results = index.query(
        vector=query_embedding,
        top_k=top_k,
        include_metadata=True
    )

    documents = []
    for match in results.matches:
        if match.score < SIMILARITY_THRESHOLD:
            continue
            
        text = match.metadata.pop('text')
        documents.append((text, match.metadata))

    return documents