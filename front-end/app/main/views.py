
from flask import render_template, redirect, url_for

from app.main import main
from .forms import UploadForm

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
def image(id):
    image = None # function to fetch the image with id
    return render_template('image.html', image=image)

@main.route('/upload', methods=['GET', 'POST'])
def upload():
    form = UploadForm()
    if form.validate_on_submit():
        ## upload ops
        return redirect(url_for('main.index'))
    return render_template('upload.html', form=form)