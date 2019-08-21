from flask_restplus import Namespace, fields


class Dto:
    name = 'buyer'
    api = Namespace(name)
    model = api.model(name, {
        'buyer_id': fields.Integer(required=False),
        'user_id': fields.Integer(required=False),
        'buying_place': fields.String(required=False),
        'buying_time': fields.DateTime(required=False),
        'buying_date': fields.Date(required=False),
        'desired_place_receive': fields.String(required=False),
        'desired_time_receive': fields.DateTime(required=False),
        'desired_date_receive': fields.Date(required=False),
        'search_radius': fields.Float(required=False),
        'search_place': fields.String(required=False)
    })
