import enum
import uuid
from datetime import datetime, timedelta
from sqlalchemy import Column, Integer, BigInteger, DateTime, Enum, String, Index, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from sqlalchemy.orm import validates, relationship
from core.base import Base

class LoanStatus(enum.Enum):
    PENDING = "pending"
    UNDER_REVIEW = "under_review"
    APPROVED = "approved"
    REJECTED = "rejected"
    DISBURSED = "disbursed"
    IN_REPAYMENT = "in_repayment"
    PAID_OFF = "paid_off"
    DEFAULTED = "defaulted"

class CheckoutStatus(enum.Enum):
    NOT_STARTED = "not_started"
    INITIATED = "initiated"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

class Loan(Base):
    __tablename__ = 'loans'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=True, index=True)
    merchant_id = Column(Integer, nullable=False)
    loan_amount_cents = Column(BigInteger, nullable=False)
    loan_term_months = Column(Integer, nullable=True)
    interest_rate = Column(Integer, nullable=True)  # Stored as basis points (e.g., 500 for 5.00%)
    status = Column(Enum(LoanStatus), default=LoanStatus.PENDING, index=True)

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    # One-to-one relationship with CheckoutSession
    checkout_session = relationship("CheckoutSession", back_populates="loan", uselist=False)

    __table_args__ = (
        Index('idx_user_id_status', 'user_id', 'status'),
    )

    @validates('loan_amount_cents', 'loan_term_months', 'interest_rate')
    def validate_fields(self, key, value):
        if key == 'loan_amount_cents' and value <= 0:
            raise ValueError("Loan amount must be positive")
        return value

    @property
    def loan_amount_dollars(self):
        return self.loan_amount_cents / 100

    @loan_amount_dollars.setter
    def loan_amount_dollars(self, value):
        self.loan_amount_cents = int(value * 100)

    @property
    def interest_rate_percentage(self):
        return self.interest_rate / 100

    @interest_rate_percentage.setter
    def interest_rate_percentage(self, value):
        self.interest_rate = int(value * 100)

    def update_status(self, new_status: LoanStatus):
        if not isinstance(new_status, LoanStatus):
            raise ValueError("Invalid loan status")
        self.status = new_status

class CheckoutSession(Base):
    __tablename__ = 'checkout_sessions'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    loan_id = Column(Integer, ForeignKey('loans.id'), nullable=False, unique=True)
    order_id = Column(String(255), nullable=False, unique=True)
    success_redirect_url = Column(String(512), nullable=False)
    cancel_redirect_url = Column(String(512), nullable=False)
    checkout_url = Column(String(512), nullable=False)
    status = Column(Enum(CheckoutStatus), default=CheckoutStatus.INITIATED)
    expires_at = Column(DateTime, nullable=False, index=True)

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    # One-to-one relationship with Loan
    loan = relationship("Loan", back_populates="checkout_session", uselist=False)

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