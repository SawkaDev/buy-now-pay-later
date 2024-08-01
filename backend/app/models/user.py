from app.extensions import db
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID
import uuid

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    api_keys = db.relationship('APIKey', back_populates='user')

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'api_keys': [key.json() for key in self.api_keys]
        }