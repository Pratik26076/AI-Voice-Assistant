from PyQt5 import QtWidgets, QtGui,QtCore
from PyQt5.QtGui import QMovie
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
import pyttsx3
import speech_recognition as sr
import os
import time
import webbrowser
import datetime

import pyttsx3 #pip installpyttsx3 == text data into speech using python
import datetime
import speech_recognition as sr #pip install SpeechRecognition == speech from mic to text
import smtplib
import pyautogui
import webbrowser as wb
from time import sleep
import wikipedia
import pywhatkit
import requests
from pytube import YouTube
import os
from newsapi import NewsApiClient
import clipboard
import pyjokes
import time as tt
import string
import random
import psutil

flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[2].id)
engine.setProperty('rate',180)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def date():
    year = int (datetime.datetime.now().year)
    month = int (datetime.datetime.now().month)
    day = int (datetime.datetime.now().day)
    speak("The current date is : ")
    speak(year)
    speak(month)
    speak(day)

def greeting():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good morning sir!")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon sir!")
    elif hour >= 18 and hour < 24:
        speak("Good evening sir!")
    else :
        speak("Good night sir!")

def wishme():
    speak("Welcome back Boss!")
    #time()
    date()
    greeting()
    speak("Charlie at your service, please tell me how can i help you?")

def takeCommandCMD():
    query = input("please tell me how can i help you?\n")
    return query

def takeCommandMic():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening...")
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        speak("Recognizing...")
        print("Recognizing...")
        query = r.recognize_google(audio , language="en-IN")
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again please...")
        return "None"
    return query

def sendwhatsmsg(phone_no, message):
    Message = message
    wb.open('https://web.whatsapp.com/send?phone='+phone_no+'&text='+Message)
    sleep(25)
    pyautogui.press('enter')  #OR enter

def searchgoogle():
    speak('what should i search for?')
    search = takeCommandMic()
    wb.open('https://www.google.com/search?q='+search)

class mainT(QThread):
    def __init__(self):
        super(mainT,self).__init__()
    
    def run(self):
        self.CHARLIE()
    
    def STT(self):
        R = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...........")
            audio = R.listen(source)
        try:
            print("Recog......")
            text = R.recognize_google(audio,language='en-in')
            print(">> ",text)
        except Exception:
            speak("Sorry Speak Again")
            return "None"
        text = text.lower()
        return text


    def CHARLIE(self):
        #wishme()
        while True:
            self.query = self.STT()
            
            if 'time' in self.query:
                Time = datetime.datetime.now().strftime("%I:%M:%S")# hour = I minutes = M seconds = S 
                speak("The current time is : ")
                speak(Time)
            
            elif 'date' in self.query:
                year = int (datetime.datetime.now().year)
                month = int (datetime.datetime.now().month)
                day = int (datetime.datetime.now().day)
                speak("The current date is : ")
                speak(year)
                speak(month)
                speak(day)

            elif 'message' in self.query:
                user_name = {
                    'Pratik':'+91 8261876431','Rajshri':'+91 9588426689','Gayatri':'+91 8483003236','Sakshi':'+91 9356286323',
                    'Ranjit':'+91 7719949070','Siddhant':'+91 8010409676','Nilkanth':'+91 9322301800','Krishna':'+91 8421969604'
                }
                try:
                    speak("To whom you want to send the whatsapp message?")
                    name = takeCommandMic()
                    phone_no = user_name[name]
                    speak("What is the message?")
                    message = takeCommandMic()
                    sendwhatsmsg(phone_no, message)
                    speak("whatsapp message has been send")
                except Exception as e:
                    print(e)
                    speak("Unable to send the whatsapp message") 


            elif 'search' in self.query:
                speak('what should i search for?')
                search = takeCommandMic()
                wb.open('https://www.google.com/search?q='+search)

            elif 'youtube' in self.query:
                speak("what should i search for you on youtube?")
                topic = takeCommandMic()
                pywhatkit.playonyt(topic)

            elif 'news' in self.query:
                newsapi = NewsApiClient(api_key = 'faee7d5b693841ff82a54952bbbeab8b')
                speak('What topic you need the news about?')
                topic = takeCommandMic()
                data = newsapi.get_top_headlines(q = topic,
                                                language = 'en',
                                                page_size = 5)
                newsdata = data['articles']
                for x,y in enumerate(newsdata):
                    print(f'{x}{y["description"]}')
                    speak(f'{x}{y["description"]}')
                speak("that's it for now i'll update you in some time")

            elif 'download video' in self.query:
                    import os
                    os.system("start cmd")
                    sleep(60)
                    # link = str(input("Enter your link here : "))
                    # youtube_1 = YouTube(link)
                    # print(youtube_1.title)
                    # print(youtube_1.thumbnail_url)
                    # stream = youtube_1.streams.get_highest_resolution()
                    # stream.download()
                    # print("Downolad is Successful")
                                
            elif 'download audio' in self.query:
                import os
                os.system("start cmd")
                sleep(60)
                # link = str(input("Enter your link here : "))
                # youtube_1 = YouTube(link)
                # print(youtube_1.title)
                # print(youtube_1.thumbnail_url)

                # videos = youtube_1.streams.filter(only_audio=True)  #only audio
                # stream = youtube_1.streams.get_highest_resolution()
                # stream.download()
                # print("Downolad is Successful")
            
            elif 'download playlist' in self.query:
                import os
                os.system("start cmd")
                sleep(60)
                # #For Downloading playlist
                # from pytube import Playlist
                # link = str(input("Enter your link here : "))
                # youtube_1 = YouTube(link)   #paste Plalist link here
                # print(f'Downloading : {link.title}')
                # for video in link.videos:
                #     video.streams.first().download()
                        
            elif 'text to speech' in self.query:
                text = clipboard.paste()
                print(text)
                speak(text)
                        
            elif 'screenshot' in self.query:
                name_img = tt.time()
                name_img = f'E:\\GUI-CHARLIE-main\\Screenshot\\{name_img}.png'
                img = pyautogui.screenshot(name_img)
                img.show()

            elif 'password' in self.query:
                s1 = string.ascii_uppercase
                s2 = string.ascii_lowercase
                s3 = string.digits
                s4 = string.punctuation

                passlen = 8
                s = []
                s.extend(list(s1))
                s.extend(list(s2))
                s.extend(list(s3))
                s.extend(list(s4))
                
                random.shuffle(s)
                newpass = ("".join(s[0:passlen]))
                print(newpass)
                speak(newpass)

            elif 'flip' in self.query:
                speak("Okay sir, flipping a coin")
                coin = ['heads', 'tails']
                toss = []
                toss.extend(coin)
                random.shuffle(toss)
                toss = ("".join(toss[0]))
                speak("I fliiped the coin and you got "+toss)

            elif 'roll' in self.query:
                speak("Okay sir, rolling a die for you")
                die = ['1','2','3','4','5','6']
                roll = []
                roll.extend(die)
                random.shuffle(roll)
                roll = ("".join(roll[0]))
                speak("I rolled a die and  you got " +roll)

            elif 'weather' in self.query:
                city = 'Baramati'
                url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid=e9518ef7a73718bd074f8d092b657465'
                res = requests.get(url)
                data = res.json()

                weather = data['weather'] [0] ['main']
                temp = data['main']['temp']
                desp = data['weather'] [0] ['description']
                temp = round((temp - 32) * 5/9)
                print(weather)
                print(temp)
                print(desp)
                speak(f'weather in{city} city is like')
                speak('Temperature : {} degree celcius'.format(temp))
                speak('weather is {}'.format(desp))

            elif 'wikipedia' in self.query:
                speak('searching on wikipedia....')
                self.query = self.query.replace("wikipedia", "")
                result = wikipedia.summary(self.query, sentences = 10)
                print(result)
                speak(result)
            
            elif 'open document' in self.query:
                import os
                os.system('explorer C://{}'.format(self.query.replace('open',''))) #to open my documents

            elif 'open code' in self.query:
                import os
                codepath = 'E:\\VS code\\Microsoft VS Code\\Code.exe'
                os.startfile(codepath)

            elif 'joke' in self.query:
                speak(pyjokes.get_joke())
            
            elif 'open google' in self.query:
                webbrowser.open('www.google.co.in')
                speak("opening google")
            
            elif 'remember that' in self.query :
                speak("What should I remember?")
                data = takeCommandMic()
                speak("What said me to remember that" + data)
                remember = open('data.txt','w')
                remember.write(data)
                remember.close()

            elif 'do you know anything' in self.query:
                remember = open('data.txt', 'r')
                speak("you told me to remember that " + remember.read())

            elif 'cpu' in self.query:
                usage = str(psutil.cpu_percent())
                speak('CPU is at'+usage)
                battery = psutil.sensors_battery()
                speak("Battery is at")
                speak(battery.percent)

            elif 'offline' in self.query:
                sys.exit()
                











FROM_MAIN,_ = loadUiType(os.path.join(os.path.dirname(__file__),"./scifi.ui"))

class Main(QMainWindow,FROM_MAIN):
    def __init__(self,parent=None):
        super(Main,self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(1920,1080)
        self.label_7 = QLabel
        self.exitB.setStyleSheet("background-image:url(./lib/exit - Copy.png);\n"
        "border:none;")
        self.exitB.clicked.connect(self.close)
        self.setWindowFlags(flags)
        Dspeak = mainT()
        self.label_7 = QMovie("./lib/gifloader.gif", QByteArray(), self)
        self.label_7.setCacheMode(QMovie.CacheAll)
        self.label_4.setMovie(self.label_7)
        self.label_7.start()

        self.ts = time.strftime("%A, %d %B")

        Dspeak.start()
        self.label.setPixmap(QPixmap("./lib/tuse.png"))
        self.label_5.setText("<font size=8 color='white'>"+self.ts+"</font>")
        self.label_5.setFont(QFont(QFont('Acens',8)))


app = QtWidgets.QApplication(sys.argv)
main = Main()
main.show()
exit(app.exec_())