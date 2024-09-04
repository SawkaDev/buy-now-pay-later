import grpc
from google.protobuf import empty_pb2
from . import credit_service_pb2, credit_service_pb2_grpc
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

    def get_all_credit_profiles(self):
        request = empty_pb2.Empty()
        return self.stub.GetAllCreditProfiles(request)

    def create_default_loan_application(self, loan_amount_cents, merchant_id):
        request = credit_service_pb2.CreateDefaultLoanApplicationRequest(
            loan_amount_cents=loan_amount_cents,
            merchant_id=merchant_id,
        )
        return self.stub.CreateDefaultLoanApplication(request)

    def get_loan_options(self, user_id, session_id):
        request = credit_service_pb2.GetLoanOptionsRequest(
            user_id=user_id,
            session_id=session_id,
        )
        return self.stub.GetLoanOptions(request)

    def update_checkout_session_for_loan(self, loan_id, checkout_session_id):
        request = credit_service_pb2.UpdateCheckoutSessionForLoanRequest(
            loan_id=loan_id,
            checkout_session_id=checkout_session_id
        )
        response = self.stub.UpdateCheckoutSessionForLoan(request)
        return response.success


    def select_loan(self, user_id, checkout_session_id, loan_term_months, 
                    interest_rate, monthly_payment_cents, total_payment_amount_cents):
        request = credit_service_pb2.SelectLoanRequest(
            user_id=user_id,
            checkout_session_id=checkout_session_id,
            loan_term_months=loan_term_months,
            interest_rate=interest_rate,
            monthly_payment_cents=monthly_payment_cents,
            total_payment_amount_cents=total_payment_amount_cents
        )
        return self.stub.SelectLoan(request)

    def get_loan_for_checkout_session(self, checkout_session_id, user_id):
        request = credit_service_pb2.GetLoanForCheckoutSessionRequest(
            checkout_session_id=checkout_session_id,
            user_id=user_id
        )
        response = self.stub.GetLoanForCheckoutSession(request)
        return response.status