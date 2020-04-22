# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FieldDescriptor as google___protobuf___descriptor___FieldDescriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    Optional as typing___Optional,
    Union as typing___Union,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int
if sys.version_info < (3,):
    builtin___buffer = buffer
    builtin___unicode = unicode


class SetHiliteModeMessage(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    hiliteMode = ... # type: builtin___int

    def __init__(self,
        *,
        hiliteMode : typing___Optional[builtin___int] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> SetHiliteModeMessage: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> SetHiliteModeMessage: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"hiliteMode",b"hiliteMode"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"hiliteMode",b"hiliteMode"]) -> None: ...
global___SetHiliteModeMessage = SetHiliteModeMessage

setHiliteModeMessage = ... # type: google___protobuf___descriptor___FieldDescriptor
