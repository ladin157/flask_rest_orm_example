from app import db


class Product(db.Model):
    __tablename__ = 'product'

    product_id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    buyer_id = db.Column(db.Integer, db.ForeignKey('buyer.buyer_id'), nullable=False)
    buyer = db.relationship('Buyer', backref=db.backref('products', lazy=True))

    product_name = db.Column(db.String(255), nullable=True)
    product_price = db.Column(db.Float, nullable=True)
    qrcode = db.Column(db.String(45))
    barcode = db.Column(db.String(45))

    vendor_name = db.Column(db.String(80))
    photo_path = db.Column(db.String(255))
    store_name = db.Column(db.String(255))
    store_address = db.Column(db.String(255))

    category = db.Column(db.String(80))
    volume = db.Column(db.Float)
    unit = db.Column(db.String(45))

    def __init__(self, buyer_id, product_name, product_price, qrcode=None, barcode=None, vendor_name=None,
                 photo_path=None, store_name=None, store_address=None, category=None, volume=None, unit=None):
        self.buyer_id = buyer_id
        self.product_name = product_name
        self.product_price = product_price
        self.qrcode = qrcode
        self.barcode = barcode
        self.vendor_name = vendor_name
        self.photo_path = photo_path
        self.store_name = store_name
        self.store_address = store_address
        self.category = category
        self.volume = volume
        self.unit = unit
