#For Downloading playlist
from pytube import Playlist
from pytube import YouTube

import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',180)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

link = str(input("Enter your link here : "))
youtube_1 = YouTube(link)   #paste Plalist link here
print("Downloading.........")
speak("Downloading.........")
print(f'Downloading : {link.title}')
for video in link.videos:
    video.streams.first().download('E:\\GUI-Jarvis-main\\Playlist')