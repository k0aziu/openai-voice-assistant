import os
import subprocess
from modules.gpt.gpt import gpt_query
from modules.speechRecognition.speechRecognition import speech_recognize
from variables import Variables

def record_audio():
    audio_file = 'output.wav'
    subprocess.run(['termux-microphone-record', '-f', audio_file, '-l', '5', '-q'])
    return audio_file

while True:
    audio_file = record_audio()
    text = speech_recognize(audio_file)
    print(text)
    if text:
        response = gpt_query(text, Variables.OPENAI_API_KEY)
        print(response)
