from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.template_folder = 'my_templates'
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///music.db'
app.config['SECRET_KEY'] = 'sre2oyawa7esh'
db = SQLAlchemy(app)


from musicPackage import routes


# app.app_context().push()