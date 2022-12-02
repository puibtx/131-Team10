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
    if request.method == 'POST': # and form.validate():
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')
        username = request.form.get('username')
        password = request.form.get('password')
        confirm = request.form.get('confirm')
        if password != confirm:
            flash("Passwords don't match")
        else:
            new_user = User(email=email, first_name=first_name, last_name=last_name,
                            username=username, password=generate_password_hash(password, method='sha512'))
            db.session.add(new_user)
            db.session.commit()

            flash('Success! welcome')
            return redirect(url_for('auth.login'))
    return render_template("signup.html", form=form)
