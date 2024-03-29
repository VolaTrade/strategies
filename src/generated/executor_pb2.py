# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: src/proto/executor.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='src/proto/executor.proto',
  package='executor',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x18src/proto/executor.proto\x12\x08\x65xecutor\"\xaa\x01\n\x0e\x45xecuteRequest\x12>\n\x0bstratParams\x18\x01 \x03(\x0b\x32).executor.ExecuteRequest.StratParamsEntry\x12\x11\n\tbuyUpdate\x18\x02 \x01(\x08\x12\x11\n\tsessionID\x18\x03 \x01(\t\x1a\x32\n\x10StratParamsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x01:\x02\x38\x01\"<\n\x0c\x45xecuteReply\x12\r\n\x05value\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x0c\n\x04\x63ode\x18\x03 \x01(\r2W\n\x08\x45xecutor\x12K\n\x15\x45xecuteStrategyUpdate\x12\x18.executor.ExecuteRequest\x1a\x16.executor.ExecuteReply\"\x00\x62\x06proto3'
)




_EXECUTEREQUEST_STRATPARAMSENTRY = _descriptor.Descriptor(
  name='StratParamsEntry',
  full_name='executor.ExecuteRequest.StratParamsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='executor.ExecuteRequest.StratParamsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='executor.ExecuteRequest.StratParamsEntry.value', index=1,
      number=2, type=1, cpp_type=5, label=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=159,
  serialized_end=209,
)

_EXECUTEREQUEST = _descriptor.Descriptor(
  name='ExecuteRequest',
  full_name='executor.ExecuteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='stratParams', full_name='executor.ExecuteRequest.stratParams', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='buyUpdate', full_name='executor.ExecuteRequest.buyUpdate', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sessionID', full_name='executor.ExecuteRequest.sessionID', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_EXECUTEREQUEST_STRATPARAMSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=39,
  serialized_end=209,
)


_EXECUTEREPLY = _descriptor.Descriptor(
  name='ExecuteReply',
  full_name='executor.ExecuteReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='executor.ExecuteReply.value', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='executor.ExecuteReply.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='code', full_name='executor.ExecuteReply.code', index=2,
      number=3, type=13, cpp_type=3, label=1,
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
  serialized_start=211,
  serialized_end=271,
)

_EXECUTEREQUEST_STRATPARAMSENTRY.containing_type = _EXECUTEREQUEST
_EXECUTEREQUEST.fields_by_name['stratParams'].message_type = _EXECUTEREQUEST_STRATPARAMSENTRY
DESCRIPTOR.message_types_by_name['ExecuteRequest'] = _EXECUTEREQUEST
DESCRIPTOR.message_types_by_name['ExecuteReply'] = _EXECUTEREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ExecuteRequest = _reflection.GeneratedProtocolMessageType('ExecuteRequest', (_message.Message,), {

  'StratParamsEntry' : _reflection.GeneratedProtocolMessageType('StratParamsEntry', (_message.Message,), {
    'DESCRIPTOR' : _EXECUTEREQUEST_STRATPARAMSENTRY,
    '__module__' : 'src.proto.executor_pb2'
    # @@protoc_insertion_point(class_scope:executor.ExecuteRequest.StratParamsEntry)
    })
  ,
  'DESCRIPTOR' : _EXECUTEREQUEST,
  '__module__' : 'src.proto.executor_pb2'
  # @@protoc_insertion_point(class_scope:executor.ExecuteRequest)
  })
_sym_db.RegisterMessage(ExecuteRequest)
_sym_db.RegisterMessage(ExecuteRequest.StratParamsEntry)

ExecuteReply = _reflection.GeneratedProtocolMessageType('ExecuteReply', (_message.Message,), {
  'DESCRIPTOR' : _EXECUTEREPLY,
  '__module__' : 'src.proto.executor_pb2'
  # @@protoc_insertion_point(class_scope:executor.ExecuteReply)
  })
_sym_db.RegisterMessage(ExecuteReply)


_EXECUTEREQUEST_STRATPARAMSENTRY._options = None

_EXECUTOR = _descriptor.ServiceDescriptor(
  name='Executor',
  full_name='executor.Executor',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=273,
  serialized_end=360,
  methods=[
  _descriptor.MethodDescriptor(
    name='ExecuteStrategyUpdate',
    full_name='executor.Executor.ExecuteStrategyUpdate',
    index=0,
    containing_service=None,
    input_type=_EXECUTEREQUEST,
    output_type=_EXECUTEREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_EXECUTOR)

DESCRIPTOR.services_by_name['Executor'] = _EXECUTOR

# @@protoc_insertion_point(module_scope)
