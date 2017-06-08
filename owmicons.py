#!/usr/bin/env python
#
# Interpret OpenWeatherMap codes as icons
#
def interpret_icons(id):
    icons = {
    "200": {
    "label": "thunderstorm with light rain",
    "icon": "RAIN"
    },

    "201": {
    "label": "thunderstorm with rain",
    "icon": "RAIN"
    },

    "202": {
    "label": "thunderstorm with heavy rain",
    "icon": "RAIN"
    },

    "210": {
    "label": "light thunderstorm",
    "icon": "RAIN"
    },

    "211": {
    "label": "thunderstorm",
    "icon": "RAIN"
    },

    "212": {
    "label": "heavy thunderstorm",
    "icon": "RAIN"
    },

    "221": {
    "label": "ragged thunderstorm",
    "icon": "RAIN"
    },

    "230": {
    "label": "thunderstorm with light drizzle",
    "icon": "RAIN"
    },

    "231": {
    "label": "thunderstorm with drizzle",
    "icon": "RAIN"
    },

    "232": {
    "label": "thunderstorm with heavy drizzle",
    "icon": "RAIN"
    },

    "300": {
    "label": "light intensity drizzle",
    "icon": "RAIN"
    },

    "301": {
    "label": "drizzle",
    "icon": "RAIN"
    },

    "302": {
    "label": "heavy intensity drizzle",
    "icon": "RAIN"
    },

    "310": {
    "label": "light intensity drizzle rain",
    "icon": "RAIN"
    },

    "311": {
    "label": "drizzle rain",
    "icon": "RAIN"
    },

    "312": {
    "label": "heavy intensity drizzle rain",
    "icon": "RAIN"
    },

    "313": {
    "label": "shower rain and drizzle",
    "icon": "RAIN"
    },

    "314": {
    "label": "heavy shower rain and drizzle",
    "icon": "RAIN"
    },

    "321": {
    "label": "shower drizzle",
    "icon": "RAIN"
    },

    "500": {
    "label": "light rain",
    "icon": "RAIN"
    },

    "501": {
    "label": "moderate rain",
    "icon": "RAIN"
    },

    "502": {
    "label": "heavy intensity rain",
    "icon": "RAIN"
    },

    "503": {
    "label": "very heavy rain",
    "icon": "RAIN"
    },

    "504": {
    "label": "extreme rain",
    "icon": "RAIN"
    },

    "511": {
    "label": "freezing rain",
    "icon": "RAIN"
    },

    "520": {
    "label": "light intensity shower rain",
    "icon": "RAIN"
    },

    "521": {
    "label": "shower rain",
    "icon": "RAIN"
    },

    "522": {
    "label": "heavy intensity shower rain",
    "icon": "RAIN"
    },

    "531": {
    "label": "ragged shower rain",
    "icon": "RAIN"
    },

    "600": {
    "label": "light snow",
    "icon": "RAIN"
    },

    "601": {
    "label": "snow",
    "icon": "RAIN"
    },

    "602": {
    "label": "heavy snow",
    "icon": "RAIN"
    },

    "611": {
    "label": "sleet",
    "icon": "RAIN"
    },

    "612": {
    "label": "shower sleet",
    "icon": "RAIN"
    },

    "615": {
    "label": "light rain and snow",
    "icon": "RAIN"
    },

    "616": {
    "label": "rain and snow",
    "icon": "RAIN"
    },

    "620": {
    "label": "light shower snow",
    "icon": "RAIN"
    },

    "621": {
    "label": "shower snow",
    "icon": "RAIN"
    },

    "622": {
    "label": "heavy shower snow",
    "icon": "RAIN"
    },

    "701": {
    "label": "mist",
    "icon": "RAIN"
    },

    "711": {
    "label": "smoke",
    "icon": "CLOUD"
    },

    "721": {
    "label": "haze",
    "icon": "MOST"
    },

    "731": {
    "label": "sand, dust whirls",
    "icon": "MOST"
    },

    "741": {
    "label": "fog",
    "icon": "MOST"
    },

    "751": {
    "label": "sand",
    "icon": "MOST"
    },

    "761": {
    "label": "dust",
    "icon": "MOST"
    },

    "762": {
    "label": "volcanic ash",
    "icon": "MOST"
    },

    "771": {
    "label": "squalls",
    "icon": "MIXED"
    },

    "781": {
    "label": "tornado",
    "icon": "MIXED"
    },

    "800": {
    "label": "clear sky",
    "icon": "SUN"
    },

    "801": {
    "label": "few clouds",
    "icon": "CLOUD"
    },

    "802": {
    "label": "scattered clouds",
    "icon": "MOST"
    },

    "803": {
    "label": "broken clouds",
    "icon": "MOST"
    },

    "804": {
    "label": "overcast clouds",
    "icon": "CLOUD"
    },


    "900": {
    "label": "tornado",
    "icon": "MIXED"
    },

    "901": {
    "label": "tropical storm",
    "icon": "MIXED"
    },

    "902": {
    "label": "hurricane",
    "icon": "MIXED"
    },

    "903": {
    "label": "cold",
    "icon": "MIXED"
    },

    "904": {
    "label": "hot",
    "icon": "SUN"
    },

    "905": {
    "label": "windy",
    "icon": "MIXED"
    },

    "906": {
    "label": "hail",
    "icon": "MIXED"
    },

    "951": {
    "label": "calm",
    "icon": "SUN"
    },

    "952": {
    "label": "light breeze",
    "icon": "MIXED"
    },

    "953": {
    "label": "gentle breeze",
    "icon": "MIXED"
    },

    "954": {
    "label": "moderate breeze",
    "icon": "MIXED"
    },

    "955": {
    "label": "fresh breeze",
    "icon": "MIXED"
    },

    "956": {
    "label": "strong breeze",
    "icon": "MIXED"
    },

    "957": {
    "label": "high wind, near gale",
    "icon": "MIXED"
    },

    "958": {
    "label": "gale",
    "icon": "MIXED"
    },

    "959": {
    "label": "severe gale",
    "icon": "MIXED"
    },

    "960": {
    "label": "storm",
    "icon": "MIXED"
    },

    "961": {
    "label": "violent storm",
    "icon": "MIXED"
    },

    "962": {
    "label": "hurricane",
    "icon": "MIXED"
    }
    }
    return(icons[id])
