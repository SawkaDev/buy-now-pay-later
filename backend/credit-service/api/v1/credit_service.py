# credit_service_v1.py

import logging
import grpc
from google.protobuf import empty_pb2
from credit_client.v1 import credit_service_pb2, credit_service_pb2_grpc
from core.db import SessionLocal
from .credit_service_logic import CreditService

logger = logging.getLogger(__name__)

class CreditServiceV1(credit_service_pb2_grpc.CreditServiceServicer):

    def CreateCreditProfile(self, request, context):
        logger.info(f"Received create credit profile request for user {request.name}")
        db = SessionLocal()
        try:
            credit_service = CreditService(db)
            profile = credit_service.create_credit_profile(
                name=request.name,
                credit_score=request.credit_score,
                number_of_accounts=request.number_of_accounts,
                credit_utilization_ratio=request.credit_utilization_ratio,
                recent_soft_inquiries=request.recent_soft_inquiries,
                bankruptcies=request.bankruptcies,
                tax_liens=request.tax_liens,
                judgments=request.judgments
            )
            return self._credit_profile_to_proto(profile)
        except ValueError as e:
            logger.warning(f"Invalid input: {str(e)}")
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details(str(e))
        except Exception as e:
            logger.error(f"Error creating credit profile: {str(e)}", exc_info=True)
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details('An internal error occurred')
        finally:
            db.close()
        return credit_service_pb2.CreditProfileResponse()

    def GetAllCreditProfiles(self, request, context):
        logger.info("Received request to get all credit profiles")
        db = SessionLocal()
        try:
            credit_service = CreditService(db)
            profiles = credit_service.get_all_credit_profiles()
            
            response = credit_service_pb2.GetAllCreditProfilesResponse()
            for profile in profiles:
                profile_proto = response.profiles.add()
                self._populate_credit_profile_proto(profile, profile_proto)
            
            return response
        except Exception as e:
            logger.error(f"Error retrieving all credit profiles: {str(e)}", exc_info=True)
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details('An internal error occurred')
        finally:
            db.close()
        return credit_service_pb2.GetAllCreditProfilesResponse()

    def CreateDefaultLoanApplication(self, request, context):
        logger.info(f"Received create default loan application request for user ID {request.loan_amount_cents}")
        db = SessionLocal()
        try:
            credit_service = CreditService(db)
            success, new_loan_id = credit_service.create_default_loan_application(
                loan_amount_cents=request.loan_amount_cents,
                merchant_id=request.merchant_id,
            )
            return credit_service_pb2.CreateDefaultLoanApplicationResponse(success=success, loan_id=new_loan_id)
        except ValueError as e:
            logger.warning(f"Invalid input: {str(e)}")
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details(str(e))
        except Exception as e:
            logger.error(f"Error creating default loan application: {str(e)}", exc_info=True)
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details('An internal error occurred')
        finally:
            db.close()
        return credit_service_pb2.CreateDefaultLoanApplicationResponse(success=False, loan_id="")
        
    def _credit_profile_to_proto(self, profile):
        profile_proto = credit_service_pb2.CreditProfileResponse()
        self._populate_credit_profile_proto(profile, profile_proto)
        return profile_proto

    def _populate_credit_profile_proto(self, profile, profile_proto):
        profile_proto.id = str(profile.id)
        profile_proto.user_id = str(profile.user_id)
        profile_proto.name = profile.name
        profile_proto.credit_score = profile.credit_score
        profile_proto.number_of_accounts = profile.number_of_accounts
        profile_proto.credit_utilization_ratio = profile.credit_utilization_ratio
        profile_proto.recent_soft_inquiries = profile.recent_soft_inquiries
        profile_proto.bankruptcies = profile.bankruptcies
        profile_proto.tax_liens = profile.tax_liens
        profile_proto.judgments = profile.judgments
        profile_proto.created_at = profile.created_at.isoformat() if profile.created_at else ""
        profile_proto.updated_at = profile.updated_at.isoformat() if profile.updated_at else ""


    def GetLoanOptions(self, request, context):
        logger.info(f"Received get loan options request for user ID {request.user_id} / session {request.session_id}")

        db = SessionLocal()
        try:
            credit_service = CreditService(db)
            loan_options = credit_service.get_loan_options(request.user_id, request.session_id)

            response = credit_service_pb2.GetLoanOptionsResponse()
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

        return credit_service_pb2.GetLoanOptionsResponse()

    def UpdateCheckoutSessionForLoan(self, request, context):
        logger.info(f"Received update checkout session request for loan ID {request.loan_id}")
        db = SessionLocal()
        try:
            credit_service = CreditService(db)
            success = credit_service.update_checkout_session_for_loan(
                loan_id=request.loan_id,
                checkout_session_id=request.checkout_session_id
            )
            return credit_service_pb2.UpdateCheckoutSessionForLoanResponse(success=success)
        except ValueError as e:
            logger.warning(f"Invalid input: {str(e)}")
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details(str(e))
        except Exception as e:
            logger.error(f"Error updating checkout session for loan: {str(e)}", exc_info=True)
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details('An internal error occurred')
        finally:
            db.close()
        return credit_service_pb2.UpdateCheckoutSessionForLoanResponse(success=False)
        
    def _loan_to_proto(self, loan):
        return credit_service_pb2.Loan(
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
        
def add_to_server(server):
    credit_service_pb2_grpc.add_CreditServiceServicer_to_server(CreditServiceV1(), server)
