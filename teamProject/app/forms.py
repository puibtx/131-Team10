from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, BooleanField, SubmitField, StringField
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
    password = PasswordField('Password', validators=[InputRequired()])
    confirm = PasswordField('Confirm Password', validators=[InputRequired(), EqualTo(
        password, message='Passwords must match')])
    create = SubmitField('Create Account')
