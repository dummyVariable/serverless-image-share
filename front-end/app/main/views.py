
from flask import render_template, redirect

from app.main import main
from .forms import PostForm

'''
image = {
    'title',
    'user',
    'url',
    'fullUrl',
    'orgUrl',
    'tags',
    'date'
}
'''


@main.route('/')
def index():
    images = None # function to fetch all images
    return render_template("index.html", images=images)

@main.route('/image/<id>', methods=['GET', 'POST'])
def post(id):
    image = None # function to fetch the image with id
    return render_template('image.html', image=image)
