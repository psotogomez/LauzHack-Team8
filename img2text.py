import base64
import requests
from keys import OPENAI

# OpenAI API Key
api_key = OPENAI

# Function to encode the image
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def img2text(image_path: str, prompt: str) -> dict:
    # Getting the base64 string
    base64_image = encode_image(image_path)

    headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
    }
    payload = {
    "model": "gpt-4-turbo",
    "messages": [
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": prompt
            },
            {
            "type": "image_url",
            "image_url": {
                "url": f"data:image/jpeg;base64,{base64_image}"
            }
            }
        ]
        }
    ],
    "max_tokens": 100
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    return response.json()['choices'][0]['message']['content']


if __name__ == "__main__":
    # Path to your image
    image_path = "example.png"
    prompt = "What’s in this image? The description is to guide a blind person to understand where the objects are in the image and gain insight about the image."
    output = img2text(image_path, prompt)
    print(output)