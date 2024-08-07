import pyttsx3
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices' , voices[0].id)
engine.setProperty('rate' , 170)

#tect to speech converter
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning Sir")
    elif hour>12 and hour <=18:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir")

    speak("Please tell me How can I help you ?")

