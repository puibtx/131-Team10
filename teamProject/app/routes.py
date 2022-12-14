from flask import current_app, Blueprint, render_template, flash, redirect, url_for, request
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from .forms import SignupForm, UploadForm
from PIL import Image
import uuid as uuid
import config
import os
import pathlib


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


@views.route('/home/<username>/post', methods=['GET', 'POST'])
@login_required
def post(username):
    form = UploadForm()

    if request.method == 'POST' and form.validate_on_submit():
        post = request.form.get('post')
        image_id = None
        image = request.files['image']
        if image:
            try:
                image_id = str(uuid.uuid1()) + "_" + secure_filename(image.filename)
                image.save(os.path.join(current_app.config['UPLOAD_FOLDER'], image_id))
                new_post = Post(data=post, user_id=current_user.id, image=image_id)
                db.session.add(new_post)
                db.session.commit()
                flash('Post uploaded', category='success')
                return redirect(url_for('routes.home', username=username))

            except OSError as err:
                print("OS error:", err)
                flash('fail')
    
        if len(post) > 250:
            flash('Text no more than 250 characters!', category='error')
        else:
            new_post = Post(data=post, user_id=current_user.id, image=image_id)
            db.session.add(new_post)
            db.session.commit()
            flash('Post uploaded', category='success')
            return redirect(url_for('routes.home', username=username))

    return render_template('post.html', user=current_user, username=username, form=form)


@views.route('/home/<username>/delete-post/<int:id>')
@login_required
def deletePost(id, username):
    deleted_post = Post.query.get_or_404(id)
    db.session.delete(deleted_post)
    db.session.commit()

    return redirect(url_for('routes.home', username=username))


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
    profile_pic = user.get_pic()

    return render_template('home.html', username=current_user.username, userhome=current_user.username, bio=bio, posts=posts, profile_pic=profile_pic)


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
    profile_pic = other_user.get_pic()
    following = current.is_following(other_user)
    return render_template(
        'home.html', username=current_user.username, userhome=other_username, bio=bio, posts=posts, following=following, profile_pic=profile_pic)


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


@views.route('/update-info/<username>', methods=['GET', 'POST'])
@login_required
def update(username):
    form = SignupForm()
    update_user = User.query.filter_by(
        username=current_user.username).first()

    if request.method == 'POST':

        update_user.username = request.form.get('username')
        update_user.update_bio(request.form.get('bio'))
        if request.files['profile_pic']:
            print('profile_pic')

            update_user.profile_pic = request.files['profile_pic']

            # update_user.profile_pic = request.files['profile_pic']
            pic_filename = secure_filename(update_user.profile_pic.filename)
            # create a random name
            pic_name = str(uuid.uuid1()) + "_" + pic_filename
            # save pic at location in init

            # save profile_pic string
            update_user.profile_pic = pic_name

            save_file = request.files['profile_pic']
            try:

                db.session.commit()

                save_file.save(os.path.join(
                    current_app.config['UPLOAD_FOLDER'], pic_name))

                flash('update changed')

                return redirect(url_for('routes.home', username=username))
            except OSError as err:
                print("OS error:", err)
                flash('fail')
                return render_template('update.html', username=username, form=form, update_user=update_user)
        db.session.commit()
        return redirect(url_for('routes.home', username=username))
    return render_template('update.html', username=username, form=form,  update_user=update_user, bio=update_user.get_bio())
