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
    Single: IntType = 0
    Jagged: IntType = 1
    Rectangular: IntType = 2
    SingleOffset: IntType = 3
    JaggedOffset: IntType = 4
    RectangularOffset: IntType = 5


class BinaryHeaderEnum(Enum):
    SerializedStreamHeader: IntType = 0
    Object: IntType = 1
    ObjectWithMap: IntType = 2
    ObjectWithMapAssemId: IntType = 3
    ObjectWithMapTyped: IntType = 4
    ObjectWithMapTypedAssemId: IntType = 5
    ObjectString: IntType = 6
    Array: IntType = 7
    MemberPrimitiveTyped: IntType = 8
    MemberReference: IntType = 9
    ObjectNull: IntType = 10
    MessageEnd: IntType = 11
    Assembly: IntType = 12
    ObjectNullMultiple256: IntType = 13
    ObjectNullMultiple: IntType = 14
    ArraySinglePrimitive: IntType = 15
    ArraySingleObject: IntType = 16
    ArraySingleString: IntType = 17
    CrossAppDomainMap: IntType = 18
    CrossAppDomainString: IntType = 19
    CrossAppDomainAssembly: IntType = 20
    MethodCall: IntType = 21
    MethodReturn: IntType = 22


class BinaryTypeEnum(Enum):
    Primitive: IntType = 0
    String: IntType = 1
    Object: IntType = 2
    ObjectUrt: IntType = 3
    ObjectUser: IntType = 4
    ObjectArray: IntType = 5
    StringArray: IntType = 6
    PrimitiveArray: IntType = 7


class InternalArrayTypeE(Enum):
    Empty: IntType = 0
    Single: IntType = 1
    Jagged: IntType = 2
    Rectangular: IntType = 3
    Base64: IntType = 4


class InternalElementTypeE(Enum):
    ObjectBegin: IntType = 0
    ObjectEnd: IntType = 1
    Member: IntType = 2


class InternalMemberTypeE(Enum):
    Empty: IntType = 0
    Header: IntType = 1
    Field: IntType = 2
    Item: IntType = 3


class InternalMemberValueE(Enum):
    Empty: IntType = 0
    InlineValue: IntType = 1
    Nested: IntType = 2
    Reference: IntType = 3
    Null: IntType = 4


class InternalNameSpaceE(Enum):
    #None: IntType = 0
    Soap: IntType = 1
    XdrPrimitive: IntType = 2
    XdrString: IntType = 3
    UrtSystem: IntType = 4
    UrtUser: IntType = 5
    UserNameSpace: IntType = 6
    MemberName: IntType = 7
    Interop: IntType = 8
    CallElement: IntType = 9


class InternalObjectPositionE(Enum):
    Empty: IntType = 0
    Top: IntType = 1
    Child: IntType = 2
    Headers: IntType = 3


class InternalObjectTypeE(Enum):
    Empty: IntType = 0
    Object: IntType = 1
    Array: IntType = 2


class InternalParseStateE(Enum):
    Initial: IntType = 0
    Object: IntType = 1
    Member: IntType = 2
    MemberChild: IntType = 3


class InternalParseTypeE(Enum):
    Empty: IntType = 0
    SerializedStreamHeader: IntType = 1
    Object: IntType = 2
    Member: IntType = 3
    ObjectEnd: IntType = 4
    MemberEnd: IntType = 5
    Headers: IntType = 6
    HeadersEnd: IntType = 7
    SerializedStreamHeaderEnd: IntType = 8
    Envelope: IntType = 9
    EnvelopeEnd: IntType = 10
    Body: IntType = 11
    BodyEnd: IntType = 12


class InternalPrimitiveTypeE(Enum):
    Invalid: IntType = 0
    Boolean: IntType = 1
    Byte: IntType = 2
    Char: IntType = 3
    Currency: IntType = 4
    Decimal: IntType = 5
    Double: IntType = 6
    Int16: IntType = 7
    Int32: IntType = 8
    Int64: IntType = 9
    SByte: IntType = 10
    Single: IntType = 11
    TimeSpan: IntType = 12
    DateTime: IntType = 13
    UInt16: IntType = 14
    UInt32: IntType = 15
    UInt64: IntType = 16
    Null: IntType = 17
    String: IntType = 18


class InternalSerializerTypeE(Enum):
    Soap: IntType = 1
    Binary: IntType = 2


class MessageEnum(Enum):
    NoArgs: IntType = 1
    ArgsInline: IntType = 2
    ArgsIsArray: IntType = 4
    ArgsInArray: IntType = 8
    NoContext: IntType = 16
    ContextInline: IntType = 32
    ContextInArray: IntType = 64
    MethodSignatureInArray: IntType = 128
    PropertyInArray: IntType = 256
    NoReturnValue: IntType = 512
    ReturnValueVoid: IntType = 1024
    ReturnValueInline: IntType = 2048
    ReturnValueInArray: IntType = 4096
    ExceptionInArray: IntType = 8192
    GenericMethod: IntType = 32768


class SoapAttributeType(Enum):
    #None: IntType = 0
    SchemaType: IntType = 1
    Embedded: IntType = 2
    XmlElement: IntType = 4
    XmlAttribute: IntType = 8


class ValueFixupEnum(Enum):
    Empty: IntType = 0
    Array: IntType = 1
    Header: IntType = 2
    Member: IntType = 3


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
