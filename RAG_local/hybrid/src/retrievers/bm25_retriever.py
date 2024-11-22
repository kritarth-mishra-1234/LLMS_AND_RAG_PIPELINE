# src/retrievers/bm25_retriever.py
from rank_bm25 import BM25Okapi
import numpy as np

def initialize_bm25(texts):
    """Initialize BM25 with given texts."""
    tokenized_corpus = [doc.lower().split() for doc in texts]
    return BM25Okapi(tokenized_corpus)

def get_bm25_documents(bm25, texts, query, k=2):
    """Get relevant documents using BM25."""
    tokenized_query = query.lower().split()
    doc_scores = bm25.get_scores(tokenized_query)
    top_k_indices = np.argsort(doc_scores)[-k:][::-1]
    
    return [{"text": texts[i], "score": doc_scores[i]} 
            for i in top_k_indices]