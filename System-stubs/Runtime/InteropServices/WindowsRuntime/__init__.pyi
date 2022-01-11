from __future__ import annotations

from abc import ABC
from typing import Callable, Generic, List, Protocol, Tuple, TypeVar, Union, overload

from System import Action, Array, AsyncCallback, Attribute, Boolean, Byte, Char, DateTimeOffset, Double, Enum, EventArgs, EventHandler, Func, Guid, IAsyncResult, ICloneable, IDisposable, Int16, Int32, Int64, IntPtr, MarshalByRefObject, MulticastDelegate, Object, Single, String, TimeSpan, Type, UInt16, UInt32, UInt64, ValueType, Void, __ComObject
from System.Collections import ICollection, IEnumerable, IEnumerator, IList
from System.Collections.Generic import ICollection, IDictionary, IEnumerable, IEnumerator, IReadOnlyDictionary, IReadOnlyList, KeyValuePair
from System.Collections.ObjectModel import Collection
from System.Collections.Specialized import NotifyCollectionChangedAction, NotifyCollectionChangedEventArgs, NotifyCollectionChangedEventHandler
from System.ComponentModel import PropertyChangedEventArgs, PropertyChangedEventHandler
from System.Reflection import Assembly, PropertyInfo
from System.Runtime.InteropServices import CustomQueryInterfaceResult, ICustomQueryInterface, _Attribute
from System.Runtime.Serialization import ISerializable

# ---------- Types ---------- #

K = TypeVar('K')
T = TypeVar('T')
T1 = TypeVar('T1')
T2 = TypeVar('T2')
TKey = TypeVar('TKey')
TValue = TypeVar('TValue')
V = TypeVar('V')

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
ByteType = Union[int, Byte]
CharType = Union[str, Char]
DoubleType = Union[float, Double]
FloatType = Union[float, Single]
IntType = Union[int, Int32]
LongType = Union[int, Int64]
NIntType = Union[int, IntPtr]
ObjectType = Object
ShortType = Union[int, Int16]
StringType = Union[str, String]
TypeType = Union[type, Type]
UIntType = Union[int, UInt32]
ULongType = Union[int, UInt64]
UShortType = Union[int, UInt16]
VoidType = Union[None, Void]


class EventType(Generic[T]):
    def __iadd__(self, other: T): ...
    
    def __isub__(self, other: T): ...



# ---------- Classes ---------- #

class BindableIterableToEnumerableAdapter(ObjectType):
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


class BindableVectorToCollectionAdapter(ObjectType):
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


class BindableVectorToListAdapter(ObjectType):
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


class CLRIKeyValuePairImpl(Generic[K, V], ObjectType, IKeyValuePair[K, V]):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, pair: KeyValuePair[K, V]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Key(self) -> K: ...
    
    @property
    def Value(self) -> V: ...
    
    # ---------- Methods ---------- #
    
    def ToString(self) -> StringType: ...
    
    def get_Key(self) -> K: ...
    
    def get_Value(self) -> V: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CLRIPropertyValueImpl(ObjectType, IPropertyValue):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def IsNumericScalar(self) -> BooleanType: ...
    
    @property
    def Type(self) -> PropertyType: ...
    
    # ---------- Methods ---------- #
    
    def GetBoolean(self) -> BooleanType: ...
    
    def GetBooleanArray(self) -> ArrayType[BooleanType]: ...
    
    def GetChar16(self) -> CharType: ...
    
    def GetChar16Array(self) -> ArrayType[CharType]: ...
    
    def GetDateTime(self) -> DateTimeOffset: ...
    
    def GetDateTimeArray(self) -> ArrayType[DateTimeOffset]: ...
    
    def GetDouble(self) -> DoubleType: ...
    
    def GetDoubleArray(self) -> ArrayType[DoubleType]: ...
    
    def GetGuid(self) -> Guid: ...
    
    def GetGuidArray(self) -> ArrayType[Guid]: ...
    
    def GetInspectable(self) -> ObjectType: ...
    
    def GetInspectableArray(self) -> ArrayType[ObjectType]: ...
    
    def GetInt16(self) -> ShortType: ...
    
    def GetInt16Array(self) -> ArrayType[ShortType]: ...
    
    def GetInt32(self) -> IntType: ...
    
    def GetInt32Array(self) -> ArrayType[IntType]: ...
    
    def GetInt64(self) -> LongType: ...
    
    def GetInt64Array(self) -> ArrayType[LongType]: ...
    
    def GetPoint(self) -> Point: ...
    
    def GetPointArray(self) -> ArrayType[Point]: ...
    
    def GetRect(self) -> Rect: ...
    
    def GetRectArray(self) -> ArrayType[Rect]: ...
    
    def GetSingle(self) -> FloatType: ...
    
    def GetSingleArray(self) -> ArrayType[FloatType]: ...
    
    def GetSize(self) -> Size: ...
    
    def GetSizeArray(self) -> ArrayType[Size]: ...
    
    def GetString(self) -> StringType: ...
    
    def GetStringArray(self) -> ArrayType[StringType]: ...
    
    def GetTimeSpan(self) -> TimeSpan: ...
    
    def GetTimeSpanArray(self) -> ArrayType[TimeSpan]: ...
    
    def GetUInt16(self) -> UShortType: ...
    
    def GetUInt16Array(self) -> ArrayType[UShortType]: ...
    
    def GetUInt32(self) -> UIntType: ...
    
    def GetUInt32Array(self) -> ArrayType[UIntType]: ...
    
    def GetUInt64(self) -> ULongType: ...
    
    def GetUInt64Array(self) -> ArrayType[ULongType]: ...
    
    def GetUInt8(self) -> ByteType: ...
    
    def GetUInt8Array(self) -> ArrayType[ByteType]: ...
    
    def ToString(self) -> StringType: ...
    
    def get_IsNumericScalar(self) -> BooleanType: ...
    
    def get_Type(self) -> PropertyType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CLRIReferenceArrayImpl(Generic[T], CLRIPropertyValueImpl, IPropertyValue, IReferenceArray[T], ICustomPropertyProvider, IList, ICollection, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, type: PropertyType, obj: ArrayType[T]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> ArrayType[T]: ...
    
    # ---------- Methods ---------- #
    
    def ToString(self) -> StringType: ...
    
    def get_Value(self) -> ArrayType[T]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CLRIReferenceImpl(Generic[T], CLRIPropertyValueImpl, IPropertyValue, IReference[T], ICustomPropertyProvider):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, type: PropertyType, obj: T): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> T: ...
    
    # ---------- Methods ---------- #
    
    def ToString(self) -> StringType: ...
    
    def get_Value(self) -> T: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ConstantSplittableMap(Generic[TKey, TValue], ObjectType, IMapView[TKey, TValue], IIterable[IKeyValuePair[TKey, TValue]], IEnumerable[IKeyValuePair[TKey, TValue]], IEnumerable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    def __getitem__(self, key: TKey) -> TValue: ...
    
    @property
    def Keys(self) -> IEnumerable[TKey]: ...
    
    @property
    def Size(self) -> UIntType: ...
    
    @property
    def Values(self) -> IEnumerable[TValue]: ...
    
    # ---------- Methods ---------- #
    
    def ContainsKey(self, key: TKey) -> BooleanType: ...
    
    def First(self) -> IIterator[IKeyValuePair[TKey, TValue]]: ...
    
    def GetEnumerator(self) -> IEnumerator[IKeyValuePair[TKey, TValue]]: ...
    
    def HasKey(self, key: TKey) -> BooleanType: ...
    
    def Lookup(self, key: TKey) -> TValue: ...
    
    def Split(self, firstPartition: IMapView[TKey, TValue], secondPartition: IMapView[TKey, TValue]) -> Tuple[VoidType, IMapView[TKey, TValue], IMapView[TKey, TValue]]: ...
    
    def TryGetValue(self, key: TKey, value: TValue) -> Tuple[BooleanType, TValue]: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_Item(self, key: TKey) -> TValue: ...
    
    def get_Keys(self) -> IEnumerable[TKey]: ...
    
    def get_Size(self) -> UIntType: ...
    
    def get_Values(self) -> IEnumerable[TValue]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CustomPropertyImpl(ObjectType, ICustomProperty):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, propertyInfo: PropertyInfo): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CanRead(self) -> BooleanType: ...
    
    @property
    def CanWrite(self) -> BooleanType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def Type(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def GetValue(self, target: ObjectType) -> ObjectType: ...
    
    @overload
    def GetValue(self, target: ObjectType, indexValue: ObjectType) -> ObjectType: ...
    
    @overload
    def SetValue(self, target: ObjectType, value: ObjectType) -> VoidType: ...
    
    @overload
    def SetValue(self, target: ObjectType, value: ObjectType, indexValue: ObjectType) -> VoidType: ...
    
    def get_CanRead(self) -> BooleanType: ...
    
    def get_CanWrite(self) -> BooleanType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_Type(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DefaultInterfaceAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, defaultInterface: TypeType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def DefaultInterface(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def get_DefaultInterface(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DesignerNamespaceResolveEventArgs(EventArgs):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, namespaceName: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def NamespaceName(self) -> StringType: ...
    
    @property
    def ResolvedAssemblyFiles(self) -> Collection[StringType]: ...
    
    # ---------- Methods ---------- #
    
    def get_NamespaceName(self) -> StringType: ...
    
    def get_ResolvedAssemblyFiles(self) -> Collection[StringType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DictionaryKeyCollection(Generic[TKey, TValue], ObjectType, ICollection[TKey], IEnumerable[TKey], IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, dictionary: IDictionary[TKey, TValue]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def Contains(self, item: TKey) -> BooleanType: ...
    
    def CopyTo(self, array: ArrayType[TKey], index: IntType) -> VoidType: ...
    
    def GetEnumerator(self) -> IEnumerator[TKey]: ...
    
    def get_Count(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DictionaryKeyEnumerator(Generic[TKey, TValue], ObjectType, IEnumerator[TKey], IDisposable, IEnumerator):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, dictionary: IDictionary[TKey, TValue]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Current(self) -> TKey: ...
    
    # ---------- Methods ---------- #
    
    def MoveNext(self) -> BooleanType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Current(self) -> TKey: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DictionaryToMapAdapter(ObjectType):
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


class DictionaryValueCollection(Generic[TKey, TValue], ObjectType, ICollection[TValue], IEnumerable[TValue], IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, dictionary: IDictionary[TKey, TValue]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def Contains(self, item: TValue) -> BooleanType: ...
    
    def CopyTo(self, array: ArrayType[TValue], index: IntType) -> VoidType: ...
    
    def GetEnumerator(self) -> IEnumerator[TValue]: ...
    
    def get_Count(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DictionaryValueEnumerator(Generic[TKey, TValue], ObjectType, IEnumerator[TValue], IDisposable, IEnumerator):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, dictionary: IDictionary[TKey, TValue]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Current(self) -> TValue: ...
    
    # ---------- Methods ---------- #
    
    def MoveNext(self) -> BooleanType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Current(self) -> TValue: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EnumerableToBindableIterableAdapter(ObjectType):
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


class EnumerableToIterableAdapter(ObjectType):
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


class EnumeratorToIteratorAdapter(Generic[T], ObjectType, IIterator[T], IBindableIterator):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Current(self) -> T: ...
    
    @property
    def HasCurrent(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def GetMany(self, items: ArrayType[T]) -> IntType: ...
    
    def MoveNext(self) -> BooleanType: ...
    
    def get_Current(self) -> T: ...
    
    def get_HasCurrent(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EventRegistrationTokenTable(Generic[T], ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def InvocationList(self) -> T: ...
    
    @InvocationList.setter
    def InvocationList(self, value: T) -> None: ...
    
    # ---------- Methods ---------- #
    
    def AddEventHandler(self, handler: T) -> EventRegistrationToken: ...
    
    @staticmethod
    def GetOrCreateEventRegistrationTokenTable(refEventTable: EventRegistrationTokenTable[T]) -> Tuple[EventRegistrationTokenTable[T], EventRegistrationTokenTable[T]]: ...
    
    @overload
    def RemoveEventHandler(self, token: EventRegistrationToken) -> VoidType: ...
    
    @overload
    def RemoveEventHandler(self, handler: T) -> VoidType: ...
    
    def get_InvocationList(self) -> T: ...
    
    def set_InvocationList(self, value: T) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class GetEnumerator_Delegate(Generic[T], MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> IEnumerator[T]: ...
    
    def Invoke(self) -> IEnumerator[T]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class IClosableToIDisposableAdapter(ObjectType):
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


class ICommandAdapterHelpers(ABC, ObjectType):
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


class ICommandToManagedAdapter(ObjectType):
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


class ICommandToWinRTAdapter(ObjectType):
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


class ICustomPropertyProviderImpl(ABC, ObjectType):
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


class ICustomPropertyProviderProxy(Generic[T1, T2], ObjectType, IGetProxyTarget, ICustomPropertyProvider, ICustomQueryInterface, IEnumerable, IBindableVector, IBindableIterable, IBindableVectorView):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetEnumerator(self) -> IEnumerator: ...
    
    def GetInterface(self, iid: Guid, ppv: NIntType) -> Tuple[CustomQueryInterfaceResult, Guid, NIntType]: ...
    
    def ToString(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class IDisposableToIClosableAdapter(ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class IMapViewToIReadOnlyDictionaryAdapter(ObjectType):
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


class IReadOnlyDictionaryToIMapViewAdapter(ObjectType):
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


class IReadOnlyListToIVectorViewAdapter(ObjectType):
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


class IReferenceFactory(ABC, ObjectType):
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


class IStringableHelper(ObjectType):
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


class IVectorViewToIReadOnlyListAdapter(ObjectType):
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


class Indexer_Get_Delegate(Generic[T], MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, index: IntType, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> T: ...
    
    def Invoke(self, index: IntType) -> T: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class InterfaceImplementedInVersionAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, interfaceType: TypeType, majorVersion: ByteType, minorVersion: ByteType, buildVersion: ByteType, revisionVersion: ByteType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def BuildVersion(self) -> ByteType: ...
    
    @property
    def InterfaceType(self) -> TypeType: ...
    
    @property
    def MajorVersion(self) -> ByteType: ...
    
    @property
    def MinorVersion(self) -> ByteType: ...
    
    @property
    def RevisionVersion(self) -> ByteType: ...
    
    # ---------- Methods ---------- #
    
    def get_BuildVersion(self) -> ByteType: ...
    
    def get_InterfaceType(self) -> TypeType: ...
    
    def get_MajorVersion(self) -> ByteType: ...
    
    def get_MinorVersion(self) -> ByteType: ...
    
    def get_RevisionVersion(self) -> ByteType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class IterableToEnumerableAdapter(ObjectType):
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


class IteratorToEnumeratorAdapter(Generic[T], ObjectType, IEnumerator[T], IDisposable, IEnumerator):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Current(self) -> T: ...
    
    # ---------- Methods ---------- #
    
    def Dispose(self) -> VoidType: ...
    
    def MoveNext(self) -> BooleanType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Current(self) -> T: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ListToBindableVectorAdapter(ObjectType):
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


class ListToBindableVectorViewAdapter(ObjectType, IBindableVectorView, IBindableIterable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Size(self) -> UIntType: ...
    
    # ---------- Methods ---------- #
    
    def First(self) -> IBindableIterator: ...
    
    def GetAt(self, index: UIntType) -> ObjectType: ...
    
    def IndexOf(self, value: ObjectType, index: UIntType) -> Tuple[BooleanType, UIntType]: ...
    
    def get_Size(self) -> UIntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ListToVectorAdapter(ObjectType):
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


class ManagedActivationFactory(ObjectType, IActivationFactory, IManagedActivationFactory):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def ActivateInstance(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MapToCollectionAdapter(ObjectType):
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


class MapToDictionaryAdapter(ObjectType):
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


class MapViewToReadOnlyCollectionAdapter(ObjectType):
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


class NamespaceResolveEventArgs(EventArgs):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, namespaceName: StringType, requestingAssembly: Assembly): ...
    
    # ---------- Properties ---------- #
    
    @property
    def NamespaceName(self) -> StringType: ...
    
    @property
    def RequestingAssembly(self) -> Assembly: ...
    
    @property
    def ResolvedAssemblies(self) -> Collection[Assembly]: ...
    
    # ---------- Methods ---------- #
    
    def get_NamespaceName(self) -> StringType: ...
    
    def get_RequestingAssembly(self) -> Assembly: ...
    
    def get_ResolvedAssemblies(self) -> Collection[Assembly]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class NotifyCollectionChangedEventArgsMarshaler(ABC, ObjectType):
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


class NotifyCollectionChangedEventHandler_WinRT(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, sender: ObjectType, e: NotifyCollectionChangedEventArgs, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, sender: ObjectType, e: NotifyCollectionChangedEventArgs) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class NotifyCollectionChangedToManagedAdapter(ObjectType):
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


class NotifyCollectionChangedToWinRTAdapter(ObjectType):
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


class NotifyPropertyChangedToManagedAdapter(ObjectType):
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


class NotifyPropertyChangedToWinRTAdapter(ObjectType):
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


class PropertyChangedEventArgsMarshaler(ABC, ObjectType):
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


class PropertyChangedEventHandler_WinRT(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, sender: ObjectType, e: PropertyChangedEventArgs, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, sender: ObjectType, e: PropertyChangedEventArgs) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ReadOnlyArrayAttribute(Attribute, _Attribute):
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


class ReadOnlyDictionaryKeyCollection(Generic[TKey, TValue], ObjectType, IEnumerable[TKey], IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, dictionary: IReadOnlyDictionary[TKey, TValue]): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetEnumerator(self) -> IEnumerator[TKey]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ReadOnlyDictionaryKeyEnumerator(Generic[TKey, TValue], ObjectType, IEnumerator[TKey], IDisposable, IEnumerator):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, dictionary: IReadOnlyDictionary[TKey, TValue]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Current(self) -> TKey: ...
    
    # ---------- Methods ---------- #
    
    def MoveNext(self) -> BooleanType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Current(self) -> TKey: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ReadOnlyDictionaryValueCollection(Generic[TKey, TValue], ObjectType, IEnumerable[TValue], IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, dictionary: IReadOnlyDictionary[TKey, TValue]): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetEnumerator(self) -> IEnumerator[TValue]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ReadOnlyDictionaryValueEnumerator(Generic[TKey, TValue], ObjectType, IEnumerator[TValue], IDisposable, IEnumerator):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, dictionary: IReadOnlyDictionary[TKey, TValue]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Current(self) -> TValue: ...
    
    # ---------- Methods ---------- #
    
    def MoveNext(self) -> BooleanType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Current(self) -> TValue: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ReturnValueNameAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, name: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Name(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_Name(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RuntimeClass(ABC, __ComObject):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UnsafeNativeMethods(ABC, ObjectType):
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


class VectorToCollectionAdapter(ObjectType):
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


class VectorToListAdapter(ObjectType):
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


class VectorViewToReadOnlyCollectionAdapter(ObjectType):
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


class WinRTClassActivator(MarshalByRefObject, IWinRTClassActivator):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def ActivateInstance(self, activatableClassId: StringType) -> ObjectType: ...
    
    def GetActivationFactory(self, activatableClassId: StringType, iid: Guid) -> Tuple[NIntType, Guid]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class WindowsFoundationEventHandler(Generic[T], MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, sender: ObjectType, args: T, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, sender: ObjectType, args: T) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class WindowsRuntimeBufferHelper(ABC, ObjectType):
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


class WindowsRuntimeImportAttribute(Attribute, _Attribute):
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


class WindowsRuntimeMarshal(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def AddEventHandler(addMethod: Func[T, EventRegistrationToken], removeMethod: Action[EventRegistrationToken], handler: T) -> VoidType: ...
    
    @staticmethod
    def FreeHString(ptr: NIntType) -> VoidType: ...
    
    @staticmethod
    def GetActivationFactory(type: TypeType) -> IActivationFactory: ...
    
    @staticmethod
    def PtrToStringHString(ptr: NIntType) -> StringType: ...
    
    @staticmethod
    def RemoveAllEventHandlers(removeMethod: Action[EventRegistrationToken]) -> VoidType: ...
    
    @staticmethod
    def RemoveEventHandler(removeMethod: Action[EventRegistrationToken], handler: T) -> VoidType: ...
    
    @staticmethod
    def StringToHString(s: StringType) -> NIntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class WindowsRuntimeMetadata(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    @overload
    def ResolveNamespace(namespaceName: StringType, packageGraphFilePaths: IEnumerable[StringType]) -> IEnumerable[StringType]: ...
    
    @staticmethod
    @overload
    def ResolveNamespace(namespaceName: StringType, windowsSdkFilePath: StringType, packageGraphFilePaths: IEnumerable[StringType]) -> IEnumerable[StringType]: ...
    
    @staticmethod
    def add_DesignerNamespaceResolve(value: EventHandler[DesignerNamespaceResolveEventArgs]) -> VoidType: ...
    
    @staticmethod
    def add_ReflectionOnlyNamespaceResolve(value: EventHandler[NamespaceResolveEventArgs]) -> VoidType: ...
    
    @staticmethod
    def remove_DesignerNamespaceResolve(value: EventHandler[DesignerNamespaceResolveEventArgs]) -> VoidType: ...
    
    @staticmethod
    def remove_ReflectionOnlyNamespaceResolve(value: EventHandler[NamespaceResolveEventArgs]) -> VoidType: ...
    
    # ---------- Events ---------- #
    
    DesignerNamespaceResolve: EventType[EventHandler[DesignerNamespaceResolveEventArgs]] = ...
    
    ReflectionOnlyNamespaceResolve: EventType[EventHandler[NamespaceResolveEventArgs]] = ...
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class WriteOnlyArrayAttribute(Attribute, _Attribute):
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


# ---------- Structs ---------- #

class EventRegistrationToken(ValueType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    @staticmethod
    def op_Equality(left: EventRegistrationToken, right: EventRegistrationToken) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(left: EventRegistrationToken, right: EventRegistrationToken) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class HSTRING_HEADER(ValueType):
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


class Point(ValueType):
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


class Rect(ValueType):
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


class Size(ValueType):
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


# ---------- Interfaces ---------- #

class IActivationFactory(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def ActivateInstance(self) -> ObjectType: ...
    
    # No Events


class IBindableIterable(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def First(self) -> IBindableIterator: ...
    
    # No Events


class IBindableIterator(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def Current(self) -> ObjectType: ...
    
    @property
    def HasCurrent(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def MoveNext(self) -> BooleanType: ...
    
    def get_Current(self) -> ObjectType: ...
    
    def get_HasCurrent(self) -> BooleanType: ...
    
    # No Events


class IBindableVector(Protocol, IBindableIterable):
    # ---------- Properties ---------- #
    
    @property
    def Size(self) -> UIntType: ...
    
    # ---------- Methods ---------- #
    
    def Append(self, value: ObjectType) -> VoidType: ...
    
    def Clear(self) -> VoidType: ...
    
    def GetAt(self, index: UIntType) -> ObjectType: ...
    
    def GetView(self) -> IBindableVectorView: ...
    
    def IndexOf(self, value: ObjectType, index: UIntType) -> Tuple[BooleanType, UIntType]: ...
    
    def InsertAt(self, index: UIntType, value: ObjectType) -> VoidType: ...
    
    def RemoveAt(self, index: UIntType) -> VoidType: ...
    
    def RemoveAtEnd(self) -> VoidType: ...
    
    def SetAt(self, index: UIntType, value: ObjectType) -> VoidType: ...
    
    def get_Size(self) -> UIntType: ...
    
    # No Events


class IBindableVectorView(Protocol, IBindableIterable):
    # ---------- Properties ---------- #
    
    @property
    def Size(self) -> UIntType: ...
    
    # ---------- Methods ---------- #
    
    def GetAt(self, index: UIntType) -> ObjectType: ...
    
    def IndexOf(self, value: ObjectType, index: UIntType) -> Tuple[BooleanType, UIntType]: ...
    
    def get_Size(self) -> UIntType: ...
    
    # No Events


class IClosable(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    # No Events


class ICommand_WinRT(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def CanExecute(self, parameter: ObjectType) -> BooleanType: ...
    
    def Execute(self, parameter: ObjectType) -> VoidType: ...
    
    def add_CanExecuteChanged(self, value: EventHandler[ObjectType]) -> EventRegistrationToken: ...
    
    def remove_CanExecuteChanged(self, token: EventRegistrationToken) -> VoidType: ...
    
    # No Events


class ICustomProperty(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def CanRead(self) -> BooleanType: ...
    
    @property
    def CanWrite(self) -> BooleanType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def Type(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def GetValue(self, target: ObjectType) -> ObjectType: ...
    
    @overload
    def GetValue(self, target: ObjectType, indexValue: ObjectType) -> ObjectType: ...
    
    @overload
    def SetValue(self, target: ObjectType, value: ObjectType) -> VoidType: ...
    
    @overload
    def SetValue(self, target: ObjectType, value: ObjectType, indexValue: ObjectType) -> VoidType: ...
    
    def get_CanRead(self) -> BooleanType: ...
    
    def get_CanWrite(self) -> BooleanType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_Type(self) -> TypeType: ...
    
    # No Events


class ICustomPropertyProvider(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def Type(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def GetCustomProperty(self, name: StringType) -> ICustomProperty: ...
    
    def GetIndexedProperty(self, name: StringType, indexParameterType: TypeType) -> ICustomProperty: ...
    
    def GetStringRepresentation(self) -> StringType: ...
    
    def get_Type(self) -> TypeType: ...
    
    # No Events


class IGetProxyTarget(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetTarget(self) -> ObjectType: ...
    
    # No Events


class IIterable(Protocol[T], IEnumerable[T], IEnumerable):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def First(self) -> IIterator[T]: ...
    
    # No Events


class IIterator(Protocol[T]):
    # ---------- Properties ---------- #
    
    @property
    def Current(self) -> T: ...
    
    @property
    def HasCurrent(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def GetMany(self, items: ArrayType[T]) -> Tuple[IntType, ArrayType[T]]: ...
    
    def MoveNext(self) -> BooleanType: ...
    
    def get_Current(self) -> T: ...
    
    def get_HasCurrent(self) -> BooleanType: ...
    
    # No Events


class IKeyValuePair(Protocol[K, V]):
    # ---------- Properties ---------- #
    
    @property
    def Key(self) -> K: ...
    
    @property
    def Value(self) -> V: ...
    
    # ---------- Methods ---------- #
    
    def get_Key(self) -> K: ...
    
    def get_Value(self) -> V: ...
    
    # No Events


class IManagedActivationFactory(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def RunClassConstructor(self) -> VoidType: ...
    
    # No Events


class IMap(Protocol[K, V], IIterable[IKeyValuePair[K, V]], IEnumerable[IKeyValuePair[K, V]], IEnumerable):
    # ---------- Properties ---------- #
    
    @property
    def Size(self) -> UIntType: ...
    
    # ---------- Methods ---------- #
    
    def Clear(self) -> VoidType: ...
    
    def GetView(self) -> IReadOnlyDictionary[K, V]: ...
    
    def HasKey(self, key: K) -> BooleanType: ...
    
    def Insert(self, key: K, value: V) -> BooleanType: ...
    
    def Lookup(self, key: K) -> V: ...
    
    def Remove(self, key: K) -> VoidType: ...
    
    def get_Size(self) -> UIntType: ...
    
    # No Events


class IMapView(Protocol[K, V], IIterable[IKeyValuePair[K, V]], IEnumerable[IKeyValuePair[K, V]], IEnumerable):
    # ---------- Properties ---------- #
    
    @property
    def Size(self) -> UIntType: ...
    
    # ---------- Methods ---------- #
    
    def HasKey(self, key: K) -> BooleanType: ...
    
    def Lookup(self, key: K) -> V: ...
    
    def Split(self, first: IMapView[K, V], second: IMapView[K, V]) -> Tuple[VoidType, IMapView[K, V], IMapView[K, V]]: ...
    
    def get_Size(self) -> UIntType: ...
    
    # No Events


class INotifyCollectionChangedEventArgs(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def Action(self) -> NotifyCollectionChangedAction: ...
    
    @property
    def NewItems(self) -> IList: ...
    
    @property
    def NewStartingIndex(self) -> IntType: ...
    
    @property
    def OldItems(self) -> IList: ...
    
    @property
    def OldStartingIndex(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def get_Action(self) -> NotifyCollectionChangedAction: ...
    
    def get_NewItems(self) -> IList: ...
    
    def get_NewStartingIndex(self) -> IntType: ...
    
    def get_OldItems(self) -> IList: ...
    
    def get_OldStartingIndex(self) -> IntType: ...
    
    # No Events


class INotifyCollectionChanged_WinRT(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def add_CollectionChanged(self, value: NotifyCollectionChangedEventHandler) -> EventRegistrationToken: ...
    
    def remove_CollectionChanged(self, token: EventRegistrationToken) -> VoidType: ...
    
    # No Events


class INotifyPropertyChanged_WinRT(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def add_PropertyChanged(self, value: PropertyChangedEventHandler) -> EventRegistrationToken: ...
    
    def remove_PropertyChanged(self, token: EventRegistrationToken) -> VoidType: ...
    
    # No Events


class IPropertyChangedEventArgs(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def PropertyName(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_PropertyName(self) -> StringType: ...
    
    # No Events


class IPropertyValue(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def IsNumericScalar(self) -> BooleanType: ...
    
    @property
    def Type(self) -> PropertyType: ...
    
    # ---------- Methods ---------- #
    
    def GetBoolean(self) -> BooleanType: ...
    
    def GetBooleanArray(self) -> ArrayType[BooleanType]: ...
    
    def GetChar16(self) -> CharType: ...
    
    def GetChar16Array(self) -> ArrayType[CharType]: ...
    
    def GetDateTime(self) -> DateTimeOffset: ...
    
    def GetDateTimeArray(self) -> ArrayType[DateTimeOffset]: ...
    
    def GetDouble(self) -> DoubleType: ...
    
    def GetDoubleArray(self) -> ArrayType[DoubleType]: ...
    
    def GetGuid(self) -> Guid: ...
    
    def GetGuidArray(self) -> ArrayType[Guid]: ...
    
    def GetInspectableArray(self) -> ArrayType[ObjectType]: ...
    
    def GetInt16(self) -> ShortType: ...
    
    def GetInt16Array(self) -> ArrayType[ShortType]: ...
    
    def GetInt32(self) -> IntType: ...
    
    def GetInt32Array(self) -> ArrayType[IntType]: ...
    
    def GetInt64(self) -> LongType: ...
    
    def GetInt64Array(self) -> ArrayType[LongType]: ...
    
    def GetPoint(self) -> Point: ...
    
    def GetPointArray(self) -> ArrayType[Point]: ...
    
    def GetRect(self) -> Rect: ...
    
    def GetRectArray(self) -> ArrayType[Rect]: ...
    
    def GetSingle(self) -> FloatType: ...
    
    def GetSingleArray(self) -> ArrayType[FloatType]: ...
    
    def GetSize(self) -> Size: ...
    
    def GetSizeArray(self) -> ArrayType[Size]: ...
    
    def GetString(self) -> StringType: ...
    
    def GetStringArray(self) -> ArrayType[StringType]: ...
    
    def GetTimeSpan(self) -> TimeSpan: ...
    
    def GetTimeSpanArray(self) -> ArrayType[TimeSpan]: ...
    
    def GetUInt16(self) -> UShortType: ...
    
    def GetUInt16Array(self) -> ArrayType[UShortType]: ...
    
    def GetUInt32(self) -> UIntType: ...
    
    def GetUInt32Array(self) -> ArrayType[UIntType]: ...
    
    def GetUInt64(self) -> ULongType: ...
    
    def GetUInt64Array(self) -> ArrayType[ULongType]: ...
    
    def GetUInt8(self) -> ByteType: ...
    
    def GetUInt8Array(self) -> ArrayType[ByteType]: ...
    
    def get_IsNumericScalar(self) -> BooleanType: ...
    
    def get_Type(self) -> PropertyType: ...
    
    # No Events


class IReference(Protocol[T], IPropertyValue):
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> T: ...
    
    # ---------- Methods ---------- #
    
    def get_Value(self) -> T: ...
    
    # No Events


class IReferenceArray(Protocol[T], IPropertyValue):
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> ArrayType[T]: ...
    
    # ---------- Methods ---------- #
    
    def get_Value(self) -> ArrayType[T]: ...
    
    # No Events


class IRestrictedErrorInfo(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetErrorDetails(self, description: StringType, error: IntType, restrictedDescription: StringType, capabilitySid: StringType) -> Tuple[VoidType, StringType, IntType, StringType, StringType]: ...
    
    def GetReference(self, reference: StringType) -> Tuple[VoidType, StringType]: ...
    
    # No Events


class IStringable(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def ToString(self) -> StringType: ...
    
    # No Events


class IVector(Protocol[T], IIterable[T], IEnumerable[T], IEnumerable):
    # ---------- Properties ---------- #
    
    @property
    def Size(self) -> UIntType: ...
    
    # ---------- Methods ---------- #
    
    def Append(self, value: T) -> VoidType: ...
    
    def Clear(self) -> VoidType: ...
    
    def GetAt(self, index: UIntType) -> T: ...
    
    def GetMany(self, startIndex: UIntType, items: ArrayType[T]) -> Tuple[UIntType, ArrayType[T]]: ...
    
    def GetView(self) -> IReadOnlyList[T]: ...
    
    def IndexOf(self, value: T, index: UIntType) -> Tuple[BooleanType, UIntType]: ...
    
    def InsertAt(self, index: UIntType, value: T) -> VoidType: ...
    
    def RemoveAt(self, index: UIntType) -> VoidType: ...
    
    def RemoveAtEnd(self) -> VoidType: ...
    
    def ReplaceAll(self, items: ArrayType[T]) -> VoidType: ...
    
    def SetAt(self, index: UIntType, value: T) -> VoidType: ...
    
    def get_Size(self) -> UIntType: ...
    
    # No Events


class IVectorView(Protocol[T], IIterable[T], IEnumerable[T], IEnumerable):
    # ---------- Properties ---------- #
    
    @property
    def Size(self) -> UIntType: ...
    
    # ---------- Methods ---------- #
    
    def GetAt(self, index: UIntType) -> T: ...
    
    def GetMany(self, startIndex: UIntType, items: ArrayType[T]) -> Tuple[UIntType, ArrayType[T]]: ...
    
    def IndexOf(self, value: T, index: UIntType) -> Tuple[BooleanType, UIntType]: ...
    
    def get_Size(self) -> UIntType: ...
    
    # No Events


class IVector_Raw(Protocol[T], IIterable[T], IEnumerable[T], IEnumerable):
    # ---------- Properties ---------- #
    
    @property
    def Size(self) -> UIntType: ...
    
    # ---------- Methods ---------- #
    
    def Append(self, value: T) -> VoidType: ...
    
    def Clear(self) -> VoidType: ...
    
    def GetAt(self, index: UIntType) -> T: ...
    
    def GetMany(self, startIndex: UIntType, items: ArrayType[T]) -> Tuple[UIntType, ArrayType[T]]: ...
    
    def GetView(self) -> IVectorView[T]: ...
    
    def IndexOf(self, value: T, index: UIntType) -> Tuple[BooleanType, UIntType]: ...
    
    def InsertAt(self, index: UIntType, value: T) -> VoidType: ...
    
    def RemoveAt(self, index: UIntType) -> VoidType: ...
    
    def RemoveAtEnd(self) -> VoidType: ...
    
    def ReplaceAll(self, items: ArrayType[T]) -> VoidType: ...
    
    def SetAt(self, index: UIntType, value: T) -> VoidType: ...
    
    def get_Size(self) -> UIntType: ...
    
    # No Events


class IWinRTClassActivator(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def ActivateInstance(self, activatableClassId: StringType) -> ObjectType: ...
    
    def GetActivationFactory(self, activatableClassId: StringType, iid: Guid) -> Tuple[NIntType, Guid]: ...
    
    # No Events


# ---------- Enums ---------- #

class InterfaceForwardingSupport(Enum):
    #None: IntType = 0
    IBindableVector: IntType = 1
    IVector: IntType = 2
    IBindableVectorView: IntType = 4
    IVectorView: IntType = 8
    IBindableIterableOrIIterable: IntType = 16


class PropertyType(Enum):
    Empty: IntType = 0
    UInt8: IntType = 1
    Int16: IntType = 2
    UInt16: IntType = 3
    Int32: IntType = 4
    UInt32: IntType = 5
    Int64: IntType = 6
    UInt64: IntType = 7
    Single: IntType = 8
    Double: IntType = 9
    Char16: IntType = 10
    Boolean: IntType = 11
    String: IntType = 12
    Inspectable: IntType = 13
    DateTime: IntType = 14
    TimeSpan: IntType = 15
    Guid: IntType = 16
    Point: IntType = 17
    Size: IntType = 18
    Rect: IntType = 19
    Other: IntType = 20
    UInt8Array: IntType = 1025
    Int16Array: IntType = 1026
    UInt16Array: IntType = 1027
    Int32Array: IntType = 1028
    UInt32Array: IntType = 1029
    Int64Array: IntType = 1030
    UInt64Array: IntType = 1031
    SingleArray: IntType = 1032
    DoubleArray: IntType = 1033
    Char16Array: IntType = 1034
    BooleanArray: IntType = 1035
    StringArray: IntType = 1036
    InspectableArray: IntType = 1037
    DateTimeArray: IntType = 1038
    TimeSpanArray: IntType = 1039
    GuidArray: IntType = 1040
    PointArray: IntType = 1041
    SizeArray: IntType = 1042
    RectArray: IntType = 1043
    OtherArray: IntType = 1044


# ---------- Delegates ---------- #

GetEnumerator_Delegate = Callable[[], IEnumerator[T]]

Indexer_Get_Delegate = Callable[[IntType], T]

NotifyCollectionChangedEventHandler_WinRT = Callable[[ObjectType, NotifyCollectionChangedEventArgs], VoidType]

PropertyChangedEventHandler_WinRT = Callable[[ObjectType, PropertyChangedEventArgs], VoidType]

WindowsFoundationEventHandler = Callable[[ObjectType, T], VoidType]

__all__ = [
    BindableIterableToEnumerableAdapter,
    BindableVectorToCollectionAdapter,
    BindableVectorToListAdapter,
    CLRIKeyValuePairImpl,
    CLRIPropertyValueImpl,
    CLRIReferenceArrayImpl,
    CLRIReferenceImpl,
    ConstantSplittableMap,
    CustomPropertyImpl,
    DefaultInterfaceAttribute,
    DesignerNamespaceResolveEventArgs,
    DictionaryKeyCollection,
    DictionaryKeyEnumerator,
    DictionaryToMapAdapter,
    DictionaryValueCollection,
    DictionaryValueEnumerator,
    EnumerableToBindableIterableAdapter,
    EnumerableToIterableAdapter,
    EnumeratorToIteratorAdapter,
    EventRegistrationTokenTable,
    GetEnumerator_Delegate,
    IClosableToIDisposableAdapter,
    ICommandAdapterHelpers,
    ICommandToManagedAdapter,
    ICommandToWinRTAdapter,
    ICustomPropertyProviderImpl,
    ICustomPropertyProviderProxy,
    IDisposableToIClosableAdapter,
    IMapViewToIReadOnlyDictionaryAdapter,
    IReadOnlyDictionaryToIMapViewAdapter,
    IReadOnlyListToIVectorViewAdapter,
    IReferenceFactory,
    IStringableHelper,
    IVectorViewToIReadOnlyListAdapter,
    Indexer_Get_Delegate,
    InterfaceImplementedInVersionAttribute,
    IterableToEnumerableAdapter,
    IteratorToEnumeratorAdapter,
    ListToBindableVectorAdapter,
    ListToBindableVectorViewAdapter,
    ListToVectorAdapter,
    ManagedActivationFactory,
    MapToCollectionAdapter,
    MapToDictionaryAdapter,
    MapViewToReadOnlyCollectionAdapter,
    NamespaceResolveEventArgs,
    NotifyCollectionChangedEventArgsMarshaler,
    NotifyCollectionChangedEventHandler_WinRT,
    NotifyCollectionChangedToManagedAdapter,
    NotifyCollectionChangedToWinRTAdapter,
    NotifyPropertyChangedToManagedAdapter,
    NotifyPropertyChangedToWinRTAdapter,
    PropertyChangedEventArgsMarshaler,
    PropertyChangedEventHandler_WinRT,
    ReadOnlyArrayAttribute,
    ReadOnlyDictionaryKeyCollection,
    ReadOnlyDictionaryKeyEnumerator,
    ReadOnlyDictionaryValueCollection,
    ReadOnlyDictionaryValueEnumerator,
    ReturnValueNameAttribute,
    RuntimeClass,
    UnsafeNativeMethods,
    VectorToCollectionAdapter,
    VectorToListAdapter,
    VectorViewToReadOnlyCollectionAdapter,
    WinRTClassActivator,
    WindowsFoundationEventHandler,
    WindowsRuntimeBufferHelper,
    WindowsRuntimeImportAttribute,
    WindowsRuntimeMarshal,
    WindowsRuntimeMetadata,
    WriteOnlyArrayAttribute,
    EventRegistrationToken,
    HSTRING_HEADER,
    Point,
    Rect,
    Size,
    IActivationFactory,
    IBindableIterable,
    IBindableIterator,
    IBindableVector,
    IBindableVectorView,
    IClosable,
    ICommand_WinRT,
    ICustomProperty,
    ICustomPropertyProvider,
    IGetProxyTarget,
    IIterable,
    IIterator,
    IKeyValuePair,
    IManagedActivationFactory,
    IMap,
    IMapView,
    INotifyCollectionChangedEventArgs,
    INotifyCollectionChanged_WinRT,
    INotifyPropertyChanged_WinRT,
    IPropertyChangedEventArgs,
    IPropertyValue,
    IReference,
    IReferenceArray,
    IRestrictedErrorInfo,
    IStringable,
    IVector,
    IVectorView,
    IVector_Raw,
    IWinRTClassActivator,
    InterfaceForwardingSupport,
    PropertyType,
    GetEnumerator_Delegate,
    Indexer_Get_Delegate,
    NotifyCollectionChangedEventHandler_WinRT,
    PropertyChangedEventHandler_WinRT,
    WindowsFoundationEventHandler,
]
