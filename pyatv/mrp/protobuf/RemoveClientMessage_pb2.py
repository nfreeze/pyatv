# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pyatv/mrp/protobuf/RemoveClientMessage.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyatv.mrp.protobuf import ProtocolMessage_pb2 as pyatv_dot_mrp_dot_protobuf_dot_ProtocolMessage__pb2
from pyatv.mrp.protobuf import NowPlayingClient_pb2 as pyatv_dot_mrp_dot_protobuf_dot_NowPlayingClient__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pyatv/mrp/protobuf/RemoveClientMessage.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=b'\n,pyatv/mrp/protobuf/RemoveClientMessage.proto\x1a(pyatv/mrp/protobuf/ProtocolMessage.proto\x1a)pyatv/mrp/protobuf/NowPlayingClient.proto\"8\n\x13RemoveClientMessage\x12!\n\x06\x63lient\x18\x01 \x01(\x0b\x32\x11.NowPlayingClient:C\n\x13removeClientMessage\x12\x10.ProtocolMessage\x18\x39 \x01(\x0b\x32\x14.RemoveClientMessage'
  ,
  dependencies=[pyatv_dot_mrp_dot_protobuf_dot_ProtocolMessage__pb2.DESCRIPTOR,pyatv_dot_mrp_dot_protobuf_dot_NowPlayingClient__pb2.DESCRIPTOR,])


REMOVECLIENTMESSAGE_FIELD_NUMBER = 57
removeClientMessage = _descriptor.FieldDescriptor(
  name='removeClientMessage', full_name='removeClientMessage', index=0,
  number=57, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)


_REMOVECLIENTMESSAGE = _descriptor.Descriptor(
  name='RemoveClientMessage',
  full_name='RemoveClientMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='client', full_name='RemoveClientMessage.client', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=133,
  serialized_end=189,
)

_REMOVECLIENTMESSAGE.fields_by_name['client'].message_type = pyatv_dot_mrp_dot_protobuf_dot_NowPlayingClient__pb2._NOWPLAYINGCLIENT
DESCRIPTOR.message_types_by_name['RemoveClientMessage'] = _REMOVECLIENTMESSAGE
DESCRIPTOR.extensions_by_name['removeClientMessage'] = removeClientMessage
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RemoveClientMessage = _reflection.GeneratedProtocolMessageType('RemoveClientMessage', (_message.Message,), {
  'DESCRIPTOR' : _REMOVECLIENTMESSAGE,
  '__module__' : 'pyatv.mrp.protobuf.RemoveClientMessage_pb2'
  # @@protoc_insertion_point(class_scope:RemoveClientMessage)
  })
_sym_db.RegisterMessage(RemoveClientMessage)

removeClientMessage.message_type = _REMOVECLIENTMESSAGE
pyatv_dot_mrp_dot_protobuf_dot_ProtocolMessage__pb2.ProtocolMessage.RegisterExtension(removeClientMessage)

# @@protoc_insertion_point(module_scope)
