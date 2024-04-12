from flask import Flask, request, jsonify
import os
import requests

app = Flask(__name__)

@app.route('/')
def get_weather():
    lat_str = request.args.get('lat')
    lon_str = request.args.get('lon')
    api_key = os.getenv('API_KEY')
    
    if lat_str is not None and lon_str is not None:
        try:
            latitude = float(lat_str)
            longitude = float(lon_str)

            url = f"http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}"
            response = requests.get(url)
            data = response.json()

            coord = data['coord']
            weather = data['weather'][0]
            main = data['main']
            wind = data['wind']
            sys = data['sys']

            weather_info = {
                "coordinates": {"longitude": coord['lon'], "latitude": coord['lat']},
                "description": weather['description'],
                "temperature": main['temp'],
                "wind_speed": wind['speed'],
                "pressure": main['pressure'],
                "humidity": main['humidity'],
                "country": sys['country']
            }
            return jsonify(weather_info)
        except ValueError:
            return "Les valeurs de latitude et de longitude ne sont pas valides.", 400
    else:
        return "Les variables d'environnement LAT et LONG ne sont pas définies.", 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8081)
