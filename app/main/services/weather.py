import os
import json
from darksky.api import DarkSky, DarkSkyAsync
from darksky.types import languages, units, weather


class Weather(object):
    def __init__(self):
        self.name='weather'

    def get_forecast(self):
        api_key = os.getenv('SKIES_API_KEY')
        latitude = 43.073051
        longitude = -89.401230
        darksky = DarkSky(api_key)
        response = darksky.get_forecast(
        latitude, longitude, extend=False, # default `False`
        lang=languages.ENGLISH, # default `ENGLISH`
        units=units.AUTO, # default `auto`
        exclude=[weather.MINUTELY, weather.ALERTS] # default `[]`
        )
        return response

    # def get_lat_long():
    # # use query params from api request to figure out lat and long; return dictionary
    # # TODO - take zip code from api request and use a library to get the lat+long - AD 2019-10-12
    # lat_long = {'latitude':'42.3601', 'longitude':'-71.0589'}
    # return lat_long