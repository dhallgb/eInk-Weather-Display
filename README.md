# Weather calendar

A simple weather display using weather and forecast icons to display on an Waveshare epaper 4.3" display. It will work on Micropython, and may work on CPython implementations if you use another library. This uses the eInk library from https://github.com/dhallgb/eInk-micropython. Icons are taken from The Noun Project (https://thenounproject.com/), and I have used the weather icons from artist 'Per'. I have implemented the Weather Underground and Open Weather Map services, pull offers to add others gratefully received.

## Requirements
* NodeRED running on server
* microprocessor running MicroPython
* NodeRED nodes node-red-contrib-config, or alternate way of setting flow context variables (you could use a function node, for example)

## Components
* NodeRED flow publishing to MQTT topic
* embedded microprocessor driving Waveshare e-ink display, such as the ESP8266 or WiPy2

## Installation
1. create accounts on the weather service you wish to use, and generate API keys
1. create the file __config.json__ from the template __config.json.template__ and replace the example values for your selected weather service. 
1. install the __weather-config.html/js__ files into your NodeRED node directory
1. install the e-ink library, and device.py code on your device

## Usage
1. trigger the NodeRED flow using whatever method you wish, perhaps using the *inject* node on interval
1. run the device code, it will loop and sleep 
