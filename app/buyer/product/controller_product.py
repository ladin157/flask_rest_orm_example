from app import db
from .product import Product


class ControllerProduct:

    def create(self, data):
        if not isinstance(data, dict):
            return False
        if not 'buyer_id' in data:
            return False
        try:
            product = self._parse_product(data=data)
            db.session.add(product)
            db.session.commit()
            return True
            # return send_result(message="Create products successfully!")
        except Exception as e:
            # return send_error(message="Could not create product!")
            return False

    def get(self):
        products = Product.query.all()
        return products
        # data = marshal(products, ProductDto.model)
        # return send_result(data=data, message="Get list of products successfully.")

    def get_by_id(self, object_id):
        product = Product.query.filter_by(product_id=object_id).first()
        return product

    def update(self, object_id, data):
        try:
            product = Product.query.filter_by(product_id=object_id).first()
            if product is None:
                return False
            product = self._parse_product(data=data, product=product)
            db.session.commit()
            return True
        except Exception as e:
            return False

    def delete(self, object_id):
        try:
            product = Product.query.filter_by(product_id=object_id).first()
            if product is None:
                return False
            db.session.delete(product)
            db.session.commit()
            return True
        except Exception as e:
            return False

    def _parse_product(self, data, product=None):
        buyer_id, product_name, product_price, qrcode, barcode, vendor_name, photo_path, store_name, store_address, category, volume, unit = None, None, None, None, None, None, None, None, None, None, None, None
        if 'buyer_id' in data:
            buyer_id = data['buyer_id']
        if 'product_name' in data:
            product_name = data['product_name']
        if 'product_price' in data:
            product_price = data['product_price']
        if 'qrcode' in data:
            qrcode = data['qrcode']
        if 'barcode' in data:
            barcode = data['barcode']
        if 'vendor_name' in data:
            vendor_name = data['vendor_name']
        if 'photo_path' in data:
            photo_path = data['photo_path']
        if 'store_name' in data:
            store_name = data['store_name']
        if 'store_address' in data:
            store_address = data['store_address']
        if 'category' in data:
            category = data['category']
        if 'volume' in data:
            volume = data['volume']
        if 'unit' in data:
            unit = data['unit']
        if product is None:
            product = Product(buyer_id=buyer_id, product_name=product_name, product_price=product_price, qrcode=qrcode,
                              barcode=barcode, vendor_name=vendor_name, photo_path=photo_path, store_name=store_name,
                              store_address=store_address, category=category, volume=volume, unit=unit)
        else:
            (product.buyer_id, product.product_name, product.product_price, product.qrcode, product.barcode,
             product.vendor_name, product.photo_path, product.store_name, product.store_address, product.category,
             product.volume, product.unit) = (
                buyer_id, product_name, product_price, qrcode, barcode, vendor_name, photo_path, store_name,
                store_address,
                category, volume, unit)
        return product
