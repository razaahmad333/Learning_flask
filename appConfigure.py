from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vegetables.db'
app.secret_key = b'generate api keys from where i dont know '
