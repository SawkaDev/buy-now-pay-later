from flask import Blueprint, jsonify, request
from client.v1.loan import LoanClientV1
from google.protobuf.json_format import MessageToDict
import grpc
from grpc import StatusCode

loan_bp = Blueprint('loan', __name__)

# Initialize the LoanClientV1
loan_client = LoanClientV1(host='loan-service', port=50052)

@loan_bp.route('/api/loan-service/loan/<int:loan_id>', methods=['GET'])
def get_loan(loan_id):
    try:
        response = loan_client.get_loan(loan_id)
        
        result = {
            **MessageToDict(response, preserving_proto_field_name=True)
        }
    
        return jsonify(result), 200
    except grpc.RpcError as e:
        error_messages = {
            grpc.StatusCode.NOT_FOUND: ('Loan not found', 404),
            grpc.StatusCode.INTERNAL: ('Internal server error', 500)
        }
        message, status_code = error_messages.get(e.code(), (str(e.details()), 500))
        return jsonify({'error': message}), status_code

@loan_bp.route('/api/loan-service/loan/status/update', methods=['POST'])
def update_loan_status():
    data = request.get_json()
    loan_id = data.get('loan_id')
    new_status = data.get('new_status')

    if not loan_id or not new_status:
        return jsonify({'error': 'Loan ID and new status are required'}), 400

    try:
        response = loan_client.update_loan_status(loan_id, new_status)
        loan_dict = MessageToDict(response.loan, preserving_proto_field_name=True)
        return jsonify({'message': 'Loan status updated successfully', 'loan': loan_dict}), 200
    except grpc.RpcError as e:
        status_code = e.code()
        if status_code == StatusCode.NOT_FOUND:
            return jsonify({'error': 'Loan not found'}), 404
        elif status_code == StatusCode.INVALID_ARGUMENT:
            return jsonify({'error': 'Invalid loan status'}), 400
        elif status_code == StatusCode.INTERNAL:
            return jsonify({'error': 'Internal server error'}), 500
        else:
            return jsonify({'error': str(e.details())}), 500

@loan_bp.route('/api/loan-service/loan/payment/update', methods=['POST'])
def update_payment():
    data = request.get_json()
    loan_id = data.get('loan_id')
    payment_status = data.get('payment_status')

    if not loan_id or not payment_status:
        return jsonify({'error': 'Loan ID and payment status are required'}), 400

    try:
        response = loan_client.update_payment(loan_id, payment_status)
        if response.success:
            return jsonify({'message': 'Payment updated successfully'}), 200
        else:
            return jsonify({'error': 'Failed to update payment'}), 400
    except grpc.RpcError as e:
        status_code = e.code()
        if status_code == StatusCode.NOT_FOUND:
            return jsonify({'error': 'Loan not found'}), 404
        elif status_code == StatusCode.INVALID_ARGUMENT:
            return jsonify({'error': 'Invalid payment status'}), 400
        elif status_code == StatusCode.INTERNAL:
            return jsonify({'error': 'Internal server error'}), 500
        else:
            return jsonify({'error': str(e.details())}), 500

@loan_bp.route('/api/loan-service/checkout/generate', methods=['POST'])
def generate_checkout_session():
    data = request.get_json()
    loan_amount_cents = data.get('loan_amount_cents')
    merchant_id = data.get('merchant_id')
    order_id = data.get('order_id')
    success_redirect_url = data.get('success_redirect_url')
    cancel_redirect_url = data.get('cancel_redirect_url')

    if not all([loan_amount_cents, merchant_id, order_id, success_redirect_url, cancel_redirect_url]):
        return jsonify({'error': 'Missing required fields'}), 400

    try:
        response = loan_client.generate_checkout_session(
            loan_amount_cents, 
            merchant_id, order_id, success_redirect_url, cancel_redirect_url
        )
        return jsonify({'checkout_url': response.checkout_url}), 200
    except grpc.RpcError as e:
        status_code = e.code()
        if status_code == StatusCode.INVALID_ARGUMENT:
            return jsonify({'error': 'Invalid arguments'}), 400
        elif status_code == StatusCode.PERMISSION_DENIED:
            return jsonify({'error': 'Permission denied'}), 403
        elif status_code == StatusCode.INTERNAL:
            return jsonify({'error': 'Internal server error'}), 500
        else:
            return jsonify({'error': str(e.details())}), 500

@loan_bp.route('/api/loan-service/loan-options', methods=['POST'])
def get_loan_options():
    data = request.get_json()
    user_id = data.get('user_id')
    session_id = data.get('session_id')

    if not user_id or not session_id:
        return jsonify({'error': 'User ID and session ID are required'}), 400

    try:
        response = loan_client.get_loan_options(user_id, session_id)
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
