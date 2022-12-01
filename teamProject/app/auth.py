from flask import Blueprint, render_template, request, flash, redirect, url_for
from .forms import LoginForm, SignupForm
from .models import User
from . import db

from werkzeug.security import generate_password_hash, check_password_hash
# pages here are for login, signup, etc...

auth = Blueprint('auth', __name__)


@auth.route("/")
@auth.route("/signin", methods=['GET', 'POST'])
def login():
    form = LoginForm()

    return render_template("signin.html", form=form)


@auth.route("/signup", methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if request.method == 'POST' and form.validate():
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        lastName = request.form.get('lastName')
        username = request.form.get('username')
        password = request.form.get('password')
        new_user = User(email=email, firstName=firstName, lastName=lastName,
                        username=username, password=generate_password_hash(password, method='sha512'))
        db.session.add(new_user)
        db.session.commit()

        flash('Succes! welcome')
        return redirect(url_for('auth.signin'))
    return render_template("signup.html", form=form)
