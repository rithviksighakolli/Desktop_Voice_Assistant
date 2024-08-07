import pyttsx3
import speech_recognition
import requests
import datetime
import webbrowser
import random
import pywhatkit
from bs4 import BeautifulSoup
import smtplib

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

query = takeCommand().lower()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices' , voices[0].id)
engine.setProperty('rate' , 170)

#tect to speech converter
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def sendEmail(to, cm):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login('rithviksighakolli@gmail.com', 'Chotta10g')
    server.sendmail('rithviksighakolli@gmail.com', to, cm)
    server.close()

