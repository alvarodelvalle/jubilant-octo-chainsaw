import os
import json

import zipcodes
from darksky.api import DarkSky, DarkSkyAsync
from darksky.types import languages, units, weather


class Weather(object):
    def __init__(self):
        self.name='weather'

    def get_forecast(self, zipcode, units):
        api_key = os.getenv('SKIES_API_KEY')
        lat_long = zipcodes.matching(zipcode)
        latitude = lat_long[0].get('lat')
        longitude = lat_long[0].get('long')
        
        darksky = DarkSky(api_key)
        
        response = darksky.get_forecast(
        latitude, longitude, 
        exclude=[weather.MINUTELY, weather.ALERTS]
        )
        # TODO: update response with correct temperature given the units requested
        return response