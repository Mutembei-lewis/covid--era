import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 
from flask_login import LoginManager

login_manager = LoginManager()


app = Flask(__name__)


app.config['SECRET_KEY'] = 'gotthekeystothecity'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/walker/E-mobilis/trial/store.db'
app.config['SQLALCHENY_TRACK_MODIFICATION'] = False

db = SQLAlchemy(app)

Migrate(app,db)

login_manager.init_app(app)
login_manager.login_view = 'login'

