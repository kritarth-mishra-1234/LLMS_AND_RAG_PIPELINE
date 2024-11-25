import requests
import os
import openai
import time
# from dotenv import load_dotenv

# load_dotenv()

def eleven_labs_text_to_speech(text):
  
  api_key= os.environ.get("ELEVEN_LABS_API_KEY")
#   CHUNK_SIZE = 1024
  url = "https://api.elevenlabs.io/v1/text-to-speech/<voice-id>"
  headers = {
  "Accept": "audio/mpeg",
  "Content-Type": "application/json",
  "xi-api-key": api_key
  }
  payload = {
  "text": text,
  "model_id": "eleven_monolingual_v1",
  "voice_settings": {
    "stability": 0.5,
    "similarity_boost": 0.5
    }
  }
  output_file="speechelevenlabs.mp3"
  start_time = time.time()
  response = requests.request("POST", url, json=payload, headers=headers)
  end_time = time.time()
  print(f"Time taken: {end_time - start_time} seconds")
  with open(output_file, 'wb') as f:
      for chunk in response.iter_content(chunk_size=8192):
          if chunk:
                f.write(chunk)

  return output_file
def sarvam_ai_text_to_speech(text):

  url = "https://api.sarvam.ai/text-to-speech"
  api_key= os.environ.get("SARVAM_API_KEY")
  headers = {
    "Content-Type": "application/json",
    "API-Subscription-Key": api_key
    }
  payload = {
  "inputs": text,
  "target_language_code": "hi-IN",
  "speaker": "meera",
  "speech_sample_rate": 8000,
  "enable_preprocessing": True,
  "model": "bulbul:v1"
  }
  output_file="speechsarvam.mp3"
  start_time = time.time()
  response = requests.request("POST", url, json=payload, headers=headers)
  end_time = time.time()
  print(f"Time taken: {end_time - start_time} seconds")

  with open(output_file, 'wb') as f:
      for chunk in response.iter_content(chunk_size=8192):
          if chunk:
                f.write(chunk)
    
  return output_file
  



def text_to_speech(text):
    
    api_key= os.environ.get("OPENAI_API_KEY")
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "input": text,
        "model": "tts-1",
        "voice": "alloy"
    }
    output_file="speechopenai.mp3"
    start_time = time.time()
    response = requests.post(
        "https://api.openai.com/v1/audio/speech",
        headers=headers,
        json=payload,
        stream=True
    )
    end_time = time.time()
    print(f"Time taken: {end_time - start_time} seconds")
    response.raise_for_status()
    
    with open(output_file, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)
    
    return output_file

if __name__ == "__main__":
    text="how are you"
    print("enter 1 for openai, 2 for eleven labs, 3 for sarvam ai")
    choice=int(input())
    if choice==1:
        text_to_speech(text)
    elif choice==2:
        eleven_labs_text_to_speech(text)
    elif choice==3:
        sarvam_ai_text_to_speech(text)