from flask_app import app, db
from flask_app.models import User, FormSubmission
from flask import render_template, flash, redirect, url_for, request
from flask_app.forms import LoginForm, RegistrationForm, GeneralForm
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse


@app.route('/')
def index():  # Home page
    return render_template('index.html', title='Home')


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
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':  # Ensure relative URL
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', titlw='Sign In', form=form)  # Validation errors will print


@app.route('/logout')  # Only visible if logged in
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/resources')
def resources():
    return render_template('index.html')


@app.route('/stats')
@login_required
def stats():
    return render_template('index.html')


@app.route('/forms')
def forms():
    return render_template('forms.html')


@app.route('/physical')
def phys_health_form():
    form = GeneralForm()
    if form.validate_on_submit():
        name = form.name.data or 'Anonymous'
        contact = form.contact.data or 'No Response'
        submission = FormSubmission(name=name, contact=contact, body=form.body.data)
        db.session.add(submission)
        db.session.commit()
        flash('Post successful!')
        return redirect(url_for('forms'))
    return render_template('phys_health_form.html', form=form)


@app.route('/mental')
def mental_health_form():
    form = GeneralForm()
    if form.validate_on_submit():
        name = form.name.data or 'Anonymous'
        contact = form.contact.data or 'No Response'
        submission = FormSubmission(name=name, contact=contact, body=form.body.data)
        db.session.add(submission)
        db.session.commit()
        flash('Post successful!')
        return redirect(url_for('forms'))
    return render_template('mental_health_form.html', form=form)


@app.route('/hazard')
def hazard_report_form():
    form = GeneralForm()
    if form.validate_on_submit():
        name = form.name.data or 'Anonymous'
        contact = form.contact.data or 'No Response'
        submission = FormSubmission(name=name, contact=contact, body=form.body.data)
        db.session.add(submission)
        db.session.commit()
        flash('Post successful!')
        return redirect(url_for('forms'))
    return render_template('hazard_report.html', form=form)


@app.route('/diversity')
def diversity_form():
    form = GeneralForm()
    if form.validate_on_submit():
        name = form.name.data or 'Anonymous'
        contact = form.contact.data or 'No Response'
        submission = FormSubmission(name=name, contact=contact, body=form.body.data)
        db.session.add(submission)
        db.session.commit()
        flash('Post successful!')
        return redirect(url_for('forms'))
    return render_template('diversity_feedback.html', form=form)


@app.route('/resourceform')
def resource_form():
    form = GeneralForm()
    if form.validate_on_submit():
        name = form.name.data or 'Anonymous'
        contact = form.contact.data or 'No Response'
        submission = FormSubmission(name=name, contact=contact, body=form.body.data)
        db.session.add(submission)
        db.session.commit()
        flash('Post successful!')
        return redirect(url_for('forms'))
    return render_template('health_resource.html', form=form)


@app.route('/misc')
def misc_form():
    form = GeneralForm()
    if form.validate_on_submit():
        name = form.name.data or 'Anonymous'
        contact = form.contact.data or 'No Response'
        submission = FormSubmission(name=name, contact=contact, body=form.body.data)
        db.session.add(submission)
        db.session.commit()
        flash('Post successful!')
        return redirect(url_for('forms'))
    return render_template('misc_request.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:  # Logged in already
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Sign up successful!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)
