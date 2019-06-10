from flask_pymongo import PyMongo
from flask_admin import Admin
from flask_login import LoginManager

mongo = PyMongo()
login_manager = LoginManager()
login_manager.session_protection = 'basic'
login_manager.login_view = 'auth.login'


def init_extension(app):
    mongo.init_app(app)
    login_manager.init_app(app)

