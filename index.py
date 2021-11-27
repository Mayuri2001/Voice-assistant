import time
import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
import requests
from requests import get
import socket
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
import sys
import pyjokes
import pyautogui
import email_to
import instaloader

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
        audio = r.listen(source,timeout=0,phrase_time_limit=5)
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

def sendEmail(to,content):
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("patidarmayuri27@gmail.com","k_meenu_11")
    server.sendmail("patidarmayuri27@gmail.com",to,content)
    server.close()

def news():
    main_url="http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=8278dad38c6348e9855fe64f71b1919c"
    main_page = requests.get(main_url).json()
    articles = main_page["articles"]

    head=[]
    day=["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        speak(f"today's {day[i]} news is: {head[i]}")
    main_url='http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=36e001fb0f524f7ea59b5faaffbe0300'

    main_page=requests.get(main_url).json()
    #print(main_page)
    articles=main_page["articles"]
    #print(articles)
    head=[]
    day=["first","second","third","fourth","fifth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        #print (f"today's {day[i]} news is: ",head[i])
        speak(f"today's {day[i]} news is:{head[i]}")

if __name__=="__main__":
    wish()
    while True:
    # if 1:
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
        
        elif "wikipedia" in query:
            speak("searching wikipedia....")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            speak(results)
            
        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")

        elif "open stackoverflow" in query:
            webbrowser.open("www.stackoverflow.com")   

        elif "open google" in query:
            speak("sir,what should i search on google")
            cm=takecommand().lower()
            webbrowser.open(f"{cm}") 

        elif "send message" in query:
            kit.sendwhatmsg("+917582897416","How you doin'?",20,59)

        elif "play song on youtube" in query:
            kit.playonyt("Perfect")

        # elif "email to palak" in query:
        #     try:
        #         speak("What should i say?")
        #         content=takecommand().lower()
        #         to="palakmehta030@gmail.com"
        #         sendEmail(to,content)
        #         speak("email has been sent to mayuri")

        #     except Exception as e:
        #         print(e)
        #         speak("sorry sir, i am not able to send this mail to mayuri")

        elif "you can go to sleep" in query:
            speak("thanks for using me sir,have a good day")
            sys.exit()

        elif "close notepad" in query:
            speak("okay sir, closing notepad")
            os.system("taskkill /f /im notepad.exe")

        elif "set an alarm" in query:
            nn=int(datetime.datetime.now().hour)
            if nn==22:
                music_dir='C:\\songs'
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir,songs[0]))
        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)
        elif "shut down the system" in query:
            os.system("shutdown /r /t s")
        elif "restart the system" in query:
            os.system("shutdown /r /t s")
        elif "sleep the system" in query:
            os.system("rundl132.exe powrprof dil,SetSuspendState 0,1,0")
        elif "change the window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")
        
        elif "tell me the news" in query:
            speak("please wait sir, fetching the latest news")
            news()

        elif "switch the window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press('tab')
            time.sleep(1)
            pyautogui.keyUp("alt")

        elif "tell me news" in query:
            speak("please wait sir,fetching the latest news")
            news()

        elif "email to palak" in query:
            speak("sir what should i say")
            query=takecommand().lower()
            if "send a file" in query:
                email='patidarmayuri27@gmail.com'
                password='k_meenu_11'
                send_to_email='palakmehta030@gmail.com'
                speak("okay sir,what is the subject for this email")
                query=takecommand().lower()
                subject=query
                speak("and sir,what is the message for this email")
                query2=takecommand().lower()
                message=query2
                speak("sir please enter the correct path of file in shell")
                file_location=input("Please enter the path here")

                speak("Please wait, i am sending email now")

                msg=MIMEMultipart()
                msg['From']=email
                msg['To']=send_to_email
                msg['Subject']=subject

                msg.attach(MIMEText(message,'plain'))

                #Setup the attachment
                filename=os.path.basename(file_location)
                attachment=open(file_location,"rb")
                part=MIMEBase('application','octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition',"attachment; filename=%s" % filename)

                msg.attach(part)

                server = smtplib.SMTP('smtp.gmail.com',587)
                server.starttls()
                server.login(email,password)
                text = msg.as_string()
                server.sendmail(email,send_to_email,message)
                server.quit()
                speak("email has been sent")
            else:
                email = "patidarmayuri27@gmail.com"
                password = "k_meenu_11"
                send_to_email = "palakmehta03@gmail.com"
                message = query 

                server = smtplib.SMTP('smtp.gmail.com',587)
                server.starttls()
                server.login(email,password)
                server.sendmail(email,send_to_email,message)
                server.quit()
                speak("email has been sent")

        elif "where i am" in query or "where we are" in query:
                speak("wait sir, let me check")
                try:
                    ipAdd = requests.get('https://api.ipify.org').text
                    print(ipAdd)
                    url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'json'
                    geo_requests = requests.get(url)
                    geo_data = geo_requests.json()

                    city = geo_data['city']

                    country = geo_data['country']

                    speak(f"sir i am not sure, but i think we are in {city} city of {country}")
                except Exception as e:
                    speak("sorry sir , due to network issues i am not able to find where we are ")
                    pass 

        elif "instagram profile" in query or "profile on instagram" in query:
                speak("sir please enter the user name correctly")
                name = input("Enter the username here:")
                webbrowser.open(f"www.instagram.com/{name}")
                speak("sir would you like to download profile picture of this account.")
                condition = takecommand().lower()
                if "yes" in condition:
                    mod = instaloader.instaloader()
                    mod.download_profile(name,profile_pic_only=True)
                    speak("i am done sir, profile picture is saved in our main folder") 
                else:
                    pass
        elif "take screenshot" in query or "take a screenshot" in query:
            speak("sir,please tell me the name for this screenshot file")
            name = takecommand().lower()
            speak("please sir hold the screen for few seconds, i am taking screenshot")
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("i am done sir, the screenshot is saved in our main folder");