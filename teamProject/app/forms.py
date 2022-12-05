from flask_wtf import FlaskForm
<<<<<<< HEAD
from wtforms import EmailField, PasswordField, BooleanField, SubmitField, StringField, validators
from wtforms.validators import DataRequired, Length, InputRequired, EqualTo
=======
from wtforms import EmailField, PasswordField, BooleanField, SubmitField, StringField
from wtforms.validators import ValidationError, DataRequired, EqualTo, Length
>>>>>>> 84109d3c4398770d8d53c3d9f93dcc300b7326e1


class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class SignupForm(FlaskForm):
<<<<<<< HEAD
    email = EmailField('Email', validators=[InputRequired()])
    firstName = StringField(
        'First Name', validators=[InputRequired(), Length(min=2, max=15)])
    lastName = StringField('Last Name', validators=[
                           InputRequired(), Length(min=2, max=15)])
    username = StringField('Username', validators=[
                           InputRequired(), Length(min=6, max=15)])
    password = PasswordField('Password', validators = [DataRequired(), Length(min=8)], id = "password")
    confirm = PasswordField('Confirm Password', validators = [DataRequired(), EqualTo('password', message = "Passwords don't match")], id = "conpassword")
=======
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
>>>>>>> 84109d3c4398770d8d53c3d9f93dcc300b7326e1
    create = SubmitField('Create Account')
