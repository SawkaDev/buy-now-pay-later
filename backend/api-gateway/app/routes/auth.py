from flask import Flask, request, jsonify, session, Blueprint
from flask_session import Session
from app.services.service_registry import services
import requests

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/auth/register', methods=['POST'])
def register():
    data = request.json
    response = requests.post(f'http://user-service:4000/user-service/v1/auth/register', json=data)
    
    if response.status_code == 201:
        return jsonify({"message": "User registered successfully"}), 201
    elif response.status_code == 400:
        return jsonify(response.json()), 400
    else:
        return jsonify({"message": "Registration Issue"}), response.status_code

@auth_bp.route('/auth/login', methods=['POST'])
def login():
    data = request.json
    response = requests.post(f'http://user-service:4000/user-service/v1/auth/login', json=data)
    if response.status_code == 200:
        user_data = response.json()
        if user_data.get('user'):
            session['user_id'] = user_data['user']['id']
            return jsonify({"message": "Logged in successfully",'user': user_data['user']}), 200
    return jsonify({"message": "Invalid credentials"}), 401

@auth_bp.route('/auth/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)
    return jsonify({"message": "Logged out"}), 200

@auth_bp.route('/auth/session', methods=['GET'])
def get_session():
    if 'user_id' in session:
        return jsonify(session['user_id'])
    return jsonify({'message': 'No valid session'}), 401