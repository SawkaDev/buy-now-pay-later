import grpc
from generated.v1 import api_key_service_pb2, api_key_service_pb2_grpc

class APIKeyClientV1:
    def __init__(self, host='localhost', port=50051):
        self.channel = grpc.insecure_channel(f'{host}:{port}')
        self.stub = api_key_service_pb2_grpc.APIKeyServiceStub(self.channel)

    def generate_api_key(self, user_id):
        request = api_key_service_pb2.GenerateAPIKeyRequest(user_id=user_id)
        return self.stub.GenerateAPIKey(request)

    def validate_api_key(self, key_id):
        request = api_key_service_pb2.ValidateAPIKeyRequest(key_id=key_id)
        return self.stub.ValidateAPIKey(request)

    def revoke_api_key(self, key_id):
        request = api_key_service_pb2.RevokeAPIKeyRequest(key_id=key_id)
        return self.stub.RevokeAPIKey(request)

    def get_api_keys_for_user(self, user_id):
        request = api_key_service_pb2.GetAPIKeysForUserRequest(user_id=user_id)
        return self.stub.GetAPIKeysForUser(request)
