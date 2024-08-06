from .auth import auth_bp
from .routes import api_bp

# List of blueprints to be registered
blueprints = [auth_bp, api_bp]
