#!/usr/bin/env python
#
# e-ink weather display
# Client code to subscribe to weather service topic and display. 
#
from eInk import *
from umqtt.simple import MQTTClient
from weathericons import interpret_icons
import gc
import time
CONFIG = 'config.json'
service = 'weatherunderground'
Tx='G12'
Rx='G13'
uartnum=1


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

def weather_msg(topic, msg):
    print((topic, msg))

def main(server="lonna"):
    setup()
    draw_structure()
    c = MQTTClient("eink_display", server)
    c.set_callback(weather_msg)
    c.connect()
    c.subscribe(b"raw/weather")
    while True:
        gc.collect()
        w=get_weather(service)
        v=interpret_icons(service,str(w[5]))
        print(w)
        eink_set_en_font(ASCII32)
        eink_disp_string(v["label"], 50, 250)
        eink_disp_bitmap(v["icon"]+'.BMP', 100, 100)
        eink_set_en_font(ASCII64)
        eink_disp_string(str(w[0]), 100, 350)
        for i in range(1,4):
            y = ((i*2)-1)*100
            eink_disp_string(w[6][i]["low"],400,y)
            eink_disp_string(w[6][i]["high"],600,y)
        eink_update()
        sleep(55)
        if True:
            c.wait_msg()
        else:
            c.check_msg()
            time.sleep(55)
    c.disconnect()

main()
