from flask import Blueprint, jsonify, request
from client.v1.loan import LoanClientV1
from google.protobuf.json_format import MessageToDict
import grpc
from grpc import StatusCode

loan_bp = Blueprint('loan', __name__)

# Initialize the LoanClientV1
loan_client = LoanClientV1(host='loan-service', port=50052)

@loan_bp.route('/api/loan-service/loan/create', methods=['POST'])
def create_loan():
    data = request.get_json()
    user_id = data.get('user_id')
    loan_amount = data.get('loan_amount')
    loan_term_months = data.get('loan_term_months')
    interest_rate = data.get('interest_rate')
    purpose = data.get('purpose')
    merchant_id = data.get('merchant_id')

    if not all([user_id, loan_amount, loan_term_months, interest_rate, purpose]):
        return jsonify({'error': 'Missing required fields'}), 400

    try:
        response = loan_client.create_loan(user_id, loan_amount, loan_term_months, interest_rate, purpose, merchant_id)
        loan_dict = MessageToDict(response, preserving_proto_field_name=True)
        return jsonify({'message': 'Loan created successfully', **loan_dict}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@loan_bp.route('/api/loan-service/loan/<int:loan_id>', methods=['GET'])
def get_loan(loan_id):
    try:
        response = loan_client.get_loan(loan_id)
        loan_dict = MessageToDict(response, preserving_proto_field_name=True)
        return jsonify(**loan_dict), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@loan_bp.route('/api/loan-service/loan/status/update', methods=['POST'])
def update_loan_status():
    data = request.get_json()
    loan_id = data.get('loan_id')
    new_status = data.get('new_status')

    if not loan_id or not new_status:
        return jsonify({'error': 'Loan ID and new status are required'}), 400

    try:
        response = loan_client.update_loan_status(loan_id, new_status)
        # Convert the Loan protobuf message to a dictionary
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
        elif status_code == StatusCode.INTERNAL:
            return jsonify({'error': 'Internal server error'}), 500
        else:
            return jsonify({'error': str(e.details())}), 500
