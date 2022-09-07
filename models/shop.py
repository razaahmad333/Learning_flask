import imp
from databaseConfigure import db


class Shop(db.Model):
    id = db.Column('shop_id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(100))
    address = db.Column('address', db.String(100))
    phone = db.Column('phone', db.String(100))
    email = db.Column('email', db.String(100))
    password = db.Column('password', db.String(100))
    products = db.relationship('Product', backref='shop', lazy='dynamic')

    def __init__(self, name, address, phone, email, password):
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email
        self.password = password

    def __repr__(self):
        return '<Shop %r>' % self.name
