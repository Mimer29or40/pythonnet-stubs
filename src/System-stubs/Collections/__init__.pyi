"""Automatically generated stubs for C# namespace: System.Collections."""

from abc import ABC
from collections.abc import Iterator
from typing import ClassVar
from typing import overload

from System import Array
from System import ICloneable
from System import Object
from System import Type
from System import ValueType
from System.Globalization import CultureInfo
from System.Runtime.Serialization import IDeserializationCallback
from System.Runtime.Serialization import ISerializable
from System.Runtime.Serialization import SerializationInfo
from System.Runtime.Serialization import StreamingContext

class ArrayList(Object, ICollection, IEnumerable, IList, ICloneable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, capacity: int) -> None:
        """"""
    @overload
    def __init__(self, c: ICollection) -> None:
        """"""
    @property
    def Capacity(self) -> int:
        """"""
    @Capacity.setter
    def Capacity(self, value: int) -> None: ...
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
    def SyncRoot(self) -> object:
        """"""
    @classmethod
    def Adapter(cls, list: IList) -> ArrayList:
        """"""
    def Add(self, value: object) -> int:
        """"""
    def AddRange(self, c: ICollection) -> None:
        """"""
    @overload
    def BinarySearch(self, index: int, count: int, value: object, comparer: IComparer) -> int:
        """"""
    @overload
    def BinarySearch(self, value: object) -> int:
        """"""
    @overload
    def BinarySearch(self, value: object, comparer: IComparer) -> int:
        """"""
    def Clear(self) -> None:
        """"""
    def Clone(self) -> object:
        """"""
    def Contains(self, item: object) -> bool:
        """"""
    @overload
    def CopyTo(self, array: Array) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array, arrayIndex: int) -> None:
        """"""
    @overload
    def CopyTo(self, index: int, array: Array, arrayIndex: int, count: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    @overload
    def FixedSize(cls, list: ArrayList) -> ArrayList:
        """"""
    @classmethod
    @overload
    def FixedSize(cls, list: IList) -> IList:
        """"""
    @overload
    def GetEnumerator(self) -> IEnumerator:
        """"""
    @overload
    def GetEnumerator(self, index: int, count: int) -> IEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetRange(self, index: int, count: int) -> ArrayList:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IndexOf(self, value: object) -> int:
        """"""
    @overload
    def IndexOf(self, value: object, startIndex: int) -> int:
        """"""
    @overload
    def IndexOf(self, value: object, startIndex: int, count: int) -> int:
        """"""
    def Insert(self, index: int, value: object) -> None:
        """"""
    def InsertRange(self, index: int, c: ICollection) -> None:
        """"""
    @overload
    def LastIndexOf(self, value: object) -> int:
        """"""
    @overload
    def LastIndexOf(self, value: object, startIndex: int) -> int:
        """"""
    @overload
    def LastIndexOf(self, value: object, startIndex: int, count: int) -> int:
        """"""
    @classmethod
    @overload
    def ReadOnly(cls, list: ArrayList) -> ArrayList:
        """"""
    @classmethod
    @overload
    def ReadOnly(cls, list: IList) -> IList:
        """"""
    def Remove(self, obj: object) -> None:
        """"""
    def RemoveAt(self, index: int) -> None:
        """"""
    def RemoveRange(self, index: int, count: int) -> None:
        """"""
    @classmethod
    def Repeat(cls, value: object, count: int) -> ArrayList:
        """"""
    @overload
    def Reverse(self) -> None:
        """"""
    @overload
    def Reverse(self, index: int, count: int) -> None:
        """"""
    def SetRange(self, index: int, c: ICollection) -> None:
        """"""
    @overload
    def Sort(self) -> None:
        """"""
    @overload
    def Sort(self, comparer: IComparer) -> None:
        """"""
    @overload
    def Sort(self, index: int, count: int, comparer: IComparer) -> None:
        """"""
    @classmethod
    @overload
    def Synchronized(cls, list: ArrayList) -> ArrayList:
        """"""
    @classmethod
    @overload
    def Synchronized(cls, list: IList) -> IList:
        """"""
    @overload
    def ToArray(self) -> Array[object]:
        """"""
    @overload
    def ToArray(self, type: Type) -> Array:
        """"""
    def ToString(self) -> str:
        """"""
    def TrimToSize(self) -> None:
        """"""
    def __contains__(self, item: object) -> bool:
        """"""
    @overload
    def __iter__(self) -> Iterator:
        """"""
    @overload
    def __iter__(self, index: int, count: int) -> Iterator:
        """"""
    def __delitem__(self, obj: object) -> None:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, index: int) -> object:
        """"""
    def __setitem__(self, index: int, value: object) -> None:
        """"""

class BitArray(Object, ICollection, IEnumerable, ICloneable):
    """"""
    @overload
    def __init__(self, length: int) -> None:
        """"""
    @overload
    def __init__(self, length: int, defaultValue: bool) -> None:
        """"""
    @overload
    def __init__(self, bytes: Array[int]) -> None:
        """"""
    @overload
    def __init__(self, values: Array[bool]) -> None:
        """"""
    @overload
    def __init__(self, values: Array[int]) -> None:
        """"""
    @overload
    def __init__(self, bits: BitArray) -> None:
        """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def Item(self) -> bool:
        """"""
    @Item.setter
    def Item(self, value: bool) -> None: ...
    @property
    def Length(self) -> int:
        """"""
    @Length.setter
    def Length(self, value: int) -> None: ...
    @property
    def SyncRoot(self) -> object:
        """"""
    def And(self, value: BitArray) -> BitArray:
        """"""
    def Clone(self) -> object:
        """"""
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Get(self, index: int) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Not(self) -> BitArray:
        """"""
    def Or(self, value: BitArray) -> BitArray:
        """"""
    def Set(self, index: int, value: bool) -> None:
        """"""
    def SetAll(self, value: bool) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def Xor(self, value: BitArray) -> BitArray:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, index: int) -> bool:
        """"""
    def __setitem__(self, index: int, value: bool) -> None:
        """"""

class CaseInsensitiveComparer(Object, IComparer):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, culture: CultureInfo) -> None:
        """"""
    @classmethod
    @property
    def Default(cls) -> CaseInsensitiveComparer:
        """"""
    @classmethod
    @property
    def DefaultInvariant(cls) -> CaseInsensitiveComparer:
        """"""
    def Compare(self, a: object, b: object) -> int:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class CaseInsensitiveHashCodeProvider(Object, IHashCodeProvider):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, culture: CultureInfo) -> None:
        """"""
    @classmethod
    @property
    def Default(cls) -> CaseInsensitiveHashCodeProvider:
        """"""
    @classmethod
    @property
    def DefaultInvariant(cls) -> CaseInsensitiveHashCodeProvider:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetHashCode(self, obj: object) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class CollectionBase(ABC, Object, ICollection, IEnumerable, IList):
    """"""
    @property
    def Capacity(self) -> int:
        """"""
    @Capacity.setter
    def Capacity(self, value: int) -> None: ...
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
    def SyncRoot(self) -> object:
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
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
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

class Comparer(Object, IComparer, ISerializable):
    """"""

    Default: ClassVar[Comparer]
    """"""
    DefaultInvariant: ClassVar[Comparer]
    """"""
    def __init__(self, culture: CultureInfo) -> None:
        """"""
    def Compare(self, a: object, b: object) -> int:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class CompatibleComparer(Object, IEqualityComparer):
    """"""
    def Compare(self, a: object, b: object) -> int:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, a: object, b: object) -> bool:
        """"""
    @overload
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetHashCode(self, obj: object) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class DictionaryBase(ABC, Object, ICollection, IDictionary, IEnumerable):
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
    def Contains(self, key: object) -> bool:
        """"""
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IDictionaryEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
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

class DictionaryEntry(ValueType):
    """"""
    def __init__(self, key: object, value: object) -> None:
        """"""
    @property
    def Key(self) -> object:
        """"""
    @Key.setter
    def Key(self, value: object) -> None: ...
    @property
    def Value(self) -> object:
        """"""
    @Value.setter
    def Value(self, value: object) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class EmptyReadOnlyDictionaryInternal(Object, ICollection, IDictionary, IEnumerable):
    """"""
    def __init__(self) -> None:
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
    def Contains(self, key: object) -> bool:
        """"""
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IDictionaryEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
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

class HashHelpers(ABC, Object):
    """"""

    HashCollisionThreshold: ClassVar[int]
    """"""
    MaxPrimeArrayLength: ClassVar[int]
    """"""
    primes: ClassVar[Array[int]]
    """"""
    s_UseRandomizedStringHashing: ClassVar[bool]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def ExpandPrime(cls, oldSize: int) -> int:
        """"""
    @classmethod
    def GetEqualityComparerForSerialization(cls, comparer: object) -> object:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @classmethod
    def GetMinPrime(cls) -> int:
        """"""
    @classmethod
    def GetPrime(cls, min: int) -> int:
        """"""
    @classmethod
    def GetRandomizedEqualityComparer(cls, comparer: object) -> IEqualityComparer:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def IsPrime(cls, candidate: int) -> bool:
        """"""
    @classmethod
    def IsWellKnownEqualityComparer(cls, comparer: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

class Hashtable(
    Object,
    ICollection,
    IDictionary,
    IEnumerable,
    IDeserializationCallback,
    ISerializable,
    ICloneable,
):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, capacity: int) -> None:
        """"""
    @overload
    def __init__(self, capacity: int, loadFactor: float) -> None:
        """"""
    @overload
    def __init__(
        self, capacity: int, loadFactor: float, hcp: IHashCodeProvider, comparer: IComparer
    ) -> None:
        """"""
    @overload
    def __init__(
        self, capacity: int, loadFactor: float, equalityComparer: IEqualityComparer
    ) -> None:
        """"""
    @overload
    def __init__(self, hcp: IHashCodeProvider, comparer: IComparer) -> None:
        """"""
    @overload
    def __init__(self, equalityComparer: IEqualityComparer) -> None:
        """"""
    @overload
    def __init__(self, capacity: int, hcp: IHashCodeProvider, comparer: IComparer) -> None:
        """"""
    @overload
    def __init__(self, capacity: int, equalityComparer: IEqualityComparer) -> None:
        """"""
    @overload
    def __init__(self, d: IDictionary) -> None:
        """"""
    @overload
    def __init__(self, d: IDictionary, loadFactor: float) -> None:
        """"""
    @overload
    def __init__(self, d: IDictionary, hcp: IHashCodeProvider, comparer: IComparer) -> None:
        """"""
    @overload
    def __init__(self, d: IDictionary, equalityComparer: IEqualityComparer) -> None:
        """"""
    @overload
    def __init__(
        self, d: IDictionary, loadFactor: float, hcp: IHashCodeProvider, comparer: IComparer
    ) -> None:
        """"""
    @overload
    def __init__(
        self, d: IDictionary, loadFactor: float, equalityComparer: IEqualityComparer
    ) -> None:
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
    @classmethod
    def Synchronized(cls, table: Hashtable) -> Hashtable:
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

class ICollection(ABC, IEnumerable):
    """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def SyncRoot(self) -> object:
        """"""
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    def __len__(self) -> int:
        """"""

class IComparer(ABC):
    """"""
    def Compare(self, x: object, y: object) -> int:
        """"""

class IDictionary(ABC, ICollection, IEnumerable):
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
    def Contains(self, key: object) -> bool:
        """"""
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    def GetEnumerator(self) -> IDictionaryEnumerator:
        """"""
    def Remove(self, key: object) -> None:
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

class IDictionaryEnumerator(ABC, IEnumerator):
    """"""
    @property
    def Current(self) -> object:
        """"""
    @property
    def Entry(self) -> DictionaryEntry:
        """"""
    @property
    def Key(self) -> object:
        """"""
    @property
    def Value(self) -> object:
        """"""
    def MoveNext(self) -> bool:
        """"""
    def Reset(self) -> None:
        """"""

class IEnumerable(ABC):
    """"""
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def __iter__(self) -> Iterator:
        """"""

class IEnumerator(ABC):
    """"""
    @property
    def Current(self) -> object:
        """"""
    def MoveNext(self) -> bool:
        """"""
    def Reset(self) -> None:
        """"""

class IEqualityComparer(ABC):
    """"""
    def Equals(self, x: object, y: object) -> bool:
        """"""
    def GetHashCode(self, obj: object) -> int:
        """"""

class IHashCodeProvider(ABC):
    """"""
    def GetHashCode(self, obj: object) -> int:
        """"""

class IList(ABC, ICollection, IEnumerable):
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
    def SyncRoot(self) -> object:
        """"""
    def Add(self, value: object) -> int:
        """"""
    def Clear(self) -> None:
        """"""
    def Contains(self, value: object) -> bool:
        """"""
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def IndexOf(self, value: object) -> int:
        """"""
    def Insert(self, index: int, value: object) -> None:
        """"""
    def Remove(self, value: object) -> None:
        """"""
    def RemoveAt(self, index: int) -> None:
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

class IStructuralComparable(ABC):
    """"""
    def CompareTo(self, other: object, comparer: IComparer) -> int:
        """"""

class IStructuralEquatable(ABC):
    """"""
    def Equals(self, other: object, comparer: IEqualityComparer) -> bool:
        """"""
    def GetHashCode(self, comparer: IEqualityComparer) -> int:
        """"""

class KeyValuePairs(Object):
    """"""
    def __init__(self, key: object, value: object) -> None:
        """"""
    @property
    def Key(self) -> object:
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

class ListDictionaryInternal(Object, ICollection, IDictionary, IEnumerable):
    """"""
    def __init__(self) -> None:
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
    def Contains(self, key: object) -> bool:
        """"""
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IDictionaryEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
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

class Queue(Object, ICollection, IEnumerable, ICloneable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, capacity: int) -> None:
        """"""
    @overload
    def __init__(self, capacity: int, growFactor: float) -> None:
        """"""
    @overload
    def __init__(self, col: ICollection) -> None:
        """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def SyncRoot(self) -> object:
        """"""
    def Clear(self) -> None:
        """"""
    def Clone(self) -> object:
        """"""
    def Contains(self, obj: object) -> bool:
        """"""
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    def Dequeue(self) -> object:
        """"""
    def Enqueue(self, obj: object) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Peek(self) -> object:
        """"""
    @classmethod
    def Synchronized(cls, queue: Queue) -> Queue:
        """"""
    def ToArray(self) -> Array[object]:
        """"""
    def ToString(self) -> str:
        """"""
    def TrimToSize(self) -> None:
        """"""
    def __contains__(self, obj: object) -> bool:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    def __len__(self) -> int:
        """"""

class ReadOnlyCollectionBase(ABC, Object, ICollection, IEnumerable):
    """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def SyncRoot(self) -> object:
        """"""
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    def __len__(self) -> int:
        """"""

class SortedList(Object, ICollection, IDictionary, IEnumerable, ICloneable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, initialCapacity: int) -> None:
        """"""
    @overload
    def __init__(self, comparer: IComparer) -> None:
        """"""
    @overload
    def __init__(self, comparer: IComparer, capacity: int) -> None:
        """"""
    @overload
    def __init__(self, d: IDictionary) -> None:
        """"""
    @overload
    def __init__(self, d: IDictionary, comparer: IComparer) -> None:
        """"""
    @property
    def Capacity(self) -> int:
        """"""
    @Capacity.setter
    def Capacity(self, value: int) -> None: ...
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
    def GetByIndex(self, index: int) -> object:
        """"""
    def GetEnumerator(self) -> IDictionaryEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetKey(self, index: int) -> object:
        """"""
    def GetKeyList(self) -> IList:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetValueList(self) -> IList:
        """"""
    def IndexOfKey(self, key: object) -> int:
        """"""
    def IndexOfValue(self, value: object) -> int:
        """"""
    def Remove(self, key: object) -> None:
        """"""
    def RemoveAt(self, index: int) -> None:
        """"""
    def SetByIndex(self, index: int, value: object) -> None:
        """"""
    @classmethod
    def Synchronized(cls, list: SortedList) -> SortedList:
        """"""
    def ToString(self) -> str:
        """"""
    def TrimToSize(self) -> None:
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

class Stack(Object, ICollection, IEnumerable, ICloneable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, initialCapacity: int) -> None:
        """"""
    @overload
    def __init__(self, col: ICollection) -> None:
        """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def SyncRoot(self) -> object:
        """"""
    def Clear(self) -> None:
        """"""
    def Clone(self) -> object:
        """"""
    def Contains(self, obj: object) -> bool:
        """"""
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Peek(self) -> object:
        """"""
    def Pop(self) -> object:
        """"""
    def Push(self, obj: object) -> None:
        """"""
    @classmethod
    def Synchronized(cls, stack: Stack) -> Stack:
        """"""
    def ToArray(self) -> Array[object]:
        """"""
    def ToString(self) -> str:
        """"""
    def __contains__(self, obj: object) -> bool:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    def __len__(self) -> int:
        """"""

class StructuralComparer(Object, IComparer):
    """"""
    def __init__(self) -> None:
        """"""
    def Compare(self, x: object, y: object) -> int:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class StructuralComparisons(ABC, Object):
    """"""
    @classmethod
    @property
    def StructuralComparer(cls) -> IComparer:
        """"""
    @classmethod
    @property
    def StructuralEqualityComparer(cls) -> IEqualityComparer:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class StructuralEqualityComparer(Object, IEqualityComparer):
    """"""
    def __init__(self) -> None:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, x: object, y: object) -> bool:
        """"""
    @overload
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetHashCode(self, obj: object) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
