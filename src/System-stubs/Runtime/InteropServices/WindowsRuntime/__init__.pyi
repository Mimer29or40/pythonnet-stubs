"""Automatically generated stubs for C# namespace: System.Runtime.InteropServices.WindowsRuntime."""

from abc import ABC
from collections.abc import Callable
from collections.abc import Iterator
from typing import Self
from typing import overload

from System import Action
from System import Array
from System import Attribute
from System import Char
from System import DateTimeOffset
from System import Enum
from System import EventArgs
from System import EventHandler
from System import Func
from System import Guid
from System import IDisposable
from System import Int32
from System import IntPtr
from System import MarshalByRefObject
from System import Object
from System import String
from System import TimeSpan
from System import Type
from System import UInt32
from System import ValueType
from System import __ComObject
from System.Collections import ICollection
from System.Collections import IEnumerable
from System.Collections import IEnumerator
from System.Collections import IList
from System.Collections.Generic import ICollection
from System.Collections.Generic import IDictionary
from System.Collections.Generic import IEnumerable
from System.Collections.Generic import IEnumerator
from System.Collections.Generic import IReadOnlyDictionary
from System.Collections.Generic import IReadOnlyList
from System.Collections.Generic import KeyValuePair
from System.Collections.ObjectModel import Collection
from System.Collections.Specialized import NotifyCollectionChangedAction
from System.Collections.Specialized import NotifyCollectionChangedEventArgs
from System.ComponentModel import PropertyChangedEventArgs
from System.Reflection import Assembly
from System.Reflection import PropertyInfo
from System.Runtime.InteropServices import CustomQueryInterfaceResult
from System.Runtime.InteropServices import ICustomQueryInterface
from System.Runtime.InteropServices import _Attribute
from System.Runtime.Remoting import ObjRef

class EventType[T]:
    def __iadd__(self, other: T) -> Self: ...
    def __isub__(self, other: T) -> Self: ...

class BindableIterableToEnumerableAdapter(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class BindableVectorToCollectionAdapter(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class BindableVectorToListAdapter(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class CLRIKeyValuePairImpl[K, V](Object, IKeyValuePair[K, V]):
    """"""
    def __init__(self, pair: KeyValuePair[K, V]) -> None:
        """"""
    @property
    def Key(self) -> K:
        """"""
    @property
    def Value(self) -> V:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class CLRIPropertyValueImpl(Object, IPropertyValue):
    """"""
    @property
    def IsNumericScalar(self) -> bool:
        """"""
    @property
    def Type(self) -> PropertyType:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetBoolean(self) -> bool:
        """"""
    def GetBooleanArray(self) -> Array[bool]:
        """"""
    def GetChar16(self) -> Char:
        """"""
    def GetChar16Array(self) -> Array[Char]:
        """"""
    def GetDateTime(self) -> DateTimeOffset:
        """"""
    def GetDateTimeArray(self) -> Array[DateTimeOffset]:
        """"""
    def GetDouble(self) -> float:
        """"""
    def GetDoubleArray(self) -> Array[float]:
        """"""
    def GetGuid(self) -> Guid:
        """"""
    def GetGuidArray(self) -> Array[Guid]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetInspectable(self) -> object:
        """"""
    def GetInspectableArray(self) -> Array[object]:
        """"""
    def GetInt16(self) -> int:
        """"""
    def GetInt16Array(self) -> Array[int]:
        """"""
    def GetInt32(self) -> int:
        """"""
    def GetInt32Array(self) -> Array[int]:
        """"""
    def GetInt64(self) -> int:
        """"""
    def GetInt64Array(self) -> Array[int]:
        """"""
    def GetPoint(self) -> Point:
        """"""
    def GetPointArray(self) -> Array[Point]:
        """"""
    def GetRect(self) -> Rect:
        """"""
    def GetRectArray(self) -> Array[Rect]:
        """"""
    def GetSingle(self) -> float:
        """"""
    def GetSingleArray(self) -> Array[float]:
        """"""
    def GetSize(self) -> Size:
        """"""
    def GetSizeArray(self) -> Array[Size]:
        """"""
    def GetString(self) -> str:
        """"""
    def GetStringArray(self) -> Array[str]:
        """"""
    def GetTimeSpan(self) -> TimeSpan:
        """"""
    def GetTimeSpanArray(self) -> Array[TimeSpan]:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetUInt16(self) -> int:
        """"""
    def GetUInt16Array(self) -> Array[int]:
        """"""
    def GetUInt32(self) -> int:
        """"""
    def GetUInt32Array(self) -> Array[int]:
        """"""
    def GetUInt64(self) -> int:
        """"""
    def GetUInt64Array(self) -> Array[int]:
        """"""
    def GetUInt8(self) -> int:
        """"""
    def GetUInt8Array(self) -> Array[int]:
        """"""
    def ToString(self) -> str:
        """"""

class CLRIReferenceArrayImpl[T](
    CLRIPropertyValueImpl,
    ICollection,
    IEnumerable,
    IList,
    ICustomPropertyProvider,
    IPropertyValue,
    IReferenceArray[T],
):
    """"""
    def __init__(self, type: PropertyType, obj: Array[T]) -> None:
        """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsFixedSize(self) -> bool:
        """"""
    @property
    def IsNumericScalar(self) -> bool:
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
    def SyncRoot(self) -> object:
        """"""
    @property
    def Type(self) -> PropertyType:
        """"""
    @property
    def Value(self) -> Array[T]:
        """"""
    def Add(self, value: object) -> int:
        """"""
    def Clear(self) -> None:
        """"""
    def Contains(self, value: object) -> bool:
        """"""
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetBoolean(self) -> bool:
        """"""
    def GetBooleanArray(self) -> Array[bool]:
        """"""
    def GetChar16(self) -> Char:
        """"""
    def GetChar16Array(self) -> Array[Char]:
        """"""
    def GetCustomProperty(self, name: str) -> ICustomProperty:
        """"""
    def GetDateTime(self) -> DateTimeOffset:
        """"""
    def GetDateTimeArray(self) -> Array[DateTimeOffset]:
        """"""
    def GetDouble(self) -> float:
        """"""
    def GetDoubleArray(self) -> Array[float]:
        """"""
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def GetGuid(self) -> Guid:
        """"""
    def GetGuidArray(self) -> Array[Guid]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIndexedProperty(self, name: str, indexParameterType: Type) -> ICustomProperty:
        """"""
    def GetInspectable(self) -> object:
        """"""
    def GetInspectableArray(self) -> Array[object]:
        """"""
    def GetInt16(self) -> int:
        """"""
    def GetInt16Array(self) -> Array[int]:
        """"""
    def GetInt32(self) -> int:
        """"""
    def GetInt32Array(self) -> Array[int]:
        """"""
    def GetInt64(self) -> int:
        """"""
    def GetInt64Array(self) -> Array[int]:
        """"""
    def GetPoint(self) -> Point:
        """"""
    def GetPointArray(self) -> Array[Point]:
        """"""
    def GetRect(self) -> Rect:
        """"""
    def GetRectArray(self) -> Array[Rect]:
        """"""
    def GetSingle(self) -> float:
        """"""
    def GetSingleArray(self) -> Array[float]:
        """"""
    def GetSize(self) -> Size:
        """"""
    def GetSizeArray(self) -> Array[Size]:
        """"""
    def GetString(self) -> str:
        """"""
    def GetStringArray(self) -> Array[str]:
        """"""
    def GetStringRepresentation(self) -> str:
        """"""
    def GetTimeSpan(self) -> TimeSpan:
        """"""
    def GetTimeSpanArray(self) -> Array[TimeSpan]:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetUInt16(self) -> int:
        """"""
    def GetUInt16Array(self) -> Array[int]:
        """"""
    def GetUInt32(self) -> int:
        """"""
    def GetUInt32Array(self) -> Array[int]:
        """"""
    def GetUInt64(self) -> int:
        """"""
    def GetUInt64Array(self) -> Array[int]:
        """"""
    def GetUInt8(self) -> int:
        """"""
    def GetUInt8Array(self) -> Array[int]:
        """"""
    def IndexOf(self, value: object) -> int:
        """"""
    def Insert(self, index: int, value: object) -> None:
        """"""
    def Remove(self, value: object) -> None:
        """"""
    def RemoveAt(self, index: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def __contains__(self, value: object) -> bool:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    def __delitem__(self, value: object) -> None:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, index: int) -> object:
        """"""
    def __setitem__(self, index: int, value: object) -> None:
        """"""

class CLRIReferenceImpl[T](
    CLRIPropertyValueImpl, ICustomPropertyProvider, IPropertyValue, IReference[T]
):
    """"""
    def __init__(self, type: PropertyType, obj: T) -> None:
        """"""
    @property
    def IsNumericScalar(self) -> bool:
        """"""
    @property
    def Type(self) -> PropertyType:
        """"""
    @property
    def Value(self) -> T:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetBoolean(self) -> bool:
        """"""
    def GetBooleanArray(self) -> Array[bool]:
        """"""
    def GetChar16(self) -> Char:
        """"""
    def GetChar16Array(self) -> Array[Char]:
        """"""
    def GetCustomProperty(self, name: str) -> ICustomProperty:
        """"""
    def GetDateTime(self) -> DateTimeOffset:
        """"""
    def GetDateTimeArray(self) -> Array[DateTimeOffset]:
        """"""
    def GetDouble(self) -> float:
        """"""
    def GetDoubleArray(self) -> Array[float]:
        """"""
    def GetGuid(self) -> Guid:
        """"""
    def GetGuidArray(self) -> Array[Guid]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIndexedProperty(self, name: str, indexParameterType: Type) -> ICustomProperty:
        """"""
    def GetInspectable(self) -> object:
        """"""
    def GetInspectableArray(self) -> Array[object]:
        """"""
    def GetInt16(self) -> int:
        """"""
    def GetInt16Array(self) -> Array[int]:
        """"""
    def GetInt32(self) -> int:
        """"""
    def GetInt32Array(self) -> Array[int]:
        """"""
    def GetInt64(self) -> int:
        """"""
    def GetInt64Array(self) -> Array[int]:
        """"""
    def GetPoint(self) -> Point:
        """"""
    def GetPointArray(self) -> Array[Point]:
        """"""
    def GetRect(self) -> Rect:
        """"""
    def GetRectArray(self) -> Array[Rect]:
        """"""
    def GetSingle(self) -> float:
        """"""
    def GetSingleArray(self) -> Array[float]:
        """"""
    def GetSize(self) -> Size:
        """"""
    def GetSizeArray(self) -> Array[Size]:
        """"""
    def GetString(self) -> str:
        """"""
    def GetStringArray(self) -> Array[str]:
        """"""
    def GetStringRepresentation(self) -> str:
        """"""
    def GetTimeSpan(self) -> TimeSpan:
        """"""
    def GetTimeSpanArray(self) -> Array[TimeSpan]:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetUInt16(self) -> int:
        """"""
    def GetUInt16Array(self) -> Array[int]:
        """"""
    def GetUInt32(self) -> int:
        """"""
    def GetUInt32Array(self) -> Array[int]:
        """"""
    def GetUInt64(self) -> int:
        """"""
    def GetUInt64Array(self) -> Array[int]:
        """"""
    def GetUInt8(self) -> int:
        """"""
    def GetUInt8Array(self) -> Array[int]:
        """"""
    def ToString(self) -> str:
        """"""

class ConstantSplittableMap[TKey, TValue](
    Object,
    IEnumerable[IKeyValuePair[TKey, TValue]],
    IEnumerable,
    IIterable[IKeyValuePair[TKey, TValue]],
    IMapView[TKey, TValue],
):
    """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def Item(self) -> TValue:
        """"""
    @property
    def Keys(self) -> IEnumerable[TKey]:
        """"""
    @property
    def Size(self) -> int:
        """"""
    @property
    def Values(self) -> IEnumerable[TValue]:
        """"""
    def ContainsKey[TKey](self, key: TKey) -> bool:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def First(self) -> IIterator[IKeyValuePair[TKey, TValue]]:
        """"""
    def GetEnumerator(self) -> IEnumerator[IKeyValuePair[TKey, TValue]]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def HasKey[TKey](self, key: TKey) -> bool:
        """"""
    def Lookup[TKey, TValue](self, key: TKey) -> TValue:
        """"""
    def Split(
        self, firstPartition: IMapView[TKey, TValue], secondPartition: IMapView[TKey, TValue]
    ) -> tuple[None, IMapView[TKey, TValue], IMapView[TKey, TValue]]:
        """"""
    def ToString(self) -> str:
        """"""
    def TryGetValue[TKey](self, key: TKey, value: TValue) -> tuple[bool, TValue]:
        """"""
    def __contains__[TKey](self, key: TKey) -> bool:
        """"""
    def __iter__(self) -> Iterator[IKeyValuePair[TKey, TValue]]:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__[TKey, TValue](self, key: TKey) -> TValue:
        """"""

class CustomPropertyImpl(Object, ICustomProperty):
    """"""
    def __init__(self, propertyInfo: PropertyInfo) -> None:
        """"""
    @property
    def CanRead(self) -> bool:
        """"""
    @property
    def CanWrite(self) -> bool:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def Type(self) -> Type:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def GetValue(self, target: object) -> object:
        """"""
    @overload
    def GetValue(self, target: object, indexValue: object) -> object:
        """"""
    @overload
    def SetValue(self, target: object, value: object) -> None:
        """"""
    @overload
    def SetValue(self, target: object, value: object, indexValue: object) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class DefaultInterfaceAttribute(Attribute, _Attribute):
    """"""
    def __init__(self, defaultInterface: Type) -> None:
        """"""
    @property
    def DefaultInterface(self) -> Type:
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

class DesignerNamespaceResolveEventArgs(EventArgs):
    """"""
    def __init__(self, namespaceName: str) -> None:
        """"""
    @property
    def NamespaceName(self) -> str:
        """"""
    @property
    def ResolvedAssemblyFiles(self) -> Collection[str]:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class DictionaryKeyCollection[TKey, TValue](
    Object, ICollection[TKey], IEnumerable[TKey], IEnumerable
):
    """"""
    def __init__(self, dictionary: IDictionary[TKey, TValue]) -> None:
        """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    def Add[TKey](self, item: TKey) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    def Contains[TKey](self, item: TKey) -> bool:
        """"""
    def CopyTo(self, array: Array[TKey], index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator[TKey]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Remove[TKey](self, item: TKey) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    def __contains__[TKey](self, item: TKey) -> bool:
        """"""
    def __iter__(self) -> Iterator[TKey]:
        """"""
    def __delitem__[TKey](self, item: TKey) -> bool:
        """"""
    def __len__(self) -> int:
        """"""

class DictionaryKeyEnumerator[TKey, TValue](Object, IEnumerator[TKey], IEnumerator, IDisposable):
    """"""
    def __init__(self, dictionary: IDictionary[TKey, TValue]) -> None:
        """"""
    @property
    def Current(self) -> TKey:
        """"""
    def Dispose(self) -> None:
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

class DictionaryToMapAdapter(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class DictionaryValueCollection[TKey, TValue](
    Object, ICollection[TValue], IEnumerable[TValue], IEnumerable
):
    """"""
    def __init__(self, dictionary: IDictionary[TKey, TValue]) -> None:
        """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    def Add[TValue](self, item: TValue) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    def Contains[TValue](self, item: TValue) -> bool:
        """"""
    def CopyTo(self, array: Array[TValue], index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator[TValue]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Remove[TValue](self, item: TValue) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    def __contains__[TValue](self, item: TValue) -> bool:
        """"""
    def __iter__(self) -> Iterator[TValue]:
        """"""
    def __delitem__[TValue](self, item: TValue) -> bool:
        """"""
    def __len__(self) -> int:
        """"""

class DictionaryValueEnumerator[TKey, TValue](
    Object, IEnumerator[TValue], IEnumerator, IDisposable
):
    """"""
    def __init__(self, dictionary: IDictionary[TKey, TValue]) -> None:
        """"""
    @property
    def Current(self) -> TValue:
        """"""
    def Dispose(self) -> None:
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

class EnumerableToBindableIterableAdapter(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class EnumerableToIterableAdapter(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class EnumeratorToIteratorAdapter[T](Object, IBindableIterator, IIterator[T]):
    """"""
    @property
    def Current(self) -> T:
        """"""
    @property
    def HasCurrent(self) -> bool:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetMany(self, items: Array[T]) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def MoveNext(self) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

class EventRegistrationToken(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def op_Equality(cls, left: EventRegistrationToken, right: EventRegistrationToken) -> bool:
        """"""
    @classmethod
    def op_Inequality(cls, left: EventRegistrationToken, right: EventRegistrationToken) -> bool:
        """"""
    def __eq__(self, other: EventRegistrationToken) -> bool:
        """"""
    def __ne__(self, other: EventRegistrationToken) -> bool:
        """"""

class EventRegistrationTokenTable[T](Object):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def InvocationList(self) -> T:
        """"""
    @InvocationList.setter
    def InvocationList(self, value: T) -> None: ...
    def AddEventHandler[T](self, handler: T) -> EventRegistrationToken:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @classmethod
    def GetOrCreateEventRegistrationTokenTable(
        cls, refEventTable: EventRegistrationTokenTable[T]
    ) -> EventRegistrationTokenTable[T]:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def RemoveEventHandler[T](self, handler: T) -> None:
        """"""
    @overload
    def RemoveEventHandler(self, token: EventRegistrationToken) -> None:
        """"""
    def ToString(self) -> str:
        """"""

GetEnumerator_Delegate: Callable[[], IEnumerator[T]] = ...
""""""

class HSTRING_HEADER(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class IActivationFactory:
    """"""
    def ActivateInstance(self) -> object:
        """"""

class IBindableIterable:
    """"""
    def First(self) -> IBindableIterator:
        """"""

class IBindableIterator:
    """"""
    @property
    def Current(self) -> object:
        """"""
    @property
    def HasCurrent(self) -> bool:
        """"""
    def MoveNext(self) -> bool:
        """"""

class IBindableVector(IBindableIterable):
    """"""
    @property
    def Size(self) -> int:
        """"""
    def Append(self, value: object) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    def First(self) -> IBindableIterator:
        """"""
    def GetAt(self, index: int) -> object:
        """"""
    def GetView(self) -> IBindableVectorView:
        """"""
    def IndexOf(self, value: object, index: UInt32) -> tuple[bool, UInt32]:
        """"""
    def InsertAt(self, index: int, value: object) -> None:
        """"""
    def RemoveAt(self, index: int) -> None:
        """"""
    def RemoveAtEnd(self) -> None:
        """"""
    def SetAt(self, index: int, value: object) -> None:
        """"""

class IBindableVectorView(IBindableIterable):
    """"""
    @property
    def Size(self) -> int:
        """"""
    def First(self) -> IBindableIterator:
        """"""
    def GetAt(self, index: int) -> object:
        """"""
    def IndexOf(self, value: object, index: UInt32) -> tuple[bool, UInt32]:
        """"""

class IClosable:
    """"""
    def Close(self) -> None:
        """"""

class IClosableToIDisposableAdapter(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ICommandAdapterHelpers(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ICommandToManagedAdapter(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ICommandToWinRTAdapter(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ICommand_WinRT:
    """"""
    def CanExecute(self, parameter: object) -> bool:
        """"""
    def Execute(self, parameter: object) -> None:
        """"""

class ICustomProperty:
    """"""
    @property
    def CanRead(self) -> bool:
        """"""
    @property
    def CanWrite(self) -> bool:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def Type(self) -> Type:
        """"""
    @overload
    def GetValue(self, target: object) -> object:
        """"""
    @overload
    def GetValue(self, target: object, indexValue: object) -> object:
        """"""
    @overload
    def SetValue(self, target: object, value: object) -> None:
        """"""
    @overload
    def SetValue(self, target: object, value: object, indexValue: object) -> None:
        """"""

class ICustomPropertyProvider:
    """"""
    @property
    def Type(self) -> Type:
        """"""
    def GetCustomProperty(self, name: str) -> ICustomProperty:
        """"""
    def GetIndexedProperty(self, name: str, indexParameterType: Type) -> ICustomProperty:
        """"""
    def GetStringRepresentation(self) -> str:
        """"""

class ICustomPropertyProviderImpl(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ICustomPropertyProviderProxy[T1, T2](
    Object,
    IEnumerable,
    IBindableIterable,
    IBindableVector,
    IBindableVectorView,
    ICustomPropertyProvider,
    IGetProxyTarget,
    ICustomQueryInterface,
):
    """"""
    @property
    def Size(self) -> int:
        """"""
    @property
    def Type(self) -> Type:
        """"""
    def Append(self, value: object) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def First(self) -> IBindableIterator:
        """"""
    def GetAt(self, index: int) -> object:
        """"""
    def GetCustomProperty(self, name: str) -> ICustomProperty:
        """"""
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIndexedProperty(self, name: str, indexParameterType: Type) -> ICustomProperty:
        """"""
    def GetInterface(self, iid: Guid, ppv: IntPtr) -> tuple[CustomQueryInterfaceResult, IntPtr]:
        """"""
    def GetStringRepresentation(self) -> str:
        """"""
    def GetTarget(self) -> object:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetView(self) -> IBindableVectorView:
        """"""
    def IndexOf(self, value: object, index: UInt32) -> tuple[bool, UInt32]:
        """"""
    def InsertAt(self, index: int, value: object) -> None:
        """"""
    def RemoveAt(self, index: int) -> None:
        """"""
    def RemoveAtEnd(self) -> None:
        """"""
    def SetAt(self, index: int, value: object) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def __iter__(self) -> Iterator:
        """"""

class IDisposableToIClosableAdapter(Object):
    """"""
    def Close(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class IGetProxyTarget:
    """"""
    def GetTarget(self) -> object:
        """"""

class IIterable[T](IEnumerable[T], IEnumerable):
    """"""
    def First(self) -> IIterator[T]:
        """"""
    def GetEnumerator(self) -> IEnumerator[T]:
        """"""
    def __iter__(self) -> Iterator[T]:
        """"""

class IIterator[T]:
    """"""
    @property
    def Current(self) -> T:
        """"""
    @property
    def HasCurrent(self) -> bool:
        """"""
    def GetMany(self, items: Array[T]) -> tuple[int, Array[T]]:
        """"""
    def MoveNext(self) -> bool:
        """"""

class IKeyValuePair[K, V]:
    """"""
    @property
    def Key(self) -> K:
        """"""
    @property
    def Value(self) -> V:
        """"""

class IManagedActivationFactory:
    """"""
    def RunClassConstructor(self) -> None:
        """"""

class IMapViewToIReadOnlyDictionaryAdapter(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class IMapView[K, V](IEnumerable[IKeyValuePair[K, V]], IEnumerable, IIterable[IKeyValuePair[K, V]]):
    """"""
    @property
    def Size(self) -> int:
        """"""
    def First(self) -> IIterator[IKeyValuePair[K, V]]:
        """"""
    def GetEnumerator(self) -> IEnumerator[IKeyValuePair[K, V]]:
        """"""
    def HasKey[K](self, key: K) -> bool:
        """"""
    def Lookup[K, V](self, key: K) -> V:
        """"""
    def Split(
        self, first: IMapView[K, V], second: IMapView[K, V]
    ) -> tuple[None, IMapView[K, V], IMapView[K, V]]:
        """"""
    def __iter__(self) -> Iterator[IKeyValuePair[K, V]]:
        """"""

class IMap[K, V](IEnumerable[IKeyValuePair[K, V]], IEnumerable, IIterable[IKeyValuePair[K, V]]):
    """"""
    @property
    def Size(self) -> int:
        """"""
    def Clear(self) -> None:
        """"""
    def First(self) -> IIterator[IKeyValuePair[K, V]]:
        """"""
    def GetEnumerator(self) -> IEnumerator[IKeyValuePair[K, V]]:
        """"""
    def GetView(self) -> IReadOnlyDictionary[K, V]:
        """"""
    def HasKey[K](self, key: K) -> bool:
        """"""
    def Insert[K, V](self, key: K, value: V) -> bool:
        """"""
    def Lookup[K, V](self, key: K) -> V:
        """"""
    def Remove[K](self, key: K) -> None:
        """"""
    def __iter__(self) -> Iterator[IKeyValuePair[K, V]]:
        """"""
    def __delitem__[K](self, key: K) -> None:
        """"""

class INotifyCollectionChangedEventArgs:
    """"""
    @property
    def Action(self) -> NotifyCollectionChangedAction:
        """"""
    @property
    def NewItems(self) -> IList:
        """"""
    @property
    def NewStartingIndex(self) -> int:
        """"""
    @property
    def OldItems(self) -> IList:
        """"""
    @property
    def OldStartingIndex(self) -> int:
        """"""

class INotifyCollectionChanged_WinRT:
    """"""

class INotifyPropertyChanged_WinRT:
    """"""

class IPropertyChangedEventArgs:
    """"""
    @property
    def PropertyName(self) -> str:
        """"""

class IPropertyValue:
    """"""
    @property
    def IsNumericScalar(self) -> bool:
        """"""
    @property
    def Type(self) -> PropertyType:
        """"""
    def GetBoolean(self) -> bool:
        """"""
    def GetBooleanArray(self) -> Array[bool]:
        """"""
    def GetChar16(self) -> Char:
        """"""
    def GetChar16Array(self) -> Array[Char]:
        """"""
    def GetDateTime(self) -> DateTimeOffset:
        """"""
    def GetDateTimeArray(self) -> Array[DateTimeOffset]:
        """"""
    def GetDouble(self) -> float:
        """"""
    def GetDoubleArray(self) -> Array[float]:
        """"""
    def GetGuid(self) -> Guid:
        """"""
    def GetGuidArray(self) -> Array[Guid]:
        """"""
    def GetInspectableArray(self) -> Array[object]:
        """"""
    def GetInt16(self) -> int:
        """"""
    def GetInt16Array(self) -> Array[int]:
        """"""
    def GetInt32(self) -> int:
        """"""
    def GetInt32Array(self) -> Array[int]:
        """"""
    def GetInt64(self) -> int:
        """"""
    def GetInt64Array(self) -> Array[int]:
        """"""
    def GetPoint(self) -> Point:
        """"""
    def GetPointArray(self) -> Array[Point]:
        """"""
    def GetRect(self) -> Rect:
        """"""
    def GetRectArray(self) -> Array[Rect]:
        """"""
    def GetSingle(self) -> float:
        """"""
    def GetSingleArray(self) -> Array[float]:
        """"""
    def GetSize(self) -> Size:
        """"""
    def GetSizeArray(self) -> Array[Size]:
        """"""
    def GetString(self) -> str:
        """"""
    def GetStringArray(self) -> Array[str]:
        """"""
    def GetTimeSpan(self) -> TimeSpan:
        """"""
    def GetTimeSpanArray(self) -> Array[TimeSpan]:
        """"""
    def GetUInt16(self) -> int:
        """"""
    def GetUInt16Array(self) -> Array[int]:
        """"""
    def GetUInt32(self) -> int:
        """"""
    def GetUInt32Array(self) -> Array[int]:
        """"""
    def GetUInt64(self) -> int:
        """"""
    def GetUInt64Array(self) -> Array[int]:
        """"""
    def GetUInt8(self) -> int:
        """"""
    def GetUInt8Array(self) -> Array[int]:
        """"""

class IReadOnlyDictionaryToIMapViewAdapter(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class IReadOnlyListToIVectorViewAdapter(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class IReferenceArray[T](IPropertyValue):
    """"""
    @property
    def IsNumericScalar(self) -> bool:
        """"""
    @property
    def Type(self) -> PropertyType:
        """"""
    @property
    def Value(self) -> Array[T]:
        """"""
    def GetBoolean(self) -> bool:
        """"""
    def GetBooleanArray(self) -> Array[bool]:
        """"""
    def GetChar16(self) -> Char:
        """"""
    def GetChar16Array(self) -> Array[Char]:
        """"""
    def GetDateTime(self) -> DateTimeOffset:
        """"""
    def GetDateTimeArray(self) -> Array[DateTimeOffset]:
        """"""
    def GetDouble(self) -> float:
        """"""
    def GetDoubleArray(self) -> Array[float]:
        """"""
    def GetGuid(self) -> Guid:
        """"""
    def GetGuidArray(self) -> Array[Guid]:
        """"""
    def GetInspectableArray(self) -> Array[object]:
        """"""
    def GetInt16(self) -> int:
        """"""
    def GetInt16Array(self) -> Array[int]:
        """"""
    def GetInt32(self) -> int:
        """"""
    def GetInt32Array(self) -> Array[int]:
        """"""
    def GetInt64(self) -> int:
        """"""
    def GetInt64Array(self) -> Array[int]:
        """"""
    def GetPoint(self) -> Point:
        """"""
    def GetPointArray(self) -> Array[Point]:
        """"""
    def GetRect(self) -> Rect:
        """"""
    def GetRectArray(self) -> Array[Rect]:
        """"""
    def GetSingle(self) -> float:
        """"""
    def GetSingleArray(self) -> Array[float]:
        """"""
    def GetSize(self) -> Size:
        """"""
    def GetSizeArray(self) -> Array[Size]:
        """"""
    def GetString(self) -> str:
        """"""
    def GetStringArray(self) -> Array[str]:
        """"""
    def GetTimeSpan(self) -> TimeSpan:
        """"""
    def GetTimeSpanArray(self) -> Array[TimeSpan]:
        """"""
    def GetUInt16(self) -> int:
        """"""
    def GetUInt16Array(self) -> Array[int]:
        """"""
    def GetUInt32(self) -> int:
        """"""
    def GetUInt32Array(self) -> Array[int]:
        """"""
    def GetUInt64(self) -> int:
        """"""
    def GetUInt64Array(self) -> Array[int]:
        """"""
    def GetUInt8(self) -> int:
        """"""
    def GetUInt8Array(self) -> Array[int]:
        """"""

class IReferenceFactory(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class IReference[T](IPropertyValue):
    """"""
    @property
    def IsNumericScalar(self) -> bool:
        """"""
    @property
    def Type(self) -> PropertyType:
        """"""
    @property
    def Value(self) -> T:
        """"""
    def GetBoolean(self) -> bool:
        """"""
    def GetBooleanArray(self) -> Array[bool]:
        """"""
    def GetChar16(self) -> Char:
        """"""
    def GetChar16Array(self) -> Array[Char]:
        """"""
    def GetDateTime(self) -> DateTimeOffset:
        """"""
    def GetDateTimeArray(self) -> Array[DateTimeOffset]:
        """"""
    def GetDouble(self) -> float:
        """"""
    def GetDoubleArray(self) -> Array[float]:
        """"""
    def GetGuid(self) -> Guid:
        """"""
    def GetGuidArray(self) -> Array[Guid]:
        """"""
    def GetInspectableArray(self) -> Array[object]:
        """"""
    def GetInt16(self) -> int:
        """"""
    def GetInt16Array(self) -> Array[int]:
        """"""
    def GetInt32(self) -> int:
        """"""
    def GetInt32Array(self) -> Array[int]:
        """"""
    def GetInt64(self) -> int:
        """"""
    def GetInt64Array(self) -> Array[int]:
        """"""
    def GetPoint(self) -> Point:
        """"""
    def GetPointArray(self) -> Array[Point]:
        """"""
    def GetRect(self) -> Rect:
        """"""
    def GetRectArray(self) -> Array[Rect]:
        """"""
    def GetSingle(self) -> float:
        """"""
    def GetSingleArray(self) -> Array[float]:
        """"""
    def GetSize(self) -> Size:
        """"""
    def GetSizeArray(self) -> Array[Size]:
        """"""
    def GetString(self) -> str:
        """"""
    def GetStringArray(self) -> Array[str]:
        """"""
    def GetTimeSpan(self) -> TimeSpan:
        """"""
    def GetTimeSpanArray(self) -> Array[TimeSpan]:
        """"""
    def GetUInt16(self) -> int:
        """"""
    def GetUInt16Array(self) -> Array[int]:
        """"""
    def GetUInt32(self) -> int:
        """"""
    def GetUInt32Array(self) -> Array[int]:
        """"""
    def GetUInt64(self) -> int:
        """"""
    def GetUInt64Array(self) -> Array[int]:
        """"""
    def GetUInt8(self) -> int:
        """"""
    def GetUInt8Array(self) -> Array[int]:
        """"""

class IRestrictedErrorInfo:
    """"""
    def GetErrorDetails(
        self,
        description: String,
        error: Int32,
        restrictedDescription: String,
        capabilitySid: String,
    ) -> tuple[None, String, Int32, String, String]:
        """"""
    def GetReference(self, reference: String) -> tuple[None, String]:
        """"""

class IStringable:
    """"""
    def ToString(self) -> str:
        """"""

class IStringableHelper(Object):
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

class IVectorViewToIReadOnlyListAdapter(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class IVectorView[T](IEnumerable[T], IEnumerable, IIterable[T]):
    """"""
    @property
    def Size(self) -> int:
        """"""
    def First(self) -> IIterator[T]:
        """"""
    def GetAt[T](self, index: int) -> T:
        """"""
    def GetEnumerator(self) -> IEnumerator[T]:
        """"""
    def GetMany(self, startIndex: int, items: Array[T]) -> tuple[int, Array[T]]:
        """"""
    def IndexOf[T](self, value: T, index: UInt32) -> tuple[bool, UInt32]:
        """"""
    def __iter__(self) -> Iterator[T]:
        """"""

class IVector[T](IEnumerable[T], IEnumerable, IIterable[T]):
    """"""
    @property
    def Size(self) -> int:
        """"""
    def Append[T](self, value: T) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    def First(self) -> IIterator[T]:
        """"""
    def GetAt[T](self, index: int) -> T:
        """"""
    def GetEnumerator(self) -> IEnumerator[T]:
        """"""
    def GetMany(self, startIndex: int, items: Array[T]) -> tuple[int, Array[T]]:
        """"""
    def GetView(self) -> IReadOnlyList[T]:
        """"""
    def IndexOf[T](self, value: T, index: UInt32) -> tuple[bool, UInt32]:
        """"""
    def InsertAt[T](self, index: int, value: T) -> None:
        """"""
    def RemoveAt(self, index: int) -> None:
        """"""
    def RemoveAtEnd(self) -> None:
        """"""
    def ReplaceAll(self, items: Array[T]) -> None:
        """"""
    def SetAt[T](self, index: int, value: T) -> None:
        """"""
    def __iter__(self) -> Iterator[T]:
        """"""

class IVector_Raw[T](IEnumerable[T], IEnumerable, IIterable[T]):
    """"""
    @property
    def Size(self) -> int:
        """"""
    def Append[T](self, value: T) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    def First(self) -> IIterator[T]:
        """"""
    def GetAt[T](self, index: int) -> T:
        """"""
    def GetEnumerator(self) -> IEnumerator[T]:
        """"""
    def GetMany(self, startIndex: int, items: Array[T]) -> tuple[int, Array[T]]:
        """"""
    def GetView(self) -> IVectorView[T]:
        """"""
    def IndexOf[T](self, value: T, index: UInt32) -> tuple[bool, UInt32]:
        """"""
    def InsertAt[T](self, index: int, value: T) -> None:
        """"""
    def RemoveAt(self, index: int) -> None:
        """"""
    def RemoveAtEnd(self) -> None:
        """"""
    def ReplaceAll(self, items: Array[T]) -> None:
        """"""
    def SetAt[T](self, index: int, value: T) -> None:
        """"""
    def __iter__(self) -> Iterator[T]:
        """"""

class IWinRTClassActivator:
    """"""
    def ActivateInstance(self, activatableClassId: str) -> object:
        """"""
    def GetActivationFactory(self, activatableClassId: str, iid: Guid) -> IntPtr:
        """"""

Indexer_Get_Delegate: Callable[[int], T] = ...
""""""

class InterfaceForwardingSupport(Enum):
    """"""

    _None: InterfaceForwardingSupport = ...
    """"""
    IBindableVector: InterfaceForwardingSupport = ...
    """"""
    IVector: InterfaceForwardingSupport = ...
    """"""
    IBindableVectorView: InterfaceForwardingSupport = ...
    """"""
    IVectorView: InterfaceForwardingSupport = ...
    """"""
    IBindableIterableOrIIterable: InterfaceForwardingSupport = ...
    """"""

class InterfaceImplementedInVersionAttribute(Attribute, _Attribute):
    """"""
    def __init__(
        self,
        interfaceType: Type,
        majorVersion: int,
        minorVersion: int,
        buildVersion: int,
        revisionVersion: int,
    ) -> None:
        """"""
    @property
    def BuildVersion(self) -> int:
        """"""
    @property
    def InterfaceType(self) -> Type:
        """"""
    @property
    def MajorVersion(self) -> int:
        """"""
    @property
    def MinorVersion(self) -> int:
        """"""
    @property
    def RevisionVersion(self) -> int:
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

class IterableToEnumerableAdapter(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class IteratorToEnumeratorAdapter[T](Object, IEnumerator[T], IEnumerator, IDisposable):
    """"""
    @property
    def Current(self) -> T:
        """"""
    def Dispose(self) -> None:
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

class ListToBindableVectorAdapter(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ListToBindableVectorViewAdapter(Object, IBindableIterable, IBindableVectorView):
    """"""
    @property
    def Size(self) -> int:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def First(self) -> IBindableIterator:
        """"""
    def GetAt(self, index: int) -> object:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def IndexOf(self, value: object, index: UInt32) -> tuple[bool, UInt32]:
        """"""
    def ToString(self) -> str:
        """"""

class ListToVectorAdapter(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ManagedActivationFactory(Object, IActivationFactory, IManagedActivationFactory):
    """"""
    def ActivateInstance(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def RunClassConstructor(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class MapToCollectionAdapter(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class MapToDictionaryAdapter(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class MapViewToReadOnlyCollectionAdapter(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class NamespaceResolveEventArgs(EventArgs):
    """"""
    def __init__(self, namespaceName: str, requestingAssembly: Assembly) -> None:
        """"""
    @property
    def NamespaceName(self) -> str:
        """"""
    @property
    def RequestingAssembly(self) -> Assembly:
        """"""
    @property
    def ResolvedAssemblies(self) -> Collection[Assembly]:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class NotifyCollectionChangedEventArgsMarshaler(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

NotifyCollectionChangedEventHandler_WinRT: Callable[
    [object, NotifyCollectionChangedEventArgs], None
] = ...
""""""

class NotifyCollectionChangedToManagedAdapter(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class NotifyCollectionChangedToWinRTAdapter(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class NotifyPropertyChangedToManagedAdapter(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class NotifyPropertyChangedToWinRTAdapter(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class Point(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class PropertyChangedEventArgsMarshaler(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

PropertyChangedEventHandler_WinRT: Callable[[object, PropertyChangedEventArgs], None] = ...
""""""

class PropertyType(Enum):
    """"""

    Empty: PropertyType = ...
    """"""
    UInt8: PropertyType = ...
    """"""
    Int16: PropertyType = ...
    """"""
    UInt16: PropertyType = ...
    """"""
    Int32: PropertyType = ...
    """"""
    UInt32: PropertyType = ...
    """"""
    Int64: PropertyType = ...
    """"""
    UInt64: PropertyType = ...
    """"""
    Single: PropertyType = ...
    """"""
    Double: PropertyType = ...
    """"""
    Char16: PropertyType = ...
    """"""
    Boolean: PropertyType = ...
    """"""
    String: PropertyType = ...
    """"""
    Inspectable: PropertyType = ...
    """"""
    DateTime: PropertyType = ...
    """"""
    TimeSpan: PropertyType = ...
    """"""
    Guid: PropertyType = ...
    """"""
    Point: PropertyType = ...
    """"""
    Size: PropertyType = ...
    """"""
    Rect: PropertyType = ...
    """"""
    Other: PropertyType = ...
    """"""
    UInt8Array: PropertyType = ...
    """"""
    Int16Array: PropertyType = ...
    """"""
    UInt16Array: PropertyType = ...
    """"""
    Int32Array: PropertyType = ...
    """"""
    UInt32Array: PropertyType = ...
    """"""
    Int64Array: PropertyType = ...
    """"""
    UInt64Array: PropertyType = ...
    """"""
    SingleArray: PropertyType = ...
    """"""
    DoubleArray: PropertyType = ...
    """"""
    Char16Array: PropertyType = ...
    """"""
    BooleanArray: PropertyType = ...
    """"""
    StringArray: PropertyType = ...
    """"""
    InspectableArray: PropertyType = ...
    """"""
    DateTimeArray: PropertyType = ...
    """"""
    TimeSpanArray: PropertyType = ...
    """"""
    GuidArray: PropertyType = ...
    """"""
    PointArray: PropertyType = ...
    """"""
    SizeArray: PropertyType = ...
    """"""
    RectArray: PropertyType = ...
    """"""
    OtherArray: PropertyType = ...
    """"""

class ReadOnlyArrayAttribute(Attribute, _Attribute):
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

class ReadOnlyDictionaryKeyCollection[TKey, TValue](Object, IEnumerable[TKey], IEnumerable):
    """"""
    def __init__(self, dictionary: IReadOnlyDictionary[TKey, TValue]) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator[TKey]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def __iter__(self) -> Iterator[TKey]:
        """"""

class ReadOnlyDictionaryKeyEnumerator[TKey, TValue](
    Object, IEnumerator[TKey], IEnumerator, IDisposable
):
    """"""
    def __init__(self, dictionary: IReadOnlyDictionary[TKey, TValue]) -> None:
        """"""
    @property
    def Current(self) -> TKey:
        """"""
    def Dispose(self) -> None:
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

class ReadOnlyDictionaryValueCollection[TKey, TValue](Object, IEnumerable[TValue], IEnumerable):
    """"""
    def __init__(self, dictionary: IReadOnlyDictionary[TKey, TValue]) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator[TValue]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def __iter__(self) -> Iterator[TValue]:
        """"""

class ReadOnlyDictionaryValueEnumerator[TKey, TValue](
    Object, IEnumerator[TValue], IEnumerator, IDisposable
):
    """"""
    def __init__(self, dictionary: IReadOnlyDictionary[TKey, TValue]) -> None:
        """"""
    @property
    def Current(self) -> TValue:
        """"""
    def Dispose(self) -> None:
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

class Rect(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ReturnValueNameAttribute(Attribute, _Attribute):
    """"""
    def __init__(self, name: str) -> None:
        """"""
    @property
    def Name(self) -> str:
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

class RuntimeClass(ABC, __ComObject):
    """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetLifetimeService(self) -> object:
        """"""
    def GetType(self) -> Type:
        """"""
    def InitializeLifetimeService(self) -> object:
        """"""
    def ToString(self) -> str:
        """"""

class Size(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class UnsafeNativeMethods(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class VectorToCollectionAdapter(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class VectorToListAdapter(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class VectorViewToReadOnlyCollectionAdapter(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class WinRTClassActivator(MarshalByRefObject, IWinRTClassActivator):
    """"""
    def __init__(self) -> None:
        """"""
    def ActivateInstance(self, activatableClassId: str) -> object:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetActivationFactory(self, activatableClassId: str, iid: Guid) -> IntPtr:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetLifetimeService(self) -> object:
        """"""
    def GetType(self) -> Type:
        """"""
    def InitializeLifetimeService(self) -> object:
        """"""
    def ToString(self) -> str:
        """"""

WindowsFoundationEventHandler: Callable[[object, T], None] = ...
""""""

class WindowsRuntimeBufferHelper(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class WindowsRuntimeImportAttribute(Attribute, _Attribute):
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

class WindowsRuntimeMarshal(ABC, Object):
    """"""
    @classmethod
    def AddEventHandler[T](
        cls,
        addMethod: Func[T, EventRegistrationToken],
        removeMethod: Action[EventRegistrationToken],
        handler: T,
    ) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def FreeHString(cls, ptr: IntPtr) -> None:
        """"""
    @classmethod
    def GetActivationFactory(cls, type: Type) -> IActivationFactory:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def PtrToStringHString(cls, ptr: IntPtr) -> str:
        """"""
    @classmethod
    def RemoveAllEventHandlers(cls, removeMethod: Action[EventRegistrationToken]) -> None:
        """"""
    @classmethod
    def RemoveEventHandler[T](
        cls, removeMethod: Action[EventRegistrationToken], handler: T
    ) -> None:
        """"""
    @classmethod
    def StringToHString(cls, s: str) -> IntPtr:
        """"""
    def ToString(self) -> str:
        """"""

class WindowsRuntimeMetadata(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    @overload
    def ResolveNamespace(
        cls, namespaceName: str, packageGraphFilePaths: IEnumerable[str]
    ) -> IEnumerable[str]:
        """"""
    @classmethod
    @overload
    def ResolveNamespace(
        cls, namespaceName: str, windowsSdkFilePath: str, packageGraphFilePaths: IEnumerable[str]
    ) -> IEnumerable[str]:
        """"""
    def ToString(self) -> str:
        """"""
    DesignerNamespaceResolve: EventType[EventHandler[DesignerNamespaceResolveEventArgs]] = ...
    """"""
    ReflectionOnlyNamespaceResolve: EventType[EventHandler[NamespaceResolveEventArgs]] = ...
    """"""

class WriteOnlyArrayAttribute(Attribute, _Attribute):
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
