# src/retrievers/pinecone_retriever.py
import pinecone
from config.config import (
    PINECONE_API_KEY, 
    PINECONE_INDEX_NAME
)
import os
from pinecone import Pinecone, ServerlessSpec

pc = Pinecone(api_key=PINECONE_API_KEY)
# def initialize_pinecone():

#     if PINECONE_INDEX_NAME not in pinecone.list_indexes():
#         pinecone.create_index(
#             name=PINECONE_INDEX_NAME,
#             dimension=1536,  # OpenAI embedding dimension
#             metric='cosine'
#         )
    
#     return pinecone.Index(PINECONE_INDEX_NAME)




def initialize_pinecone():
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


def add_texts_to_pinecone(index, texts, embeddings):
    """Add texts and their embeddings to Pinecone."""
    vectors = [
        (str(i), embedding, {"text": text})
        for i, (text, embedding) in enumerate(zip(texts, embeddings))
    ]
    index.upsert(vectors=vectors)

def get_pinecone_documents(index, query_embedding, k=2):
    """Get relevant documents from Pinecone."""
    results = index.query(
        vector=query_embedding,
        top_k=k,
        include_metadata=True
    )
    
    return [{"text": match.metadata["text"], "score": match.score} 
            for match in results.matches]