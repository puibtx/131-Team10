from flask import Blueprint, render_template, flash, redirect, url_for, request, jsonify
from flask_login import login_required, current_user

from .models import User, Post
from . import db
import json

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





@views.route('/dashboard/<username>/post', methods=['GET', 'POST'])
@login_required
def post(username):
    if request.method == 'POST':
        post = request.form.get('post')

        if len(post) > 250:
            flash('Text no more than 250 characters!', category='error')
        else:
            new_post = Post(data=post, user_id=current_user.id)
            db.session.add(new_post)
            db.session.commit()
            flash('Post uploaded', category='success')


    return render_template('post.html', user=current_user, username=username)


@views.route('/dashboard/<username>/delete-post/<int:id>')
@login_required
def deletePost(id, username):
    deleted_post = Post.query.get_or_404(id)
    db.session.delete(deleted_post)
    db.session.commit()
    
    return render_template('post.html', username=username, user=current_user)


@views.route('/feed/<username>', methods=['GET', 'POST'])
@login_required
def feed(username):

    return render_template('feed.html', username=username)


@views.route('/dashboard/<username>', methods=['GET', 'POST'])
@login_required
def home(username):

    return render_template('home.html', username=username)


@views.route("/search", methods=['GET', 'POST'])
@login_required
def search():
    if request.method == 'POST':
        username = request.form.get('searched')
        searched_user = User.query.filter_by(username=username).first()

        if searched_user:

            return redirect(url_for('routes.home', username=username))
        else:
            flash('user does not exist.', category='error')
