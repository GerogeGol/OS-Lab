#!/usr/bin/python
import geocoder
import json
import requests
import sys


API_KEY = "d42027c53bdcc122e7f74bcc8f84a5ef"
g = geocoder.ip("me")
lat = g.latlng[0]
lon = g.latlng[1]


url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={API_KEY}"

req = requests.get(url=url)
data = req.json()
info = f"City: {data['name']}.\n\
    Weather: \n\
        Main: {data['weather'][0]['main']}\n\
        Description: {data['weather'][0]['description']}\n\
        Temperature: {data['main']['temp']}℃ \n\
        Feels Like: {data['main']['feels_like']}℃\n"

if len(sys.argv) >= 2:
    with open(sys.argv[1], "w") as f:
        f.write(info)
else:
    print(info)
