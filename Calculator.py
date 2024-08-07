import wolframalpha
import pyttsx3
import speech_recognition

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

def Wolframalpha(query):
    apikey = "K29APK-5A73A9KWPQ"
    requester = wolframalpha.Client(apikey)
    requested = requester.query(query)

    try:
        answer = next(requested.results).text
        return answer
    except:
        speak("THe value is not answerable")

def  Calc(query):
    Term = str(query)
    Term = Term.replace("jarvis","")
    Term = Term.replace("multipy","")
    Term = Term.replace("divide","")
    Term = Term.replace("plus","")
    Term = Term.replace("minus","")

    Final = str(Term)
    try:
        result = Wolframalpha(Final)
        print(f"{result}")
        speak(result)

    except:
        speak("The value is not answerable")
        