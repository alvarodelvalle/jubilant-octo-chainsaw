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


def convert_temp(orig_temp, units):
    """Static function to convert the temperature from F to K or C"""
    switcher = {
        'k': ((orig_temp - 32) * 5.0 / 9.0) + 273.15,
        'c': (orig_temp - 32) * 5.0 / 9.0,
        'f': orig_temp
    }
    temperature = switcher.get(units.lower())
    conversion = dict(original=orig_temp, units=units, temperature=temperature)
    return conversion


@api.route('/api/v1/weather')
@api.doc(params={'zip': 'format: xxxxx,us', 'units': u'one of the following: `F`arenheit `C`elcius `K`elvin'})
class Weather(Resource):
    """Get the weather in given units for the provided zip code"""

    @auth.login_required
    @api.marshal_with(weather_model)
    def get(self):
        zip_code = request.args['zip']
        zip_code = zip_code.split(',')
        if zip_code.__len__() > 1:
            try:
                country_code = zip_code[1].lower()
                if country_code != 'us':
                    raise Exception
            except:
                raise BadRequest

        requested_units = request.args['units']

        try:
            data = self.get_forecast(zip_code[0], requested_units)
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
        converted_temp = convert_temp(dark_forecast.currently.temperature, requested_units)
        forecast = {
            'Temperature': converted_temp['temperature'],
            'Description': dark_forecast.currently.summary,
            'OriginalTemp': converted_temp['original'],
            'ConvertedToUnits': converted_temp['units']
        }
        return forecast
