import requests    # Request for getting some type of data

# Pulling the current weather with input of city state and country codes

API_KEY = "~insert your own Weather API Key~"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
state = input("Enter a state code: ")
country = input("Enter a country code: ")

request_url = f"{BASE_URL}?appid={API_KEY}&q={city},{state},{country}"

response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = round(data['main']['temp'] - 273.15, 2)
    
    print("Weather: ", weather)
    print("Temperature: ", temperature, " Degree Celsius")
else:
    print("An error occured")


# Sample input/output    
# > python weather.py
# Enter a city name: paris
# Enter a state code: tx
# Enter a country code: us
# Weather:  overcast clouds
# Temperature:  10.96  Degree Celsius
