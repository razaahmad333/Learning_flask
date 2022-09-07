from flask import render_template, request, redirect
from models.vegetable import Vegetable
from databaseConfigure import db


def index():
    return render_template('vegetables/index.html', vegetables=Vegetable.query.all())


def createVegetable():
    if request.method == 'POST':

        name = request.form['name']
        price = request.form['price']
        quantity = request.form['quantity']

        new_vegetable = Vegetable(
            name, price, quantity=quantity if quantity else 0)
        db.session.add(new_vegetable)
        db.session.commit()
        new_vegetable.say_hi()

        return redirect('/')
    else:
        return render_template('vegetables/create_vegetable.html')


def deleteVegetable(id):
    vegetable = Vegetable.query.get(id)
    db.session.delete(vegetable)
    db.session.commit()

    return redirect('/')


def editVegetable(id):
    if request.method == "POST":
        vegetable = Vegetable.query.get(id)
        vegetable.name = request.form['name']
        vegetable.price = request.form['price']
        vegetable.quantity = request.form['quantity']
        db.session.commit()
        return redirect('/')
    else:
        vegetable = Vegetable.query.get(id)
        return render_template('vegetables/create_vegetable.html', vegetable=vegetable)
