import logging
from flask import request

logger = logging.getLogger(__name__)

def log_request_info(request_id, service, path):
    logger.info(
        f"Request: {request_id} | "
        f"Method: {request.method} | "
        f"Service: {service} | "
        f"Path: {path} | "
        f"IP: {request.remote_addr} | "
        f"User-Agent: {request.headers.get('User-Agent')} | "
        f"Payload: {request.get_data(as_text=True)}"
    )

def log_response_info(request_id, service, status_code, response_time):
    logger.info(
        f"Response: {request_id} | "
        f"Service: {service} | "
        f"Status: {status_code} | "
        f"Time: {response_time:.2f}s"
    )
