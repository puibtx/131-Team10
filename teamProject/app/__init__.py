from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from os import path
from flask_login import LoginManager
from .forms import SearchForm

from flask import Flask, render_template, request, redirect, url_for, session
from flask_socketio import SocketIO, join_room, leave_room, emit
from flask_session import Session


#database is created
db = SQLAlchemy()

DB_NAME = "app.db"


def build_app():
    myapp = Flask(__name__)
    myapp.config["SECRET_KEY"] = 'TEAM-10-ROCKS-XD'
    myapp.config['SESSION_TYPE'] = 'filesystem'
    from .routes import views
    from .auth import auth

    # session and chat contents
    Session(views)
    socketio = SocketIO(myapp, manage_session=False)
    wsgi_app = myapp.wsgi_app
    socketio.run(myapp)

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

    # with myapp.app_context():

    #     u1 = User(username='john1312', email='john1231@example.com')
    #     u2 = User(username='susan1123', email='susan1231@example.com')
    #     u3 = User(username='mary1123', email='mary1231@example.com')
    #     u4 = User(username='david1123', email='david1231@example.com')
    #     u5 = User(username='puibtx', email='puibtx@gmail.com',password=generate_password_hash('1234567', method='sha512'))
    #     db.session.add_all([u1, u2, u3, u4, u5])
    #     db.session.commit()
    #     u5.follow(u1)  # john follows susan
    #     u5.follow(u2)
    #     u5.follow(u3)  # john follows david
    #     u5.follow(u4)  # john follows david

    #     u1.follow(u5)
    #     u2.follow(u5)
    #     u3.follow(u5)
    #     # u1.unfollow(u2)
    #     # u1.unfollow(u3)
    #     db.session.commit()

    return myapp
