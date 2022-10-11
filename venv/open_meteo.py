import datetime as dt
import requests
import json

url = "https://api.open-meteo.com/v1/forecast?latitude=41.4993&longitude=-81.6944" \
      "&hourly=temperature_2m,apparent_temperature,precipitation&daily=weathercode," \
      "sunrise,sunset&temperature_unit=fahrenheit&windspeed_unit=mph&precipitation_unit" \
      "=inch&timezone=America%2FNew_York"

response = requests.get(url).json()

with open('weather_data.json', 'w') as f:
    json.dump(response, f, indent=3)

while True:  # WMO weather interpretation codes (WW)
    weather_code = response["daily"]["weathercode"][0]
    if weather_code == 0:
        print("Clear sky")
    if weather_code == 1:
        print('Mainly clear')
    elif weather_code == 2:
        print("partly cloudy")
    elif weather_code == 3:
        print("overcast")
    elif weather_code == 45:
        print("Fog")
    elif weather_code == 48:
        print("Depositing rime fog")
    elif weather_code == 51:
        print("Light drizzle")
    elif weather_code == 53:
        print("Moderate drizzle")
    elif weather_code == 55:
        print("Dense drizzle")
    elif weather_code == 56:
        print("Light freezing drizzle")
    elif weather_code == 57:
        print("Heavy freezing drizzle")
    elif weather_code == 61:
        print("Slight rain")
    elif weather_code == 63:
        print("Moderate rain")
    elif weather_code == 65:
        print("Heavy rain")
    elif weather_code == 66:
        print("Light freezing rain")
    elif weather_code == 67:
        print("Moderate freezing rain")
    elif weather_code == 71:
        print("Slight snowfall")
    elif weather_code == 73:
        print("Moderate snowfall")
    elif weather_code == 75:
        print("Heavy snowfall")
    elif weather_code == 77:
        print("Snow grains")
    elif weather_code == 80:
        print("Slight rain showers")
    elif weather_code == 81:
        print("Moderate rain showers")
    elif weather_code == 82:
        print("Violent rain showers")
    elif weather_code == 85:
        print("Heavy snow showers")
    elif weather_code == 86:
        print("Slight Thunderstorm")
    elif weather_code == 95:
        print("Moderate Thunderstorm")
    elif weather_code == 96:
        print("Thunderstorm with slight hail")
    elif weather_code == 99:
        print("Thunderstorm with slight and heavy hail")
    break
