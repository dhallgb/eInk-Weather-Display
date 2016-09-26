# Weather calendar

A simple calendar pulled from Google, using weather and forecast icons to display on an eink display from Waveshare. It uses the library dhallgb/eInk. It will work on Micropython, and should work on other CPython implementations.

To use, create the file __config.json__ from the template __config.json.template__ and replace the example values.

This is a calendar and weather display using the Waveshare 4.3inch e-ink/e-paper display.

1. Adafruit Feather Huzzah
2. Waveshare 4.3inch e-Paper display

Access to weather and calendar information are taken from Open Weather Map (http://openweathermap.org) and Google Calendar, both of which need API keys. These are held in the config.ino file and not uploaded to this Github repository. You should edit this file to add the needed information.

Icons are taken from The Noun Project (https://thenounproject.com/) and I have used the weather icons from artist 'Per'.




