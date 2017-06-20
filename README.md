# Weather calendar

A simple weather display using weather and forecast icons to display on an Waveshare epaper 4.3" display. It will work on Micropython, and may work on CPython implementations if you use another library. This uses the eInk library from https://github.com/dhallgb/eInk-micropython. Icons are taken from The Noun Project (https://thenounproject.com/), and I have used the weather icons from artist 'Per'. I have implemented the Weather Underground and Open Weather Map services, pull offers to add others gratefully received.

## Components
* server component running on NodeRED on server such as Raspberry Pi or Odroid
* embedded microprocessor driving Waveshare e-ink display, such as the ESP8266 or WiPy2

## Installation
1. Create accounts on the weather service you wish to use, and generate API keys.
1. create the file __config.json__ from the template __config.json.template__ and replace the example values for your selected weather service. 
1. put the config.sys into your NodeRED data directory
1. put the config.sys file onto your embedded device
1. 

## Usage
1. run the server component on your host platform on a regular basis, perhaps using either NodeRED or cron jobs

