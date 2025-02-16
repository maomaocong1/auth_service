from flask import Blueprint

user_bp = Blueprint('user', __name__, url_prefix='/api/v1/users')

# Import the controller functions (but don't call them here!)
from ..controllers.user import register_user, get_user, update_user, delete_user

# Define the routes and associate them with the controller functions:
user_bp.add_url_rule('', methods=['POST'], view_func=register_user)
user_bp.add_url_rule('/<int:user_id>', methods=['GET'], view_func=get_user)
user_bp.add_url_rule('/<int:user_id>', methods=['PUT'], view_func=update_user)
user_bp.add_url_rule('/<int:user_id>', methods=['DELETE'], view_func=delete_user)

# ... other routes