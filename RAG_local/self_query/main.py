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

    # Save output to file
    with open("selfqueryoutput.txt", "w", encoding="utf-8") as f:
        f.write(f"Q: {query1}\n")
        for result in results1:
            f.write(f"A: {result}\n")

    query2 = "What are two wines with a rating above 97"
    results2 = retriever.get_relevant_documents(query2)
    print(f"\nResults for query: {query2}")
    # Save output to file
    with open("selfqueryoutput.txt", "a", encoding="utf-8") as f:
        f.write(f"\nQ: {query2}\n")
        for result in results2:
            f.write(f"A: {result}\n")