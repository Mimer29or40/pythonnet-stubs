from __future__ import annotations

from abc import ABC
from typing import ClassVar
from typing import Final
from typing import Iterator
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
    def __init__(self):
        """"""
    @overload
    def __init__(self, c: ICollection):
        """

        :param c:
        """
    @overload
    def __init__(self, capacity: int):
        """

        :param capacity:
        """
    @property
    def Capacity(self) -> int:
        """

        :return:
        """
    @Capacity.setter
    def Capacity(self, value: int) -> None: ...
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
    @classmethod
    def Adapter(cls, list: IList) -> ArrayList:
        """

        :param list:
        :return:
        """
    def Add(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    def AddRange(self, c: ICollection) -> None:
        """

        :param c:
        """
    @overload
    def BinarySearch(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def BinarySearch(self, value: object, comparer: IComparer) -> int:
        """

        :param value:
        :param comparer:
        :return:
        """
    @overload
    def BinarySearch(self, index: int, count: int, value: object, comparer: IComparer) -> int:
        """

        :param index:
        :param count:
        :param value:
        :param comparer:
        :return:
        """
    def Clear(self) -> None:
        """"""
    def Clone(self) -> object:
        """

        :return:
        """
    def Contains(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def CopyTo(self, array: Array) -> None:
        """

        :param array:
        """
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    @overload
    def CopyTo(self, index: int, array: Array, arrayIndex: int, count: int) -> None:
        """

        :param index:
        :param array:
        :param arrayIndex:
        :param count:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @classmethod
    @overload
    def FixedSize(cls, list: ArrayList) -> ArrayList:
        """

        :param list:
        :return:
        """
    @classmethod
    @overload
    def FixedSize(cls, list: IList) -> IList:
        """

        :param list:
        :return:
        """
    @overload
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    @overload
    def GetEnumerator(self, index: int, count: int) -> IEnumerator:
        """

        :param index:
        :param count:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetRange(self, index: int, count: int) -> ArrayList:
        """

        :param index:
        :param count:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def IndexOf(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def IndexOf(self, value: object, startIndex: int) -> int:
        """

        :param value:
        :param startIndex:
        :return:
        """
    @overload
    def IndexOf(self, value: object, startIndex: int, count: int) -> int:
        """

        :param value:
        :param startIndex:
        :param count:
        :return:
        """
    def Insert(self, index: int, value: object) -> None:
        """

        :param index:
        :param value:
        """
    def InsertRange(self, index: int, c: ICollection) -> None:
        """

        :param index:
        :param c:
        """
    @overload
    def LastIndexOf(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def LastIndexOf(self, value: object, startIndex: int) -> int:
        """

        :param value:
        :param startIndex:
        :return:
        """
    @overload
    def LastIndexOf(self, value: object, startIndex: int, count: int) -> int:
        """

        :param value:
        :param startIndex:
        :param count:
        :return:
        """
    @classmethod
    @overload
    def ReadOnly(cls, list: ArrayList) -> ArrayList:
        """

        :param list:
        :return:
        """
    @classmethod
    @overload
    def ReadOnly(cls, list: IList) -> IList:
        """

        :param list:
        :return:
        """
    def Remove(self, value: object) -> None:
        """

        :param value:
        """
    def RemoveAt(self, index: int) -> None:
        """

        :param index:
        """
    def RemoveRange(self, index: int, count: int) -> None:
        """

        :param index:
        :param count:
        """
    @classmethod
    def Repeat(cls, value: object, count: int) -> ArrayList:
        """

        :param value:
        :param count:
        :return:
        """
    @overload
    def Reverse(self) -> None:
        """"""
    @overload
    def Reverse(self, index: int, count: int) -> None:
        """

        :param index:
        :param count:
        """
    def SetRange(self, index: int, c: ICollection) -> None:
        """

        :param index:
        :param c:
        """
    @overload
    def Sort(self) -> None:
        """"""
    @overload
    def Sort(self, comparer: IComparer) -> None:
        """

        :param comparer:
        """
    @overload
    def Sort(self, index: int, count: int, comparer: IComparer) -> None:
        """

        :param index:
        :param count:
        :param comparer:
        """
    @classmethod
    @overload
    def Synchronized(cls, list: ArrayList) -> ArrayList:
        """

        :param list:
        :return:
        """
    @classmethod
    @overload
    def Synchronized(cls, list: IList) -> IList:
        """

        :param list:
        :return:
        """
    @overload
    def ToArray(self) -> Array[object]:
        """

        :return:
        """
    @overload
    def ToArray(self, type: Type) -> Array:
        """

        :param type:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def TrimToSize(self) -> None:
        """"""
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

class BitArray(Object, ICollection, IEnumerable, ICloneable):
    """"""

    @overload
    def __init__(self, bits: BitArray):
        """

        :param bits:
        """
    @overload
    def __init__(self, values: Array[bool]):
        """

        :param values:
        """
    @overload
    def __init__(self, bytes: Array[int]):
        """

        :param bytes:
        """
    @overload
    def __init__(self, values: Array[int]):
        """

        :param values:
        """
    @overload
    def __init__(self, length: int):
        """

        :param length:
        """
    @overload
    def __init__(self, length: int, defaultValue: bool):
        """

        :param length:
        :param defaultValue:
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
    @property
    def IsSynchronized(self) -> bool:
        """

        :return:
        """
    @property
    def Item(self) -> bool:
        """

        :return:
        """
    @Item.setter
    def Item(self, value: bool) -> None: ...
    @property
    def Length(self) -> int:
        """

        :return:
        """
    @Length.setter
    def Length(self, value: int) -> None: ...
    @property
    def SyncRoot(self) -> object:
        """

        :return:
        """
    def And(self, value: BitArray) -> BitArray:
        """

        :param value:
        :return:
        """
    def Clone(self) -> object:
        """

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
    def Get(self, index: int) -> bool:
        """

        :param index:
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
    def Not(self) -> BitArray:
        """

        :return:
        """
    def Or(self, value: BitArray) -> BitArray:
        """

        :param value:
        :return:
        """
    def Set(self, index: int, value: bool) -> None:
        """

        :param index:
        :param value:
        """
    def SetAll(self, value: bool) -> None:
        """

        :param value:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Xor(self, value: BitArray) -> BitArray:
        """

        :param value:
        :return:
        """
    def __contains__(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    def __getitem__(self, index: int) -> bool:
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
    def __setitem__(self, index: int, value: bool) -> None:
        """

        :param index:
        :param value:
        """

class CaseInsensitiveComparer(Object, IComparer):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, culture: CultureInfo):
        """

        :param culture:
        """
    @classmethod
    @property
    def Default(cls) -> CaseInsensitiveComparer:
        """

        :return:
        """
    @classmethod
    @property
    def DefaultInvariant(cls) -> CaseInsensitiveComparer:
        """

        :return:
        """
    def Compare(self, x: object, y: object) -> int:
        """

        :param x:
        :param y:
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

class CaseInsensitiveHashCodeProvider(Object, IHashCodeProvider):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, culture: CultureInfo):
        """

        :param culture:
        """
    @classmethod
    @property
    def Default(cls) -> CaseInsensitiveHashCodeProvider:
        """

        :return:
        """
    @classmethod
    @property
    def DefaultInvariant(cls) -> CaseInsensitiveHashCodeProvider:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetHashCode(self, obj: object) -> int:
        """

        :param obj:
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

class CollectionBase(ABC, Object, ICollection, IEnumerable, IList):
    """"""

    @property
    def Capacity(self) -> int:
        """

        :return:
        """
    @Capacity.setter
    def Capacity(self, value: int) -> None: ...
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

class Comparer(Object, IComparer, ISerializable):
    """"""

    Default: Final[ClassVar[Comparer]] = ...
    """
    
    :return: 
    """
    DefaultInvariant: Final[ClassVar[Comparer]] = ...
    """
    
    :return: 
    """
    def __init__(self, culture: CultureInfo):
        """

        :param culture:
        """
    def Compare(self, x: object, y: object) -> int:
        """

        :param x:
        :param y:
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
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CompatibleComparer(Object, IEqualityComparer):
    """"""

    def Compare(self, a: object, b: object) -> int:
        """

        :param a:
        :param b:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def Equals(self, x: object, y: object) -> bool:
        """

        :param x:
        :param y:
        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetHashCode(self, obj: object) -> int:
        """

        :param obj:
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

class DictionaryBase(ABC, Object, ICollection, IDictionary, IEnumerable):
    """"""

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
    def Keys(self) -> ICollection:
        """

        :return:
        """
    @property
    def SyncRoot(self) -> object:
        """

        :return:
        """
    @property
    def Values(self) -> ICollection:
        """

        :return:
        """
    def Add(self, key: object, value: object) -> None:
        """

        :param key:
        :param value:
        """
    def Clear(self) -> None:
        """"""
    def Contains(self, key: object) -> bool:
        """

        :param key:
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
    def Remove(self, key: object) -> None:
        """

        :param key:
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
    def __getitem__(self, key: object) -> object:
        """

        :param key:
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
    def __setitem__(self, key: object, value: object) -> None:
        """

        :param key:
        :param value:
        """

class DictionaryEntry(ValueType):
    """"""

    def __init__(self, key: object, value: object):
        """

        :param key:
        :param value:
        """
    @property
    def Key(self) -> object:
        """

        :return:
        """
    @Key.setter
    def Key(self, value: object) -> None: ...
    @property
    def Value(self) -> object:
        """

        :return:
        """
    @Value.setter
    def Value(self, value: object) -> None: ...
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

class EmptyReadOnlyDictionaryInternal(Object, ICollection, IDictionary, IEnumerable):
    """"""

    def __init__(self):
        """"""
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
    def Keys(self) -> ICollection:
        """

        :return:
        """
    @property
    def SyncRoot(self) -> object:
        """

        :return:
        """
    @property
    def Values(self) -> ICollection:
        """

        :return:
        """
    def Add(self, key: object, value: object) -> None:
        """

        :param key:
        :param value:
        """
    def Clear(self) -> None:
        """"""
    def Contains(self, key: object) -> bool:
        """

        :param key:
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
    def Remove(self, key: object) -> None:
        """

        :param key:
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
    def __getitem__(self, key: object) -> object:
        """

        :param key:
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
    def __setitem__(self, key: object, value: object) -> None:
        """

        :param key:
        :param value:
        """

class HashHelpers(ABC, Object):
    """"""

    HashCollisionThreshold: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    MaxPrimeArrayLength: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    primes: Final[ClassVar[Array[int]]] = ...
    """
    
    :return: 
    """
    s_UseRandomizedStringHashing: Final[ClassVar[bool]] = ...
    """
    
    :return: 
    """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @classmethod
    def ExpandPrime(cls, oldSize: int) -> int:
        """

        :param oldSize:
        :return:
        """
    @classmethod
    def GetEqualityComparerForSerialization(cls, comparer: object) -> object:
        """

        :param comparer:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @classmethod
    def GetMinPrime(cls) -> int:
        """

        :return:
        """
    @classmethod
    def GetPrime(cls, min: int) -> int:
        """

        :param min:
        :return:
        """
    @classmethod
    def GetRandomizedEqualityComparer(cls, comparer: object) -> IEqualityComparer:
        """

        :param comparer:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @classmethod
    def IsPrime(cls, candidate: int) -> bool:
        """

        :param candidate:
        :return:
        """
    @classmethod
    def IsWellKnownEqualityComparer(cls, comparer: object) -> bool:
        """

        :param comparer:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

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
    def __init__(self):
        """"""
    @overload
    def __init__(self, d: IDictionary):
        """

        :param d:
        """
    @overload
    def __init__(self, equalityComparer: IEqualityComparer):
        """

        :param equalityComparer:
        """
    @overload
    def __init__(self, capacity: int):
        """

        :param capacity:
        """
    @overload
    def __init__(self, d: IDictionary, equalityComparer: IEqualityComparer):
        """

        :param d:
        :param equalityComparer:
        """
    @overload
    def __init__(self, d: IDictionary, loadFactor: float):
        """

        :param d:
        :param loadFactor:
        """
    @overload
    def __init__(self, hcp: IHashCodeProvider, comparer: IComparer):
        """

        :param hcp:
        :param comparer:
        """
    @overload
    def __init__(self, capacity: int, equalityComparer: IEqualityComparer):
        """

        :param capacity:
        :param equalityComparer:
        """
    @overload
    def __init__(self, capacity: int, loadFactor: float):
        """

        :param capacity:
        :param loadFactor:
        """
    @overload
    def __init__(self, d: IDictionary, hcp: IHashCodeProvider, comparer: IComparer):
        """

        :param d:
        :param hcp:
        :param comparer:
        """
    @overload
    def __init__(self, d: IDictionary, loadFactor: float, equalityComparer: IEqualityComparer):
        """

        :param d:
        :param loadFactor:
        :param equalityComparer:
        """
    @overload
    def __init__(self, capacity: int, hcp: IHashCodeProvider, comparer: IComparer):
        """

        :param capacity:
        :param hcp:
        :param comparer:
        """
    @overload
    def __init__(self, capacity: int, loadFactor: float, equalityComparer: IEqualityComparer):
        """

        :param capacity:
        :param loadFactor:
        :param equalityComparer:
        """
    @overload
    def __init__(
        self, d: IDictionary, loadFactor: float, hcp: IHashCodeProvider, comparer: IComparer
    ):
        """

        :param d:
        :param loadFactor:
        :param hcp:
        :param comparer:
        """
    @overload
    def __init__(
        self, capacity: int, loadFactor: float, hcp: IHashCodeProvider, comparer: IComparer
    ):
        """

        :param capacity:
        :param loadFactor:
        :param hcp:
        :param comparer:
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
    def Keys(self) -> ICollection:
        """

        :return:
        """
    @property
    def SyncRoot(self) -> object:
        """

        :return:
        """
    @property
    def Values(self) -> ICollection:
        """

        :return:
        """
    def Add(self, key: object, value: object) -> None:
        """

        :param key:
        :param value:
        """
    def Clear(self) -> None:
        """"""
    def Clone(self) -> object:
        """

        :return:
        """
    def Contains(self, key: object) -> bool:
        """

        :param key:
        :return:
        """
    def ContainsKey(self, key: object) -> bool:
        """

        :param key:
        :return:
        """
    def ContainsValue(self, value: object) -> bool:
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
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def OnDeserialization(self, sender: object) -> None:
        """

        :param sender:
        """
    def Remove(self, key: object) -> None:
        """

        :param key:
        """
    @classmethod
    def Synchronized(cls, table: Hashtable) -> Hashtable:
        """

        :param table:
        :return:
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
    def __getitem__(self, key: object) -> object:
        """

        :param key:
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
    def __setitem__(self, key: object, value: object) -> None:
        """

        :param key:
        :param value:
        """

class ICollection(IEnumerable):
    """"""

    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def IsSynchronized(self) -> bool:
        """

        :return:
        """
    @property
    def SyncRoot(self) -> object:
        """

        :return:
        """
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    def __contains__(self, value: object) -> bool:
        """

        :param value:
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

class IComparer:
    """"""

    def Compare(self, x: object, y: object) -> int:
        """

        :param x:
        :param y:
        :return:
        """

class IDictionary(ICollection, IEnumerable):
    """"""

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
    def Keys(self) -> ICollection:
        """

        :return:
        """
    @property
    def SyncRoot(self) -> object:
        """

        :return:
        """
    @property
    def Values(self) -> ICollection:
        """

        :return:
        """
    def Add(self, key: object, value: object) -> None:
        """

        :param key:
        :param value:
        """
    def Clear(self) -> None:
        """"""
    def Contains(self, key: object) -> bool:
        """

        :param key:
        :return:
        """
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    def Remove(self, key: object) -> None:
        """

        :param key:
        """
    def __contains__(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    def __getitem__(self, key: object) -> object:
        """

        :param key:
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
    def __setitem__(self, key: object, value: object) -> None:
        """

        :param key:
        :param value:
        """

class IDictionaryEnumerator(IEnumerator):
    """"""

    @property
    def Current(self) -> object:
        """

        :return:
        """
    @property
    def Entry(self) -> DictionaryEntry:
        """

        :return:
        """
    @property
    def Key(self) -> object:
        """

        :return:
        """
    @property
    def Value(self) -> object:
        """

        :return:
        """
    def MoveNext(self) -> bool:
        """

        :return:
        """
    def Reset(self) -> None:
        """"""

class IEnumerable:
    """"""

    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """

class IEnumerator:
    """"""

    @property
    def Current(self) -> object:
        """

        :return:
        """
    def MoveNext(self) -> bool:
        """

        :return:
        """
    def Reset(self) -> None:
        """"""

class IEqualityComparer:
    """"""

    def Equals(self, x: object, y: object) -> bool:
        """

        :param x:
        :param y:
        :return:
        """
    def GetHashCode(self, obj: object) -> int:
        """

        :param obj:
        :return:
        """

class IHashCodeProvider:
    """"""

    def GetHashCode(self, obj: object) -> int:
        """

        :param obj:
        :return:
        """

class IList(ICollection, IEnumerable):
    """"""

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
    def GetEnumerator(self) -> IEnumerator:
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

class IStructuralComparable:
    """"""

    def CompareTo(self, other: object, comparer: IComparer) -> int:
        """

        :param other:
        :param comparer:
        :return:
        """

class IStructuralEquatable:
    """"""

    def Equals(self, other: object, comparer: IEqualityComparer) -> bool:
        """

        :param other:
        :param comparer:
        :return:
        """
    def GetHashCode(self, comparer: IEqualityComparer) -> int:
        """

        :param comparer:
        :return:
        """

class KeyValuePairs(Object):
    """"""

    def __init__(self, key: object, value: object):
        """

        :param key:
        :param value:
        """
    @property
    def Key(self) -> object:
        """

        :return:
        """
    @property
    def Value(self) -> object:
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

class ListDictionaryInternal(Object, ICollection, IDictionary, IEnumerable):
    """"""

    def __init__(self):
        """"""
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
    def Keys(self) -> ICollection:
        """

        :return:
        """
    @property
    def SyncRoot(self) -> object:
        """

        :return:
        """
    @property
    def Values(self) -> ICollection:
        """

        :return:
        """
    def Add(self, key: object, value: object) -> None:
        """

        :param key:
        :param value:
        """
    def Clear(self) -> None:
        """"""
    def Contains(self, key: object) -> bool:
        """

        :param key:
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
    def Remove(self, key: object) -> None:
        """

        :param key:
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
    def __getitem__(self, key: object) -> object:
        """

        :param key:
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
    def __setitem__(self, key: object, value: object) -> None:
        """

        :param key:
        :param value:
        """

class Queue(Object, ICollection, IEnumerable, ICloneable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, col: ICollection):
        """

        :param col:
        """
    @overload
    def __init__(self, capacity: int):
        """

        :param capacity:
        """
    @overload
    def __init__(self, capacity: int, growFactor: float):
        """

        :param capacity:
        :param growFactor:
        """
    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def IsSynchronized(self) -> bool:
        """

        :return:
        """
    @property
    def SyncRoot(self) -> object:
        """

        :return:
        """
    def Clear(self) -> None:
        """"""
    def Clone(self) -> object:
        """

        :return:
        """
    def Contains(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    def Dequeue(self) -> object:
        """

        :return:
        """
    def Enqueue(self, obj: object) -> None:
        """

        :param obj:
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
    def Peek(self) -> object:
        """

        :return:
        """
    @classmethod
    def Synchronized(cls, queue: Queue) -> Queue:
        """

        :param queue:
        :return:
        """
    def ToArray(self) -> Array[object]:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def TrimToSize(self) -> None:
        """"""
    def __contains__(self, value: object) -> bool:
        """

        :param value:
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

class ReadOnlyCollectionBase(ABC, Object, ICollection, IEnumerable):
    """"""

    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def IsSynchronized(self) -> bool:
        """

        :return:
        """
    @property
    def SyncRoot(self) -> object:
        """

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
    def __contains__(self, value: object) -> bool:
        """

        :param value:
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

class SortedList(Object, ICollection, IDictionary, IEnumerable, ICloneable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, comparer: IComparer):
        """

        :param comparer:
        """
    @overload
    def __init__(self, d: IDictionary):
        """

        :param d:
        """
    @overload
    def __init__(self, initialCapacity: int):
        """

        :param initialCapacity:
        """
    @overload
    def __init__(self, comparer: IComparer, capacity: int):
        """

        :param comparer:
        :param capacity:
        """
    @overload
    def __init__(self, d: IDictionary, comparer: IComparer):
        """

        :param d:
        :param comparer:
        """
    @property
    def Capacity(self) -> int:
        """

        :return:
        """
    @Capacity.setter
    def Capacity(self, value: int) -> None: ...
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
    def Keys(self) -> ICollection:
        """

        :return:
        """
    @property
    def SyncRoot(self) -> object:
        """

        :return:
        """
    @property
    def Values(self) -> ICollection:
        """

        :return:
        """
    def Add(self, key: object, value: object) -> None:
        """

        :param key:
        :param value:
        """
    def Clear(self) -> None:
        """"""
    def Clone(self) -> object:
        """

        :return:
        """
    def Contains(self, key: object) -> bool:
        """

        :param key:
        :return:
        """
    def ContainsKey(self, key: object) -> bool:
        """

        :param key:
        :return:
        """
    def ContainsValue(self, value: object) -> bool:
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
    def GetByIndex(self, index: int) -> object:
        """

        :param index:
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
    def GetKey(self, index: int) -> object:
        """

        :param index:
        :return:
        """
    def GetKeyList(self) -> IList:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetValueList(self) -> IList:
        """

        :return:
        """
    def IndexOfKey(self, key: object) -> int:
        """

        :param key:
        :return:
        """
    def IndexOfValue(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    def Remove(self, key: object) -> None:
        """

        :param key:
        """
    def RemoveAt(self, index: int) -> None:
        """

        :param index:
        """
    def SetByIndex(self, index: int, value: object) -> None:
        """

        :param index:
        :param value:
        """
    @classmethod
    def Synchronized(cls, list: SortedList) -> SortedList:
        """

        :param list:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def TrimToSize(self) -> None:
        """"""
    def __contains__(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    def __getitem__(self, key: object) -> object:
        """

        :param key:
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
    def __setitem__(self, key: object, value: object) -> None:
        """

        :param key:
        :param value:
        """

class Stack(Object, ICollection, IEnumerable, ICloneable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, col: ICollection):
        """

        :param col:
        """
    @overload
    def __init__(self, initialCapacity: int):
        """

        :param initialCapacity:
        """
    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def IsSynchronized(self) -> bool:
        """

        :return:
        """
    @property
    def SyncRoot(self) -> object:
        """

        :return:
        """
    def Clear(self) -> None:
        """"""
    def Clone(self) -> object:
        """

        :return:
        """
    def Contains(self, obj: object) -> bool:
        """

        :param obj:
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
    def Peek(self) -> object:
        """

        :return:
        """
    def Pop(self) -> object:
        """

        :return:
        """
    def Push(self, obj: object) -> None:
        """

        :param obj:
        """
    @classmethod
    def Synchronized(cls, stack: Stack) -> Stack:
        """

        :param stack:
        :return:
        """
    def ToArray(self) -> Array[object]:
        """

        :return:
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
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    def __len__(self) -> int:
        """

        :return:
        """

class StructuralComparer(Object, IComparer):
    """"""

    def __init__(self):
        """"""
    def Compare(self, x: object, y: object) -> int:
        """

        :param x:
        :param y:
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

class StructuralComparisons(ABC, Object):
    """"""

    @classmethod
    @property
    def StructuralComparer(cls) -> IComparer:
        """

        :return:
        """
    @classmethod
    @property
    def StructuralEqualityComparer(cls) -> IEqualityComparer:
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

class StructuralEqualityComparer(Object, IEqualityComparer):
    """"""

    def __init__(self):
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def Equals(self, x: object, y: object) -> bool:
        """

        :param x:
        :param y:
        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetHashCode(self, obj: object) -> int:
        """

        :param obj:
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
