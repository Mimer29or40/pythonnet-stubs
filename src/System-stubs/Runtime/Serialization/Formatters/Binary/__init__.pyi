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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IStreamable(ABC):
    """"""
    def Read(self, input: __BinaryParser) -> None:
        """"""
    def Write(self, sout: __BinaryWriter) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class InternalElementTypeE(Enum):
    """"""

    ObjectBegin: InternalElementTypeE = ...
    """"""
    ObjectEnd: InternalElementTypeE = ...
    """"""
    Member: InternalElementTypeE = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class InternalObjectTypeE(Enum):
    """"""

    Empty: InternalObjectTypeE = ...
    """"""
    Object: InternalObjectTypeE = ...
    """"""
    Array: InternalObjectTypeE = ...
    """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class InternalSerializerTypeE(Enum):
    """"""

    Soap: InternalSerializerTypeE = ...
    """"""
    Binary: InternalSerializerTypeE = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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
