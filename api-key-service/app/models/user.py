from app.extensions import db
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID
import uuid

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email
        }