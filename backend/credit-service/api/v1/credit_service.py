# credit_service_v1.py

import logging
import grpc
from generated.v1 import credit_service_pb2, credit_service_pb2_grpc
from core.db import SessionLocal
from .credit_service_logic import CreditService

logger = logging.getLogger(__name__)

class CreditServiceV1(credit_service_pb2_grpc.CreditServiceServicer):

    def CreateCreditProfile(self, request, context):
        logger.info(f"Received create credit profile request for user ID {request.name}")
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

    def GetCreditProfile(self, request, context):
        logger.info(f"Received get credit profile request for user ID {request.user_id}")
        db = SessionLocal()
        try:
            credit_service = CreditService(db)
            profile = credit_service.get_credit_profile(request.user_id)
            return self._credit_profile_to_proto(profile)
        except LookupError:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('Credit profile not found')
        except Exception as e:
            logger.error(f"Error retrieving credit profile: {str(e)}", exc_info=True)
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details('An internal error occurred')
        finally:
            db.close()
        return credit_service_pb2.CreditProfileResponse()

    def UpdateCreditProfile(self, request, context):
        logger.info(f"Received update credit profile request for user ID {request.user_id}")
        db = SessionLocal()
        try:
            credit_service = CreditService(db)
            profile = credit_service.update_credit_profile(
                user_id=request.user_id,
                credit_score=request.credit_score,
                number_of_accounts=request.number_of_accounts,
                credit_utilization_ratio=request.credit_utilization_ratio,
                recent_soft_inquiries=request.recent_soft_inquiries,
                bankruptcies=request.bankruptcies,
                tax_liens=request.tax_liens,
                judgments=request.judgments
            )
            return self._credit_profile_to_proto(profile)
        except LookupError:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('Credit profile not found')
        except ValueError as e:
            logger.warning(f"Invalid input: {str(e)}")
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details(str(e))
        except Exception as e:
            logger.error(f"Error updating credit profile: {str(e)}", exc_info=True)
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details('An internal error occurred')
        finally:
            db.close()
        return credit_service_pb2.CreditProfileResponse()

    def _credit_profile_to_proto(self, profile):
        return credit_service_pb2.CreditProfileResponse(
            id=str(profile.id),
            user_id=str(profile.user_id),
            name=profile.name,
            credit_score=profile.credit_score,
            number_of_accounts=profile.number_of_accounts,
            credit_utilization_ratio=profile.credit_utilization_ratio,
            recent_soft_inquiries=profile.recent_soft_inquiries,
            bankruptcies=profile.bankruptcies,
            tax_liens=profile.tax_liens,
            judgments=profile.judgments,
            created_at=profile.created_at.isoformat() if profile.created_at else "",
            updated_at=profile.updated_at.isoformat() if profile.updated_at else ""
        )

def add_to_server(server):
    credit_service_pb2_grpc.add_CreditServiceServicer_to_server(CreditServiceV1(), server)
