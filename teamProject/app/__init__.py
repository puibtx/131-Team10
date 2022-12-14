from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

from os import path
from flask_login import LoginManager


#database is created
db = SQLAlchemy()

DB_NAME = "app2.db"
UPLOAD_FOLDER = 'app/static/images/'


def build_app():
    # initialized our app
    myapp = Flask(__name__)
    myapp.config["SECRET_KEY"] = 'TEAM-10-ROCKS-XD'
    myapp.config['SESSION_TYPE'] = 'filesystem'
    myapp.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    from .routes import views
    from .auth import auth

    # configured database
    myapp.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    # extend the application with its contents
    myapp.register_blueprint(views, url_prefix='/')
    myapp.register_blueprint(auth, url_prefix='/')

    from .models import User, Post

    # login configuration from flask login
    db.init_app(myapp)
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(myapp)

    @login_manager.user_loader
    def load(id):
        return User.query.get(int(id))

    # creates our data base
    with myapp.app_context():
        db.create_all()

    return myapp
