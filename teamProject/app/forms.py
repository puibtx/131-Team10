from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, BooleanField, SubmitField, StringField
from wtforms.validators import ValidationError, DataRequired, EqualTo, Length
from .models import User

class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


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

    def validate_email(self, email):
        user_object = User.query.filter_by(email=email.data).first()
        if user_object:
            raise ValidationError("Email already taken. Please pick a different Email address.")

    def validate_username(self, username):
        user_object = User.query.filter_by(username=username.data).first()
        if user_object:
            raise ValidationError("Username already exists. Please pick a different username.")