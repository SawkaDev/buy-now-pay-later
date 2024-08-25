import grpc
from generated.v1 import webhook_service_pb2, webhook_service_pb2_grpc
from models.webhooks import Webhook
from core.db import SessionLocal
from sqlalchemy.exc import SQLAlchemyError
from urllib.parse import urlparse
from google.protobuf.timestamp_pb2 import Timestamp

class WebhookServiceV1(webhook_service_pb2_grpc.WebhookServiceServicer):
    def is_valid_url(self, url):
        try:
            result = urlparse(url)
            return all([result.scheme, result.netloc])
        except ValueError:
            return False

    def GetWebhooks(self, request, context):
        db = SessionLocal()
        try:
            webhooks = db.query(Webhook).filter(Webhook.user_id == request.user_id).all()
            return webhook_service_pb2.GetWebhooksResponse(
                webhooks=[self.webhook_to_proto(w) for w in webhooks]
            )
        finally:
            db.close()

    def CreateWebhook(self, request, context):
        if not self.is_valid_url(request.url):
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details('Invalid URL format')
            return webhook_service_pb2.Webhook()

        db = SessionLocal()
        try:
            new_webhook = Webhook(user_id=request.user_id, url=request.url)
            db.add(new_webhook)
            db.commit()
            db.refresh(new_webhook)
            return self.webhook_to_proto(new_webhook)
        except SQLAlchemyError as e:
            db.rollback()
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f'Database error occurred: {str(e)}')
            return webhook_service_pb2.Webhook()
        finally:
            db.close()

    def GetWebhook(self, request, context):
        db = SessionLocal()
        try:
            webhook = db.query(Webhook).get(request.webhook_id)
            if not webhook:
                context.set_code(grpc.StatusCode.NOT_FOUND)
                context.set_details('Webhook not found')
                return webhook_service_pb2.Webhook()
            return self.webhook_to_proto(webhook)
        finally:
            db.close()

    def UpdateWebhook(self, request, context):
        if not self.is_valid_url(request.url):
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details('Invalid URL format')
            return webhook_service_pb2.Webhook()

        db = SessionLocal()
        try:
            webhook = db.query(Webhook).get(request.webhook_id)
            if not webhook:
                context.set_code(grpc.StatusCode.NOT_FOUND)
                context.set_details('Webhook not found')
                return webhook_service_pb2.Webhook()

            webhook.url = request.url
            db.commit()
            db.refresh(webhook)
            return self.webhook_to_proto(webhook)
        except SQLAlchemyError as e:
            db.rollback()
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f'Database error occurred: {str(e)}')
            return webhook_service_pb2.Webhook()
        finally:
            db.close()

    def DisableWebhook(self, request, context):
        db = SessionLocal()
        try:
            webhook = db.query(Webhook).get(request.webhook_id)
            if not webhook:
                context.set_code(grpc.StatusCode.NOT_FOUND)
                context.set_details('Webhook not found')
                return webhook_service_pb2.DisableWebhookResponse()

            if not webhook.is_active:
                context.set_code(grpc.StatusCode.FAILED_PRECONDITION)
                context.set_details('Webhook is already inactive')
                return webhook_service_pb2.DisableWebhookResponse()

            webhook.is_active = False
            db.commit()
            return webhook_service_pb2.DisableWebhookResponse(message='Webhook revoked successfully')
        finally:
            db.close()

    def webhook_to_proto(self, webhook):
        proto_webhook = webhook_service_pb2.Webhook(
            id=webhook.id,
            user_id=webhook.user_id,
            url=webhook.url,
            is_active=webhook.is_active,
            created_at=webhook.created_at.isoformat() if webhook.created_at else None,
            updated_at=webhook.updated_at.isoformat() if webhook.updated_at else None
        )
        return proto_webhook

def add_to_server(server):
    webhook_service_pb2_grpc.add_WebhookServiceServicer_to_server(WebhookServiceV1(), server)
