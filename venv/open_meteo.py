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


#  while True:  # WMO weather interpretation codes (WW)
weather_code_dict = {0:"Clear sky", 1:'Mainly clear', 2:"partly cloudy", 3:"overcast", 45:"Fog",
                     48:"Depositing rime fog", 51:"Light drizzle", 53:"Moderate drizzle", 55:"Dense drizzle",
                     56:"Light freezing drizzle", 57:"Heavy freezing drizzle", 61:"Slight rain", 63:"Moderate rain",
                     65:"Heavy rain", 66:"Light freezing rain", 67:"Moderate freezing rain", 71:"Slight snowfall",
                     73:"Moderate snowfall", 75:"Heavy snowfall", 77:"Snow grains", 80:"Slight rain showers",
                     81:"Moderate rain showers", 82:"Violent rain showers", 85:"Heavy snow showers",
                     86:"Slight Thunderstorms", 95:"Moderate Thunderstorms", 96:"Thunderstorms with slight hail",
                     99:"Thunderstorms with slight and heavy hail"}

''' list comprehension used in next line to pair key/values from both dictionaries. Matches WMO code from JSON into a 
dictionary list that has name of the weather type. avoids long elif statement previously used.
".get" needed to be used to avoid key value errors from other pairs not matching, 
returns 'none' if null pair is encountered.'''

dict3 = {k:list(map(weather_code_dict.get, vs)) for k, vs in my_data["daily"].items()}
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


print("Printing weather code details for the next seven days:")
print(dict3["weathercode"], "\n")
print(f"The current tempurature is:", my_data["current_weather"]["temperature"],
      my_data["daily_units"]["temperature_2m_max"], "\nToday you can expect",
      dict3["weathercode"][0], "\nwith a windspead of:", my_data["current_weather"]["windspeed"], wind_cardinal)
print(f"You can expect a high of", my_data["daily"]["temperature_2m_max"][0],
      my_data["daily_units"]["temperature_2m_max"], "and a low of", my_data["daily"]["temperature_2m_min"][0],
      my_data["daily_units"]["temperature_2m_max"])
print(f"The real feel today will be between", my_data["daily"]["apparent_temperature_max"][0],
      my_data["daily_units"]["temperature_2m_max"], "and", my_data["daily"]["apparent_temperature_min"][0],
      my_data["daily_units"]["temperature_2m_max"])
