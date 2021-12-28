# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: profile/ProfileCompat.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ..common import Common_pb2 as common_dot_Common__pb2
from ..profile import Profile_pb2 as profile_dot_Profile__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='profile/ProfileCompat.proto',
  package='',
  syntax='proto3',
  serialized_options=b'\n<org.apache.apm.apm.network.language.profile.v3.compatP\001Z<apm.apache.org/repo/goapi/collect/language/profile/v3\270\001\001\252\002\035SkyWalking.NetworkProtocol.V3',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1bprofile/ProfileCompat.proto\x1a\x13\x63ommon/Common.proto\x1a\x15profile/Profile.proto2\x90\x02\n\x0bProfileTask\x12[\n\x16getProfileTaskCommands\x12&.apm.v3.ProfileTaskCommandQuery\x1a\x17.apm.v3.Commands\"\x00\x12M\n\x0f\x63ollectSnapshot\x12\x1d.apm.v3.ThreadSnapshot\x1a\x17.apm.v3.Commands\"\x00(\x01\x12U\n\x10reportTaskFinish\x12&.apm.v3.ProfileTaskFinishReport\x1a\x17.apm.v3.Commands\"\x00\x42\xa1\x01\n<org.apache.apm.apm.network.language.profile.v3.compatP\x01Z<apm.apache.org/repo/goapi/collect/language/profile/v3\xb8\x01\x01\xaa\x02\x1dSkyWalking.NetworkProtocol.V3b\x06proto3'
  ,
  dependencies=[common_dot_Common__pb2.DESCRIPTOR,profile_dot_Profile__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None

_PROFILETASK = _descriptor.ServiceDescriptor(
  name='ProfileTask',
  full_name='ProfileTask',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=76,
  serialized_end=348,
  methods=[
  _descriptor.MethodDescriptor(
    name='getProfileTaskCommands',
    full_name='ProfileTask.getProfileTaskCommands',
    index=0,
    containing_service=None,
    input_type=profile_dot_Profile__pb2._PROFILETASKCOMMANDQUERY,
    output_type=common_dot_Common__pb2._COMMANDS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='collectSnapshot',
    full_name='ProfileTask.collectSnapshot',
    index=1,
    containing_service=None,
    input_type=profile_dot_Profile__pb2._THREADSNAPSHOT,
    output_type=common_dot_Common__pb2._COMMANDS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='reportTaskFinish',
    full_name='ProfileTask.reportTaskFinish',
    index=2,
    containing_service=None,
    input_type=profile_dot_Profile__pb2._PROFILETASKFINISHREPORT,
    output_type=common_dot_Common__pb2._COMMANDS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_PROFILETASK)

DESCRIPTOR.services_by_name['ProfileTask'] = _PROFILETASK

# @@protoc_insertion_point(module_scope)