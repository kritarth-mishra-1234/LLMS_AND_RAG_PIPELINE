from db.pinecone_client import get_pinecone_index
from db.embeddings import generate_embeddings

# def upload_documents(documents_with_metadata):
#     """
#     Upload documents to Pinecone
#     Args:
#         documents_with_metadata: List of tuples containing (text_content, metadata_dict)
#     """
#     index = get_pinecone_index()
#     vectors = [
#         (str(i), generate_embeddings(doc_content), metadata)
#         for i, (doc_content, metadata) in enumerate(documents_with_metadata)
#     ]
#     index.upsert(vectors)

def upload_documents(documents):
    """
    Upload documents to Pinecone
    Args:
        documents: List of Document objects
    """
    index = get_pinecone_index()
    documents_with_metadata = [
        (doc.page_content, doc.metadata) for doc in documents
    ]
    vectors = [
        (str(i), generate_embeddings(doc_content), metadata)
        for i, (doc_content, metadata) in enumerate(documents_with_metadata)
    ]
    index.upsert(vectors)
