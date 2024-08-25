from sqlalchemy import Column, Integer, String, Boolean, DateTime
from webhook_service.core.db import Base
from sqlalchemy.sql import func

class Webhook(Base):
    __tablename__ = 'webhooks'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    url = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
