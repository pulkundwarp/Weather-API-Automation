import requests    # Request for getting some type of data

# Pulling the current weather with input of city state and country codes

API_KEY = "~insert your own Weather API Key~"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# If a combination of city and country code is entered which does not actually exist, it will give an error message
city = input("Enter a city name: ")
country = input("Enter a country code: ")

request_url = f"{BASE_URL}?appid={API_KEY}&q={city},{country}"

response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = round(data['main']['temp'] - 273.15, 2)
    
    print("Weather: ", weather)
    print("Temperature: ", temperature, " Degree celsius")
else:
    print("An error occured")


# Sample input/output    
# > python weather.py
# Enter a city name: Paris
# Enter a country code: US
# Weather:  overcast clouds
# Temperature:  10.96  Degree celsius
