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
print("Downloading.........")
speak("Downloading.........")
print(youtube_1.title)
print(youtube_1.thumbnail_url)
stream = youtube_1.streams.get_highest_resolution()
stream.download('E:\\GUI-CHARLIE-main\\Video Files')
print("Downolad is Successful")