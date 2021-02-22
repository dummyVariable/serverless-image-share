
from flask import render_template, redirect
from flask_login import current_user, login_required

from app.main import main
from .forms import PostForm
from app.models import Post, User, db


@main.route('/')
@login_required
def index():
    posts = Post.query.all()[::-1]
    return render_template('index.html', posts=posts)

@main.route('/post', methods=['GET', 'POST'])
@login_required
def post():
    form = PostForm()

    if form.validate_on_submit():
        title = form.title.data
        body = form.body.data
        post = Post(title=title,body=body, user=current_user)
        db.session.add(post)
        db.session.commit()
        return redirect('/')
    return render_template('post.html', form=form)

@main.route('/about')
@login_required
def about():
    posts = current_user.posts[::-1]
    return render_template('about.html', posts=posts)