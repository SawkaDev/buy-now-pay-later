from .user_routes import user_bp
from .auth_routes import auth_bp

# List of blueprints to be registered
blueprints = [auth_bp, user_bp]
