import pinecone
from typing import List, Dict
from . import embedding_utils
from .document_utils import Document
from config import PINECONE_API_KEY,PINECONE_INDEX_NAME

def init_pinecone() -> pinecone.Index:
    '''Initialize Pinecone and return index'''
    pinecone.init(api_key=PINECONE_API_KEY, environment=PINECONE_ENV)
    
    # Create index if it doesn't exist
    if PINECONE_INDEX_NAME not in pinecone.list_indexes():
        pinecone.create_index(
            name=PINECONE_INDEX_NAME,
            dimension=384,  # dimension for 'all-MiniLM-L6-v2'
            metric='cosine'
        )
    
    return pinecone.Index(PINECONE_INDEX_NAME)

pc = Pinecone(api_key=PINECONE_API_KEY)
def init_pinecone() -> pinecone.Index:
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


def add_documents(index: pinecone.Index, documents: List[Document]):
    '''Add documents to Pinecone index'''
    for i, doc in enumerate(documents):
        embedding = embedding_utils.embed_text(doc["content"])
        index.upsert(
            vectors=[(str(i), embedding, {"content": doc["content"], **doc["metadata"]})]
        )

def similarity_search(index: pinecone.Index, query: str, k: int = 4) -> List[Document]:
    '''Search for similar documents'''
    query_embedding = embedding_utils.embed_text(query)
    results = index.query(query_embedding, top_k=k, include_metadata=True)
    
    documents = []
    for match in results.matches:
        metadata = dict(match.metadata)
        content = metadata.pop("content")
        documents.append({
            "content": content,
            "metadata": metadata
        })
    
    return documents