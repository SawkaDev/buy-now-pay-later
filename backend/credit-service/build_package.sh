#!/bin/bash

ORIGINAL_DIR=$(pwd)

cd ./protos/v1 || exit 1

# Run the gRPC tools command
python -m grpc_tools.protoc -I. \
    --python_out=./../../client/v1 \
    --grpc_python_out=./../../client/v1 \
    credit_service.proto

cd "$ORIGINAL_DIR" || exit 1

# Run a Python script to fix imports
python - <<EOF
import os
import re

def fix_imports(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    
    # Replace absolute import with relative import
    content = re.sub(
        r'import credit_service_pb2 as credit__service__pb2',
        'from . import credit_service_pb2 as credit__service__pb2',
        content
    )
    
    with open(file_path, 'w') as file:
        file.write(content)

# Fix imports in the generated files
fix_imports('./client/v1/credit_service_pb2_grpc.py')

print("Imports fixed successfully.")
EOF

# Run the sdist command
python setup.py sdist --formats=gztar --dist-dir=../shared

# Remove the .egg-info directory
find . -name "*.egg-info" -type d -exec rm -r {} +