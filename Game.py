import googletrans
from googletrans import Translator
from gtts import gTTS
import googletrans
import pyttsx3
import speech_recognition
import os
import random

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

def game_play():
    speak("Let's play")
    i = 0
    Me_score = 0
    Com_score = 0

    while(i<5):
        choose = ("rock", "paper", "scissor")
        com_choose = random.choice(choose)
        query = takeCommand().lower()
        if (query == "rock"):
            if (com_choose == "rock"):
                speak("ROCK")
                speak(f"Score's are, Rithvik {Me_score}, Jarvis {Com_score}")
            elif (com_choose == "paper"):
                speak("PAPER")
                Com_score +=1
                speak(f"Score's are, Rithvik {Me_score}, Jarvis {Com_score}")
            else:
                speak("SCISSORS")
                Me_score +=1
                speak(f"Score's are, Rithvik {Me_score}, Jarvis {Com_score}")
        elif (query == "paper"):
            if (com_choose == "rock"):
                speak("ROCK")
                Me_score +=1
                speak(f"Score's are, Rithvik {Me_score}, Jarvis {Com_score}")
            elif (com_choose == "paper"):
                speak("PAPER")
                speak(f"Score's are, Rithvik {Me_score}, Jarvis {Com_score}")
            else:
                speak("SCISSORS")
                Com_score +=1
                speak(f"Score's are, Rithvik {Me_score}, Jarvis {Com_score}")
        elif (query == "scissors" or query == "scissor"):
            if (com_choose == "rock"):
                speak("ROCK")
                Com_score +=1
                speak(f"Score's are, Rithvik {Me_score}, Jarvis {Com_score}")
            elif (com_choose == "paper"):
                speak("PAPER")
                Me_score +=1
                speak(f"Score's are, Rithvik {Me_score}, Jarvis {Com_score}")
            else:
                speak("SCISSORS")
                speak(f"Score's are, Rithvik {Me_score}, Jarvis {Com_score}")
        i +=1
    speak(f"The final scores are , RIthvik {Me_score}, Jarvis {Com_score}")