import os
from flask import Flask
from flask_cors import CORS
from config import config
from app.models import User, APIKey
from app.routes import blueprints
from app.extensions import db, migrate

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app)

    for blueprint in blueprints:
        app.register_blueprint(blueprint, url_prefix='/api/flask')
        
    return app
