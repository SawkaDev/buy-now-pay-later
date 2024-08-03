from flask import Flask
from flask_cors import CORS
from .utils.rate_limiting import limiter
from .routes.routes import api_bp

def create_app():
    app = Flask(__name__)
    CORS(app)
    limiter.init_app(app)
    app.register_blueprint(api_bp)
    setup_logging(app)
    return app

def setup_logging(app):
    import logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    logger = logging.getLogger(__name__)
    app.logger = logger
