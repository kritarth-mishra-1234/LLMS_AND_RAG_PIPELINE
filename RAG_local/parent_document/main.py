from document_loader import load_documents
from text_splitter import split_text
from embeddings import get_embeddings
from vector_store import init_pinecone, store_documents, similarity_search
from qa_system import generate_answer
from config import CHUNK_SIZE
import os
def main():
    # Initialize Pinecone
    init_pinecone()
    
    # Load documents
    file_paths = [
        'RAG_local/parent_document/langchain_blog_posts.langchain.dev_announcing-langsmith_.txt',
        'RAG_local/parent_document/langchain_blog_posts.langchain.dev_benchmarking-question-answering-over-csv-data_.txt'
    ]
    documents = load_documents(file_paths)
    
    # Process and store documents
    all_chunks = []
    for doc in documents:
        chunks = split_text(doc['text'], CHUNK_SIZE)
        for chunk in chunks:
            all_chunks.append({
                'text': chunk,
                'source': doc['source'],
                'metadata': doc['metadata']
            })
    
    # Generate embeddings
    chunk_texts = [chunk['text'] for chunk in all_chunks]
    embeddings = get_embeddings(chunk_texts)
    
    # Store in Pinecone
    store_documents(all_chunks, embeddings)
    
    # Example query
    query = "What is Langsmith?"
    query_embedding = get_embeddings([query])[0]
    relevant_docs = similarity_search(query_embedding, k=2)
    
    # Generate answer
    answer = generate_answer(query, relevant_docs)
    os.makedirs('RAG_local/parent_document/output', exist_ok=True)
    with open('RAG_local/parent_document/output/parent_document_answer.txt', 'w') as file:
        file.write(answer)
    print(f"Question: {query}")
    print(f"Answer: {answer}")

if __name__ == "__main__":
    main()
