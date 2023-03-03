import pyttsx3
import webbrowser
import wikipedia
import datetime
import wolframalpha
import os
import speech_recognition
import datetime 
from pyttsx3 import speak
import requests
import multiprocessing
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
       
def assis() :
  print('\t','\t',"Type 'action' to know what I can do")
  a=input('ask something: ')
  if a=='hi' :
    speak ('Hi i am SPIDEY ')
    print('SPIDEY - Specialized Personal Intelligent Designed to Enhance You')
    speak('Specialized Personal Intelligent Designed to Enhance You')
  elif a=='time' :
    t=datetime.datetime.now().strftime('%H:%M')
    speak(t)
    print(t)
  elif a=='action' :
    print( '\t','\t','\t','\t','action') 
    print('hi - introduce itself')
    print('time - shows time with date')
    print('answer - can answer you like GK question,mathematical question')
    print('data - answer in 5 sentences about the query like review which is in wikipedia page ')
    print('short data - gives categorical idea which can be used in data and full data  ')
    print('full data - answer about the query like book review which is in wikipedia page ')
    print("weather - says today's weather about the city you ask for ")
    print('done - ends the program from repeating')
  elif a=='answer' :
     t=input(' your query : ')
     #appid=' YKKUUE-7HRJJP6VRL'
     client=wolframalpha.Client('YKKUUE-7HRJJP6VRL')
     response=client.query(t)
     answer=next(response.results).text
     print('searching....') 
     print(answer) 
     speak(answer)   
  elif a=='data' :
    t=input('what should i search for you:  ')
    ans=wikipedia.summary(t,sentences=5)
    print('searching....') 
    print(ans)  
    speak(ans)
  elif a=='short data' :
     t= input('what should i search for you:  ')
     ans=wikipedia.search(t)
     print('searching....') 
     print(ans) 
     speak(ans)
  elif a== 'full data' :
     t= input('what should i search for you:  ')
     ans=(wikipedia.page(t).content)
     print('searching....') 
     print(ans)   
     #speak(ans)
  elif a=='open' :
    t=input('mention the name the file to be opened: ' )
    os.system(t)
  elif a== 'weather' :
    print(" \t \t \t Today's weather ")
    appid='https://api.openweathermap.org/data/2.5/weather?appid=bcee71c095bc32238890e627fc9a450e&q='
    t = input('enter the city : ')
    url = appid+t
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
     return
print(wish())
print(assis())         
