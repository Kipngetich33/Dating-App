from flask import render_template
from . import main

@main.route('/')
def index():
    '''
    View function that returns the index template and its data
    '''
    return render_template('index.html')