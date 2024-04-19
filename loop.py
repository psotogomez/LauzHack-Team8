
from img2textgpt import image_to_text
# 1. I need a Image an a fixed first promp

image_path = "classroom.jpg"

prompt = """
Image Description: Describe the image to the AI, providing enough context for understanding. Be descriptive and clear in your explanation.

Questions:
1. What is in the image?
2. Can you describe the colors of the objects?
3. Are there any people in the image? If so, what are they doing?
4. Is there anything notable about the background?
5. Can you identify any text in the image?
6. Are there any animals present? If yes, what type?

Response in with few sentences
"""

output = image_to_text(image_path, prompt)
print("-----Prompt----")
print(prompt)
print("-----Answer----")
print(output)

counter = 0
context = output
while True:
    counter += 1 
    #2. Make a new question
    user_input = input('\n Make a new question....\n User:')
    if user_input == "Z":
        break
    #3. Add to previuos conversarsation
    prompt = f'Context: {context} \n Next Question: {user_input} \n Just answer the Next Question taking into consideration the context provided'
    context = context + f'\n {counter}. {user_input}'
    #4. Ask to the model with the full new context
    output = image_to_text(image_path, prompt)
    print("-----Prompt----")
    print(prompt)
    print("-----Answer----")
    print(output)


    
    



