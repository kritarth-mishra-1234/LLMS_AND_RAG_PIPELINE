# from langchain.llms import OpenAI
# from langchain.retrievers.self_query.base import SelfQueryRetriever
# from retriever.metadata import metadata_field_info
# from db.pinecone_client import get_pinecone_index

# document_content_description = "Brief description of the wine"

# def get_retriever():
#     llm = OpenAI(temperature=0)
#     index = get_pinecone_index()
#     retriever = SelfQueryRetriever.from_llm(
#         llm=llm,
#         vectorstore=index,
#         document_content_description=document_content_description,
#         metadata_field_info=metadata_field_info,
#         verbose=True,
#     )
#     return retriever
from typing import Dict, Any
from openai import OpenAI
from config.settings import OPENAI_API_KEY
from retriever.metadata import metadata_field_info
from db.pinecone_client import get_pinecone_index
import json
from db.embeddings import generate_embeddings

document_content_description = "Brief description of the wine"

class CustomSelfQueryRetriever:
    def __init__(self, llm, vectorstore, metadata_field_info, document_content_description, verbose=False):
        self.llm = llm
        self.vectorstore = vectorstore
        self.metadata_field_info = metadata_field_info
        self.document_content_description = document_content_description
        self.verbose = verbose

    def get_relevant_documents(self, query: str):
        # Create a system prompt for structured query extraction
        system_prompt = f"""Given a natural language query, extract the semantic query and metadata filters.
        The document content contains: {self.document_content_description}
        The metadata fields are: {self.metadata_field_info}
        Format the output as JSON with 'query' and 'filters' keys."""

        response = self.llm.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": query}
            ],
            response_format={ "type": "json_object" }
        )
        
        structured_query = response.choices[0].message.content
        
        # return self.vectorstore.similarity_search(
        #     structured_query["query"],
        #     filter=structured_query.get("filters", {})
        # )
        # the above is the original code, below is the modified code to use the similarity_search
        # because the original code was not working
            
        # Parse the JSON string into a Python dictionary
        structured_query = json.loads(response.choices[0].message.content)
        return self.similarity_search(
            structured_query["query"],
            filter=structured_query.get("filters", {})
        )
    def similarity_search(self, query: str, filter: Dict[str, Any] = None, k: int = 4):
        """
        Perform similarity search on the vectorstore with optional metadata filtering.
        
        Args:
            query (str): The query text to search for
            filter (Dict[str, Any], optional): Metadata filters to apply
            k (int): Number of results to return (default: 4)
        """
        # Get embeddings for the query
        query_embedding = generate_embeddings(query)
        
        # Perform the search in Pinecone
        results = self.vectorstore.query(
            vector=query_embedding,
            filter=filter,
            top_k=k,
            include_metadata=True
        )
        
        # Convert Pinecone results to documents
        documents = []
        for result in results.matches:
            documents.append({
                'content': result.metadata.get('text', ''),
                'metadata': {k:v for k,v in result.metadata.items() if k != 'text'}
            })
            
        return documents
def get_retriever():
    client = OpenAI(api_key=OPENAI_API_KEY)
    index = get_pinecone_index()
    retriever = CustomSelfQueryRetriever(
        llm=client,
        vectorstore=index,
        document_content_description=document_content_description,
        metadata_field_info=metadata_field_info,
        verbose=True,
    )
    return retriever