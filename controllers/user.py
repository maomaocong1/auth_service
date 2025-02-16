from flask import request, jsonify
from ..models.user import User
from flask_bcrypt import Bcrypt
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..database import db, init_db # Import your db instance

bcrypt = Bcrypt()

def register_user():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if User.query.filter_by(username=username).first():
        return jsonify({'error': 'Username already exists'}), 400
    if User.query.filter_by(email=email).first():
        return jsonify({'error': 'Email already exists'}), 400

    new_user = User(username=username, email=email)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.to_dict()), 201

@jwt_required()
def get_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    if user:
        return jsonify(user.to_dict()), 200
    return jsonify({'message': 'User not found'}), 404

@jwt_required()
def update_user(user_id):
    current_user = get_jwt_identity()
    user = User.query.filter_by(id=user_id).first()

    if not user:
        return jsonify({'message': 'User not found'}), 404

    if current_user != user.username:  # Authorization check
        return jsonify({"message": "Unauthorized"}), 403

    data = request.get_json()
    user.email = data.get('email', user.email)  # Use current value as default
    user.username = data.get('username', user.username)
    password = data.get('password')
    if password:
        user.set_password(password)

    db.session.commit()
    return jsonify(user.to_dict()), 200


@jwt_required()
def delete_user(user_id):
    current_user = get_jwt_identity()
    user = User.query.filter_by(id=user_id).first()

    if not user:
        return jsonify({'message': 'User not found'}), 404

    if current_user != user.username: # Authorization check
        return jsonify({"message": "Unauthorized"}), 403

    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted'}), 204