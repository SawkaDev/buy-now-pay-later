import uuid
import enum
from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, Index, Enum, ForeignKey, BigInteger
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import validates, relationship
from sqlalchemy.sql import func
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

class LoanStatus(enum.Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"
    ACTIVE = "active"
    PAID = "paid"
    DEFAULTED = "defaulted"

class Loan(Base):
    __tablename__ = 'loans'

    id = Column(Integer, primary_key=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey('credit_profiles.user_id'), nullable=False)
    merchant_id = Column(Integer, nullable=False)
    checkout_session_id = Column(UUID(as_uuid=True), nullable=False)
    loan_amount_cents = Column(BigInteger, nullable=False)
    loan_term_months = Column(Integer, nullable=True)
    interest_rate = Column(Integer, nullable=True)  # Stored as basis points (e.g., 500 for 5.00%)
    status = Column(Enum(LoanStatus), default=LoanStatus.PENDING, index=True)
    monthly_payment_cents = Column(BigInteger, nullable=True)
    total_payment_amount_cents = Column(BigInteger, nullable=True)
    approval_date = Column(DateTime, nullable=True)
    rejection_reason = Column(String(255), nullable=True)

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    credit_profile = relationship("CreditProfile", back_populates="loans")

    __table_args__ = (
        Index('idx_user_id_status', 'user_id', 'status'),
    )

    @validates('loan_amount_cents', 'loan_term_months', 'interest_rate', 'monthly_payment_cents', 'total_payment_amount_cents')
    def validate_fields(self, key, value):
        if key in ['loan_amount_cents', 'monthly_payment_cents', 'total_payment_amount_cents'] and value <= 0:
            raise ValueError(f"{key} must be positive")
        if key == 'loan_term_months' and value <= 0:
            raise ValueError("Loan term must be positive")
        if key == 'interest_rate' and value < 0:
            raise ValueError("Interest rate cannot be negative")
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

    def approve_loan(self, approval_date: datetime):
        self.status = LoanStatus.APPROVED
        self.approval_date = approval_date

    def reject_loan(self, reason: str):
        self.status = LoanStatus.REJECTED
        self.rejection_reason = reason

    def __repr__(self):
        return f"<Loan(id={self.id}, user_id='{self.user_id}', amount=${self.loan_amount_dollars:.2f}, status={self.status.value})>"

CreditProfile.loans = relationship("Loan", back_populates="credit_profile")
