# webhook_service/api/v1/api_key_service.py

import grpc
from generated.v1 import api_key_service_pb2, api_key_service_pb2_grpc
from models.api_key import APIKey
from core.db import SessionLocal
from sqlalchemy.exc import SQLAlchemyError
from google.protobuf.timestamp_pb2 import Timestamp
from datetime import datetime, timedelta
import secrets

def create_api_key_token():
    return secrets.token_urlsafe(32)

class APIKeyServiceV1(api_key_service_pb2_grpc.APIKeyServiceServicer):
    def GenerateAPIKey(self, request, context):
        db = SessionLocal()
        try:
            active_api_keys_count = db.query(APIKey).filter_by(user_id=request.user_id, is_active=True).count()
            if active_api_keys_count >= 5:
                context.set_code(grpc.StatusCode.FAILED_PRECONDITION)
                context.set_details('Maximum number of active API keys has been reached.')
                return api_key_service_pb2.APIKeyResponse()

            new_key = APIKey(
                key=create_api_key_token(),
                user_id=request.user_id,
                expires_at=datetime.utcnow() + timedelta(days=30)
            )
            db.add(new_key)
            db.commit()
            db.refresh(new_key)
            return api_key_service_pb2.APIKeyResponse(api_key=self.api_key_to_proto(new_key))
        except SQLAlchemyError as e:
            db.rollback()
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f'Database error occurred: {str(e)}')
            return api_key_service_pb2.APIKeyResponse()
        finally:
            db.close()

    def ValidateAPIKey(self, request, context):
        db = SessionLocal()
        try:
            api_key = db.query(APIKey).filter_by(key=request.key_id).first()
            if api_key:
                api_key.check_expiration()
                if api_key.is_active:
                    return api_key_service_pb2.ValidateAPIKeyResponse(is_valid=True, message="API key is valid")
                else:
                    return api_key_service_pb2.ValidateAPIKeyResponse(is_valid=False, message="API key has expired")
            return api_key_service_pb2.ValidateAPIKeyResponse(is_valid=False, message="Invalid API key")
        finally:
            db.close()

    def RevokeAPIKey(self, request, context):
        db = SessionLocal()
        try:
            api_key = db.query(APIKey).get(request.key_id)
            if not api_key:
                context.set_code(grpc.StatusCode.NOT_FOUND)
                context.set_details('API key not found')
                return api_key_service_pb2.RevokeAPIKeyResponse()

            if not api_key.is_active:
                context.set_code(grpc.StatusCode.FAILED_PRECONDITION)
                context.set_details('API key is already inactive')
                return api_key_service_pb2.RevokeAPIKeyResponse()

            api_key.is_active = False
            db.commit()
            return api_key_service_pb2.RevokeAPIKeyResponse(success=True, message='API key revoked successfully')
        except SQLAlchemyError as e:
            db.rollback()
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f'Database error occurred: {str(e)}')
            return api_key_service_pb2.RevokeAPIKeyResponse()
        finally:
            db.close()

    def GetAPIKeysForUser(self, request, context):
        db = SessionLocal()
        try:
            api_keys = db.query(APIKey).filter_by(user_id=request.user_id).all()
            if not api_keys:
                context.set_code(grpc.StatusCode.NOT_FOUND)
                context.set_details('No API keys found for the user')
                return api_key_service_pb2.GetAPIKeysForUserResponse()
            return api_key_service_pb2.GetAPIKeysForUserResponse(
                api_keys=[self.api_key_to_proto(key) for key in api_keys]
            )
        finally:
            db.close()

    def api_key_to_proto(self, api_key):
        proto_api_key = api_key_service_pb2.APIKey(
            id=api_key.id,
            key=api_key.key,
            user_id=api_key.user_id,
            is_active=api_key.is_active,
            is_expired=api_key.is_expired,
            created_at=api_key.created_at.isoformat() if api_key.created_at else None,
            expires_at=api_key.expires_at.isoformat() if api_key.expires_at else None
        )

        return proto_api_key

def add_to_server(server):
    api_key_service_pb2_grpc.add_APIKeyServiceServicer_to_server(APIKeyServiceV1(), server)
