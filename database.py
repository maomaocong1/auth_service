# database.py
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()  # Initialize SQLAlchemy *outside* of any function

def init_db(app): # Initialize SQLAlchemy with the app
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or ''
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)  # This is the crucial line!