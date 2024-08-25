from sqlalchemy import Column, Integer, String, Boolean, DateTime
from core.db import Base
from sqlalchemy.sql import func

class Webhook(Base):
    __tablename__ = 'webhooks'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    url = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    def json(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'url': self.url,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            'is_active': self.is_active
        }