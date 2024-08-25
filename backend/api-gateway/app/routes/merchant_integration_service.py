from flask import Blueprint, jsonify, request
from google.protobuf.json_format import MessageToDict
from client.v1 import WebhookClientV1
import uuid
import time
from app.utils.logging_utils import log_request_info, log_response_info, logger
import logging

logger = logging.getLogger(__name__)


webhook_bp = Blueprint('webhook', __name__)
webhook_client = WebhookClientV1(host='merchant-integration-service', port=50051)

@webhook_bp.route('/api/merchant-integration-service/webhooks/user/<int:user_id>', methods=['GET'])
def get_webhooks(user_id):
    
    request_id = str(uuid.uuid4())
    start_time = time.time()
    log_request_info(request_id, 'merchant-integration-service', f'get_webhooks/{user_id}')
    try:
        response = webhook_client.get_webhooks(user_id)
        response_dict = MessageToDict(response, preserving_proto_field_name=True)
        
        end_time = time.time()
        response_time = end_time - start_time
        log_response_info(request_id, 'merchant-integration-service', 200, response_time)
        
        return jsonify(response_dict), 200
    except Exception as e:
        logger.error(f"Request: {request_id} | Error in get_webhooks: {str(e)}")
        return jsonify({'error': 'Internal Server Error'}), 500

        return jsonify(response_dict), 200

@webhook_bp.route('/api/merchant-integration-service/webhooks', methods=['POST'])
def create_webhook():
    request_id = str(uuid.uuid4())
    start_time = time.time()
    log_request_info(request_id, 'merchant-integration-service', 'create_webhook')
    
    try:
        data = request.json
        user_id = data.get('user_id')
        url = data.get('url')
        
        if not user_id or not url:
            return jsonify({'error': 'user_id and url are required'}), 400
        
        response = webhook_client.create_webhook(user_id, url)
        response_dict = MessageToDict(response, preserving_proto_field_name=True)
        
        end_time = time.time()
        response_time = end_time - start_time
        log_response_info(request_id, 'merchant-integration-service', 201, response_time)
        
        return jsonify(response_dict), 201
    except Exception as e:
        logger.error(f"Request: {request_id} | Error in create_webhook: {str(e)}")
        return jsonify({'error': 'Internal Server Error'}), 500

@webhook_bp.route('/api/merchant-integration-service/webhooks/<int:webhook_id>', methods=['DELETE'])
def disable_webhook(webhook_id):
    request_id = str(uuid.uuid4())
    start_time = time.time()
    log_request_info(request_id, 'merchant-integration-service', f'disable_webhook/{webhook_id}')
    
    try:
        response = webhook_client.disable_webhook(webhook_id)
        response_dict = MessageToDict(response, preserving_proto_field_name=True)
        
        end_time = time.time()
        response_time = end_time - start_time
        log_response_info(request_id, 'merchant-integration-service', 200, response_time)
        
        return jsonify(response_dict), 200
    except Exception as e:
        logger.error(f"Request: {request_id} | Error in disable_webhook: {str(e)}")
        return jsonify({'error': 'Internal Server Error'}), 500