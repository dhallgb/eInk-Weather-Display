# Weather calendar

A simple weather display using weather and forecast icons to display on an Waveshare epaper 4.3" display. It will work on Micropython, and may work on CPython implementations if you use another library.  Icons are taken from The Noun Project (https://thenounproject.com/), and I have used the weather icons from artist 'Per'. I have implemented the Weather Underground and Open Weather Map services, pull offers to add others gratefully received.

## Requirements
* NodeRED running on server
* microprocessor running MicroPython
* MQTT server

## Components
* NodeRED flow publishing to MQTT topic __raw/weather__
-- NodeRED new node __node-red-contrib-file-function__
-- NodeREd new node __node-red-contrib-config__
* embedded microprocessor driving Waveshare e-ink display, such as the ESP8266 or WiPy2
* microPython eInk library from https://github.com/dhallgb/eInk-micropython

## Installation
1. create accounts on the weather service you wish to use, and generate API keys
-- Weather Underground[https://www.wunderground.com/?apiref=95cb3adea9249d3a]
1. install the e-ink library, and device.py code on your device
1. install the new NodeRED nodes listed above

## Usage
* trigger the NodeRED flow using whatever method you wish, perhaps using the *inject* node on interval
* run the device code, it will loop and sleep
* when a new weather message is posted on the MQTT topic, the display will update
