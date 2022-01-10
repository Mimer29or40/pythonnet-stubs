from __future__ import annotations

from abc import ABC
from typing import Callable, List, Protocol, Tuple, Union, overload

from System import Array, AsyncCallback, Attribute, Boolean, Byte, Char, DateTime, Decimal, Double, Enum, EventArgs, Exception, IAsyncResult, ICloneable, Int16, Int32, Int64, IntPtr, MulticastDelegate, Object, RuntimeFieldHandle, SByte, Single, String, SystemException, Type, TypeCode, UInt16, UInt32, UInt64, ValueType, Void
from System.Collections import Hashtable, ICollection, IDictionary, IEnumerable, IEnumerator
from System.Globalization import CultureInfo
from System.IO import Stream
from System.Reflection import Assembly, Binder, BindingFlags, FieldAttributes, FieldInfo, ICustomAttributeProvider, MemberInfo, Module
from System.Runtime.InteropServices import _Attribute, _Exception, _FieldInfo, _MemberInfo
from System.Runtime.Serialization.Formatters import TypeFilterLevel

# ---------- Types ---------- #

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
ByteType = Union[int, Byte]
CharType = Union[str, Char]
DecimalType = Union[float, Decimal]
DoubleType = Union[float, Double]
FloatType = Union[float, Single]
IntType = Union[int, Int32]
LongType = Union[int, Int64]
NIntType = Union[int, IntPtr]
ObjectType = Object
SByteType = Union[int, SByte]
ShortType = Union[int, Int16]
StringType = Union[str, String]
TypeType = Union[type, Type]
UIntType = Union[int, UInt32]
ULongType = Union[int, UInt64]
UShortType = Union[int, UInt16]
VoidType = Union[None, Void]

# ---------- Classes ---------- #

class DeserializationEventHandler(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, sender: ObjectType, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, sender: ObjectType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DeserializationEventHandler(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, sender: ObjectType, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, sender: ObjectType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DeserializationEventHandler(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, sender: ObjectType, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, sender: ObjectType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class FixupHolder(ObjectType):
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


class FixupHolder(ObjectType):
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


class FixupHolder(ObjectType):
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


class FixupHolderList(ObjectType):
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


class FixupHolderList(ObjectType):
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


class FixupHolderList(ObjectType):
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


class Formatter(ABC, ObjectType, IFormatter):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Binder(self) -> SerializationBinder: ...
    
    @Binder.setter
    def Binder(self, value: SerializationBinder) -> None: ...
    
    @property
    def Context(self) -> StreamingContext: ...
    
    @Context.setter
    def Context(self, value: StreamingContext) -> None: ...
    
    @property
    def SurrogateSelector(self) -> ISurrogateSelector: ...
    
    @SurrogateSelector.setter
    def SurrogateSelector(self, value: ISurrogateSelector) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Deserialize(self, serializationStream: Stream) -> ObjectType: ...
    
    def Serialize(self, serializationStream: Stream, graph: ObjectType) -> VoidType: ...
    
    def get_Binder(self) -> SerializationBinder: ...
    
    def get_Context(self) -> StreamingContext: ...
    
    def get_SurrogateSelector(self) -> ISurrogateSelector: ...
    
    def set_Binder(self, value: SerializationBinder) -> VoidType: ...
    
    def set_Context(self, value: StreamingContext) -> VoidType: ...
    
    def set_SurrogateSelector(self, value: ISurrogateSelector) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Formatter(ABC, ObjectType, IFormatter):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Binder(self) -> SerializationBinder: ...
    
    @Binder.setter
    def Binder(self, value: SerializationBinder) -> None: ...
    
    @property
    def Context(self) -> StreamingContext: ...
    
    @Context.setter
    def Context(self, value: StreamingContext) -> None: ...
    
    @property
    def SurrogateSelector(self) -> ISurrogateSelector: ...
    
    @SurrogateSelector.setter
    def SurrogateSelector(self, value: ISurrogateSelector) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Deserialize(self, serializationStream: Stream) -> ObjectType: ...
    
    def Serialize(self, serializationStream: Stream, graph: ObjectType) -> VoidType: ...
    
    def get_Binder(self) -> SerializationBinder: ...
    
    def get_Context(self) -> StreamingContext: ...
    
    def get_SurrogateSelector(self) -> ISurrogateSelector: ...
    
    def set_Binder(self, value: SerializationBinder) -> VoidType: ...
    
    def set_Context(self, value: StreamingContext) -> VoidType: ...
    
    def set_SurrogateSelector(self, value: ISurrogateSelector) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Formatter(ABC, ObjectType, IFormatter):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Binder(self) -> SerializationBinder: ...
    
    @Binder.setter
    def Binder(self, value: SerializationBinder) -> None: ...
    
    @property
    def Context(self) -> StreamingContext: ...
    
    @Context.setter
    def Context(self, value: StreamingContext) -> None: ...
    
    @property
    def SurrogateSelector(self) -> ISurrogateSelector: ...
    
    @SurrogateSelector.setter
    def SurrogateSelector(self, value: ISurrogateSelector) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Deserialize(self, serializationStream: Stream) -> ObjectType: ...
    
    def Serialize(self, serializationStream: Stream, graph: ObjectType) -> VoidType: ...
    
    def get_Binder(self) -> SerializationBinder: ...
    
    def get_Context(self) -> StreamingContext: ...
    
    def get_SurrogateSelector(self) -> ISurrogateSelector: ...
    
    def set_Binder(self, value: SerializationBinder) -> VoidType: ...
    
    def set_Context(self, value: StreamingContext) -> VoidType: ...
    
    def set_SurrogateSelector(self, value: ISurrogateSelector) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class FormatterConverter(ObjectType, IFormatterConverter):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def Convert(self, value: ObjectType, type: TypeType) -> ObjectType: ...
    
    @overload
    def Convert(self, value: ObjectType, typeCode: TypeCode) -> ObjectType: ...
    
    def ToBoolean(self, value: ObjectType) -> BooleanType: ...
    
    def ToByte(self, value: ObjectType) -> ByteType: ...
    
    def ToChar(self, value: ObjectType) -> CharType: ...
    
    def ToDateTime(self, value: ObjectType) -> DateTime: ...
    
    def ToDecimal(self, value: ObjectType) -> DecimalType: ...
    
    def ToDouble(self, value: ObjectType) -> DoubleType: ...
    
    def ToInt16(self, value: ObjectType) -> ShortType: ...
    
    def ToInt32(self, value: ObjectType) -> IntType: ...
    
    def ToInt64(self, value: ObjectType) -> LongType: ...
    
    def ToSByte(self, value: ObjectType) -> SByteType: ...
    
    def ToSingle(self, value: ObjectType) -> FloatType: ...
    
    @overload
    def ToString(self, value: ObjectType) -> StringType: ...
    
    def ToUInt16(self, value: ObjectType) -> UShortType: ...
    
    def ToUInt32(self, value: ObjectType) -> UIntType: ...
    
    def ToUInt64(self, value: ObjectType) -> ULongType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class FormatterConverter(ObjectType, IFormatterConverter):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def Convert(self, value: ObjectType, type: TypeType) -> ObjectType: ...
    
    @overload
    def Convert(self, value: ObjectType, typeCode: TypeCode) -> ObjectType: ...
    
    def ToBoolean(self, value: ObjectType) -> BooleanType: ...
    
    def ToByte(self, value: ObjectType) -> ByteType: ...
    
    def ToChar(self, value: ObjectType) -> CharType: ...
    
    def ToDateTime(self, value: ObjectType) -> DateTime: ...
    
    def ToDecimal(self, value: ObjectType) -> DecimalType: ...
    
    def ToDouble(self, value: ObjectType) -> DoubleType: ...
    
    def ToInt16(self, value: ObjectType) -> ShortType: ...
    
    def ToInt32(self, value: ObjectType) -> IntType: ...
    
    def ToInt64(self, value: ObjectType) -> LongType: ...
    
    def ToSByte(self, value: ObjectType) -> SByteType: ...
    
    def ToSingle(self, value: ObjectType) -> FloatType: ...
    
    @overload
    def ToString(self, value: ObjectType) -> StringType: ...
    
    def ToUInt16(self, value: ObjectType) -> UShortType: ...
    
    def ToUInt32(self, value: ObjectType) -> UIntType: ...
    
    def ToUInt64(self, value: ObjectType) -> ULongType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class FormatterConverter(ObjectType, IFormatterConverter):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def Convert(self, value: ObjectType, type: TypeType) -> ObjectType: ...
    
    @overload
    def Convert(self, value: ObjectType, typeCode: TypeCode) -> ObjectType: ...
    
    def ToBoolean(self, value: ObjectType) -> BooleanType: ...
    
    def ToByte(self, value: ObjectType) -> ByteType: ...
    
    def ToChar(self, value: ObjectType) -> CharType: ...
    
    def ToDateTime(self, value: ObjectType) -> DateTime: ...
    
    def ToDecimal(self, value: ObjectType) -> DecimalType: ...
    
    def ToDouble(self, value: ObjectType) -> DoubleType: ...
    
    def ToInt16(self, value: ObjectType) -> ShortType: ...
    
    def ToInt32(self, value: ObjectType) -> IntType: ...
    
    def ToInt64(self, value: ObjectType) -> LongType: ...
    
    def ToSByte(self, value: ObjectType) -> SByteType: ...
    
    def ToSingle(self, value: ObjectType) -> FloatType: ...
    
    @overload
    def ToString(self, value: ObjectType) -> StringType: ...
    
    def ToUInt16(self, value: ObjectType) -> UShortType: ...
    
    def ToUInt32(self, value: ObjectType) -> UIntType: ...
    
    def ToUInt64(self, value: ObjectType) -> ULongType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class FormatterServices(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def CheckTypeSecurity(t: TypeType, securityLevel: TypeFilterLevel) -> VoidType: ...
    
    @staticmethod
    def GetObjectData(obj: ObjectType, members: ArrayType[MemberInfo]) -> ArrayType[ObjectType]: ...
    
    @staticmethod
    def GetSafeUninitializedObject(type: TypeType) -> ObjectType: ...
    
    @staticmethod
    @overload
    def GetSerializableMembers(type: TypeType, context: StreamingContext) -> ArrayType[MemberInfo]: ...
    
    @staticmethod
    @overload
    def GetSerializableMembers(type: TypeType) -> ArrayType[MemberInfo]: ...
    
    @staticmethod
    def GetSurrogateForCyclicalReference(innerSurrogate: ISerializationSurrogate) -> ISerializationSurrogate: ...
    
    @staticmethod
    def GetTypeFromAssembly(assem: Assembly, name: StringType) -> TypeType: ...
    
    @staticmethod
    def GetUninitializedObject(type: TypeType) -> ObjectType: ...
    
    @staticmethod
    def PopulateObjectMembers(obj: ObjectType, members: ArrayType[MemberInfo], data: ArrayType[ObjectType]) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class FormatterServices(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def CheckTypeSecurity(t: TypeType, securityLevel: TypeFilterLevel) -> VoidType: ...
    
    @staticmethod
    def GetObjectData(obj: ObjectType, members: ArrayType[MemberInfo]) -> ArrayType[ObjectType]: ...
    
    @staticmethod
    def GetSafeUninitializedObject(type: TypeType) -> ObjectType: ...
    
    @staticmethod
    @overload
    def GetSerializableMembers(type: TypeType, context: StreamingContext) -> ArrayType[MemberInfo]: ...
    
    @staticmethod
    @overload
    def GetSerializableMembers(type: TypeType) -> ArrayType[MemberInfo]: ...
    
    @staticmethod
    def GetSurrogateForCyclicalReference(innerSurrogate: ISerializationSurrogate) -> ISerializationSurrogate: ...
    
    @staticmethod
    def GetTypeFromAssembly(assem: Assembly, name: StringType) -> TypeType: ...
    
    @staticmethod
    def GetUninitializedObject(type: TypeType) -> ObjectType: ...
    
    @staticmethod
    def PopulateObjectMembers(obj: ObjectType, members: ArrayType[MemberInfo], data: ArrayType[ObjectType]) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class FormatterServices(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def CheckTypeSecurity(t: TypeType, securityLevel: TypeFilterLevel) -> VoidType: ...
    
    @staticmethod
    def GetObjectData(obj: ObjectType, members: ArrayType[MemberInfo]) -> ArrayType[ObjectType]: ...
    
    @staticmethod
    def GetSafeUninitializedObject(type: TypeType) -> ObjectType: ...
    
    @staticmethod
    @overload
    def GetSerializableMembers(type: TypeType, context: StreamingContext) -> ArrayType[MemberInfo]: ...
    
    @staticmethod
    @overload
    def GetSerializableMembers(type: TypeType) -> ArrayType[MemberInfo]: ...
    
    @staticmethod
    def GetSurrogateForCyclicalReference(innerSurrogate: ISerializationSurrogate) -> ISerializationSurrogate: ...
    
    @staticmethod
    def GetTypeFromAssembly(assem: Assembly, name: StringType) -> TypeType: ...
    
    @staticmethod
    def GetUninitializedObject(type: TypeType) -> ObjectType: ...
    
    @staticmethod
    def PopulateObjectMembers(obj: ObjectType, members: ArrayType[MemberInfo], data: ArrayType[ObjectType]) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class LongList(ObjectType):
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


class LongList(ObjectType):
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


class LongList(ObjectType):
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


class MemberHolder(ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MemberHolder(ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MemberHolder(ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ObjectCloneHelper(ABC, ObjectType):
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


class ObjectCloneHelper(ABC, ObjectType):
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


class ObjectCloneHelper(ABC, ObjectType):
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


class ObjectHolder(ObjectType):
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


class ObjectHolder(ObjectType):
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


class ObjectHolder(ObjectType):
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


class ObjectHolderList(ObjectType):
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


class ObjectHolderList(ObjectType):
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


class ObjectHolderList(ObjectType):
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


class ObjectHolderListEnumerator(ObjectType):
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


class ObjectHolderListEnumerator(ObjectType):
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


class ObjectHolderListEnumerator(ObjectType):
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


class ObjectIDGenerator(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetId(self, obj: ObjectType, firstTime: BooleanType) -> Tuple[LongType, BooleanType]: ...
    
    def HasId(self, obj: ObjectType, firstTime: BooleanType) -> Tuple[LongType, BooleanType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ObjectIDGenerator(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetId(self, obj: ObjectType, firstTime: BooleanType) -> Tuple[LongType, BooleanType]: ...
    
    def HasId(self, obj: ObjectType, firstTime: BooleanType) -> Tuple[LongType, BooleanType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ObjectIDGenerator(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetId(self, obj: ObjectType, firstTime: BooleanType) -> Tuple[LongType, BooleanType]: ...
    
    def HasId(self, obj: ObjectType, firstTime: BooleanType) -> Tuple[LongType, BooleanType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ObjectManager(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, selector: ISurrogateSelector, context: StreamingContext): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def DoFixups(self) -> VoidType: ...
    
    def GetObject(self, objectID: LongType) -> ObjectType: ...
    
    def RaiseDeserializationEvent(self) -> VoidType: ...
    
    def RaiseOnDeserializingEvent(self, obj: ObjectType) -> VoidType: ...
    
    @overload
    def RecordArrayElementFixup(self, arrayToBeFixed: LongType, indices: ArrayType[IntType], objectRequired: LongType) -> VoidType: ...
    
    @overload
    def RecordArrayElementFixup(self, arrayToBeFixed: LongType, index: IntType, objectRequired: LongType) -> VoidType: ...
    
    def RecordDelayedFixup(self, objectToBeFixed: LongType, memberName: StringType, objectRequired: LongType) -> VoidType: ...
    
    def RecordFixup(self, objectToBeFixed: LongType, member: MemberInfo, objectRequired: LongType) -> VoidType: ...
    
    @overload
    def RegisterObject(self, obj: ObjectType, objectID: LongType) -> VoidType: ...
    
    @overload
    def RegisterObject(self, obj: ObjectType, objectID: LongType, info: SerializationInfo) -> VoidType: ...
    
    @overload
    def RegisterObject(self, obj: ObjectType, objectID: LongType, info: SerializationInfo, idOfContainingObj: LongType, member: MemberInfo) -> VoidType: ...
    
    @overload
    def RegisterObject(self, obj: ObjectType, objectID: LongType, info: SerializationInfo, idOfContainingObj: LongType, member: MemberInfo, arrayIndex: ArrayType[IntType]) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ObjectManager(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, selector: ISurrogateSelector, context: StreamingContext): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def DoFixups(self) -> VoidType: ...
    
    def GetObject(self, objectID: LongType) -> ObjectType: ...
    
    def RaiseDeserializationEvent(self) -> VoidType: ...
    
    def RaiseOnDeserializingEvent(self, obj: ObjectType) -> VoidType: ...
    
    @overload
    def RecordArrayElementFixup(self, arrayToBeFixed: LongType, indices: ArrayType[IntType], objectRequired: LongType) -> VoidType: ...
    
    @overload
    def RecordArrayElementFixup(self, arrayToBeFixed: LongType, index: IntType, objectRequired: LongType) -> VoidType: ...
    
    def RecordDelayedFixup(self, objectToBeFixed: LongType, memberName: StringType, objectRequired: LongType) -> VoidType: ...
    
    def RecordFixup(self, objectToBeFixed: LongType, member: MemberInfo, objectRequired: LongType) -> VoidType: ...
    
    @overload
    def RegisterObject(self, obj: ObjectType, objectID: LongType) -> VoidType: ...
    
    @overload
    def RegisterObject(self, obj: ObjectType, objectID: LongType, info: SerializationInfo) -> VoidType: ...
    
    @overload
    def RegisterObject(self, obj: ObjectType, objectID: LongType, info: SerializationInfo, idOfContainingObj: LongType, member: MemberInfo) -> VoidType: ...
    
    @overload
    def RegisterObject(self, obj: ObjectType, objectID: LongType, info: SerializationInfo, idOfContainingObj: LongType, member: MemberInfo, arrayIndex: ArrayType[IntType]) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ObjectManager(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, selector: ISurrogateSelector, context: StreamingContext): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def DoFixups(self) -> VoidType: ...
    
    def GetObject(self, objectID: LongType) -> ObjectType: ...
    
    def RaiseDeserializationEvent(self) -> VoidType: ...
    
    def RaiseOnDeserializingEvent(self, obj: ObjectType) -> VoidType: ...
    
    @overload
    def RecordArrayElementFixup(self, arrayToBeFixed: LongType, indices: ArrayType[IntType], objectRequired: LongType) -> VoidType: ...
    
    @overload
    def RecordArrayElementFixup(self, arrayToBeFixed: LongType, index: IntType, objectRequired: LongType) -> VoidType: ...
    
    def RecordDelayedFixup(self, objectToBeFixed: LongType, memberName: StringType, objectRequired: LongType) -> VoidType: ...
    
    def RecordFixup(self, objectToBeFixed: LongType, member: MemberInfo, objectRequired: LongType) -> VoidType: ...
    
    @overload
    def RegisterObject(self, obj: ObjectType, objectID: LongType) -> VoidType: ...
    
    @overload
    def RegisterObject(self, obj: ObjectType, objectID: LongType, info: SerializationInfo) -> VoidType: ...
    
    @overload
    def RegisterObject(self, obj: ObjectType, objectID: LongType, info: SerializationInfo, idOfContainingObj: LongType, member: MemberInfo) -> VoidType: ...
    
    @overload
    def RegisterObject(self, obj: ObjectType, objectID: LongType, info: SerializationInfo, idOfContainingObj: LongType, member: MemberInfo, arrayIndex: ArrayType[IntType]) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class OnDeserializedAttribute(Attribute, _Attribute):
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


class OnDeserializedAttribute(Attribute, _Attribute):
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


class OnDeserializedAttribute(Attribute, _Attribute):
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


class OnDeserializingAttribute(Attribute, _Attribute):
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


class OnDeserializingAttribute(Attribute, _Attribute):
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


class OnDeserializingAttribute(Attribute, _Attribute):
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


class OnSerializedAttribute(Attribute, _Attribute):
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


class OnSerializedAttribute(Attribute, _Attribute):
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


class OnSerializedAttribute(Attribute, _Attribute):
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


class OnSerializingAttribute(Attribute, _Attribute):
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


class OnSerializingAttribute(Attribute, _Attribute):
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


class OnSerializingAttribute(Attribute, _Attribute):
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


class OptionalFieldAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def VersionAdded(self) -> IntType: ...
    
    @VersionAdded.setter
    def VersionAdded(self, value: IntType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_VersionAdded(self) -> IntType: ...
    
    def set_VersionAdded(self, value: IntType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class OptionalFieldAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def VersionAdded(self) -> IntType: ...
    
    @VersionAdded.setter
    def VersionAdded(self, value: IntType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_VersionAdded(self) -> IntType: ...
    
    def set_VersionAdded(self, value: IntType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class OptionalFieldAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def VersionAdded(self) -> IntType: ...
    
    @VersionAdded.setter
    def VersionAdded(self, value: IntType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_VersionAdded(self) -> IntType: ...
    
    def set_VersionAdded(self, value: IntType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SafeSerializationEventArgs(EventArgs):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def StreamingContext(self) -> StreamingContext: ...
    
    # ---------- Methods ---------- #
    
    def AddSerializedState(self, serializedState: ISafeSerializationData) -> VoidType: ...
    
    def get_StreamingContext(self) -> StreamingContext: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SafeSerializationEventArgs(EventArgs):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def StreamingContext(self) -> StreamingContext: ...
    
    # ---------- Methods ---------- #
    
    def AddSerializedState(self, serializedState: ISafeSerializationData) -> VoidType: ...
    
    def get_StreamingContext(self) -> StreamingContext: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SafeSerializationEventArgs(EventArgs):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def StreamingContext(self) -> StreamingContext: ...
    
    # ---------- Methods ---------- #
    
    def AddSerializedState(self, serializedState: ISafeSerializationData) -> VoidType: ...
    
    def get_StreamingContext(self) -> StreamingContext: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SafeSerializationManager(ObjectType, IObjectReference, ISerializable):
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


class SafeSerializationManager(ObjectType, IObjectReference, ISerializable):
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


class SafeSerializationManager(ObjectType, IObjectReference, ISerializable):
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


class SerializationBinder(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BindToName(self, serializedType: TypeType, assemblyName: StringType, typeName: StringType) -> Tuple[VoidType, StringType, StringType]: ...
    
    def BindToType(self, assemblyName: StringType, typeName: StringType) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SerializationBinder(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BindToName(self, serializedType: TypeType, assemblyName: StringType, typeName: StringType) -> Tuple[VoidType, StringType, StringType]: ...
    
    def BindToType(self, assemblyName: StringType, typeName: StringType) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SerializationBinder(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BindToName(self, serializedType: TypeType, assemblyName: StringType, typeName: StringType) -> Tuple[VoidType, StringType, StringType]: ...
    
    def BindToType(self, assemblyName: StringType, typeName: StringType) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SerializationEventHandler(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, context: StreamingContext, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, context: StreamingContext) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SerializationEventHandler(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, context: StreamingContext, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, context: StreamingContext) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SerializationEventHandler(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, context: StreamingContext, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, context: StreamingContext) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SerializationEvents(ObjectType):
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


class SerializationEvents(ObjectType):
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


class SerializationEvents(ObjectType):
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


class SerializationEventsCache(ABC, ObjectType):
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


class SerializationEventsCache(ABC, ObjectType):
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


class SerializationEventsCache(ABC, ObjectType):
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


class SerializationException(SystemException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SerializationException(SystemException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SerializationException(SystemException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SerializationFieldInfo(FieldInfo, ICustomAttributeProvider, _MemberInfo, _FieldInfo):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Attributes(self) -> FieldAttributes: ...
    
    @property
    def DeclaringType(self) -> TypeType: ...
    
    @property
    def FieldHandle(self) -> RuntimeFieldHandle: ...
    
    @property
    def FieldType(self) -> TypeType: ...
    
    @property
    def MetadataToken(self) -> IntType: ...
    
    @property
    def Module(self) -> Module: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def ReflectedType(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def GetCustomAttributes(self, inherit: BooleanType) -> ArrayType[ObjectType]: ...
    
    @overload
    def GetCustomAttributes(self, attributeType: TypeType, inherit: BooleanType) -> ArrayType[ObjectType]: ...
    
    def GetValue(self, obj: ObjectType) -> ObjectType: ...
    
    def IsDefined(self, attributeType: TypeType, inherit: BooleanType) -> BooleanType: ...
    
    @overload
    def SetValue(self, obj: ObjectType, value: ObjectType, invokeAttr: BindingFlags, binder: Binder, culture: CultureInfo) -> VoidType: ...
    
    def get_Attributes(self) -> FieldAttributes: ...
    
    def get_DeclaringType(self) -> TypeType: ...
    
    def get_FieldHandle(self) -> RuntimeFieldHandle: ...
    
    def get_FieldType(self) -> TypeType: ...
    
    def get_MetadataToken(self) -> IntType: ...
    
    def get_Module(self) -> Module: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_ReflectedType(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SerializationFieldInfo(FieldInfo, ICustomAttributeProvider, _MemberInfo, _FieldInfo):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Attributes(self) -> FieldAttributes: ...
    
    @property
    def DeclaringType(self) -> TypeType: ...
    
    @property
    def FieldHandle(self) -> RuntimeFieldHandle: ...
    
    @property
    def FieldType(self) -> TypeType: ...
    
    @property
    def MetadataToken(self) -> IntType: ...
    
    @property
    def Module(self) -> Module: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def ReflectedType(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def GetCustomAttributes(self, inherit: BooleanType) -> ArrayType[ObjectType]: ...
    
    @overload
    def GetCustomAttributes(self, attributeType: TypeType, inherit: BooleanType) -> ArrayType[ObjectType]: ...
    
    def GetValue(self, obj: ObjectType) -> ObjectType: ...
    
    def IsDefined(self, attributeType: TypeType, inherit: BooleanType) -> BooleanType: ...
    
    @overload
    def SetValue(self, obj: ObjectType, value: ObjectType, invokeAttr: BindingFlags, binder: Binder, culture: CultureInfo) -> VoidType: ...
    
    def get_Attributes(self) -> FieldAttributes: ...
    
    def get_DeclaringType(self) -> TypeType: ...
    
    def get_FieldHandle(self) -> RuntimeFieldHandle: ...
    
    def get_FieldType(self) -> TypeType: ...
    
    def get_MetadataToken(self) -> IntType: ...
    
    def get_Module(self) -> Module: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_ReflectedType(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SerializationFieldInfo(FieldInfo, ICustomAttributeProvider, _MemberInfo, _FieldInfo):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Attributes(self) -> FieldAttributes: ...
    
    @property
    def DeclaringType(self) -> TypeType: ...
    
    @property
    def FieldHandle(self) -> RuntimeFieldHandle: ...
    
    @property
    def FieldType(self) -> TypeType: ...
    
    @property
    def MetadataToken(self) -> IntType: ...
    
    @property
    def Module(self) -> Module: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def ReflectedType(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def GetCustomAttributes(self, inherit: BooleanType) -> ArrayType[ObjectType]: ...
    
    @overload
    def GetCustomAttributes(self, attributeType: TypeType, inherit: BooleanType) -> ArrayType[ObjectType]: ...
    
    def GetValue(self, obj: ObjectType) -> ObjectType: ...
    
    def IsDefined(self, attributeType: TypeType, inherit: BooleanType) -> BooleanType: ...
    
    @overload
    def SetValue(self, obj: ObjectType, value: ObjectType, invokeAttr: BindingFlags, binder: Binder, culture: CultureInfo) -> VoidType: ...
    
    def get_Attributes(self) -> FieldAttributes: ...
    
    def get_DeclaringType(self) -> TypeType: ...
    
    def get_FieldHandle(self) -> RuntimeFieldHandle: ...
    
    def get_FieldType(self) -> TypeType: ...
    
    def get_MetadataToken(self) -> IntType: ...
    
    def get_Module(self) -> Module: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_ReflectedType(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SerializationInfo(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, type: TypeType, converter: IFormatterConverter): ...
    
    @overload
    def __init__(self, type: TypeType, converter: IFormatterConverter, requireSameTokenInPartialTrust: BooleanType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AssemblyName(self) -> StringType: ...
    
    @AssemblyName.setter
    def AssemblyName(self, value: StringType) -> None: ...
    
    @property
    def FullTypeName(self) -> StringType: ...
    
    @FullTypeName.setter
    def FullTypeName(self, value: StringType) -> None: ...
    
    @property
    def IsAssemblyNameSetExplicit(self) -> BooleanType: ...
    
    @property
    def IsFullTypeNameSetExplicit(self) -> BooleanType: ...
    
    @property
    def MemberCount(self) -> IntType: ...
    
    @property
    def ObjectType(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def AddValue(self, name: StringType, value: ObjectType, type: TypeType) -> VoidType: ...
    
    @overload
    def AddValue(self, name: StringType, value: ObjectType) -> VoidType: ...
    
    @overload
    def AddValue(self, name: StringType, value: BooleanType) -> VoidType: ...
    
    @overload
    def AddValue(self, name: StringType, value: CharType) -> VoidType: ...
    
    @overload
    def AddValue(self, name: StringType, value: SByteType) -> VoidType: ...
    
    @overload
    def AddValue(self, name: StringType, value: ByteType) -> VoidType: ...
    
    @overload
    def AddValue(self, name: StringType, value: ShortType) -> VoidType: ...
    
    @overload
    def AddValue(self, name: StringType, value: UShortType) -> VoidType: ...
    
    @overload
    def AddValue(self, name: StringType, value: IntType) -> VoidType: ...
    
    @overload
    def AddValue(self, name: StringType, value: UIntType) -> VoidType: ...
    
    @overload
    def AddValue(self, name: StringType, value: LongType) -> VoidType: ...
    
    @overload
    def AddValue(self, name: StringType, value: ULongType) -> VoidType: ...
    
    @overload
    def AddValue(self, name: StringType, value: FloatType) -> VoidType: ...
    
    @overload
    def AddValue(self, name: StringType, value: DoubleType) -> VoidType: ...
    
    @overload
    def AddValue(self, name: StringType, value: DecimalType) -> VoidType: ...
    
    @overload
    def AddValue(self, name: StringType, value: DateTime) -> VoidType: ...
    
    def GetBoolean(self, name: StringType) -> BooleanType: ...
    
    def GetByte(self, name: StringType) -> ByteType: ...
    
    def GetChar(self, name: StringType) -> CharType: ...
    
    def GetDateTime(self, name: StringType) -> DateTime: ...
    
    def GetDecimal(self, name: StringType) -> DecimalType: ...
    
    def GetDouble(self, name: StringType) -> DoubleType: ...
    
    def GetEnumerator(self) -> SerializationInfoEnumerator: ...
    
    def GetInt16(self, name: StringType) -> ShortType: ...
    
    def GetInt32(self, name: StringType) -> IntType: ...
    
    def GetInt64(self, name: StringType) -> LongType: ...
    
    def GetSByte(self, name: StringType) -> SByteType: ...
    
    def GetSingle(self, name: StringType) -> FloatType: ...
    
    def GetString(self, name: StringType) -> StringType: ...
    
    def GetUInt16(self, name: StringType) -> UShortType: ...
    
    def GetUInt32(self, name: StringType) -> UIntType: ...
    
    def GetUInt64(self, name: StringType) -> ULongType: ...
    
    def GetValue(self, name: StringType, type: TypeType) -> ObjectType: ...
    
    def SetType(self, type: TypeType) -> VoidType: ...
    
    def get_AssemblyName(self) -> StringType: ...
    
    def get_FullTypeName(self) -> StringType: ...
    
    def get_IsAssemblyNameSetExplicit(self) -> BooleanType: ...
    
    def get_IsFullTypeNameSetExplicit(self) -> BooleanType: ...
    
    def get_MemberCount(self) -> IntType: ...
    
    def get_ObjectType(self) -> TypeType: ...
    
    def set_AssemblyName(self, value: StringType) -> VoidType: ...
    
    def set_FullTypeName(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SerializationInfo(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, type: TypeType, converter: IFormatterConverter): ...
    
    @overload
    def __init__(self, type: TypeType, converter: IFormatterConverter, requireSameTokenInPartialTrust: BooleanType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AssemblyName(self) -> StringType: ...
    
    @AssemblyName.setter
    def AssemblyName(self, value: StringType) -> None: ...
    
    @property
    def FullTypeName(self) -> StringType: ...
    
    @FullTypeName.setter
    def FullTypeName(self, value: StringType) -> None: ...
    
    @property
    def IsAssemblyNameSetExplicit(self) -> BooleanType: ...
    
    @property
    def IsFullTypeNameSetExplicit(self) -> BooleanType: ...
    
    @property
    def MemberCount(self) -> IntType: ...
    
    @property
    def ObjectType(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def AddValue(self, name: StringType, value: ObjectType, type: TypeType) -> VoidType: ...
    
    @overload
    def AddValue(self, name: StringType, value: ObjectType) -> VoidType: ...
    
    @overload
    def AddValue(self, name: StringType, value: BooleanType) -> VoidType: ...
    
    @overload
    def AddValue(self, name: StringType, value: CharType) -> VoidType: ...
    
    @overload
    def AddValue(self, name: StringType, value: SByteType) -> VoidType: ...
    
    @overload
    def AddValue(self, name: StringType, value: ByteType) -> VoidType: ...
    
    @overload
    def AddValue(self, name: StringType, value: ShortType) -> VoidType: ...
    
    @overload
    def AddValue(self, name: StringType, value: UShortType) -> VoidType: ...
    
    @overload
    def AddValue(self, name: StringType, value: IntType) -> VoidType: ...
    
    @overload
    def AddValue(self, name: StringType, value: UIntType) -> VoidType: ...
    
    @overload
    def AddValue(self, name: StringType, value: LongType) -> VoidType: ...
    
    @overload
    def AddValue(self, name: StringType, value: ULongType) -> VoidType: ...
    
    @overload
    def AddValue(self, name: StringType, value: FloatType) -> VoidType: ...
    
    @overload
    def AddValue(self, name: StringType, value: DoubleType) -> VoidType: ...
    
    @overload
    def AddValue(self, name: StringType, value: DecimalType) -> VoidType: ...
    
    @overload
    def AddValue(self, name: StringType, value: DateTime) -> VoidType: ...
    
    def GetBoolean(self, name: StringType) -> BooleanType: ...
    
    def GetByte(self, name: StringType) -> ByteType: ...
    
    def GetChar(self, name: StringType) -> CharType: ...
    
    def GetDateTime(self, name: StringType) -> DateTime: ...
    
    def GetDecimal(self, name: StringType) -> DecimalType: ...
    
    def GetDouble(self, name: StringType) -> DoubleType: ...
    
    def GetEnumerator(self) -> SerializationInfoEnumerator: ...
    
    def GetInt16(self, name: StringType) -> ShortType: ...
    
    def GetInt32(self, name: StringType) -> IntType: ...
    
    def GetInt64(self, name: StringType) -> LongType: ...
    
    def GetSByte(self, name: StringType) -> SByteType: ...
    
    def GetSingle(self, name: StringType) -> FloatType: ...
    
    def GetString(self, name: StringType) -> StringType: ...
    
    def GetUInt16(self, name: StringType) -> UShortType: ...
    
    def GetUInt32(self, name: StringType) -> UIntType: ...
    
    def GetUInt64(self, name: StringType) -> ULongType: ...
    
    def GetValue(self, name: StringType, type: TypeType) -> ObjectType: ...
    
    def SetType(self, type: TypeType) -> VoidType: ...
    
    def get_AssemblyName(self) -> StringType: ...
    
    def get_FullTypeName(self) -> StringType: ...
    
    def get_IsAssemblyNameSetExplicit(self) -> BooleanType: ...
    
    def get_IsFullTypeNameSetExplicit(self) -> BooleanType: ...
    
    def get_MemberCount(self) -> IntType: ...
    
    def get_ObjectType(self) -> TypeType: ...
    
    def set_AssemblyName(self, value: StringType) -> VoidType: ...
    
    def set_FullTypeName(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SerializationInfo(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, type: TypeType, converter: IFormatterConverter): ...
    
    @overload
    def __init__(self, type: TypeType, converter: IFormatterConverter, requireSameTokenInPartialTrust: BooleanType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AssemblyName(self) -> StringType: ...
    
    @AssemblyName.setter
    def AssemblyName(self, value: StringType) -> None: ...
    
    @property
    def FullTypeName(self) -> StringType: ...
    
    @FullTypeName.setter
    def FullTypeName(self, value: StringType) -> None: ...
    
    @property
    def IsAssemblyNameSetExplicit(self) -> BooleanType: ...
    
    @property
    def IsFullTypeNameSetExplicit(self) -> BooleanType: ...
    
    @property
    def MemberCount(self) -> IntType: ...
    
    @property
    def ObjectType(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def AddValue(self, name: StringType, value: ObjectType, type: TypeType) -> VoidType: ...
    
    @overload
    def AddValue(self, name: StringType, value: ObjectType) -> VoidType: ...
    
    @overload
    def AddValue(self, name: StringType, value: BooleanType) -> VoidType: ...
    
    @overload
    def AddValue(self, name: StringType, value: CharType) -> VoidType: ...
    
    @overload
    def AddValue(self, name: StringType, value: SByteType) -> VoidType: ...
    
    @overload
    def AddValue(self, name: StringType, value: ByteType) -> VoidType: ...
    
    @overload
    def AddValue(self, name: StringType, value: ShortType) -> VoidType: ...
    
    @overload
    def AddValue(self, name: StringType, value: UShortType) -> VoidType: ...
    
    @overload
    def AddValue(self, name: StringType, value: IntType) -> VoidType: ...
    
    @overload
    def AddValue(self, name: StringType, value: UIntType) -> VoidType: ...
    
    @overload
    def AddValue(self, name: StringType, value: LongType) -> VoidType: ...
    
    @overload
    def AddValue(self, name: StringType, value: ULongType) -> VoidType: ...
    
    @overload
    def AddValue(self, name: StringType, value: FloatType) -> VoidType: ...
    
    @overload
    def AddValue(self, name: StringType, value: DoubleType) -> VoidType: ...
    
    @overload
    def AddValue(self, name: StringType, value: DecimalType) -> VoidType: ...
    
    @overload
    def AddValue(self, name: StringType, value: DateTime) -> VoidType: ...
    
    def GetBoolean(self, name: StringType) -> BooleanType: ...
    
    def GetByte(self, name: StringType) -> ByteType: ...
    
    def GetChar(self, name: StringType) -> CharType: ...
    
    def GetDateTime(self, name: StringType) -> DateTime: ...
    
    def GetDecimal(self, name: StringType) -> DecimalType: ...
    
    def GetDouble(self, name: StringType) -> DoubleType: ...
    
    def GetEnumerator(self) -> SerializationInfoEnumerator: ...
    
    def GetInt16(self, name: StringType) -> ShortType: ...
    
    def GetInt32(self, name: StringType) -> IntType: ...
    
    def GetInt64(self, name: StringType) -> LongType: ...
    
    def GetSByte(self, name: StringType) -> SByteType: ...
    
    def GetSingle(self, name: StringType) -> FloatType: ...
    
    def GetString(self, name: StringType) -> StringType: ...
    
    def GetUInt16(self, name: StringType) -> UShortType: ...
    
    def GetUInt32(self, name: StringType) -> UIntType: ...
    
    def GetUInt64(self, name: StringType) -> ULongType: ...
    
    def GetValue(self, name: StringType, type: TypeType) -> ObjectType: ...
    
    def SetType(self, type: TypeType) -> VoidType: ...
    
    def get_AssemblyName(self) -> StringType: ...
    
    def get_FullTypeName(self) -> StringType: ...
    
    def get_IsAssemblyNameSetExplicit(self) -> BooleanType: ...
    
    def get_IsFullTypeNameSetExplicit(self) -> BooleanType: ...
    
    def get_MemberCount(self) -> IntType: ...
    
    def get_ObjectType(self) -> TypeType: ...
    
    def set_AssemblyName(self, value: StringType) -> VoidType: ...
    
    def set_FullTypeName(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SerializationInfoEnumerator(ObjectType, IEnumerator):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Current(self) -> SerializationEntry: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def ObjectType(self) -> TypeType: ...
    
    @property
    def Value(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def MoveNext(self) -> BooleanType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Current(self) -> SerializationEntry: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_ObjectType(self) -> TypeType: ...
    
    def get_Value(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SerializationInfoEnumerator(ObjectType, IEnumerator):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Current(self) -> SerializationEntry: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def ObjectType(self) -> TypeType: ...
    
    @property
    def Value(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def MoveNext(self) -> BooleanType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Current(self) -> SerializationEntry: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_ObjectType(self) -> TypeType: ...
    
    def get_Value(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SerializationInfoEnumerator(ObjectType, IEnumerator):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Current(self) -> SerializationEntry: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def ObjectType(self) -> TypeType: ...
    
    @property
    def Value(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def MoveNext(self) -> BooleanType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Current(self) -> SerializationEntry: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_ObjectType(self) -> TypeType: ...
    
    def get_Value(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SerializationObjectManager(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, context: StreamingContext): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def RaiseOnSerializedEvent(self) -> VoidType: ...
    
    def RegisterObject(self, obj: ObjectType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SerializationObjectManager(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, context: StreamingContext): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def RaiseOnSerializedEvent(self) -> VoidType: ...
    
    def RegisterObject(self, obj: ObjectType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SerializationObjectManager(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, context: StreamingContext): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def RaiseOnSerializedEvent(self) -> VoidType: ...
    
    def RegisterObject(self, obj: ObjectType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SurrogateForCyclicalReference(ObjectType, ISerializationSurrogate):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetObjectData(self, obj: ObjectType, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    
    def SetObjectData(self, obj: ObjectType, info: SerializationInfo, context: StreamingContext, selector: ISurrogateSelector) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SurrogateForCyclicalReference(ObjectType, ISerializationSurrogate):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetObjectData(self, obj: ObjectType, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    
    def SetObjectData(self, obj: ObjectType, info: SerializationInfo, context: StreamingContext, selector: ISurrogateSelector) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SurrogateForCyclicalReference(ObjectType, ISerializationSurrogate):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetObjectData(self, obj: ObjectType, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    
    def SetObjectData(self, obj: ObjectType, info: SerializationInfo, context: StreamingContext, selector: ISurrogateSelector) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SurrogateHashtable(Hashtable, IDictionary, ICollection, IEnumerable, ISerializable, IDeserializationCallback, ICloneable):
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


class SurrogateHashtable(Hashtable, IDictionary, ICollection, IEnumerable, ISerializable, IDeserializationCallback, ICloneable):
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


class SurrogateHashtable(Hashtable, IDictionary, ICollection, IEnumerable, ISerializable, IDeserializationCallback, ICloneable):
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


class SurrogateKey(ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetHashCode(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SurrogateKey(ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetHashCode(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SurrogateKey(ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetHashCode(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SurrogateSelector(ObjectType, ISurrogateSelector):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def AddSurrogate(self, type: TypeType, context: StreamingContext, surrogate: ISerializationSurrogate) -> VoidType: ...
    
    def ChainSelector(self, selector: ISurrogateSelector) -> VoidType: ...
    
    def GetNextSelector(self) -> ISurrogateSelector: ...
    
    def GetSurrogate(self, type: TypeType, context: StreamingContext, selector: ISurrogateSelector) -> Tuple[ISerializationSurrogate, ISurrogateSelector]: ...
    
    def RemoveSurrogate(self, type: TypeType, context: StreamingContext) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SurrogateSelector(ObjectType, ISurrogateSelector):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def AddSurrogate(self, type: TypeType, context: StreamingContext, surrogate: ISerializationSurrogate) -> VoidType: ...
    
    def ChainSelector(self, selector: ISurrogateSelector) -> VoidType: ...
    
    def GetNextSelector(self) -> ISurrogateSelector: ...
    
    def GetSurrogate(self, type: TypeType, context: StreamingContext, selector: ISurrogateSelector) -> Tuple[ISerializationSurrogate, ISurrogateSelector]: ...
    
    def RemoveSurrogate(self, type: TypeType, context: StreamingContext) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SurrogateSelector(ObjectType, ISurrogateSelector):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def AddSurrogate(self, type: TypeType, context: StreamingContext, surrogate: ISerializationSurrogate) -> VoidType: ...
    
    def ChainSelector(self, selector: ISurrogateSelector) -> VoidType: ...
    
    def GetNextSelector(self) -> ISurrogateSelector: ...
    
    def GetSurrogate(self, type: TypeType, context: StreamingContext, selector: ISurrogateSelector) -> Tuple[ISerializationSurrogate, ISurrogateSelector]: ...
    
    def RemoveSurrogate(self, type: TypeType, context: StreamingContext) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TypeLoadExceptionHolder(ObjectType):
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


class TypeLoadExceptionHolder(ObjectType):
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


class TypeLoadExceptionHolder(ObjectType):
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


class ValueTypeFixupInfo(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, containerID: LongType, member: FieldInfo, parentIndex: ArrayType[IntType]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ContainerID(self) -> LongType: ...
    
    @property
    def ParentField(self) -> FieldInfo: ...
    
    @property
    def ParentIndex(self) -> ArrayType[IntType]: ...
    
    # ---------- Methods ---------- #
    
    def get_ContainerID(self) -> LongType: ...
    
    def get_ParentField(self) -> FieldInfo: ...
    
    def get_ParentIndex(self) -> ArrayType[IntType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ValueTypeFixupInfo(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, containerID: LongType, member: FieldInfo, parentIndex: ArrayType[IntType]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ContainerID(self) -> LongType: ...
    
    @property
    def ParentField(self) -> FieldInfo: ...
    
    @property
    def ParentIndex(self) -> ArrayType[IntType]: ...
    
    # ---------- Methods ---------- #
    
    def get_ContainerID(self) -> LongType: ...
    
    def get_ParentField(self) -> FieldInfo: ...
    
    def get_ParentIndex(self) -> ArrayType[IntType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ValueTypeFixupInfo(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, containerID: LongType, member: FieldInfo, parentIndex: ArrayType[IntType]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ContainerID(self) -> LongType: ...
    
    @property
    def ParentField(self) -> FieldInfo: ...
    
    @property
    def ParentIndex(self) -> ArrayType[IntType]: ...
    
    # ---------- Methods ---------- #
    
    def get_ContainerID(self) -> LongType: ...
    
    def get_ParentField(self) -> FieldInfo: ...
    
    def get_ParentIndex(self) -> ArrayType[IntType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# ---------- Structs ---------- #

class SerializationEntry(ValueType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def ObjectType(self) -> TypeType: ...
    
    @property
    def Value(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def get_Name(self) -> StringType: ...
    
    def get_ObjectType(self) -> TypeType: ...
    
    def get_Value(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SerializationEntry(ValueType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def ObjectType(self) -> TypeType: ...
    
    @property
    def Value(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def get_Name(self) -> StringType: ...
    
    def get_ObjectType(self) -> TypeType: ...
    
    def get_Value(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SerializationEntry(ValueType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def ObjectType(self) -> TypeType: ...
    
    @property
    def Value(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def get_Name(self) -> StringType: ...
    
    def get_ObjectType(self) -> TypeType: ...
    
    def get_Value(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class StreamingContext(ValueType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, state: StreamingContextStates): ...
    
    @overload
    def __init__(self, state: StreamingContextStates, additional: ObjectType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Context(self) -> ObjectType: ...
    
    @property
    def State(self) -> StreamingContextStates: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def get_Context(self) -> ObjectType: ...
    
    def get_State(self) -> StreamingContextStates: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class StreamingContext(ValueType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, state: StreamingContextStates): ...
    
    @overload
    def __init__(self, state: StreamingContextStates, additional: ObjectType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Context(self) -> ObjectType: ...
    
    @property
    def State(self) -> StreamingContextStates: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def get_Context(self) -> ObjectType: ...
    
    def get_State(self) -> StreamingContextStates: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class StreamingContext(ValueType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, state: StreamingContextStates): ...
    
    @overload
    def __init__(self, state: StreamingContextStates, additional: ObjectType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Context(self) -> ObjectType: ...
    
    @property
    def State(self) -> StreamingContextStates: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def get_Context(self) -> ObjectType: ...
    
    def get_State(self) -> StreamingContextStates: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# ---------- Interfaces ---------- #

class IDeserializationCallback(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def OnDeserialization(self, sender: ObjectType) -> VoidType: ...
    
    # No Events


class IDeserializationCallback(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def OnDeserialization(self, sender: ObjectType) -> VoidType: ...
    
    # No Events


class IDeserializationCallback(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def OnDeserialization(self, sender: ObjectType) -> VoidType: ...
    
    # No Events


class IFormatter(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def Binder(self) -> SerializationBinder: ...
    
    @Binder.setter
    def Binder(self, value: SerializationBinder) -> None: ...
    
    @property
    def Context(self) -> StreamingContext: ...
    
    @Context.setter
    def Context(self, value: StreamingContext) -> None: ...
    
    @property
    def SurrogateSelector(self) -> ISurrogateSelector: ...
    
    @SurrogateSelector.setter
    def SurrogateSelector(self, value: ISurrogateSelector) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Deserialize(self, serializationStream: Stream) -> ObjectType: ...
    
    def Serialize(self, serializationStream: Stream, graph: ObjectType) -> VoidType: ...
    
    def get_Binder(self) -> SerializationBinder: ...
    
    def get_Context(self) -> StreamingContext: ...
    
    def get_SurrogateSelector(self) -> ISurrogateSelector: ...
    
    def set_Binder(self, value: SerializationBinder) -> VoidType: ...
    
    def set_Context(self, value: StreamingContext) -> VoidType: ...
    
    def set_SurrogateSelector(self, value: ISurrogateSelector) -> VoidType: ...
    
    # No Events


class IFormatter(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def Binder(self) -> SerializationBinder: ...
    
    @Binder.setter
    def Binder(self, value: SerializationBinder) -> None: ...
    
    @property
    def Context(self) -> StreamingContext: ...
    
    @Context.setter
    def Context(self, value: StreamingContext) -> None: ...
    
    @property
    def SurrogateSelector(self) -> ISurrogateSelector: ...
    
    @SurrogateSelector.setter
    def SurrogateSelector(self, value: ISurrogateSelector) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Deserialize(self, serializationStream: Stream) -> ObjectType: ...
    
    def Serialize(self, serializationStream: Stream, graph: ObjectType) -> VoidType: ...
    
    def get_Binder(self) -> SerializationBinder: ...
    
    def get_Context(self) -> StreamingContext: ...
    
    def get_SurrogateSelector(self) -> ISurrogateSelector: ...
    
    def set_Binder(self, value: SerializationBinder) -> VoidType: ...
    
    def set_Context(self, value: StreamingContext) -> VoidType: ...
    
    def set_SurrogateSelector(self, value: ISurrogateSelector) -> VoidType: ...
    
    # No Events


class IFormatter(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def Binder(self) -> SerializationBinder: ...
    
    @Binder.setter
    def Binder(self, value: SerializationBinder) -> None: ...
    
    @property
    def Context(self) -> StreamingContext: ...
    
    @Context.setter
    def Context(self, value: StreamingContext) -> None: ...
    
    @property
    def SurrogateSelector(self) -> ISurrogateSelector: ...
    
    @SurrogateSelector.setter
    def SurrogateSelector(self, value: ISurrogateSelector) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Deserialize(self, serializationStream: Stream) -> ObjectType: ...
    
    def Serialize(self, serializationStream: Stream, graph: ObjectType) -> VoidType: ...
    
    def get_Binder(self) -> SerializationBinder: ...
    
    def get_Context(self) -> StreamingContext: ...
    
    def get_SurrogateSelector(self) -> ISurrogateSelector: ...
    
    def set_Binder(self, value: SerializationBinder) -> VoidType: ...
    
    def set_Context(self, value: StreamingContext) -> VoidType: ...
    
    def set_SurrogateSelector(self, value: ISurrogateSelector) -> VoidType: ...
    
    # No Events


class IFormatterConverter(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def Convert(self, value: ObjectType, type: TypeType) -> ObjectType: ...
    
    @overload
    def Convert(self, value: ObjectType, typeCode: TypeCode) -> ObjectType: ...
    
    def ToBoolean(self, value: ObjectType) -> BooleanType: ...
    
    def ToByte(self, value: ObjectType) -> ByteType: ...
    
    def ToChar(self, value: ObjectType) -> CharType: ...
    
    def ToDateTime(self, value: ObjectType) -> DateTime: ...
    
    def ToDecimal(self, value: ObjectType) -> DecimalType: ...
    
    def ToDouble(self, value: ObjectType) -> DoubleType: ...
    
    def ToInt16(self, value: ObjectType) -> ShortType: ...
    
    def ToInt32(self, value: ObjectType) -> IntType: ...
    
    def ToInt64(self, value: ObjectType) -> LongType: ...
    
    def ToSByte(self, value: ObjectType) -> SByteType: ...
    
    def ToSingle(self, value: ObjectType) -> FloatType: ...
    
    def ToString(self, value: ObjectType) -> StringType: ...
    
    def ToUInt16(self, value: ObjectType) -> UShortType: ...
    
    def ToUInt32(self, value: ObjectType) -> UIntType: ...
    
    def ToUInt64(self, value: ObjectType) -> ULongType: ...
    
    # No Events


class IFormatterConverter(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def Convert(self, value: ObjectType, type: TypeType) -> ObjectType: ...
    
    @overload
    def Convert(self, value: ObjectType, typeCode: TypeCode) -> ObjectType: ...
    
    def ToBoolean(self, value: ObjectType) -> BooleanType: ...
    
    def ToByte(self, value: ObjectType) -> ByteType: ...
    
    def ToChar(self, value: ObjectType) -> CharType: ...
    
    def ToDateTime(self, value: ObjectType) -> DateTime: ...
    
    def ToDecimal(self, value: ObjectType) -> DecimalType: ...
    
    def ToDouble(self, value: ObjectType) -> DoubleType: ...
    
    def ToInt16(self, value: ObjectType) -> ShortType: ...
    
    def ToInt32(self, value: ObjectType) -> IntType: ...
    
    def ToInt64(self, value: ObjectType) -> LongType: ...
    
    def ToSByte(self, value: ObjectType) -> SByteType: ...
    
    def ToSingle(self, value: ObjectType) -> FloatType: ...
    
    def ToString(self, value: ObjectType) -> StringType: ...
    
    def ToUInt16(self, value: ObjectType) -> UShortType: ...
    
    def ToUInt32(self, value: ObjectType) -> UIntType: ...
    
    def ToUInt64(self, value: ObjectType) -> ULongType: ...
    
    # No Events


class IFormatterConverter(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def Convert(self, value: ObjectType, type: TypeType) -> ObjectType: ...
    
    @overload
    def Convert(self, value: ObjectType, typeCode: TypeCode) -> ObjectType: ...
    
    def ToBoolean(self, value: ObjectType) -> BooleanType: ...
    
    def ToByte(self, value: ObjectType) -> ByteType: ...
    
    def ToChar(self, value: ObjectType) -> CharType: ...
    
    def ToDateTime(self, value: ObjectType) -> DateTime: ...
    
    def ToDecimal(self, value: ObjectType) -> DecimalType: ...
    
    def ToDouble(self, value: ObjectType) -> DoubleType: ...
    
    def ToInt16(self, value: ObjectType) -> ShortType: ...
    
    def ToInt32(self, value: ObjectType) -> IntType: ...
    
    def ToInt64(self, value: ObjectType) -> LongType: ...
    
    def ToSByte(self, value: ObjectType) -> SByteType: ...
    
    def ToSingle(self, value: ObjectType) -> FloatType: ...
    
    def ToString(self, value: ObjectType) -> StringType: ...
    
    def ToUInt16(self, value: ObjectType) -> UShortType: ...
    
    def ToUInt32(self, value: ObjectType) -> UIntType: ...
    
    def ToUInt64(self, value: ObjectType) -> ULongType: ...
    
    # No Events


class IObjectReference(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetRealObject(self, context: StreamingContext) -> ObjectType: ...
    
    # No Events


class IObjectReference(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetRealObject(self, context: StreamingContext) -> ObjectType: ...
    
    # No Events


class IObjectReference(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetRealObject(self, context: StreamingContext) -> ObjectType: ...
    
    # No Events


class ISafeSerializationData(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def CompleteDeserialization(self, deserialized: ObjectType) -> VoidType: ...
    
    # No Events


class ISafeSerializationData(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def CompleteDeserialization(self, deserialized: ObjectType) -> VoidType: ...
    
    # No Events


class ISafeSerializationData(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def CompleteDeserialization(self, deserialized: ObjectType) -> VoidType: ...
    
    # No Events


class ISerializable(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    
    # No Events


class ISerializable(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    
    # No Events


class ISerializable(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    
    # No Events


class ISerializationSurrogate(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetObjectData(self, obj: ObjectType, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    
    def SetObjectData(self, obj: ObjectType, info: SerializationInfo, context: StreamingContext, selector: ISurrogateSelector) -> ObjectType: ...
    
    # No Events


class ISerializationSurrogate(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetObjectData(self, obj: ObjectType, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    
    def SetObjectData(self, obj: ObjectType, info: SerializationInfo, context: StreamingContext, selector: ISurrogateSelector) -> ObjectType: ...
    
    # No Events


class ISerializationSurrogate(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetObjectData(self, obj: ObjectType, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    
    def SetObjectData(self, obj: ObjectType, info: SerializationInfo, context: StreamingContext, selector: ISurrogateSelector) -> ObjectType: ...
    
    # No Events


class ISurrogateSelector(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def ChainSelector(self, selector: ISurrogateSelector) -> VoidType: ...
    
    def GetNextSelector(self) -> ISurrogateSelector: ...
    
    def GetSurrogate(self, type: TypeType, context: StreamingContext, selector: ISurrogateSelector) -> Tuple[ISerializationSurrogate, ISurrogateSelector]: ...
    
    # No Events


class ISurrogateSelector(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def ChainSelector(self, selector: ISurrogateSelector) -> VoidType: ...
    
    def GetNextSelector(self) -> ISurrogateSelector: ...
    
    def GetSurrogate(self, type: TypeType, context: StreamingContext, selector: ISurrogateSelector) -> Tuple[ISerializationSurrogate, ISurrogateSelector]: ...
    
    # No Events


class ISurrogateSelector(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def ChainSelector(self, selector: ISurrogateSelector) -> VoidType: ...
    
    def GetNextSelector(self) -> ISurrogateSelector: ...
    
    def GetSurrogate(self, type: TypeType, context: StreamingContext, selector: ISurrogateSelector) -> Tuple[ISerializationSurrogate, ISurrogateSelector]: ...
    
    # No Events


# ---------- Enums ---------- #

class StreamingContextStates(Enum):
    CrossProcess: IntType = 1
    CrossMachine: IntType = 2
    File: IntType = 4
    Persistence: IntType = 8
    Remoting: IntType = 16
    Other: IntType = 32
    Clone: IntType = 64
    CrossAppDomain: IntType = 128
    All: IntType = 255


class StreamingContextStates(Enum):
    CrossProcess: IntType = 1
    CrossMachine: IntType = 2
    File: IntType = 4
    Persistence: IntType = 8
    Remoting: IntType = 16
    Other: IntType = 32
    Clone: IntType = 64
    CrossAppDomain: IntType = 128
    All: IntType = 255


class StreamingContextStates(Enum):
    CrossProcess: IntType = 1
    CrossMachine: IntType = 2
    File: IntType = 4
    Persistence: IntType = 8
    Remoting: IntType = 16
    Other: IntType = 32
    Clone: IntType = 64
    CrossAppDomain: IntType = 128
    All: IntType = 255


# ---------- Delegates ---------- #

DeserializationEventHandler = Callable[[ObjectType], VoidType]

DeserializationEventHandler = Callable[[ObjectType], VoidType]

DeserializationEventHandler = Callable[[ObjectType], VoidType]

SerializationEventHandler = Callable[[StreamingContext], VoidType]

SerializationEventHandler = Callable[[StreamingContext], VoidType]

SerializationEventHandler = Callable[[StreamingContext], VoidType]

__all__ = [
    DeserializationEventHandler,
    FixupHolder,
    FixupHolderList,
    Formatter,
    FormatterConverter,
    FormatterServices,
    LongList,
    MemberHolder,
    ObjectCloneHelper,
    ObjectHolder,
    ObjectHolderList,
    ObjectHolderListEnumerator,
    ObjectIDGenerator,
    ObjectManager,
    OnDeserializedAttribute,
    OnDeserializingAttribute,
    OnSerializedAttribute,
    OnSerializingAttribute,
    OptionalFieldAttribute,
    SafeSerializationEventArgs,
    SafeSerializationManager,
    SerializationBinder,
    SerializationEventHandler,
    SerializationEvents,
    SerializationEventsCache,
    SerializationException,
    SerializationFieldInfo,
    SerializationInfo,
    SerializationInfoEnumerator,
    SerializationObjectManager,
    SurrogateForCyclicalReference,
    SurrogateHashtable,
    SurrogateKey,
    SurrogateSelector,
    TypeLoadExceptionHolder,
    ValueTypeFixupInfo,
    SerializationEntry,
    StreamingContext,
    IDeserializationCallback,
    IFormatter,
    IFormatterConverter,
    IObjectReference,
    ISafeSerializationData,
    ISerializable,
    ISerializationSurrogate,
    ISurrogateSelector,
    StreamingContextStates,
    DeserializationEventHandler,
    SerializationEventHandler,
]
