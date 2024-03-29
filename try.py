import speech_recognition as sr
import pyttsx3
import os

speech = sr.Recognizer()

try:
    engine = pyttsx3.init()
except importerreor:
    print('rdinf')
except runtimeerror:
    print('dfti')

voices = engine.getProperty('voices')


engine.setProperty('voice','HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0')
rate = engine.getProperty('rate')
engine.setProperty('rate',rate)

def speak_text_cmd(cmd):
    engine.say(cmd)
    engine.runAndWait()

def read_voice_cmd():
    voice_text = ''
    print('listening........')
    with sr.Microphone() as source:
        audio = speech.listen(source)
    try:
        voice_text = speech.recognize_google(audio)
    except sr.UnknownValueError:
        pass
    except  sr.RequestError as e :
        print('Network Error')
    return voice_text


if __name__ == '__main__':
     speak_text_cmd('HELLO SIR. I AM JARVIS ')
     while True:
        voice_note = read_voice_cmd()
        print('cmd : {}'.format(voice_note))
        if 'hello' in voice_note:
            speak_text_cmd('Hello sir. How can i help you now')
            continue
        elif 'open' in voice_note:
            os.system(voice_note.format(voice_note.replace))
            continue
        elif 'bye' in voice_note:
            speak_text_cmd('bye  Mr. Prasad')
            exit()            