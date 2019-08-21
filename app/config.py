import os

basedir = os.path.dirname(os.path.dirname(__file__))


class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///"+ os.path.join(basedir, 'db.db')
