# webhook_service/main.py

import grpc
from concurrent import futures
import logging
from api.v1 import webhook_service, api_key_service
from core.config import settings
from core.db import init_db
from generated.v1 import webhook_service_pb2_grpc, api_key_service_pb2_grpc

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    
    # Add Webhook service to the server
    webhook_service_pb2_grpc.add_WebhookServiceServicer_to_server(
        webhook_service.WebhookServiceV1(), server
    )
    
    # Add API Key service to the server
    api_key_service_pb2_grpc.add_APIKeyServiceServicer_to_server(
        api_key_service.APIKeyServiceV1(), server
    )
    
    server.add_insecure_port(f'[::]:{settings.SERVER_PORT}')
    server.start()
    logging.info(f"Server started on port {settings.SERVER_PORT}")
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    init_db()
    serve()
