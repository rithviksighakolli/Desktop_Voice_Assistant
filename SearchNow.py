import pyttsx3
import speech_recognition
import pywhatkit
import wikipedia
import webbrowser

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

def searchGoogle(query):
    if "what is" in query or "define" in query or "explain" in query:
        import wikipedia as googleScrap
        query = query.replace("jarvis", "")
        query = query.replace("google search", "")
        query = query.replace("google", "")
        speak("This is what I found on google sir")

        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query, 2)
            speak(result)
        except:
            speak("No speakable output available")

def searchYoutube(query):
    if "youtube" in query:
        speak("This is what I found for your search sir")
        query = query.replace("youtube", "")
        query = query.replace("jarvis", "")
        query = query.replace("youtube search", "")

        web = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("Done, sir")

def searchWikipedia(query):
    if "wikipedia" in query:
        speak("Searching from wikipedia...")
        query = query.replace("wikipedia", "")
        query = query.replace("jarvis", "")
        query = query.replace("wikipedia search", "")
        query = query.replace("search wikipedia", "")
        results=wikipedia.summary(query, sentences = 2)
        speak("According to the wikipedia results...")
        print(results)
        speak(results)
