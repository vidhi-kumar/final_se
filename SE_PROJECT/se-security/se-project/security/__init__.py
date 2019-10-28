from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask import render_template, url_for, flash, redirect
# from forms import Registration, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '59471c063c01'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from security import routes