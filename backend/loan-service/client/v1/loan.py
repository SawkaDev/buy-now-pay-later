import grpc
from generated.v1 import loan_service_pb2, loan_service_pb2_grpc

class LoanClientV1:
    def __init__(self, host='localhost', port=50051):
        self.channel = grpc.insecure_channel(f'{host}:{port}')
        self.stub = loan_service_pb2_grpc.LoanServiceStub(self.channel)

    def create_loan(self, user_id, loan_amount, loan_term_months, interest_rate, purpose, merchant_id=None, idempotency_key=None):
        request = loan_service_pb2.CreateLoanRequest(
            user_id=user_id,
            loan_amount=loan_amount,
            loan_term_months=loan_term_months,
            interest_rate=interest_rate,
            purpose=purpose,
            merchant_id=merchant_id,
            idempotency_key=idempotency_key
        )
        return self.stub.CreateLoan(request)

    def get_loan(self, loan_id):
        request = loan_service_pb2.GetLoanRequest(loan_id=loan_id)
        return self.stub.GetLoan(request)

    def update_loan_status(self, loan_id, new_status):
        request = loan_service_pb2.UpdateLoanStatusRequest(loan_id=loan_id, new_status=new_status)
        return self.stub.UpdateLoanStatus(request)

    def update_payment(self, loan_id, payment_status):
        request = loan_service_pb2.PaymentUpdateRequest(loan_id=loan_id, payment_status=payment_status)
        return self.stub.UpdatePayment(request)
