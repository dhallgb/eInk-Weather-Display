#!/usr/bin/env python
#
# e-ink weather display
# Client code to subscribe to weather service MQTT topic, and display. 
#
from eInk import *
from umqtt import *
from weathericons import interpret_icons
import pycom
import gc
import ujson
import time
Tx='G12'
Rx='G13'
server='lonna'
service='weatherunderground'
uartnum=1
pycom.heartbeat(False)

def setup():
    eink_init()
    eink_clear()
    eink_draw_line(300,0,300,599)
    eink_draw_line(300,200,799,200)
    eink_draw_line(300,400,799,400)
    eink_update()

def weather_msg(topic, msg):
    pycom.rgbled(0x007f00)
    pycom.rgbled(0x000000)
    weather=ujson.loads(msg)
    print(weather["description"])
    icon=interpret_icons(service,weather["iconid"])
    eink_set_en_font(ASCII32)
    eink_disp_string(icon["label"], 50, 250)
    eink_disp_bitmap(icon["icon"]+'.BMP', 100, 100)
    eink_set_en_font(ASCII64)
    eink_disp_string(str(weather["temperature"]), 100, 350)
    for i in range(1,4):
        y = ((i*2)-1)*100
        eink_disp_string(str(weather["forecast"][i]["low"]),400,y)
        eink_disp_string(str(weather["forecast"][i]["high"]),600,y)
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
            print("one>>",gc.free())
            c.wait_msg()
        else:
            print("two>>",gc.free())
            c.check_msg()
            time.sleep(55)
    c.disconnect()

main()
