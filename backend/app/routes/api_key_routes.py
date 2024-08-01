from flask import Blueprint, jsonify, request
from app.models.api_key import APIKey
from app.models.user import User
from app.extensions import db
from datetime import datetime, timedelta
import secrets

api_key_bp = Blueprint('api_key', __name__)

def generate_api_key():
    return secrets.token_urlsafe(32)

@api_key_bp.route('/generate_key', methods=['POST'])
def generate_key():
    data = request.get_json()
    user_id = data.get('user_id')

    if not user_id:
        return jsonify({'message': 'User ID is required'}), 400

    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404

    new_key = APIKey(
        key=generate_api_key(),
        user=user,
        expires_at=datetime.utcnow() + timedelta(days=30)  # Key expires in 30 days
    )

    db.session.add(new_key)
    db.session.commit()

    return jsonify({'message': 'API key generated successfully', 'api_key': new_key.json()}), 201