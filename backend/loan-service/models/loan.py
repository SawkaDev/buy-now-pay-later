import enum
from sqlalchemy import Column, Integer, Float, DateTime, Enum, String, Index
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy.orm import validates
import re

Base = declarative_base()

class LoanStatus(enum.Enum):
    PENDING = "pending"
    UNDER_REVIEW = "under_review"
    APPROVED = "approved"
    REJECTED = "rejected"
    DISBURSED = "disbursed"
    IN_REPAYMENT = "in_repayment"
    PAID_OFF = "paid_off"
    DEFAULTED = "defaulted"

class Loan(Base):
    __tablename__ = 'loans'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False, index=True)
    loan_amount = Column(Float, nullable=False)
    loan_term_months = Column(Integer, nullable=False)
    interest_rate = Column(Float)
    purpose = Column(String(255), nullable=False)
    status = Column(Enum(LoanStatus), default=LoanStatus.PENDING, index=True)
    merchant_id = Column(Integer, nullable=True)

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    __table_args__ = (
        Index('idx_user_id_status', 'user_id', 'status'),
    )

    @validates('loan_amount', 'loan_term_months', 'interest_rate', 'purpose', 'idempotency_key')
    def validate_fields(self, key, value):
        if key == 'loan_amount' and value <= 0:
            raise ValueError("Loan amount must be positive")
        elif key == 'loan_term_months' and value <= 0:
            raise ValueError("Loan term must be positive")
        elif key == 'interest_rate' and value < 0:
            raise ValueError("Interest rate cannot be negative")
        elif key == 'purpose' and not value.strip():
            raise ValueError("Purpose cannot be empty")
        return value
