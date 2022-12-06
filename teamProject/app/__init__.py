from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
<<<<<<< HEAD
from os import path
=======
from flask_login import LoginManager

>>>>>>> 3e4950a9b35c4ca2e397c5be3f9b970c18692951

#database is created
db = SQLAlchemy()

DB_NAME = "app.db"


def build_app():
    myapp = Flask(__name__)
    myapp.config["SECRET_KEY"] = 'TEAM-10-ROCKS-XD'
    from .routes import views
    from .auth import auth

    # configured database
    myapp.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    # extend the application with its contents
    myapp.register_blueprint(views, url_prefix='/')
    myapp.register_blueprint(auth, url_prefix='/')

    from .models import User, Post

    db.init_app(myapp)
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(myapp)

    @login_manager.user_loader
    def load(id):
        return User.query.get(int(id))

    with myapp.app_context():
        db.create_all()

    return myapp

def create_database(myapp):
    if not path.exists('app/' + DB_NAME):
        db.create_all(myapp=myapp)

