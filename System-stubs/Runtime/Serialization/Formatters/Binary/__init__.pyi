from __future__ import annotations

from abc import ABC
from typing import List, Protocol, Union, overload

from System import Array, Boolean, Enum, Exception, ICloneable, Int32, Object, String, Type, Void
from System.IO import Stream
from System.Runtime.Remoting.Messaging import Header, HeaderHandler, IMethodCallMessage, IRemotingFormatter, LogicalCallContext
from System.Runtime.Serialization import IFormatter, ISurrogateSelector, SerializationBinder, StreamingContext
from System.Runtime.Serialization.Formatters import FormatterAssemblyStyle, FormatterTypeStyle, TypeFilterLevel

# ---------- Types ---------- #

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
IntType = Union[int, Int32]
ObjectType = Object
StringType = Union[str, String]
TypeType = Union[type, Type]
VoidType = Union[None, Void]


# ---------- Classes ---------- #

class BinaryArray(ObjectType, IStreamable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Read(self, input: __BinaryParser) -> VoidType: ...
    
    def Write(self, sout: __BinaryWriter) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class BinaryAssembly(ObjectType, IStreamable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Dump(self) -> VoidType: ...
    
    def Read(self, input: __BinaryParser) -> VoidType: ...
    
    def Write(self, sout: __BinaryWriter) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class BinaryAssemblyInfo(ObjectType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class BinaryConverter(ABC, ObjectType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class BinaryCrossAppDomainAssembly(ObjectType, IStreamable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Dump(self) -> VoidType: ...
    
    def Read(self, input: __BinaryParser) -> VoidType: ...
    
    def Write(self, sout: __BinaryWriter) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class BinaryCrossAppDomainMap(ObjectType, IStreamable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Dump(self) -> VoidType: ...
    
    def Read(self, input: __BinaryParser) -> VoidType: ...
    
    def Write(self, sout: __BinaryWriter) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class BinaryCrossAppDomainString(ObjectType, IStreamable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Dump(self) -> VoidType: ...
    
    def Read(self, input: __BinaryParser) -> VoidType: ...
    
    def Write(self, sout: __BinaryWriter) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class BinaryFormatter(ObjectType, IRemotingFormatter, IFormatter):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, selector: ISurrogateSelector, context: StreamingContext): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AssemblyFormat(self) -> FormatterAssemblyStyle: ...
    
    @AssemblyFormat.setter
    def AssemblyFormat(self, value: FormatterAssemblyStyle) -> None: ...
    
    @property
    def Binder(self) -> SerializationBinder: ...
    
    @Binder.setter
    def Binder(self, value: SerializationBinder) -> None: ...
    
    @property
    def Context(self) -> StreamingContext: ...
    
    @Context.setter
    def Context(self, value: StreamingContext) -> None: ...
    
    @property
    def FilterLevel(self) -> TypeFilterLevel: ...
    
    @FilterLevel.setter
    def FilterLevel(self, value: TypeFilterLevel) -> None: ...
    
    @property
    def SurrogateSelector(self) -> ISurrogateSelector: ...
    
    @SurrogateSelector.setter
    def SurrogateSelector(self, value: ISurrogateSelector) -> None: ...
    
    @property
    def TypeFormat(self) -> FormatterTypeStyle: ...
    
    @TypeFormat.setter
    def TypeFormat(self, value: FormatterTypeStyle) -> None: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Deserialize(self, serializationStream: Stream) -> ObjectType: ...
    
    @overload
    def Deserialize(self, serializationStream: Stream, handler: HeaderHandler) -> ObjectType: ...
    
    def DeserializeMethodResponse(self, serializationStream: Stream, handler: HeaderHandler, methodCallMessage: IMethodCallMessage) -> ObjectType: ...
    
    @overload
    def Serialize(self, serializationStream: Stream, graph: ObjectType) -> VoidType: ...
    
    @overload
    def Serialize(self, serializationStream: Stream, graph: ObjectType, headers: ArrayType[Header]) -> VoidType: ...
    
    def UnsafeDeserialize(self, serializationStream: Stream, handler: HeaderHandler) -> ObjectType: ...
    
    def UnsafeDeserializeMethodResponse(self, serializationStream: Stream, handler: HeaderHandler, methodCallMessage: IMethodCallMessage) -> ObjectType: ...
    
    def get_AssemblyFormat(self) -> FormatterAssemblyStyle: ...
    
    def get_Binder(self) -> SerializationBinder: ...
    
    def get_Context(self) -> StreamingContext: ...
    
    def get_FilterLevel(self) -> TypeFilterLevel: ...
    
    def get_SurrogateSelector(self) -> ISurrogateSelector: ...
    
    def get_TypeFormat(self) -> FormatterTypeStyle: ...
    
    def set_AssemblyFormat(self, value: FormatterAssemblyStyle) -> VoidType: ...
    
    def set_Binder(self, value: SerializationBinder) -> VoidType: ...
    
    def set_Context(self, value: StreamingContext) -> VoidType: ...
    
    def set_FilterLevel(self, value: TypeFilterLevel) -> VoidType: ...
    
    def set_SurrogateSelector(self, value: ISurrogateSelector) -> VoidType: ...
    
    def set_TypeFormat(self, value: FormatterTypeStyle) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class BinaryMethodCall(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class BinaryMethodCallMessage(ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Args(self) -> ArrayType[ObjectType]: ...
    
    @property
    def HasProperties(self) -> BooleanType: ...
    
    @property
    def InstantiationArgs(self) -> ArrayType[TypeType]: ...
    
    @property
    def LogicalCallContext(self) -> LogicalCallContext: ...
    
    @property
    def MethodName(self) -> StringType: ...
    
    @property
    def MethodSignature(self) -> ObjectType: ...
    
    @property
    def TypeName(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_Args(self) -> ArrayType[ObjectType]: ...
    
    def get_HasProperties(self) -> BooleanType: ...
    
    def get_InstantiationArgs(self) -> ArrayType[TypeType]: ...
    
    def get_LogicalCallContext(self) -> LogicalCallContext: ...
    
    def get_MethodName(self) -> StringType: ...
    
    def get_MethodSignature(self) -> ObjectType: ...
    
    def get_TypeName(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class BinaryMethodReturn(ObjectType, IStreamable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Dump(self) -> VoidType: ...
    
    def Read(self, input: __BinaryParser) -> VoidType: ...
    
    def Write(self, sout: __BinaryWriter) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class BinaryMethodReturnMessage(ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Args(self) -> ArrayType[ObjectType]: ...
    
    @property
    def Exception(self) -> Exception: ...
    
    @property
    def HasProperties(self) -> BooleanType: ...
    
    @property
    def LogicalCallContext(self) -> LogicalCallContext: ...
    
    @property
    def ReturnValue(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def get_Args(self) -> ArrayType[ObjectType]: ...
    
    def get_Exception(self) -> Exception: ...
    
    def get_HasProperties(self) -> BooleanType: ...
    
    def get_LogicalCallContext(self) -> LogicalCallContext: ...
    
    def get_ReturnValue(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class BinaryObject(ObjectType, IStreamable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Dump(self) -> VoidType: ...
    
    def Read(self, input: __BinaryParser) -> VoidType: ...
    
    def Write(self, sout: __BinaryWriter) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class BinaryObjectString(ObjectType, IStreamable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Dump(self) -> VoidType: ...
    
    def Read(self, input: __BinaryParser) -> VoidType: ...
    
    def Write(self, sout: __BinaryWriter) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class BinaryObjectWithMap(ObjectType, IStreamable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Dump(self) -> VoidType: ...
    
    def Read(self, input: __BinaryParser) -> VoidType: ...
    
    def Write(self, sout: __BinaryWriter) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class BinaryObjectWithMapTyped(ObjectType, IStreamable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Read(self, input: __BinaryParser) -> VoidType: ...
    
    def Write(self, sout: __BinaryWriter) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class BinaryUtil(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    @overload
    def NVTraceI(name: StringType, value: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def NVTraceI(name: StringType, value: ObjectType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Converter(ObjectType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class IOUtil(ABC, ObjectType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class IntSizedArray(ObjectType, ICloneable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class InternalFE(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MemberPrimitiveTyped(ObjectType, IStreamable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Dump(self) -> VoidType: ...
    
    def Read(self, input: __BinaryParser) -> VoidType: ...
    
    def Write(self, sout: __BinaryWriter) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MemberPrimitiveUnTyped(ObjectType, IStreamable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Dump(self) -> VoidType: ...
    
    def Read(self, input: __BinaryParser) -> VoidType: ...
    
    def Write(self, sout: __BinaryWriter) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MemberReference(ObjectType, IStreamable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Dump(self) -> VoidType: ...
    
    def Read(self, input: __BinaryParser) -> VoidType: ...
    
    def Write(self, sout: __BinaryWriter) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MessageEnd(ObjectType, IStreamable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def Dump(self) -> VoidType: ...
    
    @overload
    def Dump(self, sout: Stream) -> VoidType: ...
    
    def Read(self, input: __BinaryParser) -> VoidType: ...
    
    def Write(self, sout: __BinaryWriter) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class NameCache(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class NameInfo(ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def IsSealed(self) -> BooleanType: ...
    
    @property
    def NIname(self) -> StringType: ...
    
    @NIname.setter
    def NIname(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_IsSealed(self) -> BooleanType: ...
    
    def get_NIname(self) -> StringType: ...
    
    def set_NIname(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ObjectMap(ObjectType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ObjectMapInfo(ObjectType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ObjectNull(ObjectType, IStreamable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Dump(self) -> VoidType: ...
    
    @overload
    def Read(self, input: __BinaryParser) -> VoidType: ...
    
    @overload
    def Read(self, input: __BinaryParser, binaryHeaderEnum: BinaryHeaderEnum) -> VoidType: ...
    
    def Write(self, sout: __BinaryWriter) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ObjectProgress(ObjectType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ObjectReader(ObjectType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ObjectWriter(ObjectType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ParseRecord(ObjectType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PrimitiveArray(ObjectType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ReadObjectInfo(ObjectType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SerObjectInfoCache(ObjectType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SerObjectInfoInit(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SerStack(ObjectType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SerializationHeaderRecord(ObjectType, IStreamable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Dump(self) -> VoidType: ...
    
    def Read(self, input: __BinaryParser) -> VoidType: ...
    
    def Write(self, sout: __BinaryWriter) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SizedArray(ObjectType, ICloneable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TypeInformation(ObjectType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ValueFixup(ObjectType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class WriteObjectInfo(ObjectType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class __BinaryParser(ObjectType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class __BinaryWriter(ObjectType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# No Structs

# ---------- Interfaces ---------- #

class IStreamable(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Read(self, input: __BinaryParser) -> VoidType: ...
    
    def Write(self, sout: __BinaryWriter) -> VoidType: ...
    
    # No Events


# ---------- Enums ---------- #

class BinaryArrayTypeEnum(Enum):
    Single = 0
    Jagged = 1
    Rectangular = 2
    SingleOffset = 3
    JaggedOffset = 4
    RectangularOffset = 5


class BinaryHeaderEnum(Enum):
    SerializedStreamHeader = 0
    Object = 1
    ObjectWithMap = 2
    ObjectWithMapAssemId = 3
    ObjectWithMapTyped = 4
    ObjectWithMapTypedAssemId = 5
    ObjectString = 6
    Array = 7
    MemberPrimitiveTyped = 8
    MemberReference = 9
    ObjectNull = 10
    MessageEnd = 11
    Assembly = 12
    ObjectNullMultiple256 = 13
    ObjectNullMultiple = 14
    ArraySinglePrimitive = 15
    ArraySingleObject = 16
    ArraySingleString = 17
    CrossAppDomainMap = 18
    CrossAppDomainString = 19
    CrossAppDomainAssembly = 20
    MethodCall = 21
    MethodReturn = 22


class BinaryTypeEnum(Enum):
    Primitive = 0
    String = 1
    Object = 2
    ObjectUrt = 3
    ObjectUser = 4
    ObjectArray = 5
    StringArray = 6
    PrimitiveArray = 7


class InternalArrayTypeE(Enum):
    Empty = 0
    Single = 1
    Jagged = 2
    Rectangular = 3
    Base64 = 4


class InternalElementTypeE(Enum):
    ObjectBegin = 0
    ObjectEnd = 1
    Member = 2


class InternalMemberTypeE(Enum):
    Empty = 0
    Header = 1
    Field = 2
    Item = 3


class InternalMemberValueE(Enum):
    Empty = 0
    InlineValue = 1
    Nested = 2
    Reference = 3
    Null = 4


class InternalNameSpaceE(Enum):
    #None = 0
    Soap = 1
    XdrPrimitive = 2
    XdrString = 3
    UrtSystem = 4
    UrtUser = 5
    UserNameSpace = 6
    MemberName = 7
    Interop = 8
    CallElement = 9


class InternalObjectPositionE(Enum):
    Empty = 0
    Top = 1
    Child = 2
    Headers = 3


class InternalObjectTypeE(Enum):
    Empty = 0
    Object = 1
    Array = 2


class InternalParseStateE(Enum):
    Initial = 0
    Object = 1
    Member = 2
    MemberChild = 3


class InternalParseTypeE(Enum):
    Empty = 0
    SerializedStreamHeader = 1
    Object = 2
    Member = 3
    ObjectEnd = 4
    MemberEnd = 5
    Headers = 6
    HeadersEnd = 7
    SerializedStreamHeaderEnd = 8
    Envelope = 9
    EnvelopeEnd = 10
    Body = 11
    BodyEnd = 12


class InternalPrimitiveTypeE(Enum):
    Invalid = 0
    Boolean = 1
    Byte = 2
    Char = 3
    Currency = 4
    Decimal = 5
    Double = 6
    Int16 = 7
    Int32 = 8
    Int64 = 9
    SByte = 10
    Single = 11
    TimeSpan = 12
    DateTime = 13
    UInt16 = 14
    UInt32 = 15
    UInt64 = 16
    Null = 17
    String = 18


class InternalSerializerTypeE(Enum):
    Soap = 1
    Binary = 2


class MessageEnum(Enum):
    NoArgs = 1
    ArgsInline = 2
    ArgsIsArray = 4
    ArgsInArray = 8
    NoContext = 16
    ContextInline = 32
    ContextInArray = 64
    MethodSignatureInArray = 128
    PropertyInArray = 256
    NoReturnValue = 512
    ReturnValueVoid = 1024
    ReturnValueInline = 2048
    ReturnValueInArray = 4096
    ExceptionInArray = 8192
    GenericMethod = 32768


class SoapAttributeType(Enum):
    #None = 0
    SchemaType = 1
    Embedded = 2
    XmlElement = 4
    XmlAttribute = 8


class ValueFixupEnum(Enum):
    Empty = 0
    Array = 1
    Header = 2
    Member = 3


# No Delegates

__all__ = [
    BinaryArray,
    BinaryAssembly,
    BinaryAssemblyInfo,
    BinaryConverter,
    BinaryCrossAppDomainAssembly,
    BinaryCrossAppDomainMap,
    BinaryCrossAppDomainString,
    BinaryFormatter,
    BinaryMethodCall,
    BinaryMethodCallMessage,
    BinaryMethodReturn,
    BinaryMethodReturnMessage,
    BinaryObject,
    BinaryObjectString,
    BinaryObjectWithMap,
    BinaryObjectWithMapTyped,
    BinaryUtil,
    Converter,
    IOUtil,
    IntSizedArray,
    InternalFE,
    MemberPrimitiveTyped,
    MemberPrimitiveUnTyped,
    MemberReference,
    MessageEnd,
    NameCache,
    NameInfo,
    ObjectMap,
    ObjectMapInfo,
    ObjectNull,
    ObjectProgress,
    ObjectReader,
    ObjectWriter,
    ParseRecord,
    PrimitiveArray,
    ReadObjectInfo,
    SerObjectInfoCache,
    SerObjectInfoInit,
    SerStack,
    SerializationHeaderRecord,
    SizedArray,
    TypeInformation,
    ValueFixup,
    WriteObjectInfo,
    __BinaryParser,
    __BinaryWriter,
    IStreamable,
    BinaryArrayTypeEnum,
    BinaryHeaderEnum,
    BinaryTypeEnum,
    InternalArrayTypeE,
    InternalElementTypeE,
    InternalMemberTypeE,
    InternalMemberValueE,
    InternalNameSpaceE,
    InternalObjectPositionE,
    InternalObjectTypeE,
    InternalParseStateE,
    InternalParseTypeE,
    InternalPrimitiveTypeE,
    InternalSerializerTypeE,
    MessageEnum,
    SoapAttributeType,
    ValueFixupEnum,
]
