from __future__ import annotations

from abc import ABC
from typing import Callable
from typing import Generic
from typing import Iterator
from typing import Tuple
from typing import TypeVar
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
from System import IntPtr
from System import MarshalByRefObject
from System import Object
from System import TimeSpan
from System import Type
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

K = TypeVar("K")
T = TypeVar("T")
T1 = TypeVar("T1")
T2 = TypeVar("T2")
TKey = TypeVar("TKey")
TValue = TypeVar("TValue")
V = TypeVar("V")

class EventType(Generic[T]):
    def __iadd__(self, other: T): ...
    def __isub__(self, other: T): ...

class BindableIterableToEnumerableAdapter(Object):
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

class BindableVectorToCollectionAdapter(Object):
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

class BindableVectorToListAdapter(Object):
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

class CLRIKeyValuePairImpl(Generic[K, V], Object, IKeyValuePair[K, V]):
    """"""

    def __init__(self, pair: KeyValuePair[K, V]):
        """

        :param pair:
        """
    @property
    def Key(self) -> K:
        """

        :return:
        """
    @property
    def Value(self) -> V:
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

class CLRIPropertyValueImpl(Object, IPropertyValue):
    """"""

    @property
    def IsNumericScalar(self) -> bool:
        """

        :return:
        """
    @property
    def Type(self) -> PropertyType:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetBoolean(self) -> bool:
        """

        :return:
        """
    def GetBooleanArray(self) -> Array[bool]:
        """

        :return:
        """
    def GetChar16(self) -> Char:
        """

        :return:
        """
    def GetChar16Array(self) -> Array[Char]:
        """

        :return:
        """
    def GetDateTime(self) -> DateTimeOffset:
        """

        :return:
        """
    def GetDateTimeArray(self) -> Array[DateTimeOffset]:
        """

        :return:
        """
    def GetDouble(self) -> float:
        """

        :return:
        """
    def GetDoubleArray(self) -> Array[float]:
        """

        :return:
        """
    def GetGuid(self) -> Guid:
        """

        :return:
        """
    def GetGuidArray(self) -> Array[Guid]:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetInspectable(self) -> object:
        """

        :return:
        """
    def GetInspectableArray(self) -> Array[object]:
        """

        :return:
        """
    def GetInt16(self) -> int:
        """

        :return:
        """
    def GetInt16Array(self) -> Array[int]:
        """

        :return:
        """
    def GetInt32(self) -> int:
        """

        :return:
        """
    def GetInt32Array(self) -> Array[int]:
        """

        :return:
        """
    def GetInt64(self) -> int:
        """

        :return:
        """
    def GetInt64Array(self) -> Array[int]:
        """

        :return:
        """
    def GetPoint(self) -> Point:
        """

        :return:
        """
    def GetPointArray(self) -> Array[Point]:
        """

        :return:
        """
    def GetRect(self) -> Rect:
        """

        :return:
        """
    def GetRectArray(self) -> Array[Rect]:
        """

        :return:
        """
    def GetSingle(self) -> float:
        """

        :return:
        """
    def GetSingleArray(self) -> Array[float]:
        """

        :return:
        """
    def GetSize(self) -> Size:
        """

        :return:
        """
    def GetSizeArray(self) -> Array[Size]:
        """

        :return:
        """
    def GetString(self) -> str:
        """

        :return:
        """
    def GetStringArray(self) -> Array[str]:
        """

        :return:
        """
    def GetTimeSpan(self) -> TimeSpan:
        """

        :return:
        """
    def GetTimeSpanArray(self) -> Array[TimeSpan]:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetUInt16(self) -> int:
        """

        :return:
        """
    def GetUInt16Array(self) -> Array[int]:
        """

        :return:
        """
    def GetUInt32(self) -> int:
        """

        :return:
        """
    def GetUInt32Array(self) -> Array[int]:
        """

        :return:
        """
    def GetUInt64(self) -> int:
        """

        :return:
        """
    def GetUInt64Array(self) -> Array[int]:
        """

        :return:
        """
    def GetUInt8(self) -> int:
        """

        :return:
        """
    def GetUInt8Array(self) -> Array[int]:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CLRIReferenceArrayImpl(
    Generic[T],
    CLRIPropertyValueImpl,
    ICollection,
    IEnumerable,
    IList,
    ICustomPropertyProvider,
    IPropertyValue,
    IReferenceArray[T],
):
    """"""

    def __init__(self, type: PropertyType, obj: Array[T]):
        """

        :param type:
        :param obj:
        """
    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def IsFixedSize(self) -> bool:
        """

        :return:
        """
    @property
    def IsNumericScalar(self) -> bool:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def IsSynchronized(self) -> bool:
        """

        :return:
        """
    @property
    def Item(self) -> object:
        """

        :return:
        """
    @Item.setter
    def Item(self, value: object) -> None: ...
    @property
    def SyncRoot(self) -> object:
        """

        :return:
        """
    @property
    def Type(self) -> PropertyType:
        """

        :return:
        """
    @property
    def Type(self) -> Type:
        """

        :return:
        """
    @property
    def Value(self) -> Array[T]:
        """

        :return:
        """
    def Add(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    def Clear(self) -> None:
        """"""
    def Contains(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetBoolean(self) -> bool:
        """

        :return:
        """
    def GetBooleanArray(self) -> Array[bool]:
        """

        :return:
        """
    def GetChar16(self) -> Char:
        """

        :return:
        """
    def GetChar16Array(self) -> Array[Char]:
        """

        :return:
        """
    def GetCustomProperty(self, name: str) -> ICustomProperty:
        """

        :param name:
        :return:
        """
    def GetDateTime(self) -> DateTimeOffset:
        """

        :return:
        """
    def GetDateTimeArray(self) -> Array[DateTimeOffset]:
        """

        :return:
        """
    def GetDouble(self) -> float:
        """

        :return:
        """
    def GetDoubleArray(self) -> Array[float]:
        """

        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    def GetGuid(self) -> Guid:
        """

        :return:
        """
    def GetGuidArray(self) -> Array[Guid]:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetIndexedProperty(self, name: str, indexParameterType: Type) -> ICustomProperty:
        """

        :param name:
        :param indexParameterType:
        :return:
        """
    def GetInspectable(self) -> object:
        """

        :return:
        """
    def GetInspectableArray(self) -> Array[object]:
        """

        :return:
        """
    def GetInt16(self) -> int:
        """

        :return:
        """
    def GetInt16Array(self) -> Array[int]:
        """

        :return:
        """
    def GetInt32(self) -> int:
        """

        :return:
        """
    def GetInt32Array(self) -> Array[int]:
        """

        :return:
        """
    def GetInt64(self) -> int:
        """

        :return:
        """
    def GetInt64Array(self) -> Array[int]:
        """

        :return:
        """
    def GetPoint(self) -> Point:
        """

        :return:
        """
    def GetPointArray(self) -> Array[Point]:
        """

        :return:
        """
    def GetRect(self) -> Rect:
        """

        :return:
        """
    def GetRectArray(self) -> Array[Rect]:
        """

        :return:
        """
    def GetSingle(self) -> float:
        """

        :return:
        """
    def GetSingleArray(self) -> Array[float]:
        """

        :return:
        """
    def GetSize(self) -> Size:
        """

        :return:
        """
    def GetSizeArray(self) -> Array[Size]:
        """

        :return:
        """
    def GetString(self) -> str:
        """

        :return:
        """
    def GetStringArray(self) -> Array[str]:
        """

        :return:
        """
    def GetStringRepresentation(self) -> str:
        """

        :return:
        """
    def GetTimeSpan(self) -> TimeSpan:
        """

        :return:
        """
    def GetTimeSpanArray(self) -> Array[TimeSpan]:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetUInt16(self) -> int:
        """

        :return:
        """
    def GetUInt16Array(self) -> Array[int]:
        """

        :return:
        """
    def GetUInt32(self) -> int:
        """

        :return:
        """
    def GetUInt32Array(self) -> Array[int]:
        """

        :return:
        """
    def GetUInt64(self) -> int:
        """

        :return:
        """
    def GetUInt64Array(self) -> Array[int]:
        """

        :return:
        """
    def GetUInt8(self) -> int:
        """

        :return:
        """
    def GetUInt8Array(self) -> Array[int]:
        """

        :return:
        """
    def IndexOf(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    def Insert(self, index: int, value: object) -> None:
        """

        :param index:
        :param value:
        """
    def Remove(self, value: object) -> None:
        """

        :param value:
        """
    def RemoveAt(self, index: int) -> None:
        """

        :param index:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def __contains__(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    def __getitem__(self, index: int) -> object:
        """

        :param index:
        :return:
        """
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    def __len__(self) -> int:
        """

        :return:
        """
    def __setitem__(self, index: int, value: object) -> None:
        """

        :param index:
        :param value:
        """

class CLRIReferenceImpl(
    Generic[T], CLRIPropertyValueImpl, ICustomPropertyProvider, IPropertyValue, IReference[T]
):
    """"""

    def __init__(self, type: PropertyType, obj: T):
        """

        :param type:
        :param obj:
        """
    @property
    def IsNumericScalar(self) -> bool:
        """

        :return:
        """
    @property
    def Type(self) -> Type:
        """

        :return:
        """
    @property
    def Type(self) -> PropertyType:
        """

        :return:
        """
    @property
    def Value(self) -> T:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetBoolean(self) -> bool:
        """

        :return:
        """
    def GetBooleanArray(self) -> Array[bool]:
        """

        :return:
        """
    def GetChar16(self) -> Char:
        """

        :return:
        """
    def GetChar16Array(self) -> Array[Char]:
        """

        :return:
        """
    def GetCustomProperty(self, name: str) -> ICustomProperty:
        """

        :param name:
        :return:
        """
    def GetDateTime(self) -> DateTimeOffset:
        """

        :return:
        """
    def GetDateTimeArray(self) -> Array[DateTimeOffset]:
        """

        :return:
        """
    def GetDouble(self) -> float:
        """

        :return:
        """
    def GetDoubleArray(self) -> Array[float]:
        """

        :return:
        """
    def GetGuid(self) -> Guid:
        """

        :return:
        """
    def GetGuidArray(self) -> Array[Guid]:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetIndexedProperty(self, name: str, indexParameterType: Type) -> ICustomProperty:
        """

        :param name:
        :param indexParameterType:
        :return:
        """
    def GetInspectable(self) -> object:
        """

        :return:
        """
    def GetInspectableArray(self) -> Array[object]:
        """

        :return:
        """
    def GetInt16(self) -> int:
        """

        :return:
        """
    def GetInt16Array(self) -> Array[int]:
        """

        :return:
        """
    def GetInt32(self) -> int:
        """

        :return:
        """
    def GetInt32Array(self) -> Array[int]:
        """

        :return:
        """
    def GetInt64(self) -> int:
        """

        :return:
        """
    def GetInt64Array(self) -> Array[int]:
        """

        :return:
        """
    def GetPoint(self) -> Point:
        """

        :return:
        """
    def GetPointArray(self) -> Array[Point]:
        """

        :return:
        """
    def GetRect(self) -> Rect:
        """

        :return:
        """
    def GetRectArray(self) -> Array[Rect]:
        """

        :return:
        """
    def GetSingle(self) -> float:
        """

        :return:
        """
    def GetSingleArray(self) -> Array[float]:
        """

        :return:
        """
    def GetSize(self) -> Size:
        """

        :return:
        """
    def GetSizeArray(self) -> Array[Size]:
        """

        :return:
        """
    def GetString(self) -> str:
        """

        :return:
        """
    def GetStringArray(self) -> Array[str]:
        """

        :return:
        """
    def GetStringRepresentation(self) -> str:
        """

        :return:
        """
    def GetTimeSpan(self) -> TimeSpan:
        """

        :return:
        """
    def GetTimeSpanArray(self) -> Array[TimeSpan]:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetUInt16(self) -> int:
        """

        :return:
        """
    def GetUInt16Array(self) -> Array[int]:
        """

        :return:
        """
    def GetUInt32(self) -> int:
        """

        :return:
        """
    def GetUInt32Array(self) -> Array[int]:
        """

        :return:
        """
    def GetUInt64(self) -> int:
        """

        :return:
        """
    def GetUInt64Array(self) -> Array[int]:
        """

        :return:
        """
    def GetUInt8(self) -> int:
        """

        :return:
        """
    def GetUInt8Array(self) -> Array[int]:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class ConstantSplittableMap(
    Generic[TKey, TValue],
    Object,
    IEnumerable[IKeyValuePair, TValue],
    IEnumerable,
    IIterable[IKeyValuePair, TValue],
    IMapView[TKey, TValue],
):
    """"""

    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def Item(self) -> TValue:
        """

        :return:
        """
    @property
    def Keys(self) -> IEnumerable[TKey]:
        """

        :return:
        """
    @property
    def Size(self) -> int:
        """

        :return:
        """
    @property
    def Values(self) -> IEnumerable[TValue]:
        """

        :return:
        """
    def ContainsKey(self, key: TKey) -> bool:
        """

        :param key:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def First(self) -> IIterator[IKeyValuePair, TValue]:
        """

        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

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
    def HasKey(self, key: TKey) -> bool:
        """

        :param key:
        :return:
        """
    def Lookup(self, key: TKey) -> TValue:
        """

        :param key:
        :return:
        """
    def Split(
        self, first: IMapView[TKey, TValue], second: IMapView[TKey, TValue]
    ) -> Tuple[None, IMapView[TKey, TValue], IMapView[TKey, TValue]]:
        """

        :param first:
        :param second:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def TryGetValue(self, key: TKey, value: TValue) -> Tuple[bool, TValue]:
        """

        :param key:
        :param value:
        :return:
        """
    def __getitem__(self, key: TKey) -> TValue:
        """

        :param key:
        :return:
        """
    @overload
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[IKeyValuePair, TValue]:
        """

        :return:
        """

class CustomPropertyImpl(Object, ICustomProperty):
    """"""

    def __init__(self, propertyInfo: PropertyInfo):
        """

        :param propertyInfo:
        """
    @property
    def CanRead(self) -> bool:
        """

        :return:
        """
    @property
    def CanWrite(self) -> bool:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Type(self) -> Type:
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
    @overload
    def GetValue(self, target: object) -> object:
        """

        :param target:
        :return:
        """
    @overload
    def GetValue(self, target: object, indexValue: object) -> object:
        """

        :param target:
        :param indexValue:
        :return:
        """
    @overload
    def SetValue(self, target: object, value: object) -> None:
        """

        :param target:
        :param value:
        """
    @overload
    def SetValue(self, target: object, value: object, indexValue: object) -> None:
        """

        :param target:
        :param value:
        :param indexValue:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class DefaultInterfaceAttribute(Attribute, _Attribute):
    """"""

    def __init__(self, defaultInterface: Type):
        """

        :param defaultInterface:
        """
    @property
    def DefaultInterface(self) -> Type:
        """

        :return:
        """
    @property
    def TypeId(self) -> object:
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
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """

        :return:
        """
    def Match(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class DesignerNamespaceResolveEventArgs(EventArgs):
    """"""

    def __init__(self, namespaceName: str):
        """

        :param namespaceName:
        """
    @property
    def NamespaceName(self) -> str:
        """

        :return:
        """
    @property
    def ResolvedAssemblyFiles(self) -> Collection[str]:
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

class DictionaryKeyCollection(
    Generic[TKey, TValue], Object, ICollection[TKey], IEnumerable[TKey], IEnumerable
):
    """"""

    def __init__(self, dictionary: IDictionary[TKey, TValue]):
        """

        :param dictionary:
        """
    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    def Add(self, item: TKey) -> None:
        """

        :param item:
        """
    def Clear(self) -> None:
        """"""
    def Contains(self, item: TKey) -> bool:
        """

        :param item:
        :return:
        """
    def CopyTo(self, array: Array[TKey], arrayIndex: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

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
    def Remove(self, item: TKey) -> bool:
        """

        :param item:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def __contains__(self, value: TKey) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[TKey]:
        """

        :return:
        """
    def __len__(self) -> int:
        """

        :return:
        """

class DictionaryKeyEnumerator(
    Generic[TKey, TValue], Object, IEnumerator[TKey], IEnumerator, IDisposable
):
    """"""

    def __init__(self, dictionary: IDictionary[TKey, TValue]):
        """

        :param dictionary:
        """
    @property
    def Current(self) -> object:
        """

        :return:
        """
    def Dispose(self) -> None:
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
    def MoveNext(self) -> bool:
        """

        :return:
        """
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class DictionaryToMapAdapter(Object):
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

class DictionaryValueCollection(
    Generic[TKey, TValue], Object, ICollection[TValue], IEnumerable[TValue], IEnumerable
):
    """"""

    def __init__(self, dictionary: IDictionary[TKey, TValue]):
        """

        :param dictionary:
        """
    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    def Add(self, item: TValue) -> None:
        """

        :param item:
        """
    def Clear(self) -> None:
        """"""
    def Contains(self, item: TValue) -> bool:
        """

        :param item:
        :return:
        """
    def CopyTo(self, array: Array[TValue], arrayIndex: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

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
    def Remove(self, item: TValue) -> bool:
        """

        :param item:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def __contains__(self, value: TValue) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[TValue]:
        """

        :return:
        """
    def __len__(self) -> int:
        """

        :return:
        """

class DictionaryValueEnumerator(
    Generic[TKey, TValue], Object, IEnumerator[TValue], IEnumerator, IDisposable
):
    """"""

    def __init__(self, dictionary: IDictionary[TKey, TValue]):
        """

        :param dictionary:
        """
    @property
    def Current(self) -> object:
        """

        :return:
        """
    def Dispose(self) -> None:
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
    def MoveNext(self) -> bool:
        """

        :return:
        """
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class EnumerableToBindableIterableAdapter(Object):
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

class EnumerableToIterableAdapter(Object):
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

class EnumeratorToIteratorAdapter(Generic[T], Object, IBindableIterator, IIterator[T]):
    """"""

    @property
    def Current(self) -> T:
        """

        :return:
        """
    @property
    def Current(self) -> object:
        """

        :return:
        """
    @property
    def HasCurrent(self) -> bool:
        """

        :return:
        """
    @property
    def HasCurrent(self) -> bool:
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
    def GetMany(self, items: Array[T]) -> Tuple[int, Array[T]]:
        """

        :param items:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def MoveNext(self) -> bool:
        """

        :return:
        """
    @overload
    def MoveNext(self) -> bool:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class EventRegistrationToken(ValueType):
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
    def __eq__(self, other: EventRegistrationToken) -> bool:
        """

        :param other:
        :return:
        """
    def __ne__(self, other: EventRegistrationToken) -> bool:
        """

        :param other:
        :return:
        """
    @classmethod
    def op_Equality(cls, left: EventRegistrationToken, right: EventRegistrationToken) -> bool:
        """

        :param left:
        :param right:
        :return:
        """
    @classmethod
    def op_Inequality(cls, left: EventRegistrationToken, right: EventRegistrationToken) -> bool:
        """

        :param left:
        :param right:
        :return:
        """

class EventRegistrationTokenTable(Generic[T], Object):
    """"""

    def __init__(self):
        """"""
    @property
    def InvocationList(self) -> T:
        """

        :return:
        """
    @InvocationList.setter
    def InvocationList(self, value: T) -> None: ...
    def AddEventHandler(self, handler: T) -> EventRegistrationToken:
        """

        :param handler:
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
    @classmethod
    def GetOrCreateEventRegistrationTokenTable(
        cls, refEventTable: EventRegistrationTokenTable[T]
    ) -> EventRegistrationTokenTable[T]:
        """

        :param refEventTable:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def RemoveEventHandler(self, handler: T) -> None:
        """

        :param handler:
        """
    @overload
    def RemoveEventHandler(self, token: EventRegistrationToken) -> None:
        """

        :param token:
        """
    def ToString(self) -> str:
        """

        :return:
        """

GetEnumerator_Delegate: Callable[[], IEnumerator[T]] = ...
"""

:return: 
"""

class HSTRING_HEADER(ValueType):
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

class IActivationFactory:
    """"""

    def ActivateInstance(self) -> object:
        """

        :return:
        """

class IBindableIterable:
    """"""

    def First(self) -> IBindableIterator:
        """

        :return:
        """

class IBindableIterator:
    """"""

    @property
    def Current(self) -> object:
        """

        :return:
        """
    @property
    def HasCurrent(self) -> bool:
        """

        :return:
        """
    def MoveNext(self) -> bool:
        """

        :return:
        """

class IBindableVector(IBindableIterable):
    """"""

    @property
    def Size(self) -> int:
        """

        :return:
        """
    def Append(self, value: object) -> None:
        """

        :param value:
        """
    def Clear(self) -> None:
        """"""
    def First(self) -> IBindableIterator:
        """

        :return:
        """
    def GetAt(self, index: int) -> object:
        """

        :param index:
        :return:
        """
    def GetView(self) -> IBindableVectorView:
        """

        :return:
        """
    def IndexOf(self, value: object, index: int) -> Tuple[bool, int]:
        """

        :param value:
        :param index:
        :return:
        """
    def InsertAt(self, index: int, value: object) -> None:
        """

        :param index:
        :param value:
        """
    def RemoveAt(self, index: int) -> None:
        """

        :param index:
        """
    def RemoveAtEnd(self) -> None:
        """"""
    def SetAt(self, index: int, value: object) -> None:
        """

        :param index:
        :param value:
        """

class IBindableVectorView(IBindableIterable):
    """"""

    @property
    def Size(self) -> int:
        """

        :return:
        """
    def First(self) -> IBindableIterator:
        """

        :return:
        """
    def GetAt(self, index: int) -> object:
        """

        :param index:
        :return:
        """
    def IndexOf(self, value: object, index: int) -> Tuple[bool, int]:
        """

        :param value:
        :param index:
        :return:
        """

class IClosable:
    """"""

    def Close(self) -> None:
        """"""

class IClosableToIDisposableAdapter(Object):
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

class ICommandAdapterHelpers(ABC, Object):
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

class ICommandToManagedAdapter(Object):
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

class ICommandToWinRTAdapter(Object):
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

class ICommand_WinRT:
    """"""

    def CanExecute(self, parameter: object) -> bool:
        """

        :param parameter:
        :return:
        """
    def Execute(self, parameter: object) -> None:
        """

        :param parameter:
        """

class ICustomProperty:
    """"""

    @property
    def CanRead(self) -> bool:
        """

        :return:
        """
    @property
    def CanWrite(self) -> bool:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Type(self) -> Type:
        """

        :return:
        """
    @overload
    def GetValue(self, target: object) -> object:
        """

        :param target:
        :return:
        """
    @overload
    def GetValue(self, target: object, indexValue: object) -> object:
        """

        :param target:
        :param indexValue:
        :return:
        """
    @overload
    def SetValue(self, target: object, value: object) -> None:
        """

        :param target:
        :param value:
        """
    @overload
    def SetValue(self, target: object, value: object, indexValue: object) -> None:
        """

        :param target:
        :param value:
        :param indexValue:
        """

class ICustomPropertyProvider:
    """"""

    @property
    def Type(self) -> Type:
        """

        :return:
        """
    def GetCustomProperty(self, name: str) -> ICustomProperty:
        """

        :param name:
        :return:
        """
    def GetIndexedProperty(self, name: str, indexParameterType: Type) -> ICustomProperty:
        """

        :param name:
        :param indexParameterType:
        :return:
        """
    def GetStringRepresentation(self) -> str:
        """

        :return:
        """

class ICustomPropertyProviderImpl(ABC, Object):
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

class ICustomPropertyProviderProxy(
    Generic[T1, T2],
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
        """

        :return:
        """
    @property
    def Size(self) -> int:
        """

        :return:
        """
    @property
    def Type(self) -> Type:
        """

        :return:
        """
    def Append(self, value: object) -> None:
        """

        :param value:
        """
    def Clear(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def First(self) -> IBindableIterator:
        """

        :return:
        """
    @overload
    def GetAt(self, index: int) -> object:
        """

        :param index:
        :return:
        """
    @overload
    def GetAt(self, index: int) -> object:
        """

        :param index:
        :return:
        """
    def GetCustomProperty(self, name: str) -> ICustomProperty:
        """

        :param name:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetIndexedProperty(self, name: str, indexParameterType: Type) -> ICustomProperty:
        """

        :param name:
        :param indexParameterType:
        :return:
        """
    def GetInterface(self, iid: Guid, ppv: IntPtr) -> Tuple[CustomQueryInterfaceResult, IntPtr]:
        """

        :param iid:
        :param ppv:
        :return:
        """
    def GetStringRepresentation(self) -> str:
        """

        :return:
        """
    def GetTarget(self) -> object:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetView(self) -> IBindableVectorView:
        """

        :return:
        """
    @overload
    def IndexOf(self, value: object, index: int) -> Tuple[bool, int]:
        """

        :param value:
        :param index:
        :return:
        """
    @overload
    def IndexOf(self, value: object, index: int) -> Tuple[bool, int]:
        """

        :param value:
        :param index:
        :return:
        """
    def InsertAt(self, index: int, value: object) -> None:
        """

        :param index:
        :param value:
        """
    def RemoveAt(self, index: int) -> None:
        """

        :param index:
        """
    def RemoveAtEnd(self) -> None:
        """"""
    def SetAt(self, index: int, value: object) -> None:
        """

        :param index:
        :param value:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """

class IDisposableToIClosableAdapter(Object):
    """"""

    def Close(self) -> None:
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

class IGetProxyTarget:
    """"""

    def GetTarget(self) -> object:
        """

        :return:
        """

class IIterable(Generic[T], IEnumerable[T], IEnumerable):
    """"""

    def First(self) -> IIterator[T]:
        """

        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[T]:
        """

        :return:
        """

class IIterator(Generic[T]):
    """"""

    @property
    def Current(self) -> T:
        """

        :return:
        """
    @property
    def HasCurrent(self) -> bool:
        """

        :return:
        """
    def GetMany(self, items: Array[T]) -> Tuple[int, Array[T]]:
        """

        :param items:
        :return:
        """
    def MoveNext(self) -> bool:
        """

        :return:
        """

class IKeyValuePair(Generic[K, V]):
    """"""

    @property
    def Key(self) -> K:
        """

        :return:
        """
    @property
    def Value(self) -> V:
        """

        :return:
        """

class IManagedActivationFactory:
    """"""

    def RunClassConstructor(self) -> None:
        """"""

class IMapViewToIReadOnlyDictionaryAdapter(Object):
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

class IMapView(
    Generic[K, V], IEnumerable[IKeyValuePair, V], IEnumerable, IIterable[IKeyValuePair, V]
):
    """"""

    @property
    def Size(self) -> int:
        """

        :return:
        """
    def First(self) -> IIterator[IKeyValuePair, V]:
        """

        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    def HasKey(self, key: K) -> bool:
        """

        :param key:
        :return:
        """
    def Lookup(self, key: K) -> V:
        """

        :param key:
        :return:
        """
    def Split(
        self, first: IMapView[K, V], second: IMapView[K, V]
    ) -> Tuple[None, IMapView[K, V], IMapView[K, V]]:
        """

        :param first:
        :param second:
        """
    @overload
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[IKeyValuePair, V]:
        """

        :return:
        """

class IMap(Generic[K, V], IEnumerable[IKeyValuePair, V], IEnumerable, IIterable[IKeyValuePair, V]):
    """"""

    @property
    def Size(self) -> int:
        """

        :return:
        """
    def Clear(self) -> None:
        """"""
    def First(self) -> IIterator[IKeyValuePair, V]:
        """

        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    def GetView(self) -> IReadOnlyDictionary[K, V]:
        """

        :return:
        """
    def HasKey(self, key: K) -> bool:
        """

        :param key:
        :return:
        """
    def Insert(self, key: K, value: V) -> bool:
        """

        :param key:
        :param value:
        :return:
        """
    def Lookup(self, key: K) -> V:
        """

        :param key:
        :return:
        """
    def Remove(self, key: K) -> None:
        """

        :param key:
        """
    @overload
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[IKeyValuePair, V]:
        """

        :return:
        """

class INotifyCollectionChangedEventArgs:
    """"""

    @property
    def Action(self) -> NotifyCollectionChangedAction:
        """

        :return:
        """
    @property
    def NewItems(self) -> IList:
        """

        :return:
        """
    @property
    def NewStartingIndex(self) -> int:
        """

        :return:
        """
    @property
    def OldItems(self) -> IList:
        """

        :return:
        """
    @property
    def OldStartingIndex(self) -> int:
        """

        :return:
        """

class INotifyCollectionChanged_WinRT:
    """"""

class INotifyPropertyChanged_WinRT:
    """"""

class IPropertyChangedEventArgs:
    """"""

    @property
    def PropertyName(self) -> str:
        """

        :return:
        """

class IPropertyValue:
    """"""

    @property
    def IsNumericScalar(self) -> bool:
        """

        :return:
        """
    @property
    def Type(self) -> PropertyType:
        """

        :return:
        """
    def GetBoolean(self) -> bool:
        """

        :return:
        """
    def GetBooleanArray(self) -> Array[bool]:
        """

        :return:
        """
    def GetChar16(self) -> Char:
        """

        :return:
        """
    def GetChar16Array(self) -> Array[Char]:
        """

        :return:
        """
    def GetDateTime(self) -> DateTimeOffset:
        """

        :return:
        """
    def GetDateTimeArray(self) -> Array[DateTimeOffset]:
        """

        :return:
        """
    def GetDouble(self) -> float:
        """

        :return:
        """
    def GetDoubleArray(self) -> Array[float]:
        """

        :return:
        """
    def GetGuid(self) -> Guid:
        """

        :return:
        """
    def GetGuidArray(self) -> Array[Guid]:
        """

        :return:
        """
    def GetInspectableArray(self) -> Array[object]:
        """

        :return:
        """
    def GetInt16(self) -> int:
        """

        :return:
        """
    def GetInt16Array(self) -> Array[int]:
        """

        :return:
        """
    def GetInt32(self) -> int:
        """

        :return:
        """
    def GetInt32Array(self) -> Array[int]:
        """

        :return:
        """
    def GetInt64(self) -> int:
        """

        :return:
        """
    def GetInt64Array(self) -> Array[int]:
        """

        :return:
        """
    def GetPoint(self) -> Point:
        """

        :return:
        """
    def GetPointArray(self) -> Array[Point]:
        """

        :return:
        """
    def GetRect(self) -> Rect:
        """

        :return:
        """
    def GetRectArray(self) -> Array[Rect]:
        """

        :return:
        """
    def GetSingle(self) -> float:
        """

        :return:
        """
    def GetSingleArray(self) -> Array[float]:
        """

        :return:
        """
    def GetSize(self) -> Size:
        """

        :return:
        """
    def GetSizeArray(self) -> Array[Size]:
        """

        :return:
        """
    def GetString(self) -> str:
        """

        :return:
        """
    def GetStringArray(self) -> Array[str]:
        """

        :return:
        """
    def GetTimeSpan(self) -> TimeSpan:
        """

        :return:
        """
    def GetTimeSpanArray(self) -> Array[TimeSpan]:
        """

        :return:
        """
    def GetUInt16(self) -> int:
        """

        :return:
        """
    def GetUInt16Array(self) -> Array[int]:
        """

        :return:
        """
    def GetUInt32(self) -> int:
        """

        :return:
        """
    def GetUInt32Array(self) -> Array[int]:
        """

        :return:
        """
    def GetUInt64(self) -> int:
        """

        :return:
        """
    def GetUInt64Array(self) -> Array[int]:
        """

        :return:
        """
    def GetUInt8(self) -> int:
        """

        :return:
        """
    def GetUInt8Array(self) -> Array[int]:
        """

        :return:
        """

class IReadOnlyDictionaryToIMapViewAdapter(Object):
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

class IReadOnlyListToIVectorViewAdapter(Object):
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

class IReferenceArray(Generic[T], IPropertyValue):
    """"""

    @property
    def IsNumericScalar(self) -> bool:
        """

        :return:
        """
    @property
    def Type(self) -> PropertyType:
        """

        :return:
        """
    @property
    def Value(self) -> Array[T]:
        """

        :return:
        """
    def GetBoolean(self) -> bool:
        """

        :return:
        """
    def GetBooleanArray(self) -> Array[bool]:
        """

        :return:
        """
    def GetChar16(self) -> Char:
        """

        :return:
        """
    def GetChar16Array(self) -> Array[Char]:
        """

        :return:
        """
    def GetDateTime(self) -> DateTimeOffset:
        """

        :return:
        """
    def GetDateTimeArray(self) -> Array[DateTimeOffset]:
        """

        :return:
        """
    def GetDouble(self) -> float:
        """

        :return:
        """
    def GetDoubleArray(self) -> Array[float]:
        """

        :return:
        """
    def GetGuid(self) -> Guid:
        """

        :return:
        """
    def GetGuidArray(self) -> Array[Guid]:
        """

        :return:
        """
    def GetInspectableArray(self) -> Array[object]:
        """

        :return:
        """
    def GetInt16(self) -> int:
        """

        :return:
        """
    def GetInt16Array(self) -> Array[int]:
        """

        :return:
        """
    def GetInt32(self) -> int:
        """

        :return:
        """
    def GetInt32Array(self) -> Array[int]:
        """

        :return:
        """
    def GetInt64(self) -> int:
        """

        :return:
        """
    def GetInt64Array(self) -> Array[int]:
        """

        :return:
        """
    def GetPoint(self) -> Point:
        """

        :return:
        """
    def GetPointArray(self) -> Array[Point]:
        """

        :return:
        """
    def GetRect(self) -> Rect:
        """

        :return:
        """
    def GetRectArray(self) -> Array[Rect]:
        """

        :return:
        """
    def GetSingle(self) -> float:
        """

        :return:
        """
    def GetSingleArray(self) -> Array[float]:
        """

        :return:
        """
    def GetSize(self) -> Size:
        """

        :return:
        """
    def GetSizeArray(self) -> Array[Size]:
        """

        :return:
        """
    def GetString(self) -> str:
        """

        :return:
        """
    def GetStringArray(self) -> Array[str]:
        """

        :return:
        """
    def GetTimeSpan(self) -> TimeSpan:
        """

        :return:
        """
    def GetTimeSpanArray(self) -> Array[TimeSpan]:
        """

        :return:
        """
    def GetUInt16(self) -> int:
        """

        :return:
        """
    def GetUInt16Array(self) -> Array[int]:
        """

        :return:
        """
    def GetUInt32(self) -> int:
        """

        :return:
        """
    def GetUInt32Array(self) -> Array[int]:
        """

        :return:
        """
    def GetUInt64(self) -> int:
        """

        :return:
        """
    def GetUInt64Array(self) -> Array[int]:
        """

        :return:
        """
    def GetUInt8(self) -> int:
        """

        :return:
        """
    def GetUInt8Array(self) -> Array[int]:
        """

        :return:
        """

class IReferenceFactory(ABC, Object):
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

class IReference(Generic[T], IPropertyValue):
    """"""

    @property
    def IsNumericScalar(self) -> bool:
        """

        :return:
        """
    @property
    def Type(self) -> PropertyType:
        """

        :return:
        """
    @property
    def Value(self) -> T:
        """

        :return:
        """
    def GetBoolean(self) -> bool:
        """

        :return:
        """
    def GetBooleanArray(self) -> Array[bool]:
        """

        :return:
        """
    def GetChar16(self) -> Char:
        """

        :return:
        """
    def GetChar16Array(self) -> Array[Char]:
        """

        :return:
        """
    def GetDateTime(self) -> DateTimeOffset:
        """

        :return:
        """
    def GetDateTimeArray(self) -> Array[DateTimeOffset]:
        """

        :return:
        """
    def GetDouble(self) -> float:
        """

        :return:
        """
    def GetDoubleArray(self) -> Array[float]:
        """

        :return:
        """
    def GetGuid(self) -> Guid:
        """

        :return:
        """
    def GetGuidArray(self) -> Array[Guid]:
        """

        :return:
        """
    def GetInspectableArray(self) -> Array[object]:
        """

        :return:
        """
    def GetInt16(self) -> int:
        """

        :return:
        """
    def GetInt16Array(self) -> Array[int]:
        """

        :return:
        """
    def GetInt32(self) -> int:
        """

        :return:
        """
    def GetInt32Array(self) -> Array[int]:
        """

        :return:
        """
    def GetInt64(self) -> int:
        """

        :return:
        """
    def GetInt64Array(self) -> Array[int]:
        """

        :return:
        """
    def GetPoint(self) -> Point:
        """

        :return:
        """
    def GetPointArray(self) -> Array[Point]:
        """

        :return:
        """
    def GetRect(self) -> Rect:
        """

        :return:
        """
    def GetRectArray(self) -> Array[Rect]:
        """

        :return:
        """
    def GetSingle(self) -> float:
        """

        :return:
        """
    def GetSingleArray(self) -> Array[float]:
        """

        :return:
        """
    def GetSize(self) -> Size:
        """

        :return:
        """
    def GetSizeArray(self) -> Array[Size]:
        """

        :return:
        """
    def GetString(self) -> str:
        """

        :return:
        """
    def GetStringArray(self) -> Array[str]:
        """

        :return:
        """
    def GetTimeSpan(self) -> TimeSpan:
        """

        :return:
        """
    def GetTimeSpanArray(self) -> Array[TimeSpan]:
        """

        :return:
        """
    def GetUInt16(self) -> int:
        """

        :return:
        """
    def GetUInt16Array(self) -> Array[int]:
        """

        :return:
        """
    def GetUInt32(self) -> int:
        """

        :return:
        """
    def GetUInt32Array(self) -> Array[int]:
        """

        :return:
        """
    def GetUInt64(self) -> int:
        """

        :return:
        """
    def GetUInt64Array(self) -> Array[int]:
        """

        :return:
        """
    def GetUInt8(self) -> int:
        """

        :return:
        """
    def GetUInt8Array(self) -> Array[int]:
        """

        :return:
        """

class IRestrictedErrorInfo:
    """"""

    def GetErrorDetails(
        self, description: str, error: int, restrictedDescription: str, capabilitySid: str
    ) -> Tuple[None, str, int, str, str]:
        """

        :param description:
        :param error:
        :param restrictedDescription:
        :param capabilitySid:
        """
    def GetReference(self, reference: str) -> Tuple[None, str]:
        """

        :param reference:
        """

class IStringable:
    """"""

    def ToString(self) -> str:
        """

        :return:
        """

class IStringableHelper(Object):
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

class IVectorViewToIReadOnlyListAdapter(Object):
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

class IVectorView(Generic[T], IEnumerable[T], IEnumerable, IIterable[T]):
    """"""

    @property
    def Size(self) -> int:
        """

        :return:
        """
    def First(self) -> IIterator[T]:
        """

        :return:
        """
    def GetAt(self, index: int) -> T:
        """

        :param index:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    def GetMany(self, startIndex: int, items: Array[T]) -> Tuple[int, Array[T]]:
        """

        :param startIndex:
        :param items:
        :return:
        """
    def IndexOf(self, value: T, index: int) -> Tuple[bool, int]:
        """

        :param value:
        :param index:
        :return:
        """
    @overload
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[T]:
        """

        :return:
        """

class IVector(Generic[T], IEnumerable[T], IEnumerable, IIterable[T]):
    """"""

    @property
    def Size(self) -> int:
        """

        :return:
        """
    def Append(self, value: T) -> None:
        """

        :param value:
        """
    def Clear(self) -> None:
        """"""
    def First(self) -> IIterator[T]:
        """

        :return:
        """
    def GetAt(self, index: int) -> T:
        """

        :param index:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    def GetMany(self, startIndex: int, items: Array[T]) -> Tuple[int, Array[T]]:
        """

        :param startIndex:
        :param items:
        :return:
        """
    def GetView(self) -> IReadOnlyList[T]:
        """

        :return:
        """
    def IndexOf(self, value: T, index: int) -> Tuple[bool, int]:
        """

        :param value:
        :param index:
        :return:
        """
    def InsertAt(self, index: int, value: T) -> None:
        """

        :param index:
        :param value:
        """
    def RemoveAt(self, index: int) -> None:
        """

        :param index:
        """
    def RemoveAtEnd(self) -> None:
        """"""
    def ReplaceAll(self, items: Array[T]) -> None:
        """

        :param items:
        """
    def SetAt(self, index: int, value: T) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[T]:
        """

        :return:
        """

class IVector_Raw(Generic[T], IEnumerable[T], IEnumerable, IIterable[T]):
    """"""

    @property
    def Size(self) -> int:
        """

        :return:
        """
    def Append(self, value: T) -> None:
        """

        :param value:
        """
    def Clear(self) -> None:
        """"""
    def First(self) -> IIterator[T]:
        """

        :return:
        """
    def GetAt(self, index: int) -> T:
        """

        :param index:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    def GetMany(self, startIndex: int, items: Array[T]) -> Tuple[int, Array[T]]:
        """

        :param startIndex:
        :param items:
        :return:
        """
    def GetView(self) -> IVectorView[T]:
        """

        :return:
        """
    def IndexOf(self, value: T, index: int) -> Tuple[bool, int]:
        """

        :param value:
        :param index:
        :return:
        """
    def InsertAt(self, index: int, value: T) -> None:
        """

        :param index:
        :param value:
        """
    def RemoveAt(self, index: int) -> None:
        """

        :param index:
        """
    def RemoveAtEnd(self) -> None:
        """"""
    def ReplaceAll(self, items: Array[T]) -> None:
        """

        :param items:
        """
    def SetAt(self, index: int, value: T) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[T]:
        """

        :return:
        """

class IWinRTClassActivator:
    """"""

    def ActivateInstance(self, activatableClassId: str) -> object:
        """

        :param activatableClassId:
        :return:
        """
    def GetActivationFactory(self, activatableClassId: str, iid: Guid) -> IntPtr:
        """

        :param activatableClassId:
        :param iid:
        :return:
        """

Indexer_Get_Delegate: Callable[[int], T] = ...
"""

:param index: 
:return: 
"""

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
    ):
        """

        :param interfaceType:
        :param majorVersion:
        :param minorVersion:
        :param buildVersion:
        :param revisionVersion:
        """
    @property
    def BuildVersion(self) -> int:
        """

        :return:
        """
    @property
    def InterfaceType(self) -> Type:
        """

        :return:
        """
    @property
    def MajorVersion(self) -> int:
        """

        :return:
        """
    @property
    def MinorVersion(self) -> int:
        """

        :return:
        """
    @property
    def RevisionVersion(self) -> int:
        """

        :return:
        """
    @property
    def TypeId(self) -> object:
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
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """

        :return:
        """
    def Match(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class IterableToEnumerableAdapter(Object):
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

class IteratorToEnumeratorAdapter(Generic[T], Object, IEnumerator[T], IEnumerator, IDisposable):
    """"""

    @property
    def Current(self) -> object:
        """

        :return:
        """
    def Dispose(self) -> None:
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
    def MoveNext(self) -> bool:
        """

        :return:
        """
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class ListToBindableVectorAdapter(Object):
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

class ListToBindableVectorViewAdapter(Object, IBindableIterable, IBindableVectorView):
    """"""

    @property
    def Size(self) -> int:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def First(self) -> IBindableIterator:
        """

        :return:
        """
    def GetAt(self, index: int) -> object:
        """

        :param index:
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
    def IndexOf(self, value: object, index: int) -> Tuple[bool, int]:
        """

        :param value:
        :param index:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class ListToVectorAdapter(Object):
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

class ManagedActivationFactory(Object, IActivationFactory, IManagedActivationFactory):
    """"""

    def ActivateInstance(self) -> object:
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
    def RunClassConstructor(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class MapToCollectionAdapter(Object):
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

class MapToDictionaryAdapter(Object):
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

class MapViewToReadOnlyCollectionAdapter(Object):
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

class NamespaceResolveEventArgs(EventArgs):
    """"""

    def __init__(self, namespaceName: str, requestingAssembly: Assembly):
        """

        :param namespaceName:
        :param requestingAssembly:
        """
    @property
    def NamespaceName(self) -> str:
        """

        :return:
        """
    @property
    def RequestingAssembly(self) -> Assembly:
        """

        :return:
        """
    @property
    def ResolvedAssemblies(self) -> Collection[Assembly]:
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

class NotifyCollectionChangedEventArgsMarshaler(ABC, Object):
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

NotifyCollectionChangedEventHandler_WinRT: Callable[
    [object, NotifyCollectionChangedEventArgs], None
] = ...
"""

:param sender: 
:param e: 
"""

class NotifyCollectionChangedToManagedAdapter(Object):
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

class NotifyCollectionChangedToWinRTAdapter(Object):
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

class NotifyPropertyChangedToManagedAdapter(Object):
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

class NotifyPropertyChangedToWinRTAdapter(Object):
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

class Point(ValueType):
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

class PropertyChangedEventArgsMarshaler(ABC, Object):
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

PropertyChangedEventHandler_WinRT: Callable[[object, PropertyChangedEventArgs], None] = ...
"""

:param sender: 
:param e: 
"""

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

    def __init__(self):
        """"""
    @property
    def TypeId(self) -> object:
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
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """

        :return:
        """
    def Match(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class ReadOnlyDictionaryKeyCollection(
    Generic[TKey, TValue], Object, IEnumerable[TKey], IEnumerable
):
    """"""

    def __init__(self, dictionary: IReadOnlyDictionary[TKey, TValue]):
        """

        :param dictionary:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

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
    @overload
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[TKey]:
        """

        :return:
        """

class ReadOnlyDictionaryKeyEnumerator(
    Generic[TKey, TValue], Object, IEnumerator[TKey], IEnumerator, IDisposable
):
    """"""

    def __init__(self, dictionary: IReadOnlyDictionary[TKey, TValue]):
        """

        :param dictionary:
        """
    @property
    def Current(self) -> object:
        """

        :return:
        """
    def Dispose(self) -> None:
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
    def MoveNext(self) -> bool:
        """

        :return:
        """
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class ReadOnlyDictionaryValueCollection(
    Generic[TKey, TValue], Object, IEnumerable[TValue], IEnumerable
):
    """"""

    def __init__(self, dictionary: IReadOnlyDictionary[TKey, TValue]):
        """

        :param dictionary:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

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
    @overload
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[TValue]:
        """

        :return:
        """

class ReadOnlyDictionaryValueEnumerator(
    Generic[TKey, TValue], Object, IEnumerator[TValue], IEnumerator, IDisposable
):
    """"""

    def __init__(self, dictionary: IReadOnlyDictionary[TKey, TValue]):
        """

        :param dictionary:
        """
    @property
    def Current(self) -> object:
        """

        :return:
        """
    def Dispose(self) -> None:
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
    def MoveNext(self) -> bool:
        """

        :return:
        """
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class Rect(ValueType):
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

class ReturnValueNameAttribute(Attribute, _Attribute):
    """"""

    def __init__(self, name: str):
        """

        :param name:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def TypeId(self) -> object:
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
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """

        :return:
        """
    def Match(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class RuntimeClass(ABC, __ComObject):
    """"""

    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """

        :param requestedType:
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
    def GetLifetimeService(self) -> object:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def InitializeLifetimeService(self) -> object:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class Size(ValueType):
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

class UnsafeNativeMethods(ABC, Object):
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

class VectorToCollectionAdapter(Object):
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

class VectorToListAdapter(Object):
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

class VectorViewToReadOnlyCollectionAdapter(Object):
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

class WinRTClassActivator(MarshalByRefObject, IWinRTClassActivator):
    """"""

    def __init__(self):
        """"""
    def ActivateInstance(self, activatableClassId: str) -> object:
        """

        :param activatableClassId:
        :return:
        """
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """

        :param requestedType:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetActivationFactory(self, activatableClassId: str, iid: Guid) -> IntPtr:
        """

        :param activatableClassId:
        :param iid:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetLifetimeService(self) -> object:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def InitializeLifetimeService(self) -> object:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

WindowsFoundationEventHandler: Callable[[object, T], None] = ...
"""

:param sender: 
:param args: 
"""

class WindowsRuntimeBufferHelper(ABC, Object):
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

class WindowsRuntimeImportAttribute(Attribute, _Attribute):
    """"""

    def __init__(self):
        """"""
    @property
    def TypeId(self) -> object:
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
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """

        :return:
        """
    def Match(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class WindowsRuntimeMarshal(ABC, Object):
    """"""

    @classmethod
    def AddEventHandler(
        cls,
        addMethod: Func[T, EventRegistrationToken],
        removeMethod: Action[EventRegistrationToken],
        handler: T,
    ) -> None:
        """

        :param addMethod:
        :param removeMethod:
        :param handler:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @classmethod
    def FreeHString(cls, ptr: IntPtr) -> None:
        """

        :param ptr:
        """
    @classmethod
    def GetActivationFactory(cls, type: Type) -> IActivationFactory:
        """

        :param type:
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
    def PtrToStringHString(cls, ptr: IntPtr) -> str:
        """

        :param ptr:
        :return:
        """
    @classmethod
    def RemoveAllEventHandlers(cls, removeMethod: Action[EventRegistrationToken]) -> None:
        """

        :param removeMethod:
        """
    @classmethod
    def RemoveEventHandler(cls, removeMethod: Action[EventRegistrationToken], handler: T) -> None:
        """

        :param removeMethod:
        :param handler:
        """
    @classmethod
    def StringToHString(cls, s: str) -> IntPtr:
        """

        :param s:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class WindowsRuntimeMetadata(ABC, Object):
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
    def ResolveNamespace(
        cls, namespaceName: str, packageGraphFilePaths: IEnumerable[str]
    ) -> IEnumerable[str]:
        """

        :param namespaceName:
        :param packageGraphFilePaths:
        :return:
        """
    @classmethod
    @overload
    def ResolveNamespace(
        cls, namespaceName: str, windowsSdkFilePath: str, packageGraphFilePaths: IEnumerable[str]
    ) -> IEnumerable[str]:
        """

        :param namespaceName:
        :param windowsSdkFilePath:
        :param packageGraphFilePaths:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    DesignerNamespaceResolve: EventType[EventHandler[DesignerNamespaceResolveEventArgs]] = ...
    """"""
    ReflectionOnlyNamespaceResolve: EventType[EventHandler[NamespaceResolveEventArgs]] = ...
    """"""

class WriteOnlyArrayAttribute(Attribute, _Attribute):
    """"""

    def __init__(self):
        """"""
    @property
    def TypeId(self) -> object:
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
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """

        :return:
        """
    def Match(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
