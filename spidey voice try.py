import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia
import datetime
import wolframalpha
import os
import speech_recognition
from datetime import time
from pyttsx3 import speak
import requests
import time

def wish():
  z=int(datetime.datetime.now().hour)
  if z>6 and z<=12 :
      print("Good morning sir")
      speak("Good morning sir")
  elif z>12 and z<=16 :
      print("Good afternoon sir")
      speak("Good afternoon sir")
  elif z>16 and z<=22 :
      print("Good evening sir")
      speak("Good evening sir")
  elif z>22 and z<=6 :
      print("Good night sir")
      speak("Good night sir")
  return time.ctime()

def vinput():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('speak something: ') 
        r.pause_threshold=1
        audio = r.listen(source)
    try :
        a=r.recognize_google(audio,language='en-in')
        print('you said:', a)
    except Exception  :
        speak('sorry I did not hear that. please repeat it ')  
        return(vinput())
    return a

def assis() : 
    print('\t','\t',"Type 'action' to know what I can do")
    a=vinput().lower()
    if a=='hello' :
           speak ('Hi,  I am SPIDEY ')
           print('SPIDEY - Specialized Personal Intelligence Designed to Enhance You')
           speak('Specialized Personal Intelligence Designed to Enhance You')
    elif a=='time' :
           t=datetime.datetime.now()
           speak(t)
           print(t)
    elif a=='action' :
           print( '\t','\t','\t','\t','action') 
           print('time - shows time with date')
           print('answer - can answer you like GK question,mathematical question')
           print('data - answer in 5 sentences about the query like review which is in wikipedia page ')
           print('short data - gives categorical idea which can be used in data and full data  ')
           print('full data - answer about the query like book review which is in wikipedia page ')
           print('open - opens the software in pc')
           print("weather - says today's weather for which city you ask for ")
           print('none - ends the program from repeating')
    elif a=='answer' :
            b=vinput().lower
            #appid=' YKKUUE-7HRJJP6VRL'
            client=wolframalpha.Client('YKKUUE-7HRJJP6VRL')
            response=client.query(b)
            answer=next(response.results).text
            print('searching....') 
            print(answer) 
            speak(answer)   
    elif a=='data' :
            b=vinput().lower
            ans=wikipedia.summary(b,sentences=5)
            print('searching....') 
            print(ans)  
            speak(ans)
    elif a=='short data' :
            b= input('what should i search for you:  ')
            ans=wikipedia.search(b)
            print('searching....') 
            print(ans) 
            speak(ans)
    elif a== 'full data' :
            b= input('what should i search for you:  ')
            ans=(wikipedia.page(b).content)
            print('searching....') 
            print(ans)   
            speak(ans)
    elif a=='open' :
            b=input('mention the app to be opened: ' )
            os.system(b)
    elif a== 'weather' :
           print(" \t \t \t Today's weather ")
           appid='https://api.openweathermap.org/data/2.5/weather?appid=bcee71c095bc32238890e627fc9a450e&q='
           city = input('enter the city : ')
           url = appid+city
           data=requests.get(url).json()
           ldata=data['weather'][0]['main']
           wdata=data['weather'] [0]['description']
           print('Full info :',wdata)
           print('Short info :',ldata)
           speak(wdata)
           speak(ldata)
    elif a=='done'  :
            speak('thank you sir')
            pass  
    while a!='done'  :
            print(assis())
            return ('done')
print(wish())
print(assis())             
