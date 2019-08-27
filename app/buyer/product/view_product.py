from flask_restplus import Resource

from .controller_product import ControllerProduct
from .dto_product import ProductDto

api = ProductDto.api
product = ProductDto.model


@api.route('')
class ProductList(Resource):
    @api.marshal_list_with(product)
    def get(self):
        controller = ControllerProduct()
        return controller.get()

    @api.expect(product)
    def post(self):
        data = api.payload
        controller = ControllerProduct()
        return controller.create(data=data)


@api.route('/<int:product_id>')
@api.response(404, "Product not found")
@api.param('product_id', 'The product identifer')
class Product(Resource):
    @api.marshal_with(product)
    def get(self, product_id):
        controller = ControllerProduct()
        return controller.get_by_id(object_id=product_id)

    @api.expect(product)
    def put(self, product_id):
        data = api.payload
        controller = ControllerProduct()
        return controller.update(object_id=product_id, data=data)

    def delete(self, product_id):
        controller = ControllerProduct()
        return controller.delete(object_id=product_id)
