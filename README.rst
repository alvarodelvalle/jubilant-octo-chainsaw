RESTful API
=====================================

Description
-----------

A flask-restful API, written in Python 3 that returns a
variety of data when GET calls are made to the endpoints.
The API is containerized for ease of use.

API Endpoints
-------------
.. list-table::
  :header-rows: 1
  :widths: 12 30 88

  * - Method
    - Endpoint
    - Description
  * - GET
    - /api/v1/datetime
    - returns the current time and date (UTC or local)
  * - GET
    - /api/v1/weather
    - returns the current weather for a given zip code (details below)

* Basic authentication
* The weather check accepts a minimal request with the following query
  arguments: :code:`GET /api/v1/weather?zip={zipcode,countrycode}&units={units}`

  .. list-table::
    :header-rows: 1
    :widths: 12 112

    * - Argument
      - Description
    * - zip
      - US Zip code with or without ISO 3166-1 Alpha-2 formatted country code.
    * - units
      - Unit of measure for temperature. Will be one of :code:`celsius`, :code:`farenheit`, or :code:`kelvin`. OR, you
        may abbreviate units as :code:`c`, :code:`f`, or :code:`k` (upper or lower should be able to be submitted).

  The returned JSON blob includes the following fields, though additional fields may be returned:

  .. list-table::
    :header-rows: 1
    :widths: 12 12 112

    * - Property
      - Type
      - Description
    * - temperature
      - Number
      - The current temperature at the location specified by :code:`zip` in the units specified by :code:`units`.
    * - description
      - String
      - A human-readable summary of the current weather such as :code:`sunny`, :code:`cloudy`, or :code:`rainy`.

Getting Started
===============
I wrote the RESTful API using the flask framework and it's popular plugin flask-restplus
for inherent Swagger documentation. To get started, you will need to create an
:code:`.env` file in :code:`root` to store the following environment variables:

  .. list-table::
    :header-rows: 0
    :widths: 150

    * - SKIES_API_KEY=34a12b1326745f8070f12148ea6e8e98
    * - PYTHONPATH="src:tests"
    * - PYTHON_ENV=proxied
    * - FLASK_ENV=production
    * - FLASK_DEBUG=false

Next, run :code:`docker-compose up` to create both project containers.

Afterwards, you may invoke the endpoints using a Rest client like Postman.
For convenience here are the curl commands

* curl -X GET \
  http://localhost/api/v1/datetime \
  -H 'Accept-Encoding: gzip, deflate' \
  -H 'Authorization: Basic YWx2YXJvQGJlc3RhdGVsZXNzLmNvbTp2YWxpZCBwYXNzd29yZA==' \
  -H 'Cache-Control: no-cache' \
  -H 'Connection: keep-alive' \
  -H 'Host: localhost' \
  -H 'Postman-Token: bfd1f12c-cea5-44d7-8008-136a462f1a25,c206e9f7-70f5-4a6c-ba33-75c2470d467b' \
  -H 'User-Agent: PostmanRuntime/7.17.1' \
  -H 'accept: application/json' \
  -H 'cache-control: no-cache'
* curl -X GET \
  'http://localhost/api/v1/weather?zip=80301,us&units=f' \
  -H 'Accept-Encoding: gzip, deflate' \
  -H 'Authorization: Basic YWx2YXJvQGJlc3RhdGVsZXNzLmNvbTp2YWxpZCBwYXNzd29yZA==' \
  -H 'Cache-Control: no-cache' \
  -H 'Connection: keep-alive' \
  -H 'Host: localhost' \
  -H 'Postman-Token: 70f238d0-ae82-4fc4-8a44-da2d69e5483a,b4aa7b73-51d2-4e88-b9e5-069182ef1ab1' \
  -H 'User-Agent: PostmanRuntime/7.17.1' \
  -H 'accept: application/json' \
  -H 'cache-control: no-cache'

You may also go to http://localhost/swagger to view the documentation and
invoke the endpoints there. You will also notice that I have included response
models in the swagger documentation. Upon invoking the endpoint, you will be
asked for basic authentication. The credentials are:

* username: alvaro@bestateless.com
* password: valid password

Lastly, running the API tests can be done by commands :code:`pipenv install --dev`
followed by :code:`pipenv run pytest`.

As always if you have any questions please feel free to contact me!