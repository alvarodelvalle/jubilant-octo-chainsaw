import os 

basedir = os.path.abspath(os.path.dirname(__file__))

class Configuration:
    SKIES_API_KEY = os.getenv('SKIES_API_KEY')
    DEBUG = False

class DevConfig(Configuration):
    DEBUG = True

class TestingConfig(Configuration):
    DEBUG = True
    TESTING = True
class ProductionConfig(Configuration):
    DEBUG = False

configurations = dict(
    dev=DevConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

SKIES_API_KEY = Configuration.SKIES_API_KEY