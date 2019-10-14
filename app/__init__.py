# app/__init__.py

from flask_restplus import Api
from flask import Blueprint

from .main.controllers.datetime_controller import api as datetime
from .main.controllers.weather_controller import api as weather

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='REST API',
          version='0.1',
          description='a flask restplus web service'
          )

api.add_namespace(datetime, path='/api/v1')
api.add_namespace(weather, path='/api/v1')