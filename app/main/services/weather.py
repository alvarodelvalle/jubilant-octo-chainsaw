import os
import json

import zipcodes

from werkzeug.exceptions import BadRequest, NotFound, InternalServerError
from darksky.api import DarkSky, DarkSkyAsync
from darksky.types import languages, units, weather


class Weather(object):
    """Class that gets the weather forecast"""
    def get_forecast(self, zipcode, units):
        u"""Get the current temperature in specified units and description(eg:'clear')"""
        api_key = os.getenv('SKIES_API_KEY')
        # zipcode param may be passed as an invalid format
        try:
            lat_long = zipcodes.matching(zipcode)
        except ValueError as err:
            raise BadRequest(err)

        # zipcode can be passed as 00000 or 00000-0000
        try:
            latitude = lat_long[0].get('lat')
            longitude = lat_long[0].get('long')
        except IndexError as e:
            raise BadRequest(e)
        
        darksky = DarkSky(api_key)
        
        dark_forecast = darksky.get_forecast(
        latitude, longitude, 
        exclude=[weather.MINUTELY, weather.ALERTS]
        )
        converted_temp = self.temp_convert(dark_forecast.currently.temperature, units)
        forecast = {'temperature': converted_temp, 'description': dark_forecast.currently.summary}
        return forecast

    def temp_convert(self, current_temp, units):
        """Convert the temperature from F to K or C"""
        switcher = {
            'k': ((current_temp - 32) * 5.0/9.0) + 273.15,
            'c': (current_temp - 32) * 5.0/9.0,
            'f': current_temp
        }
        temperature = switcher.get(units.lower())
        return temperature

    def __init__(self):
        self.name='weather'