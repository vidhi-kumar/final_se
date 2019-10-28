from flask import Flask
from security import app
from security.forms import RegistrationForm, LoginForm
from security.models import User, Post
from flask import render_template, url_for, flash, redirect


posts = [
    {
        'type' : 'WatchMan',
        'units' : 10,
        'date' : '10/10/19'
    },
    {
        'type' : 'BodyGuard',
        'units' : 2,
        'date' : '16/12/19'
    }
]
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for { form.username.data }', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

# @app.route('/data')
# def data():
#     return render_template('data.html', posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'ojha@gmail.com' or form.password.data == 'ojharocks':
            flash('You have been logged in', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful, Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)
