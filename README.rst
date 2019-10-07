Stateless DevOps Technical Assessment
=====================================

Context and Description
-----------------------

Your task is to create an API, written in Python 3 that returns a
variety of data when GET calls are made to the endpoints specified below.
Your API should be containerized for ease of use and well documented.
You may use frameworks so long as the decision to do so is clearly documented.
Be sure to also include tests to validate calls to your endpoints return
correctly. The final API code should be packaged in a Docker container.

API Endpoints
-------------

====== ================ =================================================================
Method Endpoint         Description
====== ================ =================================================================
GET    /api/v1/datetime returns the current time and date (UTC or local)
GET    /api/v1/weather  returns the current weather for a given zip code (details below)
====== ================ =================================================================

Submitting Your Results
-----------------------
Stateless will provide you with a private repo to submit your
work to. Fork the repo to your account, then push your work to the master
branch on the fork you created (in your account), then create a merge
request with notes back to the Stateless repo for final submission.
Commit often. We want to see your progress with notes rather than one
big push.

Expectations and Evaluation Criteria
------------------------------------
Your project will be evaluated on the following criteria:

* Correctness: Measures if the assignment produces the correct output
* Testing: Evaluates how thoroughly the candidate tested their submission. An ideal submission will have a thorough unit test suite and include/document tests done with larger corpus files 
* Readability: Using meaningful variable names, easy to follow logic and control flow, adequate commenting, and amount of code reuse

Requirements for correctness
---------------------------
Ensure your assignment meets the following requirements:

* Add basic authentication to your API (you may hard-code credentials)
* The weather check should accept a minimal request with the following query arguments: :code:`GET /api/v1/weather?zip={zipcode,countrycode}&units={units}`

  .. list-table::
    :header-rows: 1
    :widths: 12 112

    * - Argument
      - Description
    * - zip
      - US Zip code or ISO 3166-1 Alpha-2 formatted country code.
    * - units
      - Unit of measure for temperature. Will be one of :code:`celsius`, :code:`farenheit`, or :code:`kelvin`.  OR, you
        may abbreviate units as :code:`C`, :code:`F`, or :code:`K`.

  The returned JSON blob must include the following fields, though additional fields may be returned:

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
* Write your code in Python 3 and document it well
* Containerize your code with Docker -- we should be able to clone your repo and
  run 'docker-compose up' to bring the API up to test it
* Make the API  handle errors gracefully and return error codes and messages
  that are easy to interpret
* Create a good set of tests with a testing framework that checks API endpoints for
  expected results in normal and error conditions.
* Return all data as JSON
* Add API documentation in OpenAPI / Swagger / ReDoc spec.
* Add a reverse web proxy on the front end (in another container)
