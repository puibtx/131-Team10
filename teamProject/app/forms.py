from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, BooleanField, SubmitField, StringField
from wtforms.validators import DataRequired, EqualTo, Length


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
