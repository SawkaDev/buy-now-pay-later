import os
from flask import Flask
from flask_cors import CORS
from config import config
from app.routes import blueprints
from app.extensions import db, migrate

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    db.init_app(app)

    with app.app_context():
        db.create_all()  # This creates the tables
        
    migrate.init_app(app, db)
    CORS(app)

    for blueprint in blueprints:
        app.register_blueprint(blueprint, url_prefix='/api-key-service')
        
    return app
