from flask import Blueprint, render_template, flash, redirect, url_for, request, jsonify
from flask_login import login_required, current_user
from .models import User, Post
from . import db
import json

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


@views.route('/home')
@login_required
def user_home():
    return render_template('index.html', user=current_user)

@views.route('/post', methods=['GET', 'POST'])
@login_required
def post():
    if request.method == 'POST':
        post = request.form.get('post')

        if len(post) > 250:
            flash('Text up to 250 characters', category='error')
        else:
            new_post = Post(data=post, user_id = current_user.id)
            db.session.add(new_post)
            db.session.commit()
            flash('Post uploaded', category='success')
            return redirect(url_for('routes.user_home'))

    return render_template('post.html', user=current_user)

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