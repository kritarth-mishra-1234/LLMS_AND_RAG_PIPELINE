import openai
from openai import OpenAI
import os

OPEN_AI_API=os.environ.get("OPENAI_API_KEY")
client=OpenAI(api_key=OPEN_AI_API)

chat=client.chat.completions.create(
    messages=[
            {
             "role":"system",
             "content":"Act as a less talkative model",
            },
            {
             "role":"user",
             "content":"explain how much do you like to talk about science?",
            }
    ],
    model="gpt-4o"
)
print(chat.choices[0].message.content)
