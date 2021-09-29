import pyttsx3 as p
import speech_recognition as sr
from selenium_web import *
from youtube import *
from news import *
import randfacts



engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 130)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


r = sr.Recognizer()

speak("Hello sir and mam, im your voice assistant. How are you?")

with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source, 1.2)
    print("Listening...")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)
if "what" and "about" and "you" in text:
    print("I am having a good day sir and mam")
    speak("I am having a good day sir and mam")
    print("What can i do for you")
    speak("What can i do for you")

with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source, 1.2)
    print("Listening...")
    audio = r.listen(source)
    text2 = r.recognize_google(audio)

if "information" in text2:
    speak("you need information related to which topic?")

    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("Listening...")
        audio = r.listen(source)
        infor = r.recognize_google(audio)
    speak("Searching {} in wikipedia".format(infor))
    print("Searching {} in wikipedia".format(infor))
    assist = infow()
    assist.get_info(infor)

elif "play" and "video" in text2:
    speak("you want me to play which video?")
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("Listening...")
        audio = r.listen(source)
        vid = r.recognize_google(audio)
    speak("Playing {} on youtube".format(vid))
    print("Playing {} on youtube".format(vid))
    assist = music()
    assist.play(vid)

elif "news" in text2:
    print("Sure sir, Now i will read news for you.")
    speak("Sure sir, Now i will read news for you.")
    arr=news()
    for i in range(len(arr)):
        print(arr[i])
        speak(arr[i])

elif "fact" or "facts" in text2:
    speak("Sure sir, ")
    x=randfacts.getFact()
    print(x)
    speak("Did you know that, "+x)

elif "jokes" or "joke" in text2:
    arr=joke()
    print(arr[0])
    speak(arr[0])
    print(arr[1])
    speak(arr[1])




