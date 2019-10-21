from typing import Any, Union

import pytest
from flask import url_for

from src.resources.weather import Weather
from server.instance import server

url = '/api/v1/weather'
w = Weather


@pytest.fixture
def app():
    """Creates a global fixture for the flask `app` instance"""
    app = server.app
    return app


def query_params(**kwargs):
    params = dict(kwargs)
    return params


def headers(**kwargs):
    request_headers = dict(kwargs)
    return request_headers


class TestWeatherClass:
    """Tests the weather api"""
    valid_auth = 'Basic YWx2YXJvQGJlc3RhdGVsZXNzLmNvbTp2YWxpZCBwYXNzd29yZA=='
    invalid_auth = 'Basic YWx2YXJvQGJlc3RhdGVsZXNzLmNvbTppbnZhbGlkIHBhc3N3b3Jk'

    def test_weather_response_code(self, client):
        response = client.get(
            url,
            query_string=query_params(zip='80301,us', units='f'),
            headers=headers(
                accept='application/json',
                Authorization=self.valid_auth)
        )

        assert response.status_code == 200

    def test_weather_response_body(self, client):
        response = client.get(
            url,
            query_string=query_params(zip='80301,us', units='f'),
            headers=headers(
                accept='application/json',
                Authorization=self.valid_auth)
        )
        temp, desc, o_temp, c_to_units = response.json
        assert temp == 'Temperature'
        assert desc == 'Description'
        assert o_temp == 'OriginalTemp'
        assert c_to_units == 'ConvertedToUnits'
        assert type(response.json['Temperature']) == float
        assert type(response.json['Description']) == str
        assert type(response.json['OriginalTemp']) == float
        assert type(response.json['ConvertedToUnits']) == str

    def test_unauthorized_response(self, client):
        response = client.get(
            url,
            query_string=query_params(zip='80301,us', units='f'),
            headers=headers(
                accept='application/json',
                Authorization=self.invalid_auth)
        )

        assert response.status_code == 401

    def test_valid_country_code(self, client):
        response = client.get(
            url,
            query_string=query_params(zip='80301,us', units='f'),
            headers=headers(
                accept='application/json',
                Authorization=self.valid_auth)
        )

        assert response.status_code == 200

    def test_invalid_country_code(self, client):
        response = client.get(
            url,
            query_string=query_params(zip='80301,mx', units='f'),
            headers=headers(
                accept='application/json',
                Authorization=self.valid_auth)
        )

        assert response.status_code == 400

    def test_kelvin_temp_conversion(self, client):
        response = client.get(
            url,
            query_string=query_params(zip='80301,us', units='k'),
            headers=headers(
                accept='application/json',
                Authorization=self.valid_auth)
        )
        assert response.json['ConvertedToUnits'] == 'k'

    def test_celsius_temp_conversion(self, client):
        response = client.get(
            url,
            query_string=query_params(zip='80301,us', units='c'),
            headers=headers(
                accept='application/json',
                Authorization=self.valid_auth)
        )
        assert response.json['ConvertedToUnits'] == 'c'

    def test_missing_country_code(self, client):
        response = client.get(
            url,
            query_string=query_params(zip='80301', units='f'),
            headers=headers(
                accept='application/json',
                Authorization=self.valid_auth)
        )
        assert response.status_code == 200

    def test_missing_units(self, client):
        response = client.get(
            url,
            query_string=query_params(zip='80301,us', units=None),
            headers=headers(
                accept='application/json',
                Authorization=self.valid_auth)
        )
        assert response.status_code == 400

    def test_invalid_zip(self, client):
        response = client.get(
            url,
            query_string=query_params(zip='00000', units='f'),
            headers=headers(
                accept='application/json',
                Authorization=self.valid_auth)
        )
        assert response.status_code == 400

    def test_missing_zip(self, client):
        response = client.get(
            url,
            query_string=query_params(zip=None, units='f'),
            headers=headers(
                accept='application/json',
                Authorization=self.valid_auth)
        )
        assert response.status_code == 400
