from datetime import datetime, timezone

from flask_restplus import Resource, marshal

from models.datetime import datetimeutc
from resources.authorization_helper import auth
from server.instance import server

app, api = server.app, server.api


@api.route('/api/v1/datetime')
class DateTimeUtc(Resource):
    """Gets the datetime in UTC"""

    @api.doc('Get datetime in UTC')
    @auth.login_required
    @api.marshal_with(datetimeutc)
    def get(self):
        data = {'DateTime': datetime.now(timezone.utc).isoformat()}
        response = marshal(data, datetimeutc)
        return response
