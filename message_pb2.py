# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: message.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rmessage.proto\x12\x07message\"\x1e\n\x0eMessageRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"#\n\x0fMessageResponse\x12\x10\n\x08greeting\x18\x01 \x01(\t2L\n\x0eMessageService\x12:\n\x05Greet\x12\x17.message.MessageRequest\x1a\x18.message.MessageResponseb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'message_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _MESSAGEREQUEST._serialized_start=26
  _MESSAGEREQUEST._serialized_end=56
  _MESSAGERESPONSE._serialized_start=58
  _MESSAGERESPONSE._serialized_end=93
  _MESSAGESERVICE._serialized_start=95
  _MESSAGESERVICE._serialized_end=171
# @@protoc_insertion_point(module_scope)
