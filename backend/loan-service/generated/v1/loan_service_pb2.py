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




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12loan_service.proto\x12\x04loan\"\x95\x01\n\x16\x43heckoutSessionRequest\x12\x19\n\x11loan_amount_cents\x18\x01 \x01(\x03\x12\x13\n\x0bmerchant_id\x18\x02 \x01(\x05\x12\x10\n\x08order_id\x18\x03 \x01(\t\x12\x1c\n\x14success_redirect_url\x18\x04 \x01(\t\x12\x1b\n\x13\x63\x61ncel_redirect_url\x18\x05 \x01(\t\"/\n\x17\x43heckoutSessionResponse\x12\x14\n\x0c\x63heckout_url\x18\x01 \x01(\t2g\n\x0bLoanService\x12X\n\x17GenerateCheckoutSession\x12\x1c.loan.CheckoutSessionRequest\x1a\x1d.loan.CheckoutSessionResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'loan_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_CHECKOUTSESSIONREQUEST']._serialized_start=29
  _globals['_CHECKOUTSESSIONREQUEST']._serialized_end=178
  _globals['_CHECKOUTSESSIONRESPONSE']._serialized_start=180
  _globals['_CHECKOUTSESSIONRESPONSE']._serialized_end=227
  _globals['_LOANSERVICE']._serialized_start=229
  _globals['_LOANSERVICE']._serialized_end=332
# @@protoc_insertion_point(module_scope)
