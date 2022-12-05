from flask import Blueprint, render_template, flash, redirect, url_for
from . import login_manager
from flask_login import login_required, current_user, login_session
from .models import User
from . import db

routes = Blueprint('routes', __name__)


@routes.route('/delete/<int:id>')
@login_required
def delete(id):

    delete_user = User.query.get_or_404(current_user.id)
    username = login_session['username']

    try:
        db.session.delete(delete_user)
        db.session.commit()
        flash(f'{username} deleted successfully')
        redirect(url_for('auth.login'))

    except:
        flash('failed to delete account')
