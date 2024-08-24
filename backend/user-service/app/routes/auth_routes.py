from flask import Flask, request, jsonify, session, Blueprint
from flask_session import Session
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import User
from app.extensions import db
from sqlalchemy.exc import IntegrityError

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/auth/register', methods=['POST'])
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
        return jsonify({"message": "User registered successfully"}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "User already exists. Please return to login."}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


@auth_bp.route('/auth/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    user = User.query.filter_by(email=email).first()
    if user and check_password_hash(user.password, password):
        return jsonify({
            'message': 'Login successful',
            'user': user.json()
        }), 200
    
    return jsonify({'message': 'Invalid credentials'}), 401