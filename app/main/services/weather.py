import os
import json

import zipcodes
from darksky.api import DarkSky, DarkSkyAsync
from darksky.types import languages, units, weather


class Weather(object):

    def get_forecast(self, zipcode, units):
        api_key = os.getenv('SKIES_API_KEY')
        lat_long = zipcodes.matching(zipcode)
        latitude = lat_long[0].get('lat')
        longitude = lat_long[0].get('long')
        
        darksky = DarkSky(api_key)
        
        dark_forecast = darksky.get_forecast(
        latitude, longitude, 
        exclude=[weather.MINUTELY, weather.ALERTS]
        )
        converted_temp = self.temp_convert(dark_forecast.currently.temperature, units)
        forecast = {'temperature': converted_temp, 'description': dark_forecast.currently.summary}
        return forecast

    def temp_convert(self, current_temp, units):
        switcher = {
            'k': ((current_temp - 32) * 5.0/9.0) + 273.15,
            'c': (current_temp - 32) * 5.0/9.0,
            'f': current_temp
        }
        temperature = switcher.get(units.lower())
        return temperature

    def __init__(self):
        self.name='weather'