from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from core.db import Base, SessionLocal

class APIKey(Base):
    __tablename__ = 'api_keys'
    id = Column(Integer, primary_key=True)
    key = Column(String(64), unique=True, nullable=False)
    user_id = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    expires_at = Column(DateTime, nullable=False)
    is_active = Column(Boolean, default=True)

    @property
    def is_expired(self):
        return datetime.utcnow() > self.expires_at

    def check_expiration(self):
        if self.is_expired and self.is_active:
            self.is_active = False
            session = SessionLocal()
            try:
                session.add(self)
                session.commit()
            except Exception as e:
                session.rollback()
                raise e
            finally:
                session.close()

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
