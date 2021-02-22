
from flask import render_template, redirect

from app.main import main
from .forms import PostForm

'''
image = {
    'title',
    'user',
    'url',
    'fullUrl',
    'tags',
    'date'
}
'''


@main.route('/')
def index():
    images = None # function to fetch all images
    return render_template("index.html", images=images)

@main.route('/post', methods=['GET', 'POST'])
def post():
    pass
