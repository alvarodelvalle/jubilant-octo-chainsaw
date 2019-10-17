from flask_restplus import fields
from server.instance import server

weather_model = server.api.model('Weather',
                                 {
                                     'Temperature': fields.Float(description='*The temperature in requested units'),
                                     'Description': fields.String(description='*Overall summary of the current weather')
                                 })
