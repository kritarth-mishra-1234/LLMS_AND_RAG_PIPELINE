import os
from embeddings import embed_documents, embed_query
from document_processor import process_documents
from vector_store import get_pinecone_index, add_documents, similarity_search

def pretty_print_docs(docs):
    """Helper function to print documents nicely."""
    print(f"\n{'-' * 100}\n".join(
        [f"Document {i+1}:\n\n" + doc[0] for i, doc in enumerate(docs)]
    ))

def main():
    # Process documents
    blog_posts_dir = "langchain_blog_posts"
    file_paths = [
        os.path.join(blog_posts_dir, "blog.langchain.dev_announcing-langsmith_.txt"),
        os.path.join(blog_posts_dir, "blog.langchain.dev_benchmarking-question-answering-over-csv-data_.txt")
    ]
    
    print("Processing documents...")
    processed_docs = process_documents(file_paths)
    
    # Generate embeddings for documents
    print("Generating embeddings...")
    doc_embeddings = embed_documents([doc[0] for doc in processed_docs])
    
    # Initialize Pinecone and get index
    print("Initializing Pinecone vector store...")
    index = get_pinecone_index()
    
    # Add documents to vector store
    print("Adding documents to vector store...")
    add_documents(index, processed_docs, doc_embeddings)
    
    # Perform similarity search
    query = "What is LangSmith?"
    print(f"\nExecuting query: {query}")
    
    # Generate query embedding and search
    query_embedding = embed_query(query)
    relevant_docs = similarity_search(index, query_embedding)
    
    # Print results
    print("\nRelevant documents found:")
    pretty_print_docs(relevant_docs)

if __name__ == "__main__":
    main()