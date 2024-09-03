import sys
import os

# Add the site-packages directory to the Python path
site_packages_path = '/usr/local/lib/python3.10/site-packages'
sys.path.insert(0, site_packages_path)

from datetime import datetime, timedelta
from sqlalchemy.exc import SQLAlchemyError
from models.loan import CheckoutSession
from sqlalchemy.orm import joinedload
import random
import uuid

from client.v1.credit import CreditClientV1

class LoanService:
    def __init__(self, db_session):
        self.db = db_session
        self.credit_client = CreditClientV1(host='credit-service', port=50053)

    def generate_checkout_session(self, loan_amount_cents: int, 
                                  merchant_id: int, order_id: str, 
                                  success_redirect_url: str, cancel_redirect_url: str) -> str:
        try:
            # Perform credit check
            # credit_check_result = self.credit_client.check_credit(merchant_id)  # Assuming merchant_id is used for credit check
            # if not credit_check_result.approved:
            #     raise PermissionError("Credit check failed")

            # Create a new checkout session
            checkout_session = CheckoutSession(
                loan_id=uuid.uuid4(),
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

