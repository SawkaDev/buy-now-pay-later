# webhook_service/main.py

import grpc
from concurrent import futures
import logging
from api.v1 import webhook_service
from core.config import settings
from core.db import init_db
from generated.v1 import webhook_service_pb2_grpc  # Add this import

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    webhook_service_pb2_grpc.add_WebhookServiceServicer_to_server(
        webhook_service.WebhookServiceV1(), server
    )
    server.add_insecure_port(f'[::]:{settings.SERVER_PORT}')
    server.start()
    logging.info(f"Server started on port {settings.SERVER_PORT}")
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    init_db()
    serve()
