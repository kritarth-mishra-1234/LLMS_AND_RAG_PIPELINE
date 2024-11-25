import os
import requests
import time
from pathlib import Path
def sarvam_ai_speech_to_text(audio_path):
    api_key= os.environ.get("SARVAM_API_KEY")
    url = "https://api.sarvam.ai/speech-to-text-translate"

    payload = {'model': 'saaras:v1',
    'prompt': ''}
    files=[
    ('file',(audio_path,open(audio_path,'rb'),'audio/wav'))
    ]
    headers = {
    'api-subscription-key': api_key
    }
    start_time = time.time()
    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    end_time = time.time()
    print(f"Time taken: {end_time - start_time} seconds")
    output_path = Path(os.getcwd()) / "outputs_speech_to_text" / "sarvam_ai_response.txt"
    output_path.parent.mkdir(exist_ok=True)
    with open(output_path, "w") as f:
        f.write(response.text)
    print(f"Output saved to {output_path}")
    return response.text


def openai_speech_to_text(audio_path):
    api_key= os.environ.get("OPENAI_API_KEY")
    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    
    # Prepare the files and data
    files = {
        "file": open(audio_path, "rb")
    }
    
    data = {
        "model": "whisper-1",
        "response_format": "text"
    }
    start_time = time.time()
    response = requests.post(
        "https://api.openai.com/v1/audio/transcriptions",
        headers=headers,
        files=files,
        data=data
    )
    end_time = time.time()
    print(f"Time taken: {end_time - start_time} seconds")
    response.raise_for_status()
    output_path = Path(os.getcwd()) / "outputs_speech_to_text" / "openai_response.txt"
    output_path.parent.mkdir(exist_ok=True)
    with open(output_path, "w") as f:
        f.write(response.text)
    print(f"Output saved to {output_path}")
    return response.text


if __name__ == "__main__":
    audio_file_path="/Users/mohitmishra/Desktop/Yardstick_AI_work/llmapis/speechopenai.mp3"
    print("enter 1 for sarvam ai and 2 for openai")
    choice=int(input())
    if choice==1:
        print(sarvam_ai_speech_to_text(audio_file_path))
    elif choice==2:
        print(openai_speech_to_text(audio_file_path))
    