from .model import Buyer
from app import db


class Controller:
    def get(self):
        buyers = Buyer.query.all()
        return buyers

    def get_by_id(self, buyer_id):
        buyer = Buyer.query.filter_by(buyer_id=buyer_id)

    def insert(self, data):
        if not isinstance(data, dict):
            return
        user_id = data['user_id']
        buying_place = data['buying_place']
        search_radius = data['search_radius']
        buyer = Buyer(user_id=user_id, buying_place=buying_place, search_place=search_radius)
        self._save_buyer(buyer, created=True)

    def update(self, buy_id, data):
        pass

    def delete(self, buyer_id):
        pass

    def _save_buyer(self, buyer, created = False, deleted= False):
        if created:
            db.session.add(buyer)
        if deleted:
            db.session.delete(buyer)
        db.session.commit()
