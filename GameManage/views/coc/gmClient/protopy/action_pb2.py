# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: action.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='action.proto',
  package='ACTION',
  serialized_pb='\n\x0c\x61\x63tion.proto\x12\x06\x41\x43TION\"\xb0\x01\n\nbuild_info\x12\n\n\x02id\x18\x01 \x02(\x05\x12\r\n\x05level\x18\x02 \x02(\x05\x12\r\n\x05index\x18\x03 \x02(\x05\x12\t\n\x01x\x18\x04 \x02(\x05\x12\t\n\x01y\x18\x05 \x02(\x05\x12\x0e\n\x06\x66inish\x18\x06 \x02(\x05\x12\x13\n\x0bremain_time\x18\x07 \x01(\x05\x12\x13\n\x0btime_c_type\x18\x08 \x01(\x05\x12\x14\n\x0c\x63ollect_time\x18\t \x01(\x05\x12\x12\n\nbuild_time\x18\n \x01(\x05\"]\n\x04\x61rmy\x12\n\n\x02id\x18\x01 \x02(\x05\x12\r\n\x05\x63ount\x18\x02 \x02(\x05\x12\x10\n\x08\x63ounting\x18\x03 \x02(\x05\x12\x13\n\x0b\x63reate_time\x18\x04 \x02(\x05\x12\x13\n\x0bremain_time\x18\x05 \x02(\x05\"f\n\tarmy_info\x12\r\n\x05index\x18\x01 \x02(\x05\x12\n\n\x02id\x18\x02 \x02(\x05\x12\x11\n\tsum_count\x18\x03 \x02(\x05\x12\x0e\n\x06\x66inish\x18\x04 \x02(\x05\x12\x1b\n\x05\x61rmys\x18\x05 \x03(\x0b\x32\x0c.ACTION.army\"$\n\x07\x61rmy_lv\x12\n\n\x02id\x18\x01 \x02(\x05\x12\r\n\x05level\x18\x02 \x02(\x05\"\x99\x02\n\trole_info\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\r\n\x05level\x18\x02 \x02(\x05\x12\x0b\n\x03\x65xp\x18\x03 \x02(\x05\x12\x0e\n\x06points\x18\x04 \x02(\x05\x12\x0b\n\x03gem\x18\x05 \x02(\x05\x12\x10\n\x08goldcoin\x18\x06 \x02(\x05\x12\x14\n\x0cmax_goldcoin\x18\x07 \x02(\x05\x12\r\n\x05water\x18\x08 \x02(\x05\x12\x11\n\tmax_water\x18\t \x02(\x05\x12\x13\n\x0b\x62uild_count\x18\n \x02(\x05\x12\"\n\x06\x62uilds\x18\x0b \x03(\x0b\x32\x12.ACTION.build_info\x12 \n\x05\x61rmys\x18\x0c \x03(\x0b\x32\x11.ACTION.army_info\x12 \n\x07\x61rmylvs\x18\r \x03(\x0b\x32\x0f.ACTION.army_lv\"\x1f\n\x0f\x63reate_role_req\x12\x0c\n\x04name\x18\x01 \x02(\t\"F\n\x0f\x63reate_role_rsp\x12\x0e\n\x06result\x18\x01 \x02(\x05\x12#\n\x08roleinfo\x18\x02 \x02(\x0b\x32\x11.ACTION.role_info\"D\n\rload_role_rsp\x12\x0e\n\x06result\x18\x01 \x02(\x05\x12#\n\x08roleinfo\x18\x02 \x01(\x0b\x32\x11.ACTION.role_info\"\xc8\x04\n\x0f\x62uildaction_req\x12\x0c\n\x04type\x18\x01 \x02(\x05\x12\x36\n\x07upgrade\x18\x02 \x01(\x0b\x32%.ACTION.buildaction_req.upgrade_build\x12\x32\n\x05place\x18\x03 \x01(\x0b\x32#.ACTION.buildaction_req.place_build\x12\x39\n\x07\x63ollect\x18\x04 \x01(\x0b\x32(.ACTION.buildaction_req.collect_resource\x12\x30\n\x04move\x18\x05 \x01(\x0b\x32\".ACTION.buildaction_req.move_build\x12\x36\n\x07produce\x18\x06 \x01(\x0b\x32%.ACTION.buildaction_req.produce_armys\x1a*\n\rupgrade_build\x12\n\n\x02id\x18\x01 \x02(\x05\x12\r\n\x05index\x18\x02 \x02(\x05\x1a/\n\x0bplace_build\x12\n\n\x02id\x18\x01 \x02(\x05\x12\t\n\x01x\x18\x02 \x02(\x05\x12\t\n\x01y\x18\x03 \x02(\x05\x1a-\n\x10\x63ollect_resource\x12\n\n\x02id\x18\x01 \x02(\x05\x12\r\n\x05index\x18\x02 \x02(\x05\x1a=\n\nmove_build\x12\n\n\x02id\x18\x01 \x02(\x05\x12\r\n\x05index\x18\x02 \x02(\x05\x12\t\n\x01x\x18\x03 \x02(\x05\x12\t\n\x01y\x18\x04 \x02(\x05\x1aK\n\rproduce_armys\x12\n\n\x02id\x18\x01 \x02(\x05\x12\r\n\x05\x63ount\x18\x02 \x02(\x05\x12\x10\n\x08\x62uild_id\x18\x03 \x02(\x05\x12\r\n\x05index\x18\x04 \x02(\x05\"?\n\x0f\x62uildaction_rsp\x12\x0e\n\x06result\x18\x01 \x02(\x05\x12\r\n\x05index\x18\x02 \x01(\x05\x12\r\n\x05value\x18\x03 \x01(\x05\"+\n\x0f\x65nteraction_req\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x0c\n\x04type\x18\x02 \x02(\x05\"B\n\x0f\x65nteraction_rsp\x12\x0b\n\x03ret\x18\x01 \x02(\x05\x12\"\n\x06\x62uilds\x18\x02 \x03(\x0b\x32\x12.ACTION.build_info\"\x1e\n\x10\x61ttackaction_req\x12\n\n\x02id\x18\x01 \x02(\x05')




_BUILD_INFO = _descriptor.Descriptor(
  name='build_info',
  full_name='ACTION.build_info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ACTION.build_info.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='level', full_name='ACTION.build_info.level', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='index', full_name='ACTION.build_info.index', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='x', full_name='ACTION.build_info.x', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='y', full_name='ACTION.build_info.y', index=4,
      number=5, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='finish', full_name='ACTION.build_info.finish', index=5,
      number=6, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='remain_time', full_name='ACTION.build_info.remain_time', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='time_c_type', full_name='ACTION.build_info.time_c_type', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='collect_time', full_name='ACTION.build_info.collect_time', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='build_time', full_name='ACTION.build_info.build_time', index=9,
      number=10, type=5, cpp_type=1, label=1,
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
  serialized_start=25,
  serialized_end=201,
)


_ARMY = _descriptor.Descriptor(
  name='army',
  full_name='ACTION.army',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ACTION.army.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='count', full_name='ACTION.army.count', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='counting', full_name='ACTION.army.counting', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='create_time', full_name='ACTION.army.create_time', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='remain_time', full_name='ACTION.army.remain_time', index=4,
      number=5, type=5, cpp_type=1, label=2,
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
  serialized_start=203,
  serialized_end=296,
)


_ARMY_INFO = _descriptor.Descriptor(
  name='army_info',
  full_name='ACTION.army_info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='index', full_name='ACTION.army_info.index', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='ACTION.army_info.id', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sum_count', full_name='ACTION.army_info.sum_count', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='finish', full_name='ACTION.army_info.finish', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='armys', full_name='ACTION.army_info.armys', index=4,
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
  serialized_start=298,
  serialized_end=400,
)


_ARMY_LV = _descriptor.Descriptor(
  name='army_lv',
  full_name='ACTION.army_lv',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ACTION.army_lv.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='level', full_name='ACTION.army_lv.level', index=1,
      number=2, type=5, cpp_type=1, label=2,
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
  serialized_start=402,
  serialized_end=438,
)


_ROLE_INFO = _descriptor.Descriptor(
  name='role_info',
  full_name='ACTION.role_info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='ACTION.role_info.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='level', full_name='ACTION.role_info.level', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='exp', full_name='ACTION.role_info.exp', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='points', full_name='ACTION.role_info.points', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gem', full_name='ACTION.role_info.gem', index=4,
      number=5, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='goldcoin', full_name='ACTION.role_info.goldcoin', index=5,
      number=6, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_goldcoin', full_name='ACTION.role_info.max_goldcoin', index=6,
      number=7, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='water', full_name='ACTION.role_info.water', index=7,
      number=8, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_water', full_name='ACTION.role_info.max_water', index=8,
      number=9, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='build_count', full_name='ACTION.role_info.build_count', index=9,
      number=10, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='builds', full_name='ACTION.role_info.builds', index=10,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='armys', full_name='ACTION.role_info.armys', index=11,
      number=12, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='armylvs', full_name='ACTION.role_info.armylvs', index=12,
      number=13, type=11, cpp_type=10, label=3,
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
  serialized_start=441,
  serialized_end=722,
)


_CREATE_ROLE_REQ = _descriptor.Descriptor(
  name='create_role_req',
  full_name='ACTION.create_role_req',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='ACTION.create_role_req.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  serialized_start=724,
  serialized_end=755,
)


_CREATE_ROLE_RSP = _descriptor.Descriptor(
  name='create_role_rsp',
  full_name='ACTION.create_role_rsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='ACTION.create_role_rsp.result', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='roleinfo', full_name='ACTION.create_role_rsp.roleinfo', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
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
  serialized_start=757,
  serialized_end=827,
)


_LOAD_ROLE_RSP = _descriptor.Descriptor(
  name='load_role_rsp',
  full_name='ACTION.load_role_rsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='ACTION.load_role_rsp.result', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='roleinfo', full_name='ACTION.load_role_rsp.roleinfo', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=829,
  serialized_end=897,
)


_BUILDACTION_REQ_UPGRADE_BUILD = _descriptor.Descriptor(
  name='upgrade_build',
  full_name='ACTION.buildaction_req.upgrade_build',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ACTION.buildaction_req.upgrade_build.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='index', full_name='ACTION.buildaction_req.upgrade_build.index', index=1,
      number=2, type=5, cpp_type=1, label=2,
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
  serialized_start=1206,
  serialized_end=1248,
)

_BUILDACTION_REQ_PLACE_BUILD = _descriptor.Descriptor(
  name='place_build',
  full_name='ACTION.buildaction_req.place_build',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ACTION.buildaction_req.place_build.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='x', full_name='ACTION.buildaction_req.place_build.x', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='y', full_name='ACTION.buildaction_req.place_build.y', index=2,
      number=3, type=5, cpp_type=1, label=2,
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
  serialized_start=1250,
  serialized_end=1297,
)

_BUILDACTION_REQ_COLLECT_RESOURCE = _descriptor.Descriptor(
  name='collect_resource',
  full_name='ACTION.buildaction_req.collect_resource',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ACTION.buildaction_req.collect_resource.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='index', full_name='ACTION.buildaction_req.collect_resource.index', index=1,
      number=2, type=5, cpp_type=1, label=2,
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
  serialized_start=1299,
  serialized_end=1344,
)

_BUILDACTION_REQ_MOVE_BUILD = _descriptor.Descriptor(
  name='move_build',
  full_name='ACTION.buildaction_req.move_build',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ACTION.buildaction_req.move_build.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='index', full_name='ACTION.buildaction_req.move_build.index', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='x', full_name='ACTION.buildaction_req.move_build.x', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='y', full_name='ACTION.buildaction_req.move_build.y', index=3,
      number=4, type=5, cpp_type=1, label=2,
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
  serialized_start=1346,
  serialized_end=1407,
)

_BUILDACTION_REQ_PRODUCE_ARMYS = _descriptor.Descriptor(
  name='produce_armys',
  full_name='ACTION.buildaction_req.produce_armys',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ACTION.buildaction_req.produce_armys.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='count', full_name='ACTION.buildaction_req.produce_armys.count', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='build_id', full_name='ACTION.buildaction_req.produce_armys.build_id', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='index', full_name='ACTION.buildaction_req.produce_armys.index', index=3,
      number=4, type=5, cpp_type=1, label=2,
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
  serialized_start=1409,
  serialized_end=1484,
)

_BUILDACTION_REQ = _descriptor.Descriptor(
  name='buildaction_req',
  full_name='ACTION.buildaction_req',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='ACTION.buildaction_req.type', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='upgrade', full_name='ACTION.buildaction_req.upgrade', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='place', full_name='ACTION.buildaction_req.place', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='collect', full_name='ACTION.buildaction_req.collect', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='move', full_name='ACTION.buildaction_req.move', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='produce', full_name='ACTION.buildaction_req.produce', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_BUILDACTION_REQ_UPGRADE_BUILD, _BUILDACTION_REQ_PLACE_BUILD, _BUILDACTION_REQ_COLLECT_RESOURCE, _BUILDACTION_REQ_MOVE_BUILD, _BUILDACTION_REQ_PRODUCE_ARMYS, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=900,
  serialized_end=1484,
)


_BUILDACTION_RSP = _descriptor.Descriptor(
  name='buildaction_rsp',
  full_name='ACTION.buildaction_rsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='ACTION.buildaction_rsp.result', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='index', full_name='ACTION.buildaction_rsp.index', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='ACTION.buildaction_rsp.value', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=1486,
  serialized_end=1549,
)


_ENTERACTION_REQ = _descriptor.Descriptor(
  name='enteraction_req',
  full_name='ACTION.enteraction_req',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ACTION.enteraction_req.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='ACTION.enteraction_req.type', index=1,
      number=2, type=5, cpp_type=1, label=2,
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
  serialized_start=1551,
  serialized_end=1594,
)


_ENTERACTION_RSP = _descriptor.Descriptor(
  name='enteraction_rsp',
  full_name='ACTION.enteraction_rsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret', full_name='ACTION.enteraction_rsp.ret', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='builds', full_name='ACTION.enteraction_rsp.builds', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=1596,
  serialized_end=1662,
)


_ATTACKACTION_REQ = _descriptor.Descriptor(
  name='attackaction_req',
  full_name='ACTION.attackaction_req',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ACTION.attackaction_req.id', index=0,
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
  serialized_start=1664,
  serialized_end=1694,
)

_ARMY_INFO.fields_by_name['armys'].message_type = _ARMY
_ROLE_INFO.fields_by_name['builds'].message_type = _BUILD_INFO
_ROLE_INFO.fields_by_name['armys'].message_type = _ARMY_INFO
_ROLE_INFO.fields_by_name['armylvs'].message_type = _ARMY_LV
_CREATE_ROLE_RSP.fields_by_name['roleinfo'].message_type = _ROLE_INFO
_LOAD_ROLE_RSP.fields_by_name['roleinfo'].message_type = _ROLE_INFO
_BUILDACTION_REQ_UPGRADE_BUILD.containing_type = _BUILDACTION_REQ;
_BUILDACTION_REQ_PLACE_BUILD.containing_type = _BUILDACTION_REQ;
_BUILDACTION_REQ_COLLECT_RESOURCE.containing_type = _BUILDACTION_REQ;
_BUILDACTION_REQ_MOVE_BUILD.containing_type = _BUILDACTION_REQ;
_BUILDACTION_REQ_PRODUCE_ARMYS.containing_type = _BUILDACTION_REQ;
_BUILDACTION_REQ.fields_by_name['upgrade'].message_type = _BUILDACTION_REQ_UPGRADE_BUILD
_BUILDACTION_REQ.fields_by_name['place'].message_type = _BUILDACTION_REQ_PLACE_BUILD
_BUILDACTION_REQ.fields_by_name['collect'].message_type = _BUILDACTION_REQ_COLLECT_RESOURCE
_BUILDACTION_REQ.fields_by_name['move'].message_type = _BUILDACTION_REQ_MOVE_BUILD
_BUILDACTION_REQ.fields_by_name['produce'].message_type = _BUILDACTION_REQ_PRODUCE_ARMYS
_ENTERACTION_RSP.fields_by_name['builds'].message_type = _BUILD_INFO
DESCRIPTOR.message_types_by_name['build_info'] = _BUILD_INFO
DESCRIPTOR.message_types_by_name['army'] = _ARMY
DESCRIPTOR.message_types_by_name['army_info'] = _ARMY_INFO
DESCRIPTOR.message_types_by_name['army_lv'] = _ARMY_LV
DESCRIPTOR.message_types_by_name['role_info'] = _ROLE_INFO
DESCRIPTOR.message_types_by_name['create_role_req'] = _CREATE_ROLE_REQ
DESCRIPTOR.message_types_by_name['create_role_rsp'] = _CREATE_ROLE_RSP
DESCRIPTOR.message_types_by_name['load_role_rsp'] = _LOAD_ROLE_RSP
DESCRIPTOR.message_types_by_name['buildaction_req'] = _BUILDACTION_REQ
DESCRIPTOR.message_types_by_name['buildaction_rsp'] = _BUILDACTION_RSP
DESCRIPTOR.message_types_by_name['enteraction_req'] = _ENTERACTION_REQ
DESCRIPTOR.message_types_by_name['enteraction_rsp'] = _ENTERACTION_RSP
DESCRIPTOR.message_types_by_name['attackaction_req'] = _ATTACKACTION_REQ

class build_info(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _BUILD_INFO

  # @@protoc_insertion_point(class_scope:ACTION.build_info)

class army(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ARMY

  # @@protoc_insertion_point(class_scope:ACTION.army)

class army_info(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ARMY_INFO

  # @@protoc_insertion_point(class_scope:ACTION.army_info)

class army_lv(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ARMY_LV

  # @@protoc_insertion_point(class_scope:ACTION.army_lv)

class role_info(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ROLE_INFO

  # @@protoc_insertion_point(class_scope:ACTION.role_info)

class create_role_req(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CREATE_ROLE_REQ

  # @@protoc_insertion_point(class_scope:ACTION.create_role_req)

class create_role_rsp(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CREATE_ROLE_RSP

  # @@protoc_insertion_point(class_scope:ACTION.create_role_rsp)

class load_role_rsp(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _LOAD_ROLE_RSP

  # @@protoc_insertion_point(class_scope:ACTION.load_role_rsp)

class buildaction_req(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType

  class upgrade_build(_message.Message):
    __metaclass__ = _reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _BUILDACTION_REQ_UPGRADE_BUILD

    # @@protoc_insertion_point(class_scope:ACTION.buildaction_req.upgrade_build)

  class place_build(_message.Message):
    __metaclass__ = _reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _BUILDACTION_REQ_PLACE_BUILD

    # @@protoc_insertion_point(class_scope:ACTION.buildaction_req.place_build)

  class collect_resource(_message.Message):
    __metaclass__ = _reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _BUILDACTION_REQ_COLLECT_RESOURCE

    # @@protoc_insertion_point(class_scope:ACTION.buildaction_req.collect_resource)

  class move_build(_message.Message):
    __metaclass__ = _reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _BUILDACTION_REQ_MOVE_BUILD

    # @@protoc_insertion_point(class_scope:ACTION.buildaction_req.move_build)

  class produce_armys(_message.Message):
    __metaclass__ = _reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _BUILDACTION_REQ_PRODUCE_ARMYS

    # @@protoc_insertion_point(class_scope:ACTION.buildaction_req.produce_armys)
  DESCRIPTOR = _BUILDACTION_REQ

  # @@protoc_insertion_point(class_scope:ACTION.buildaction_req)

class buildaction_rsp(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _BUILDACTION_RSP

  # @@protoc_insertion_point(class_scope:ACTION.buildaction_rsp)

class enteraction_req(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ENTERACTION_REQ

  # @@protoc_insertion_point(class_scope:ACTION.enteraction_req)

class enteraction_rsp(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ENTERACTION_RSP

  # @@protoc_insertion_point(class_scope:ACTION.enteraction_rsp)

class attackaction_req(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ATTACKACTION_REQ

  # @@protoc_insertion_point(class_scope:ACTION.attackaction_req)


# @@protoc_insertion_point(module_scope)
