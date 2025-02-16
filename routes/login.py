from flask import Blueprint

login_bp = Blueprint('login', __name__, url_prefix='/api/v1/login')

# Import the controller functions (but don't call them here!)
from ..controllers.login import login_user,protected

# Define the routes and associate them with the controller functions:
login_bp.add_url_rule('', methods=['POST'], view_func=login_user)
login_bp.add_url_rule('/protected', methods=['GET'], view_func=protected)


# ... other routes