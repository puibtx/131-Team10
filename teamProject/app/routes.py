from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_required, current_user
from .models import User
from . import db

views = Blueprint('routes', __name__)


@views.route('/delete/<int:id>')
@login_required
def delete(id):

    delete_user = User.query.get_or_404(current_user.id)

    try:
        db.session.delete(delete_user)
        db.session.commit()
        flash('account deleted')
        redirect(url_for('auth.login'))

    except:
        flash('failed to delete account')


@login_required
@views.route('/home')
def user_home():
    return render_template('home.html')
