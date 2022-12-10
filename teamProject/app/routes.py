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
            flash('Text up to 250 characters', category='error')
        else:
            new_post = Post(data=post, user_id=current_user.id)
            db.session.add(new_post)
            db.session.commit()
            flash('Post uploaded', category='success')
            return redirect(url_for('routes.home'))

    return render_template('home.html', user=current_user)


@views.route('/delete-post', methods=['POST'])
@login_required
def deletePost():
    post = json.loads(request.data)
    postId = post['postId']
    post = Post.query.get(postId)
    if post:
        if post.user_id == current_user.id:
            db.session.delete(post)
            db.session.commit()

    return jsonify({})


@views.route('/feed/<username>', methods=['GET', 'POST'])
@login_required
def feed(username):

    return render_template('feed.html', username=username)


@views.route('/home/<username>', methods=['GET', 'POST'])
@login_required
def home(username):
    user = User.query.filter_by(username=username).first()
    return render_template('home.html', user=user)


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

# @views.route("/home/<username>/followers>")
# @login_required
# def showfollowers(username):
#     user = User.query.filter_by(username=username).first()
#     followers = user.follower

#     return render_template('followers.html',users=followers)


@views.route("/home/<username>/followers")
@login_required
def showfollowers(username):
    user = User.query.filter_by(username=username).first()
    followers_ = user.followers
    return render_template('followers.html', users=followers_)


@views.route("/home/<username>/following")
@login_required
def showfollowing(username):
    user = User.query.filter_by(username=username).first()
    following = user.followed
    # return render_template('following.html', username=username)
    return render_template('following.html', users=following)

# lmao
# @views.route("/home/<username>/followed")
# @login_required
# def search():
#     if request.method == 'POST':
