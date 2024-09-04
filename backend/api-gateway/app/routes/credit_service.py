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


@credit_bp.route('/api/credit-service/loan-options', methods=['POST'])
def get_loan_options():
    data = request.get_json()
    user_id = data.get('user_id')
    session_id = data.get('session_id')

    if not user_id or not session_id:
        return jsonify({'error': 'User ID and session ID are required'}), 400

    try:
        response = credit_client.get_loan_options(user_id, session_id)
        loan_options = MessageToDict(response, preserving_proto_field_name=True)
        return jsonify(loan_options), 200
    except grpc.RpcError as e:
        status_code = e.code()
        if status_code == StatusCode.NOT_FOUND:
            return jsonify({'error': 'Loan options not found'}), 404
        elif status_code == StatusCode.INVALID_ARGUMENT:
            return jsonify({'error': 'Invalid arguments'}), 400
        elif status_code == StatusCode.INTERNAL:
            return jsonify({'error': 'Internal server error'}), 500
        else:
            return jsonify({'error': str(e.details())}), 500

@credit_bp.route('/api/credit-service/select-loan', methods=['POST'])
def select_loan():
    data = request.get_json()
    required_fields = ['user_id', 'checkout_session_id', 'loan_term_months', 
                       'interest_rate', 'monthly_payment_cents', 'total_payment_amount_cents']
    
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing required fields'}), 400

    try:
        response = credit_client.select_loan(
            user_id=data['user_id'],
            checkout_session_id=data['checkout_session_id'],
            loan_term_months=data['loan_term_months'],
            interest_rate=data['interest_rate'],
            monthly_payment_cents=data['monthly_payment_cents'],
            total_payment_amount_cents=data['total_payment_amount_cents']
        )
        response_dict = MessageToDict(response, preserving_proto_field_name=True)
        return jsonify(response_dict), 200
    except grpc.RpcError as e:
        error_messages = {
            grpc.StatusCode.INVALID_ARGUMENT: ('Invalid input', 400),
            grpc.StatusCode.NOT_FOUND: ('Loan not found', 404),
            grpc.StatusCode.INTERNAL: ('Internal server error', 500)
        }
        message, status_code = error_messages.get(e.code(), (str(e.details()), 500))
        return jsonify({'error': message}), status_code

@credit_bp.route('/api/credit-service/loan-status', methods=['GET'])
def get_loan_status():
    checkout_session_id = request.args.get('checkout_session_id')
    user_id = request.args.get('user_id')

    if not checkout_session_id or not user_id:
        return jsonify({'error': 'Checkout session ID and user ID are required'}), 400

    try:
        status = credit_client.get_loan_for_checkout_session(checkout_session_id, user_id)
        return jsonify({'status': status}), 200
    except grpc.RpcError as e:
        error_messages = {
            grpc.StatusCode.INVALID_ARGUMENT: ('Invalid input', 400),
            grpc.StatusCode.NOT_FOUND: ('Loan not found', 404),
            grpc.StatusCode.INTERNAL: ('Internal server error', 500)
        }
        message, status_code = error_messages.get(e.code(), (str(e.details()), 500))
        return jsonify({'error': message}), status_code