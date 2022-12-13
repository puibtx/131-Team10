from flask import current_app, Blueprint, render_template, flash, redirect, url_for, request, jsonify
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from .forms import SignupForm
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
    if request.method == 'POST':
        post = request.form.get('post')

        if len(post) > 250:
            flash('Text no more than 250 characters!', category='error')
        else:
            new_post = Post(data=post, user_id=current_user.id)
            db.session.add(new_post)
            db.session.commit()
            flash('Post uploaded', category='success')
            return redirect(url_for('routes.home', username=username))

    return render_template('post.html', user=current_user, username=username)


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


def follow(current, other_user): #adding a button so people can follow each other 

    if not current.is_following(other_user):     #check if the user is already following or not 
        # user toggle button and resulted in a following
        current_user.follow(other_user) # if not, follow them 
        db.session.commit()  #apply change to the db 
        flash(f'followed ')

    else:
        current_user.unfollow(other_user)  #if already following 
        db.session.commit()  #if apply change to db
        flash(f'Unfollowed')


@views.route("/<username>/followers")    #create url route that redirect the user to check on their followers
@login_required                          #make sure the user is logged in 
def showfollowers(username):                               #func def and we need to take in the username 
    user = User.query.filter_by(username=username).first()     #using query.filter find the user that match with the current user name
    followers_ = user.followers                                #make followers_ the user's followers
    return render_template('followers.html', users=followers_)       #pass that followers list and pass it in


@views.route("/<username>/following")
@login_required                                #make sure the user is logged in 
def showfollowing(username):
    user = User.query.filter_by(username=username).first()    #create url route that redirect the user to check on their followering list
    following = user.followed                       #make followering_ the input user's following
    # return render_template('following.html', username=username)
    return render_template('following.html', users=following)   # pass it into the render template 


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
