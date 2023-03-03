import speech_recognition as sr
import microphone
import pyttsx3
from pyttsx3 import speak
r=sr.Recognizer()

with sr.Microphone() as source:
    print('speak something: ')
    audio = r.listen(source)
    text=r.recognize_google(audio)
    print('you said: {}'.format(text))  
    speak(text) 