from flask_restplus import Resource
from .dto import Dto
from .controller import Controller

api = Dto.api
_buyer = Dto.model


@api.route('/')
class BuyerList(Resource):
    @api.doc('List buyers')
    @api.marshal_list_with(_buyer)
    def get(self):
        """
        Return buyers list.
        :return:
        """
        controller = Controller()
        buyers = controller.get()
        return buyers

    @api.expect(_buyer)
    def post(self):
        """
        Create new buyer
        :return:
        """
        data = api.payload
        controller = Controller()
        controller.insert(data)


@api.route('/<int:buyer_id>')
class BuyerId(Resource):
    @api.marshal_with(_buyer)
    def get(self, buyer_id):
        controller = Controller()
        buyer = controller.get_by_id(buyer_id)
        return buyer

    @api.expect(_buyer)
    def put(self, user_id):
        pass

    def delete(self, user_id):
        pass
