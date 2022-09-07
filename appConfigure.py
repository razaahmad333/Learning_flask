from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vegetables.db'
app.secret_key = b'3ba197f32520c8e7daaab75581c20a0276a421553dc7c06f84bfca0d6bc86375'
