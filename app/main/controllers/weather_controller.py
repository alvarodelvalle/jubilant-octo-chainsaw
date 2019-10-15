import json

from flask import request
from flask_restplus import Resource, Namespace
from werkzeug.exceptions import BadRequest, HTTPException, NotFound

from app.main.services.weather import Weather

api = Namespace('weather', description='v1 api calls')

@api.route('/weather')
class WeatherController(Resource):
    @api.doc('Get forecast')
    def get(self):
        rzip = request.args['zip']
        # check for args in request.args, if `zip` or `units` are missing or if country isn't `us`, return a 400
        rzip = rzip.split(',')
        if rzip.__len__() > 1:
            try:
                country_code = rzip[1].lower()
                if country_code != 'us':
                    raise Exception
            except:
                raise BadRequest     
        
        runits = request.args['units'] 
        weather = Weather()
        try:
            forecast = weather.get_forecast(rzip[0], runits)
        except BadRequest as e:
            raise e
        except NotFound as e:
            return e
        except HTTPException as e:
            return e
        return forecast