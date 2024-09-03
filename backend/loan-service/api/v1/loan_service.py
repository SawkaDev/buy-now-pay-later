# loan_service_v1.py

import logging
import grpc
from loan_client.v1 import loan_service_pb2, loan_service_pb2_grpc
from core.db import SessionLocal
from .loan_service_logic import LoanService

logger = logging.getLogger(__name__)

class LoanServiceV1(loan_service_pb2_grpc.LoanServiceServicer):
    def GenerateCheckoutSession(self, request, context):
        logger.info(f"Received checkout session request for order {request.order_id}")
        
        if not self._validate_checkout_request(request):
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details('Invalid request parameters')
            return loan_service_pb2.CheckoutSessionResponse()

        db = SessionLocal()
        try:
            loan_service = LoanService(db)
            checkout_url = loan_service.generate_checkout_session(
                loan_amount_cents=request.loan_amount_cents,
                merchant_id=request.merchant_id,
                order_id=request.order_id,
                success_redirect_url=request.success_redirect_url,
                cancel_redirect_url=request.cancel_redirect_url
            )
            
            return loan_service_pb2.CheckoutSessionResponse(checkout_url=checkout_url)
        
        except ValueError as e:
            logger.warning(f"Invalid input: {str(e)}")
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details(str(e))
        except PermissionError:
            logger.warning(f"Unauthorized merchant {request.merchant_id} for order {request.order_id}")
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details('Merchant not authorized for this user')
        except Exception as e:
            logger.error(f"Error generating checkout session: {str(e)}", exc_info=True)
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details('An internal error occurred')
        finally:
            db.close()
        
        return loan_service_pb2.CheckoutSessionResponse()

    def _validate_checkout_request(self, request):
        # Implement validation logic here
        return True  # Placeholder

    def _checkout_session_to_proto(self, checkout_session):
        if not checkout_session:
            return None

        return loan_service_pb2.CheckoutSession(
            id=str(checkout_session.id),
            loan_id=checkout_session.loan_id,
            order_id=checkout_session.order_id,
            success_redirect_url=checkout_session.success_redirect_url,
            cancel_redirect_url=checkout_session.cancel_redirect_url,
            checkout_url=checkout_session.checkout_url,
            status=checkout_session.status.value,
            expires_at=checkout_session.expires_at.isoformat() if checkout_session.expires_at else None,
            created_at=checkout_session.created_at.isoformat() if checkout_session.created_at else None,
            updated_at=checkout_session.updated_at.isoformat() if checkout_session.updated_at else None
        )

def add_to_server(server):
    loan_service_pb2_grpc.add_LoanServiceServicer_to_server(LoanServiceV1(), server)
