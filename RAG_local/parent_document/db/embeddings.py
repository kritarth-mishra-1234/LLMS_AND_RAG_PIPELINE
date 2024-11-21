# from langchain.embeddings.openai import OpenAIEmbeddings
# import openai
from openai import OpenAI
from config.settings import OPENAI_API_KEY, EMBEDDING_MODEL
client = OpenAI(api_key=OPENAI_API_KEY)

# Initialize OpenAI Embeddings
# embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
# openai.api_key = OPENAI_API_KEY
# def generate_embeddings(text: str):
#     response = openai.Embedding.create(
#         model=EMBEDDING_MODEL,
#         input=text
#     )
#     return response['data'][0]['embedding']

def generate_embeddings(text,model=EMBEDDING_MODEL):
    text = text.replace("\n", " ")
    response = client.embeddings.create(input=[text], model=model)
    return response.data[0].embedding
