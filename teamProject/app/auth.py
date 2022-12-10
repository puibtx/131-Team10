from flask import Blueprint, render_template, request, flash, redirect, url_for
from .forms import LoginForm, SignupForm
from .models import User
from . import db
from flask_login import logout_user, login_required, login_user, current_user

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
            return redirect(url_for('routes.home', username=user.get_username()))
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

        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if not user:
            check_username = User.query.filter_by(
                username=request.form.get('username')).first()
            if check_username:
                flash('Username already exists', category='error')
            else:
                username = request.form.get('username')
                user = User(email=email,
                            username=username, password=generate_password_hash(password, method='sha512'))
                db.session.add(user)
                db.session.commit()
                flash('Success! welcome', category='success')
                return redirect(url_for('auth.login'))

        else:
            flash('User already exists', category='error')

    return render_template("signup.html", form=form)


@auth.route('/follow/<username>', methods=['POST'])
@login_required
def follow(username):
    form = EmptyForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=username).first()
        if user is None:
            flash('User {} not found.'.format(username))
            return redirect(url_for('index'))
        if user == current_user:
            flash('You cannot follow yourself!')
            return redirect(url_for('user', username=username))
        current_user.follow(user)
        db.session.commit()
        flash('You are following {} now !'.format(username))
        return redirect(url_for('user', username=username))
    else:
        return redirect(url_for('index'))


@auth.route('/unfollow/<username>', methods=['POST'])
@login_required
def unfollow(username):
    form = EmptyForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=username).first()
        if user is None:
            flash('User {} not found.'.format(username))
            return redirect(url_for('index'))
        if user == current_user:
            flash('You cannot unfollow yourself!')
            return redirect(url_for('user', username=username))
        current_user.unfollow(user)
        db.session.commit()
        flash('You are not following {} anymore.'.format(username))
        return redirect(url_for('user', username=username))
    else:
        return redirect(url_for('index'))

# @auth.route("/home/<username>/following")
# @login_required
# def showfollowing(username):
#     # user = User.query.filter_by(username=username).first()
#     # following = user.followed
#     return render_template('following.html')
#     # return render_template('following.html',users=following)
