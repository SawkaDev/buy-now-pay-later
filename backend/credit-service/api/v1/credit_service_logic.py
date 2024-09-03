# credit_service.py

from sqlalchemy.exc import SQLAlchemyError
from models.credit import CreditProfile, LoanStatus, Loan
from sqlalchemy.orm import joinedload
from uuid import uuid4
from typing import List
import random

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

        loan_amount = random.randint(2, 20) * 5000

        loan_terms = [6, 12, 18, 24]
        interest_rates = [5, 7, 9, 11]

        for i in range(4):
            term = random.choice(loan_terms)
            rate = random.choice(interest_rates)

            interest = (loan_amount / 100) * (rate / 100) * (term / 12)
            total_payment = loan_amount / 100 + interest
            monthly_payment = total_payment / term

            loan_option = {
                "id": f"Loan-Ref-{i+1}",
                "loan_amount_cents": loan_amount,
                "loan_term_months": term,
                "interest_rate": rate,
                "monthly_payment": round(monthly_payment * 100),
                "total_payment_amount": round(total_payment * 100)
            }
            loan_options.append(loan_option)

        loan_options.sort(key=lambda x: x['loan_term_months'])

        return loan_options
