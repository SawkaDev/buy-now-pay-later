# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from . import credit_service_pb2 as credit__service__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2

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
        + f' but the generated code in credit_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class CreditServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateCreditProfile = channel.unary_unary(
                '/credit.CreditService/CreateCreditProfile',
                request_serializer=credit__service__pb2.CreateCreditProfileRequest.SerializeToString,
                response_deserializer=credit__service__pb2.CreditProfileResponse.FromString,
                _registered_method=True)
        self.GetAllCreditProfiles = channel.unary_unary(
                '/credit.CreditService/GetAllCreditProfiles',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=credit__service__pb2.GetAllCreditProfilesResponse.FromString,
                _registered_method=True)
        self.CreateDefaultLoanApplication = channel.unary_unary(
                '/credit.CreditService/CreateDefaultLoanApplication',
                request_serializer=credit__service__pb2.CreateDefaultLoanApplicationRequest.SerializeToString,
                response_deserializer=credit__service__pb2.CreateDefaultLoanApplicationResponse.FromString,
                _registered_method=True)
        self.GetLoanOptions = channel.unary_unary(
                '/credit.CreditService/GetLoanOptions',
                request_serializer=credit__service__pb2.GetLoanOptionsRequest.SerializeToString,
                response_deserializer=credit__service__pb2.GetLoanOptionsResponse.FromString,
                _registered_method=True)
        self.UpdateCheckoutSessionForLoan = channel.unary_unary(
                '/credit.CreditService/UpdateCheckoutSessionForLoan',
                request_serializer=credit__service__pb2.UpdateCheckoutSessionForLoanRequest.SerializeToString,
                response_deserializer=credit__service__pb2.UpdateCheckoutSessionForLoanResponse.FromString,
                _registered_method=True)
        self.SelectLoan = channel.unary_unary(
                '/credit.CreditService/SelectLoan',
                request_serializer=credit__service__pb2.SelectLoanRequest.SerializeToString,
                response_deserializer=credit__service__pb2.SelectLoanResponse.FromString,
                _registered_method=True)
        self.GetLoanForCheckoutSession = channel.unary_unary(
                '/credit.CreditService/GetLoanForCheckoutSession',
                request_serializer=credit__service__pb2.GetLoanForCheckoutSessionRequest.SerializeToString,
                response_deserializer=credit__service__pb2.GetLoanForCheckoutSessionResponse.FromString,
                _registered_method=True)


class CreditServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateCreditProfile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAllCreditProfiles(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateDefaultLoanApplication(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetLoanOptions(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateCheckoutSessionForLoan(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SelectLoan(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetLoanForCheckoutSession(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CreditServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateCreditProfile': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateCreditProfile,
                    request_deserializer=credit__service__pb2.CreateCreditProfileRequest.FromString,
                    response_serializer=credit__service__pb2.CreditProfileResponse.SerializeToString,
            ),
            'GetAllCreditProfiles': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAllCreditProfiles,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=credit__service__pb2.GetAllCreditProfilesResponse.SerializeToString,
            ),
            'CreateDefaultLoanApplication': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateDefaultLoanApplication,
                    request_deserializer=credit__service__pb2.CreateDefaultLoanApplicationRequest.FromString,
                    response_serializer=credit__service__pb2.CreateDefaultLoanApplicationResponse.SerializeToString,
            ),
            'GetLoanOptions': grpc.unary_unary_rpc_method_handler(
                    servicer.GetLoanOptions,
                    request_deserializer=credit__service__pb2.GetLoanOptionsRequest.FromString,
                    response_serializer=credit__service__pb2.GetLoanOptionsResponse.SerializeToString,
            ),
            'UpdateCheckoutSessionForLoan': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateCheckoutSessionForLoan,
                    request_deserializer=credit__service__pb2.UpdateCheckoutSessionForLoanRequest.FromString,
                    response_serializer=credit__service__pb2.UpdateCheckoutSessionForLoanResponse.SerializeToString,
            ),
            'SelectLoan': grpc.unary_unary_rpc_method_handler(
                    servicer.SelectLoan,
                    request_deserializer=credit__service__pb2.SelectLoanRequest.FromString,
                    response_serializer=credit__service__pb2.SelectLoanResponse.SerializeToString,
            ),
            'GetLoanForCheckoutSession': grpc.unary_unary_rpc_method_handler(
                    servicer.GetLoanForCheckoutSession,
                    request_deserializer=credit__service__pb2.GetLoanForCheckoutSessionRequest.FromString,
                    response_serializer=credit__service__pb2.GetLoanForCheckoutSessionResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'credit.CreditService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('credit.CreditService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class CreditService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateCreditProfile(request,
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
            '/credit.CreditService/CreateCreditProfile',
            credit__service__pb2.CreateCreditProfileRequest.SerializeToString,
            credit__service__pb2.CreditProfileResponse.FromString,
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
    def GetAllCreditProfiles(request,
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
            '/credit.CreditService/GetAllCreditProfiles',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            credit__service__pb2.GetAllCreditProfilesResponse.FromString,
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
    def CreateDefaultLoanApplication(request,
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
            '/credit.CreditService/CreateDefaultLoanApplication',
            credit__service__pb2.CreateDefaultLoanApplicationRequest.SerializeToString,
            credit__service__pb2.CreateDefaultLoanApplicationResponse.FromString,
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
    def GetLoanOptions(request,
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
            '/credit.CreditService/GetLoanOptions',
            credit__service__pb2.GetLoanOptionsRequest.SerializeToString,
            credit__service__pb2.GetLoanOptionsResponse.FromString,
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
    def UpdateCheckoutSessionForLoan(request,
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
            '/credit.CreditService/UpdateCheckoutSessionForLoan',
            credit__service__pb2.UpdateCheckoutSessionForLoanRequest.SerializeToString,
            credit__service__pb2.UpdateCheckoutSessionForLoanResponse.FromString,
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
    def SelectLoan(request,
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
            '/credit.CreditService/SelectLoan',
            credit__service__pb2.SelectLoanRequest.SerializeToString,
            credit__service__pb2.SelectLoanResponse.FromString,
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
    def GetLoanForCheckoutSession(request,
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
            '/credit.CreditService/GetLoanForCheckoutSession',
            credit__service__pb2.GetLoanForCheckoutSessionRequest.SerializeToString,
            credit__service__pb2.GetLoanForCheckoutSessionResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
