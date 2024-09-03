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
        logger.info(f"Received create default loan application request for user ID {request.user_id}")
        db = SessionLocal()
        try:
            credit_service = CreditService(db)
            success = credit_service.create_default_loan_application(
                user_id=request.user_id,
                loan_amount_cents=request.loan_amount_cents,
                loan_term_months=request.loan_term_months,
                merchant_id=request.merchant_id,
                session_id=request.session_id
            )
            return credit_service_pb2.CreateDefaultLoanApplicationResponse(success=success)
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
        return credit_service_pb2.CreateDefaultLoanApplicationResponse(success=False)
        
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

def add_to_server(server):
    credit_service_pb2_grpc.add_CreditServiceServicer_to_server(CreditServiceV1(), server)
