# gRPC Service


python -m grpc_tools.protoc -I. --python_out=../../generated/v1 --grpc_python_out=../../generated/v1 webhook_service.proto