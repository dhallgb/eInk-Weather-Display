#!/usr/bin/env python

from eInk import *
from time import sleep
import sys
import ujson
import usocket

CONFIG = 'config.json'

def urlopen(url, data=None, method="GET"):
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

def setup():
    global cfg
    f = open(CONFIG, 'r')
    x = f.readall()
    cfg = ujson.loads(x)
    eink_init()
    eink_clear()

def draw_structure():
    eink_draw_line(300,0,300,599)
    eink_draw_line(300,100,799,100)
    eink_draw_line(300,200,799,200)
    eink_draw_line(300,300,799,300)
    eink_draw_line(300,400,799,400)
    eink_draw_line(300,500,799,500)
    eink_update()

def get_weather():
    pt1 = "http://api.openweathermap.org/data/2.5/weather?id="
    pt2 = "&units=metric&appid="
    url = pt1+cfg["Openweathercity"]+pt2+cfg["OpenWeatherAPI"]
    req = urlopen(url)
    weather = req.read()
    weather_json = ujson.loads(weather.decode("utf-8"))
    print(weather_json)
    print("temp = ", round(weather_json["main"]["temp"]))
    print("wind = ", round(weather_json["wind"]["speed"]))
    print("humidity = ",weather_json["main"]["humidity"])
    print("description = ", weather_json["weather"][0]["description"])
    print("pressure = ", weather_json["main"]["pressure"])

def get_calendar():
    pass

if __name__=="__main__":
    setup()
    draw_structure()
    get_weather()
