from flask import Blueprint, jsonify, request
from app.models.api_key import APIKey
from app.models.user import User
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

    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    active_api_keys_count = APIKey.query.filter_by(user_id=user.id, is_active=True).count()

    if active_api_keys_count >= 5:
        return jsonify({'error': 'Maximum number of active API keys has been reached.'}), 400

    new_key = APIKey(
        key=create_api_key_token(),
        user=user,
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

    api_key = APIKey.query.filter_by(id=api_key_id).first()

    if api_key:
        api_key.check_expiration()
        if api_key.is_active:
            # Use the API key
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
