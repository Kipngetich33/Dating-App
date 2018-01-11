from flask import render_template, request, redirect, url_for, abort
from . import main
from ..models import User, Messages
from flask_login import login_required, current_user
from .. import db, photos
from .forms import UpdateProfile, MessageForm
from ..email import mail_message

@main.route('/')
def index():
    '''
    View function that returns the index template and its data
    '''
    return render_template('index.html')


@main.route('/Profile/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/Update/<uname>/Profile',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data
        user.age= form.age.data
        user.status= form.status.data
        user.intrested_in = form.intrested_in.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/view/all/users')
def all_users():
    all_users = User.query.filter_by(is_available=True).all()

    return render_template('view_users.html',all_users = all_users)

@main.route('/view/matches')
@login_required
def view_matches():
    all_matches = User.get_match(current_user.age)
    matches=[]
    username =[]
    for match in all_matches:
        if match.username != current_user.username:
            matches.append(match)

    return render_template('view_matches.html', matches = matches)

@main.route('/send/message/<int:id>', methods=['GET','POST'])
@login_required
def send_messages(id):
    form = MessageForm()
    if form.validate_on_submit():
        message_body = form.message.data
        message= Messages(sender= current_user.username ,message =message_body, user_id=id)
        message.save_message()


    return render_template('send_message.html',form = form )

@main.route('/view/messages')
@login_required
def view_messages():
    messages = Messages.get_messages(current_user.id)
    return render_template('view_messages.html',messages = messages)
