//
//   Returned formats are different between services, hence this routine.
//
var fs = require('fs');
var contents = fs.readFileSync('weather.json', 'utf8');
var weather_json = JSON.parse(contents);


// service = flow.get('service')||0;
service = "weatherunderground";
switch (service) {
	case "openweathermap":
        temperature = weather_json.main.temp;
        wind 		= weather_json.wind.speed;
        humidity 	= weather_json.main.humidity;
        description = weather_json.weather.0.description;
        pressure 	= weather_json.main.pressure;
        iconid 		= weather_json.weather.0.id;
        break;
    case "weatherunderground":
        temperature = weather_json.current_observation.temp_c;
        wind 		= weather_json.current_observation.wind_kph;
        humidity 	= weather_json.current_observation.relative_humidity;
        description = weather_json.current_observation.weather;
        pressure 	= weather_json.current_observation.pressure_mb;
        iconid 		= weather_json.current_observation.icon;
        var forecast = [];
        for (var i = 0; 4; i++) {
            forecast.i.high = weather_json.forecast.simpleforecast.forecastday.i.high.celsius;
            forecast.i.low  = weather_json.forecast.simpleforecast.forecastday.i.low.celsius;;
        	}
        break;
    default:
        console.log("Error: invalid service selected");
	}
/*
weather_json=(temperature, wind, humidity, description, pressure, iconid, forecast);
return weather_json;
*/
require('make-runnable');
