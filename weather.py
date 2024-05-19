import requests
import datetime as dt

api_key = 'ff725740d3c48de16300e3204883a51a'

location = input("Location: ")

result = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&appid={api_key}')

print(result.json())
description = result.json()['weather'][0]['description']
temp = result.json()['main']['temp']
feel = result.json()['main']['feels_like']
temp_max = result.json()['main']['temp_max']
temp_min = result.json()['main']['temp_min']

print(f"The weather in {location} is currently {temp}° C and feels like {feel}° C")
print(f"The max temperature is {temp_max}° C and the lowest is {temp_min}° C")