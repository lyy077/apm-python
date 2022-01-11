# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: language-agent/TracingCompat.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ..common import Common_pb2 as common_dot_Common__pb2
from ..language_agent import Tracing_pb2 as language__agent_dot_Tracing__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='language-agent/TracingCompat.proto',
  package='',
  syntax='proto3',
  serialized_options=b'\n:org.apache.skywalking.apm.network.language.agent.v3.compatP\001Z:skywalking.apache.org/repo/goapi/collect/language/agent/v3\270\001\001\252\002\035SkyWalking.NetworkProtocol.V3',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\"language-agent/TracingCompat.proto\x1a\x13\x63ommon/Common.proto\x1a\x1clanguage-agent/Tracing.proto2\xaf\x01\n\x19TraceSegmentReportService\x12\x44\n\x07\x63ollect\x12\x1c.skywalking.v3.SegmentObject\x1a\x17.skywalking.v3.Commands\"\x00(\x01\x12L\n\rcollectInSync\x12 .skywalking.v3.SegmentCollection\x1a\x17.skywalking.v3.Commands\"\x00\x42\x9d\x01\n:org.apache.skywalking.apm.network.language.agent.v3.compatP\x01Z:skywalking.apache.org/repo/goapi/collect/language/agent/v3\xb8\x01\x01\xaa\x02\x1dSkyWalking.NetworkProtocol.V3b\x06proto3'
  ,
  dependencies=[common_dot_Common__pb2.DESCRIPTOR,language__agent_dot_Tracing__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None

_TRACESEGMENTREPORTSERVICE = _descriptor.ServiceDescriptor(
  name='TraceSegmentReportService',
  full_name='TraceSegmentReportService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=90,
  serialized_end=265,
  methods=[
  _descriptor.MethodDescriptor(
    name='collect',
    full_name='TraceSegmentReportService.collect',
    index=0,
    containing_service=None,
    input_type=language__agent_dot_Tracing__pb2._SEGMENTOBJECT,
    output_type=common_dot_Common__pb2._COMMANDS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='collectInSync',
    full_name='TraceSegmentReportService.collectInSync',
    index=1,
    containing_service=None,
    input_type=language__agent_dot_Tracing__pb2._SEGMENTCOLLECTION,
    output_type=common_dot_Common__pb2._COMMANDS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_TRACESEGMENTREPORTSERVICE)

DESCRIPTOR.services_by_name['TraceSegmentReportService'] = _TRACESEGMENTREPORTSERVICE

# @@protoc_insertion_point(module_scope)
