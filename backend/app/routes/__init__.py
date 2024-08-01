from .user_routes import user_bp
from .api_key_routes import api_key_bp

# List of blueprints to be registered
blueprints = [user_bp, api_key_bp]
