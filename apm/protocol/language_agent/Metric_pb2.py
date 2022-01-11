# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: language-agent/Metric.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ..common import Common_pb2 as common_dot_Common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='language-agent/Metric.proto',
  package='skywalking.v3',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1blanguage-agent/Metric.proto\x12\rskywalking.v3\x1a\x13\x63ommon/Common.proto\"d\n\x10MetricCollection\x12&\n\x07metrics\x18\x01 \x01(\x0b\x32\x15.skywalking.v3.Metric\x12\x0f\n\x07service\x18\x02 \x01(\t\x12\x17\n\x0fserviceInstance\x18\x03 \x01(\t\"\xbe\x01\n\x06Metric\x12\x0c\n\x04time\x18\x01 \x01(\x03\x12\x14\n\x0c\x63reated_time\x18\x02 \x01(\x03\x12\x1f\n\x03\x63pu\x18\x03 \x01(\x0b\x32\x12.skywalking.v3.CPU\x12\'\n\x06memory\x18\x04 \x01(\x0b\x32\x17.skywalking.v3.PyMemory\x12\'\n\x06thread\x18\x05 \x01(\x0b\x32\x17.skywalking.v3.PyThread\x12\x1d\n\x02io\x18\x06 \x01(\x0b\x32\x11.skywalking.v3.IO\" \n\x08PyMemory\x12\x14\n\x0cusagePercent\x18\x01 \x01(\x01\"2\n\x08PyThread\x12\x11\n\tliveCount\x18\x01 \x01(\x03\x12\x13\n\x0b\x64\x61\x65monCount\x18\x02 \x01(\x03\"R\n\x02IO\x12\x11\n\treadCount\x18\x01 \x01(\x03\x12\x12\n\nwriteCount\x18\x02 \x01(\x03\x12\x11\n\treadBytes\x18\x03 \x01(\x03\x12\x12\n\nwriteBytes\x18\x04 \x01(\x03\x32\\\n\x13MetricReportService\x12\x45\n\x07\x63ollect\x12\x1f.skywalking.v3.MetricCollection\x1a\x17.skywalking.v3.Commands\"\x00\x62\x06proto3'
  ,
  dependencies=[common_dot_Common__pb2.DESCRIPTOR,])




_METRICCOLLECTION = _descriptor.Descriptor(
  name='MetricCollection',
  full_name='skywalking.v3.MetricCollection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='metrics', full_name='skywalking.v3.MetricCollection.metrics', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='service', full_name='skywalking.v3.MetricCollection.service', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='serviceInstance', full_name='skywalking.v3.MetricCollection.serviceInstance', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=67,
  serialized_end=167,
)


_METRIC = _descriptor.Descriptor(
  name='Metric',
  full_name='skywalking.v3.Metric',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='time', full_name='skywalking.v3.Metric.time', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created_time', full_name='skywalking.v3.Metric.created_time', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cpu', full_name='skywalking.v3.Metric.cpu', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='memory', full_name='skywalking.v3.Metric.memory', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='thread', full_name='skywalking.v3.Metric.thread', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='io', full_name='skywalking.v3.Metric.io', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=170,
  serialized_end=360,
)


_PYMEMORY = _descriptor.Descriptor(
  name='PyMemory',
  full_name='skywalking.v3.PyMemory',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='usagePercent', full_name='skywalking.v3.PyMemory.usagePercent', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=362,
  serialized_end=394,
)


_PYTHREAD = _descriptor.Descriptor(
  name='PyThread',
  full_name='skywalking.v3.PyThread',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='liveCount', full_name='skywalking.v3.PyThread.liveCount', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='daemonCount', full_name='skywalking.v3.PyThread.daemonCount', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=396,
  serialized_end=446,
)


_IO = _descriptor.Descriptor(
  name='IO',
  full_name='skywalking.v3.IO',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='readCount', full_name='skywalking.v3.IO.readCount', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='writeCount', full_name='skywalking.v3.IO.writeCount', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='readBytes', full_name='skywalking.v3.IO.readBytes', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='writeBytes', full_name='skywalking.v3.IO.writeBytes', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=448,
  serialized_end=530,
)

_METRICCOLLECTION.fields_by_name['metrics'].message_type = _METRIC
_METRIC.fields_by_name['cpu'].message_type = common_dot_Common__pb2._CPU
_METRIC.fields_by_name['memory'].message_type = _PYMEMORY
_METRIC.fields_by_name['thread'].message_type = _PYTHREAD
_METRIC.fields_by_name['io'].message_type = _IO
DESCRIPTOR.message_types_by_name['MetricCollection'] = _METRICCOLLECTION
DESCRIPTOR.message_types_by_name['Metric'] = _METRIC
DESCRIPTOR.message_types_by_name['PyMemory'] = _PYMEMORY
DESCRIPTOR.message_types_by_name['PyThread'] = _PYTHREAD
DESCRIPTOR.message_types_by_name['IO'] = _IO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MetricCollection = _reflection.GeneratedProtocolMessageType('MetricCollection', (_message.Message,), {
  'DESCRIPTOR' : _METRICCOLLECTION,
  '__module__' : 'language_agent.Metric_pb2'
  # @@protoc_insertion_point(class_scope:skywalking.v3.MetricCollection)
  })
_sym_db.RegisterMessage(MetricCollection)

Metric = _reflection.GeneratedProtocolMessageType('Metric', (_message.Message,), {
  'DESCRIPTOR' : _METRIC,
  '__module__' : 'language_agent.Metric_pb2'
  # @@protoc_insertion_point(class_scope:skywalking.v3.Metric)
  })
_sym_db.RegisterMessage(Metric)

PyMemory = _reflection.GeneratedProtocolMessageType('PyMemory', (_message.Message,), {
  'DESCRIPTOR' : _PYMEMORY,
  '__module__' : 'language_agent.Metric_pb2'
  # @@protoc_insertion_point(class_scope:skywalking.v3.PyMemory)
  })
_sym_db.RegisterMessage(PyMemory)

PyThread = _reflection.GeneratedProtocolMessageType('PyThread', (_message.Message,), {
  'DESCRIPTOR' : _PYTHREAD,
  '__module__' : 'language_agent.Metric_pb2'
  # @@protoc_insertion_point(class_scope:skywalking.v3.PyThread)
  })
_sym_db.RegisterMessage(PyThread)

IO = _reflection.GeneratedProtocolMessageType('IO', (_message.Message,), {
  'DESCRIPTOR' : _IO,
  '__module__' : 'language_agent.Metric_pb2'
  # @@protoc_insertion_point(class_scope:skywalking.v3.IO)
  })
_sym_db.RegisterMessage(IO)



_METRICREPORTSERVICE = _descriptor.ServiceDescriptor(
  name='MetricReportService',
  full_name='skywalking.v3.MetricReportService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=532,
  serialized_end=624,
  methods=[
  _descriptor.MethodDescriptor(
    name='collect',
    full_name='skywalking.v3.MetricReportService.collect',
    index=0,
    containing_service=None,
    input_type=_METRICCOLLECTION,
    output_type=common_dot_Common__pb2._COMMANDS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_METRICREPORTSERVICE)

DESCRIPTOR.services_by_name['MetricReportService'] = _METRICREPORTSERVICE

# @@protoc_insertion_point(module_scope)
