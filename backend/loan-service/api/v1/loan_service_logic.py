from datetime import datetime, timedelta
from sqlalchemy.exc import SQLAlchemyError
from models.loan import CheckoutSession
from sqlalchemy.orm import joinedload
import random
import uuid
import logging

logger = logging.getLogger(__name__)

from credit_client.v1.credit import CreditClientV1

class LoanService:
    def __init__(self, db_session):
        self.db = db_session
        self.credit_client = CreditClientV1(host='credit-service', port=50053)

    def generate_checkout_session(self, loan_amount_cents: int, 
                                  merchant_id: int, order_id: str, 
                                  success_redirect_url: str, cancel_redirect_url: str) -> str:
        try:
            # Create default loan application
            response = self.credit_client.create_default_loan_application(loan_amount_cents=loan_amount_cents, merchant_id=merchant_id)
            checkout_session = CheckoutSession(
                loan_id=uuid.UUID(response.loan_id),
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
