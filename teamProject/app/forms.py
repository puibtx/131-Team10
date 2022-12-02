from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, BooleanField, SubmitField, StringField, validators
from wtforms.validators import DataRequired, Length, InputRequired, EqualTo


class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class SignupForm(FlaskForm):
    email = EmailField('Email', validators=[InputRequired()])
    firstName = StringField(
        'First Name', validators=[InputRequired(), Length(min=2, max=15)])
    lastName = StringField('Last Name', validators=[
                           InputRequired(), Length(min=2, max=15)])
    username = StringField('Username', validators=[
                           InputRequired(), Length(min=6, max=15)])
    password = PasswordField('Password', validators = [DataRequired(), Length(min=8)], id = "password")
    confirm = PasswordField('Confirm Password', validators = [DataRequired(), EqualTo('password', message = "Passwords don't match")], id = "conpassword")
    create = SubmitField('Create Account')
