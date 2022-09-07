from calendar import c
from urllib import response
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import urllib.request, json
from math import floor

import views

app = Flask(__name__)

api_base_url = 'https://fakestoreapi.com/products/1'
api_jokes_url = "https://v2.jokeapi.dev/joke/Programming?amount=10"
jokes_api_url_base = "https://v2.jokeapi.dev/joke"

app.add_url_rule('/fruits/banana', view_func= views.banana)
app.add_url_rule('/fruits/apple', view_func= views.apple)


global categories
categories = ["Programming", "Misc", "Puns", "Dark", "Christmas"]

global currentCategory
currentCategory = 'Programming'


global jokesState 
jokesState = {}

for category in categories:
    jokesState[category] = []

def getDistributedJokes(jokes):
    len_ = len(jokes)
    dJokes = [jokes[0 : floor(len_/4)], jokes[floor(len_/4): 2*floor(len_/4)],jokes[2*floor(len_/4): 3*floor(len_/4)],jokes[3*floor(len_/4): len_]]
    return dJokes

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    global jokesState
    global categories
    if request.method == 'POST':
        response = urllib.request.urlopen(api_jokes_url)
        jokes = json.loads(response.read())
        jokesState[currentCategory] = jokesState[currentCategory] +  jokes['jokes']
        return redirect(url_for('hello_world'))
    else:
        return render_template('index.html', totalJokes = len(jokesState[currentCategory]), categories=categories, jokesData=getDistributedJokes(jokesState[currentCategory]))




@app.route('/jokes/<category>')
def jokesByCategory(category):
    global jokesState
    global categories
    global currentCategory
    currentCategory = category
    response = urllib.request.urlopen(jokes_api_url_base + '/' + category + '?amount=10')
    jokes = json.loads(response.read())
    jokesState[currentCategory] = jokesState[currentCategory] +  jokes['jokes']
    return redirect(url_for('hello_world'))
    # return render_template('index.html', totalJokes = len(jokesState), categories=categories, jokesData=getDistributedJokes(jokesState))



@app.route('/products')
def items():
    response= urllib.request.urlopen(api_jokes_url)
    # print(response_)
    products = json.loads(response.read())
    print(products)
    return "hii"+api_base_url + '/products'