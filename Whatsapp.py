import pywhatkit
import pyttsx3
import datetime
import speech_recognition
import webbrowser
from bs4 import BeautifulSoup
from time import sleep
import os
from datetime import timedelta
from datetime import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices' , voices[0].id)
engine.setProperty('rate' , 170)

#tect to speech converter
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#voice recognition
def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Understanding...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"You said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query
strTime = int(datetime.now().strftime("%H"))
update = int((datetime.now()+timedelta(minutes = 2)).strftime("%M"))

def sendMessage():
    speak("Who do you want to message")
    tk = takeCommand().lower()
    
    if "mom" in tk:
        speak("what message should i message sir")
        message = takeCommand().lower()
        pywhatkit.sendwhatmsg("+919440638992", message, time_hour = strTime, time_min = update)
    elif "daddy" in tk:
        speak("what message should i message sir")
        message = takeCommand().lower()
        pywhatkit.sendwhatmsg("+919515486684", message, time_hour = strTime, time_min = update)
    elif "grandma" in tk:
        speak("what message should i message sir")
        message = takeCommand().lower()
        pywhatkit.sendwhatmsg("+919394838253", message, time_hour = strTime, time_min = update)
    elif "grandpa" in tk:
        speak("what message should i message sir")
        message = takeCommand().lower()
        pywhatkit.sendwhatmsg("+919397925363", message, time_hour = strTime, time_min = update)
    elif "kushal" in tk:
        speak("what message should i message sir")
        message = takeCommand().lower()
        pywhatkit.sendwhatmsg("+917569170680", message, time_hour = strTime, time_min = update)
    elif "myself" in tk:
        speak("what message should i message sir")
        message = takeCommand().lower()
        pywhatkit.sendwhatmsg("+918919034243", message, time_hour = strTime, time_min = update)


