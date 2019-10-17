import os

import zipcodes
from darksky.api import DarkSky
from darksky.types import weather
from flask import request
from flask_restplus import Resource, marshal
from werkzeug.exceptions import BadRequest, HTTPException, NotFound

from models.weather import weather_model
from resources.authorization_helper import auth
from server.instance import server

app, api = server.app, server.api


# api = Namespace('datetime', description='v1 api calls')

def temp_convert(current_temp, units):
    """Static function to convert the temperature from F to K or C"""
    switcher = {
        'k': ((current_temp - 32) * 5.0 / 9.0) + 273.15,
        'c': (current_temp - 32) * 5.0 / 9.0,
        'f': current_temp
    }
    temperature = switcher.get(units.lower())
    return temperature


@api.route('/api/v1/weather')
@api.doc(params={'zip': 'format: xxxxx,us', 'units': 'one of the following: (F)arenheit (C)elcius (K)elvin'})
class Weather(Resource):
    """Get the weather in given units for the provided zip code"""

    @auth.login_required
    @api.marshal_with(weather_model)
    def get(self):
        zip_code, country_code = request.args['zip'].split(',')
        if zip_code.__len__() > 1:
            try:
                country_code = country_code.lower()
                if country_code != 'us':
                    raise Exception
            except:
                raise BadRequest

        requested_units = request.args['units']

        try:
            data = self.get_forecast(zip_code, requested_units)
        except BadRequest as e:
            raise e
        except NotFound as e:
            return e
        except HTTPException as e:
            return e

        forecast = marshal(data, weather_model)
        return forecast

    def get_forecast(self, zipcode, requested_units):
        u"""Get the current temperature in specified units and description(eg:'clear')"""
        # zip code param may be passed as an invalid format
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

        # once lat, long, and units are validated, make the call to the upstream API for weather
        api_key = os.getenv('SKIES_API_KEY')
        darksky = DarkSky(api_key)

        dark_forecast = darksky.get_forecast(
            latitude, longitude,
            exclude=[weather.MINUTELY, weather.ALERTS]
        )
        converted_temp = temp_convert(dark_forecast.currently.temperature, requested_units)
        forecast = {'Temperature': converted_temp, 'Description': dark_forecast.currently.summary}
        return forecast
