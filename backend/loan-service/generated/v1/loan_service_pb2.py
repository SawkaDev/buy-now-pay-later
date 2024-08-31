# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: loan_service.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'loan_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12loan_service.proto\x12\x04loan\"!\n\x0eGetLoanRequest\x12\x0f\n\x07loan_id\x18\x01 \x01(\x05\">\n\x17UpdateLoanStatusRequest\x12\x0f\n\x07loan_id\x18\x01 \x01(\x05\x12\x12\n\nnew_status\x18\x02 \x01(\t\"Y\n\x0cLoanResponse\x12\x18\n\x04loan\x18\x01 \x01(\x0b\x32\n.loan.Loan\x12/\n\x10\x63heckout_session\x18\x02 \x01(\x0b\x32\x15.loan.CheckoutSession\"\xbc\x01\n\x04Loan\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0f\n\x07user_id\x18\x02 \x01(\x05\x12\x19\n\x11loan_amount_cents\x18\x03 \x01(\x03\x12\x18\n\x10loan_term_months\x18\x04 \x01(\x05\x12\x15\n\rinterest_rate\x18\x05 \x01(\x05\x12\x0e\n\x06status\x18\x06 \x01(\t\x12\x13\n\x0bmerchant_id\x18\x07 \x01(\x05\x12\x12\n\ncreated_at\x18\x08 \x01(\t\x12\x12\n\nupdated_at\x18\t \x01(\t\"\xdd\x01\n\x0f\x43heckoutSession\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07loan_id\x18\x02 \x01(\x05\x12\x10\n\x08order_id\x18\x03 \x01(\t\x12\x1c\n\x14success_redirect_url\x18\x04 \x01(\t\x12\x1b\n\x13\x63\x61ncel_redirect_url\x18\x05 \x01(\t\x12\x14\n\x0c\x63heckout_url\x18\x06 \x01(\t\x12\x0e\n\x06status\x18\x07 \x01(\t\x12\x12\n\nexpires_at\x18\x08 \x01(\t\x12\x12\n\ncreated_at\x18\t \x01(\t\x12\x12\n\nupdated_at\x18\n \x01(\t\"?\n\x14PaymentUpdateRequest\x12\x0f\n\x07loan_id\x18\x01 \x01(\x05\x12\x16\n\x0epayment_status\x18\x02 \x01(\t\"(\n\x15PaymentUpdateResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"\x95\x01\n\x16\x43heckoutSessionRequest\x12\x19\n\x11loan_amount_cents\x18\x01 \x01(\x03\x12\x13\n\x0bmerchant_id\x18\x02 \x01(\x05\x12\x10\n\x08order_id\x18\x03 \x01(\t\x12\x1c\n\x14success_redirect_url\x18\x04 \x01(\t\x12\x1b\n\x13\x63\x61ncel_redirect_url\x18\x05 \x01(\t\"/\n\x17\x43heckoutSessionResponse\x12\x14\n\x0c\x63heckout_url\x18\x01 \x01(\t\"<\n\x15GetLoanOptionsRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x12\n\nsession_id\x18\x02 \x01(\t\"@\n\x16GetLoanOptionsResponse\x12&\n\x0cloan_options\x18\x01 \x03(\x0b\x32\x10.loan.LoanOption\"\x9b\x01\n\nLoanOption\x12\n\n\x02id\x18\x01 \x01(\t\x12\x19\n\x11loan_amount_cents\x18\x02 \x01(\x05\x12\x18\n\x10loan_term_months\x18\x03 \x01(\x05\x12\x15\n\rinterest_rate\x18\x04 \x01(\x02\x12\x17\n\x0fmonthly_payment\x18\x05 \x01(\x02\x12\x1c\n\x14total_payment_amount\x18\x06 \x01(\x02\x32\x82\x03\n\x0bLoanService\x12\x35\n\x07GetLoan\x12\x14.loan.GetLoanRequest\x1a\x12.loan.LoanResponse\"\x00\x12G\n\x10UpdateLoanStatus\x12\x1d.loan.UpdateLoanStatusRequest\x1a\x12.loan.LoanResponse\"\x00\x12J\n\rUpdatePayment\x12\x1a.loan.PaymentUpdateRequest\x1a\x1b.loan.PaymentUpdateResponse\"\x00\x12X\n\x17GenerateCheckoutSession\x12\x1c.loan.CheckoutSessionRequest\x1a\x1d.loan.CheckoutSessionResponse\"\x00\x12M\n\x0eGetLoanOptions\x12\x1b.loan.GetLoanOptionsRequest\x1a\x1c.loan.GetLoanOptionsResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'loan_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_GETLOANREQUEST']._serialized_start=28
  _globals['_GETLOANREQUEST']._serialized_end=61
  _globals['_UPDATELOANSTATUSREQUEST']._serialized_start=63
  _globals['_UPDATELOANSTATUSREQUEST']._serialized_end=125
  _globals['_LOANRESPONSE']._serialized_start=127
  _globals['_LOANRESPONSE']._serialized_end=216
  _globals['_LOAN']._serialized_start=219
  _globals['_LOAN']._serialized_end=407
  _globals['_CHECKOUTSESSION']._serialized_start=410
  _globals['_CHECKOUTSESSION']._serialized_end=631
  _globals['_PAYMENTUPDATEREQUEST']._serialized_start=633
  _globals['_PAYMENTUPDATEREQUEST']._serialized_end=696
  _globals['_PAYMENTUPDATERESPONSE']._serialized_start=698
  _globals['_PAYMENTUPDATERESPONSE']._serialized_end=738
  _globals['_CHECKOUTSESSIONREQUEST']._serialized_start=741
  _globals['_CHECKOUTSESSIONREQUEST']._serialized_end=890
  _globals['_CHECKOUTSESSIONRESPONSE']._serialized_start=892
  _globals['_CHECKOUTSESSIONRESPONSE']._serialized_end=939
  _globals['_GETLOANOPTIONSREQUEST']._serialized_start=941
  _globals['_GETLOANOPTIONSREQUEST']._serialized_end=1001
  _globals['_GETLOANOPTIONSRESPONSE']._serialized_start=1003
  _globals['_GETLOANOPTIONSRESPONSE']._serialized_end=1067
  _globals['_LOANOPTION']._serialized_start=1070
  _globals['_LOANOPTION']._serialized_end=1225
  _globals['_LOANSERVICE']._serialized_start=1228
  _globals['_LOANSERVICE']._serialized_end=1614
# @@protoc_insertion_point(module_scope)
