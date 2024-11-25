# main.py
import config
from embeddings import get_embeddings
from vector_store import init_pinecone, upsert_to_pinecone, query_pinecone
from document_loader import load_documents
from text_splitter import process_documents
from typing import List, Dict, Any, Tuple
import os
def process_and_store_documents(
    file_paths: List[str],
    chunk_size: int = 1000,
    chunk_overlap: int = 0
) -> List[Tuple[str, Dict[str, Any]]]:
    """
    Complete pipeline for processing documents and storing in vector database.
    
    Args:
        file_paths: List of paths to text files
        chunk_size: Size of text chunks
        chunk_overlap: Overlap between chunks
        
    Returns:
        List of processed document chunks with metadata
    """
    blog_posts_dir = "langchain_blog_posts"
    file_paths = [
        os.path.join(blog_posts_dir, "blog.langchain.dev_announcing-langsmith_.txt"),
        os.path.join(blog_posts_dir, "blog.langchain.dev_benchmarking-question-answering-over-csv-data_.txt")
    ]
    # Initialize Pinecone
    index = init_pinecone()
    
    # Load and process documents
    raw_docs = load_documents(file_paths)
    processed_chunks = process_documents(raw_docs, chunk_size, chunk_overlap)
    
    # Get embeddings
    texts = [chunk for chunk, _ in processed_chunks]
    embeddings = get_embeddings(texts)
    
    # Store in Pinecone
    metadata = [meta for _, meta in processed_chunks]
    upsert_to_pinecone(index, texts, embeddings, metadata)
    
    return processed_chunks

def search_documents(
    query: str,
    top_k: int = 3
) -> List[Dict[str, Any]]:
    """
    Search for relevant document chunks.
    
    Args:
        query: Search query
        top_k: Number of results to return
        
    Returns:
        List of relevant chunks with scores and metadata
    """
    index = init_pinecone()
    query_embedding = get_embeddings([query])[0]
    return query_pinecone(index, query_embedding, top_k)

def main():
    # Example usage
    file_paths = [
        '/content/blog_posts/blog.langchain.dev_announcing-langsmith_.txt',
        '/content/blog_posts/blog.langchain.dev_benchmarking-question-answering-over-csv-data_.txt',
        '/content/blog_posts/blog.langchain.dev_chat-loaders-finetune-a-chatmodel-in-your-voice_.txt'
    ]
    
    # Process and store documents
    processed_chunks = process_and_store_documents(
        file_paths,
        chunk_size=1000,
        chunk_overlap=0
    )
    print(f"\nProcessed {len(processed_chunks)} document chunks")
    
    # Example search
    query = "What is LangSmith?"
    results = search_documents(query)
    
    print("\nQuery:", query)
    print("\nRelevant document chunks:")
    for i, result in enumerate(results, 1):
        print(f"\n{i}. Score: {result['score']:.3f}")
        print(f"   Text: {result['text'][:200]}...")
        print(f"   Source: {result['metadata'].get('filename', 'Unknown')}")

if __name__ == "__main__":
    main()