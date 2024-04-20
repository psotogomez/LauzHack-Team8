# GuideBot

## Installation

```bash
# 1) create and activate virtual environment with conda
conda create -n apis_env python=3.11
conda activate apis_env

# 2) install dependencies (apis_env) and create a bot with Bot Father
pip install -r requirements.txt
```

rename keys.txt -> keys.py and complete the following API Keys

On the TELEGRAM_KEY include the one provided by Bot Father

```
TELEGRAM_KEY = ""
HUGGING_FACE_KEY = ""
OPENAI = ""
```


Launching project!

Still in conda env

```bash
 python demo.py
```
## How to use the bot?

1) you have to send a picture to the Telegram bot and he will firstly describe the image. 
2) After you have received the response from the bot, you can ask any question related to the image in audio format.
3) You can send any other picture to start a new conversation

