import openai
from typing import List, Dict
from config import OPENAI_API_KEY
from openai import OpenAI

client =OpenAI(api_key=OPENAI_API_KEY)

def generate_answer(query: str, context: List[Dict]) -> str:
    """Generate answer using OpenAI API."""
    context_text = "\n".join([doc['text'] for doc in context])
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that answers questions based on the provided context."},
                {"role": "user", "content": f"Context:\n{context_text}\n\nQuestion: {query}"}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error generating answer: {str(e)}")
        return "Sorry, I couldn't generate an answer at this time."