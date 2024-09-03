# credit_service/main.py

import grpc
from concurrent import futures
import logging
from api.v1 import credit_service
from core.config import settings
from core.db import init_db
from client.v1 import credit_service_pb2_grpc

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    
    credit_service_pb2_grpc.add_CreditServiceServicer_to_server(
        credit_service.CreditServiceV1(), server
    )
    
    server.add_insecure_port(f'[::]:{settings.SERVER_PORT}')
    server.start()
    logging.info(f"Server started on port {settings.SERVER_PORT}")
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    init_db()
    serve()
