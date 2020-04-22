# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.internal.containers import (
    RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
    Text as typing___Text,
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


class NowPlayingClient(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    processIdentifier = ... # type: builtin___int
    bundleIdentifier = ... # type: typing___Text
    parentApplicationBundleIdentifier = ... # type: typing___Text
    processUserIdentifier = ... # type: builtin___int
    nowPlayingVisibility = ... # type: builtin___int
    displayName = ... # type: typing___Text
    bundleIdentifierHierarchys = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]

    def __init__(self,
        *,
        processIdentifier : typing___Optional[builtin___int] = None,
        bundleIdentifier : typing___Optional[typing___Text] = None,
        parentApplicationBundleIdentifier : typing___Optional[typing___Text] = None,
        processUserIdentifier : typing___Optional[builtin___int] = None,
        nowPlayingVisibility : typing___Optional[builtin___int] = None,
        displayName : typing___Optional[typing___Text] = None,
        bundleIdentifierHierarchys : typing___Optional[typing___Iterable[typing___Text]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> NowPlayingClient: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> NowPlayingClient: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"bundleIdentifier",b"bundleIdentifier",u"displayName",b"displayName",u"nowPlayingVisibility",b"nowPlayingVisibility",u"parentApplicationBundleIdentifier",b"parentApplicationBundleIdentifier",u"processIdentifier",b"processIdentifier",u"processUserIdentifier",b"processUserIdentifier"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"bundleIdentifier",b"bundleIdentifier",u"bundleIdentifierHierarchys",b"bundleIdentifierHierarchys",u"displayName",b"displayName",u"nowPlayingVisibility",b"nowPlayingVisibility",u"parentApplicationBundleIdentifier",b"parentApplicationBundleIdentifier",u"processIdentifier",b"processIdentifier",u"processUserIdentifier",b"processUserIdentifier"]) -> None: ...
global___NowPlayingClient = NowPlayingClient
