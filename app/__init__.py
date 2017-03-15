from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = "os.urandom(24)"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://lab5:password@localhost/lab5"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning

DEBUG= 'True'
SECRET_KEY= 'secretkey'
UPLOAD_FOLDER = "./app/static/uploads"

db = SQLAlchemy(app)

# Flask-Login login manager
userprofile = LoginManager()
userprofile.init_app(app)
#login_manager.login_view='login'

app.config.from_object(__name__)
from app import views
