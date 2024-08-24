from .api_key_routes import api_key_bp
from .webhook_routes import webhook_bp
# List of blueprints to be registered
blueprints = [api_key_bp, webhook_bp]
