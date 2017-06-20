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
Tx='G12'
Rx='G13'
server='lonna'
service='wunderground'
uartnum=1

def setup():
    eink_init()
    eink_clear()
    eink_draw_line(300,0,300,599)
    eink_draw_line(300,200,799,200)
    eink_draw_line(300,400,799,400)
    eink_update()

def weather_msg(topic, msg):
    v=interpret_icons(service,str(msg[5]))
    print(msg)
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

def main():
    setup()
    c = MQTTClient("eink_display", server)
    c.set_callback(weather_msg)
    c.connect()
    c.subscribe(b"raw/weather")
    while True:
        gc.collect()
        if True:
            c.wait_msg()
        else:
            c.check_msg()
            time.sleep(55)
    c.disconnect()

main()
