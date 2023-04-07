import pyttsx3
import datetime
import wikipedia
import speech_recognition as sr
import webbrowser
import os
engine=pyttsx3.init('sapi5')
voice=engine.getProperty('voices')
engine.setProperty('voice',voice[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening!")
    speak("I am Friday,Been with Tony Stark at his last minutes  Well he made me only to help you   Please tell me how can i help you?")
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing.....")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said:{query}\n")
        
        
    except Exception as e:
        #print(e)
        speak("say that again please...")
        return "None"
    return query

    #it takes microphone input from the user and returns string output
if __name__=="__main__":
    wishMe()
    while 1:
        query=takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'the time'in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"ma'am the time is {strTime}")
        elif 'jarvis' in query:
            speak("I am friday,Jarvis was killed by Ultron")
        
                