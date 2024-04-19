import requests
from keys import IMAGE2TEXT

API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
headers = {"Authorization": f"Bearer {IMAGE2TEXT}"}

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()

def image_to_text(image_path: str) -> dict:
    return query(image_path)

if __name__ == "__main__":
    output = query("example.png")
    print(output)