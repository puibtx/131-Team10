from flask import Blueprint, render_template, request, flash, redirect, url_for
from .forms import LoginForm, SignupForm
from .models import User
from . import db

from werkzeug.security import generate_password_hash, check_password_hash
# pages here are for login, signup, etc...

auth = Blueprint('auth', __name__)


@auth.route("/", methods=['GET', 'POST'])
@auth.route("/signin", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid login or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('homepage'))
    return render_template('signin.html', form=form)

@auth.route("/signup", methods=['GET', 'POST'])
def signup():
    form = SignupForm()

    if request.method == 'POST' and form.validate_on_submit():
        email = request.form.get('email')
        #first_name = request.form.get('firstName')
        #last_name = request.form.get('lastName')
        username = request.form.get('username')
        password = request.form.get('password')

        new_user = User(email=email,
                        username=username, password=generate_password_hash(password, method='sha512'))
        db.session.add(new_user)
        db.session.commit()

        flash('Success! welcome')
        return redirect(url_for('auth.login'))
    return render_template("signup.html", form=form)


@auth.route("/homepage", methods=['GET', 'POST'])
# @login_required
def homepage():
    return render_template("homepage.html")
    # form = UpdateAccountForm()
    # if form.validate_on_submit():
    #     if form.picture.data:
    #         picture_file = save_picture(form.picture.data)
    #         current_user.image_file = picture_file
    #     current_user.username = form.username.data
    #     current_user.email = form.email.data
    #     db.session.commit()
    #     flash('Your account has been updated!', 'success')
    #     return redirect(url_for('account'))
    # elif request.method == 'GET':
    #     form.username.data = current_user.username
    #     form.email.data = current_user.email
    # image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    # return render_template('account.html', title='Account',
    #                        image_file=image_file, form=form)

