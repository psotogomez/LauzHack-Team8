import requests
from keys import SPEECH2TEXT

API_URL = "https://api-inference.huggingface.co/models/openai/whisper-large-v3"
headers = {"Authorization": f"Bearer {SPEECH2TEXT}"}

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()

def speech2text(filename: str) -> dict:
    return query(filename)['text']

if __name__ == "__main__":
    output = speech2text("output.mp3")
    print(output)

    
