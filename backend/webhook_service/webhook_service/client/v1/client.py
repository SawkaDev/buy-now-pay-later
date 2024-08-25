import grpc
from webhook_service.generated.v1 import webhook_service_pb2, webhook_service_pb2_grpc

class WebhookClientV1:
    def __init__(self, host='localhost', port=50051):
        self.channel = grpc.insecure_channel(f'{host}:{port}')
        self.stub = webhook_service_pb2_grpc.WebhookServiceStub(self.channel)

    def get_webhooks(self, user_id):
        request = webhook_service_pb2.GetWebhooksRequest(user_id=user_id)
        return self.stub.GetWebhooks(request)

    def create_webhook(self, user_id, url):
        request = webhook_service_pb2.CreateWebhookRequest(user_id=user_id, url=url)
        return self.stub.CreateWebhook(request)

    def get_webhook(self, webhook_id):
        request = webhook_service_pb2.GetWebhookRequest(webhook_id=webhook_id)
        return self.stub.GetWebhook(request)

    def update_webhook(self, webhook_id, url):
        request = webhook_service_pb2.UpdateWebhookRequest(webhook_id=webhook_id, url=url)
        return self.stub.UpdateWebhook(request)

    def disable_webhook(self, webhook_id):
        request = webhook_service_pb2.DisableWebhookRequest(webhook_id=webhook_id)
        return self.stub.DisableWebhook(request)
