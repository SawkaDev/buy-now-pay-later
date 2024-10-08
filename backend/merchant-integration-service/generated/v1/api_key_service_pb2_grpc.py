# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from . import api_key_service_pb2 as api__key__service__pb2

GRPC_GENERATED_VERSION = '1.66.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in api_key_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class APIKeyServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GenerateAPIKey = channel.unary_unary(
                '/apikey.APIKeyService/GenerateAPIKey',
                request_serializer=api__key__service__pb2.GenerateAPIKeyRequest.SerializeToString,
                response_deserializer=api__key__service__pb2.APIKeyResponse.FromString,
                _registered_method=True)
        self.ValidateAPIKey = channel.unary_unary(
                '/apikey.APIKeyService/ValidateAPIKey',
                request_serializer=api__key__service__pb2.ValidateAPIKeyRequest.SerializeToString,
                response_deserializer=api__key__service__pb2.ValidateAPIKeyResponse.FromString,
                _registered_method=True)
        self.RevokeAPIKey = channel.unary_unary(
                '/apikey.APIKeyService/RevokeAPIKey',
                request_serializer=api__key__service__pb2.RevokeAPIKeyRequest.SerializeToString,
                response_deserializer=api__key__service__pb2.RevokeAPIKeyResponse.FromString,
                _registered_method=True)
        self.GetAPIKeysForUser = channel.unary_unary(
                '/apikey.APIKeyService/GetAPIKeysForUser',
                request_serializer=api__key__service__pb2.GetAPIKeysForUserRequest.SerializeToString,
                response_deserializer=api__key__service__pb2.GetAPIKeysForUserResponse.FromString,
                _registered_method=True)


class APIKeyServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GenerateAPIKey(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ValidateAPIKey(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RevokeAPIKey(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAPIKeysForUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_APIKeyServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GenerateAPIKey': grpc.unary_unary_rpc_method_handler(
                    servicer.GenerateAPIKey,
                    request_deserializer=api__key__service__pb2.GenerateAPIKeyRequest.FromString,
                    response_serializer=api__key__service__pb2.APIKeyResponse.SerializeToString,
            ),
            'ValidateAPIKey': grpc.unary_unary_rpc_method_handler(
                    servicer.ValidateAPIKey,
                    request_deserializer=api__key__service__pb2.ValidateAPIKeyRequest.FromString,
                    response_serializer=api__key__service__pb2.ValidateAPIKeyResponse.SerializeToString,
            ),
            'RevokeAPIKey': grpc.unary_unary_rpc_method_handler(
                    servicer.RevokeAPIKey,
                    request_deserializer=api__key__service__pb2.RevokeAPIKeyRequest.FromString,
                    response_serializer=api__key__service__pb2.RevokeAPIKeyResponse.SerializeToString,
            ),
            'GetAPIKeysForUser': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAPIKeysForUser,
                    request_deserializer=api__key__service__pb2.GetAPIKeysForUserRequest.FromString,
                    response_serializer=api__key__service__pb2.GetAPIKeysForUserResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'apikey.APIKeyService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('apikey.APIKeyService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class APIKeyService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GenerateAPIKey(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/apikey.APIKeyService/GenerateAPIKey',
            api__key__service__pb2.GenerateAPIKeyRequest.SerializeToString,
            api__key__service__pb2.APIKeyResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ValidateAPIKey(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/apikey.APIKeyService/ValidateAPIKey',
            api__key__service__pb2.ValidateAPIKeyRequest.SerializeToString,
            api__key__service__pb2.ValidateAPIKeyResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def RevokeAPIKey(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/apikey.APIKeyService/RevokeAPIKey',
            api__key__service__pb2.RevokeAPIKeyRequest.SerializeToString,
            api__key__service__pb2.RevokeAPIKeyResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetAPIKeysForUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/apikey.APIKeyService/GetAPIKeysForUser',
            api__key__service__pb2.GetAPIKeysForUserRequest.SerializeToString,
            api__key__service__pb2.GetAPIKeysForUserResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
