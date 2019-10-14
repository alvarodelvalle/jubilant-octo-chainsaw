import os
import unittest

from flask import current_app
from flask_testing import TestCase

from manage import app
from app.main.config import basedir

# TODO - find out why it says 'ran 0 test cases' and why the app import fails on debug - AD 20191011
class DevelopmentConfig(TestCase):
    def create_app(self):
        app.config.from_object('app.main.config.DevConfig')
        return app

    def is_app_development(self):
        self.assertFalse(current_app is None)
        self.assertTrue(app.config['DEBUG'] is True)
        self.assertTrue(app.config['SKIES_API_KEY'] is 'SKIES_API_KEY')

if __name__ == '__main__':
    unittest.main()