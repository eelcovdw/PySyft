# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/core/tensor/single_entity_phi_tensor.proto
"""Generated protocol buffer code."""
# third party
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


# syft absolute
from syft.proto.core.adp import entity_pb2 as proto_dot_core_dot_adp_dot_entity__pb2
from syft.proto.core.common import (
    common_object_pb2 as proto_dot_core_dot_common_dot_common__object__pb2,
)
from syft.proto.core.io import address_pb2 as proto_dot_core_dot_io_dot_address__pb2
from syft.proto.core.tensor import (
    tensor_pb2 as proto_dot_core_dot_tensor_dot_tensor__pb2,
)
from syft.proto.lib.numpy import array_pb2 as proto_dot_lib_dot_numpy_dot_array__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
    name="proto/core/tensor/single_entity_phi_tensor.proto",
    package="syft.core.tensor",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b"\n0proto/core/tensor/single_entity_phi_tensor.proto\x12\x10syft.core.tensor\x1a\x1bproto/core/adp/entity.proto\x1a\x1eproto/core/tensor/tensor.proto\x1a\x1bproto/lib/numpy/array.proto\x1a\x1bproto/core/io/address.proto\x1a%proto/core/common/common_object.proto\"\x82\x03\n)TensorWrappedSingleEntityPhiTensorPointer\x12%\n\x06\x65ntity\x18\x01 \x01(\x0b\x32\x15.syft.core.adp.Entity\x12,\n\x08min_vals\x18\x02 \x01(\x0b\x32\x1a.syft.lib.numpy.NumpyProto\x12,\n\x08max_vals\x18\x03 \x01(\x0b\x32\x1a.syft.lib.numpy.NumpyProto\x12'\n\x08location\x18\x04 \x01(\x0b\x32\x15.syft.core.io.Address\x12\x16\n\x0escalar_manager\x18\x05 \x01(\x0c\x12-\n\x0eid_at_location\x18\x06 \x01(\x0b\x32\x15.syft.core.common.UID\x12\x13\n\x0bobject_type\x18\x07 \x01(\t\x12\x0c\n\x04tags\x18\x08 \x03(\t\x12\x13\n\x0b\x64\x65scription\x18\t \x01(\t\x12\x19\n\x0cpublic_shape\x18\n \x01(\x0cH\x00\x88\x01\x01\x42\x0f\n\r_public_shapeb\x06proto3",
    dependencies=[
        proto_dot_core_dot_adp_dot_entity__pb2.DESCRIPTOR,
        proto_dot_core_dot_tensor_dot_tensor__pb2.DESCRIPTOR,
        proto_dot_lib_dot_numpy_dot_array__pb2.DESCRIPTOR,
        proto_dot_core_dot_io_dot_address__pb2.DESCRIPTOR,
        proto_dot_core_dot_common_dot_common__object__pb2.DESCRIPTOR,
    ],
)


_TENSORWRAPPEDSINGLEENTITYPHITENSORPOINTER = _descriptor.Descriptor(
    name="TensorWrappedSingleEntityPhiTensorPointer",
    full_name="syft.core.tensor.TensorWrappedSingleEntityPhiTensorPointer",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="entity",
            full_name="syft.core.tensor.TensorWrappedSingleEntityPhiTensorPointer.entity",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="min_vals",
            full_name="syft.core.tensor.TensorWrappedSingleEntityPhiTensorPointer.min_vals",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="max_vals",
            full_name="syft.core.tensor.TensorWrappedSingleEntityPhiTensorPointer.max_vals",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="location",
            full_name="syft.core.tensor.TensorWrappedSingleEntityPhiTensorPointer.location",
            index=3,
            number=4,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="scalar_manager",
            full_name="syft.core.tensor.TensorWrappedSingleEntityPhiTensorPointer.scalar_manager",
            index=4,
            number=5,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"",
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="id_at_location",
            full_name="syft.core.tensor.TensorWrappedSingleEntityPhiTensorPointer.id_at_location",
            index=5,
            number=6,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="object_type",
            full_name="syft.core.tensor.TensorWrappedSingleEntityPhiTensorPointer.object_type",
            index=6,
            number=7,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="tags",
            full_name="syft.core.tensor.TensorWrappedSingleEntityPhiTensorPointer.tags",
            index=7,
            number=8,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="description",
            full_name="syft.core.tensor.TensorWrappedSingleEntityPhiTensorPointer.description",
            index=8,
            number=9,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="public_shape",
            full_name="syft.core.tensor.TensorWrappedSingleEntityPhiTensorPointer.public_shape",
            index=9,
            number=10,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"",
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name="_public_shape",
            full_name="syft.core.tensor.TensorWrappedSingleEntityPhiTensorPointer._public_shape",
            index=0,
            containing_type=None,
            create_key=_descriptor._internal_create_key,
            fields=[],
        ),
    ],
    serialized_start=229,
    serialized_end=615,
)

_TENSORWRAPPEDSINGLEENTITYPHITENSORPOINTER.fields_by_name[
    "entity"
].message_type = proto_dot_core_dot_adp_dot_entity__pb2._ENTITY
_TENSORWRAPPEDSINGLEENTITYPHITENSORPOINTER.fields_by_name[
    "min_vals"
].message_type = proto_dot_lib_dot_numpy_dot_array__pb2._NUMPYPROTO
_TENSORWRAPPEDSINGLEENTITYPHITENSORPOINTER.fields_by_name[
    "max_vals"
].message_type = proto_dot_lib_dot_numpy_dot_array__pb2._NUMPYPROTO
_TENSORWRAPPEDSINGLEENTITYPHITENSORPOINTER.fields_by_name[
    "location"
].message_type = proto_dot_core_dot_io_dot_address__pb2._ADDRESS
_TENSORWRAPPEDSINGLEENTITYPHITENSORPOINTER.fields_by_name[
    "id_at_location"
].message_type = proto_dot_core_dot_common_dot_common__object__pb2._UID
_TENSORWRAPPEDSINGLEENTITYPHITENSORPOINTER.oneofs_by_name[
    "_public_shape"
].fields.append(
    _TENSORWRAPPEDSINGLEENTITYPHITENSORPOINTER.fields_by_name["public_shape"]
)
_TENSORWRAPPEDSINGLEENTITYPHITENSORPOINTER.fields_by_name[
    "public_shape"
].containing_oneof = _TENSORWRAPPEDSINGLEENTITYPHITENSORPOINTER.oneofs_by_name[
    "_public_shape"
]
DESCRIPTOR.message_types_by_name[
    "TensorWrappedSingleEntityPhiTensorPointer"
] = _TENSORWRAPPEDSINGLEENTITYPHITENSORPOINTER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TensorWrappedSingleEntityPhiTensorPointer = _reflection.GeneratedProtocolMessageType(
    "TensorWrappedSingleEntityPhiTensorPointer",
    (_message.Message,),
    {
        "DESCRIPTOR": _TENSORWRAPPEDSINGLEENTITYPHITENSORPOINTER,
        "__module__": "proto.core.tensor.single_entity_phi_tensor_pb2"
        # @@protoc_insertion_point(class_scope:syft.core.tensor.TensorWrappedSingleEntityPhiTensorPointer)
    },
)
_sym_db.RegisterMessage(TensorWrappedSingleEntityPhiTensorPointer)


# @@protoc_insertion_point(module_scope)
