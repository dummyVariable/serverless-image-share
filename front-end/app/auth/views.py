from flask import render_template, redirect, flash, url_for

from app.auth import auth
from app.auth.forms import LoginForm, RegisterForm


@auth.route('/login', methods=['POST','GET'])
def login():
    pass

@auth.route('/register', methods=['POST','GET'])
def register():
    pass

@auth.route('/logout')
def logout():
    pass