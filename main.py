import random
from word import wordList
import pyautogui
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import webbrowser
import pyjokes
import requests
n=1
d=1









listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            talk("Listening.....")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alex' in command:
                command = command.replace('alex', '')
                print(command)
    except:
        pass

    return command

def run_alex():
    command = take_command()
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt('playing' + song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('current time is ' + time)

    elif 'how' in command:

        talk('I am good , What about you?')
        print('I am good , What about you?')

    elif 'boss' in command:
        print('My boss is Yubraj Sigdel')
        talk("My boss is Yubraj Sigdel")

    elif 'tell me something about' in command:
        person = command.replace ('tell me something about' , '')
        info = wikipedia.summary(person , 1)
        print(info)
        talk(info)

    elif 'instagram' in command:
        talk('Opening instagram')
        chrome = "%c :/Program Files (86)/Google/Chrome/Application/chrome.exe %s"
        webbrowser.get(chrome).open_new("google.com")

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif 'family members' in command:
        talk("Madan , Sharada , Indira and Januka")

    elif 'word' in command:
        word = random.choices(wordList)
        print(word)
        talk(word)

    elif 'message' in command:
        talk('sending...')
        while (True):
            pyautogui.typewrite("this is spam message")
            pyautogui.press('enter')

    elif 'Laugh' in command:
        talk('ofcourse i can laugh   Hehe  haha  huhu  hoho')

    elif 'weather' in command:
        city=input('Enter your city name-->')

        Api_key="7037ec5da1bb5035bdeca683a61f0f46"

        final_URL="http://api.openweathermap.org/data/2.5/weather?id={}&appid={}".format(city, Api_key)

        result = requests.get(final_URL)
        data= result.json()
       # temperature = data['main']['temp']

        print(data)





            




    else:
        talk("Say the valid command")







while (n!=6):
    run_alex()
    n=n+1


talk("signing off")


