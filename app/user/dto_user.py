from flask_restplus import Namespace, fields


class Dto:
    name = 'user'
    api = Namespace(name)
    model = api.model(name, {
        'id':fields.Integer(required=False, description='The user identifier'),
        'username': fields.String(required=True, desciption='User name'),
        'email': fields.String(required=True, description='User email address')
    })
