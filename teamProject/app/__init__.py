from flask import Flask, render_template
from config import Config

def build_app():
    myapp = Flask(__name__)
    myapp.config["SECRET_KEY"] = 'TEAM-10-ROCKS-XD'
    from .routes import routes
    from .auth import auth

    myapp.register_blueprint(routes, url_prefix='/')
    myapp.register_blueprint(auth, url_prefix='/')

    return myapp


