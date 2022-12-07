from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_required, current_user
from .models import User
from . import db

views = Blueprint('routes', __name__)


@views.route('/delete/<username>')
@login_required
def delete(username):

    delete_user = User.query.get_or_404(current_user.username)

    try:
        db.session.delete(delete_user)
        db.session.commit()
        flash('account deleted')
        redirect(url_for('auth.login'))

    except:
        flash('failed to delete account')


@views.route('/home/<username>')
@login_required
def user_home(username):
    return render_template('home.html', username=username)
    
    

@views.route('/home/profile', methods=['GET', 'POST'])
@login_required
def user_profile():
    return render_template('profile.html')  
  
