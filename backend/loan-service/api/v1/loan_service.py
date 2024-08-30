# loan_service_v1.py

import logging
import grpc
from generated.v1 import loan_service_pb2, loan_service_pb2_grpc
from models.loan import LoanStatus
from core.db import SessionLocal
from .loan_service_logic import LoanService

logger = logging.getLogger(__name__)

class LoanServiceV1(loan_service_pb2_grpc.LoanServiceServicer):
    def GetLoan(self, request, context):
        logger.info(f"Received get loan request for loan ID {request.loan_id}")
        
        db = SessionLocal()
        try:
            loan_service = LoanService(db)
            loan = loan_service.get_loan(request.loan_id)
            loan_proto = self._loan_to_proto(loan)
            checkout_session_proto = self._checkout_session_to_proto(loan.checkout_session) if loan.checkout_session else None
            return loan_service_pb2.LoanResponse(loan=loan_proto, checkout_session=checkout_session_proto)
        except LookupError:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('Loan not found')
        except Exception as e:
            logger.error(f"Error retrieving loan: {str(e)}", exc_info=True)
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details('An internal error occurred')
        finally:
            db.close()
        
        return loan_service_pb2.LoanResponse()

    def UpdateLoanStatus(self, request, context):
        logger.info(f"Received update loan status request for loan ID {request.loan_id}")
        
        db = SessionLocal()
        try:
            loan_service = LoanService(db)
            loan = loan_service.update_loan_status(request.loan_id, request.new_status)
            return loan_service_pb2.LoanResponse(loan=self._loan_to_proto(loan))
        
        except ValueError as e:
            logger.warning(f"Invalid loan status: {str(e)}")
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details('Invalid loan status')
        except LookupError:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('Loan not found')
        except Exception as e:
            logger.error(f"Error updating loan status: {str(e)}", exc_info=True)
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details('An internal error occurred')
        finally:
            db.close()
        
        return loan_service_pb2.LoanResponse()

    def UpdatePayment(self, request, context):
        logger.info(f"Received update payment request for loan ID {request.loan_id}")
        
        db = SessionLocal()
        try:
            loan_service = LoanService(db)
            success = loan_service.update_payment(request.loan_id, request.payment_status)
            return loan_service_pb2.PaymentUpdateResponse(success=success)
        
        except ValueError as e:
            logger.warning(f"Invalid payment status: {str(e)}")
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details('Invalid payment status')
        except LookupError:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('Loan not found')
        except Exception as e:
            logger.error(f"Error updating payment: {str(e)}", exc_info=True)
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details('An internal error occurred')
        finally:
            db.close()
        
        return loan_service_pb2.PaymentUpdateResponse(success=False)

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

    def GetLoanOptions(self, request, context):
        logger.info(f"Received get loan options request for user ID {request.user_id} / session {request.session_id}")
        
        db = SessionLocal()
        try:
            loan_service = LoanService(db)
            loan_options = loan_service.get_loan_options(request.user_id, request.session_id)
            
            response = loan_service_pb2.GetLoanOptionsResponse()
            for option in loan_options:
                loan_option = response.loan_options.add()
                loan_option.id = option['id']
                loan_option.loan_amount_cents = option['loan_amount_cents']
                loan_option.loan_term_months = option['loan_term_months']
                loan_option.interest_rate = option['interest_rate']
                loan_option.monthly_payment = option['monthly_payment']
                loan_option.total_payment_amount = option['total_payment_amount']
            
            return response
        
        except Exception as e:
            logger.error(f"Error retrieving loan options: {str(e)}", exc_info=True)
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details('An internal error occurred')
        finally:
            db.close()
        
        return loan_service_pb2.GetLoanOptionsResponse()

    def _loan_to_proto(self, loan):
        return loan_service_pb2.Loan(
            id=loan.id,
            user_id=loan.user_id,
            loan_amount_cents=loan.loan_amount_cents,
            loan_term_months=loan.loan_term_months,
            interest_rate=loan.interest_rate,
            status=loan.status.value,
            merchant_id=loan.merchant_id,
            created_at=loan.created_at.isoformat() if loan.created_at else None,
            updated_at=loan.updated_at.isoformat() if loan.updated_at else None
        )

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
