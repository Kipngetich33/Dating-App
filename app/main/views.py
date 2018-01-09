from flask import render_template, request, redirect, url_for, abort  
from . import main
from ..models import User 
from flask_login import login_required, current_user
from .. import db
from .forms import ReviewForm,UpdateProfile

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

