# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gameshop.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import db_cache_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='gameshop.proto',
  package='GAMESHOP',
  serialized_pb='\n\x0egameshop.proto\x12\x08GAMESHOP\x1a\x0e\x64\x62_cache.proto\"%\n\x11\x43\x32S_Buy_Goods_Req\x12\x10\n\x08goods_id\x18\x01 \x02(\x05\"\x82\x01\n\x11S2C_Buy_Goods_Rsp\x12\x0b\n\x03ret\x18\x01 \x02(\x05\x12\x12\n\ncost_money\x18\x02 \x01(\x05\x12\x13\n\x0b\x63ost_marbel\x18\x03 \x01(\x05\x12\x15\n\rcost_goldcoin\x18\x04 \x01(\x05\x12 \n\tgain_prop\x18\x05 \x03(\x0b\x32\r.DBCACHE.Prop\">\n\x15\x43\x32S_Present_Goods_Req\x12\x10\n\x08goods_id\x18\x01 \x02(\x05\x12\x13\n\x0breceiver_id\x18\x02 \x03(\x05\")\n\x15S2C_Present_Goods_Rsp\x12\x10\n\x08ret_code\x18\x01 \x02(\x05')




_C2S_BUY_GOODS_REQ = _descriptor.Descriptor(
  name='C2S_Buy_Goods_Req',
  full_name='GAMESHOP.C2S_Buy_Goods_Req',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='goods_id', full_name='GAMESHOP.C2S_Buy_Goods_Req.goods_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=44,
  serialized_end=81,
)


_S2C_BUY_GOODS_RSP = _descriptor.Descriptor(
  name='S2C_Buy_Goods_Rsp',
  full_name='GAMESHOP.S2C_Buy_Goods_Rsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret', full_name='GAMESHOP.S2C_Buy_Goods_Rsp.ret', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cost_money', full_name='GAMESHOP.S2C_Buy_Goods_Rsp.cost_money', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cost_marbel', full_name='GAMESHOP.S2C_Buy_Goods_Rsp.cost_marbel', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cost_goldcoin', full_name='GAMESHOP.S2C_Buy_Goods_Rsp.cost_goldcoin', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gain_prop', full_name='GAMESHOP.S2C_Buy_Goods_Rsp.gain_prop', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=84,
  serialized_end=214,
)


_C2S_PRESENT_GOODS_REQ = _descriptor.Descriptor(
  name='C2S_Present_Goods_Req',
  full_name='GAMESHOP.C2S_Present_Goods_Req',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='goods_id', full_name='GAMESHOP.C2S_Present_Goods_Req.goods_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='receiver_id', full_name='GAMESHOP.C2S_Present_Goods_Req.receiver_id', index=1,
      number=2, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=216,
  serialized_end=278,
)


_S2C_PRESENT_GOODS_RSP = _descriptor.Descriptor(
  name='S2C_Present_Goods_Rsp',
  full_name='GAMESHOP.S2C_Present_Goods_Rsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret_code', full_name='GAMESHOP.S2C_Present_Goods_Rsp.ret_code', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=280,
  serialized_end=321,
)

_S2C_BUY_GOODS_RSP.fields_by_name['gain_prop'].message_type = db_cache_pb2._PROP
DESCRIPTOR.message_types_by_name['C2S_Buy_Goods_Req'] = _C2S_BUY_GOODS_REQ
DESCRIPTOR.message_types_by_name['S2C_Buy_Goods_Rsp'] = _S2C_BUY_GOODS_RSP
DESCRIPTOR.message_types_by_name['C2S_Present_Goods_Req'] = _C2S_PRESENT_GOODS_REQ
DESCRIPTOR.message_types_by_name['S2C_Present_Goods_Rsp'] = _S2C_PRESENT_GOODS_RSP

class C2S_Buy_Goods_Req(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _C2S_BUY_GOODS_REQ

  # @@protoc_insertion_point(class_scope:GAMESHOP.C2S_Buy_Goods_Req)

class S2C_Buy_Goods_Rsp(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _S2C_BUY_GOODS_RSP

  # @@protoc_insertion_point(class_scope:GAMESHOP.S2C_Buy_Goods_Rsp)

class C2S_Present_Goods_Req(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _C2S_PRESENT_GOODS_REQ

  # @@protoc_insertion_point(class_scope:GAMESHOP.C2S_Present_Goods_Req)

class S2C_Present_Goods_Rsp(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _S2C_PRESENT_GOODS_RSP

  # @@protoc_insertion_point(class_scope:GAMESHOP.S2C_Present_Goods_Rsp)


# @@protoc_insertion_point(module_scope)