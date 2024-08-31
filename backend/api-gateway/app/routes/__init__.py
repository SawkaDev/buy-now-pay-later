from .auth import auth_bp
from .routes import api_bp
from .webhook_service import webhook_bp
from .api_key_service import api_key_bp
from .loan_service import loan_bp
from .credit_service import credit_bp

# List of blueprints to be registered
blueprints = [auth_bp, api_bp, webhook_bp, api_key_bp, loan_bp, credit_bp]
