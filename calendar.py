#!/usr/bin/env python
#
# Minimal weather calendar for the Waveshare 4.3 inch e-ink display
# This runs on the WiPy 2.0; floats will not work on the WiPy 1.0. 
# May work on other mPython boards.
#
# Gets the weather data from various weather services.
# TBD: get calendar data from Google.
#
from eInk import *
from time import sleep
from weathericons import interpret_icons
import machine
import urequests as requests
CONFIG = 'config.json'
service = 'weatherunderground'
Tx='G12'
Rx='G13'
uartnum=1

def parseFloat(f):
    return(int(f.split('.')[0]))

#def urlopen(url, data=None, method="GET"):
    if data is not None and method == "GET":
        method = "POST"
    try:
        proto, dummy, host, path = url.split("/", 3)
    except ValueError:
        proto, dummy, host = url.split("/", 2)
        path = ""
    if proto == "http:":
        port = 80
    elif proto == "https:":
        import ussl
        port = 443
    else:
        raise ValueError("Unsupported protocol: " + proto)

    if ":" in host:
        host, port = host.split(":", 1)
        port = int(port)

    ai = usocket.getaddrinfo(host, port)
    addr = ai[0][4]
    s = usocket.socket()
    s.connect(addr)
    if proto == "https:":
        s = ussl.wrap_socket(s)

    s.write(method)
    s.write(b" /")
    s.write(path)
    s.write(b" HTTP/1.0\r\nHost: ")
    s.write(host)
    s.write(b"\r\n")

    if data:
        s.write(b"Content-Length: ")
        s.write(str(len(data)))
        s.write(b"\r\n")
    s.write(b"\r\n")
    if data:
        s.write(data)

    l = s.readline()
    protover, status, msg = l.split(None, 2)
    status = int(status)
    #print(protover, status, msg)
    while True:
        l = s.readline()
        if not l or l == b"\r\n":
            break
        #print(line)
        if l.startswith(b"Transfer-Encoding:"):
            if b"chunked" in line:
                raise ValueError("Unsupported " + l)
        elif l.startswith(b"Location:"):
            raise NotImplementedError("Redirects not yet supported")

    return s

def mungWeather(url,text,stop="."):
    index = url.find(text)
    index += len(text)
    index2 = url.find(stop, index)
    return(url[index:index2])

def setup():
    global cfg
    f = open(CONFIG, 'r')
    x = f.readall()
    cfg = ujson.loads(x)
    eink_init()
    eink_clear()

def draw_structure():
    eink_draw_line(300,0,300,599)
    eink_draw_line(300,200,799,200)
    eink_draw_line(300,400,799,400)
    eink_update()

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
        temperature = weather_json["current_observation"]["temp_c"]
        wind = weather_json["current_observation"]["wind_kph"]
        humidity = weather_json["current_observation"]["relative_humidity"]
        description = weather_json["current_observation"]["weather"]
        pressure = weather_json["current_observation"]["pressure_mb"]
        iconid = weather_json["current_observation"]["icon"]
        r.close()
    else:
        print("Error: invalid service selected")
    return(temperature, wind, humidity, description, pressure, iconid)

def get_calendar():
    pass

def main():
    setup()
    draw_structure()
    w=get_weather(service)
    v=interpret_icons(service,str(w[5]))
    eink_set_en_font(ASCII32)
    eink_disp_string(v["label"], 50, 250)
    eink_disp_bitmap(v["icon"]+'.BMP', 100, 100)
    eink_set_en_font(ASCII64)
    eink_disp_string(str(w[0]), 100, 350)
    eink_update()

main()
