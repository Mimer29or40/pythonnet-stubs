"""Automatically generated stubs for C# namespace: System.Runtime.Serialization."""

from abc import ABC
from collections.abc import Callable
from collections.abc import Iterator
from typing import overload

from System import Array
from System import Attribute
from System import Boolean
from System import Char
from System import DateTime
from System import Decimal
from System import Enum
from System import EventArgs
from System import Exception
from System import Guid
from System import ICloneable
from System import IntPtr
from System import Object
from System import RuntimeFieldHandle
from System import String
from System import SystemException
from System import Type
from System import TypeCode
from System import TypedReference
from System import UInt32
from System import ValueType
from System.Collections import Hashtable
from System.Collections import ICollection
from System.Collections import IDictionary
from System.Collections import IDictionaryEnumerator
from System.Collections import IEnumerable
from System.Collections import IEnumerator
from System.Collections.Generic import IEnumerable
from System.Collections.Generic import IList
from System.Globalization import CultureInfo
from System.IO import Stream
from System.Reflection import Assembly
from System.Reflection import Binder
from System.Reflection import BindingFlags
from System.Reflection import CustomAttributeData
from System.Reflection import FieldAttributes
from System.Reflection import FieldInfo
from System.Reflection import ICustomAttributeProvider
from System.Reflection import MemberInfo
from System.Reflection import MemberTypes
from System.Reflection import MethodBase
from System.Reflection import Module
from System.Runtime.InteropServices import _Attribute
from System.Runtime.InteropServices import _Exception
from System.Runtime.InteropServices import _FieldInfo
from System.Runtime.InteropServices import _MemberInfo

from .Formatters import TypeFilterLevel

type DeserializationEventHandler = Callable[[object], None]
""""""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class FixupHolder(Object):
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
class FixupHolderList(Object):
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
class Formatter(ABC, Object, IFormatter):
    """"""
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
    def SurrogateSelector(self) -> ISurrogateSelector:
        """"""
    @SurrogateSelector.setter
    def SurrogateSelector(self, value: ISurrogateSelector) -> None: ...
    def Deserialize(self, serializationStream: Stream) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Serialize(self, serializationStream: Stream, graph: object) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class FormatterConverter(Object, IFormatterConverter):
    """"""
    def __init__(self) -> None:
        """"""
    @overload
    def Convert(self, value: object, type: Type) -> object:
        """"""
    @overload
    def Convert(self, value: object, typeCode: TypeCode) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToBoolean(self, value: object) -> bool:
        """"""
    def ToByte(self, value: object) -> int:
        """"""
    def ToChar(self, value: object) -> Char:
        """"""
    def ToDateTime(self, value: object) -> DateTime:
        """"""
    def ToDecimal(self, value: object) -> Decimal:
        """"""
    def ToDouble(self, value: object) -> float:
        """"""
    def ToInt16(self, value: object) -> int:
        """"""
    def ToInt32(self, value: object) -> int:
        """"""
    def ToInt64(self, value: object) -> int:
        """"""
    def ToSByte(self, value: object) -> int:
        """"""
    def ToSingle(self, value: object) -> float:
        """"""
    @overload
    def ToString(self) -> str:
        """"""
    @overload
    def ToString(self, value: object) -> str:
        """"""
    def ToUInt16(self, value: object) -> int:
        """"""
    def ToUInt32(self, value: object) -> int:
        """"""
    def ToUInt64(self, value: object) -> int:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class FormatterServices(ABC, Object):
    """"""
    @classmethod
    def CheckTypeSecurity(cls, t: Type, securityLevel: TypeFilterLevel) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @classmethod
    def GetObjectData(cls, obj: object, members: Array[MemberInfo]) -> Array[object]:
        """"""
    @classmethod
    def GetSafeUninitializedObject(cls, type: Type) -> object:
        """"""
    @classmethod
    @overload
    def GetSerializableMembers(cls, type: Type) -> Array[MemberInfo]:
        """"""
    @classmethod
    @overload
    def GetSerializableMembers(cls, type: Type, context: StreamingContext) -> Array[MemberInfo]:
        """"""
    @classmethod
    def GetSurrogateForCyclicalReference(
        cls, innerSurrogate: ISerializationSurrogate
    ) -> ISerializationSurrogate:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def GetTypeFromAssembly(cls, assem: Assembly, name: str) -> Type:
        """"""
    @classmethod
    def GetUninitializedObject(cls, type: Type) -> object:
        """"""
    @classmethod
    def PopulateObjectMembers(
        cls, obj: object, members: Array[MemberInfo], data: Array[object]
    ) -> object:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IDeserializationCallback(ABC):
    """"""
    def OnDeserialization(self, sender: object) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IFormatter(ABC):
    """"""
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
    def SurrogateSelector(self) -> ISurrogateSelector:
        """"""
    @SurrogateSelector.setter
    def SurrogateSelector(self, value: ISurrogateSelector) -> None: ...
    def Deserialize(self, serializationStream: Stream) -> object:
        """"""
    def Serialize(self, serializationStream: Stream, graph: object) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IFormatterConverter(ABC):
    """"""
    @overload
    def Convert(self, value: object, type: Type) -> object:
        """"""
    @overload
    def Convert(self, value: object, typeCode: TypeCode) -> object:
        """"""
    def ToBoolean(self, value: object) -> bool:
        """"""
    def ToByte(self, value: object) -> int:
        """"""
    def ToChar(self, value: object) -> Char:
        """"""
    def ToDateTime(self, value: object) -> DateTime:
        """"""
    def ToDecimal(self, value: object) -> Decimal:
        """"""
    def ToDouble(self, value: object) -> float:
        """"""
    def ToInt16(self, value: object) -> int:
        """"""
    def ToInt32(self, value: object) -> int:
        """"""
    def ToInt64(self, value: object) -> int:
        """"""
    def ToSByte(self, value: object) -> int:
        """"""
    def ToSingle(self, value: object) -> float:
        """"""
    def ToString(self, value: object) -> str:
        """"""
    def ToUInt16(self, value: object) -> int:
        """"""
    def ToUInt32(self, value: object) -> int:
        """"""
    def ToUInt64(self, value: object) -> int:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IObjectReference(ABC):
    """"""
    def GetRealObject(self, context: StreamingContext) -> object:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ISafeSerializationData(ABC):
    """"""
    def CompleteDeserialization(self, deserialized: object) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ISerializable(ABC):
    """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ISerializationSurrogate(ABC):
    """"""
    def GetObjectData(
        self, obj: object, info: SerializationInfo, context: StreamingContext
    ) -> None:
        """"""
    def SetObjectData(
        self,
        obj: object,
        info: SerializationInfo,
        context: StreamingContext,
        selector: ISurrogateSelector,
    ) -> object:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ISurrogateSelector(ABC):
    """"""
    def ChainSelector(self, selector: ISurrogateSelector) -> None:
        """"""
    def GetNextSelector(self) -> ISurrogateSelector:
        """"""
    def GetSurrogate(
        self, type: Type, context: StreamingContext, selector: ISurrogateSelector
    ) -> tuple[ISerializationSurrogate, ISurrogateSelector]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class LongList(Object):
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
class MemberHolder(Object):
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
class ObjectCloneHelper(ABC, Object):
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
class ObjectHolder(Object):
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
class ObjectHolderList(Object):
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
class ObjectHolderListEnumerator(Object):
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
class ObjectIDGenerator(Object):
    """"""
    def __init__(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetId(self, obj: object, firstTime: Boolean) -> tuple[int, Boolean]:
        """"""
    def GetType(self) -> Type:
        """"""
    def HasId(self, obj: object, firstTime: Boolean) -> tuple[int, Boolean]:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ObjectManager(Object):
    """"""
    def __init__(self, selector: ISurrogateSelector, context: StreamingContext) -> None:
        """"""
    def DoFixups(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetObject(self, objectID: int) -> object:
        """"""
    def GetType(self) -> Type:
        """"""
    def RaiseDeserializationEvent(self) -> None:
        """"""
    def RaiseOnDeserializingEvent(self, obj: object) -> None:
        """"""
    @overload
    def RecordArrayElementFixup(
        self, arrayToBeFixed: int, indices: Array[int], objectRequired: int
    ) -> None:
        """"""
    @overload
    def RecordArrayElementFixup(self, arrayToBeFixed: int, index: int, objectRequired: int) -> None:
        """"""
    def RecordDelayedFixup(
        self, objectToBeFixed: int, memberName: str, objectRequired: int
    ) -> None:
        """"""
    def RecordFixup(self, objectToBeFixed: int, member: MemberInfo, objectRequired: int) -> None:
        """"""
    @overload
    def RegisterObject(self, obj: object, objectID: int) -> None:
        """"""
    @overload
    def RegisterObject(self, obj: object, objectID: int, info: SerializationInfo) -> None:
        """"""
    @overload
    def RegisterObject(
        self,
        obj: object,
        objectID: int,
        info: SerializationInfo,
        idOfContainingObj: int,
        member: MemberInfo,
    ) -> None:
        """"""
    @overload
    def RegisterObject(
        self,
        obj: object,
        objectID: int,
        info: SerializationInfo,
        idOfContainingObj: int,
        member: MemberInfo,
        arrayIndex: Array[int],
    ) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class OnDeserializedAttribute(Attribute, _Attribute):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """"""
    def GetTypeInfoCount(self, pcTInfo: UInt32) -> tuple[None, UInt32]:
        """"""
    def Invoke(
        self,
        dispIdMember: int,
        riid: Guid,
        lcid: int,
        wFlags: int,
        pDispParams: IntPtr,
        pVarResult: IntPtr,
        pExcepInfo: IntPtr,
        puArgErr: IntPtr,
    ) -> None:
        """"""
    def IsDefaultAttribute(self) -> bool:
        """"""
    def Match(self, obj: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class OnDeserializingAttribute(Attribute, _Attribute):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """"""
    def GetTypeInfoCount(self, pcTInfo: UInt32) -> tuple[None, UInt32]:
        """"""
    def Invoke(
        self,
        dispIdMember: int,
        riid: Guid,
        lcid: int,
        wFlags: int,
        pDispParams: IntPtr,
        pVarResult: IntPtr,
        pExcepInfo: IntPtr,
        puArgErr: IntPtr,
    ) -> None:
        """"""
    def IsDefaultAttribute(self) -> bool:
        """"""
    def Match(self, obj: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class OnSerializedAttribute(Attribute, _Attribute):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """"""
    def GetTypeInfoCount(self, pcTInfo: UInt32) -> tuple[None, UInt32]:
        """"""
    def Invoke(
        self,
        dispIdMember: int,
        riid: Guid,
        lcid: int,
        wFlags: int,
        pDispParams: IntPtr,
        pVarResult: IntPtr,
        pExcepInfo: IntPtr,
        puArgErr: IntPtr,
    ) -> None:
        """"""
    def IsDefaultAttribute(self) -> bool:
        """"""
    def Match(self, obj: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class OnSerializingAttribute(Attribute, _Attribute):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """"""
    def GetTypeInfoCount(self, pcTInfo: UInt32) -> tuple[None, UInt32]:
        """"""
    def Invoke(
        self,
        dispIdMember: int,
        riid: Guid,
        lcid: int,
        wFlags: int,
        pDispParams: IntPtr,
        pVarResult: IntPtr,
        pExcepInfo: IntPtr,
        puArgErr: IntPtr,
    ) -> None:
        """"""
    def IsDefaultAttribute(self) -> bool:
        """"""
    def Match(self, obj: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class OptionalFieldAttribute(Attribute, _Attribute):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
    @property
    def VersionAdded(self) -> int:
        """"""
    @VersionAdded.setter
    def VersionAdded(self, value: int) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """"""
    def GetTypeInfoCount(self, pcTInfo: UInt32) -> tuple[None, UInt32]:
        """"""
    def Invoke(
        self,
        dispIdMember: int,
        riid: Guid,
        lcid: int,
        wFlags: int,
        pDispParams: IntPtr,
        pVarResult: IntPtr,
        pExcepInfo: IntPtr,
        puArgErr: IntPtr,
    ) -> None:
        """"""
    def IsDefaultAttribute(self) -> bool:
        """"""
    def Match(self, obj: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SafeSerializationEventArgs(EventArgs):
    """"""
    @property
    def StreamingContext(self) -> StreamingContext:
        """"""
    def AddSerializedState(self, serializedState: ISafeSerializationData) -> None:
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
class SafeSerializationManager(Object, IObjectReference, ISerializable):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetRealObject(self, context: StreamingContext) -> object:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SerializationBinder(ABC, Object):
    """"""
    def BindToName(
        self, serializedType: Type, assemblyName: String, typeName: String
    ) -> tuple[None, String, String]:
        """"""
    def BindToType(self, assemblyName: str, typeName: str) -> Type:
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
class SerializationEntry(ValueType):
    """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def ObjectType(self) -> Type:
        """"""
    @property
    def Value(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

type SerializationEventHandler = Callable[[StreamingContext], None]
""""""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SerializationEvents(Object):
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
class SerializationEventsCache(ABC, Object):
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
class SerializationException(SystemException, _Exception, ISerializable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, message: str) -> None:
        """"""
    @overload
    def __init__(self, message: str, innerException: Exception) -> None:
        """"""
    @property
    def Data(self) -> IDictionary:
        """"""
    @property
    def HResult(self) -> int:
        """"""
    @property
    def HelpLink(self) -> str:
        """"""
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """"""
    @property
    def Message(self) -> str:
        """"""
    @property
    def Source(self) -> str:
        """"""
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """"""
    @property
    def TargetSite(self) -> MethodBase:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetBaseException(self) -> Exception:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SerializationFieldInfo(FieldInfo, ICustomAttributeProvider, _FieldInfo, _MemberInfo):
    """"""
    @property
    def Attributes(self) -> FieldAttributes:
        """"""
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]:
        """"""
    @property
    def DeclaringType(self) -> Type:
        """"""
    @property
    def FieldHandle(self) -> RuntimeFieldHandle:
        """"""
    @property
    def FieldType(self) -> Type:
        """"""
    @property
    def IsAssembly(self) -> bool:
        """"""
    @property
    def IsFamily(self) -> bool:
        """"""
    @property
    def IsFamilyAndAssembly(self) -> bool:
        """"""
    @property
    def IsFamilyOrAssembly(self) -> bool:
        """"""
    @property
    def IsInitOnly(self) -> bool:
        """"""
    @property
    def IsLiteral(self) -> bool:
        """"""
    @property
    def IsNotSerialized(self) -> bool:
        """"""
    @property
    def IsPinvokeImpl(self) -> bool:
        """"""
    @property
    def IsPrivate(self) -> bool:
        """"""
    @property
    def IsPublic(self) -> bool:
        """"""
    @property
    def IsSecurityCritical(self) -> bool:
        """"""
    @property
    def IsSecuritySafeCritical(self) -> bool:
        """"""
    @property
    def IsSecurityTransparent(self) -> bool:
        """"""
    @property
    def IsSpecialName(self) -> bool:
        """"""
    @property
    def IsStatic(self) -> bool:
        """"""
    @property
    def MemberType(self) -> MemberTypes:
        """"""
    @property
    def MetadataToken(self) -> int:
        """"""
    @property
    def Module(self) -> Module:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def ReflectedType(self) -> Type:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """"""
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """"""
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    def GetOptionalCustomModifiers(self) -> Array[Type]:
        """"""
    def GetRawConstantValue(self) -> object:
        """"""
    def GetRequiredCustomModifiers(self) -> Array[Type]:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """"""
    def GetTypeInfoCount(self, pcTInfo: UInt32) -> tuple[None, UInt32]:
        """"""
    def GetValue(self, obj: object) -> object:
        """"""
    def GetValueDirect(self, obj: TypedReference) -> object:
        """"""
    def Invoke(
        self,
        dispIdMember: int,
        riid: Guid,
        lcid: int,
        wFlags: int,
        pDispParams: IntPtr,
        pVarResult: IntPtr,
        pExcepInfo: IntPtr,
        puArgErr: IntPtr,
    ) -> None:
        """"""
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """"""
    @overload
    def SetValue(self, obj: object, value: object) -> None:
        """"""
    @overload
    def SetValue(
        self,
        obj: object,
        value: object,
        invokeAttr: BindingFlags,
        binder: Binder,
        culture: CultureInfo,
    ) -> None:
        """"""
    def SetValueDirect(self, obj: TypedReference, value: object) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SerializationInfo(Object):
    """"""
    @overload
    def __init__(self, type: Type, converter: IFormatterConverter) -> None:
        """"""
    @overload
    def __init__(
        self, type: Type, converter: IFormatterConverter, requireSameTokenInPartialTrust: bool
    ) -> None:
        """"""
    @property
    def AssemblyName(self) -> str:
        """"""
    @AssemblyName.setter
    def AssemblyName(self, value: str) -> None: ...
    @property
    def FullTypeName(self) -> str:
        """"""
    @FullTypeName.setter
    def FullTypeName(self, value: str) -> None: ...
    @property
    def IsAssemblyNameSetExplicit(self) -> bool:
        """"""
    @property
    def IsFullTypeNameSetExplicit(self) -> bool:
        """"""
    @property
    def MemberCount(self) -> int:
        """"""
    @property
    def ObjectType(self) -> Type:
        """"""
    @overload
    def AddValue(self, name: str, value: bool) -> None:
        """"""
    @overload
    def AddValue(self, name: str, value: int) -> None:
        """"""
    @overload
    def AddValue(self, name: str, value: Char) -> None:
        """"""
    @overload
    def AddValue(self, name: str, value: DateTime) -> None:
        """"""
    @overload
    def AddValue(self, name: str, value: Decimal) -> None:
        """"""
    @overload
    def AddValue(self, name: str, value: float) -> None:
        """"""
    @overload
    def AddValue(self, name: str, value: int) -> None:
        """"""
    @overload
    def AddValue(self, name: str, value: int) -> None:
        """"""
    @overload
    def AddValue(self, name: str, value: int) -> None:
        """"""
    @overload
    def AddValue(self, name: str, value: object) -> None:
        """"""
    @overload
    def AddValue(self, name: str, value: object, type: Type) -> None:
        """"""
    @overload
    def AddValue(self, name: str, value: int) -> None:
        """"""
    @overload
    def AddValue(self, name: str, value: float) -> None:
        """"""
    @overload
    def AddValue(self, name: str, value: int) -> None:
        """"""
    @overload
    def AddValue(self, name: str, value: int) -> None:
        """"""
    @overload
    def AddValue(self, name: str, value: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetBoolean(self, name: str) -> bool:
        """"""
    def GetByte(self, name: str) -> int:
        """"""
    def GetChar(self, name: str) -> Char:
        """"""
    def GetDateTime(self, name: str) -> DateTime:
        """"""
    def GetDecimal(self, name: str) -> Decimal:
        """"""
    def GetDouble(self, name: str) -> float:
        """"""
    def GetEnumerator(self) -> SerializationInfoEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetInt16(self, name: str) -> int:
        """"""
    def GetInt32(self, name: str) -> int:
        """"""
    def GetInt64(self, name: str) -> int:
        """"""
    def GetSByte(self, name: str) -> int:
        """"""
    def GetSingle(self, name: str) -> float:
        """"""
    def GetString(self, name: str) -> str:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetUInt16(self, name: str) -> int:
        """"""
    def GetUInt32(self, name: str) -> int:
        """"""
    def GetUInt64(self, name: str) -> int:
        """"""
    def GetValue(self, name: str, type: Type) -> object:
        """"""
    def SetType(self, type: Type) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def __iter__(self) -> Iterator:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SerializationInfoEnumerator(Object, IEnumerator):
    """"""
    @property
    def Current(self) -> SerializationEntry:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def ObjectType(self) -> Type:
        """"""
    @property
    def Value(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def MoveNext(self) -> bool:
        """"""
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SerializationObjectManager(Object):
    """"""
    def __init__(self, context: StreamingContext) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def RaiseOnSerializedEvent(self) -> None:
        """"""
    def RegisterObject(self, obj: object) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class StreamingContext(ValueType):
    """"""
    @overload
    def __init__(self, state: StreamingContextStates) -> None:
        """"""
    @overload
    def __init__(self, state: StreamingContextStates, additional: object) -> None:
        """"""
    @property
    def Context(self) -> object:
        """"""
    @property
    def State(self) -> StreamingContextStates:
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
class StreamingContextStates(Enum):
    """"""

    CrossProcess: StreamingContextStates = ...
    """"""
    CrossMachine: StreamingContextStates = ...
    """"""
    File: StreamingContextStates = ...
    """"""
    Persistence: StreamingContextStates = ...
    """"""
    Remoting: StreamingContextStates = ...
    """"""
    Other: StreamingContextStates = ...
    """"""
    Clone: StreamingContextStates = ...
    """"""
    CrossAppDomain: StreamingContextStates = ...
    """"""
    All: StreamingContextStates = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SurrogateForCyclicalReference(Object, ISerializationSurrogate):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetObjectData(
        self, obj: object, info: SerializationInfo, context: StreamingContext
    ) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def SetObjectData(
        self,
        obj: object,
        info: SerializationInfo,
        context: StreamingContext,
        selector: ISurrogateSelector,
    ) -> object:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SurrogateHashtable(
    Hashtable,
    ICollection,
    IDictionary,
    IEnumerable,
    IDeserializationCallback,
    ISerializable,
    ICloneable,
):
    """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsFixedSize(self) -> bool:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def Item(self) -> object:
        """"""
    @Item.setter
    def Item(self, value: object) -> None: ...
    @property
    def Keys(self) -> ICollection:
        """"""
    @property
    def SyncRoot(self) -> object:
        """"""
    @property
    def Values(self) -> ICollection:
        """"""
    def Add(self, key: object, value: object) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    def Clone(self) -> object:
        """"""
    def Contains(self, key: object) -> bool:
        """"""
    def ContainsKey(self, key: object) -> bool:
        """"""
    def ContainsValue(self, value: object) -> bool:
        """"""
    def CopyTo(self, array: Array, arrayIndex: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IDictionaryEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def OnDeserialization(self, sender: object) -> None:
        """"""
    def Remove(self, key: object) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def __contains__(self, key: object) -> bool:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    def __delitem__(self, key: object) -> None:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, key: object) -> object:
        """"""
    def __setitem__(self, key: object, value: object) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SurrogateKey(Object):
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
class SurrogateSelector(Object, ISurrogateSelector):
    """"""
    def __init__(self) -> None:
        """"""
    def AddSurrogate(
        self, type: Type, context: StreamingContext, surrogate: ISerializationSurrogate
    ) -> None:
        """"""
    def ChainSelector(self, selector: ISurrogateSelector) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetNextSelector(self) -> ISurrogateSelector:
        """"""
    def GetSurrogate(
        self, type: Type, context: StreamingContext, selector: ISurrogateSelector
    ) -> tuple[ISerializationSurrogate, ISurrogateSelector]:
        """"""
    def GetType(self) -> Type:
        """"""
    def RemoveSurrogate(self, type: Type, context: StreamingContext) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class TypeLoadExceptionHolder(Object):
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
class ValueTypeFixupInfo(Object):
    """"""
    def __init__(self, containerID: int, member: FieldInfo, parentIndex: Array[int]) -> None:
        """"""
    @property
    def ContainerID(self) -> int:
        """"""
    @property
    def ParentField(self) -> FieldInfo:
        """"""
    @property
    def ParentIndex(self) -> Array[int]:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
