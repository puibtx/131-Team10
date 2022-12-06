from flask import Blueprint, render_template, request, flash, redirect, url_for
from .forms import LoginForm, SignupForm, SearchForm
from .models import User
from . import db
from flask_login import logout_user, login_required, login_user

from werkzeug.security import generate_password_hash, check_password_hash
# pages here are for login, signup, etc...

auth = Blueprint('auth', __name__)


@auth.route("/", methods=['GET', 'POST'])
@auth.route("/signin", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        remember = request.form.get('remember_me')
        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):

            login_user(user, remember=remember)
            return redirect(url_for('routes.user_home', username=user.get_username()))
        else:
            flash('invalid email or password!', category='error')
    return render_template("signin.html", form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route("/signup", methods=['GET', 'POST'])
def signup():
    form = SignupForm()

    if request.method == 'POST' and form.validate_on_submit():
        email = request.form.get('email')
        #first_name = request.form.get('firstName')
        #last_name = request.form.get('lastName')
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if not user:

            user = User(email=email,
                        username=username, password=generate_password_hash(password, method='sha512'))
            db.session.add(user)
            db.session.commit()
            flash('Success! welcome', category='success')
            return redirect(url_for('auth.login'))

        else:
            flash('User already exists', category='error')

    return render_template("signup.html", form=form)

@auth.route("/search", methods=['GET', 'POST'])
def search():
        form = SearchForm()
        if form.validate_on_submit():
            post.searched = form.searched.data
            return render_template("search.html",form=form,searched=post.searched)

# return render_template("search.html",form=form,searched=post.searched)
