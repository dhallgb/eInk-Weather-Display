# Weather calendar

A simple weather board using weather and forecast icons to display on an Waveshare epaper 4.3" display. It will work on Micropython, and may work on CPython implementations if you use another library. This uses the eInk library from https://github.com/dhallgb/eInk-micropython

To use, create the file __config.json__ from the template __config.json.template__ and replace the example values for your selected weather service and Google Calendar, both of which need API keys. I have implemented the Weather Underground and Open Weather Map services, pull offers to add others gratefully received.

Icons are taken from The Noun Project (https://thenounproject.com/), and I have used the weather icons from artist 'Per'.

Requires urequests module https://github.com/micropython/micropython-lib/blob/master/urequests/urequests.py
