import requests
from keys import TEXT2SPEECH

API_URL = "https://api-inference.huggingface.co/models/facebook/mms-tts-eng"
headers = {"Authorization": f"Bearer {TEXT2SPEECH}"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content

def text_to_speech(text: str, save: bool, save_path: str ='./', file_name: str ='audio.mp3') -> bytes:
    audio_bytes = query({
        "inputs": text,
    })
    if save:
        with open(save_path+file_name, "wb") as f:
            f.write(audio_bytes)
    return audio_bytes


if __name__ == "__main__":
    text = "Hello, my name is John Doe. I am a software engineer."

    audio_bytes = text_to_speech(text, save=True, save_path='./', file_name='output.mp3')
