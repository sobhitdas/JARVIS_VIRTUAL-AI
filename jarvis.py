import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour <12:
        speak("Good Morning!")
    elif hour>=12 and hour <=18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis Please tell me how may I help you")

def takeCommand():


     r = sr.Recognizer()
     with sr.Microphone() as source:
         print("Listening....")
         r.pause_threshold=1
         audio = r.listen(source)

     try:
        print("Recognizing....")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said : {query}\n")

     except Exception as e:
        print("Say that again please...")
        return "None"
     return query



if  __name__ == '__main__':
     wishMe()
     while True:
         query = takeCommand().lower()

         if 'what is' in query:
             speak('Searching ...')
             query = query.replace("wikipedia","")
             results = wikipedia.summary(query,sentences = 2)
             speak("According to Sources")
             print(results)
             speak(results)

         elif 'open youtube' in query:
             webbrowser.open("youtube.com")
         elif 'open google' in query:
             webbrowser.open("google.com")
         elif 'open gmail' in query:
             webbrowser.open("gmail.com")
         elif  'time' in query:
             strTime = datetime.datetime.now().strftime("%H:%M:%S")
             print(strTime)
             speak(f" Sir,  The time is {strTime}")
         elif 'open picture' in query:
             picPath ="C:\\Users\\Sobhit Das\\Pictures"
             os.startfile(picPath)
         elif 'date' in query:
             strTime1 = datetime.datetime.now().strftime("%m/%d/%Y")
             print(strTime1)
             speak(f"Sir ,the date is {strTime1}")
         elif 'weather' in query:
             webbrowser.open("https:///www.accuweather.com")
         elif 'who are you' in query:
             speak("I am Jarvis Sir.")
         elif 'how are you' in query:
             speak("I am fine Sir." )












