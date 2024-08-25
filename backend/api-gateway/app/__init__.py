from flask import Flask
from flask_cors import CORS
from .utils.rate_limiting import limiter
from .routes.routes import api_bp
from .routes.auth import auth_bp
from flask_session import Session
from config import config
import redis
import os
from .routes import blueprints

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    CORS(app, supports_credentials=True)
    Session(app)

    limiter.init_app(app)

    for blueprint in blueprints:
        app.register_blueprint(blueprint, url_prefix='')

    setup_logging(app)
    return app

def setup_logging(app):
    import logging
    logging.basicConfig(
        level=app.config['LOGGING_LEVEL'],
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    logger = logging.getLogger(__name__)
    app.logger = logger
