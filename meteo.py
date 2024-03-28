import os
import requests

def get_weather(lat, lon):
    api_key = os.getenv('API_KEY')
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    return data

if __name__ == "__main__":
    latitude = float(os.getenv('LAT'))
    longitude = float(os.getenv('LONG'))
    weather_data = get_weather(latitude, longitude)
    print(weather_data)
