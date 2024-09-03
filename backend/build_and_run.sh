#!/bin/bash

ORIGINAL_DIR=$(pwd)

cd ./credit-service
./build_package.sh

cd "$ORIGINAL_DIR" || exit 1

cd ./loan-service
./build_package.sh

cd "$ORIGINAL_DIR" || exit 1

# docker compose up --build