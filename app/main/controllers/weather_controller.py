import json

from flask import request
from flask_restplus import Resource, Namespace

from app.main.services.weather import Weather

api = Namespace('weather', description='v1 api calls')

@api.route('/weather')
class WeatherController(Resource):
    @api.doc('Get forecast')
    def get(self):
        # check for args in request.args, if `zip` or `units` are missing, return a 400
        rzip = request.args['zip'] 
        runits = request.args['units'] 
        print("Zip: {a:s}; Units: {b:s}".format(a=rzip, b=runits))

        weather = Weather()
        forecast = weather.get_forecast(rzip, runits)
        return forecast

