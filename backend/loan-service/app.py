# loan_service/main.py

import grpc
from concurrent import futures
import logging
from api.v1 import loan_service
from core.config import settings
from core.db import init_db
from generated.v1 import loan_service_pb2_grpc

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    
    # Add Loan service to the server
    loan_service_pb2_grpc.add_LoanServiceServicer_to_server(
        loan_service.LoanServiceV1(), server
    )
    
    server.add_insecure_port(f'[::]:{settings.SERVER_PORT}')
    server.start()
    logging.info(f"Server started on port {settings.SERVER_PORT}")
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    init_db()
    serve()
