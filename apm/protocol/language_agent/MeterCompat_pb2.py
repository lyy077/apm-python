# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: language-agent/MeterCompat.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ..common import Common_pb2 as common_dot_Common__pb2
from ..language_agent import Meter_pb2 as language__agent_dot_Meter__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='language-agent/MeterCompat.proto',
  package='',
  syntax='proto3',
  serialized_options=b'\n:org.apache.skywalking.apm.network.language.agent.v3.compatP\001Z:skywalking.apache.org/repo/goapi/collect/language/agent/v3\270\001\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n language-agent/MeterCompat.proto\x1a\x13\x63ommon/Common.proto\x1a\x1alanguage-agent/Meter.proto2V\n\x12MeterReportService\x12@\n\x07\x63ollect\x12\x18.skywalking.v3.MeterData\x1a\x17.skywalking.v3.Commands\"\x00(\x01\x42}\n:org.apache.skywalking.apm.network.language.agent.v3.compatP\x01Z:skywalking.apache.org/repo/goapi/collect/language/agent/v3\xb8\x01\x01\x62\x06proto3'
  ,
  dependencies=[common_dot_Common__pb2.DESCRIPTOR,language__agent_dot_Meter__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None

_METERREPORTSERVICE = _descriptor.ServiceDescriptor(
  name='MeterReportService',
  full_name='MeterReportService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=85,
  serialized_end=171,
  methods=[
  _descriptor.MethodDescriptor(
    name='collect',
    full_name='MeterReportService.collect',
    index=0,
    containing_service=None,
    input_type=language__agent_dot_Meter__pb2._METERDATA,
    output_type=common_dot_Common__pb2._COMMANDS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_METERREPORTSERVICE)

DESCRIPTOR.services_by_name['MeterReportService'] = _METERREPORTSERVICE

# @@protoc_insertion_point(module_scope)
