from dotenv import load_dotenv
from pprint import pprint
import os
import requests

"""load api key"""
load_dotenv()


"""request data from api"""
def get_current_weather(city='Dallas'):

    request_url = f'http://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=imperial'
   
    weather_data = requests.get(request_url).json()
    # pprint(weather_data)

    return weather_data

"""modulize this file"""
"""If called directly from this file, use terminal for variable inputs"""

if __name__ == "__main__":
    print('\n*** Get Current Weather Conditions ***\n')

    city = input("Please enter a city name:\n")

    if city: 
        weather_data = get_current_weather(city)
    else:
        weather_data = get_current_weather()

    print()
    pprint(weather_data['main']['feels_like'])