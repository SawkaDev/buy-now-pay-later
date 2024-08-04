from flask import Blueprint, request, jsonify, make_response
from app.models import User
from app.extensions import db

user_bp = Blueprint('user', __name__)

@user_bp.route('/users', methods=['POST'])
def create_user():
    try:
        data = request.get_json()
        new_user = User(name=data['name'], email=data['email'])
        db.session.add(new_user)
        db.session.commit()
        return jsonify(new_user.json()), 201
    except Exception as e:
        return make_response(jsonify({'message': 'error creating user', 'error': str(e)}), 500)

@user_bp.route('/users', methods=['GET'])
def get_users():
    try:
        users = User.query.all()
        return jsonify([user.json() for user in users]), 200
    except Exception as e:
        return make_response(jsonify({'message': 'error getting users', 'error': str(e)}), 500)

@user_bp.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    try:
        user = User.query.get_or_404(id)
        return jsonify(user.json()), 200
    except Exception as e:
        return make_response(jsonify({'message': 'error getting user', 'error': str(e)}), 500)

@user_bp.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    try:
        user = User.query.get_or_404(id)
        data = request.get_json()
        user.name = data['name']
        user.email = data['email']
        db.session.commit()
        return jsonify({'message': 'user updated'}), 200
    except Exception as e:
        return make_response(jsonify({'message': 'error updating user', 'error': str(e)}), 500)

@user_bp.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    try:
        user = User.query.get_or_404(id)
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'user deleted'}), 200
    except Exception as e:
        return make_response(jsonify({'message': 'error deleting user', 'error': str(e)}), 500)

@user_bp.route('/user/<int:user_id>/api_keys', methods=['GET'])
def get_api_keys_for_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    api_keys = [key.json() for key in user.api_keys]
    return jsonify(api_keys), 200