import requests

api_key = '08b7e56615d0752156e6ecafb523fd7d'

location = input('Please enter the location to look up weather in: ')

params = {
    'appid': api_key,
    'q': location,
    'units': 'imperial',
}

response = requests.get(f'http://api.openweathermap.org/data/2.5/weather', params=params)
weather_data = response.json()

print(f'Here is the weather for {location}:')
print(f'Description: {weather_data["weather"][0]["description"]}')
print(f'Current Temp: {weather_data["main"]["temp"]}F')
