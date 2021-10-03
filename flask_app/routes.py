from flask_app import app
from flask_app.models import User
from flask import render_template, flash, redirect, url_for
from flask_app.forms import LoginForm
from flask_login import current_user, login_user


@app.route('/')
def index():  # Home page
    user = {'username: Admin'}
    return render_template('index.html', title='Home', user=user)


@app.route('/login', methods=['GET', 'POST'])
def login():  # Login page
    if current_user.is_authenticated:  # If logged in already, redirect
        flash('Logged in already!')
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):  # If wrong username or password
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', titlw='Sign In', form=form)  # Validation errors will print
