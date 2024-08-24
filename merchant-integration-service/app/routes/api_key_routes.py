from flask import Blueprint, jsonify, request
from app.models.api_key import APIKey
from app.extensions import db
from datetime import datetime, timedelta
import secrets

api_key_bp = Blueprint('api_key', __name__)

def create_api_key_token():
    return secrets.token_urlsafe(32)

@api_key_bp.route('/key/generate', methods=['POST'])
def generate_api_key():
    data = request.get_json()
    user_id = data.get('user_id')

    if not user_id:
        return jsonify({'error': 'User ID is required'}), 400

    active_api_keys_count = APIKey.query.filter_by(user_id=user_id, is_active=True).count()

    if active_api_keys_count >= 5:
        return jsonify({'error': 'Maximum number of active API keys has been reached.'}), 400

    new_key = APIKey(
        key=create_api_key_token(),
        user_id=user_id,
        expires_at=datetime.utcnow() + timedelta(days=30)  # Key expires in 30 days
    )

    db.session.add(new_key)
    db.session.commit()

    return jsonify({'message': 'API key generated successfully', 'api_key': new_key.json()}), 201

@api_key_bp.route('/key/validate', methods=['POST'])
def validate_api_key():
    data = request.get_json()
    api_key_value = data.get('key_id')

    if not api_key_value:
        return jsonify({"error": "API key is required"}), 400

    api_key = APIKey.query.filter_by(key=api_key_value).first()

    if api_key:
        api_key.check_expiration()
        if api_key.is_active:
            return jsonify({"message": "API key is valid"}), 200
        else:
            return jsonify({"error": "API key has expired"}), 403
    return jsonify({"error": "Invalid API key"}), 404

@api_key_bp.route('/key/revoke', methods=['POST'])
def revoke_api_key():
    data = request.get_json()
    key_id = data.get('key_id')

    if not key_id:
        return jsonify({'error': 'Key ID is required'}), 400

    api_key = APIKey.query.get(key_id)
    if not api_key:
        return jsonify({'error': 'API key not found'}), 404

    if not api_key.is_active:
        return jsonify({'error': 'API key is already inactive'}), 400

    api_key.is_active = False
    db.session.commit()

    return jsonify({'message': 'API key revoked successfully'}), 200

@api_key_bp.route('/keys/<int:user_id>', methods=['GET'])
def get_api_keys_for_user(user_id):
    api_keys = APIKey.query.filter_by(user_id=user_id).all()
    if not api_keys:
        return jsonify({'error': 'No API keys found for the user'}), 404

    return jsonify({'api_keys': [key.json() for key in api_keys]}), 200
