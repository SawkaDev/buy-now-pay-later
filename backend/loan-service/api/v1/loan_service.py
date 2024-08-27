import grpc
from generated.v1 import loan_service_pb2, loan_service_pb2_grpc
from models.loan import Loan, LoanStatus
from core.db import SessionLocal
from sqlalchemy.exc import SQLAlchemyError

class LoanServiceV1(loan_service_pb2_grpc.LoanServiceServicer):
    def CreateLoan(self, request, context):
        db = SessionLocal()
        try:
            new_loan = Loan(
                user_id=request.user_id,
                loan_amount=request.loan_amount,
                loan_term_months=request.loan_term_months,
                interest_rate=request.interest_rate,
                purpose=request.purpose,
                merchant_id=request.merchant_id
            )
            db.add(new_loan)
            db.commit()
            db.refresh(new_loan)
            return loan_service_pb2.LoanResponse(
                loan=self.loan_to_proto(new_loan)
            )
        except SQLAlchemyError as e:
            db.rollback()
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f'Database error occurred: {str(e)}')
            return loan_service_pb2.LoanResponse()
        finally:
            db.close()

    def GetLoan(self, request, context):
        db = SessionLocal()
        try:
            loan = db.query(Loan).get(request.loan_id)
            if not loan:
                context.set_code(grpc.StatusCode.NOT_FOUND)
                context.set_details('Loan not found')
                return loan_service_pb2.LoanResponse()
            return loan_service_pb2.LoanResponse(
                loan=self.loan_to_proto(loan)
            )
        finally:
            db.close()

    def UpdateLoanStatus(self, request, context):
        db = SessionLocal()
        try:
            loan = db.query(Loan).get(request.loan_id)
            if not loan:
                context.set_code(grpc.StatusCode.NOT_FOUND)
                context.set_details('Loan not found')
                return loan_service_pb2.LoanResponse()
            
            try:
                new_status = LoanStatus(request.new_status)
            except ValueError:
                context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
                context.set_details('Invalid loan status')
                return loan_service_pb2.LoanResponse()
             
            loan.status = new_status
            db.commit()
            db.refresh(loan)
            return loan_service_pb2.LoanResponse(
                loan=self.loan_to_proto(loan)
            )
        except SQLAlchemyError as e:
            db.rollback()
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f'Database error occurred: {str(e)}')
            return loan_service_pb2.LoanResponse()
        finally:
            db.close()

    def UpdatePayment(self, request, context):
        db = SessionLocal()
        try:
            loan = db.query(Loan).get(request.loan_id)
            if not loan:
                context.set_code(grpc.StatusCode.NOT_FOUND)
                context.set_details('Loan not found')
                return loan_service_pb2.PaymentUpdateResponse(success=False)
            
            if request.payment_status == 'PAID_OFF':
                loan.status = LoanStatus.PAID_OFF
            elif loan.status == LoanStatus.APPROVED and request.payment_status == 'PAYMENT_RECEIVED':
                loan.status = LoanStatus.IN_REPAYMENT
            elif request.payment_status == 'DEFAULTED':
                loan.status = LoanStatus.DEFAULTED
            
            db.commit()
            return loan_service_pb2.PaymentUpdateResponse(success=True)
        except SQLAlchemyError as e:
            db.rollback()
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f'Database error occurred: {str(e)}')
            return loan_service_pb2.PaymentUpdateResponse(success=False)
        finally:
            db.close()

    def loan_to_proto(self, loan):
        return loan_service_pb2.Loan(
            id=loan.id,
            user_id=loan.user_id,
            loan_amount=loan.loan_amount,
            loan_term_months=loan.loan_term_months,
            interest_rate=loan.interest_rate,
            purpose=loan.purpose,
            status=loan.status.value,
            merchant_id=loan.merchant_id,
            created_at=loan.created_at.isoformat() if loan.created_at else None,
            updated_at=loan.updated_at.isoformat() if loan.updated_at else None
        )

def add_to_server(server):
    loan_service_pb2_grpc.add_LoanServiceServicer_to_server(LoanServiceV1(), server)
