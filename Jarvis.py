import pyttsx3
from sklearn.model_selection import train_test_split
import speech_recognition
import requests
from requests import get
import datetime
import webbrowser
import random
import pywhatkit
import os
import sys
from bs4 import BeautifulSoup
import smtplib
import pyjokes
import time
import cv2
import pyautogui
from plyer import notification
from pygame import mixer
import math
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
import nltk
import warnings
warnings.simplefilter('ignore')

#hello world


from Clap import MainClapExe
MainClapExe

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

def news():
    main_url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=ee05e992db7341ffa80706950f14f490"
    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head = []
    day = ["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        speak(f"today's {day[i]} news is : {head[i]}")

def get_age(birthday):
    today = datetime.datetime.today()
    age = today.year - birthday.year - (today.month - birthday.month < 0)
    return age

for i in range(3):
    a = input("Enter password to open Jarvis :- ")
    pw_file = open("Password.txt","r")
    pw = pw_file.read()
    pw_file.close()
    if a == pw:
        print("Welcome sir ! Please Speak to load me up")
        break
    elif (i == 2 and a != pw):
        exit()
    elif a!=pw:
        print("Try again")

from Intro import play_gif
play_gif

intents = {
    "greetings": {
        "patterns": ["hello", "hi", "hey", "howdy", "greetings", "good morning", "good afternoon", "good evening", "hi there", "hey there", "what's up", "hello there"],
        "responses": ["Hello! How can I assist you?", "Hi there!", "Hey! What can I do for you?", "Howdy! What brings you here?", "Greetings! How may I help you?", "Good morning! How can I be of service?", "Good afternoon! What do you need assistance with?", "Good evening! How may I assist you?", "Hey there! How can I help?", "Hi! What's on your mind?", "Hello there! How can I assist you today?"]
    },
    "goodbye": {
        "patterns": ["bye", "see you later", "goodbye", "farewell", "take care", "until next time", "bye bye", "catch you later", "have a good one", "so long"],
        "responses": ["Goodbye!", "See you later!", "Have a great day!", "Farewell! Take care.", "Goodbye! Until next time.", "Take care! Have a wonderful day.", "Bye bye!", "Catch you later!", "Have a good one!", "So long!"]
    },
    "gratitude": {
        "patterns": ["thank you", "thanks", "appreciate it", "thank you so much", "thanks a lot", "much appreciated"],
        "responses": ["You're welcome!", "Happy to help!", "Glad I could assist.", "Anytime!", "You're welcome! Have a great day.", "No problem!"]
    },
    "apologies": {
        "patterns": ["sorry", "my apologies", "apologize", "I'm sorry"],
        "responses": ["No problem at all.", "It's alright.", "No need to apologize.", "That's okay.", "Don't worry about it.", "Apology accepted."]
    },
    "positive_feedback": {
        "patterns": ["great job", "well done", "awesome", "fantastic", "amazing work", "excellent"],
        "responses": ["Thank you! I appreciate your feedback.", "Glad to hear that!", "Thank you for the compliment!", "I'm glad I could meet your expectations.", "Your words motivate me!", "Thank you for your kind words."]
    },
    "negative_feedback": {
        "patterns": ["not good", "disappointed", "unsatisfied", "poor service", "needs improvement", "could be better"],
        "responses": ["I'm sorry to hear that. Can you please provide more details so I can assist you better?", "I apologize for the inconvenience. Let me help resolve the issue.", "I'm sorry you're not satisfied. Please let me know how I can improve.", "Your feedback is valuable. I'll work on improving."]
    },
    "help": {
        "patterns": ["help", "can you help me?", "I need assistance", "support"],
        "responses": ["Sure, I'll do my best to assist you.", "Of course, I'm here to help!", "How can I assist you?", "I'll help you with your query."]
    },
    "music": {
        "patterns": ["play music", "music please", "song recommendation", "music suggestion"],
        "responses": ["Sure, playing some music for you!", "Here's a song you might like: [song_name]", "How about some music?"]
    },
    "food": {
        "patterns": ["recommend a restaurant", "food places nearby", "what's good to eat?", "restaurant suggestion"],
        "responses": ["Sure, here are some recommended restaurants: [restaurant_names]", "Hungry? Let me find some good food places for you!", "I can suggest some great places to eat nearby."]
    },
    "movies": {
        "patterns": ["movie suggestions", "recommend a movie", "what should I watch?", "best movies"],
        "responses": ["How about watching [movie_name]?", "Here's a movie suggestion for you.", "Let me recommend some great movies!"]
    },
    "sports": {
        "patterns": ["sports news", "score updates", "latest sports events", "upcoming games"],
        "responses": ["I'll get you the latest sports updates.", "Stay updated with the current sports events!", "Let me check the sports scores for you."]
    },
    "gaming": {
        "patterns": ["video game recommendations", "best games to play", "recommend a game", "gaming suggestions"],
        "responses": ["How about trying out [game_name]?", "Here are some gaming suggestions for you!", "Let me recommend some fun games to play!"]
    },
        "tech_support": {
        "patterns": ["technical help", "computer issues", "troubleshooting", "IT support"],
        "responses": ["I can assist with technical issues. What problem are you facing?", "Let's troubleshoot your technical problem together.", "Tell me about the technical issue you're experiencing."]
    },
    "book_recommendation": {
        "patterns": ["recommend a book", "good books to read", "book suggestions", "what should I read?"],
        "responses": ["How about reading [book_title]?", "I've got some great book recommendations for you!", "Let me suggest some interesting books for you to read."]
    },
    "fitness_tips": {
        "patterns": ["fitness advice", "workout tips", "exercise suggestions", "healthy habits"],
        "responses": ["Staying fit is important! Here are some fitness tips: [fitness_tips]", "I can help you with workout suggestions and fitness advice.", "Let me provide some exercise recommendations for you."]
    },
    "travel_recommendation": {
        "patterns": ["travel suggestions", "places to visit", "recommend a destination", "travel ideas"],
        "responses": ["Looking for travel recommendations? Here are some great destinations: [travel_destinations]", "I can suggest some amazing places for your next travel adventure!", "Let me help you with travel destination ideas."]
    },
    "education": {
        "patterns": ["learning resources", "study tips", "education advice", "academic help"],
        "responses": ["I can assist with educational queries. What subject are you studying?", "Let's explore learning resources together.", "Tell me about your educational goals or questions."]
    },
    "pet_advice": {
        "patterns": ["pet care tips", "animal advice", "pet health", "taking care of pets"],
        "responses": ["Pets are wonderful! Here are some pet care tips: [pet_care_tips]", "I can provide advice on pet health and care.", "Let's talk about your pet and their well-being."]
    },
    "shopping": {
        "patterns": ["online shopping", "buying something", "shopping advice", "product recommendations"],
        "responses": ["I can help you with online shopping. What are you looking to buy?", "Let's find the perfect item for you!", "Tell me what you're interested in purchasing."]
    },
    "career_advice": {
        "patterns": ["job search help", "career guidance", "career change advice", "professional development"],
        "responses": ["I can provide career advice. What specific guidance do you need?", "Let's explore career opportunities together.", "Tell me about your career goals or concerns."]
    },
    "relationship_advice": {
        "patterns": ["relationship help", "love advice", "dating tips", "relationship problems"],
        "responses": ["Relationships can be complex. How can I assist you?", "I can offer advice on relationships and dating.", "Tell me about your relationship situation."]
    },
    "mental_health": {
        "patterns": ["mental health support", "coping strategies", "stress relief tips", "emotional well-being"],
        "responses": ["Mental health is important. How can I support you?", "I can provide guidance for managing stress and emotions.", "Let's talk about strategies for maintaining mental well-being."]
    },
    "language_learning": {
        "patterns": ["language learning tips", "language practice", "learning new languages", "language study advice"],
        "responses": ["Learning a new language can be exciting! How can I assist you?", "I can help with language learning tips and practice.", "Tell me which language you're interested in learning."]
    },
    "finance_advice": {
        "patterns": ["financial planning help", "money management tips", "investment advice", "budgeting assistance"],
        "responses": ["I can provide guidance on financial matters. What specific advice do you need?", "Let's discuss your financial goals and plans.", "Tell me about your financial situation or goals."]
    },
}

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        query = query.lower()
        if "wake up" in query:
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if "go to sleep" in query or "see you later" in query or "catch you later" in query or "bye" in query or "good bye" in query or "goodbye" in query:
                    speak("Ok sir You can wake me up anytime")
                    break
                elif "hello" in query or "hi" in query or "hey" in query or "greetings" in query or "hi there" in query or "hey there" in query or "what's up" in query or "hello there" in query:
                    speak("Hello sir how can i help you sir ?")
                elif "introduce yourself" in query or "introduce your self" in query:
                    speak("Hello sir my name is jarvis")
                    speak("I'm an AI generated assistant. I can help you with your daily works")
                    speak("What can I do for you ?")
                elif "my name is" in query:
                    speak("Nice to hear that sir")
                elif "i am fine" in query:
                    speak("That's great sir")
                elif "your age" in query:
                    birthday = datetime.date(2023, 1, 12)
                    age = get_age(birthday)
                    speak(age)
                    print(age)
                elif "my age" in query:
                    birthday = datetime.date(2005, 11, 29)
                    age = get_age(birthday)
                    speak(age)
                    print(age)
                
                elif "temperature" in query:
                    search = "temperature in "
                    speak("At what place should i search for ?")
                    cm = takeCommand().lower()
                    url = f"https://www.google.com/search?q={search}+{cm}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} {cm} is {temp}")
                
                elif "weather" in query:
                    search = "temperature in "
                    speak("At what place should i search for ?")
                    cm = takeCommand().lower()
                    url = f"https://www.google.com/search?q={search}+{cm}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} {cm} is {temp}")
                
                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"Sir, the time is {strTime}")

                elif "internet speed" in query:
                    import speedtest
                    st = speedtest.Speedtest()
                    dl = st.download()
                    up = st.upload()
                    dl = dl/1000000
                    up = up/1000000
                    dl = round(dl)
                    up = round(up)
                    speak(f"Sir we have {dl} Megabits per second download speed and {up} Megabits per second upload speed")

                elif "ip address" in query:
                    ip = get('https://api.ipify.org').text
                    speak(f"Sir, your IP address is {ip}")

                elif "how are you?" in query:
                    speak("I am perfect sir")
                elif "thank you" in query:
                    speak("You are welcome sir")
                elif "what is my name" in query:
                    speak("Sir, your name is Rithvik")
                elif "rude" in query:
                    speak("Sorry sir. I will behave properly next time")
                elif "angry on you" in query:
                    speak("Sorry sir and forgive me if I have done anything wrong")
                    speak("Can you please say the mistake i did ?")
                    cm = takeCommand().lower()
                    speak("Apologies sir and i'll try to correct the mistake")
                elif "so good" in query:
                    speak("Thank you sir")

                elif "wikipedia" in query or "search in wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)

                elif "what is" in query:
                    query = query.replace("jarvis", "")
                    from SearchNow import searchGoogle
                    searchGoogle(query)

                elif "what are" in query:
                    query = query.replace("jarvis", "")
                    from SearchNow import searchGoogle
                    searchGoogle(query)

                elif "define" in query:
                    query = query.replace("jarvis", "")
                    from SearchNow import searchGoogle
                    searchGoogle(query)

                elif "explain" in query:
                    query = query.replace("jarvis", "")
                    from SearchNow import searchGoogle
                    searchGoogle(query)

                elif "search" in query:
                    query = query.replace("jarvis", "")
                    from SearchNow import searchGoogle
                    searchGoogle(query)

                elif "open notepad" in query:
                    npath = "C:\\Windows\\notepad.exe"
                    os.startfile(npath)
                elif "open edge" in query:
                    npath = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
                    os.startfile(npath)
                elif "open word" in query:
                    npath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
                    os.startfile(npath)
                elif "open excel" in query:
                    npath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
                    os.startfile(npath)
                elif "open command prompt" in query:
                    npath = "C:\\Windows\\system32\\cmd.exe"
                    os.startfile(npath)
                elif "open powerpoint" in query:
                    npath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
                    os.startfile(npath)
                elif "open teams" in query:
                    npath = "C:\\Users\\Rithvik\\AppData\\Local\\Microsoft\\Teams\\Update.exe"

                elif "close notepad" in query:
                    speak("Okay sir, closing notepad")
                    os.system("taskkill /f /im notepad.exe")
                elif "close word" in query:
                    speak("Okay sir, closing word")
                    os.system("taskkill /f /im WINWORD.exe")
                elif "close excel" in query:
                    speak("Okay sir, closing excel")
                    os.system("taskkill /f /im EXCEL.exe")
                elif "close powerpoint" in query:
                    speak("Okay sir, closing powerpoint")
                    os.system("taskkill /f /im POWERPNT.exe")
                elif "close edge" in query:
                    speak("Okay sir, closing edge")
                    os.system("taskkill /f /im msedge.exe")
                elif "close google" in query:
                    speak("Okay sir, closing google")
                    os.system('taskkill /f /im chrome.exe')
                elif "close teams" in query:
                    speak("Okay sir, closing teams")

                elif "alarm" in query:
                    speak("Sir please tell me time to set alarm. for example, set alarm to 5:30 am")
                    tt = takeCommand()
                    tt = tt.replace("set alarm to ","")
                    tt = tt.replace("Set Alarm to ","")
                    tt = tt.replace(".","")
                    tt = tt.upper()
                    import Myalarm
                    Myalarm.alarm(tt)

                elif "search in chatgpt" in query or "search in chat gpt" in query or "search in charge gpt" in query:
                    webbrowser.open("https://chat.openai.com")
                    from pynput.keyboard import Key, Controller
                    import Keyboard
                    keyboard = Controller()
                    speak("Sir what do you want to search ?")
                    cm = takeCommand().lower()
                    keyboard.type(cm)
                    keyboard.press(Key.enter)

                elif "search in bard" in query or "search in google bard" in query or "search in bard google" in query:
                    webbrowser.open("https://bard.google.com/chat")
                    from pynput.keyboard import Key, Controller
                    import Keyboard
                    keyboard = Controller()
                    speak("Sir what do you want to search ?")
                    cm = takeCommand().lower()
                    keyboard.type(cm)
                    keyboard.press(Key.enter)
                
                elif "open google" in query:
                    speak("Sir, What should i search for you")
                    cm=takeCommand().lower()
                    webbrowser.open(f"{cm}")
                elif "open youtube" in query:
                    webbrowser.open("www.youtube.com")
                elif "open facebook" in query:
                    webbrowser.open("www.facebook.com")
                elif "open instagram" in query:
                    webbrowser.open("www.instagram.com")
                elif "open chatgpt" in query or "open chat gpt" in query:
                    webbrowser.open("https://chat.openai.com")
                elif "open vtop" in query:
                    webbrowser.open("https://vtopcc.vit.ac.in/vtop/open/page")
                elif "open twitter" in query:
                    webbrowser.open("https://twitter.com/home")
                elif "open linkedin" in query:
                    webbrowser.open("https://www.linkedin.com/feed/")
                elif "open you AI" in query or "open u ai" in query or "open uai" in query:
                    webbrowser.open("https://you.com/")

                elif "close this tab" in query or "close the tab" in query or "close tab" in query:
                    from pynput.keyboard import Key, Controller
                    import Keyboard
                    keyboard = Controller()
                    keyboard.press(Key.ctrl)
                    keyboard.press('w')
                    keyboard.release(Key.ctrl)

                elif "news" in query:
                    speak("Please wait sir. Fetching the latest news for you")
                    news()

                elif "calculate" in query:
                    from Calculator import Wolframalpha
                    from Calculator import Calc
                    query = query.replace("calculate","")
                    query = query.replace("jarvis","")
                    Calc(query)
                
                elif "play a song on youtube" in query:
                    speak("Sir, which song should i play for you ?")
                    cm=takeCommand().lower()
                    pywhatkit.playonyt(cm)
                    speak("Done sir")

                elif "send an email" in query:
                    try:
                        speak("sir, what should i send ?")
                        cm = takeCommand().lower()
                        to = "rithviksnsr2911@gmail.com"
                        from SendEmail import sendEmail
                        sendEmail(to, cm)
                        speak("Email has been sent sir")
                    except Exception as e:
                        print(e)
                        speak("Sorry, I am unable to send this email at the moment.")

                elif "joke" in query:
                    joke = pyjokes.get_joke()
                    speak(joke)

                elif "how much power left" in query or "how much power we have" in query or "battery" in query or "power" in query:
                    import psutil
                    battery = psutil.sensors_battery()
                    percentage = battery.percent
                    speak(f"sir our system has {percentage} percent battery power")
                    if percentage >=75:
                        speak("we have enough power to continue with our work")
                    elif percentage >=40 and percentage <75:
                        speak("we should connect our system to charging point to charge the battery")
                    elif percentage <=15 and percentage <=30:
                        speak("we don't have enough power to work on. Please consider connecting to the charger")
                    elif percentage<=15:
                        speak("we have very low power. please connect the charger or our system will shut down soon")

                elif "shut down immediately" in query:
                    os.system("shutdown /p /f")
                
                elif "shut down the system" in query:
                    os.system("shutdown /s /t S")

                elif "restart the system" in query:
                    os.system("shutdown /r /t S")
                
                elif "play a game" in query or "rock paper scissors" in query:
                    speak("Let's play rock-paper-scissors")
                    from Game import game_play
                    game_play()

                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused sir")
                elif "play" in query:
                    pyautogui.press("k")
                    speak("video played sir")
                elif "mute the video" in query:
                    pyautogui.press("m")
                    speak("video muted sir")
                elif "mute" in query:
                    from Keyboard import volumemute
                    speak("Turning the volume mute")
                    volumemute()
                elif "volume up" in query:
                    from Keyboard import volumeup
                    speak("Turning volume up sir")
                    volumeup()
                elif "volume down" in query:
                    from Keyboard import volumedown
                    speak("Turning volume down sir")
                    volumedown()

                elif "where I am" in query or "where am I" in query or "where we are now" in query or "where we are" in query:
                    speak("Wait sir let me check")
                    try:
                        ipAdd = requests.get("https://api.ipify.org").text
                        print(ipAdd)
                        url = "https://get.geojs.io/v1/ip/geo/"+ipAdd+".json"
                        geo_requests = requests.get(url)
                        geo_data = geo_requests.json()
                        city = geo_data["city"]
                        country = geo_data["country"]
                        speak(f"sir i am not sure but i think we are in  {city} city  of {country} country")
                    except Exception as e:
                        speak("Sorry sir, due to network issue i am not able to find where we are")
                        pass

                elif "screenshot" in query:
                    speak("Sir in what name should i save the file ?")
                    cm = takeCommand().lower()
                    import pyautogui
                    im = pyautogui.screenshot()
                    im.save(f"{cm}.jpg")

                elif "click my photo" in query or "click a photo" in query:
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(2)
                    pyautogui.press("enter")
                
                elif "open bing AI" in query or " open Bing AI" in query or "open bing ai" in query or "open Bing ai" in query:
                    from Keyboard import openbingai
                    from pynput.keyboard import Key, Controller
                    import Keyboard
                    keyboard = Controller()
                    openbingai()
                    speak("Sir what do you want to search ?")
                    cm = takeCommand().lower()
                    keyboard.type(cm)
                    keyboard.press(Key.enter)

                elif "close bing AI" in query or " close Bing AI" in query or "close bing ai" in query or "close Bing ai" in query or "bing AI" in query or "Bing AI" in query:
                    from Keyboard import closebingai
                    closebingai()

                elif "activate how to do mode" in query or "activate how to do mod" in query:
                    from pywikihow import search_wikihow
                    speak("Sir how to do mode is activated. You can now ask anything you want")
                    cm = takeCommand().lower()
                    max_results = 1
                    how_to = search_wikihow(cm , max_results)
                    assert len(how_to) == 1
                    how_to[0].print()
                    speak(how_to[0].summary)

                elif "tired" in query:
                    speak("What happened sir ?")
                    cm = takeCommand().lower()
                    speak("Let me cool you down sir")
                    speak("playing a song for you sir")
                    a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
                    b = random.choice(a)
                    if b == 1:
                        cm = "College papa"
                        pywhatkit.playonyt(cm)
                    elif b == 2:
                        cm = "Why this kolaveri de"
                        pywhatkit.playonyt(cm)
                    elif b == 3:
                        cm = "maate vinaduga"
                        pywhatkit.playonyt(cm)
                    elif b == 4:
                        cm = ""
                        pywhatkit.playonyt(cm)
                    elif b == 5:
                        cm = ""
                        pywhatkit.playonyt(cm)
                    elif b == 6:
                        cm = ""
                        pywhatkit.playonyt(cm)
                    elif b == 7:
                        cm = ""
                        pywhatkit.playonyt(cm)
                    elif b == 8:
                        cm = ""
                        pywhatkit.playonyt(cm)
                    elif b == 9:
                        cm = ""
                        pywhatkit.playonyt(cm)
                    elif b == 10:
                        cm = ""
                        pywhatkit.playonyt(cm)
                    os.system('taskkill /f /im chrome.exe')

                elif "change password" in query:
                    speak("what's the new password that you want to enter sir ?")
                    new_pw = input("enter the new password :- ")
                    new_password = open("Password.txt","w")
                    new_password.close()
                    speak("Done sir")
                    speak(f"Your new password is {new_pw}")
                
                elif "switch the window" in query:
                    pyautogui.keyDown("alt")
                    pyautogui.press("tab")
                    time.sleep(1)
                    pyautogui.keyUp("alt")

                elif "whatsapp message" in query:
                    from Whatsapp import sendMessage
                    sendMessage()

                elif "schedule my day" in query:
                    tasks = []
                    speak("Do you want to clear old tasks (Please say yes or no)")
                    query = takeCommand().lower()
                    if "yes" in query:
                        file = open("Tasks.txt","w")
                        file.write(f"")
                        file.close()
                        no_tasks = int(input("Enter the number of tasks :- "))
                        i = 0
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("Tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()
                    elif "no" in query:
                        i = 0
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("Tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()

                    elif "show my schedule" in query:
                        file = open("Tasks.txt", "r")
                        content = file.read()
                        file.close()
                        mixer.init()
                        mixer.music.load("Notification.mp3")
                        mixer.music.play()

                        notification.notify(
                            title = "My schedule :- ",
                            message = content,
                            timeout = 15
                        )
                
                elif "exit" in query or "exit" in query:
                    speak("Thanks for using me sir, have a good day")
                    sys.exit()





'''training_data = []
labels = []
for intent, data in intents.items():
    for pattern  in data['patterns']:
        training_data.append(pattern.lower())
        labels.append(intent)

Vectorizer =  TfidfVectorizer(tokenizer = nltk.word_tokenize, stop_words = "english",max_df = 0.8, min_df = 1)
X_train = Vectorizer.fit_transform(training_data)
X_train, X_test, Y_train, Y_test = train_test_split(X_train, labels, test_size=0.4, random_state=42, stratify = labels)

model = SVC(kernel = 'linear', probability = True, C=1.0)
model.fit(X_train, Y_train)
predictions = model.predict(X_test)

def predict_intent(user_input):
    input_vector = Vectorizer.transform([user_input])
    intent = model.predict(input_vector)[0]
    return intent

print("AI Assistent: Hello! How can I assist you ?")
while True:
    user_input = takeCommand().lower()
    if user_input.lower() == 'exit':
        print("AI Assistent: Goodbye!")
        break

    intent = predict_intent(user_input)
    if intent in intents:
        responses = intents[intent]['responses']
        response = random.choice(responses)
        speak(response)

    else:
        speak("Sorry, I'm not sure how to respond to it")
'''
