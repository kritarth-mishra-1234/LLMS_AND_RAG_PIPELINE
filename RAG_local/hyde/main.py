import config
from embeddings import get_embeddings
from vector_store import init_pinecone, upsert_to_pinecone, query_pinecone
from llm import generate_completions

def process_query(query: str, n_hypotheticals: int = 4) -> List[Dict[str, Any]]:
    """
    Process a query using hypothetical document embeddings.
    
    Args:
        query: Input query
        n_hypotheticals: Number of hypothetical documents to generate
        
    Returns:
        List of similar results
    """
    # Initialize Pinecone
    index = init_pinecone()
    
    # Generate hypothetical documents
    prompt = f"Please answer the following question as a single food item\nQuestion: {query}\nAnswer:"
    hypothetical_docs = generate_completions(prompt, n=n_hypotheticals)
    
    # Get embeddings
    hypothetical_embeddings = get_embeddings(hypothetical_docs)
    
    # Store in Pinecone
    upsert_to_pinecone(index, hypothetical_docs, hypothetical_embeddings)
    
    # Get query embedding and find similar items
    query_embedding = get_embeddings([query])[0]
    similar_results = query_pinecone(index, query_embedding)
    
    return similar_results

def main():
    # Example usage
    query = "What is McDonald's best selling item?"
    results = process_query(query)
    
    print("\nQuery:", query)
    print("\nSimilar results:")
    for i, result in enumerate(results, 1):
        print(f"\n{i}. Score: {result['score']:.3f}")
        print(f"   Text: {result['text']}")

if __name__ == "__main__":
    main()