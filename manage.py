from app import db
from app.apis import api
from flask import Flask
from app.config import Config
from werkzeug.contrib.fixers import ProxyFix
from flask_restplus import Resource

ap = Flask(__name__)
ap.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI
ap.wsgi_app = ProxyFix(ap.wsgi_app)
api.init_app(ap)
db.init_app(ap)


@api.route('/')
class HelloWorld(Resource):
    @staticmethod
    def get(self):
        return {'Hello': 'Hello World!'}


if __name__ == '__main__':
    db.create_all()
    ap.run(debug=True)
