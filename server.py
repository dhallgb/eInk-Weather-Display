#!/usr/bin/env python
#
# Minimal weather calendar for the Waveshare 4.3 inch e-ink display
# Server component
#
# Gets the weather data from various weather services.
#
from time import sleep
import json
import requests
CONFIG = 'config.json'
service = 'weatherunderground'

def setup():
    global cfg
    f = open(CONFIG, 'r')
    x = f.readall()
    cfg = json.loads(x)

def get_weather(service):
#
#   Get weather conditions and forecast using API call and REST call.
#   Returned formats are different between services, hence this routine.
#
    if service == "openweathermap":
        pt1 = "http://api.openweathermap.org/data/2.5/weather?id="
        pt2 = "&units=metric&cnt=3&appid="
        url = pt1+cfg["Openweathercity"]+pt2+cfg["OpenWeatherAPI"]
        r = requests.get(url)
        weather_json = r.json()
        r.close()
        temp = round(weather_json["main"]["temp"])
        wind = round(weather_json["wind"]["speed"])
        humidity = weather_json["main"]["humidity"]
        description = weather_json["weather"][0]["description"]
        pressure = weather_json["main"]["pressure"]
        iconid = weather_json["weather"][0]["id"]
    elif service == "weatherunderground":
        pt1 = "http://api.wunderground.com/api/"
        pt2 = "/forecast/conditions/q/"
        url = pt1+cfg["WundergroundAPI"]+pt2+cfg["WundergroundCity"]+".json"
        r = requests.get(url)
        weather_json = r.json()
        r.close()
        temperature = weather_json["current_observation"]["temp_c"]
        wind = weather_json["current_observation"]["wind_kph"]
        humidity = weather_json["current_observation"]["relative_humidity"]
        description = weather_json["current_observation"]["weather"]
        pressure = weather_json["current_observation"]["pressure_mb"]
        iconid = weather_json["current_observation"]["icon"]
        forecast = {}
        for i in range(1,4):
            forecast[i] = {}
            forecast[i]["high"] = weather_json["forecast"]["simpleforecast"]["forecastday"][i]["high"]["celsius"]
            forecast[i]["low"]  = weather_json["forecast"]["simpleforecast"]["forecastday"][i]["low"]["celsius"]
    else:
        print("Error: invalid service selected")
    return(temperature, wind, humidity, description, pressure, iconid, forecast)

def main():
    setup()
    while True:
        w=get_weather(service)
        v=interpret_icons(service,str(w[5]))
        print(w)
        sleep(55)

main()
