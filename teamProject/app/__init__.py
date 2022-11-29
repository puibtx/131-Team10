from flask import Flask, render_template
from config import Config
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"


def build_app():
    myapp = Flask(__name__)
    myapp.config["SECRET_KEY"] = 'TEAM-10-ROCKS-XD'
    from .routes import routes
    from .auth import auth

    myapp.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    db.init_app(myapp)

    myapp.register_blueprint(routes, url_prefix='/')
    myapp.register_blueprint(auth, url_prefix='/')

    from .models import User

    with myapp.app_context():
        db.create_all()

    return myapp


def build_DB(myapp):
    if not path.exists('app/' + DB_NAME):
        db.create_all(myapp=myapp)
