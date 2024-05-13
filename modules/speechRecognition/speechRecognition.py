import speech_recognition as sr

def speech_recognize():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        print("Proszę mówić...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language='pl-PL')
        print("Rozpoznano: " + text)
        return text
    except sr.UnknownValueError:
        print("Nie udało się rozpoznać mowy.")
        return None
    except sr.RequestError as e:
        print(f"Błąd serwisu; {e}")
        return None
