# Weather calendar

A simple weather display using weather and forecast icons to display on an Waveshare epaper 4.3" display. It will work on Micropython, and may work on CPython implementations if you use another library. This uses the eInk library from https://github.com/dhallgb/eInk-micropython. Icons are taken from The Noun Project (https://thenounproject.com/), and I have used the weather icons from artist 'Per'.

## Components
 server component running on another full CPython implementation such as a home Raspberry Pi or Odroid single-board computer
 embedded microprocessor driving e-ink such as the ESP8266 or Pycom WiPy2

## To Use
1. Create accounts on the weather service you wish to use, and generate API keys.
1. create the file __config.json__ from the template __config.json.template__ and replace the example values for your selected weather service. I have implemented the Weather Underground and Open Weather Map services, pull offers to add others gratefully received.
1. run the server component on your host platform on a regular basis, perhaps using either NodeRED or cron jobs
