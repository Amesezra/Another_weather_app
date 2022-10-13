#  https://bobbyhadz.com/blog/python-typeerror-the-json-object-must-be-str-bytes-or-bytearray-not-textiowrapper
#  super helpful for figuring out load() vs loads()
#  https://stackoverflow.com/questions/6648493/how-to-open-a-file-for-both-reading-and-writing
#  I/O behaviors
import datetime as dt
import requests
import json

url = "https://api.open-meteo.com/v1/forecast?latitude=41.4993&longitude=-81.6944&hourly=temperature_2m," \
      "apparent_temperature,precipitation&daily=weathercode,temperature_2m_max,temperature_2m_min," \
      "apparent_temperature_max,apparent_temperature_min,sunrise,sunset&current_weather=true&temperature_unit" \
      "=fahrenheit&windspeed_unit=mph&precipitation_unit=inch&timezone=America%2FNew_York"

response = requests.get(url).json()

with open('weather_data.json', 'w', encoding='utf-8') as f:
    json.dump(response, f, indent=3)

with open('weather_data.json', 'r', encoding='utf-8') as f:
    my_data = json.loads(f.read())

print("Printing weather code details for the next seven days:")
print(my_data["daily"]["weathercode"])
print()


while True:  # WMO weather interpretation codes (WW)
    weather_code = my_data["daily"]["weathercode"][0]
    if weather_code == 0:
        weather_code = "Clear sky"
    if weather_code == 1:
        weather_code = 'Mainly clear'
    elif weather_code == 2:
        weather_code = "partly cloudy"
    elif weather_code == 3:
        weather_code = "overcast"
    elif weather_code == 45:
        weather_code = "Fog"
    elif weather_code == 48:
        weather_code = "Depositing rime fog"
    elif weather_code == 51:
        weather_code = "Light drizzle"
    elif weather_code == 53:
        weather_code = "Moderate drizzle"
    elif weather_code == 55:
        weather_code = "Dense drizzle"
    elif weather_code == 56:
        weather_code = "Light freezing drizzle"
    elif weather_code == 57:
        weather_code = "Heavy freezing drizzle"
    elif weather_code == 61:
        weather_code = "Slight rain"
    elif weather_code == 63:
        weather_code = "Moderate rain"
    elif weather_code == 65:
        weather_code = "Heavy rain"
    elif weather_code == 66:
        weather_code = "Light freezing rain"
    elif weather_code == 67:
        weather_code = "Moderate freezing rain"
    elif weather_code == 71:
        weather_code = "Slight snowfall"
    elif weather_code == 73:
        weather_code = "Moderate snowfall"
    elif weather_code == 75:
        weather_code = "Heavy snowfall"
    elif weather_code == 77:
        weather_code = "Snow grains"
    elif weather_code == 80:
        weather_code = "Slight rain showers"
    elif weather_code == 81:
        weather_code = "Moderate rain showers"
    elif weather_code == 82:
        weather_code = "Violent rain showers"
    elif weather_code == 85:
        weather_code = "Heavy snow showers"
    elif weather_code == 86:
        weather_code = "Slight Thunderstorm"
    elif weather_code == 95:
        weather_code = "Moderate Thunderstorm"
    elif weather_code == 96:
        weather_code = "Thunderstorm with slight hail"
    elif weather_code == 99:
        weather_code = "Thunderstorm with slight and heavy hail"
    break

while True:
    wind_cardinal = my_data["current_weather"]["winddirection"]
    if wind_cardinal >= 0 < 25:
        wind_cardinal = "North"
    elif wind_cardinal >= 25 < 65:
        wind_cardinal = "North East"
    elif wind_cardinal >= 65 < 115:
        wind_cardinal = "East"
    elif wind_cardinal >= 115 < 155:
        wind_cardinal = "South East"
    elif wind_cardinal >= 155 < 205:
        wind_cardinal = "South"
    elif wind_cardinal >= 205 < 245:
        wind_cardinal = "South West"
    elif wind_cardinal >= 245 < 295:
        wind_cardinal = "West"
    elif wind_cardinal >= 295 < 335:
        wind_cardinal = "North West"
    elif wind_cardinal >= 335 < 360:
        wind_cardinal = "North"
    break


print(f"The current tempurature is:", my_data["current_weather"]["temperature"],
      my_data["daily_units"]["temperature_2m_max"], "\nToday you can expect",
      weather_code, "weather,""\nwith a windspead of:", my_data["current_weather"]["windspeed"], wind_cardinal)

print(f"You can expect a high of", my_data["daily"]["temperature_2m_max"][0],
      my_data["daily_units"]["temperature_2m_max"], "and a low of", my_data["daily"]["temperature_2m_min"][0],
      my_data["daily_units"]["temperature_2m_max"])
print(f"The real feel today will be between", my_data["daily"]["apparent_temperature_max"][0],
      my_data["daily_units"]["temperature_2m_max"], "and", my_data["daily"]["apparent_temperature_min"][0],
      my_data["daily_units"]["temperature_2m_max"])
