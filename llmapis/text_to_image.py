import os
import requests
import time

def generate_image(prompt):
    api_key = os.environ.get("OPENAI_API_KEY")
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    
    payload = {
        "model": "dall-e-3",
        "prompt": prompt,
        "n": 1,
        "size": "1024x1024"
    }

    start_time = time.time()
    response = requests.post(
        "https://api.openai.com/v1/images/generations",
        headers=headers,
        json=payload
    )
    end_time = time.time()
    print(f"Time taken: {end_time - start_time} seconds")
    response.raise_for_status()
    
    # Get image URL from response
    image_url = response.json()["data"][0]["url"]
    
    # Download and save the image
    image_response = requests.get(image_url)
    image_response.raise_for_status()
    
    # Save image with a filename based on the first few words of the prompt
    filename = f"dalle_{prompt[:30].replace(' ', '_')}.png"
    
    with open(filename, 'wb') as f:
        f.write(image_response.content)
    

def stability_ai_image(prompt):
  api_key= os.environ.get("STABILITY_AI_API_KEY")
  start_time = time.time()
  response = requests.post(
    f"https://api.stability.ai/v2beta/stable-image/generate/ultra",
    headers={
        "authorization": f"Bearer {api_key}",
        "accept": "image/*"
    },
    files={"none": ''},
    data={
        "prompt": "Lighthouse on a cliff overlooking the ocean",
        "output_format": "webp",
    },
   )
  end_time = time.time()
  print(f"Time taken: {end_time - start_time} seconds")
  if response.status_code == 200:
        with open("./lighthouse.webp", 'wb') as file:
          file.write(response.content)
  else:
      raise Exception(str(response.json()))

if __name__ == "__main__":
    prompt="a beautiful sunset over the ocean"
    print("enter 1 for openai, 2 for stability ai")
    choice=int(input())
    if choice==1:
        generate_image(prompt)
    elif choice==2:
        stability_ai_image(prompt)
