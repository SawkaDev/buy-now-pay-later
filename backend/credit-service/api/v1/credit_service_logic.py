# credit_service.py

from sqlalchemy.exc import SQLAlchemyError
from models.credit import CreditProfile, LoanStatus, Loan
from sqlalchemy.orm import joinedload
from uuid import uuid4
from typing import List
import random
import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

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

    def get_loan_options(self, user_id: str, session_id: str) -> list:
        loan_options = []

        loan = self.db.query(Loan).filter(Loan.checkout_session_id == session_id).first()

        if not loan:
            return []

        loan_amount = loan.loan_amount_cents

        loan_terms = [6, 12, 18, 24]
        interest_rates = [5, 7, 9, 11]

        for i, (term, rate) in enumerate(zip(loan_terms, interest_rates), 1):
            interest = (loan_amount / 100) * (rate / 100) * (term / 12)
            total_payment = (loan_amount / 100) + interest
            monthly_payment = total_payment / term

            loan_option = {
                "id": f"Loan-Ref-{i}",
                "loan_amount_cents": loan_amount,
                "loan_term_months": term,
                "interest_rate": rate,
                "monthly_payment_cents": round(monthly_payment * 100),
                "total_payment_amount_cents": round(total_payment * 100)
            }
            loan_options.append(loan_option)
        return loan_options

    def select_loan(self, user_id: str, checkout_session_id: str, loan_term_months: int, 
                    interest_rate: float, monthly_payment_cents: int, 
                    total_payment_amount_cents: int) -> bool:
        try:
            loan = self.db.query(Loan).filter(Loan.checkout_session_id == checkout_session_id).first()

            if not loan:
                raise ValueError(f"Loan with checkout_session_id {checkout_session_id} not found")

            loan.user_id = user_id
            loan.loan_term_months = loan_term_months
            loan.interest_rate = interest_rate
            loan.monthly_payment_cents = monthly_payment_cents
            loan.total_payment_amount_cents = total_payment_amount_cents
            loan.status = LoanStatus.APPROVED

            self.db.commit()
            return True
        except SQLAlchemyError as e:
            self.db.rollback()
            raise RuntimeError(f"Database error occurred: {str(e)}")
        except ValueError as e:
            raise e

    def update_checkout_session_for_loan(self, loan_id: str, checkout_session_id: str) -> bool:
        try:
            loan = self.db.query(Loan).filter(Loan.id == loan_id).first()
            if not loan:
                raise ValueError(f"Loan with id {loan_id} not found")
            
            loan.checkout_session_id = checkout_session_id
            self.db.commit()
            return True
        except SQLAlchemyError as e:
            self.db.rollback()
            raise RuntimeError(f"Database error occurred: {str(e)}")
        except ValueError as e:
            raise e

    def get_loan_for_checkout_session(self, checkout_session_id: str, user_id: str) -> str:
 
        try:
            loan = self.db.query(Loan).filter(Loan.checkout_session_id == checkout_session_id).first()
            logger.info(f"Loan found: {loan.user_id}")
            if not loan:
                raise ValueError(f"Loan not found for checkout session {checkout_session_id}")

            if loan.user_id is None:
                return ""
            else:
                if str(loan.user_id) != str(user_id):
                    return "Unauthorized"
                else:
                    return loan.status.value
        except SQLAlchemyError as e:
            raise RuntimeError(f"Database error occurred: {str(e)}")
        except ValueError as e:
            raise e