from flask import render_template, redirect, flash, url_for

from app.auth import auth
from app.auth.forms import LoginForm, SignUpForm, ConfirmSignUpForm
from app.auth.model import login_validation, set_cookie


@auth.route('/login', methods=['POST','GET'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        token, error = login_validation(username, password)
        if error:
            return redirect(url_for('auth.login'))
        return set_cookie(token)

    return render_template('/auth/login.html', form=form)

@auth.route('/sign-up', methods=['POST','GET'])
def sign_up():
    form = SignUpForm()
    
    if form.validate_on_submit():
        return redirect(url_for('auth.confirm_sign_up'))

    return render_template('/auth/sign-up.html', form=form)

@auth.route('/confirm-sign-up', methods=['POST','GET'])
def confirm_sign_up():
    form = ConfirmSignUpForm()
    
    if form.validate_on_submit():
        return redirect(url_for('main.index'))

    return render_template('/auth/confirm-sign-up.html', form=form)


@auth.route('/logout')
def logout():
    pass