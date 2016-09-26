# Weather calendar

A simple calendar pulled from Google, using weather and forecast icons to display on an eink display 4.3" display from Waveshare. It will work on Micropython, and may work on other CPython implementations. I used a WiPy 2.0 from Pycom.io.

To use, create the file __config.json__ from the template __config.json.template__ and replace the example values.

Access to weather and calendar information are taken from Open Weather Map (http://openweathermap.org) and Google Calendar, both of which need API keys. These are held in the config.json file and not uploaded to this Github repository. You should edit this file to add the needed information. Icons are taken from The Noun Project (https://thenounproject.com/) and I have used the weather icons from artist 'Per'.
