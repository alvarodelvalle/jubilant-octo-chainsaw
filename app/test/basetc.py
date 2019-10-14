from flask_testing import TestCase

from manage import app

class BaseTestCases(TestCase):
    def create_app(self):
        app.config.from_object('app.main.config.TestingConfig')