from app.extensions import db
from datetime import datetime

class APIKey(db.Model):
    __tablename__ = 'api_keys'
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(64), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    expires_at = db.Column(db.DateTime, nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    user = db.relationship('User', back_populates='api_keys')

    @property
    def is_expired(self):
        return datetime.utcnow() > self.expires_at

    def check_expiration(self):
        if self.is_expired and self.is_active:
            self.is_active = False
            try:
                db.session.commit()
            except Exception as e:
                db.session.rollback()   
                         
    def json(self):
        self.check_expiration()  # Ensure status is up-to-date
        return {
            'id': self.id,
            'key': self.key,
            'created_at': self.created_at.isoformat(),
            'expires_at': self.expires_at.isoformat(),
            'is_active': self.is_active,
            'is_expired': self.is_expired
        }

