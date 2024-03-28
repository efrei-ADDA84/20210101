import os
import requests

def get_weather(lat, lon):
    api_key = os.getenv('API_KEY')
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    return data

if __name__ == "__main__":
    lat_str = os.getenv('LAT')
    lon_str = os.getenv('LONG')

    if lat_str is not None and lon_str is not None:
        try:
            latitude = float(lat_str)
            longitude = float(lon_str)

            weather_data = get_weather(latitude, longitude)
            
            coord = weather_data['coord']
            weather = weather_data['weather'][0]
            main = weather_data['main']
            wind = weather_data['wind']
            sys = weather_data['sys']

            print(f"Coordonnées : longitude {coord['lon']}, latitude {coord['lat']}")
            print(f"Météo : {weather['description']}")
            print(f"Température : {main['temp']} Kelvin")
            print(f"Vitesse du vent : {wind['speed']} m/s")
            print(f"Pression atmosphérique : {main['pressure']} hPa")
            print(f"Humidité : {main['humidity']}%")
            print(f"Pays : {sys['country']}")
        except ValueError:
            print("Les valeurs de latitude et de longitude ne sont pas valides.")
    else:
        print("Les variables d'environnement LAT et LONG ne sont pas définies.")
