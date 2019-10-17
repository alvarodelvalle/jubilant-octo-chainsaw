import pytest
from freezegun import freeze_time

from src.resources.datetime import *
from server.instance import server

url = '/api/v1/datetime'
dt = DateTimeUtc

@pytest.fixture
def app():
    """Creates a global fixture for the flask `app` instance"""
    app = server.app
    return app


class TestDateTimeClass:

    @freeze_time("2019-10-17")
    def test_datetime_response(self, client):
        headers = {
            'accept': 'application/json',
            'Authorization': 'Basic YWx2YXJvQGJlc3RhdGVsZXNzLmNvbTp0aGlzIGlzIG5vdCBteSBwYXNzd29yZA=='
        }
        response = client.get(url, headers=headers)
        # Validate the response
        assert response.status_code == 200
        assert response.json == dict(DateTime='2019-10-17T00:00:00+00:00')

    def test_datetime_unauthorized(self, client):
        headers = {
            'accept': 'application/json',
            'Authorization': 'Basic YWx2YXJvQGJlc3RhdGVsZXNzLmNvbTp0aGlzIGlzIG15IHdyb25nIHBhc3N3b3Jk'
        }
        response = client.get(url, headers=headers)
        assert response.status_code == 401
