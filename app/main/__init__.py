from flask import Flask
from .config import configurations

def create_app(configuration_name):
    app = Flask(__name__)
    app.config.from_object(configurations[configuration_name])
    return app