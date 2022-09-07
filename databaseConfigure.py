from flask_sqlalchemy import SQLAlchemy

from appConfigure import app

db = SQLAlchemy(app)

SQLALCHEMY_TRACK_MODIFICATIONS = False
