from flask import render_template, redirect, flash, url_for
from flask_login import login_required, login_user, logout_user, current_user

from app.auth import auth
from app.auth.forms import LoginForm, RegisterForm
from app.models import User, db


@auth.route('/login', methods=['POST','GET'])
def login():
    if current_user.is_active:
        return redirect('/')    
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.query.filter_by(username=username).first()
        if user and user.verify_password(password):
            login_user(user, remember=1)
            return redirect('/')
        flash('Incorrect details')
    return render_template('/auth/login.html', form=form)

@auth.route('/register', methods=['POST','GET'])
def register():
    if current_user.is_active:
        return redirect('/')
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.query.filter_by(username=username).first()
        if not user:
            user = User(username=username)
            user.password = password
            db.session.add(user)
            db.session.commit()
            flash('You can login now')
            return redirect(url_for('auth.login'))
        flash('Username exists')
    return render_template('/auth/register.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))