from setuptools import setup, find_packages

setup(
    name="merchant-integration-service",
    version="0.1.1",
    packages=find_packages(),
    install_requires=[
        "grpcio",
        "protobuf",
    ],
)
