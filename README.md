#Etape suivi :

Création du code

##Test du code et de l'API : 

Initialiser les valeurs :

```
set LAT=5.902785
set LONG=102.754175
set API_KEY=29ebece2943379cab1c8a846b5fc2c97
```
Executer le code :
```
python meteo.py
```
Résultat :
```
Coordonnées : longitude 102.7542, latitude 5.9028
Météo : overcast clouds
Température : 301.8 Kelvin
Vitesse du vent : 6.33 m/s
Pression atmosphérique : 1012 hPa
Humidité : 78%
Pays : MY
```

##Pour créer l'image docker :
```
docker build -t my_weather_api .
```

On peut tester le code en faisant la comande suivante :
```
docker run --env LAT=5.902785 --env LONG=102.754175 --env API_KEY="29ebece2943379cab1c8a846b5fc2c97" my_weather_api
```

Pour push l'image sur dockerhub :
```
docker tag my_weather_api corentin339/20210101
```
Ensuite, je suis allé sur docker desktop, appuyé sur les trois petits points à côté de l'image créée et appuyé sur "Push to Hub".

##Pour l'installer, vous devez faire :
```
docker pull corentin332/20210101
docker run --env LAT=5.902785 --env LONG=102.754175 --env API_KEY="your_key" my_weather_api
```
Ne pas oublier de changer "your_key" par votre clé
