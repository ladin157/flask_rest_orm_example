from flask_restplus import Resource
from .dto import Dto
from .controller import Controller
from flask import request

api = Dto.api
_user = Dto.model


@api.route('/')
class UserList(Resource):
    @api.doc('List users')
    @api.marshal_list_with(_user)
    def get(self):
        """
        Return user lists
        :return:
        """
        controller = Controller()
        users = controller.get()
        return users

    @api.expect(_user)
    def post(self):
        """
        Create new user
        :return:
        """
        data = api.payload
        controller = Controller()
        controller.post(data, create=True)


@api.route('/<int:user_id>')
class UserID(Resource):
    @api.doc('get user')
    @api.marshal_with(_user)
    def get(self, user_id):
        """
        Get user by id
        :param id:
        :return:
        """
        controller = Controller()
        user = controller.get_by_id(user_id)
        return user

    @api.doc("Update user")
    @api.expect(_user)
    def put(self, user_id):
        """
        Update user information
        :param user_id:
        :return:
        """
        data = api.payload
        controller = Controller()
        controller.post(user_id, data)

    @api.doc("Delete User")
    @api.response(204, 'User deleted')
    def delete(self, user_id):
        """
        Delete user by ID
        :param user_id:
        :return:
        """
        controller = Controller()
        controller.delete(user_id)
