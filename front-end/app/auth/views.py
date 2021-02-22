from flask import render_template, redirect, flash, url_for

from app.auth import auth
from app.auth.forms import LoginForm, RegisterForm


@auth.route('/login', methods=['POST','GET'])
def login():
    pass

@auth.route('/sign-up', methods=['POST','GET'])
def sign_up():
    pass

@auth.route('/confirm-sign-up', methods=['POST','GET'])
def confirm_sign_up():
    pass

@auth.route('/logout')
def logout():
    pass