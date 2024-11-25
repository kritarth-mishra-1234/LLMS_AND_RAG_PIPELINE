import openai
from openai import OpenAI
import os
import anthropic
from anthropic import Anthropic
from groq import Groq
from pathlib import Path
from openai import OpenAI

def openai_LLM():
    OPEN_AI_API = os.environ.get("OPENAI_API_KEY")
    client = OpenAI(api_key=OPEN_AI_API)  # Fixed indentation

    chat = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "Act as a less talkative model",
            },
            {
                "role": "user",
                "content": "explain how much do you like to talk about science?",
            }
        ],
        model="gpt-4o"
    )
    print(chat.choices[0].message.content)

def groq_LLM():
    
    from groq import Groq
    GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
    client = Groq(api_key=GROQ_API_KEY)

    chat = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "you are a nice LLM",
            },
            {
                "role": "user",
                "content": "explain the importance of LLMs?",
            }
        ],
        model="llama3-8b-8192"
    )
    print(chat.choices[0].message.content)

def claude_LLM():
    anthropic_api = os.environ.get("ANTHROPIC_API_KEY")
    client = Anthropic(api_key=anthropic_api)
    message = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1000,
        temperature=0,
        system="You are a world-class poet. Respond only with short poems.",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Why is the ocean salty?"
                    }
                ]
            },
        ],
    )
    print(message.content)

#text to speech files


def openai_tts():
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

    speech_file_path = Path(os.getcwd()).parent / "speech.mp3"
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input="Today is a wonderful day to build something people love!"
    )

    response.stream_to_file(speech_file_path)

def openai_tts_streaming():
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    response = client.audio.speech.create(
            model="tts-1",
            voice="alloy",
            input="Hello world! This is a streaming test.",
        )

    response.stream_to_file("output.mp3")

#speech to text files
def openai_stt():
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

    audio_file= open("/Users/mohitmishra/Desktop/Yardstick_AI_work/llmapis/speech.mp3", "rb")
    transcription = client.audio.transcriptions.create(
        model="whisper-1", 
        file=audio_file
    )
    print(transcription.text)

#text_to_image

def openai_text_to_image():
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

    response = client.images.generate(
        model="dall-e-3",
        prompt="a white siamese cat",
        size="1024x1024",
        quality="standard",
        n=1,
    )
    image_url = response.data[0].url   

if __name__ == "__main__":
    openai_LLM()
    groq_LLM()
    claude_LLM()
    openai_tts()
    openai_tts_streaming()