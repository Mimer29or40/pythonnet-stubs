"""Automatically generated stubs for C# namespace: System.Runtime.Serialization.Formatters.Binary."""

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
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Read(self, input: __BinaryParser) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def Write(self, sout: __BinaryWriter) -> None:
        """"""

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
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Read(self, input: __BinaryParser) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def Write(self, sout: __BinaryWriter) -> None:
        """"""

class BinaryAssemblyInfo(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class BinaryConverter(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class BinaryCrossAppDomainAssembly(Object, IStreamable):
    """"""
    def Dump(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Read(self, input: __BinaryParser) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def Write(self, sout: __BinaryWriter) -> None:
        """"""

class BinaryCrossAppDomainMap(Object, IStreamable):
    """"""
    def Dump(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Read(self, input: __BinaryParser) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def Write(self, sout: __BinaryWriter) -> None:
        """"""

class BinaryCrossAppDomainString(Object, IStreamable):
    """"""
    def Dump(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Read(self, input: __BinaryParser) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def Write(self, sout: __BinaryWriter) -> None:
        """"""

class BinaryFormatter(Object, IRemotingFormatter, IFormatter):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, selector: ISurrogateSelector, context: StreamingContext) -> None:
        """"""
    @property
    def AssemblyFormat(self) -> FormatterAssemblyStyle:
        """"""
    @AssemblyFormat.setter
    def AssemblyFormat(self, value: FormatterAssemblyStyle) -> None: ...
    @property
    def Binder(self) -> SerializationBinder:
        """"""
    @Binder.setter
    def Binder(self, value: SerializationBinder) -> None: ...
    @property
    def Context(self) -> StreamingContext:
        """"""
    @Context.setter
    def Context(self, value: StreamingContext) -> None: ...
    @property
    def FilterLevel(self) -> TypeFilterLevel:
        """"""
    @FilterLevel.setter
    def FilterLevel(self, value: TypeFilterLevel) -> None: ...
    @property
    def SurrogateSelector(self) -> ISurrogateSelector:
        """"""
    @SurrogateSelector.setter
    def SurrogateSelector(self, value: ISurrogateSelector) -> None: ...
    @property
    def TypeFormat(self) -> FormatterTypeStyle:
        """"""
    @TypeFormat.setter
    def TypeFormat(self, value: FormatterTypeStyle) -> None: ...
    @overload
    def Deserialize(self, serializationStream: Stream) -> object:
        """"""
    @overload
    def Deserialize(self, serializationStream: Stream, handler: HeaderHandler) -> object:
        """"""
    def DeserializeMethodResponse(
        self,
        serializationStream: Stream,
        handler: HeaderHandler,
        methodCallMessage: IMethodCallMessage,
    ) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def Serialize(self, serializationStream: Stream, graph: object) -> None:
        """"""
    @overload
    def Serialize(self, serializationStream: Stream, graph: object, headers: Array[Header]) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def UnsafeDeserialize(self, serializationStream: Stream, handler: HeaderHandler) -> object:
        """"""
    def UnsafeDeserializeMethodResponse(
        self,
        serializationStream: Stream,
        handler: HeaderHandler,
        methodCallMessage: IMethodCallMessage,
    ) -> object:
        """"""

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
    def __init__(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class BinaryMethodCallMessage(Object):
    """"""
    @property
    def Args(self) -> Array[object]:
        """"""
    @property
    def HasProperties(self) -> bool:
        """"""
    @property
    def InstantiationArgs(self) -> Array[Type]:
        """"""
    @property
    def LogicalCallContext(self) -> LogicalCallContext:
        """"""
    @property
    def MethodName(self) -> str:
        """"""
    @property
    def MethodSignature(self) -> object:
        """"""
    @property
    def TypeName(self) -> str:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class BinaryMethodReturn(Object, IStreamable):
    """"""
    def Dump(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Read(self, input: __BinaryParser) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def Write(self, sout: __BinaryWriter) -> None:
        """"""

class BinaryMethodReturnMessage(Object):
    """"""
    @property
    def Args(self) -> Array[object]:
        """"""
    @property
    def Exception(self) -> Exception:
        """"""
    @property
    def HasProperties(self) -> bool:
        """"""
    @property
    def LogicalCallContext(self) -> LogicalCallContext:
        """"""
    @property
    def ReturnValue(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class BinaryObject(Object, IStreamable):
    """"""
    def Dump(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Read(self, input: __BinaryParser) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def Write(self, sout: __BinaryWriter) -> None:
        """"""

class BinaryObjectString(Object, IStreamable):
    """"""
    def Dump(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Read(self, input: __BinaryParser) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def Write(self, sout: __BinaryWriter) -> None:
        """"""

class BinaryObjectWithMap(Object, IStreamable):
    """"""
    def Dump(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Read(self, input: __BinaryParser) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def Write(self, sout: __BinaryWriter) -> None:
        """"""

class BinaryObjectWithMapTyped(Object, IStreamable):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Read(self, input: __BinaryParser) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def Write(self, sout: __BinaryWriter) -> None:
        """"""

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
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    @overload
    def NVTraceI(cls, name: str, value: object) -> None:
        """"""
    @classmethod
    @overload
    def NVTraceI(cls, name: str, value: str) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class Converter(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class IOUtil(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class IStreamable(ABC):
    """"""
    def Read(self, input: __BinaryParser) -> None:
        """"""
    def Write(self, sout: __BinaryWriter) -> None:
        """"""

class IntSizedArray(Object, ICloneable):
    """"""
    def __init__(self) -> None:
        """"""
    def Clone(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

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
    def __init__(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

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
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Read(self, input: __BinaryParser) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def Write(self, sout: __BinaryWriter) -> None:
        """"""

class MemberPrimitiveUnTyped(Object, IStreamable):
    """"""
    def Dump(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Read(self, input: __BinaryParser) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def Write(self, sout: __BinaryWriter) -> None:
        """"""

class MemberReference(Object, IStreamable):
    """"""
    def Dump(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Read(self, input: __BinaryParser) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def Write(self, sout: __BinaryWriter) -> None:
        """"""

class MessageEnd(Object, IStreamable):
    """"""
    @overload
    def Dump(self) -> None:
        """"""
    @overload
    def Dump(self, sout: Stream) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Read(self, input: __BinaryParser) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def Write(self, sout: __BinaryWriter) -> None:
        """"""

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
    def __init__(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class NameInfo(Object):
    """"""
    @property
    def IsSealed(self) -> bool:
        """"""
    @property
    def NIname(self) -> str:
        """"""
    @NIname.setter
    def NIname(self, value: str) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ObjectMap(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ObjectMapInfo(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ObjectNull(Object, IStreamable):
    """"""
    def Dump(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def Read(self, input: __BinaryParser) -> None:
        """"""
    @overload
    def Read(self, input: __BinaryParser, binaryHeaderEnum: BinaryHeaderEnum) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def Write(self, sout: __BinaryWriter) -> None:
        """"""

class ObjectProgress(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ObjectReader(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ObjectWriter(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ParseRecord(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class PrimitiveArray(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ReadObjectInfo(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SerObjectInfoCache(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SerObjectInfoInit(Object):
    """"""
    def __init__(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SerStack(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SerializationHeaderRecord(Object, IStreamable):
    """"""
    def Dump(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Read(self, input: __BinaryParser) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def Write(self, sout: __BinaryWriter) -> None:
        """"""

class SizedArray(Object, ICloneable):
    """"""
    def Clone(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

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
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ValueFixup(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

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
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class __BinaryParser(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class __BinaryWriter(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
