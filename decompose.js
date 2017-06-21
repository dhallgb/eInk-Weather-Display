//
//   Returned formats are different between services, hence this routine.
//
var fs = require('fs');
var contents = fs.readFileSync('weather.json', 'utf8');
var weather_json = JSON.parse(contents);
// service = flow.get('service')||0;
service = "weatherunderground";
var result = {
	forecast: []
	};
switch (service) {
/*	case "openweathermap":
        result.temperature 	= weather_json.main.temp;
        result.wind 		= weather_json.wind.speed;
        result.humidity 	= weather_json.main.humidity;
        result.description 	= weather_json.weather.[0].description;
        result.pressure 	= weather_json.main.pressure;
        result.iconid 		= weather_json.weather.[0].id;
        break;
*/
    case "weatherunderground":
        result.temperature 	= weather_json.current_observation.temp_c;
        result.wind 		= weather_json.current_observation.wind_kph;
        result.humidity 	= weather_json.current_observation.relative_humidity;
        result.description 	= weather_json.current_observation.weather;
        result.pressure 	= weather_json.current_observation.pressure_mb;
        result.iconid 		= weather_json.current_observation.icon;
		for (var i in weather_json.forecast.simpleforecast.forecastday) {    
		    var item = weather_json.forecast.simpleforecast.forecastday[i];   
			result.forecast.push({ 
        		"high" : item.high.celsius,
        		"low"  : item.low.celsius
    			});
			}
        break;
    default:
        console.log("Error: invalid service selected");
	}
console.log(result);
//return msg.payload;
//require('make-runnable');
