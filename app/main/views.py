from flask import render_template
from . import main
from flask_login import login_required, current_user

@main.route('/')
def index():
    '''
    View function that returns the index template and its data
    '''
    return render_template('index.html')


@main.route('/profile/')
@login_required
def profile():
    '''
    Root function that return the logged in user profile template and its data
    '''
    pass

