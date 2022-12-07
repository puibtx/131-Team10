from flask import Blueprint, render_template, flash, redirect, url_for, request, jsonify
from flask_login import login_required, current_user
from .models import User, Post
from . import db
import json
from .forms import DeleteForm

views = Blueprint('routes', __name__)


@views.route('/delete')
@login_required
def delete():
    print('hi')
    delete_user = User.query.filter_by(id=current_user.id).first()

    try:

        db.session.delete(delete_user)
        db.session.commit()
        flash('account deleted')
        return redirect(url_for('auth.login'))

    except:
        flash('failed to delete account')


"""""
@views.route('/home')
@login_required
def user_home():
    return render_template('index.html', user=current_user)
"""""


@views.route('/home/<username>/post', methods=['GET', 'POST'])
@login_required
def post(username):
    if request.method == 'POST':
        post = request.form.get('post')

        if len(post) > 250:
            flash('Text no more than 250 characters!', category='error')
        else:
            new_post = Post(data=post, user_id = current_user.id)
            db.session.add(new_post)
            db.session.commit()
            flash('Post uploaded', category='success')


    return render_template('post.html', user=current_user, username=username)

@views.route('/delete-post', methods = ['POST'])
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

@views.route('/dashboard/<username>', methods=['GET', 'POST'])
@login_required
def dashboard(username):

    return render_template('home.html', username=username)


@views.route('/home/<username>', methods=['GET', 'POST'])
@login_required
def home(username):

    return render_template('profile.html', username=username)
