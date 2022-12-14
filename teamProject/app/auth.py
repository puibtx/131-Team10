from flask import Blueprint, render_template, request, flash, redirect, url_for
from .forms import LoginForm, SignupForm
from .models import User
from . import db
from flask_login import logout_user, login_required, login_user, current_user

from werkzeug.security import generate_password_hash, check_password_hash
# created auth for user authorization such login and sign up


auth = Blueprint('auth', __name__)

# our sign in page


@auth.route("/", methods=['GET', 'POST'])
@auth.route("/signin", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    # if post method then we request items
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        remember = request.form.get('remember_me')
        # search for the user in the db
        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            login_user(user, remember=remember)
            flash('Success! welcome', category='success')
            # if user exist we redirect the user to their home page with their username
            return redirect(url_for('routes.home', username=user.get_username()))
        else:
            flash('invalid email or password!', category='error')
    return render_template("signin.html", form=form)

# to log out the user


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

# used to sign up users (create)


@auth.route("/signup", methods=['GET', 'POST'])
def signup():
    form = SignupForm()

    if request.method == 'POST' and form.validate_on_submit():
        email = request.form.get('email')
        username = request.form.get('username')

        email_check = User.query.filter_by(email=email).first()
        name_check = User.query.filter_by(username=username).first()
        # check if username or email already exists
        if email_check:
            flash('email already in use.', category='error')
            return render_template("signup.html", form=form)

        if name_check:
            flash('username already in use.', category='error')
            return render_template("signup.html", form=form)

        # if no error we create the user and save in the db
        password = request.form.get('password')

        hashed_password = generate_password_hash(
            password, method='sha512')
        user = User(email=email,
                    username=username, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Success! welcome', category='success')
        # redirect to login
        return redirect(url_for('auth.login'))

    return render_template("signup.html", form=form)
