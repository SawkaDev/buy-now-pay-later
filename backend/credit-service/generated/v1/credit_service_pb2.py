# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: credit_service.proto
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
    'credit_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14\x63redit_service.proto\x12\x06\x63redit\"\xd9\x01\n\x1a\x43reateCreditProfileRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0c\x63redit_score\x18\x02 \x01(\x05\x12\x1a\n\x12number_of_accounts\x18\x03 \x01(\x05\x12 \n\x18\x63redit_utilization_ratio\x18\x04 \x01(\x02\x12\x1d\n\x15recent_soft_inquiries\x18\x05 \x01(\x05\x12\x14\n\x0c\x62\x61nkruptcies\x18\x06 \x01(\x05\x12\x11\n\ttax_liens\x18\x07 \x01(\x05\x12\x11\n\tjudgments\x18\x08 \x01(\x05\"\x99\x02\n\x15\x43reditProfileResponse\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07user_id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x14\n\x0c\x63redit_score\x18\x04 \x01(\x05\x12\x1a\n\x12number_of_accounts\x18\x05 \x01(\x05\x12 \n\x18\x63redit_utilization_ratio\x18\x06 \x01(\x02\x12\x1d\n\x15recent_soft_inquiries\x18\x07 \x01(\x05\x12\x14\n\x0c\x62\x61nkruptcies\x18\x08 \x01(\x05\x12\x11\n\ttax_liens\x18\t \x01(\x05\x12\x11\n\tjudgments\x18\n \x01(\x05\x12\x12\n\ncreated_at\x18\x0b \x01(\t\x12\x12\n\nupdated_at\x18\x0c \x01(\t2k\n\rCreditService\x12Z\n\x13\x43reateCreditProfile\x12\".credit.CreateCreditProfileRequest\x1a\x1d.credit.CreditProfileResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'credit_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_CREATECREDITPROFILEREQUEST']._serialized_start=33
  _globals['_CREATECREDITPROFILEREQUEST']._serialized_end=250
  _globals['_CREDITPROFILERESPONSE']._serialized_start=253
  _globals['_CREDITPROFILERESPONSE']._serialized_end=534
  _globals['_CREDITSERVICE']._serialized_start=536
  _globals['_CREDITSERVICE']._serialized_end=643
# @@protoc_insertion_point(module_scope)
