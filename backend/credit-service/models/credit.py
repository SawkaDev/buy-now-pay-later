import uuid
from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, Index
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import validates
from core.base import Base

class CreditProfile(Base):
    __tablename__ = 'credit_profiles'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), nullable=False, unique=True, default=uuid.uuid4)
    name = Column(String(100), nullable=False)
    credit_score = Column(Integer, nullable=False)
    number_of_accounts = Column(Integer, nullable=False)
    credit_utilization_ratio = Column(Float, nullable=False)
    recent_soft_inquiries = Column(Integer, nullable=False)
    bankruptcies = Column(Integer, nullable=False)
    tax_liens = Column(Integer, nullable=False)
    judgments = Column(Integer, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    __table_args__ = (
        Index('idx_credit_profile_user_id', 'user_id'),
    )

    @validates('credit_score', 'number_of_accounts', 'recent_soft_inquiries', 'bankruptcies', 'tax_liens', 'judgments')
    def validate_non_negative(self, key, value):
        if value < 0:
            raise ValueError(f"{key} must be non-negative")
        return value

    @validates('credit_utilization_ratio')
    def validate_ratio(self, key, value):
        if not 0 <= value <= 1:
            raise ValueError("Credit utilization ratio must be between 0 and 1")
        return value

    def __repr__(self):
        return f"<CreditProfile(id='{self.id}', user_id='{self.user_id}', credit_score={self.credit_score})>"