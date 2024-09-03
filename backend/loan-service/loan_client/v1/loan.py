import grpc
from . import loan_service_pb2, loan_service_pb2_grpc

class LoanClientV1:
    def __init__(self, host='localhost', port=50052):
        self.channel = grpc.insecure_channel(f'{host}:{port}')
        self.stub = loan_service_pb2_grpc.LoanServiceStub(self.channel)

    def get_loan(self, loan_id):
        request = loan_service_pb2.GetLoanRequest(loan_id=loan_id)
        return self.stub.GetLoan(request)

    def update_loan_status(self, loan_id, new_status):
        request = loan_service_pb2.UpdateLoanStatusRequest(loan_id=loan_id, new_status=new_status)
        return self.stub.UpdateLoanStatus(request)

    def update_payment(self, loan_id, payment_status):
        request = loan_service_pb2.PaymentUpdateRequest(loan_id=loan_id, payment_status=payment_status)
        return self.stub.UpdatePayment(request)

    def generate_checkout_session(self, loan_amount_cents, merchant_id, order_id, 
                                  success_redirect_url, cancel_redirect_url):
        request = loan_service_pb2.CheckoutSessionRequest(
            loan_amount_cents=loan_amount_cents,
            merchant_id=merchant_id,
            order_id=order_id,
            success_redirect_url=success_redirect_url,
            cancel_redirect_url=cancel_redirect_url
        )
        return self.stub.GenerateCheckoutSession(request)

    def get_loan_options(self, user_id, session_id):
        request = loan_service_pb2.GetLoanOptionsRequest(user_id=user_id, session_id=session_id)
        return self.stub.GetLoanOptions(request)