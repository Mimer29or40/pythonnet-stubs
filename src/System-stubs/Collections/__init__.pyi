from __future__ import annotations

from abc import ABC
from typing import List, Protocol, Union, overload

from System import Array, Boolean, Byte, ICloneable, Int32, Object, Single, Type, ValueType, Void
from System.Globalization import CultureInfo
from System.Runtime.Serialization import IDeserializationCallback, ISerializable, SerializationInfo, StreamingContext

# ---------- Types ---------- #

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
ByteType = Union[int, Byte]
FloatType = Union[float, Single]
IntType = Union[int, Int32]
ObjectType = Object
TypeType = Union[type, Type]
VoidType = Union[None, Void]


# ---------- Classes ---------- #

class ArrayList(ObjectType, IList, ICollection, IEnumerable, ICloneable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, capacity: IntType): ...
    
    @overload
    def __init__(self, c: ICollection): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Capacity(self) -> IntType: ...
    
    @Capacity.setter
    def Capacity(self, value: IntType) -> None: ...
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def IsFixedSize(self) -> BooleanType: ...
    
    @property
    def IsReadOnly(self) -> BooleanType: ...
    
    @property
    def IsSynchronized(self) -> BooleanType: ...
    
    def __getitem__(self, key: IntType) -> ObjectType: ...
    
    def __setitem__(self, key: IntType, value: ObjectType) -> None: ...
    
    @property
    def SyncRoot(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def Adapter(list: IList) -> ArrayList: ...
    
    def Add(self, value: ObjectType) -> IntType: ...
    
    def AddRange(self, c: ICollection) -> VoidType: ...
    
    @overload
    def BinarySearch(self, index: IntType, count: IntType, value: ObjectType, comparer: IComparer) -> IntType: ...
    
    @overload
    def BinarySearch(self, value: ObjectType) -> IntType: ...
    
    @overload
    def BinarySearch(self, value: ObjectType, comparer: IComparer) -> IntType: ...
    
    def Clear(self) -> VoidType: ...
    
    def Clone(self) -> ObjectType: ...
    
    def Contains(self, item: ObjectType) -> BooleanType: ...
    
    @overload
    def CopyTo(self, array: Array) -> VoidType: ...
    
    @overload
    def CopyTo(self, array: Array, arrayIndex: IntType) -> VoidType: ...
    
    @overload
    def CopyTo(self, index: IntType, array: Array, arrayIndex: IntType, count: IntType) -> VoidType: ...
    
    @staticmethod
    @overload
    def FixedSize(list: IList) -> IList: ...
    
    @staticmethod
    @overload
    def FixedSize(list: ArrayList) -> ArrayList: ...
    
    @overload
    def GetEnumerator(self) -> IEnumerator: ...
    
    @overload
    def GetEnumerator(self, index: IntType, count: IntType) -> IEnumerator: ...
    
    def GetRange(self, index: IntType, count: IntType) -> ArrayList: ...
    
    @overload
    def IndexOf(self, value: ObjectType) -> IntType: ...
    
    @overload
    def IndexOf(self, value: ObjectType, startIndex: IntType) -> IntType: ...
    
    @overload
    def IndexOf(self, value: ObjectType, startIndex: IntType, count: IntType) -> IntType: ...
    
    def Insert(self, index: IntType, value: ObjectType) -> VoidType: ...
    
    def InsertRange(self, index: IntType, c: ICollection) -> VoidType: ...
    
    @overload
    def LastIndexOf(self, value: ObjectType) -> IntType: ...
    
    @overload
    def LastIndexOf(self, value: ObjectType, startIndex: IntType) -> IntType: ...
    
    @overload
    def LastIndexOf(self, value: ObjectType, startIndex: IntType, count: IntType) -> IntType: ...
    
    @staticmethod
    @overload
    def ReadOnly(list: IList) -> IList: ...
    
    @staticmethod
    @overload
    def ReadOnly(list: ArrayList) -> ArrayList: ...
    
    def Remove(self, obj: ObjectType) -> VoidType: ...
    
    def RemoveAt(self, index: IntType) -> VoidType: ...
    
    def RemoveRange(self, index: IntType, count: IntType) -> VoidType: ...
    
    @staticmethod
    def Repeat(value: ObjectType, count: IntType) -> ArrayList: ...
    
    @overload
    def Reverse(self) -> VoidType: ...
    
    @overload
    def Reverse(self, index: IntType, count: IntType) -> VoidType: ...
    
    def SetRange(self, index: IntType, c: ICollection) -> VoidType: ...
    
    @overload
    def Sort(self) -> VoidType: ...
    
    @overload
    def Sort(self, comparer: IComparer) -> VoidType: ...
    
    @overload
    def Sort(self, index: IntType, count: IntType, comparer: IComparer) -> VoidType: ...
    
    @staticmethod
    @overload
    def Synchronized(list: IList) -> IList: ...
    
    @staticmethod
    @overload
    def Synchronized(list: ArrayList) -> ArrayList: ...
    
    @overload
    def ToArray(self) -> ArrayType[ObjectType]: ...
    
    @overload
    def ToArray(self, type: TypeType) -> Array: ...
    
    def TrimToSize(self) -> VoidType: ...
    
    def get_Capacity(self) -> IntType: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_IsFixedSize(self) -> BooleanType: ...
    
    def get_IsReadOnly(self) -> BooleanType: ...
    
    def get_IsSynchronized(self) -> BooleanType: ...
    
    def get_Item(self, index: IntType) -> ObjectType: ...
    
    def get_SyncRoot(self) -> ObjectType: ...
    
    def set_Capacity(self, value: IntType) -> VoidType: ...
    
    def set_Item(self, index: IntType, value: ObjectType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class BitArray(ObjectType, ICollection, IEnumerable, ICloneable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, length: IntType): ...
    
    @overload
    def __init__(self, length: IntType, defaultValue: BooleanType): ...
    
    @overload
    def __init__(self, bytes: ArrayType[ByteType]): ...
    
    @overload
    def __init__(self, values: ArrayType[BooleanType]): ...
    
    @overload
    def __init__(self, values: ArrayType[IntType]): ...
    
    @overload
    def __init__(self, bits: BitArray): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def IsReadOnly(self) -> BooleanType: ...
    
    @property
    def IsSynchronized(self) -> BooleanType: ...
    
    def __getitem__(self, key: IntType) -> BooleanType: ...
    
    def __setitem__(self, key: IntType, value: BooleanType) -> None: ...
    
    @property
    def Length(self) -> IntType: ...
    
    @Length.setter
    def Length(self, value: IntType) -> None: ...
    
    @property
    def SyncRoot(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def And(self, value: BitArray) -> BitArray: ...
    
    def Clone(self) -> ObjectType: ...
    
    def CopyTo(self, array: Array, index: IntType) -> VoidType: ...
    
    def Get(self, index: IntType) -> BooleanType: ...
    
    def GetEnumerator(self) -> IEnumerator: ...
    
    def Not(self) -> BitArray: ...
    
    def Or(self, value: BitArray) -> BitArray: ...
    
    def Set(self, index: IntType, value: BooleanType) -> VoidType: ...
    
    def SetAll(self, value: BooleanType) -> VoidType: ...
    
    def Xor(self, value: BitArray) -> BitArray: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_IsReadOnly(self) -> BooleanType: ...
    
    def get_IsSynchronized(self) -> BooleanType: ...
    
    def get_Item(self, index: IntType) -> BooleanType: ...
    
    def get_Length(self) -> IntType: ...
    
    def get_SyncRoot(self) -> ObjectType: ...
    
    def set_Item(self, index: IntType, value: BooleanType) -> VoidType: ...
    
    def set_Length(self, value: IntType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CaseInsensitiveComparer(ObjectType, IComparer):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, culture: CultureInfo): ...
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def Default() -> CaseInsensitiveComparer: ...
    
    @staticmethod
    @property
    def DefaultInvariant() -> CaseInsensitiveComparer: ...
    
    # ---------- Methods ---------- #
    
    def Compare(self, a: ObjectType, b: ObjectType) -> IntType: ...
    
    @staticmethod
    def get_Default() -> CaseInsensitiveComparer: ...
    
    @staticmethod
    def get_DefaultInvariant() -> CaseInsensitiveComparer: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CaseInsensitiveHashCodeProvider(ObjectType, IHashCodeProvider):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, culture: CultureInfo): ...
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def Default() -> CaseInsensitiveHashCodeProvider: ...
    
    @staticmethod
    @property
    def DefaultInvariant() -> CaseInsensitiveHashCodeProvider: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def GetHashCode(self, obj: ObjectType) -> IntType: ...
    
    @staticmethod
    def get_Default() -> CaseInsensitiveHashCodeProvider: ...
    
    @staticmethod
    def get_DefaultInvariant() -> CaseInsensitiveHashCodeProvider: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CollectionBase(ABC, ObjectType, IList, ICollection, IEnumerable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Capacity(self) -> IntType: ...
    
    @Capacity.setter
    def Capacity(self, value: IntType) -> None: ...
    
    @property
    def Count(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def Clear(self) -> VoidType: ...
    
    def GetEnumerator(self) -> IEnumerator: ...
    
    def RemoveAt(self, index: IntType) -> VoidType: ...
    
    def get_Capacity(self) -> IntType: ...
    
    def get_Count(self) -> IntType: ...
    
    def set_Capacity(self, value: IntType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Comparer(ObjectType, IComparer, ISerializable):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Default() -> Comparer: ...
    
    @staticmethod
    @property
    def DefaultInvariant() -> Comparer: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self, culture: CultureInfo): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Compare(self, a: ObjectType, b: ObjectType) -> IntType: ...
    
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CompatibleComparer(ObjectType, IEqualityComparer):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Compare(self, a: ObjectType, b: ObjectType) -> IntType: ...
    
    @overload
    def Equals(self, a: ObjectType, b: ObjectType) -> BooleanType: ...
    
    @overload
    def GetHashCode(self, obj: ObjectType) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DictionaryBase(ABC, ObjectType, IDictionary, ICollection, IEnumerable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def Clear(self) -> VoidType: ...
    
    def CopyTo(self, array: Array, index: IntType) -> VoidType: ...
    
    def GetEnumerator(self) -> IDictionaryEnumerator: ...
    
    def get_Count(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EmptyReadOnlyDictionaryInternal(ObjectType, IDictionary, ICollection, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def IsFixedSize(self) -> BooleanType: ...
    
    @property
    def IsReadOnly(self) -> BooleanType: ...
    
    @property
    def IsSynchronized(self) -> BooleanType: ...
    
    def __getitem__(self, key: ObjectType) -> ObjectType: ...
    
    def __setitem__(self, key: ObjectType, value: ObjectType) -> None: ...
    
    @property
    def Keys(self) -> ICollection: ...
    
    @property
    def SyncRoot(self) -> ObjectType: ...
    
    @property
    def Values(self) -> ICollection: ...
    
    # ---------- Methods ---------- #
    
    def Add(self, key: ObjectType, value: ObjectType) -> VoidType: ...
    
    def Clear(self) -> VoidType: ...
    
    def Contains(self, key: ObjectType) -> BooleanType: ...
    
    def CopyTo(self, array: Array, index: IntType) -> VoidType: ...
    
    def GetEnumerator(self) -> IDictionaryEnumerator: ...
    
    def Remove(self, key: ObjectType) -> VoidType: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_IsFixedSize(self) -> BooleanType: ...
    
    def get_IsReadOnly(self) -> BooleanType: ...
    
    def get_IsSynchronized(self) -> BooleanType: ...
    
    def get_Item(self, key: ObjectType) -> ObjectType: ...
    
    def get_Keys(self) -> ICollection: ...
    
    def get_SyncRoot(self) -> ObjectType: ...
    
    def get_Values(self) -> ICollection: ...
    
    def set_Item(self, key: ObjectType, value: ObjectType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class HashHelpers(ABC, ObjectType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def HashCollisionThreshold() -> IntType: ...
    
    @staticmethod
    @property
    def MaxPrimeArrayLength() -> IntType: ...
    
    @staticmethod
    @property
    def primes() -> ArrayType[IntType]: ...
    
    @staticmethod
    @property
    def s_UseRandomizedStringHashing() -> BooleanType: ...
    
    @staticmethod
    @s_UseRandomizedStringHashing.setter
    def s_UseRandomizedStringHashing(value: BooleanType) -> None: ...
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def ExpandPrime(oldSize: IntType) -> IntType: ...
    
    @staticmethod
    def GetEqualityComparerForSerialization(comparer: ObjectType) -> ObjectType: ...
    
    @staticmethod
    def GetMinPrime() -> IntType: ...
    
    @staticmethod
    def GetPrime(min: IntType) -> IntType: ...
    
    @staticmethod
    def GetRandomizedEqualityComparer(comparer: ObjectType) -> IEqualityComparer: ...
    
    @staticmethod
    def IsPrime(candidate: IntType) -> BooleanType: ...
    
    @staticmethod
    def IsWellKnownEqualityComparer(comparer: ObjectType) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Hashtable(ObjectType, IDictionary, ICollection, IEnumerable, ISerializable, IDeserializationCallback, ICloneable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, capacity: IntType): ...
    
    @overload
    def __init__(self, capacity: IntType, loadFactor: FloatType): ...
    
    @overload
    def __init__(self, capacity: IntType, loadFactor: FloatType, hcp: IHashCodeProvider, comparer: IComparer): ...
    
    @overload
    def __init__(self, capacity: IntType, loadFactor: FloatType, equalityComparer: IEqualityComparer): ...
    
    @overload
    def __init__(self, hcp: IHashCodeProvider, comparer: IComparer): ...
    
    @overload
    def __init__(self, equalityComparer: IEqualityComparer): ...
    
    @overload
    def __init__(self, capacity: IntType, hcp: IHashCodeProvider, comparer: IComparer): ...
    
    @overload
    def __init__(self, capacity: IntType, equalityComparer: IEqualityComparer): ...
    
    @overload
    def __init__(self, d: IDictionary): ...
    
    @overload
    def __init__(self, d: IDictionary, loadFactor: FloatType): ...
    
    @overload
    def __init__(self, d: IDictionary, hcp: IHashCodeProvider, comparer: IComparer): ...
    
    @overload
    def __init__(self, d: IDictionary, equalityComparer: IEqualityComparer): ...
    
    @overload
    def __init__(self, d: IDictionary, loadFactor: FloatType, hcp: IHashCodeProvider, comparer: IComparer): ...
    
    @overload
    def __init__(self, d: IDictionary, loadFactor: FloatType, equalityComparer: IEqualityComparer): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def IsFixedSize(self) -> BooleanType: ...
    
    @property
    def IsReadOnly(self) -> BooleanType: ...
    
    @property
    def IsSynchronized(self) -> BooleanType: ...
    
    def __getitem__(self, key: ObjectType) -> ObjectType: ...
    
    def __setitem__(self, key: ObjectType, value: ObjectType) -> None: ...
    
    @property
    def Keys(self) -> ICollection: ...
    
    @property
    def SyncRoot(self) -> ObjectType: ...
    
    @property
    def Values(self) -> ICollection: ...
    
    # ---------- Methods ---------- #
    
    def Add(self, key: ObjectType, value: ObjectType) -> VoidType: ...
    
    def Clear(self) -> VoidType: ...
    
    def Clone(self) -> ObjectType: ...
    
    def Contains(self, key: ObjectType) -> BooleanType: ...
    
    def ContainsKey(self, key: ObjectType) -> BooleanType: ...
    
    def ContainsValue(self, value: ObjectType) -> BooleanType: ...
    
    def CopyTo(self, array: Array, arrayIndex: IntType) -> VoidType: ...
    
    def GetEnumerator(self) -> IDictionaryEnumerator: ...
    
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    
    def OnDeserialization(self, sender: ObjectType) -> VoidType: ...
    
    def Remove(self, key: ObjectType) -> VoidType: ...
    
    @staticmethod
    def Synchronized(table: Hashtable) -> Hashtable: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_IsFixedSize(self) -> BooleanType: ...
    
    def get_IsReadOnly(self) -> BooleanType: ...
    
    def get_IsSynchronized(self) -> BooleanType: ...
    
    def get_Item(self, key: ObjectType) -> ObjectType: ...
    
    def get_Keys(self) -> ICollection: ...
    
    def get_SyncRoot(self) -> ObjectType: ...
    
    def get_Values(self) -> ICollection: ...
    
    def set_Item(self, key: ObjectType, value: ObjectType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class KeyValuePairs(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, key: ObjectType, value: ObjectType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Key(self) -> ObjectType: ...
    
    @property
    def Value(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def get_Key(self) -> ObjectType: ...
    
    def get_Value(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ListDictionaryInternal(ObjectType, IDictionary, ICollection, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def IsFixedSize(self) -> BooleanType: ...
    
    @property
    def IsReadOnly(self) -> BooleanType: ...
    
    @property
    def IsSynchronized(self) -> BooleanType: ...
    
    def __getitem__(self, key: ObjectType) -> ObjectType: ...
    
    def __setitem__(self, key: ObjectType, value: ObjectType) -> None: ...
    
    @property
    def Keys(self) -> ICollection: ...
    
    @property
    def SyncRoot(self) -> ObjectType: ...
    
    @property
    def Values(self) -> ICollection: ...
    
    # ---------- Methods ---------- #
    
    def Add(self, key: ObjectType, value: ObjectType) -> VoidType: ...
    
    def Clear(self) -> VoidType: ...
    
    def Contains(self, key: ObjectType) -> BooleanType: ...
    
    def CopyTo(self, array: Array, index: IntType) -> VoidType: ...
    
    def GetEnumerator(self) -> IDictionaryEnumerator: ...
    
    def Remove(self, key: ObjectType) -> VoidType: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_IsFixedSize(self) -> BooleanType: ...
    
    def get_IsReadOnly(self) -> BooleanType: ...
    
    def get_IsSynchronized(self) -> BooleanType: ...
    
    def get_Item(self, key: ObjectType) -> ObjectType: ...
    
    def get_Keys(self) -> ICollection: ...
    
    def get_SyncRoot(self) -> ObjectType: ...
    
    def get_Values(self) -> ICollection: ...
    
    def set_Item(self, key: ObjectType, value: ObjectType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Queue(ObjectType, ICollection, IEnumerable, ICloneable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, capacity: IntType): ...
    
    @overload
    def __init__(self, capacity: IntType, growFactor: FloatType): ...
    
    @overload
    def __init__(self, col: ICollection): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def IsSynchronized(self) -> BooleanType: ...
    
    @property
    def SyncRoot(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def Clear(self) -> VoidType: ...
    
    def Clone(self) -> ObjectType: ...
    
    def Contains(self, obj: ObjectType) -> BooleanType: ...
    
    def CopyTo(self, array: Array, index: IntType) -> VoidType: ...
    
    def Dequeue(self) -> ObjectType: ...
    
    def Enqueue(self, obj: ObjectType) -> VoidType: ...
    
    def GetEnumerator(self) -> IEnumerator: ...
    
    def Peek(self) -> ObjectType: ...
    
    @staticmethod
    def Synchronized(queue: Queue) -> Queue: ...
    
    def ToArray(self) -> ArrayType[ObjectType]: ...
    
    def TrimToSize(self) -> VoidType: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_IsSynchronized(self) -> BooleanType: ...
    
    def get_SyncRoot(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ReadOnlyCollectionBase(ABC, ObjectType, ICollection, IEnumerable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def GetEnumerator(self) -> IEnumerator: ...
    
    def get_Count(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SortedList(ObjectType, IDictionary, ICollection, IEnumerable, ICloneable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, initialCapacity: IntType): ...
    
    @overload
    def __init__(self, comparer: IComparer): ...
    
    @overload
    def __init__(self, comparer: IComparer, capacity: IntType): ...
    
    @overload
    def __init__(self, d: IDictionary): ...
    
    @overload
    def __init__(self, d: IDictionary, comparer: IComparer): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Capacity(self) -> IntType: ...
    
    @Capacity.setter
    def Capacity(self, value: IntType) -> None: ...
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def IsFixedSize(self) -> BooleanType: ...
    
    @property
    def IsReadOnly(self) -> BooleanType: ...
    
    @property
    def IsSynchronized(self) -> BooleanType: ...
    
    def __getitem__(self, key: ObjectType) -> ObjectType: ...
    
    def __setitem__(self, key: ObjectType, value: ObjectType) -> None: ...
    
    @property
    def Keys(self) -> ICollection: ...
    
    @property
    def SyncRoot(self) -> ObjectType: ...
    
    @property
    def Values(self) -> ICollection: ...
    
    # ---------- Methods ---------- #
    
    def Add(self, key: ObjectType, value: ObjectType) -> VoidType: ...
    
    def Clear(self) -> VoidType: ...
    
    def Clone(self) -> ObjectType: ...
    
    def Contains(self, key: ObjectType) -> BooleanType: ...
    
    def ContainsKey(self, key: ObjectType) -> BooleanType: ...
    
    def ContainsValue(self, value: ObjectType) -> BooleanType: ...
    
    def CopyTo(self, array: Array, arrayIndex: IntType) -> VoidType: ...
    
    def GetByIndex(self, index: IntType) -> ObjectType: ...
    
    def GetEnumerator(self) -> IDictionaryEnumerator: ...
    
    def GetKey(self, index: IntType) -> ObjectType: ...
    
    def GetKeyList(self) -> IList: ...
    
    def GetValueList(self) -> IList: ...
    
    def IndexOfKey(self, key: ObjectType) -> IntType: ...
    
    def IndexOfValue(self, value: ObjectType) -> IntType: ...
    
    def Remove(self, key: ObjectType) -> VoidType: ...
    
    def RemoveAt(self, index: IntType) -> VoidType: ...
    
    def SetByIndex(self, index: IntType, value: ObjectType) -> VoidType: ...
    
    @staticmethod
    def Synchronized(list: SortedList) -> SortedList: ...
    
    def TrimToSize(self) -> VoidType: ...
    
    def get_Capacity(self) -> IntType: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_IsFixedSize(self) -> BooleanType: ...
    
    def get_IsReadOnly(self) -> BooleanType: ...
    
    def get_IsSynchronized(self) -> BooleanType: ...
    
    def get_Item(self, key: ObjectType) -> ObjectType: ...
    
    def get_Keys(self) -> ICollection: ...
    
    def get_SyncRoot(self) -> ObjectType: ...
    
    def get_Values(self) -> ICollection: ...
    
    def set_Capacity(self, value: IntType) -> VoidType: ...
    
    def set_Item(self, key: ObjectType, value: ObjectType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Stack(ObjectType, ICollection, IEnumerable, ICloneable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, initialCapacity: IntType): ...
    
    @overload
    def __init__(self, col: ICollection): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def IsSynchronized(self) -> BooleanType: ...
    
    @property
    def SyncRoot(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def Clear(self) -> VoidType: ...
    
    def Clone(self) -> ObjectType: ...
    
    def Contains(self, obj: ObjectType) -> BooleanType: ...
    
    def CopyTo(self, array: Array, index: IntType) -> VoidType: ...
    
    def GetEnumerator(self) -> IEnumerator: ...
    
    def Peek(self) -> ObjectType: ...
    
    def Pop(self) -> ObjectType: ...
    
    def Push(self, obj: ObjectType) -> VoidType: ...
    
    @staticmethod
    def Synchronized(stack: Stack) -> Stack: ...
    
    def ToArray(self) -> ArrayType[ObjectType]: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_IsSynchronized(self) -> BooleanType: ...
    
    def get_SyncRoot(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class StructuralComparer(ObjectType, IComparer):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Compare(self, x: ObjectType, y: ObjectType) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class StructuralComparisons(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def StructuralComparer() -> IComparer: ...
    
    @staticmethod
    @property
    def StructuralEqualityComparer() -> IEqualityComparer: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def get_StructuralComparer() -> IComparer: ...
    
    @staticmethod
    def get_StructuralEqualityComparer() -> IEqualityComparer: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class StructuralEqualityComparer(ObjectType, IEqualityComparer):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def Equals(self, x: ObjectType, y: ObjectType) -> BooleanType: ...
    
    @overload
    def GetHashCode(self, obj: ObjectType) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# ---------- Structs ---------- #

class DictionaryEntry(ValueType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, key: ObjectType, value: ObjectType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Key(self) -> ObjectType: ...
    
    @Key.setter
    def Key(self, value: ObjectType) -> None: ...
    
    @property
    def Value(self) -> ObjectType: ...
    
    @Value.setter
    def Value(self, value: ObjectType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Key(self) -> ObjectType: ...
    
    def get_Value(self) -> ObjectType: ...
    
    def set_Key(self, value: ObjectType) -> VoidType: ...
    
    def set_Value(self, value: ObjectType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# ---------- Interfaces ---------- #

class ICollection(Protocol, IEnumerable):
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def IsSynchronized(self) -> BooleanType: ...
    
    @property
    def SyncRoot(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def CopyTo(self, array: Array, index: IntType) -> VoidType: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_IsSynchronized(self) -> BooleanType: ...
    
    def get_SyncRoot(self) -> ObjectType: ...
    
    # No Events


class IComparer(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Compare(self, x: ObjectType, y: ObjectType) -> IntType: ...
    
    # No Events


class IDictionary(Protocol, ICollection, IEnumerable):
    # ---------- Properties ---------- #
    
    @property
    def IsFixedSize(self) -> BooleanType: ...
    
    @property
    def IsReadOnly(self) -> BooleanType: ...
    
    def __getitem__(self, key: ObjectType) -> ObjectType: ...
    
    def __setitem__(self, key: ObjectType, value: ObjectType) -> None: ...
    
    @property
    def Keys(self) -> ICollection: ...
    
    @property
    def Values(self) -> ICollection: ...
    
    # ---------- Methods ---------- #
    
    def Add(self, key: ObjectType, value: ObjectType) -> VoidType: ...
    
    def Clear(self) -> VoidType: ...
    
    def Contains(self, key: ObjectType) -> BooleanType: ...
    
    def GetEnumerator(self) -> IDictionaryEnumerator: ...
    
    def Remove(self, key: ObjectType) -> VoidType: ...
    
    def get_IsFixedSize(self) -> BooleanType: ...
    
    def get_IsReadOnly(self) -> BooleanType: ...
    
    def get_Item(self, key: ObjectType) -> ObjectType: ...
    
    def get_Keys(self) -> ICollection: ...
    
    def get_Values(self) -> ICollection: ...
    
    def set_Item(self, key: ObjectType, value: ObjectType) -> VoidType: ...
    
    # No Events


class IDictionaryEnumerator(Protocol, IEnumerator):
    # ---------- Properties ---------- #
    
    @property
    def Entry(self) -> DictionaryEntry: ...
    
    @property
    def Key(self) -> ObjectType: ...
    
    @property
    def Value(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def get_Entry(self) -> DictionaryEntry: ...
    
    def get_Key(self) -> ObjectType: ...
    
    def get_Value(self) -> ObjectType: ...
    
    # No Events


class IEnumerable(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetEnumerator(self) -> IEnumerator: ...
    
    # No Events


class IEnumerator(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def Current(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def MoveNext(self) -> BooleanType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Current(self) -> ObjectType: ...
    
    # No Events


class IEqualityComparer(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Equals(self, x: ObjectType, y: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self, obj: ObjectType) -> IntType: ...
    
    # No Events


class IHashCodeProvider(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetHashCode(self, obj: ObjectType) -> IntType: ...
    
    # No Events


class IList(Protocol, ICollection, IEnumerable):
    # ---------- Properties ---------- #
    
    @property
    def IsFixedSize(self) -> BooleanType: ...
    
    @property
    def IsReadOnly(self) -> BooleanType: ...
    
    def __getitem__(self, key: IntType) -> ObjectType: ...
    
    def __setitem__(self, key: IntType, value: ObjectType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Add(self, value: ObjectType) -> IntType: ...
    
    def Clear(self) -> VoidType: ...
    
    def Contains(self, value: ObjectType) -> BooleanType: ...
    
    def IndexOf(self, value: ObjectType) -> IntType: ...
    
    def Insert(self, index: IntType, value: ObjectType) -> VoidType: ...
    
    def Remove(self, value: ObjectType) -> VoidType: ...
    
    def RemoveAt(self, index: IntType) -> VoidType: ...
    
    def get_IsFixedSize(self) -> BooleanType: ...
    
    def get_IsReadOnly(self) -> BooleanType: ...
    
    def get_Item(self, index: IntType) -> ObjectType: ...
    
    def set_Item(self, index: IntType, value: ObjectType) -> VoidType: ...
    
    # No Events


class IStructuralComparable(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def CompareTo(self, other: ObjectType, comparer: IComparer) -> IntType: ...
    
    # No Events


class IStructuralEquatable(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Equals(self, other: ObjectType, comparer: IEqualityComparer) -> BooleanType: ...
    
    def GetHashCode(self, comparer: IEqualityComparer) -> IntType: ...
    
    # No Events


# No Enums

# No Delegates

__all__ = [
    ArrayList,
    BitArray,
    CaseInsensitiveComparer,
    CaseInsensitiveHashCodeProvider,
    CollectionBase,
    Comparer,
    CompatibleComparer,
    DictionaryBase,
    EmptyReadOnlyDictionaryInternal,
    HashHelpers,
    Hashtable,
    KeyValuePairs,
    ListDictionaryInternal,
    Queue,
    ReadOnlyCollectionBase,
    SortedList,
    Stack,
    StructuralComparer,
    StructuralComparisons,
    StructuralEqualityComparer,
    DictionaryEntry,
    ICollection,
    IComparer,
    IDictionary,
    IDictionaryEnumerator,
    IEnumerable,
    IEnumerator,
    IEqualityComparer,
    IHashCodeProvider,
    IList,
    IStructuralComparable,
    IStructuralEquatable,
]
