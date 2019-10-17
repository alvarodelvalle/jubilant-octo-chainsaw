from flask_restplus import fields
from server.instance import server

datetimeutc = server.api.model('DateTime',
                               {
                                   'DateTime': fields.DateTime(description='*The UTC Date and Time', dt_format='iso8601')
                               })
