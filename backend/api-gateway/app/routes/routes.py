from flask import Blueprint, request, jsonify
import requests
import time
import uuid
import logging
from app.utils.logging_utils import log_request_info, log_response_info
from app.services.service_registry import services
from app.utils.rate_limiting import limiter

logger = logging.getLogger(__name__)

api_bp = Blueprint('api', __name__)

@api_bp.route('/api/<service>/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def gateway(service, path):
    request_id = str(uuid.uuid4())
    start_time = time.time()
    log_request_info(request_id, service, path)
    
    if service not in services:
        logger.warning(f"Request: {request_id} | Service not found: {service}")
        return jsonify({'error': 'Service not found'}), 404

    url = f"{services[service]['url']}/{service}/{path}"
    
    try:
        response = requests.request(
            method=request.method,
            url=url,
            headers={key: value for (key, value) in request.headers if key != 'Host'},
            data=request.get_data(),
            cookies=request.cookies,
            allow_redirects=False
        )
        
        end_time = time.time()
        response_time = end_time - start_time
        
        log_response_info(request_id, service, response.status_code, response_time)
        
        return (response.content, response.status_code, response.headers.items())
    except requests.RequestException as e:
        logger.error(f"Request: {request_id} | Service unavailable: {service}. Error: {str(e)}")
        return jsonify({'error': 'Service unavailable'}), 503

@api_bp.errorhandler(429)
def ratelimit_handler(e):
    return jsonify({'error': 'Rate limit Exceeded'}), 429
    # return jsonify(error="Rate limit exceeded", description=str(e.description)), 429
