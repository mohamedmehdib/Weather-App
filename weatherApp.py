import datetime as dt
import requests
import pprint


BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = "" # You can get this api key from the link of " api openweathermap "
while True:
    try:
        CITY = input("Enter your city : ")

        url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
        response = requests.get(url).json()

        temp = response["main"]["temp"]-273.15
        humidity = response["main"]["humidity"]
        sunrise = dt.datetime.utcfromtimestamp(response["sys"]["sunrise"]+response["timezone"])
        sunset = dt.datetime.utcfromtimestamp(response["sys"]["sunset"]+response["timezone"])
        weather = response["weather"][0]["description"]
        windSpeed = response["wind"]["speed"]

        print("***********************")
        print(f'The temperature in {CITY.capitalize()} is : {(temp):.1f}')
        print(f'The humidity in {CITY.capitalize()} : {humidity:.1f}%')
        print(f'The sunrise in {CITY.capitalize()} is on : {sunrise}')
        print(f'The sunset in {CITY.capitalize()} is on : {sunset}')
        print(f'The weather in {CITY.capitalize()} is : {weather}')
        print(f'The wind speed in {CITY.capitalize()} : {windSpeed}m/s')
    except:
        print("Please verify the city name !")
