#!/usr/bin/env python
#
# Minimal weather calendar for the Waveshare 4.3 inch e-ink display
# Gets the weather data from OpenWeatherMap, and calendar data from Google.
#
# Note: this was attempted on a WiPy 1.0, but due to the lack of floats, decimals and math library it
# was difficult to make it work. This runs on the WiPy 2.0.
#
from eInk import *
from time import sleep
import ujson
import usocket
Tx='G12'
Rx='G13'
uartnum=1

CONFIG = 'config.json'

def parseFloat(f):
    return(int(f.split('.')[0]))

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
    eink_draw_line(300,100,799,100)
    eink_draw_line(300,200,799,200)
    eink_draw_line(300,300,799,300)
    eink_draw_line(300,400,799,400)
    eink_draw_line(300,500,799,500)
    eink_update()

def interpret_icons(id):
    icons = {
    "200": {
    "label": "thunderstorm with light rain",
    "icon": "RAIN"
    },

    "201": {
    "label": "thunderstorm with rain",
    "icon": "RAIN"
    },

    "202": {
    "label": "thunderstorm with heavy rain",
    "icon": "RAIN"
    },

    "210": {
    "label": "light thunderstorm",
    "icon": "RAIN"
    },

    "211": {
    "label": "thunderstorm",
    "icon": "RAIN"
    },

    "212": {
    "label": "heavy thunderstorm",
    "icon": "RAIN"
    },

    "221": {
    "label": "ragged thunderstorm",
    "icon": "RAIN"
    },

    "230": {
    "label": "thunderstorm with light drizzle",
    "icon": "RAIN"
    },

    "231": {
    "label": "thunderstorm with drizzle",
    "icon": "RAIN"
    },

    "232": {
    "label": "thunderstorm with heavy drizzle",
    "icon": "RAIN"
    },

    "300": {
    "label": "light intensity drizzle",
    "icon": "RAIN"
    },

    "301": {
    "label": "drizzle",
    "icon": "RAIN"
    },

    "302": {
    "label": "heavy intensity drizzle",
    "icon": "RAIN"
    },

    "310": {
    "label": "light intensity drizzle rain",
    "icon": "RAIN"
    },

    "311": {
    "label": "drizzle rain",
    "icon": "RAIN"
    },

    "312": {
    "label": "heavy intensity drizzle rain",
    "icon": "RAIN"
    },

    "313": {
    "label": "shower rain and drizzle",
    "icon": "RAIN"
    },

    "314": {
    "label": "heavy shower rain and drizzle",
    "icon": "RAIN"
    },

    "321": {
    "label": "shower drizzle",
    "icon": "RAIN"
    },

    "500": {
    "label": "light rain",
    "icon": "RAIN"
    },

    "501": {
    "label": "moderate rain",
    "icon": "RAIN"
    },

    "502": {
    "label": "heavy intensity rain",
    "icon": "RAIN"
    },

    "503": {
    "label": "very heavy rain",
    "icon": "RAIN"
    },

    "504": {
    "label": "extreme rain",
    "icon": "RAIN"
    },

    "511": {
    "label": "freezing rain",
    "icon": "RAIN"
    },

    "520": {
    "label": "light intensity shower rain",
    "icon": "RAIN"
    },

    "521": {
    "label": "shower rain",
    "icon": "RAIN"
    },

    "522": {
    "label": "heavy intensity shower rain",
    "icon": "RAIN"
    },

    "531": {
    "label": "ragged shower rain",
    "icon": "RAIN"
    },

    "600": {
    "label": "light snow",
    "icon": "RAIN"
    },

    "601": {
    "label": "snow",
    "icon": "RAIN"
    },

    "602": {
    "label": "heavy snow",
    "icon": "RAIN"
    },

    "611": {
    "label": "sleet",
    "icon": "RAIN"
    },

    "612": {
    "label": "shower sleet",
    "icon": "RAIN"
    },

    "615": {
    "label": "light rain and snow",
    "icon": "RAIN"
    },

    "616": {
    "label": "rain and snow",
    "icon": "RAIN"
    },

    "620": {
    "label": "light shower snow",
    "icon": "RAIN"
    },

    "621": {
    "label": "shower snow",
    "icon": "RAIN"
    },

    "622": {
    "label": "heavy shower snow",
    "icon": "RAIN"
    },

    "701": {
    "label": "mist",
    "icon": "RAIN"
    },

    "711": {
    "label": "smoke",
    "icon": "CLOUD"
    },

    "721": {
    "label": "haze",
    "icon": "MOST"
    },

    "731": {
    "label": "sand, dust whirls",
    "icon": "MOST"
    },

    "741": {
    "label": "fog",
    "icon": "MOST"
    },

    "751": {
    "label": "sand",
    "icon": "MOST"
    },

    "761": {
    "label": "dust",
    "icon": "MOST"
    },

    "762": {
    "label": "volcanic ash",
    "icon": "MOST"
    },

    "771": {
    "label": "squalls",
    "icon": "MIXED"
    },

    "781": {
    "label": "tornado",
    "icon": "MIXED"
    },

    "800": {
    "label": "clear sky",
    "icon": "SUN"
    },

    "801": {
    "label": "few clouds",
    "icon": "CLOUD"
    },

    "802": {
    "label": "scattered clouds",
    "icon": "MOST"
    },

    "803": {
    "label": "broken clouds",
    "icon": "MOST"
    },

    "804": {
    "label": "overcast clouds",
    "icon": "CLOUD"
    },


    "900": {
    "label": "tornado",
    "icon": "MIXED"
    },

    "901": {
    "label": "tropical storm",
    "icon": "MIXED"
    },

    "902": {
    "label": "hurricane",
    "icon": "MIXED"
    },

    "903": {
    "label": "cold",
    "icon": "MIXED"
    },

    "904": {
    "label": "hot",
    "icon": "SUN"
    },

    "905": {
    "label": "windy",
    "icon": "MIXED"
    },

    "906": {
    "label": "hail",
    "icon": "MIXED"
    },

    "951": {
    "label": "calm",
    "icon": "SUN"
    },

    "952": {
    "label": "light breeze",
    "icon": "MIXED"
    },

    "953": {
    "label": "gentle breeze",
    "icon": "MIXED"
    },

    "954": {
    "label": "moderate breeze",
    "icon": "MIXED"
    },

    "955": {
    "label": "fresh breeze",
    "icon": "MIXED"
    },

    "956": {
    "label": "strong breeze",
    "icon": "MIXED"
    },

    "957": {
    "label": "high wind, near gale",
    "icon": "MIXED"
    },

    "958": {
    "label": "gale",
    "icon": "MIXED"
    },

    "959": {
    "label": "severe gale",
    "icon": "MIXED"
    },

    "960": {
    "label": "storm",
    "icon": "MIXED"
    },

    "961": {
    "label": "violent storm",
    "icon": "MIXED"
    },

    "962": {
    "label": "hurricane",
    "icon": "MIXED"
    }
    }
    return(icons[id])

def get_weather():
    pt1 = "http://api.openweathermap.org/data/2.5/weather?id="
    pt2 = "&units=metric&cnt=3&appid="
    url = pt1+cfg["Openweathercity"]+pt2+cfg["OpenWeatherAPI"]
    req = urlopen(url)
    ret = req.read()
    print(ret)
    weather = ret.decode("utf-8")
    #    weather_json = ujson.loads(weather, parse_float=parseFloat)
    weather_json = ujson.loads(weather)
    temp = round(weather_json["main"]["temp"])
    wind = round(weather_json["wind"]["speed"])
    humidity = weather_json["main"]["humidity"]
    description = weather_json["weather"][0]["description"]
    pressure = weather_json["main"]["pressure"]
    iconid = weather_json["weather"][0]["id"]
    #   
    #   Content handlers don't appear to work in ujson. So we mung them.
    #    temp = mungWeather(weather, '"temp":')
    #    wind = mungWeather(weather, '"speed":')
    #    humidity = mungWeather(weather, '"humidity":',',')
    #    description = mungWeather(weather, '"description":',',')
    #    pressure = mungWeather(weather, '"pressure":')
    return(temp, wind, humidity, description, pressure, iconid)

def get_calendar():
    pass

if __name__=="__main__":
    setup()
    draw_structure()
    w=get_weather()
    v=interpret_icons(str(w[5]))
    eink_set_en_font(ASCII32)
    eink_disp_string(v["label"], 50, 250)
    eink_disp_bitmap(v["icon"]+'.BMP', 100, 100)
    eink_set_en_font(ASCII64)
    eink_disp_string(str(w[0]), 100, 350)
    eink_update()
