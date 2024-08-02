import os
import logging
from functools import wraps
from flask import Flask, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_cors import CORS
import jwt
import requests

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configuration
JWT_SECRET = os.environ.get('JWT_SECRET', 'your-secret-key')

# Service registry with rate limits
services = {
    "api-service": {
        "url": "http://flaskapp:4000",
        "limits": ["100 per minute", "20 per second"]
    },
    # Add more services here with their specific limits
}

# Rate limiting setup
limiter = Limiter(
    key_func=get_remote_address,
    default_limits=["100 per minute", "20 per second"],
    storage_uri="memory://"
)
limiter.init_app(app)

# Helper functions
def get_service_limits():
    service = request.view_args.get('service')
    return services.get(service, {}).get("limits", ["10 per minute"])

# Decorators
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        try:
            jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
        except:
            return jsonify({'message': 'Token is invalid!'}), 401
        return f(*args, **kwargs)
    return decorated

def apply_rate_limits(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        limits = get_service_limits()
        for limit in limits:
            limiter.limit(limit)(func)(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper

# Error handlers
@app.errorhandler(429)
def ratelimit_handler(e):
    return jsonify(error="Rate limit exceeded", description=str(e.description)), 429

# Routes
@app.route('/api/<service>/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
# @token_required  # Uncomment this if you want to require authentication for all API calls
@apply_rate_limits
def gateway(service, path):
    logger.info(f"Accessing service: {service}, path: {path}")
    if service not in services:
        return jsonify({'error': 'Service not found'}), 404

    url = f"{services[service]['url']}/{path}"
    
    try:
        response = requests.request(
            method=request.method,
            url=url,
            headers={key: value for (key, value) in request.headers if key != 'Host'},
            data=request.get_data(),
            cookies=request.cookies,
            allow_redirects=False
        )
        
        logger.info(f"Response from {service}: Status {response.status_code}")
        return (response.content, response.status_code, response.headers.items())
    except requests.RequestException as e:
        logger.error(f"Service unavailable: {service}. Error: {str(e)}")
        return jsonify({'error': 'Service unavailable'}), 503

# Main execution
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)


# TODO: Rate limit based on user
# # Function to get the current user's identity or IP
# def get_user_identity():
#     token = request.headers.get('Authorization')
#     if not token:
#         return get_remote_address()  # Fall back to IP if no token
#     try:
#         payload = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
#         return payload.get('sub', get_remote_address())  # Use 'sub' claim or fall back to IP
#     except:
#         return get_remote_address()  # Fall back to IP if token is invalid
