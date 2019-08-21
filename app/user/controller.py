from .model import User
from app import db


class Controller:
    def get(self):
        """
        Tra ve hoac danh sach user
        @admin_token_required
        @token_required
        :return:
        """
        users = self._get_all_users()
        return users

    def get_by_id(self, user_id):
        """
        Tra ve thong tin cua 1 user theo id
        :param id:
        :return:
        """
        user = self._get_user_by_id(user_id)
        return user

    def post(self, user_id=None, data=None, create=False):
        if create:
            self._add_user(data)
        else:
            self._update(user_id, data)

    def delete(self, user_id):
        self._delete(user_id)

    def _insert(self, data):
        if not isinstance(data, dict):
            return
        email = data['email']
        username = data['username']
        user = User(email=email, username=username)
        self._save_user(user, create=True)

    def _get_all_users(self):
        users = User.query.all()
        return users

    def _get_user_by_id(self, id):
        user = User.query.filter_by(id=id).first()
        return user

    def _add_user(self, data):
        user = User.query.filter_by(email=data['email']).first()
        if user is None:
            new_user = User(
                username=data['username'],
                email=data['email']
            )
            self._save_user(new_user, create=True)
            return True
        else:
            return False

    def _update(self, user_id, data):
        if not isinstance(data, dict):
            return
        email = data['email']
        username = data['username']
        user = User.query.filter_by(id=user_id).first()
        if not user:
            return
        user.username = username
        user.email = email
        self._save_user(user, create=False)

    def _delete(self, user_id):
        user = User.query.filter_by(id=user_id).first()
        if not user:
            return
        self._save_user(user, delete=True)

    def _save_user(self, user, create=False, delete=False):
        if create:
            db.session.add(user)
        if delete:
            db.session.delete(user)
        db.session.commit()
