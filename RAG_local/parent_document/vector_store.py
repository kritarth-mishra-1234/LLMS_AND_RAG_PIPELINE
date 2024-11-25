import pinecone
from typing import List, Dict
from config import PINECONE_API_KEY, INDEX_NAME
from pinecone import Pinecone, ServerlessSpec
# def init_pinecone():
#     """Initialize Pinecone client."""
#     pinecone.init(api_key=PINECONE_API_KEY, environment=PINECONE_ENV)
    
#     # Create index if it doesn't exist
#     if INDEX_NAME not in pinecone.list_indexes():
#         pinecone.create_index(
#             name=INDEX_NAME,
#             dimension=1536,  # OpenAI embedding dimension
#             metric="cosine"
#         )
my_index_name = INDEX_NAME
pc = Pinecone(api_key=PINECONE_API_KEY)
def init_pinecone():
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
def store_documents(documents: List[Dict], embeddings: List[List[float]]):
    """Store documents and their embeddings in Pinecone."""
    index = init_pinecone()
    
    vectors = []
    for i, (doc, embedding) in enumerate(zip(documents, embeddings)):
        vectors.append({
            'id': f'doc_{i}',
            'values': embedding,
            'metadata': {
                'text': doc['text'],
                'source': doc['source'],
                **doc['metadata']
            }
        })
    
    # Upsert in batches
    batch_size = 100
    for i in range(0, len(vectors), batch_size):
        batch = vectors[i:i + batch_size]
        index.upsert(vectors=batch)

def similarity_search(query_embedding: List[float], k: int = 2) -> List[Dict]:
    """Search for similar documents in Pinecone."""
    index = init_pinecone()
    
    results = index.query(
        vector=query_embedding,
        top_k=k,
        include_metadata=True
    )
    
    return [
        {
            'text': match['metadata']['text'],
            'source': match['metadata']['source'],
            'score': match['score']
        }
        for match in results['matches']
    ]