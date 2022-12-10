from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(250))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), index=True, unique=True)
    username = db.Column(db.String(15), index=True, unique=True)
    first_name = db.Column(db.String(15), index=True)
    last_name = db.Column(db.String(15), index=True)
    password = db.Column(db.String(100))
    posts = db.relationship('Post')

    bio = db.Column(db.String(250))
    bio = 'about me'

    def update_bio(self, update_bio):
        self.bio = update_bio
        db.session.commit()

    def get_username(self):
        return self.username

    def get_posts(self):
        return self.posts

    def get_bio(self):
        return self.bio
