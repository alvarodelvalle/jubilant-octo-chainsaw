from datetime import datetime, timezone
import json

from flask import request
from flask_restplus import Resource, Namespace

api = Namespace('datetime', description='v1 api calls')

@api.route('/datetime')
class DateTime(Resource):
    @api.doc('Get datetime in UTC')
    def get(self):
        json_dict = {'datetime':datetime.now(timezone.utc).isoformat()}
        # TODO - response is in stringified JSON. Evaluate if this JSON type is ok for the proxy - AD 20191011
        jsondumps = json.dumps(json_dict)
        return jsondumps