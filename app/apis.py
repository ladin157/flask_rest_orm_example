from .user import ns_user
from .buyer import ns_buyer, ns_product
from flask_restplus import Api

api = Api(title='APIs',
          version='1.0',
          description='APIs')

api.add_namespace(ns=ns_user)
api.add_namespace(ns=ns_buyer)
api.add_namespace(ns=ns_product)
