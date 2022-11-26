from flask import Blueprint, render_template
# pages here are for login, signup, etc...

auth = Blueprint('auth', __name__)


@auth.route("/login")
def login():
    return render_template("login.html")


@auth.route("/signup")
def signup():
    return render_template("signup.html")
