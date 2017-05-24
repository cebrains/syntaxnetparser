# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: syntaxnet/task_spec.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='syntaxnet/task_spec.proto',
  package='syntaxnet',
  syntax='proto2',
  serialized_pb=_b('\n\x19syntaxnet/task_spec.proto\x12\tsyntaxnet\"\xe4\x01\n\tTaskInput\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x0f\n\x07\x63reator\x18\x02 \x01(\t\x12\x13\n\x0b\x66ile_format\x18\x03 \x03(\t\x12\x15\n\rrecord_format\x18\x04 \x03(\t\x12\x19\n\nmulti_file\x18\x05 \x01(\x08:\x05\x66\x61lse\x12\'\n\x04part\x18\x06 \x03(\n2\x19.syntaxnet.TaskInput.Part\x1aH\n\x04Part\x12\x14\n\x0c\x66ile_pattern\x18\x07 \x01(\t\x12\x13\n\x0b\x66ile_format\x18\x08 \x01(\t\x12\x15\n\rrecord_format\x18\t \x01(\t\"\x84\x01\n\nTaskOutput\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x13\n\x0b\x66ile_format\x18\x02 \x01(\t\x12\x15\n\rrecord_format\x18\x03 \x01(\t\x12\x11\n\x06shards\x18\x04 \x01(\x05:\x01\x30\x12\x11\n\tfile_base\x18\x05 \x01(\t\x12\x16\n\x0e\x66ile_extension\x18\x06 \x01(\t\"\xd8\x01\n\x08TaskSpec\x12\x11\n\ttask_name\x18\x01 \x01(\t\x12\x11\n\ttask_type\x18\x02 \x01(\t\x12\x30\n\tparameter\x18\x03 \x03(\n2\x1d.syntaxnet.TaskSpec.Parameter\x12#\n\x05input\x18\x06 \x03(\x0b\x32\x14.syntaxnet.TaskInput\x12%\n\x06output\x18\x07 \x03(\x0b\x32\x15.syntaxnet.TaskOutput\x1a(\n\tParameter\x12\x0c\n\x04name\x18\x04 \x02(\t\x12\r\n\x05value\x18\x05 \x01(\t')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_TASKINPUT_PART = _descriptor.Descriptor(
  name='Part',
  full_name='syntaxnet.TaskInput.Part',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='file_pattern', full_name='syntaxnet.TaskInput.Part.file_pattern', index=0,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='file_format', full_name='syntaxnet.TaskInput.Part.file_format', index=1,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='record_format', full_name='syntaxnet.TaskInput.Part.record_format', index=2,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=197,
  serialized_end=269,
)

_TASKINPUT = _descriptor.Descriptor(
  name='TaskInput',
  full_name='syntaxnet.TaskInput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='syntaxnet.TaskInput.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='creator', full_name='syntaxnet.TaskInput.creator', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='file_format', full_name='syntaxnet.TaskInput.file_format', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='record_format', full_name='syntaxnet.TaskInput.record_format', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='multi_file', full_name='syntaxnet.TaskInput.multi_file', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='part', full_name='syntaxnet.TaskInput.part', index=5,
      number=6, type=10, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_TASKINPUT_PART, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=41,
  serialized_end=269,
)


_TASKOUTPUT = _descriptor.Descriptor(
  name='TaskOutput',
  full_name='syntaxnet.TaskOutput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='syntaxnet.TaskOutput.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='file_format', full_name='syntaxnet.TaskOutput.file_format', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='record_format', full_name='syntaxnet.TaskOutput.record_format', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='shards', full_name='syntaxnet.TaskOutput.shards', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='file_base', full_name='syntaxnet.TaskOutput.file_base', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='file_extension', full_name='syntaxnet.TaskOutput.file_extension', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=272,
  serialized_end=404,
)


_TASKSPEC_PARAMETER = _descriptor.Descriptor(
  name='Parameter',
  full_name='syntaxnet.TaskSpec.Parameter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='syntaxnet.TaskSpec.Parameter.name', index=0,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='syntaxnet.TaskSpec.Parameter.value', index=1,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=583,
  serialized_end=623,
)

_TASKSPEC = _descriptor.Descriptor(
  name='TaskSpec',
  full_name='syntaxnet.TaskSpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='task_name', full_name='syntaxnet.TaskSpec.task_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='task_type', full_name='syntaxnet.TaskSpec.task_type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parameter', full_name='syntaxnet.TaskSpec.parameter', index=2,
      number=3, type=10, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='input', full_name='syntaxnet.TaskSpec.input', index=3,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='output', full_name='syntaxnet.TaskSpec.output', index=4,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_TASKSPEC_PARAMETER, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=407,
  serialized_end=623,
)

_TASKINPUT_PART.containing_type = _TASKINPUT
_TASKINPUT.fields_by_name['part'].message_type = _TASKINPUT_PART
_TASKSPEC_PARAMETER.containing_type = _TASKSPEC
_TASKSPEC.fields_by_name['parameter'].message_type = _TASKSPEC_PARAMETER
_TASKSPEC.fields_by_name['input'].message_type = _TASKINPUT
_TASKSPEC.fields_by_name['output'].message_type = _TASKOUTPUT
DESCRIPTOR.message_types_by_name['TaskInput'] = _TASKINPUT
DESCRIPTOR.message_types_by_name['TaskOutput'] = _TASKOUTPUT
DESCRIPTOR.message_types_by_name['TaskSpec'] = _TASKSPEC

TaskInput = _reflection.GeneratedProtocolMessageType('TaskInput', (_message.Message,), dict(

  Part = _reflection.GeneratedProtocolMessageType('Part', (_message.Message,), dict(
    DESCRIPTOR = _TASKINPUT_PART,
    __module__ = 'syntaxnet.task_spec_pb2'
    # @@protoc_insertion_point(class_scope:syntaxnet.TaskInput.Part)
    ))
  ,
  DESCRIPTOR = _TASKINPUT,
  __module__ = 'syntaxnet.task_spec_pb2'
  # @@protoc_insertion_point(class_scope:syntaxnet.TaskInput)
  ))
_sym_db.RegisterMessage(TaskInput)
_sym_db.RegisterMessage(TaskInput.Part)

TaskOutput = _reflection.GeneratedProtocolMessageType('TaskOutput', (_message.Message,), dict(
  DESCRIPTOR = _TASKOUTPUT,
  __module__ = 'syntaxnet.task_spec_pb2'
  # @@protoc_insertion_point(class_scope:syntaxnet.TaskOutput)
  ))
_sym_db.RegisterMessage(TaskOutput)

TaskSpec = _reflection.GeneratedProtocolMessageType('TaskSpec', (_message.Message,), dict(

  Parameter = _reflection.GeneratedProtocolMessageType('Parameter', (_message.Message,), dict(
    DESCRIPTOR = _TASKSPEC_PARAMETER,
    __module__ = 'syntaxnet.task_spec_pb2'
    # @@protoc_insertion_point(class_scope:syntaxnet.TaskSpec.Parameter)
    ))
  ,
  DESCRIPTOR = _TASKSPEC,
  __module__ = 'syntaxnet.task_spec_pb2'
  # @@protoc_insertion_point(class_scope:syntaxnet.TaskSpec)
  ))
_sym_db.RegisterMessage(TaskSpec)
_sym_db.RegisterMessage(TaskSpec.Parameter)


# @@protoc_insertion_point(module_scope)
