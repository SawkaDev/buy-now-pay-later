import grpc
from generated.v1 import credit_service_pb2, credit_service_pb2_grpc

class CreditClientV1:
    def __init__(self, host='localhost', port=50053):
        self.channel = grpc.insecure_channel(f'{host}:{port}')
        self.stub = credit_service_pb2_grpc.CreditServiceStub(self.channel)

    def create_credit_profile(self, name, credit_score, number_of_accounts, 
                              credit_utilization_ratio, recent_soft_inquiries, 
                              bankruptcies, tax_liens, judgments):
        request = credit_service_pb2.CreateCreditProfileRequest(
            name=name,
            credit_score=credit_score,
            number_of_accounts=number_of_accounts,
            credit_utilization_ratio=credit_utilization_ratio,
            recent_soft_inquiries=recent_soft_inquiries,
            bankruptcies=bankruptcies,
            tax_liens=tax_liens,
            judgments=judgments
        )
        return self.stub.CreateCreditProfile(request)