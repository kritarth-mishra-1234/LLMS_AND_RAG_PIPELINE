import os
from groq import Groq
GROQ_API_KEY=os.environ.get("GROQ_API_KEY")
client=Groq(api_key=GROQ_API_KEY)

chat=client.chat.completions.create(
    messages=[
        {
        "role":"system",
        "content":"you are a nice LLM",
        },
        {
        "role":"user",
        "content":"explain the importance of LLMs?",
        }
    ],
    model="llama3-8b-8192",
)
print(chat.choices[0].message.content)
