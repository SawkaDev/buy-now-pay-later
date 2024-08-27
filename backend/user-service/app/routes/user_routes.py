from flask import Blueprint, request, jsonify, make_response
from app.models import User
from app.extensions import db

user_bp = Blueprint('user', __name__)

@user_bp.route('/v1/users', methods=['POST'])
def create_user_v1():
    try:
        data = request.get_json()
        new_user = User(name=data['name'], email=data['email'])
        db.session.add(new_user)
        db.session.commit()
        return jsonify(new_user.json()), 201
    except Exception as e:
        return make_response(jsonify({'message': 'error creating user', 'error': str(e)}), 500)

@user_bp.route('/v1/users', methods=['GET'])
def get_users_v1():
    try:
        users = User.query.all()
        return jsonify([user.json() for user in users]), 200
    except Exception as e:
        return make_response(jsonify({'message': 'error getting users', 'error': str(e)}), 500)

@user_bp.route('/v1/users/<int:id>', methods=['GET'])
def get_user(id):
    try:
        user = User.query.get_or_404(id)
        return jsonify(user.json()), 200
    except Exception as e:
        return make_response(jsonify({'message': 'error getting user', 'error': str(e)}), 500)

@user_bp.route('/v1/users/<int:id>', methods=['PUT'])
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

@user_bp.route('/v1/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    try:
        user = User.query.get_or_404(id)
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'user deleted'}), 200
    except Exception as e:
        return make_response(jsonify({'message': 'error deleting user', 'error': str(e)}), 500)

@user_bp.route('/v1/user/register', methods=['POST'])
def register():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    name = data.get('name')
    
    if not email or not password or not name:
        return jsonify({"error": "Email, password, and name are required"}), 400
    
    hashed_password = generate_password_hash(password)
    
    new_user = User(
        email=email,
        password=hashed_password,
        name=name
    )
    
    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({
            "message": "User registered successfully",
            "user": new_user.json()
        }), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "User already exists"}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
