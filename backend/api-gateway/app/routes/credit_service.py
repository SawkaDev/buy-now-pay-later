from flask import Blueprint, jsonify, request
from credit_client.v1.credit import CreditClientV1
from google.protobuf.json_format import MessageToDict
import grpc
from grpc import StatusCode

credit_bp = Blueprint('credit', __name__)

credit_client = CreditClientV1(host='credit-service', port=50053)

@credit_bp.route('/api/credit-service/profile', methods=['POST'])
def create_credit_profile():
    data = request.get_json()
    required_fields = ['name', 'credit_score', 'number_of_accounts', 
                       'credit_utilization_ratio', 'recent_soft_inquiries', 
                       'bankruptcies', 'tax_liens', 'judgments']
    
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing required fields'}), 400

    try:
        response = credit_client.create_credit_profile(**data)
        result = MessageToDict(response, preserving_proto_field_name=True)
        return jsonify(result), 201
    except grpc.RpcError as e:
        error_messages = {
            grpc.StatusCode.INVALID_ARGUMENT: ('Invalid input', 400),
            grpc.StatusCode.INTERNAL: ('Internal server error', 500)
        }
        message, status_code = error_messages.get(e.code(), (str(e.details()), 500))
        return jsonify({'error': message}), status_code

@credit_bp.route('/api/credit-service/profiles', methods=['GET'])
def get_all_credit_profiles():
    try:
        response = credit_client.get_all_credit_profiles()
        result = MessageToDict(response, preserving_proto_field_name=True)
        return jsonify(result), 200
    except grpc.RpcError as e:
        error_messages = {
            grpc.StatusCode.INTERNAL: ('Internal server error', 500)
        }
        message, status_code = error_messages.get(e.code(), (str(e.details()), 500))
        return jsonify({'error': message}), status_code
