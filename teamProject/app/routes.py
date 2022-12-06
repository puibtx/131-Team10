from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import login_required, current_user
from .forms import DeleteForm
from .models import User
from . import db

views = Blueprint('routes', __name__)


@views.route('/delete')
@login_required
def delete():

    delete_user = User.query.filter_by(id=current_user.id).first()

    try:

        db.session.delete(delete_user)
        db.session.commit()
        flash('account deleted')
        return redirect(url_for('auth.login'))

    except:
        flash('failed to delete account')


@views.route('/dashboard/<username>', methods=['GET', 'POST'])
@login_required
def dashboard(username):

    return render_template('home.html', username=username)


@views.route('/home/<username>', methods=['GET', 'POST'])
@login_required
def home(username):

    return render_template('profile.html', username=username)
