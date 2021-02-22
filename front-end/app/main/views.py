
from flask import render_template, redirect

from app.main import main
from .forms import PostForm
from app.models import Post, User, db


@main.route('/')
def index():
    pass

@main.route('/post', methods=['GET', 'POST'])
def post():
    pass
