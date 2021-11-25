import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
import requests
from requests import get
import socket

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=5,phrase_time_limit=5)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")
    except Exception as e:
        speak("Say that again please...")
        return "none"
    return query 
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>0 and hour<12:
        speak("Good Morning")
    elif hour>12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am Jarvis , how can i help you")

if __name__=="__main__":
    wish()
    # while True:
    if 1:
        query = takecommand().lower()

        if "open notepad" in query:
            npath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)
        elif "open command prompt" in query:
            cpath="C:\\WINDOWS\\system32\\cmd.exe"
            os.startfile(cpath)
        elif "open camera" in query:
            cap=cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam',img)
                k=cv2.waitkey(50)
                if k==2:
                    break
            cap.release()
            cv2.destroyAllWindows()
        elif "play music" in query:
            music_dir = "C:\\songs"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            for song in songs:
                if song.endswith ('.mp3'):
                    os.startfile(os.path.join(music_dir,rd))
        
        # elif "ip address" in query:
        #     ipa = get('https://api.ipify.org').text
        #     speak(f"your IP adress is {ipa}")

        elif "ip address" in query:
            hostname = socket.gethostname()
            IPAddr = socket.gethostbyname(hostname)
            speak(f"your computer name is:{hostname}")
            speak(f"your computer IP Address is:{IPAddr}")

        
    # takecommand()
    # speak("Hello there, What can I do for you")