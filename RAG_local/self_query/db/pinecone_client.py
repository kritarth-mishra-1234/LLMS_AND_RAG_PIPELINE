# import pinecone
from config.settings import PINECONE_API_KEY
import os
from pinecone import Pinecone, ServerlessSpec

# # Initialize Pinecone client
# pinecone.init(api_key=PINECONE_API_KEY, environment=PINECONE_ENVIRONMENT)

# # Create/Open Pinecone index
# def get_pinecone_index():
#     if PINECONE_INDEX_NAME not in pinecone.list_indexes():
#         pinecone.create_index(PINECONE_INDEX_NAME, dimension=1536)
#     return pinecone.Index(PINECONE_INDEX_NAME)
my_index_name = 'myindex'
pc = Pinecone(api_key=PINECONE_API_KEY)
def get_pinecone_index():
    if my_index_name not in pc.list_indexes().names():
        pc.create_index(
            name=my_index_name, 
            dimension=1536, 
            metric='cosine',
            spec=ServerlessSpec(
                cloud='aws',
                region='us-east-1'
            )
        )
    index = pc.Index(my_index_name)
    # Wait for index to be ready
    index.describe_index_stats()
    return index