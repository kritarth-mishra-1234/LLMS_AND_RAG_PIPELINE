# src/main.py
from embeddings import openai_embeddings
from retrievers import (
    bm25_retriever,
    pinecone_retriever,
    ensemble_retriever
)

def main():
    # Sample documents
    doc_list = [
        "I like apples",
        "I like oranges",
        "Apples and oranges are fruits",
        "I like computers by Apple",
        "I love fruit juice"
    ]

    # Initialize BM25
    bm25_model = bm25_retriever.initialize_bm25(doc_list)
    
    # Initialize Pinecone and add documents
    pinecone_index = pinecone_retriever.initialize_pinecone()
    doc_embeddings = openai_embeddings.embed_texts(doc_list)
    pinecone_retriever.add_texts_to_pinecone(pinecone_index, doc_list, doc_embeddings)

    # Test retrievers
    query = "A green fruit"
    query_embedding = openai_embeddings.embed_query(query)

    # Get results from both retrievers
    bm25_results = bm25_retriever.get_bm25_documents(bm25_model, doc_list, query, k=2)
    pinecone_results = pinecone_retriever.get_pinecone_documents(pinecone_index, query_embedding, k=2)

    # Combine results using ensemble
    weights = [0.5, 0.5]
    final_results = ensemble_retriever.get_ensemble_documents(
        [bm25_results, pinecone_results],
        weights
    )

    # Print results
    print("Query:", query)
    print("\nResults:")
    for result in final_results:
        print(f"Text: {result['text']}")
        print(f"Score: {result['score']:.4f}\n")

if __name__ == "__main__":
    main()