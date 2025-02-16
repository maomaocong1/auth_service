from flask import request, jsonify
from ..models.user import User
from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

bcrypt = Bcrypt()

def login_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400

    user = User.query.filter_by(username=username).first()

    if not user or not user.check_password(password):
        return jsonify({'error': 'Invalid username or password'}), 401  # Unauthorized

    # Create access token (JWT)
    access_token = create_access_token(identity=user.username)  # Use username as identity

    return jsonify({'access_token': access_token}), 200

@jwt_required()  # Example protected route
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

def logout_user():
    # In a real application, you might want to implement token revocation or blacklisting
    # For this simple example, we just return a success message
    return jsonify({"message": "Logged out successfully"}), 200