from flask import Blueprint, jsonify, request
from client.v1 import APIKeyClientV1
from google.protobuf.json_format import MessageToDict

api_key_bp = Blueprint('api_key', __name__)

# Initialize the APIKeyClientV1
api_key_client = APIKeyClientV1(host='merchant-integration-service', port=50051)

@api_key_bp.route('/api/merchant-integration-service/key/generate', methods=['POST'])
def generate_api_key():
    data = request.get_json()
    user_id = data.get('user_id')

    if not user_id:
        return jsonify({'error': 'User ID is required'}), 400

    try:
        response = api_key_client.generate_api_key(user_id)
        api_key_dict = MessageToDict(response.api_key,preserving_proto_field_name=True)
        return jsonify({'message': 'API key generated successfully', 'api_key': api_key_dict}), 201
    except Exception as e:
        return jsonify({'error': str(e.details())}), 500

@api_key_bp.route('/key/validate', methods=['POST'])
def validate_api_key():
    data = request.get_json()
    key_id = data.get('key_id')

    if not key_id:
        return jsonify({"error": "API key is required"}), 400

    try:
        response = api_key_client.validate_api_key(key_id)
        return jsonify({"message": response.message, "is_valid": response.is_valid}), 200 if response.is_valid else 403
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@api_key_bp.route('/api/merchant-integration-service/key/revoke', methods=['POST'])
def revoke_api_key():
    data = request.get_json()
    key_id = data.get('key_id')

    try:
        key_id = int(key_id)  # Convert to integer
    except ValueError:
        return jsonify({'error': 'Key ID must be an integer'}), 400

    try:
        response = api_key_client.revoke_api_key(key_id)
        return jsonify({'message': response.message}), 200 if response.success else 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500
        

@api_key_bp.route('/api/merchant-integration-service/keys/<int:user_id>', methods=['GET'])
def get_api_keys_for_user(user_id):
    try:
        response = api_key_client.get_api_keys_for_user(user_id)
        api_keys = [MessageToDict(key, preserving_proto_field_name=True) for key in response.api_keys]
        return jsonify({'api_keys': api_keys}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ... (keep other existing routes)
