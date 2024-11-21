import os
import requests
import time

def sarvam_ai_speech_to_text(audio_path):
    api_key= os.environ.get("SARVAM_AI_API_KEY")
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
    return response.text


if __name__ == "__main__":
    audio_file_path="/Users/adityam/Downloads/hindiAudiosTest/hi/1719_hi.wav"
    print("enter 1 for sarvam ai and 2 for openai")
    choice=int(input())
    if choice==1:
        print(sarvam_ai_speech_to_text(audio_file_path))
    elif choice==2:
        print(openai_speech_to_text(audio_file_path))
    