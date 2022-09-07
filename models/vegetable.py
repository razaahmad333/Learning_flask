from databaseConfigure import db


class Vegetable(db.Model):
    id = db.Column('veg_id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(100))
    price = db.Column('price', db.Integer)
    quantity = db.Column('quantity', db.Integer)

    def __init__(self, name, price, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return '<Vegetable %r>' % self.name

    def say_hi(self):
        return "Hi, I'm a ${} vegetable".format(self.name)


db.create_all()
db.session.commit()
