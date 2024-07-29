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
youtube_1 = YouTube(link)
speak("Downloading.........")
print("Downloading.........")
print(youtube_1.title)
print(youtube_1.thumbnail_url)

audios = youtube_1.streams.filter(only_audio=True)  #only audio
stream = youtube_1.streams.get_audio_only()
stream.download('E:\\GUI-CHARLIE-main\\Audio FIles')
print("Downolad is Successful")