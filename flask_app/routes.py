from flask_app import app
from flask import render_template, flash, redirect, url_for
from flask_app.forms import LoginForm


@app.route('/')
def index():
    user = {'username: Admin'}
    return render_template('index.html', title='Home', user=user)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login success')
        return redirect(url_for('index'))
    return render_template('login.html', titlw='Sign In', form=form)
