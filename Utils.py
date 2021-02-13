import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
import wolframalpha
import json
import requests
import schedule
import calendar
import pyjokes

engine = pyttsx3.init()
voices = engine.getProperty('voices')

engine.setProperty('voice', 'voices[0].id')
engine.setProperty('rate', 150)
engine.setProperty('volume', 1)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Hello,Good Morning, Its Good To Have You Back")
        print("Hello,Good Morning, Its Good To Have You Back")
    elif 12 <= hour < 18:
        speak("Hello,Good Afternoon, Its Good To Have You Back")
        print("Hello,Good Afternoon, Its Good To Have You Back")
    else:
        speak("Hello,Good Evening, Its Good To Have You Back")
        print("Hello,Good Evening, Its Good To Have You Back")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            statement = r.recognize_google(audio, language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement


def todays_date(date):
    day, month, year = (int(i) for i in date.split(' '))
    day_number = calendar.weekday(year, month, day)
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days[day_number]


def weatherResponse(x):
    y = x["main"]
    current_temperature = round(y["temp"] - 273.15, 1)
    current_humidiy = y["humidity"]
    z = x["weather"]
    weather_description = z[0]["description"]
    speak(" Temperature in celsius unit is " +
          str(current_temperature) +
          "\n humidity in percentage is " +
          str(current_humidiy) +
          "\n description  " +
          str(weather_description))
    print(" Temperature in celsius unit = " +
          str(current_temperature) +
          "\n humidity (in percentage) = " +
          str(current_humidiy) +
          "\n description = " +
          str(weather_description))
    if current_temperature >= 30:
        print('The Weather Outside is Very Hot, I Suggest You Stay Hydrated')
        speak('The Weather Outside is Very Hot, I Suggest You Stay Hydrated')
    elif 24 < current_temperature < 30:
        print(
            'The Weather Outside is Moderately Hot, I Suggest You Wear Light Cloths')
        speak(
            'The Weather Outside is Moderately Hot, I Suggest You Wear Light Cloths')
    elif 16 < current_temperature <= 24:
        print('The Weather Outside is Warm, I Suggest You Go For A Walk Today')
        speak('The Weather Outside is Warm, I Suggest You Go For A Walk Today')
    elif current_temperature < 16:
        print('The Weather Outside is Cold, I Suggest You Wear Warm Clothes')
        speak('The Weather Outside is Cold, I Suggest You Wear Warm Clothes')


print("Loading your AI personal assistant eGeoffrey")
speak("Loading your AI personal assistant eGeoffrey")
wishMe()
