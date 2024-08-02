from functools import wraps
from flask import request, jsonify
import jwt
from ..config import Config

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        try:
            jwt.decode(token, Config.JWT_SECRET, algorithms=["HS256"])
        except:
            return jsonify({'message': 'Token is invalid!'}), 401
        return f(*args, **kwargs)
    return decorated

# TODO: Implement get_user_identity function here
