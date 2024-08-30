# loan_service.py

from datetime import datetime, timedelta
from sqlalchemy.exc import SQLAlchemyError
from models.loan import Loan, LoanStatus, CheckoutSession
from sqlalchemy.orm import joinedload
import random

class LoanService:
    def __init__(self, db_session):
        self.db = db_session

    def get_loan(self, loan_id: int) -> Loan:
        loan = self.db.query(Loan).options(joinedload(Loan.checkout_session)).filter(Loan.id == loan_id).first()
        if not loan:
            raise LookupError(f"Loan with id {loan_id} not found")
        return loan

    def update_loan_status(self, loan_id: int, new_status: str) -> Loan:
        loan = self.get_loan(loan_id)
        try:
            loan.status = LoanStatus(new_status)
        except ValueError:
            raise ValueError(f"Invalid loan status: {new_status}")
        
        self.db.commit()
        return loan

    def update_payment(self, loan_id: int, payment_status: str) -> bool:
        loan = self.get_loan(loan_id)
        
        if payment_status == 'PAID_OFF':
            loan.status = LoanStatus.PAID_OFF
        elif loan.status == LoanStatus.APPROVED and payment_status == 'PAYMENT_RECEIVED':
            loan.status = LoanStatus.IN_REPAYMENT
        elif payment_status == 'DEFAULTED':
            loan.status = LoanStatus.DEFAULTED
        else:
            raise ValueError(f"Invalid payment status: {payment_status}")
        
        self.db.commit()
        return True

    def generate_checkout_session(self,loan_amount_cents: int, 
                                  merchant_id: int, order_id: str, 
                                  success_redirect_url: str, cancel_redirect_url: str) -> str:
        try:
            # Create a new loan
            new_loan = Loan(
                loan_amount_cents=loan_amount_cents,
                merchant_id=merchant_id,
                status=LoanStatus.PENDING
            )
            self.db.add(new_loan)
            self.db.flush()  # This assigns an id to the new loan without committing the transaction

            # Create a new checkout session
            checkout_session = CheckoutSession(
                loan_id=new_loan.id,
                order_id=order_id,
                success_redirect_url=success_redirect_url,
                cancel_redirect_url=cancel_redirect_url,
                expires_at=datetime.utcnow() + timedelta(minutes=30),
                checkout_url=""
            )

            self.db.add(checkout_session)
            self.db.flush()  # This assigns an id to the checkout session

            # Generate the checkout URL
            base_url = "http://localhost:8081/checkout/"
            checkout_url = f"{base_url}{checkout_session.id}"
            checkout_session.checkout_url = checkout_url

            self.db.commit()
            return checkout_url

        except SQLAlchemyError as e:
            self.db.rollback()
            raise RuntimeError(f"Database error occurred: {str(e)}")

    def get_loan_options(self, user_id: int, session_id: str) -> list:
        # Mock loan options
        loan_options = []
        for i in range(4):  # Generate 3 mock loan options
            loan_option = {
                "id": f"loan-option-{i+1}",
                "loan_amount_cents": random.randint(50000, 500000),  # 500 to 5000 dollars
                "loan_term_months": random.choice([6, 12, 24]),
                "interest_rate": round(random.uniform(5, 20), 2),
                "monthly_payment": round(random.uniform(50, 500), 2),
                "total_payment_amount": round(random.uniform(600, 6000), 2)
            }
            loan_options.append(loan_option)
        
        return loan_options