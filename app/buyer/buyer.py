from app import db


class Buyer(db.Model):
    buyer_id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('buyers', lazy=True))

    buying_place = db.Column(db.String(255))
    buying_time = db.Column(db.Time)
    buying_date = db.Column(db.Date)

    desired_place_receive = db.Column(db.String(255))
    desired_time_receive = db.Column(db.Time)
    desired_date_receive = db.Column(db.Date)

    search_radius = db.Column(db.Float)
    search_place = db.Column(db.String(255))

    def __init__(self, user_id, buying_place=None, buying_time=None, buying_date=None, desire_place_receive=None,
                 desired_time_receive=None, desired_date_receive=None, search_radius=None, search_place=None):
        self.user_id = user_id
        self.buying_date = buying_date
        self.buying_time = buying_time
        self.buying_place = buying_place
        self.desired_place_receive = desire_place_receive
        self.desired_time_receive = desired_time_receive
        self.desired_date_receive = desired_date_receive
        self.search_radius = search_radius
        self.search_place = search_place
