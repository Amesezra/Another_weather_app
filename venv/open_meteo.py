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
#  url string concatenate

"""
https://api.open-meteo.com"  #  Base URL
"/v1/forecast"  #  API endpoint, accepts geographical coordinate, then can take further arguments.

#  Example of lat/long input for geographic data.
"?latitude=41.4993&longitude=-81.6944"

# requests data into a hourly format
"&hourly="
"temperature_2m"
"apparent_temperature"
"apparent_temperature"

# requests data into a daily format
"&daily="
"weathercode"
"temperature_2m_max"
"temperature_2m_min"
"apparent_temperature_max"
"apparent_temperature_min"
"sunrise"
"sunset"

# requests data about current weather conditions
"&current_weather=true"
#  default unit is celsius, will only display fahrenheit if tag is added.
"&temperature_unit=fahrenheit"

#  default windspeed is km/h, can be modified with tags below.
"&windspeed_unit=mph"
"windspeed_unit=ms"
"windspeed_unit=kn"
#  default precipitation units is millimeter, can be modified with tags below.
"&precipitation_unit=inch"

# default timezone is GMT+0, time values will match that if left blank. Below are the optional arguments.
"&timezone=America%2FSao_Paulo"
"&timezone=America%2FNew_York"
"&timezone=America%2FChicago"
"&timezone=America%2FDenver"
"&timezone=America%2FLos_Angeles"
"&timezone=America%2FAnchorage"
"&timezone=Europe%2FLondon"
"&timezone=Europe%2FBerlin"
"&timezone=Europe%2FMoscow"
"&timezone=Africa%2FCairo"
"&timezone=Asia%2FBangkok"
"&timezone=Asia%2FSingapore"
"&timezone=Asia%2FTokyo"
"&timezone=Australia%2FSydney"
&timezone=Pacific%2FAuckland"


#  weather in a date range, YYYY-MM-DD replaced with actual dates. Can go back up-to 3 months.
"&start_date=YYYY-MM-DD&end_date=YYYY-MM-DD"
"&past_days=1"
"&past_days=5"
"&past_days=7"
"&past_days=14"
"&past_days=31"
"&past_days=61"
"&past_days=92"
"""
city_location_dict = {"New York": [40.714, -74.006], "Los Angeles": [34.052, -118.244], "Chicago": [41.85, -87.65],
                      "Houston": [29.763, -95.363], "Pheonix": [33.448, -112.074], "Philadelphia": [39.952, -75.164],
                      "San Antonio": [29.424, -98.494], "San Diego": [32.716, -117.165], "Cleveland": [41.499, -81.694],
                      "Tokyo": [35.683, 139.774], "Jakarta": [-6.214, 106.845], "Delhi": [28.666, 77.216],
                      "Manila": [14.600, 120.983], "Sao Paulo": [-23.550, -46.6339], "Seoul": [37.560, 126.990]}

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
      dict3["weathercode"][0], "\nwith a windspeed of:", my_data["current_weather"]["windspeed"], wind_cardinal)
print(f"You can expect a high of", my_data["daily"]["temperature_2m_max"][0],
      my_data["daily_units"]["temperature_2m_max"], "and a low of", my_data["daily"]["temperature_2m_min"][0],
      my_data["daily_units"]["temperature_2m_max"])
print(f"The real feel today will be between", my_data["daily"]["apparent_temperature_max"][0],
      my_data["daily_units"]["temperature_2m_max"], "and", my_data["daily"]["apparent_temperature_min"][0],
      my_data["daily_units"]["temperature_2m_max"])
