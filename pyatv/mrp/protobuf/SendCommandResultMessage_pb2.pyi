# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
    FieldDescriptor as google___protobuf___descriptor___FieldDescriptor,
)

from google.protobuf.internal.containers import (
    RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from pyatv.mrp.protobuf.PlayerPath_pb2 import (
    PlayerPath as pyatv___mrp___protobuf___PlayerPath_pb2___PlayerPath,
)

from typing import (
    Iterable as typing___Iterable,
    List as typing___List,
    Optional as typing___Optional,
    Text as typing___Text,
    Tuple as typing___Tuple,
    Union as typing___Union,
    cast as typing___cast,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int
builtin___str = str
if sys.version_info < (3,):
    builtin___buffer = buffer
    builtin___unicode = unicode


class SendCommandResultMessage(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class SendError(builtin___int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: builtin___int) -> builtin___str: ...
        @classmethod
        def Value(cls, name: builtin___str) -> 'SendCommandResultMessage.SendError': ...
        @classmethod
        def keys(cls) -> typing___List[builtin___str]: ...
        @classmethod
        def values(cls) -> typing___List['SendCommandResultMessage.SendError']: ...
        @classmethod
        def items(cls) -> typing___List[typing___Tuple[builtin___str, 'SendCommandResultMessage.SendError']]: ...
        NoError = typing___cast('SendCommandResultMessage.SendError', 0)
        ApplicationNotFound = typing___cast('SendCommandResultMessage.SendError', 1)
        ConnectionFailed = typing___cast('SendCommandResultMessage.SendError', 2)
        Ignored = typing___cast('SendCommandResultMessage.SendError', 3)
        CouldNotLaunchApplication = typing___cast('SendCommandResultMessage.SendError', 4)
        TimedOut = typing___cast('SendCommandResultMessage.SendError', 5)
        OriginDoesNotExist = typing___cast('SendCommandResultMessage.SendError', 6)
        InvalidOptions = typing___cast('SendCommandResultMessage.SendError', 7)
        NoCommandHandlers = typing___cast('SendCommandResultMessage.SendError', 8)
        ApplicationNotInstalled = typing___cast('SendCommandResultMessage.SendError', 9)
    NoError = typing___cast('SendCommandResultMessage.SendError', 0)
    ApplicationNotFound = typing___cast('SendCommandResultMessage.SendError', 1)
    ConnectionFailed = typing___cast('SendCommandResultMessage.SendError', 2)
    Ignored = typing___cast('SendCommandResultMessage.SendError', 3)
    CouldNotLaunchApplication = typing___cast('SendCommandResultMessage.SendError', 4)
    TimedOut = typing___cast('SendCommandResultMessage.SendError', 5)
    OriginDoesNotExist = typing___cast('SendCommandResultMessage.SendError', 6)
    InvalidOptions = typing___cast('SendCommandResultMessage.SendError', 7)
    NoCommandHandlers = typing___cast('SendCommandResultMessage.SendError', 8)
    ApplicationNotInstalled = typing___cast('SendCommandResultMessage.SendError', 9)
    global___SendError = SendError

    class HandlerReturnStatus(builtin___int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: builtin___int) -> builtin___str: ...
        @classmethod
        def Value(cls, name: builtin___str) -> 'SendCommandResultMessage.HandlerReturnStatus': ...
        @classmethod
        def keys(cls) -> typing___List[builtin___str]: ...
        @classmethod
        def values(cls) -> typing___List['SendCommandResultMessage.HandlerReturnStatus']: ...
        @classmethod
        def items(cls) -> typing___List[typing___Tuple[builtin___str, 'SendCommandResultMessage.HandlerReturnStatus']]: ...
        Success = typing___cast('SendCommandResultMessage.HandlerReturnStatus', 0)
        NoSuchContent = typing___cast('SendCommandResultMessage.HandlerReturnStatus', 1)
        CommandFailed = typing___cast('SendCommandResultMessage.HandlerReturnStatus', 2)
        NoActionableNowPlayingItem = typing___cast('SendCommandResultMessage.HandlerReturnStatus', 10)
        DeviceNotFound = typing___cast('SendCommandResultMessage.HandlerReturnStatus', 20)
        UIKitLegacy = typing___cast('SendCommandResultMessage.HandlerReturnStatus', 3)
        SkipAdProhibited = typing___cast('SendCommandResultMessage.HandlerReturnStatus', 100)
        QueueIsUserCurated = typing___cast('SendCommandResultMessage.HandlerReturnStatus', 101)
        UserModifiedQueueDisabled = typing___cast('SendCommandResultMessage.HandlerReturnStatus', 102)
        UserQueueModificationNotSupportedForCurrentItem = typing___cast('SendCommandResultMessage.HandlerReturnStatus', 103)
        SubscriptionRequiredForSharedQueue = typing___cast('SendCommandResultMessage.HandlerReturnStatus', 104)
    Success = typing___cast('SendCommandResultMessage.HandlerReturnStatus', 0)
    NoSuchContent = typing___cast('SendCommandResultMessage.HandlerReturnStatus', 1)
    CommandFailed = typing___cast('SendCommandResultMessage.HandlerReturnStatus', 2)
    NoActionableNowPlayingItem = typing___cast('SendCommandResultMessage.HandlerReturnStatus', 10)
    DeviceNotFound = typing___cast('SendCommandResultMessage.HandlerReturnStatus', 20)
    UIKitLegacy = typing___cast('SendCommandResultMessage.HandlerReturnStatus', 3)
    SkipAdProhibited = typing___cast('SendCommandResultMessage.HandlerReturnStatus', 100)
    QueueIsUserCurated = typing___cast('SendCommandResultMessage.HandlerReturnStatus', 101)
    UserModifiedQueueDisabled = typing___cast('SendCommandResultMessage.HandlerReturnStatus', 102)
    UserQueueModificationNotSupportedForCurrentItem = typing___cast('SendCommandResultMessage.HandlerReturnStatus', 103)
    SubscriptionRequiredForSharedQueue = typing___cast('SendCommandResultMessage.HandlerReturnStatus', 104)
    global___HandlerReturnStatus = HandlerReturnStatus

    sendError = ... # type: global___SendCommandResultMessage.SendError
    handlerReturnStatus = ... # type: global___SendCommandResultMessage.HandlerReturnStatus
    handlerReturnStatusDatas = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___bytes]
    commandID = ... # type: typing___Text

    @property
    def playerPath(self) -> pyatv___mrp___protobuf___PlayerPath_pb2___PlayerPath: ...

    def __init__(self,
        *,
        sendError : typing___Optional[global___SendCommandResultMessage.SendError] = None,
        handlerReturnStatus : typing___Optional[global___SendCommandResultMessage.HandlerReturnStatus] = None,
        handlerReturnStatusDatas : typing___Optional[typing___Iterable[builtin___bytes]] = None,
        commandID : typing___Optional[typing___Text] = None,
        playerPath : typing___Optional[pyatv___mrp___protobuf___PlayerPath_pb2___PlayerPath] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> SendCommandResultMessage: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> SendCommandResultMessage: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"commandID",b"commandID",u"handlerReturnStatus",b"handlerReturnStatus",u"playerPath",b"playerPath",u"sendError",b"sendError"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"commandID",b"commandID",u"handlerReturnStatus",b"handlerReturnStatus",u"handlerReturnStatusDatas",b"handlerReturnStatusDatas",u"playerPath",b"playerPath",u"sendError",b"sendError"]) -> None: ...
global___SendCommandResultMessage = SendCommandResultMessage

sendCommandResultMessage = ... # type: google___protobuf___descriptor___FieldDescriptor
