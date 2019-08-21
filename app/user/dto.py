from flask_restplus import Namespace, fields


class Dto:
    name = 'user'
    api = Namespace(name)
    model = api.model(name, {
        'username': fields.String(required=True, desciption='User name'),
        'email': fields.String(required=True, description='User email address')
    })
