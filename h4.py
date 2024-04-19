from transformers import pipeline
from PIL import Image    
import requests

# model_id = "HuggingFaceH4/vsft-llava-1.5-7b-hf-trl"
# pipe = pipeline("image-to-text", model=model_id)
# url = "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/tasks/ai2d-demo.jpg"


# image = Image.open(requests.get(url, stream=True).raw)
# prompt = "A chat between a curious user and an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the user's questions. USER: <image>\nWhat does the label 15 represent? (1) lava (2) core (3) tunnel (4) ash cloud\nASSISTANT:"

# outputs = pipe(image, prompt=prompt, generate_kwargs={"max_new_tokens": 200})
# print(outputs)

#>>> {"generated_text": "\nUSER: What does the label 15 represent? (1) lava (2) core (3) tunnel (4) ash cloud\nASSISTANT: Lava"}