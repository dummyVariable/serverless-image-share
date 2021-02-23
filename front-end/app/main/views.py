
from flask import render_template, redirect, url_for, request, flash

from app.main import main
from app.main.forms import UploadForm
from app.main.model import save_to_S3, get_all_images, get_image_by_id, get_image_by_tag

from app.auth.model import is_logged
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
    images = get_all_images()
    return render_template("index.html", images=images)

@main.route('/image/<id>', methods=['GET', 'POST'])
def image(id: int):
    image = get_image_by_id(id)
    return render_template('image.html', image=image)

@main.route('/upload', methods=['GET', 'POST'])
def upload():
    form = UploadForm()
    if form.validate_on_submit():
        if not is_logged:
            flash('Login to upload')
            return redirect(url_for('auth.login'))
        filename = form.title.data
        image = form.image.data.read()
        done = save_to_S3(filename, image)
        if not done:
            flash('Something went wrong, Try again')
            return redirect(url_for('main.upload'))
        return redirect(url_for('main.index'))
    return render_template('upload.html', form=form)

@main.route('/search')
def search():
    tag = request.args.get('search')
    images = get_image_by_tag(tag)
    return render_template('index.html', images=images)