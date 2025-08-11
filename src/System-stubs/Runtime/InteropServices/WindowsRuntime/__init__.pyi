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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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
    def ContainsKey(self, key: TKey) -> bool:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def First[TKey, TValue](self) -> IIterator[IKeyValuePair[TKey, TValue]]:
        """"""
    def GetEnumerator[TKey, TValue](self) -> IEnumerator[IKeyValuePair[TKey, TValue]]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def HasKey[TKey](self, key: TKey) -> bool:
        """"""
    def Lookup[TKey, TValue](self, key: TKey) -> TValue:
        """"""
    def Split[TKey, TValue](
        self, firstPartition: IMapView[TKey, TValue], secondPartition: IMapView[TKey, TValue]
    ) -> tuple[None, IMapView[TKey, TValue], IMapView[TKey, TValue]]:
        """"""
    def ToString(self) -> str:
        """"""
    def TryGetValue(self, key: TKey, value: TValue) -> tuple[bool, TValue]:
        """"""
    def __contains__(self, key: TKey) -> bool:
        """"""
    def __iter__[TKey, TValue](self) -> Iterator[IKeyValuePair[TKey, TValue]]:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, key: TKey) -> TValue:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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
    def CopyTo[TKey](self, array: Array[TKey], index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator[TKey](self) -> IEnumerator[TKey]:
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
    def __iter__[TKey](self) -> Iterator[TKey]:
        """"""
    def __delitem__[TKey](self, item: TKey) -> bool:
        """"""
    def __len__(self) -> int:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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
    def CopyTo[TValue](self, array: Array[TValue], index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator[TValue](self) -> IEnumerator[TValue]:
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
    def __iter__[TValue](self) -> Iterator[TValue]:
        """"""
    def __delitem__[TValue](self, item: TValue) -> bool:
        """"""
    def __len__(self) -> int:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class EventRegistrationTokenTable[T](Object):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def InvocationList(self) -> T:
        """"""
    @InvocationList.setter
    def InvocationList(self, value: T) -> None: ...
    def AddEventHandler(self, handler: T) -> EventRegistrationToken:
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
    def RemoveEventHandler(self, handler: T) -> None:
        """"""
    @overload
    def RemoveEventHandler(self, token: EventRegistrationToken) -> None:
        """"""
    def ToString(self) -> str:
        """"""

type GetEnumerator_Delegate[T] = Callable[[], IEnumerator[T]]
""""""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IActivationFactory(ABC):
    """"""
    def ActivateInstance(self) -> object:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IBindableIterable(ABC):
    """"""
    def First(self) -> IBindableIterator:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IBindableIterator(ABC):
    """"""
    @property
    def Current(self) -> object:
        """"""
    @property
    def HasCurrent(self) -> bool:
        """"""
    def MoveNext(self) -> bool:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IBindableVector(ABC, IBindableIterable):
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IBindableVectorView(ABC, IBindableIterable):
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IClosable(ABC):
    """"""
    def Close(self) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ICommand_WinRT(ABC):
    """"""
    def CanExecute(self, parameter: object) -> bool:
        """"""
    def Execute(self, parameter: object) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ICustomProperty(ABC):
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ICustomPropertyProvider(ABC):
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IGetProxyTarget(ABC):
    """"""
    def GetTarget(self) -> object:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IIterable[T](ABC, IEnumerable[T], IEnumerable):
    """"""
    def First(self) -> IIterator[T]:
        """"""
    def GetEnumerator[T](self) -> IEnumerator[T]:
        """"""
    def __iter__[T](self) -> Iterator[T]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IIterator[T](ABC):
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IKeyValuePair[K, V](ABC):
    """"""
    @property
    def Key(self) -> K:
        """"""
    @property
    def Value(self) -> V:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IManagedActivationFactory(ABC):
    """"""
    def RunClassConstructor(self) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IMapView[K, V](
    ABC, IEnumerable[IKeyValuePair[K, V]], IEnumerable, IIterable[IKeyValuePair[K, V]]
):
    """"""
    @property
    def Size(self) -> int:
        """"""
    def First[K, V](self) -> IIterator[IKeyValuePair[K, V]]:
        """"""
    def GetEnumerator[K, V](self) -> IEnumerator[IKeyValuePair[K, V]]:
        """"""
    def HasKey(self, key: K) -> bool:
        """"""
    def Lookup(self, key: K) -> V:
        """"""
    def Split(
        self, first: IMapView[K, V], second: IMapView[K, V]
    ) -> tuple[None, IMapView[K, V], IMapView[K, V]]:
        """"""
    def __iter__[K, V](self) -> Iterator[IKeyValuePair[K, V]]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IMap[K, V](
    ABC, IEnumerable[IKeyValuePair[K, V]], IEnumerable, IIterable[IKeyValuePair[K, V]]
):
    """"""
    @property
    def Size(self) -> int:
        """"""
    def Clear(self) -> None:
        """"""
    def First[K, V](self) -> IIterator[IKeyValuePair[K, V]]:
        """"""
    def GetEnumerator[K, V](self) -> IEnumerator[IKeyValuePair[K, V]]:
        """"""
    def GetView(self) -> IReadOnlyDictionary[K, V]:
        """"""
    def HasKey(self, key: K) -> bool:
        """"""
    def Insert(self, key: K, value: V) -> bool:
        """"""
    def Lookup(self, key: K) -> V:
        """"""
    def Remove(self, key: K) -> None:
        """"""
    def __iter__[K, V](self) -> Iterator[IKeyValuePair[K, V]]:
        """"""
    def __delitem__(self, key: K) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class INotifyCollectionChangedEventArgs(ABC):
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class INotifyCollectionChanged_WinRT(ABC):
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class INotifyPropertyChanged_WinRT(ABC):
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IPropertyChangedEventArgs(ABC):
    """"""
    @property
    def PropertyName(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IPropertyValue(ABC):
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IReferenceArray[T](ABC, IPropertyValue):
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IReference[T](ABC, IPropertyValue):
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IRestrictedErrorInfo(ABC):
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IStringable(ABC):
    """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IVectorView[T](ABC, IEnumerable[T], IEnumerable, IIterable[T]):
    """"""
    @property
    def Size(self) -> int:
        """"""
    def First(self) -> IIterator[T]:
        """"""
    def GetAt(self, index: int) -> T:
        """"""
    def GetEnumerator[T](self) -> IEnumerator[T]:
        """"""
    def GetMany(self, startIndex: int, items: Array[T]) -> tuple[int, Array[T]]:
        """"""
    def IndexOf(self, value: T, index: UInt32) -> tuple[bool, UInt32]:
        """"""
    def __iter__[T](self) -> Iterator[T]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IVector[T](ABC, IEnumerable[T], IEnumerable, IIterable[T]):
    """"""
    @property
    def Size(self) -> int:
        """"""
    def Append(self, value: T) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    def First(self) -> IIterator[T]:
        """"""
    def GetAt(self, index: int) -> T:
        """"""
    def GetEnumerator[T](self) -> IEnumerator[T]:
        """"""
    def GetMany(self, startIndex: int, items: Array[T]) -> tuple[int, Array[T]]:
        """"""
    def GetView(self) -> IReadOnlyList[T]:
        """"""
    def IndexOf(self, value: T, index: UInt32) -> tuple[bool, UInt32]:
        """"""
    def InsertAt(self, index: int, value: T) -> None:
        """"""
    def RemoveAt(self, index: int) -> None:
        """"""
    def RemoveAtEnd(self) -> None:
        """"""
    def ReplaceAll(self, items: Array[T]) -> None:
        """"""
    def SetAt(self, index: int, value: T) -> None:
        """"""
    def __iter__[T](self) -> Iterator[T]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IVector_Raw[T](ABC, IEnumerable[T], IEnumerable, IIterable[T]):
    """"""
    @property
    def Size(self) -> int:
        """"""
    def Append(self, value: T) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    def First(self) -> IIterator[T]:
        """"""
    def GetAt(self, index: int) -> T:
        """"""
    def GetEnumerator[T](self) -> IEnumerator[T]:
        """"""
    def GetMany(self, startIndex: int, items: Array[T]) -> tuple[int, Array[T]]:
        """"""
    def GetView(self) -> IVectorView[T]:
        """"""
    def IndexOf(self, value: T, index: UInt32) -> tuple[bool, UInt32]:
        """"""
    def InsertAt(self, index: int, value: T) -> None:
        """"""
    def RemoveAt(self, index: int) -> None:
        """"""
    def RemoveAtEnd(self) -> None:
        """"""
    def ReplaceAll(self, items: Array[T]) -> None:
        """"""
    def SetAt(self, index: int, value: T) -> None:
        """"""
    def __iter__[T](self) -> Iterator[T]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IWinRTClassActivator(ABC):
    """"""
    def ActivateInstance(self, activatableClassId: str) -> object:
        """"""
    def GetActivationFactory(self, activatableClassId: str, iid: Guid) -> IntPtr:
        """"""

type Indexer_Get_Delegate[T] = Callable[[int], T]
""""""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

type NotifyCollectionChangedEventHandler_WinRT = Callable[
    [object, NotifyCollectionChangedEventArgs], None
]
""""""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

type PropertyChangedEventHandler_WinRT = Callable[[object, PropertyChangedEventArgs], None]
""""""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ReadOnlyDictionaryKeyCollection[TKey, TValue](Object, IEnumerable[TKey], IEnumerable):
    """"""
    def __init__(self, dictionary: IReadOnlyDictionary[TKey, TValue]) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator[TKey](self) -> IEnumerator[TKey]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def __iter__[TKey](self) -> Iterator[TKey]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ReadOnlyDictionaryValueCollection[TKey, TValue](Object, IEnumerable[TValue], IEnumerable):
    """"""
    def __init__(self, dictionary: IReadOnlyDictionary[TKey, TValue]) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator[TValue](self) -> IEnumerator[TValue]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def __iter__[TValue](self) -> Iterator[TValue]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

type WindowsFoundationEventHandler[T] = Callable[[object, T], None]
""""""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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
