from typing import Any, Union

import pytest
from flask import url_for

from src.resources.weather import *
from server.instance import server

url = '/api/v1/weather'
w = Weather

@pytest.fixture
def app():
    """Creates a global fixture for the flask `app` instance"""
    app = server.app
    return app


class TestWeatherClass:

    def test_weather_response(self, client):
        query_params = {
            'zip': '80301,us',
            'units': 'f'
        }
        headers = {
            'accept': 'application / json',
            'Authorization': 'Basic YWx2YXJvQGJlc3RhdGVsZXNzLmNvbTp0aGlzIGlzIG5vdCBteSBwYXNzd29yZA=='
        }
        response = client.get(url, query_string=query_params, headers=headers)
        assert response.status_code == 200
