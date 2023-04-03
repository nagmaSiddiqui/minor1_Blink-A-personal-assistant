import pyttsx3

def Speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    # engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()
    engine.stop()