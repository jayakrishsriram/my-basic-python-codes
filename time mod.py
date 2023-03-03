import time
import datetime
from pyttsx3 import speak
print(time.ctime())
z=int(datetime.datetime.now().hour)
if z>=6 and z<=12 :
    print("Good morning sir")
elif z>12 and z<=16 :
    print("Good afternoon sir")
    speak("Good afternoon sir")
elif z>16 and z<=22 :
    print("Good evening sir")
    speak("Good evening sir")
else :
    print("Good night sir")
    speak("Good night sir")
