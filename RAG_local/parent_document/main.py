from data.wine_data import docs
from db.document_store import upload_documents
from retriever.self_query import get_retriever

if __name__ == "__main__":
    # Upload documents to Pinecone
    upload_documents(docs)

    # Initialize retriever
    retriever = get_retriever()

    # Example queries
    query1 = "What are some red wines"
    results1 = retriever.get_relevant_documents(query1)
    print(f"Results for query: {query1}")
    for result in results1:
        print(result)

    query2 = "What are two wines with a rating above 97"
    results2 = retriever.get_relevant_documents(query2)
    print(f"\nResults for query: {query2}")
    for result in results2:
        print(result)
