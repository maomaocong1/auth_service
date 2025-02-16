import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from .database import db,init_db

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'your_secret_key'
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY') or 'your_jwt_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or ''

migrate = Migrate(app, db)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)
init_db(app)
from .models.user import User
from .routes.user import user_bp
from .routes.login import login_bp
app.register_blueprint(user_bp)
app.register_blueprint(login_bp)

@app.route('/')
def hello():
    return "Hello, World! This is the API root."

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    app.run(debug=True, host='0.0.0.0', port=port)