from __future__ import annotations

from abc import ABC
from typing import Callable, Generic, List, Protocol, TypeVar, Union, overload

from System import Array, AsyncCallback, Boolean, Enum, EventArgs, IAsyncResult, ICloneable, Int16, Int32, IntPtr, MulticastDelegate, Object, String, ValueType, Void
from System.Collections import Hashtable, ICollection, IComparer, IDictionary, IDictionaryEnumerator, IEnumerable, IEnumerator, IEqualityComparer, IHashCodeProvider, IList, SortedList
from System.Runtime.Serialization import IDeserializationCallback, ISerializable, SerializationInfo, StreamingContext

# ---------- Types ---------- #

T = TypeVar('T')

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
IntType = Union[int, Int32]
NIntType = Union[int, IntPtr]
ObjectType = Object
ShortType = Union[int, Int16]
StringType = Union[str, String]
VoidType = Union[None, Void]


class EventType(Generic[T]):
    def __iadd__(self, other: T): ...
    
    def __isub__(self, other: T): ...



# ---------- Classes ---------- #

class BackCompatibleStringComparer(ObjectType, IEqualityComparer):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    @overload
    def GetHashCode(obj: StringType) -> IntType: ...
    
    @overload
    def GetHashCode(self, o: ObjectType) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CollectionsUtil(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    @overload
    def CreateCaseInsensitiveHashtable(capacity: IntType) -> Hashtable: ...
    
    @staticmethod
    @overload
    def CreateCaseInsensitiveHashtable() -> Hashtable: ...
    
    @staticmethod
    @overload
    def CreateCaseInsensitiveHashtable(d: IDictionary) -> Hashtable: ...
    
    @staticmethod
    def CreateCaseInsensitiveSortedList() -> SortedList: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CompatibleComparer(ObjectType, IEqualityComparer):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Comparer(self) -> IComparer: ...
    
    @staticmethod
    @property
    def DefaultComparer() -> IComparer: ...
    
    @staticmethod
    @property
    def DefaultHashCodeProvider() -> IHashCodeProvider: ...
    
    @property
    def HashCodeProvider(self) -> IHashCodeProvider: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Equals(self, a: ObjectType, b: ObjectType) -> BooleanType: ...
    
    @overload
    def GetHashCode(self, obj: ObjectType) -> IntType: ...
    
    def get_Comparer(self) -> IComparer: ...
    
    @staticmethod
    def get_DefaultComparer() -> IComparer: ...
    
    @staticmethod
    def get_DefaultHashCodeProvider() -> IHashCodeProvider: ...
    
    def get_HashCodeProvider(self) -> IHashCodeProvider: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class FixedStringLookup(ABC, ObjectType):
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


class HybridDictionary(ObjectType, IDictionary, ICollection, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, initialSize: IntType): ...
    
    @overload
    def __init__(self, caseInsensitive: BooleanType): ...
    
    @overload
    def __init__(self, initialSize: IntType, caseInsensitive: BooleanType): ...
    
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


class ListDictionary(ObjectType, IDictionary, ICollection, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, comparer: IComparer): ...
    
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


class NameObjectCollectionBase(ABC, ObjectType, ICollection, IEnumerable, ISerializable, IDeserializationCallback):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def Keys(self) -> KeysCollection: ...
    
    # ---------- Methods ---------- #
    
    def GetEnumerator(self) -> IEnumerator: ...
    
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    
    def OnDeserialization(self, sender: ObjectType) -> VoidType: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_Keys(self) -> KeysCollection: ...
    
    # No Events
    
    
    # ---------- Sub Classes ---------- #
    
    class KeysCollection(ObjectType, ICollection, IEnumerable):
        # No Fields
        
        # No Constructors
        
        # ---------- Properties ---------- #
        
        @property
        def Count(self) -> IntType: ...
        
        def __getitem__(self, key: IntType) -> StringType: ...
        
        # ---------- Methods ---------- #
        
        def Get(self, index: IntType) -> StringType: ...
        
        def GetEnumerator(self) -> IEnumerator: ...
        
        def get_Count(self) -> IntType: ...
        
        def get_Item(self, index: IntType) -> StringType: ...
        
        # No Events
        
        # No Sub Classes
        
        # No Sub Structs
        
        # No Sub Interfaces
        
        # No Sub Enums
    
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class NameValueCollection(NameObjectCollectionBase, ICollection, IEnumerable, ISerializable, IDeserializationCallback):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, col: NameValueCollection): ...
    
    @overload
    def __init__(self, hashProvider: IHashCodeProvider, comparer: IComparer): ...
    
    @overload
    def __init__(self, capacity: IntType): ...
    
    @overload
    def __init__(self, equalityComparer: IEqualityComparer): ...
    
    @overload
    def __init__(self, capacity: IntType, equalityComparer: IEqualityComparer): ...
    
    @overload
    def __init__(self, capacity: IntType, col: NameValueCollection): ...
    
    @overload
    def __init__(self, capacity: IntType, hashProvider: IHashCodeProvider, comparer: IComparer): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AllKeys(self) -> ArrayType[StringType]: ...
    
    def __getitem__(self, key: StringType) -> StringType: ...
    
    def __setitem__(self, key: StringType, value: StringType) -> None: ...
    
    def __getitem__(self, key: IntType) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Add(self, c: NameValueCollection) -> VoidType: ...
    
    @overload
    def Add(self, name: StringType, value: StringType) -> VoidType: ...
    
    def Clear(self) -> VoidType: ...
    
    def CopyTo(self, dest: Array, index: IntType) -> VoidType: ...
    
    @overload
    def Get(self, name: StringType) -> StringType: ...
    
    @overload
    def Get(self, index: IntType) -> StringType: ...
    
    def GetKey(self, index: IntType) -> StringType: ...
    
    @overload
    def GetValues(self, name: StringType) -> ArrayType[StringType]: ...
    
    @overload
    def GetValues(self, index: IntType) -> ArrayType[StringType]: ...
    
    def HasKeys(self) -> BooleanType: ...
    
    def Remove(self, name: StringType) -> VoidType: ...
    
    def Set(self, name: StringType, value: StringType) -> VoidType: ...
    
    def get_AllKeys(self) -> ArrayType[StringType]: ...
    
    @overload
    def get_Item(self, name: StringType) -> StringType: ...
    
    @overload
    def get_Item(self, index: IntType) -> StringType: ...
    
    def set_Item(self, name: StringType, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class NotifyCollectionChangedEventArgs(EventArgs):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, action: NotifyCollectionChangedAction): ...
    
    @overload
    def __init__(self, action: NotifyCollectionChangedAction, changedItem: ObjectType): ...
    
    @overload
    def __init__(self, action: NotifyCollectionChangedAction, changedItem: ObjectType, index: IntType): ...
    
    @overload
    def __init__(self, action: NotifyCollectionChangedAction, changedItems: IList): ...
    
    @overload
    def __init__(self, action: NotifyCollectionChangedAction, changedItems: IList, startingIndex: IntType): ...
    
    @overload
    def __init__(self, action: NotifyCollectionChangedAction, newItem: ObjectType, oldItem: ObjectType): ...
    
    @overload
    def __init__(self, action: NotifyCollectionChangedAction, newItem: ObjectType, oldItem: ObjectType, index: IntType): ...
    
    @overload
    def __init__(self, action: NotifyCollectionChangedAction, newItems: IList, oldItems: IList): ...
    
    @overload
    def __init__(self, action: NotifyCollectionChangedAction, newItems: IList, oldItems: IList, startingIndex: IntType): ...
    
    @overload
    def __init__(self, action: NotifyCollectionChangedAction, changedItem: ObjectType, index: IntType, oldIndex: IntType): ...
    
    @overload
    def __init__(self, action: NotifyCollectionChangedAction, changedItems: IList, index: IntType, oldIndex: IntType): ...
    
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
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class NotifyCollectionChangedEventHandler(MulticastDelegate, ICloneable, ISerializable):
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


class OrderedDictionary(ObjectType, IOrderedDictionary, IDictionary, ICollection, IEnumerable, ISerializable, IDeserializationCallback):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, capacity: IntType): ...
    
    @overload
    def __init__(self, comparer: IEqualityComparer): ...
    
    @overload
    def __init__(self, capacity: IntType, comparer: IEqualityComparer): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def IsReadOnly(self) -> BooleanType: ...
    
    def __getitem__(self, key: IntType) -> ObjectType: ...
    
    def __setitem__(self, key: IntType, value: ObjectType) -> None: ...
    
    def __getitem__(self, key: ObjectType) -> ObjectType: ...
    
    def __setitem__(self, key: ObjectType, value: ObjectType) -> None: ...
    
    @property
    def Keys(self) -> ICollection: ...
    
    @property
    def Values(self) -> ICollection: ...
    
    # ---------- Methods ---------- #
    
    def Add(self, key: ObjectType, value: ObjectType) -> VoidType: ...
    
    def AsReadOnly(self) -> OrderedDictionary: ...
    
    def Clear(self) -> VoidType: ...
    
    def Contains(self, key: ObjectType) -> BooleanType: ...
    
    def CopyTo(self, array: Array, index: IntType) -> VoidType: ...
    
    def GetEnumerator(self) -> IDictionaryEnumerator: ...
    
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    
    def Insert(self, index: IntType, key: ObjectType, value: ObjectType) -> VoidType: ...
    
    def Remove(self, key: ObjectType) -> VoidType: ...
    
    def RemoveAt(self, index: IntType) -> VoidType: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_IsReadOnly(self) -> BooleanType: ...
    
    @overload
    def get_Item(self, index: IntType) -> ObjectType: ...
    
    @overload
    def get_Item(self, key: ObjectType) -> ObjectType: ...
    
    def get_Keys(self) -> ICollection: ...
    
    def get_Values(self) -> ICollection: ...
    
    @overload
    def set_Item(self, index: IntType, value: ObjectType) -> VoidType: ...
    
    @overload
    def set_Item(self, key: ObjectType, value: ObjectType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class StringCollection(ObjectType, IList, ICollection, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def IsReadOnly(self) -> BooleanType: ...
    
    @property
    def IsSynchronized(self) -> BooleanType: ...
    
    def __getitem__(self, key: IntType) -> StringType: ...
    
    def __setitem__(self, key: IntType, value: StringType) -> None: ...
    
    @property
    def SyncRoot(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def Add(self, value: StringType) -> IntType: ...
    
    def AddRange(self, value: ArrayType[StringType]) -> VoidType: ...
    
    def Clear(self) -> VoidType: ...
    
    def Contains(self, value: StringType) -> BooleanType: ...
    
    def CopyTo(self, array: ArrayType[StringType], index: IntType) -> VoidType: ...
    
    def GetEnumerator(self) -> StringEnumerator: ...
    
    def IndexOf(self, value: StringType) -> IntType: ...
    
    def Insert(self, index: IntType, value: StringType) -> VoidType: ...
    
    def Remove(self, value: StringType) -> VoidType: ...
    
    def RemoveAt(self, index: IntType) -> VoidType: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_IsReadOnly(self) -> BooleanType: ...
    
    def get_IsSynchronized(self) -> BooleanType: ...
    
    def get_Item(self, index: IntType) -> StringType: ...
    
    def get_SyncRoot(self) -> ObjectType: ...
    
    def set_Item(self, index: IntType, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class StringDictionary(ObjectType, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def IsSynchronized(self) -> BooleanType: ...
    
    def __getitem__(self, key: StringType) -> StringType: ...
    
    def __setitem__(self, key: StringType, value: StringType) -> None: ...
    
    @property
    def Keys(self) -> ICollection: ...
    
    @property
    def SyncRoot(self) -> ObjectType: ...
    
    @property
    def Values(self) -> ICollection: ...
    
    # ---------- Methods ---------- #
    
    def Add(self, key: StringType, value: StringType) -> VoidType: ...
    
    def Clear(self) -> VoidType: ...
    
    def ContainsKey(self, key: StringType) -> BooleanType: ...
    
    def ContainsValue(self, value: StringType) -> BooleanType: ...
    
    def CopyTo(self, array: Array, index: IntType) -> VoidType: ...
    
    def GetEnumerator(self) -> IEnumerator: ...
    
    def Remove(self, key: StringType) -> VoidType: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_IsSynchronized(self) -> BooleanType: ...
    
    def get_Item(self, key: StringType) -> StringType: ...
    
    def get_Keys(self) -> ICollection: ...
    
    def get_SyncRoot(self) -> ObjectType: ...
    
    def get_Values(self) -> ICollection: ...
    
    def set_Item(self, key: StringType, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class StringDictionaryWithComparer(StringDictionary, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, comparer: IEqualityComparer): ...
    
    # ---------- Properties ---------- #
    
    def __getitem__(self, key: StringType) -> StringType: ...
    
    def __setitem__(self, key: StringType, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Add(self, key: StringType, value: StringType) -> VoidType: ...
    
    def ContainsKey(self, key: StringType) -> BooleanType: ...
    
    def Remove(self, key: StringType) -> VoidType: ...
    
    def get_Item(self, key: StringType) -> StringType: ...
    
    def set_Item(self, key: StringType, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class StringEnumerator(ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Current(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def MoveNext(self) -> BooleanType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Current(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# ---------- Structs ---------- #

class BitVector32(ValueType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, data: IntType): ...
    
    @overload
    def __init__(self, value: BitVector32): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Data(self) -> IntType: ...
    
    def __getitem__(self, key: IntType) -> BooleanType: ...
    
    def __setitem__(self, key: IntType, value: BooleanType) -> None: ...
    
    def __getitem__(self, key: Section) -> IntType: ...
    
    def __setitem__(self, key: Section, value: IntType) -> None: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    @overload
    def CreateMask() -> IntType: ...
    
    @staticmethod
    @overload
    def CreateMask(previous: IntType) -> IntType: ...
    
    @staticmethod
    @overload
    def CreateSection(maxValue: ShortType) -> Section: ...
    
    @staticmethod
    @overload
    def CreateSection(maxValue: ShortType, previous: Section) -> Section: ...
    
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    @overload
    def ToString(self) -> StringType: ...
    
    @staticmethod
    @overload
    def ToString(value: BitVector32) -> StringType: ...
    
    def get_Data(self) -> IntType: ...
    
    @overload
    def get_Item(self, bit: IntType) -> BooleanType: ...
    
    @overload
    def get_Item(self, section: Section) -> IntType: ...
    
    @overload
    def set_Item(self, bit: IntType, value: BooleanType) -> VoidType: ...
    
    @overload
    def set_Item(self, section: Section, value: IntType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # ---------- Sub Structs ---------- #
    
    class Section(ValueType):
        # No Fields
        
        # No Constructors
        
        # ---------- Properties ---------- #
        
        @property
        def Mask(self) -> ShortType: ...
        
        @property
        def Offset(self) -> ShortType: ...
        
        # ---------- Methods ---------- #
        
        @overload
        def Equals(self, o: ObjectType) -> BooleanType: ...
        
        @overload
        def Equals(self, obj: Section) -> BooleanType: ...
        
        def GetHashCode(self) -> IntType: ...
        
        @overload
        def ToString(self) -> StringType: ...
        
        @staticmethod
        @overload
        def ToString(value: Section) -> StringType: ...
        
        def get_Mask(self) -> ShortType: ...
        
        def get_Offset(self) -> ShortType: ...
        
        @staticmethod
        def op_Equality(a: Section, b: Section) -> BooleanType: ...
        
        @staticmethod
        def op_Inequality(a: Section, b: Section) -> BooleanType: ...
        
        # No Events
        
        # No Sub Classes
        
        # No Sub Structs
        
        # No Sub Interfaces
        
        # No Sub Enums
    
    
    # No Sub Interfaces
    
    # No Sub Enums


# ---------- Interfaces ---------- #

class INotifyCollectionChanged(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def add_CollectionChanged(self, value: NotifyCollectionChangedEventHandler) -> VoidType: ...
    
    def remove_CollectionChanged(self, value: NotifyCollectionChangedEventHandler) -> VoidType: ...
    
    # ---------- Events ---------- #
    
    CollectionChanged: EventType[NotifyCollectionChangedEventHandler] = ...


class IOrderedDictionary(Protocol, IDictionary, ICollection, IEnumerable):
    # ---------- Properties ---------- #
    
    def __getitem__(self, key: IntType) -> ObjectType: ...
    
    def __setitem__(self, key: IntType, value: ObjectType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def GetEnumerator(self) -> IDictionaryEnumerator: ...
    
    def Insert(self, index: IntType, key: ObjectType, value: ObjectType) -> VoidType: ...
    
    def RemoveAt(self, index: IntType) -> VoidType: ...
    
    def get_Item(self, index: IntType) -> ObjectType: ...
    
    def set_Item(self, index: IntType, value: ObjectType) -> VoidType: ...
    
    # No Events


# ---------- Enums ---------- #

class NotifyCollectionChangedAction(Enum):
    Add = 0
    Remove = 1
    Replace = 2
    Move = 3
    Reset = 4


# ---------- Delegates ---------- #

NotifyCollectionChangedEventHandler = Callable[[ObjectType, NotifyCollectionChangedEventArgs], VoidType]

__all__ = [
    BackCompatibleStringComparer,
    CollectionsUtil,
    CompatibleComparer,
    FixedStringLookup,
    HybridDictionary,
    ListDictionary,
    NameObjectCollectionBase,
    NameValueCollection,
    NotifyCollectionChangedEventArgs,
    NotifyCollectionChangedEventHandler,
    OrderedDictionary,
    StringCollection,
    StringDictionary,
    StringDictionaryWithComparer,
    StringEnumerator,
    BitVector32,
    INotifyCollectionChanged,
    IOrderedDictionary,
    NotifyCollectionChangedAction,
    NotifyCollectionChangedEventHandler,
]
