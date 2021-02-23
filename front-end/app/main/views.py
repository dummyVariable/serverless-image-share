
from flask import render_template, redirect, url_for, request

from app.main import main
from app.main.forms import UploadForm
from app.main.model import save_to_S3
'''
image = {
    'id',
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
def image(id: int):
    image = None # function to fetch the image with id
    return render_template('image.html', image=image)

@main.route('/upload', methods=['GET', 'POST'])
def upload():
    form = UploadForm()
    if form.validate_on_submit():
        filename = form.title.data
        image = form.image.data.read()
        save_to_S3(filename, image)
        return redirect(url_for('main.index'))
    return render_template('upload.html', form=form)

@main.route('/search')
def search():
    tag = request.args.get('search')
    data = None # function for searching the tag
    return render_template('index.html', data=data)