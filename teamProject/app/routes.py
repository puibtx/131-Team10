from flask import Blueprint, render_template, flash, redirect, url_for, request, jsonify
from flask_login import login_required, current_user

from .models import User, Post
from . import db
import json

from flask import Flask, render_template, request, redirect, url_for, session
from flask_socketio import SocketIO, join_room, leave_room, emit
from flask_session import Session

views = Blueprint('routes', __name__)

socketio = SocketIO(views, manage_session=False)


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


@views.route('/home/<username>/post', methods=['GET', 'POST'])
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


@views.route('/home/<username>/delete-post/<int:id>')
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


@views.route('/home/<username>/', methods=['GET', 'POST'])
@login_required
def home(username):
    user = User.query.filter_by(username=current_user.username).first()
    bio = user.get_bio()
    posts = user.get_posts()

    return render_template('home.html', username=current_user.username, userhome=current_user.username, bio=bio, posts=posts)


@views.route("/home/<username>/search", methods=['GET', 'POST'])
@login_required
def search(username):
    if request.method == 'POST':
        searched_username = request.form.get('searched')
        searched = User.query.filter_by(username=searched_username).first()

        if searched:
            current = User.query.filter_by(
                username=current_user.username).first()
            following = current.is_following(searched)
            print(following)
        # if user exists then we can redirect to that users home page
            return redirect(url_for('routes.visiting', username=current_user.username, other_user=searched_username))
        else:

            flash('user does not exist.', category='error')

    return render_template('search.html', username=current_user.username)


@views.route('/visiting/<username>/<other_user>', methods=['GET', 'POST'])
@login_required
def visiting(username, other_user):

    other_user = User.query.filter_by(username=other_user).first()
    current = User.query.filter_by(username=current_user.username).first()
    if request.method == 'POST':
        follow(current, other_user)
        return redirect(url_for('routes.visiting', username=current_user.username, other_user=other_user.get_username()))
    other_username = other_user.get_username()
    bio = other_user.get_bio()
    posts = other_user.get_posts()
    following = current.is_following(other_user)
    return render_template(
        'home.html', username=current_user.username, other_user=other_user, userhome=other_username, bio=bio, posts=posts, following=following)


def follow(current, other_user):

    if not current.is_following(other_user):
        # user toggle button and resulted in a following
        current_user.follow(other_user)
        db.session.commit()
        flash(f'followed ')

    else:
        current_user.unfollow(other_user)
        db.session.commit()
        flash(f'Unfollowed')


@views.route("/<username>/followers")
@login_required
def showfollowers(username):
    user = User.query.filter_by(username=username).first()
    followers_ = user.followers
    return render_template('followers.html', users=followers_)


@views.route("/<username>/following")
@login_required
def showfollowing(username):
    user = User.query.filter_by(username=username).first()
    following = user.followed
    # return render_template('following.html', username=username)
    return render_template('following.html', users=following)


@views.route('/home/chat', methods=['GET', 'POST'])
def chat():
    if (request.method == 'POST'):
        username = request.form['username']
        room = request.form['room']
        # Store the data in session
        session['username'] = username
        session['room'] = room
        return render_template('chat.html', session=session)
    else:
        if (session.get('username') is not None):
            return render_template('chat.html', session=session)
        else:
            return redirect(url_for('feed'))


@socketio.on('join', namespace='/chat')
def join(message):
    room = session.get('room')
    join_room(room)
    emit('status', {'msg':  session.get('username') +
         ' has entered the room.'}, room=room)


@socketio.on('text', namespace='/chat')
def text(message):
    room = session.get('room')
    emit('message', {'msg': session.get('username') +
         ' : ' + message['msg']}, room=room)


@socketio.on('left', namespace='/chat')
def left(message):
    room = session.get('room')
    username = session.get('username')
    leave_room(room)
    session.clear()
    emit('status', {'msg': username + ' has left the room.'}, room=room)
