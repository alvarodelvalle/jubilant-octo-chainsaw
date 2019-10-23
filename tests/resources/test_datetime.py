import pytest
from freezegun import freeze_time

from src.resources.datetime import DateTimeUtc
from server.instance import server

url = '/api/v1/datetime'

@pytest.fixture
def app():
    """Creates a global fixture for the flask `app` instance"""
    app = server.app
    return app


def headers(**kwargs):
    request_headers = dict(kwargs)
    return request_headers


class TestDateTimeClass:
    """Tests the datetimeutc endpoint"""
    valid_auth = 'Basic YWx2YXJvQGJlc3RhdGVsZXNzLmNvbTp2YWxpZCBwYXNzd29yZA=='
    invalid_auth = 'Basic YWx2YXJvQGJlc3RhdGVsZXNzLmNvbTppbnZhbGlkIHBhc3N3b3Jk'

    @freeze_time("2019-10-17")
    def test_datetime_response(self, client):
        response = client.get(
            url,
            headers=headers(
                accept='application/json',
                Authorization=self.valid_auth)
        )
        # Validate the response
        assert response.status_code == 200
        assert response.json == dict(DateTime='2019-10-17T00:00:00+00:00')

    def test_datetime_unauthorized(self, client):
        response = client.get(url, headers=headers(
            accept='application/json',
            Authorization=self.invalid_auth)
                              )
        assert response.status_code == 401

    def test_datetime_response_body(self, client):
        response = client.get(
            url,
            headers=headers(
                accept='application/json',
                Authorization=self.valid_auth)
        )
        date_time = list(response.json)[0]
        assert date_time == 'DateTime'
        assert type(response.json['DateTime']) == str
