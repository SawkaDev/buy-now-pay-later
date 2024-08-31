from flask import Blueprint, jsonify, request
from client.v1.credit import CreditClientV1
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

@credit_bp.route('/api/credit-service/profile/<string:user_id>', methods=['GET'])
def get_credit_profile(user_id):
    try:
        response = credit_client.get_credit_profile(user_id)
        result = MessageToDict(response, preserving_proto_field_name=True)
        return jsonify(result), 200
    except grpc.RpcError as e:
        error_messages = {
            grpc.StatusCode.NOT_FOUND: ('Credit profile not found', 404),
            grpc.StatusCode.INTERNAL: ('Internal server error', 500)
        }
        message, status_code = error_messages.get(e.code(), (str(e.details()), 500))
        return jsonify({'error': message}), status_code

@credit_bp.route('/api/credit-service/profile/<string:user_id>', methods=['PUT'])
def update_credit_profile(user_id):
    data = request.get_json()
    data['user_id'] = user_id
    
    try:
        response = credit_client.update_credit_profile(**data)
        result = MessageToDict(response, preserving_proto_field_name=True)
        return jsonify(result), 200
    except grpc.RpcError as e:
        error_messages = {
            grpc.StatusCode.NOT_FOUND: ('Credit profile not found', 404),
            grpc.StatusCode.INVALID_ARGUMENT: ('Invalid input', 400),
            grpc.StatusCode.INTERNAL: ('Internal server error', 500)
        }
        message, status_code = error_messages.get(e.code(), (str(e.details()), 500))
        return jsonify({'error': message}), status_code

@credit_bp.route('/api/credit-service/profile/<string:user_id>/score', methods=['GET'])
def get_credit_score(user_id):
    try:
        response = credit_client.get_credit_profile(user_id)
        return jsonify({'credit_score': response.credit_score}), 200
    except grpc.RpcError as e:
        error_messages = {
            grpc.StatusCode.NOT_FOUND: ('Credit profile not found', 404),
            grpc.StatusCode.INTERNAL: ('Internal server error', 500)
        }
        message, status_code = error_messages.get(e.code(), (str(e.details()), 500))
        return jsonify({'error': message}), status_code

@credit_bp.route('/api/credit-service/profile/<string:user_id>/risk', methods=['GET'])
def get_credit_risk(user_id):
    try:
        response = credit_client.calculate_credit_risk(user_id)
        return jsonify({'credit_risk': response.risk_level}), 200
    except grpc.RpcError as e:
        error_messages = {
            grpc.StatusCode.NOT_FOUND: ('Credit profile not found', 404),
            grpc.StatusCode.INTERNAL: ('Internal server error', 500)
        }
        message, status_code = error_messages.get(e.code(), (str(e.details()), 500))
        return jsonify({'error': message}), status_code
