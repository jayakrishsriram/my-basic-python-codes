import requests
import pyttsx3
from pyttsx3 import speak

appid='https://api.openweathermap.org/data/2.5/weather?appid=bcee71c095bc32238890e627fc9a450e&q='
city = input('enter the city : ')
url = appid+city
data=requests.get(url).json()
wdata=data['weather'][0]['description']
print(wdata)
speak(wdata)