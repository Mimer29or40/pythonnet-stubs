from __future__ import annotations

from abc import ABC
from typing import overload

from System import Array
from System import Enum
from System import Exception
from System import ICloneable
from System import Object
from System import Type
from System.IO import Stream
from System.Runtime.Remoting.Messaging import Header
from System.Runtime.Remoting.Messaging import HeaderHandler
from System.Runtime.Remoting.Messaging import IMethodCallMessage
from System.Runtime.Remoting.Messaging import IRemotingFormatter
from System.Runtime.Remoting.Messaging import LogicalCallContext
from System.Runtime.Serialization import IFormatter
from System.Runtime.Serialization import ISurrogateSelector
from System.Runtime.Serialization import SerializationBinder
from System.Runtime.Serialization import StreamingContext
from System.Runtime.Serialization.Formatters import FormatterAssemblyStyle
from System.Runtime.Serialization.Formatters import FormatterTypeStyle
from System.Runtime.Serialization.Formatters import TypeFilterLevel

class BinaryArray(Object, IStreamable):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def Read(self, input: __BinaryParser) -> None:
        """

        :param input:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Write(self, sout: __BinaryWriter) -> None:
        """

        :param sout:
        """

class BinaryArrayTypeEnum(Enum):
    """"""

    Single: BinaryArrayTypeEnum = ...
    """"""
    Jagged: BinaryArrayTypeEnum = ...
    """"""
    Rectangular: BinaryArrayTypeEnum = ...
    """"""
    SingleOffset: BinaryArrayTypeEnum = ...
    """"""
    JaggedOffset: BinaryArrayTypeEnum = ...
    """"""
    RectangularOffset: BinaryArrayTypeEnum = ...
    """"""

class BinaryAssembly(Object, IStreamable):
    """"""

    def Dump(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def Read(self, input: __BinaryParser) -> None:
        """

        :param input:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Write(self, sout: __BinaryWriter) -> None:
        """

        :param sout:
        """

class BinaryAssemblyInfo(Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class BinaryConverter(ABC, Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class BinaryCrossAppDomainAssembly(Object, IStreamable):
    """"""

    def Dump(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def Read(self, input: __BinaryParser) -> None:
        """

        :param input:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Write(self, sout: __BinaryWriter) -> None:
        """

        :param sout:
        """

class BinaryCrossAppDomainMap(Object, IStreamable):
    """"""

    def Dump(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def Read(self, input: __BinaryParser) -> None:
        """

        :param input:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Write(self, sout: __BinaryWriter) -> None:
        """

        :param sout:
        """

class BinaryCrossAppDomainString(Object, IStreamable):
    """"""

    def Dump(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def Read(self, input: __BinaryParser) -> None:
        """

        :param input:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Write(self, sout: __BinaryWriter) -> None:
        """

        :param sout:
        """

class BinaryFormatter(Object, IRemotingFormatter, IFormatter):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, selector: ISurrogateSelector, context: StreamingContext):
        """

        :param selector:
        :param context:
        """
    @property
    def AssemblyFormat(self) -> FormatterAssemblyStyle:
        """

        :return:
        """
    @AssemblyFormat.setter
    def AssemblyFormat(self, value: FormatterAssemblyStyle) -> None: ...
    @property
    def Binder(self) -> SerializationBinder:
        """

        :return:
        """
    @Binder.setter
    def Binder(self, value: SerializationBinder) -> None: ...
    @property
    def Context(self) -> StreamingContext:
        """

        :return:
        """
    @Context.setter
    def Context(self, value: StreamingContext) -> None: ...
    @property
    def FilterLevel(self) -> TypeFilterLevel:
        """

        :return:
        """
    @FilterLevel.setter
    def FilterLevel(self, value: TypeFilterLevel) -> None: ...
    @property
    def SurrogateSelector(self) -> ISurrogateSelector:
        """

        :return:
        """
    @SurrogateSelector.setter
    def SurrogateSelector(self, value: ISurrogateSelector) -> None: ...
    @property
    def TypeFormat(self) -> FormatterTypeStyle:
        """

        :return:
        """
    @TypeFormat.setter
    def TypeFormat(self, value: FormatterTypeStyle) -> None: ...
    @overload
    def Deserialize(self, serializationStream: Stream) -> object:
        """

        :param serializationStream:
        :return:
        """
    @overload
    def Deserialize(self, serializationStream: Stream, handler: HeaderHandler) -> object:
        """

        :param serializationStream:
        :param handler:
        :return:
        """
    def DeserializeMethodResponse(
        self,
        serializationStream: Stream,
        handler: HeaderHandler,
        methodCallMessage: IMethodCallMessage,
    ) -> object:
        """

        :param serializationStream:
        :param handler:
        :param methodCallMessage:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def Serialize(self, serializationStream: Stream, graph: object) -> None:
        """

        :param serializationStream:
        :param graph:
        """
    @overload
    def Serialize(self, serializationStream: Stream, graph: object, headers: Array[Header]) -> None:
        """

        :param serializationStream:
        :param graph:
        :param headers:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def UnsafeDeserialize(self, serializationStream: Stream, handler: HeaderHandler) -> object:
        """

        :param serializationStream:
        :param handler:
        :return:
        """
    def UnsafeDeserializeMethodResponse(
        self,
        serializationStream: Stream,
        handler: HeaderHandler,
        methodCallMessage: IMethodCallMessage,
    ) -> object:
        """

        :param serializationStream:
        :param handler:
        :param methodCallMessage:
        :return:
        """

class BinaryHeaderEnum(Enum):
    """"""

    SerializedStreamHeader: BinaryHeaderEnum = ...
    """"""
    Object: BinaryHeaderEnum = ...
    """"""
    ObjectWithMap: BinaryHeaderEnum = ...
    """"""
    ObjectWithMapAssemId: BinaryHeaderEnum = ...
    """"""
    ObjectWithMapTyped: BinaryHeaderEnum = ...
    """"""
    ObjectWithMapTypedAssemId: BinaryHeaderEnum = ...
    """"""
    ObjectString: BinaryHeaderEnum = ...
    """"""
    Array: BinaryHeaderEnum = ...
    """"""
    MemberPrimitiveTyped: BinaryHeaderEnum = ...
    """"""
    MemberReference: BinaryHeaderEnum = ...
    """"""
    ObjectNull: BinaryHeaderEnum = ...
    """"""
    MessageEnd: BinaryHeaderEnum = ...
    """"""
    Assembly: BinaryHeaderEnum = ...
    """"""
    ObjectNullMultiple256: BinaryHeaderEnum = ...
    """"""
    ObjectNullMultiple: BinaryHeaderEnum = ...
    """"""
    ArraySinglePrimitive: BinaryHeaderEnum = ...
    """"""
    ArraySingleObject: BinaryHeaderEnum = ...
    """"""
    ArraySingleString: BinaryHeaderEnum = ...
    """"""
    CrossAppDomainMap: BinaryHeaderEnum = ...
    """"""
    CrossAppDomainString: BinaryHeaderEnum = ...
    """"""
    CrossAppDomainAssembly: BinaryHeaderEnum = ...
    """"""
    MethodCall: BinaryHeaderEnum = ...
    """"""
    MethodReturn: BinaryHeaderEnum = ...
    """"""

class BinaryMethodCall(Object):
    """"""

    def __init__(self):
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class BinaryMethodCallMessage(Object):
    """"""

    @property
    def Args(self) -> Array[object]:
        """

        :return:
        """
    @property
    def HasProperties(self) -> bool:
        """

        :return:
        """
    @property
    def InstantiationArgs(self) -> Array[Type]:
        """

        :return:
        """
    @property
    def LogicalCallContext(self) -> LogicalCallContext:
        """

        :return:
        """
    @property
    def MethodName(self) -> str:
        """

        :return:
        """
    @property
    def MethodSignature(self) -> object:
        """

        :return:
        """
    @property
    def TypeName(self) -> str:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class BinaryMethodReturn(Object, IStreamable):
    """"""

    def Dump(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def Read(self, input: __BinaryParser) -> None:
        """

        :param input:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Write(self, sout: __BinaryWriter) -> None:
        """

        :param sout:
        """

class BinaryMethodReturnMessage(Object):
    """"""

    @property
    def Args(self) -> Array[object]:
        """

        :return:
        """
    @property
    def Exception(self) -> Exception:
        """

        :return:
        """
    @property
    def HasProperties(self) -> bool:
        """

        :return:
        """
    @property
    def LogicalCallContext(self) -> LogicalCallContext:
        """

        :return:
        """
    @property
    def ReturnValue(self) -> object:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class BinaryObject(Object, IStreamable):
    """"""

    def Dump(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def Read(self, input: __BinaryParser) -> None:
        """

        :param input:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Write(self, sout: __BinaryWriter) -> None:
        """

        :param sout:
        """

class BinaryObjectString(Object, IStreamable):
    """"""

    def Dump(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def Read(self, input: __BinaryParser) -> None:
        """

        :param input:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Write(self, sout: __BinaryWriter) -> None:
        """

        :param sout:
        """

class BinaryObjectWithMap(Object, IStreamable):
    """"""

    def Dump(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def Read(self, input: __BinaryParser) -> None:
        """

        :param input:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Write(self, sout: __BinaryWriter) -> None:
        """

        :param sout:
        """

class BinaryObjectWithMapTyped(Object, IStreamable):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def Read(self, input: __BinaryParser) -> None:
        """

        :param input:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Write(self, sout: __BinaryWriter) -> None:
        """

        :param sout:
        """

class BinaryTypeEnum(Enum):
    """"""

    Primitive: BinaryTypeEnum = ...
    """"""
    String: BinaryTypeEnum = ...
    """"""
    Object: BinaryTypeEnum = ...
    """"""
    ObjectUrt: BinaryTypeEnum = ...
    """"""
    ObjectUser: BinaryTypeEnum = ...
    """"""
    ObjectArray: BinaryTypeEnum = ...
    """"""
    StringArray: BinaryTypeEnum = ...
    """"""
    PrimitiveArray: BinaryTypeEnum = ...
    """"""

class BinaryUtil(ABC, Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @classmethod
    @overload
    def NVTraceI(cls, name: str, value: object) -> None:
        """

        :param name:
        :param value:
        """
    @classmethod
    @overload
    def NVTraceI(cls, name: str, value: str) -> None:
        """

        :param name:
        :param value:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class Converter(Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class IOUtil(ABC, Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class IStreamable:
    """"""

    def Read(self, input: __BinaryParser) -> None:
        """

        :param input:
        """
    def Write(self, sout: __BinaryWriter) -> None:
        """

        :param sout:
        """

class IntSizedArray(Object, ICloneable):
    """"""

    def __init__(self):
        """"""
    def Clone(self) -> object:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class InternalArrayTypeE(Enum):
    """"""

    Empty: InternalArrayTypeE = ...
    """"""
    Single: InternalArrayTypeE = ...
    """"""
    Jagged: InternalArrayTypeE = ...
    """"""
    Rectangular: InternalArrayTypeE = ...
    """"""
    Base64: InternalArrayTypeE = ...
    """"""

class InternalElementTypeE(Enum):
    """"""

    ObjectBegin: InternalElementTypeE = ...
    """"""
    ObjectEnd: InternalElementTypeE = ...
    """"""
    Member: InternalElementTypeE = ...
    """"""

class InternalFE(Object):
    """"""

    def __init__(self):
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class InternalMemberTypeE(Enum):
    """"""

    Empty: InternalMemberTypeE = ...
    """"""
    Header: InternalMemberTypeE = ...
    """"""
    Field: InternalMemberTypeE = ...
    """"""
    Item: InternalMemberTypeE = ...
    """"""

class InternalMemberValueE(Enum):
    """"""

    Empty: InternalMemberValueE = ...
    """"""
    InlineValue: InternalMemberValueE = ...
    """"""
    Nested: InternalMemberValueE = ...
    """"""
    Reference: InternalMemberValueE = ...
    """"""
    Null: InternalMemberValueE = ...
    """"""

class InternalNameSpaceE(Enum):
    """"""

    _None: InternalNameSpaceE = ...
    """"""
    Soap: InternalNameSpaceE = ...
    """"""
    XdrPrimitive: InternalNameSpaceE = ...
    """"""
    XdrString: InternalNameSpaceE = ...
    """"""
    UrtSystem: InternalNameSpaceE = ...
    """"""
    UrtUser: InternalNameSpaceE = ...
    """"""
    UserNameSpace: InternalNameSpaceE = ...
    """"""
    MemberName: InternalNameSpaceE = ...
    """"""
    Interop: InternalNameSpaceE = ...
    """"""
    CallElement: InternalNameSpaceE = ...
    """"""

class InternalObjectPositionE(Enum):
    """"""

    Empty: InternalObjectPositionE = ...
    """"""
    Top: InternalObjectPositionE = ...
    """"""
    Child: InternalObjectPositionE = ...
    """"""
    Headers: InternalObjectPositionE = ...
    """"""

class InternalObjectTypeE(Enum):
    """"""

    Empty: InternalObjectTypeE = ...
    """"""
    Object: InternalObjectTypeE = ...
    """"""
    Array: InternalObjectTypeE = ...
    """"""

class InternalParseStateE(Enum):
    """"""

    Initial: InternalParseStateE = ...
    """"""
    Object: InternalParseStateE = ...
    """"""
    Member: InternalParseStateE = ...
    """"""
    MemberChild: InternalParseStateE = ...
    """"""

class InternalParseTypeE(Enum):
    """"""

    Empty: InternalParseTypeE = ...
    """"""
    SerializedStreamHeader: InternalParseTypeE = ...
    """"""
    Object: InternalParseTypeE = ...
    """"""
    Member: InternalParseTypeE = ...
    """"""
    ObjectEnd: InternalParseTypeE = ...
    """"""
    MemberEnd: InternalParseTypeE = ...
    """"""
    Headers: InternalParseTypeE = ...
    """"""
    HeadersEnd: InternalParseTypeE = ...
    """"""
    SerializedStreamHeaderEnd: InternalParseTypeE = ...
    """"""
    Envelope: InternalParseTypeE = ...
    """"""
    EnvelopeEnd: InternalParseTypeE = ...
    """"""
    Body: InternalParseTypeE = ...
    """"""
    BodyEnd: InternalParseTypeE = ...
    """"""

class InternalPrimitiveTypeE(Enum):
    """"""

    Invalid: InternalPrimitiveTypeE = ...
    """"""
    Boolean: InternalPrimitiveTypeE = ...
    """"""
    Byte: InternalPrimitiveTypeE = ...
    """"""
    Char: InternalPrimitiveTypeE = ...
    """"""
    Currency: InternalPrimitiveTypeE = ...
    """"""
    Decimal: InternalPrimitiveTypeE = ...
    """"""
    Double: InternalPrimitiveTypeE = ...
    """"""
    Int16: InternalPrimitiveTypeE = ...
    """"""
    Int32: InternalPrimitiveTypeE = ...
    """"""
    Int64: InternalPrimitiveTypeE = ...
    """"""
    SByte: InternalPrimitiveTypeE = ...
    """"""
    Single: InternalPrimitiveTypeE = ...
    """"""
    TimeSpan: InternalPrimitiveTypeE = ...
    """"""
    DateTime: InternalPrimitiveTypeE = ...
    """"""
    UInt16: InternalPrimitiveTypeE = ...
    """"""
    UInt32: InternalPrimitiveTypeE = ...
    """"""
    UInt64: InternalPrimitiveTypeE = ...
    """"""
    Null: InternalPrimitiveTypeE = ...
    """"""
    String: InternalPrimitiveTypeE = ...
    """"""

class InternalSerializerTypeE(Enum):
    """"""

    Soap: InternalSerializerTypeE = ...
    """"""
    Binary: InternalSerializerTypeE = ...
    """"""

class MemberPrimitiveTyped(Object, IStreamable):
    """"""

    def Dump(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def Read(self, input: __BinaryParser) -> None:
        """

        :param input:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Write(self, sout: __BinaryWriter) -> None:
        """

        :param sout:
        """

class MemberPrimitiveUnTyped(Object, IStreamable):
    """"""

    def Dump(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def Read(self, input: __BinaryParser) -> None:
        """

        :param input:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Write(self, sout: __BinaryWriter) -> None:
        """

        :param sout:
        """

class MemberReference(Object, IStreamable):
    """"""

    def Dump(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def Read(self, input: __BinaryParser) -> None:
        """

        :param input:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Write(self, sout: __BinaryWriter) -> None:
        """

        :param sout:
        """

class MessageEnd(Object, IStreamable):
    """"""

    @overload
    def Dump(self) -> None:
        """"""
    @overload
    def Dump(self, sout: Stream) -> None:
        """

        :param sout:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def Read(self, input: __BinaryParser) -> None:
        """

        :param input:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Write(self, sout: __BinaryWriter) -> None:
        """

        :param sout:
        """

class MessageEnum(Enum):
    """"""

    NoArgs: MessageEnum = ...
    """"""
    ArgsInline: MessageEnum = ...
    """"""
    ArgsIsArray: MessageEnum = ...
    """"""
    ArgsInArray: MessageEnum = ...
    """"""
    NoContext: MessageEnum = ...
    """"""
    ContextInline: MessageEnum = ...
    """"""
    ContextInArray: MessageEnum = ...
    """"""
    MethodSignatureInArray: MessageEnum = ...
    """"""
    PropertyInArray: MessageEnum = ...
    """"""
    NoReturnValue: MessageEnum = ...
    """"""
    ReturnValueVoid: MessageEnum = ...
    """"""
    ReturnValueInline: MessageEnum = ...
    """"""
    ReturnValueInArray: MessageEnum = ...
    """"""
    ExceptionInArray: MessageEnum = ...
    """"""
    GenericMethod: MessageEnum = ...
    """"""

class NameCache(Object):
    """"""

    def __init__(self):
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class NameInfo(Object):
    """"""

    @property
    def IsSealed(self) -> bool:
        """

        :return:
        """
    @property
    def NIname(self) -> str:
        """

        :return:
        """
    @NIname.setter
    def NIname(self, value: str) -> None: ...
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class ObjectMap(Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class ObjectMapInfo(Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class ObjectNull(Object, IStreamable):
    """"""

    def Dump(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def Read(self, input: __BinaryParser) -> None:
        """

        :param input:
        """
    @overload
    def Read(self, input: __BinaryParser, binaryHeaderEnum: BinaryHeaderEnum) -> None:
        """

        :param input:
        :param binaryHeaderEnum:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Write(self, sout: __BinaryWriter) -> None:
        """

        :param sout:
        """

class ObjectProgress(Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class ObjectReader(Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class ObjectWriter(Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class ParseRecord(Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class PrimitiveArray(Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class ReadObjectInfo(Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class SerObjectInfoCache(Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class SerObjectInfoInit(Object):
    """"""

    def __init__(self):
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class SerStack(Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class SerializationHeaderRecord(Object, IStreamable):
    """"""

    def Dump(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def Read(self, input: __BinaryParser) -> None:
        """

        :param input:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Write(self, sout: __BinaryWriter) -> None:
        """

        :param sout:
        """

class SizedArray(Object, ICloneable):
    """"""

    def Clone(self) -> object:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class SoapAttributeType(Enum):
    """"""

    _None: SoapAttributeType = ...
    """"""
    SchemaType: SoapAttributeType = ...
    """"""
    Embedded: SoapAttributeType = ...
    """"""
    XmlElement: SoapAttributeType = ...
    """"""
    XmlAttribute: SoapAttributeType = ...
    """"""

class TypeInformation(Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class ValueFixup(Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class ValueFixupEnum(Enum):
    """"""

    Empty: ValueFixupEnum = ...
    """"""
    Array: ValueFixupEnum = ...
    """"""
    Header: ValueFixupEnum = ...
    """"""
    Member: ValueFixupEnum = ...
    """"""

class WriteObjectInfo(Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class __BinaryParser(Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class __BinaryWriter(Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
