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
    # Add output saving
    output_path = Path(os.getcwd()) / "outputs" / "gpt4o_response.txt"
    output_path.parent.mkdir(exist_ok=True)
    with open(output_path, "w") as f:
        f.write(chat.choices[0].message.content)
    print(f"Output saved to {output_path}")

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
    # Add output saving
    output_path = Path(os.getcwd()) / "outputs" / "llama3_response.txt"
    output_path.parent.mkdir(exist_ok=True)
    with open(output_path, "w") as f:
        f.write(chat.choices[0].message.content)
    print(f"Output saved to {output_path}")
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
    # Add output saving
    output_path = Path(os.getcwd()) / "outputs" / "claude3_response.txt"
    output_path.parent.mkdir(exist_ok=True)
    with open(output_path, "w") as f:
        f.write(str(message.content))
    print(f"Output saved to {output_path}")
    print(message.content)

#text to speech files


def openai_tts():
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

    speech_file_path = Path(os.getcwd()).parent / "speechopenai.mp3"
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

    audio_file= open("/Users/mohitmishra/Desktop/Yardstick_AI_work/llmapis/openai_client.mp3", "rb")
    transcription = client.audio.transcriptions.create(
        model="whisper-1", 
        file=audio_file
    )
    # Add output saving
    output_path = Path(os.getcwd()) / "outputs" / "openai_stt_response.txt"
    output_path.parent.mkdir(exist_ok=True)
    with open(output_path, "w") as f:
        f.write(transcription.text)
    print(f"Output saved to {output_path}")
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
    # Save the image URL to a text file
    output_path = Path(os.getcwd()) / "outputs" / "dalle3_image_url.txt"
    output_path.parent.mkdir(exist_ok=True)
    with open(output_path, "w") as f:
        f.write(response.data[0].url)
    print(f"Image URL saved to {output_path}")
    image_url = response.data[0].url   

if __name__ == "__main__":
    # openai_LLM()
    # groq_LLM()
    # #claude_LLM()
    # openai_tts()
    # openai_tts_streaming()
    openai_stt()
    openai_text_to_image()
