from flask import Blueprint, jsonify, request
from client.v1.loan import LoanClientV1
from google.protobuf.json_format import MessageToDict
import grpc
from grpc import StatusCode

loan_bp = Blueprint('loan', __name__)

# Initialize the LoanClientV1
loan_client = LoanClientV1(host='loan-service', port=50052)

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