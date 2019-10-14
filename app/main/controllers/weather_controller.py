import json

from flask import request
from flask_restplus import Resource, Namespace

from app.main.services.weather import Weather

api = Namespace('weather', description='v1 api calls')

@api.route('/weather')
class WeatherController(Resource):
    @api.doc('Get forecast')
    def get(self):
        weather = Weather()
        forecast = weather.get_forecast()
        current_forecast = json.dumps({
            'temperature':forecast.currently.temperature,
            'description':forecast.currently.summary
            })
        return current_forecast

