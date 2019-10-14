from datetime import datetime, timezone
import json

from flask import request
from flask_restplus import Resource, Namespace

api = Namespace('datetime', description='v1 api calls')

@api.route('/datetime')
class DateTime(Resource):
    @api.doc('Get datetime in UTC')
    def get(self):
        json_datetime = {'datetime':datetime.now(timezone.utc).isoformat()}
        return json_datetime