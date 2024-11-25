import openai
from src import document_utils, vector_store
from config import OPENAI_API_KEY

def process_query(query: str, index, k: int = 4) -> str:
    '''Process a query and return the answer'''
    # Get relevant documents
    relevant_docs = vector_store.similarity_search(index, query, k)
    
    # Prepare context from relevant documents
    context = "\n".join([doc["content"] for doc in relevant_docs])
    
    # Generate response using OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system", 
                "content": "You are a helpful assistant. Use the provided context to answer the question."
            },
            {
                "role": "user", 
                "content": f"Context: {context}\n\nQuestion: {query}"
            }
        ]
    )
    
    return response.choices[0].message.content

def main():
    # Initialize OpenAI
    openai.api_key = OPENAI_API_KEY

    # Load documents
    docs = document_utils.load_directory("blog_posts")

    # Split documents into chunks
    parent_docs = document_utils.split_documents(docs, chunk_size=2000)
    child_docs = document_utils.split_documents(parent_docs, chunk_size=400)

    # Initialize Pinecone
    index = vector_store.init_pinecone()

    # Add documents to index
    vector_store.add_documents(index, child_docs)

    # Example query
    query = "What is Langsmith?"
    answer = process_query(query, index)
    print(f"Q: {query}")
    print(f"A: {answer}")

if __name__ == "__main__":
    main()