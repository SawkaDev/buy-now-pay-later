# credit_service.py

from sqlalchemy.exc import SQLAlchemyError
from models.credit import CreditProfile, LoanStatus, Loan
from sqlalchemy.orm import joinedload
from uuid import uuid4
from typing import List

class CreditService:
    def __init__(self, db_session):
        self.db = db_session

    def create_credit_profile(self, name: str, credit_score: int, 
                              number_of_accounts: int, credit_utilization_ratio: float, 
                              recent_soft_inquiries: int, bankruptcies: int, 
                              tax_liens: int, judgments: int) -> CreditProfile:
        try:
            new_profile = CreditProfile(
                id=str(uuid4()),
                user_id=str(uuid4()),
                name=name,
                credit_score=credit_score,
                number_of_accounts=number_of_accounts,
                credit_utilization_ratio=credit_utilization_ratio,
                recent_soft_inquiries=recent_soft_inquiries,
                bankruptcies=bankruptcies,
                tax_liens=tax_liens,
                judgments=judgments
            )
            self.db.add(new_profile)
            self.db.commit()
            return new_profile
        except SQLAlchemyError as e:
            self.db.rollback()
            raise RuntimeError(f"Database error occurred: {str(e)}")

    def get_all_credit_profiles(self) -> List[CreditProfile]:
        try:
            return self.db.query(CreditProfile).all()
        except SQLAlchemyError as e:
            raise RuntimeError(f"Database error occurred: {str(e)}")

    def create_default_loan_application(self, loan_amount_cents: int,  merchant_id: int) -> bool:
        try:
            new_loan = Loan(
                loan_amount_cents=loan_amount_cents,
                merchant_id=merchant_id,
            )
            self.db.add(new_loan)
            self.db.commit()
            return True, str(new_loan.id)  # Return a tuple with True and the new loan ID
        except SQLAlchemyError as e:
            self.db.rollback()
            raise RuntimeError(f"Database error occurred: {str(e)}")
