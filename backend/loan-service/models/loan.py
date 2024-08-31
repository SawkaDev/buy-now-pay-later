import enum
import uuid
from datetime import datetime, timedelta
from sqlalchemy import Column, Integer, BigInteger, DateTime, Enum, String, Index, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from sqlalchemy.orm import validates, relationship
from core.base import Base

class CheckoutStatus(enum.Enum):
    NOT_STARTED = "not_started"
    INITIATED = "initiated"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

class CheckoutSession(Base):
    __tablename__ = 'checkout_sessions'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    loan_id = Column(UUID(as_uuid=True), unique=True)
    order_id = Column(String(255), nullable=False, unique=True)
    success_redirect_url = Column(String(512), nullable=False)
    cancel_redirect_url = Column(String(512), nullable=False)
    checkout_url = Column(String(512), nullable=False)
    status = Column(Enum(CheckoutStatus), default=CheckoutStatus.INITIATED)
    expires_at = Column(DateTime, nullable=False, index=True)

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())


    def complete(self):
        if self.status != CheckoutStatus.INITIATED:
            raise ValueError("Checkout must be initiated before it can be completed")
        self.status = CheckoutStatus.COMPLETED
        self.loan.update_status(LoanStatus.APPROVED)  # Or whatever status is appropriate

    def cancel(self):
        self.status = CheckoutStatus.CANCELLED

    @property
    def is_expired(self):
        return datetime.utcnow() > self.expires_atW