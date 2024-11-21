import requests
import os
import time

def chat_with_gpt(prompt, system_message="You are a helpful assistant."):
    api_key= os.environ.get("OPENAI_API_KEY")
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    
    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": prompt}
    ]
    
    payload = {
        "model": "gpt-4",
        "messages": messages
    }
    start_time = time.time()
    response = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers=headers,
        json=payload
    )
    end_time = time.time()
    print(f"Time taken: {end_time - start_time} seconds")   
    response.raise_for_status()
    
    return response.json()["choices"][0]["message"]["content"]

def chat_with_groq(prompt):
    api_key= os.environ.get("GROQ_API_KEY")
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "llama3-8b-8192",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }
    start_time = time.time()
    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers=headers,
        json=payload
    )
    end_time = time.time()
    print(f"Time taken: {end_time - start_time} seconds")
    response.raise_for_status()
    
    return response.json()["choices"][0]["message"]["content"]

# Usage example
if __name__ == "__main__":
    prompt = "Write a haiku about recursion in programming."
    print("enter 1 for openai, 2 for groq")
    choice=int(input())
    if choice==1:
        response = chat_with_gpt(prompt)
    elif choice==2:
        response = chat_with_groq(prompt)
    print("Response:", response)