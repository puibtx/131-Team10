from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from wtforms import EmailField, PasswordField, BooleanField, SubmitField, StringField
from wtforms.validators import DataRequired, EqualTo, Length
from datetime import datetime

db = SQLAlchemy()

class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
    # username = UsernameField('Username', validators=[DataRequired()])


class SignupForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    # firstName = StringField(
    # 'First Name', validators=[DataRequired(), Length(min=2, max=15)])
    # lastName = StringField(
    # 'Last Name', validators=[
    # DataRequired(), Length(min=2, max=15)])
    username = StringField('Username', validators=[DataRequired(), Length(
        min=6, message='Username must be at least %(min)d')])
    password = PasswordField('Password', validators=[DataRequired(), Length(
        min=6, message='Password must be at least %(min)d')])
    confirm = PasswordField('Confirm Password', validators=[DataRequired(
        message='please confirm password'),
        EqualTo('password', message='Both password fields must be equal!')])
    create = SubmitField('Create Account')


class SearchForm(FlaskForm):
    searched = StringField('Searched', validators=[DataRequired()])
    submit = SubmitField('Submit')
    
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    recipient_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<Message {}>'.format(self.body)
