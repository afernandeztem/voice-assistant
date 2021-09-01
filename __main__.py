#!/usr/bin/python 
from Utils import *


if __name__=='__main__':

    while True:
        speak("Tell me how can I help you now?")
        statement = takeCommand().lower()

        if statement == 0:
            continue

        if "goodbye" in statement or "ok bye" in statement or "stop" in statement:
            speak('your personal assistant G-one is shutting down,Good bye')
            print('your personal assistant G-one is shutting down,Good bye')
            break

        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement = statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'time' in statement:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"the time is {strTime}")
            speak(f"the time is {strTime}")

        elif 'date' in statement:
            day_object = datetime.date.today().strftime("%d %m %y")
            print('Today is ' + todays_date(day_object) + ' and the Date is ' + day_object)
            speak('Today is ' + todays_date(day_object) + ' and the Date is ' + day_object)

        elif 'search' in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)

        elif "tell me a joke" in statement:
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)

        elif 'ask' in statement:
            speak('I can answer to computational and geographical questions  and what question do you want to ask now')
            question=takeCommand()
            client = wolframalpha.Client('write here your api key')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)

        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am eGeoffrey version 1 point O your personal assistant. I am programmed to minor tasks like'
                  'predict time,search wikipedia,predict weather'
                  'In different cities, get top headline news from times of Spain and you can ask me computational or geographical questions too!')


        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Angel")
            print("I was built by Angel")

        elif "weather" in statement:
            api_key = "write here your api key"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            speak("what is the city name")
            city_name = takeCommand()
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                weatherResponse(x)

