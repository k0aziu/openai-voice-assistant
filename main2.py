from content import *
from plugin.customCommandsList import *
from modules.gpt.gpt import gpt_query
from modules.speechRecognition.speechRecognition import speech_recognize
from variables import Variables

while True:
    text = speech_recognize()
    print(text)
    if Content(text, GREETINGS).ifContain():
        print(Content(text, GREETINGS).returnContent())
    elif text:
        response = gpt_query(text, Variables.OPENAI_API_KEY)
        print(response)
