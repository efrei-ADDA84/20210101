# TP1

(hash correspondant à la dernier version du TP1 : d9fa6b031b40db7192aef090e58083f921e8fa0f)

## Etape suivi :

Création du code

## Test du code et de l'API : 

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

## Pour créer l'image docker :
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

## Pour l'installer, vous devez faire :
```
docker pull corentin332/20210101
docker run --env LAT=5.902785 --env LONG=102.754175 --env API_KEY="your_key" my_weather_api
```
Ne pas oublier de changer "your_key" par votre clé

# TP2

## Etape suivi :

Modification des fichiers meteo.py et Dockerfile.
Création du fichier "docker_build_push.yaml" qui va automatiquement mettre à jour l'image docker dès que nous faisons un push sur github.

## Test de l'API

Dans un CMD, executez ce code en changeant l'API_KEY par votre numéro d'API_KEY
```docker run -p 8081:8081 --env API_KEY=29ebece2943379cab1c8a846b5fc2c97 corentin339/20210101:latest```

Dans un autre CMD, executez ce code :
```curl "http://localhost:8081/?lat=5.902785&lon=102.754175"```

On obtient le résultat suivant :
```{"coordinates":{"latitude":5.9028,"longitude":102.7542},"country":"MY","description":"overcast clouds","humidity":73,"pressure":1008,"temperature":302.41,"wind_speed":5.47}```
