# Text to speech module
from gtts import gTTS
# Module to play the audio of the text-to-speech
import os

text = "first time i'm using a package in next.py course"

audio = gTTS(text=text, lang='en')

# Saving the converted audio in a mp3
audio.save("targilaudio.mp3")

# Playing the converted file
os.system("start targilaudio.mp3")
