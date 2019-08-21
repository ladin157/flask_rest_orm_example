from .user import api as ns_user
from .buyer import api as ns_buyer
from flask_restplus import Api

api = Api(title='APIs',
          version='1.0',
          description='APIs')

api.add_namespace(ns=ns_user)
api.add_namespace(ns=ns_buyer)
