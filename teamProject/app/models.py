from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from . import login


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), index=True, unique=True)
    username = db.Column(db.String(15), index=True, unique=True)
    first_name = db.Column(db.String(15), index=True)
    last_name = db.Column(db.String(15), index=True)
    password = db.Column(db.String(100))

    def get_username(self):
        return self.username
