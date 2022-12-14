from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


followers = db.Table('followers',
                     db.Column('follower_id', db.Integer,
                               db.ForeignKey('user.id')),
                     db.Column('followed_id', db.Integer,
                               db.ForeignKey('user.id'))
                     )

# association table with follower, that keep track of the who is the follower on the follower db.column
# and using follwed_id to keep track who they are following


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(250))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), index=True, unique=True)
    username = db.Column(db.String(15), index=True, unique=True)
    password = db.Column(db.String(100))
    posts = db.relationship('Post')
    profile_pic = db.Column(db.String(), nullable=True)

    bio = db.Column(db.Text(250), nullable=True)

# many-to-many relation it link different User
# secondary config the association table, primayjoin= the left column = the followee/follower
# secnonday join = right column in the follower db, = the following/user that being followed
# backref so the right hand column has a way to "track back" it's left handside( follower column)

    followed = db.relationship(
        'User', secondary=followers,
        primaryjoin=(followers.c.follower_id == id),
        secondaryjoin=(followers.c.followed_id == id),
        backref=db.backref('followers', lazy='dynamic'), lazy='dynamic')


# i created this functions before I realized I could just use .attribute but they were helpful with multiple things through out managing and searching through our db'''


    def get_pic(self):
        return self.profile_pic

# check if the self is already following the user.
    def is_following(self, user):
        return self.followed.filter(
            followers.c.followed_id == user.id).count() > 0
# follow function

    def follow(self, user):
        if not self.is_following(user):
            self.followed.append(user)
# unfollow function

    def unfollow(self, user):
        if self.is_following(user):
            self.followed.remove(user)

    def update_bio(self, update_bio):
        self.bio = update_bio
        db.session.commit()

    def get_username(self):
        return self.username

    def get_posts(self):
        return self.posts

    def get_bio(self):
        return self.bio
