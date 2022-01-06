__all__ = [
    'ArrayList',
    'BitArray',
    'CaseInsensitiveComparer',
    'CaseInsensitiveHashCodeProvider',
    'CollectionBase',
    'Comparer',
    'DictionaryBase',
    'Hashtable',
    'Queue',
    'ReadOnlyCollectionBase',
    'SortedList',
    'Stack',
    'StructuralComparisons',
    'DictionaryEntry',
    'ICollection',
    'IComparer',
    'IDictionary',
    'IDictionaryEnumerator',
    'IEnumerable',
    'IEnumerator',
    'IEqualityComparer',
    'IHashCodeProvider',
    'IList',
    'IStructuralComparable',
    'IStructuralEquatable',
]

from abc import ABC
from typing import Protocol, TypeVar, overload, Final

from . import Generic
from .. import ValueType, ObjectType, NullableType, VoidType, Object, IntType, BooleanType, ArrayType, ICloneable, StringType, FloatType, Obsolete, ByteType, TypeType
from ..Globalization import CultureInfo
from ..Linq import ParallelQuery, IQueryable
from ..Runtime.Serialization import IDeserializationCallback, ISerializable, SerializationInfo, StreamingContext
from ..util import Item

T = TypeVar('T')


# ---------- CLASSES ---------- #

class ArrayList(Object, ICloneable, IList):
    """Implements the IList interface using an array whose size is
    dynamically increased as required."""
    
    @overload
    def __init__(self):
        """Initializes a new instance of the ArrayList class that is empty
        and has the default initial capacity."""
    
    @overload
    def __init__(self, ICollection):
        """Initializes a new instance of the ArrayList class that contains
        elements copied from the specified collection and that has the
        same initial capacity as the number of elements copied."""
    
    @overload
    def __init__(self, Int32):
        """Initializes a new instance of the ArrayList class that is empty
        and has the specified initial capacity."""
    
    @property
    def Capacity(self) -> IntType:
        """Gets the number of elements that the ArrayList can contain."""
    
    @Capacity.setter
    def Capacity(self, value: IntType) -> VoidType:
        """Sets the number of elements that the ArrayList can contain."""
    
    @staticmethod
    def Adapter(list: IList) -> ArrayList:
        """Creates an ArrayList wrapper for a specific IList."""
    
    def AddRange(self, c: ICollection) -> VoidType:
        """Adds the elements of an ICollection to the end of the ArrayList."""
    
    @overload
    def BinarySearch(self, index: IntType, count: IntType, value: NullableType[ObjectType], comparer: NullableType[IComparer]) -> IntType:
        """Searches a range of elements in the sorted ArrayList for an
        element using the specified comparer and returns the zero-based
        index of the element."""
    
    @overload
    def BinarySearch(self, value: NullableType[ObjectType]) -> IntType:
        """Searches the entire sorted ArrayList for an element using the
        default comparer and returns the zero-based index of the element."""
    
    @overload
    def BinarySearch(self, value: NullableType[ObjectType], comparer: NullableType[IComparer]) -> IntType:
        """Searches the entire sorted ArrayList for an element using the
        specified comparer and returns the zero-based index of the element."""
    
    @staticmethod
    @overload
    def FixedSize(list: ArrayList) -> ArrayList:
        """Returns an ArrayList wrapper with a fixed size."""
    
    @staticmethod
    @overload
    def FixedSize(list: IList) -> ArrayList:
        """Returns an IList wrapper with a fixed size."""
    
    def GetRange(self, index: IntType, count: IntType) -> ArrayList:
        """Returns an ArrayList which represents a subset of the elements
        in the source ArrayList."""
    
    def InsertRange(self, index: IntType, c: ICollection) -> VoidType:
        """Inserts the elements of a collection into the ArrayList at the
        specified index."""
    
    @overload
    def LastIndexOf(self, value: NullableType[ObjectType]) -> IntType:
        """Searches for the specified Object and returns the zero-based
        index of the last occurrence within the entire ArrayList."""
    
    @overload
    def LastIndexOf(self, value: NullableType[ObjectType], startIndex: IntType) -> IntType:
        """Searches for the specified Object and returns the zero-based
        index of the last occurrence within the range of elements in the
        ArrayList that extends from the first element to the specified
        index."""
    
    @overload
    def LastIndexOf(self, value: NullableType[ObjectType], startIndex: IntType, count: IntType) -> IntType:
        """Searches for the specified Object and returns the zero-based
        index of the last occurrence within the range of elements in the
        ArrayList that contains the specified number of elements and ends
        at the specified index."""
    
    @staticmethod
    @overload
    def ReadOnly(list: ArrayList) -> ArrayList:
        """Returns a read-only ArrayList wrapper."""
    
    @staticmethod
    @overload
    def ReadOnly(list: IList) -> ArrayList:
        """Returns a read-only IList wrapper."""
    
    def RemoveRange(self, index: IntType, count: IntType) -> VoidType:
        """Removes a range of elements from the ArrayList."""
    
    @staticmethod
    def Repeat(value: NullableType[ObjectType], count: IntType) -> ArrayList:
        """Returns an ArrayList whose elements are copies of the specified
        value."""
    
    @overload
    def Reverse(self) -> VoidType:
        """Reverses the order of the elements in the entire ArrayList."""
    
    @overload
    def Reverse(self, index: IntType, count: IntType) -> VoidType:
        """Reverses the order of the elements in the specified range."""
    
    def SetRange(self, index: IntType, c: ICollection) -> VoidType:
        """Copies the elements of a collection over a range of elements in
        the ArrayList."""
    
    @overload
    def Sort(self) -> VoidType:
        """Sorts the elements in the entire ArrayList."""
    
    @overload
    def Sort(self, comparer: NullableType[IComparer]) -> VoidType:
        """Sorts the elements in the entire ArrayList using the specified
        comparer."""
    
    @overload
    def Sort(self, index: IntType, count: IntType, comparer: NullableType[IComparer]) -> VoidType:
        """Sorts the elements in a range of elements in ArrayList using the
        specified comparer."""
    
    @staticmethod
    @overload
    def Synchronized(list: ArrayList) -> ArrayList:
        """Returns an ArrayList wrapper that is synchronized (thread safe)."""
    
    @staticmethod
    @overload
    def Synchronized(list: IList) -> ArrayList:
        """Returns an IList wrapper that is synchronized (thread safe)."""
    
    @overload
    def ToArray(self) -> ArrayType[NullableType[ObjectType]]:
        """Copies the elements of the ArrayList to a new Object array."""
    
    @overload
    def ToArray(self, type: TypeType) -> ArrayType:
        """Copies the elements of the ArrayList to a new array of the
        specified element type."""
    
    def TrimToSize(self) -> VoidType:
        """Sets the capacity to the actual number of elements in the
        ArrayList."""


class BitArray(Object, ICloneable, ICollection):
    """Manages a compact array of bit values, which are represented as
    Booleans, where true indicates that the bit is on (1) and false
    indicates the bit is off (0)."""
    
    @overload
    def __init__(self, bits: BitArray):
        """Initializes a new instance of the BitArray class that contains
        bit values copied from the specified BitArray."""
    
    @overload
    def __init__(self, values: ArrayType[BooleanType]):
        """Initializes a new instance of the BitArray class that contains
        bit values copied from the specified array of Booleans."""
    
    @overload
    def __init__(self, bytes: ArrayType[ByteType]):
        """Initializes a new instance of the BitArray class that contains
        bit values copied from the specified array of bytes."""
    
    @overload
    def __init__(self, length: IntType):
        """Initializes a new instance of the BitArray class that can hold
        the specified number of bit values, which are initially set to false."""
    
    @overload
    def __init__(self, length: IntType, defaultValue: BooleanType):
        """Initializes a new instance of the BitArray class that can hold
        the specified number of bit values, which are initially set to the specified value."""
    
    @overload
    def __init__(self, values: ArrayType[IntType]):
        """Initializes a new instance of the BitArray class that contains
        bit values copied from the specified array of 32-bit integers."""
    
    @property
    def IsReadOnly(self) -> BooleanType:
        """Gets a value indicating whether the BitArray is read-only."""
    
    @property
    def Item(self) -> Item[IntType, BooleanType]:
        """Gets or sets the value of the bit at a specific position in the
        BitArray."""
    
    def __getitem__(self, key: IntType) -> BooleanType: ...
    
    def __setitem__(self, key: IntType, value: BooleanType) -> VoidType: ...
    
    @property
    def Length(self) -> IntType:
        """Gets the number of elements in the BitArray."""
    
    @Length.setter
    def Length(self, value: IntType) -> VoidType:
        """Sets the number of elements in the BitArray."""
    
    def And(self, value: BitArray) -> BitArray:
        """Performs the bitwise AND operation between the elements of the
        current BitArray object and the corresponding elements in the
        specified array. The current BitArray object will be modified to
        store the result of the bitwise AND operation."""
    
    def Get(self, index: IntType) -> BooleanType:
        """Gets the value of the bit at a specific position in the BitArray."""
    
    def LeftShift(self, count: IntType) -> BitArray:
        """Shifts all the bit values of the current BitArray to the left o
         count bits."""
    
    def Not(self) -> BitArray:
        """Inverts all the bit values in the current BitArray, so that
        elements set to true are changed to false, and elements set to false
        are changed to true."""
    
    def Or(self, value: BitArray) -> BitArray:
        """Performs the bitwise OR operation between the elements of the
        current BitArray object and the corresponding elements in the
        specified array. The current BitArray object will be modified to
        store the result of the bitwise OR operation."""
    
    def RightShift(self, count: IntType) -> BitArray:
        """Shifts all the bit values of the current BitArray to the right on
        count bits."""
    
    def Set(self, index: IntType, value: BooleanType) -> VoidType:
        """Sets the bit at a specific position in the BitArray to the
        specified value."""
    
    def SetAll(self, index: BooleanType) -> VoidType:
        """Sets all bits in the BitArray to the specified value."""
    
    def Xor(self, value: BitArray) -> BitArray:
        """Performs the bitwise exclusive OR operation between the elements
        of the current BitArray object against the corresponding elements in
        the specified array. The current BitArray object will be modified to
        store the result of the bitwise exclusive OR operation."""


class CaseInsensitiveComparer(Object, IComparer):
    """Compares two objects for equivalence, ignoring the case of strings."""
    
    @overload
    def __init__(self):
        """Initializes a new instance of the CaseInsensitiveComparer class
        using the CurrentCulture of the current thread."""
    
    @overload
    def __init__(self, culture: CultureInfo):
        """Initializes a new instance of the CaseInsensitiveComparer class
        using the specified CultureInfo."""
    
    @staticmethod
    @property
    def Default() -> CaseInsensitiveComparer:
        """Gets an instance of CaseInsensitiveComparer that is associated
        with the CurrentCulture of the current thread and that is always
        available."""
    
    @staticmethod
    @property
    def DefaultInvariant() -> CaseInsensitiveComparer:
        """Gets an instance of CaseInsensitiveComparer that is associated
        with InvariantCulture and that is always available."""


class CaseInsensitiveHashCodeProvider(Object, IHashCodeProvider):
    """Obsolete.
    Supplies a hash code for an object, using a hashing algorithm that
    ignores the case of strings."""
    
    @overload
    def __init__(self) -> Obsolete:
        """Initializes a new instance of the CaseInsensitiveHashCodeProvider
        class using the CurrentCulture of the current thread."""
    
    @overload
    def __init__(self, culture: CultureInfo) -> Obsolete:
        """Initializes a new instance of the CaseInsensitiveHashCodeProvider
        class using the specified CultureInfo."""
    
    @staticmethod
    @property
    def Default() -> CaseInsensitiveHashCodeProvider:
        """Gets an instance of CaseInsensitiveHashCodeProvider that is
        associated with the CurrentCulture of the current thread and that is
        always available."""
    
    @staticmethod
    @property
    def DefaultInvariant() -> CaseInsensitiveHashCodeProvider:
        """Gets an instance of CaseInsensitiveHashCodeProvider that is
        associated with InvariantCulture and that is always available."""


class CollectionBase(ABC, Object, IList):
    """Provides the abstract base class for a strongly typed collection."""
    
    @overload
    def __init__(self):
        """Initializes a new instance of the CollectionBase class with the
        default initial capacity."""
    
    @overload
    def __init__(self, capacity: IntType):
        """Initializes a new instance of the CollectionBase class with the
        specified capacity."""
    
    @property
    def Capacity(self) -> IntType:
        """Gets the number of elements that the CollectionBase can contain."""
    
    @Capacity.setter
    def Capacity(self, value: IntType) -> VoidType:
        """Sets the number of elements that the CollectionBase can contain."""
    
    @property
    def InnerList(self) -> ArrayList:
        """Gets an ArrayList containing the list of elements in the
        CollectionBase instance."""
    
    @property
    def List(self) -> IList:
        """Gets an IList containing the list of elements in the CollectionBase
        instance."""
    
    def OnClear(self) -> VoidType:
        """Performs additional custom processes when clearing the contents of
        the CollectionBase instance."""
    
    def OnClearComplete(self) -> VoidType:
        """Performs additional custom processes after clearing the contents
        of the CollectionBase instance."""
    
    def OnInsert(self, index: IntType, value: NullableType[ObjectType]) -> VoidType:
        """Performs additional custom processes before inserting a new element into the CollectionBase instance."""
    
    def OnInsertComplete(self, index: IntType, value: NullableType[ObjectType]) -> VoidType:
        """Performs additional custom processes after inserting a new element into the CollectionBase instance."""
    
    def OnRemove(self, index: IntType, value: NullableType[ObjectType]) -> VoidType:
        """Performs additional custom processes when removing an element from the CollectionBase instance."""
    
    def OnRemoveComplete(self, index: IntType, value: NullableType[ObjectType]) -> VoidType:
        """Performs additional custom processes after removing an element from the CollectionBase instance."""
    
    def OnSet(self, index: IntType, oldValue: NullableType[ObjectType], newValue: NullableType[ObjectType]) -> VoidType:
        """Performs additional custom processes before setting a value in the CollectionBase instance."""
    
    def OnSetComplete(self, index: IntType, oldValue: NullableType[ObjectType], newValue: NullableType[ObjectType]) -> VoidType:
        """Performs additional custom processes after setting a value in the CollectionBase instance."""
    
    def OnValidate(self, value: ObjectType) -> VoidType:
        """Performs additional custom processes when validating a value."""
    
    def ToString(self) -> NullableType[StringType]:
        """Returns a string that represents the current object."""


class Comparer(Object, IComparer, ISerializable):
    """Compares two objects for equivalence, where string comparisons are
    case-sensitive."""
    
    def __init__(self, culture: CultureInfo):
        """Initializes a new instance of the Comparer class using the
        specified CultureInfo."""
    
    Default: Final[Comparer] = ...
    """Represents an instance of Comparer that is associated with the
    CurrentCulture of the current thread. This field is read-only."""
    
    DefaultInvariant: Final[Comparer] = ...
    """Represents an instance of Comparer that is associated with
    InvariantCulture. This field is read-only."""


class DictionaryBase(ABC, Object, IDictionary):
    """Provides the abstract base class for a strongly typed collection of key/value pairs."""
    
    def __init__(self):
        """Initializes a new instance of the DictionaryBase class."""
    
    @property
    def Dictionary(self) -> IDictionary:
        """Gets the list of elements contained in the DictionaryBase instance."""
    
    @property
    def InnerHashtable(self) -> Hashtable:
        """Gets the list of elements contained in the DictionaryBase instance."""
    
    def OnClear(self) -> VoidType:
        """Performs additional custom processes before clearing the contents
        of the DictionaryBase instance."""
    
    def OnClearComplete(self) -> VoidType:
        """Performs additional custom processes after clearing the contents
        of the DictionaryBase instance."""
    
    def OnGet(self, key: ObjectType, currentValue: NullableType[ObjectType]) -> NullableType[ObjectType]:
        """Gets the element with the specified key and value in the
        DictionaryBase instance."""
    
    def OnInsert(self, key: ObjectType, value: NullableType[ObjectType]) -> VoidType:
        """Performs additional custom processes before inserting a new
        element into the DictionaryBase instance."""
    
    def OnInsertComplete(self, key: ObjectType, value: NullableType[ObjectType]) -> VoidType:
        """Performs additional custom processes after inserting a new element
        into the DictionaryBase instance."""
    
    def OnRemove(self, key: ObjectType, value: NullableType[ObjectType]) -> VoidType:
        """Performs additional custom processes before removing an element
        from the DictionaryBase instance."""
    
    def OnRemoveComplete(self, key: ObjectType, value: NullableType[ObjectType]) -> VoidType:
        """Performs additional custom processes after removing an element
        from the DictionaryBase instance."""
    
    def OnSet(self, key: ObjectType, oldValue: NullableType[ObjectType], newValue: NullableType[ObjectType]) -> VoidType:
        """Performs additional custom processes before setting a value in the
        DictionaryBase instance."""
    
    def OnSetComplete(self, key: ObjectType, oldValue: NullableType[ObjectType], newValue: NullableType[ObjectType]) -> VoidType:
        """Performs additional custom processes after setting a value in the
        DictionaryBase instance."""
    
    def OnValidate(self, key: ObjectType, value: NullableType[ObjectType]) -> VoidType:
        """Performs additional custom processes when validating the element
        with the specified key and value."""


class Hashtable(Object, ICloneable, IDictionary, IDeserializationCallback, ISerializable):
    """Represents a collection of key/value pairs that are organized based
    on the hash code of the key."""
    
    @overload
    def __init__(self):
        """Initializes a new, empty instance of the Hashtable class using
        the default initial capacity, load factor, hash code provider, and
        comparer."""
    
    @overload
    def __init__(self, d: IDictionary):
        """Initializes a new instance of the Hashtable class by copying the
        elements from the specified dictionary to the new Hashtable object.
        The new Hashtable object has an initial capacity equal to the number
        of elements copied, and uses the default load factor, hash code
        provider, and comparer."""
    
    @overload
    def __init__(self, d: IDictionary, equalityComparer: NullableType[IEqualityComparer]):
        """Initializes a new instance of the Hashtable class by copying the
        elements from the specified dictionary to a new Hashtable object.
        The new Hashtable object has an initial capacity equal to the number
        of elements copied, and uses the default load factor and the
        specified IEqualityComparer object."""
    
    @overload
    def __init__(self, d: IDictionary, hcp: NullableType[IHashCodeProvider], comparer: NullableType[IComparer]) -> Obsolete:
        """Obsolete.
        Initializes a new instance of the Hashtable class by copying the
        elements from the specified dictionary to the new Hashtable object.
        The new Hashtable object has an initial capacity equal to the number
        of elements copied, and uses the default load factor, and the
        specified hash code provider and comparer. This API is obsolete. For
        an alternative, see Hashtable(IDictionary, IEqualityComparer)."""
    
    @overload
    def __init__(self, d: IDictionary, loadFactor: FloatType):
        """Initializes a new instance of the Hashtable class by copying the
        elements from the specified dictionary to the new Hashtable object.
        The new Hashtable object has an initial capacity equal to the number
        of elements copied, and uses the specified load factor, and the
        default hash code provider and comparer."""
    
    @overload
    def __init__(self, d: IDictionary, loadFactor: FloatType, equalityComparer: NullableType[IEqualityComparer]):
        """Initializes a new instance of the Hashtable class by copying the
        elements from the specified dictionary to the new Hashtable object.
        The new Hashtable object has an initial capacity equal to the number
        of elements copied, and uses the specified load factor and
        IEqualityComparer object."""
    
    @overload
    def __init__(self, d: IDictionary, loadFactor: FloatType, hcp: NullableType[IHashCodeProvider], comparer: NullableType[IComparer]) -> Obsolete:
        """Obsolete.
        Initializes a new instance of the Hashtable class by copying the
        elements from the specified dictionary to the new Hashtable object.
        The new Hashtable object has an initial capacity equal to the number
        of elements copied, and uses the specified load factor, hash code
        provider, and comparer."""
    
    @overload
    def __init__(self, equalityComparer: NullableType[IEqualityComparer]):
        """Initializes a new, empty instance of the Hashtable class using
        the default initial capacity and load factor, and the specified
        IEqualityComparer object."""
    
    @overload
    def __init__(self, hcp: NullableType[IHashCodeProvider], comparer: NullableType[IComparer]) -> Obsolete:
        """Obsolete.
        Initializes a new, empty instance of the Hashtable class using the
        default initial capacity and load factor, and the specified hash
        code provider and comparer."""
    
    @overload
    def __init__(self, capacity: IntType):
        """Initializes a new, empty instance of the Hashtable class using
        the specified initial capacity, and the default load factor, hash
        code provider, and comparer."""
    
    @overload
    def __init__(self, capacity: IntType, equalityComparer: NullableType[IEqualityComparer]):
        """Initializes a new, empty instance of the Hashtable class using
        the specified initial capacity and IEqualityComparer, and the
        default load factor."""
    
    @overload
    def __init__(self, capacity: IntType, hcp: NullableType[IHashCodeProvider], comparer: NullableType[IComparer]):
        """Obsolete.
        Initializes a new, empty instance of the Hashtable class using the
        specified initial capacity, hash code provider, comparer, and the
        default load factor."""
    
    @overload
    def __init__(self, capacity: IntType, loadFactor: FloatType):
        """Initializes a new, empty instance of the Hashtable class using
        the specified initial capacity and load factor, and the default hash
        code provider and comparer."""
    
    @overload
    def __init__(self, capacity: IntType, loadFactor: FloatType, equalityComparer: NullableType[IEqualityComparer]):
        """Initializes a new, empty instance of the Hashtable class using
        the specified initial capacity, load factor, and IEqualityComparer
        object."""
    
    @overload
    def __init__(self, capacity: IntType, loadFactor: FloatType, hcp: NullableType[IHashCodeProvider], comparer: NullableType[IComparer]):
        """Obsolete.
        Initializes a new, empty instance of the Hashtable class using the
        specified initial capacity, load factor, hash code provider, and
        comparer."""
    
    @overload
    def __init__(self, info: SerializationInfo, context: StreamingContext):
        """Initializes a new, empty instance of the Hashtable class that
        is serializable using the specified SerializationInfo and
        StreamingContext objects."""
    
    @property
    def comparer(self) -> Obsolete:
        """Obsolete.
        Gets the IComparer to use for the Hashtable."""
    
    @comparer.setter
    def comparer(self, value: NullableType[IComparer]) -> Obsolete:
        """Obsolete.
        Sets the IComparer to use for the Hashtable."""
    
    @property
    def EqualityComparer(self) -> NullableType[IEqualityComparer]:
        """Gets the IEqualityComparer to use for the Hashtable."""
    
    @property
    def hcp(self) -> Obsolete:
        """Obsolete.
        Gets the object that can dispense hash codes."""
    
    @hcp.setter
    def hcp(self, value: NullableType[IHashCodeProvider]) -> Obsolete:
        """Obsolete.
        Sets the object that can dispense hash codes."""
    
    def ContainsKey(self, key: ObjectType) -> BooleanType:
        """Determines whether the Hashtable contains a specific key."""
    
    def ContainsValue(self, value: NullableType[ObjectType]) -> BooleanType:
        """Determines whether the Hashtable contains a specific value."""
    
    def GetHash(self, key: ObjectType) -> IntType:
        """Returns the hash code for the specified key."""
    
    def KeyEquals(self, item: NullableType[ObjectType], key: ObjectType) -> BooleanType:
        """Compares a specific Object with a specific key in the Hashtable."""
    
    @staticmethod
    def Synchronized(table: Hashtable) -> Hashtable:
        """Returns a synchronized (thread-safe) wrapper for the Hashtable."""


class Queue(Object, ICloneable, ICollection):
    """Represents a first-in, first-out collection of objects."""
    
    @overload
    def __init__(self):
        """Initializes a new instance of the Queue class that is empty, has
        the default initial capacity, and uses the default growth factor."""
    
    @overload
    def __init__(self, col: ICollection):
        """Initializes a new instance of the Queue class that contains
        elements copied from the specified collection, has the same initial
        capacity as the number of elements copied, and uses the default
        growth factor."""
    
    @overload
    def __init__(self, capacity: IntType):
        """Initializes a new instance of the Queue class that is empty, has
        the specified initial capacity, and uses the default growth
        factor."""
    
    @overload
    def __init__(self, capacity: IntType, growFactor: FloatType):
        """Initializes a new instance of the Queue class that is empty, has
        the specified initial capacity, and uses the specified growth
        factor."""
    
    def Clear(self) -> VoidType:
        """Removes all objects from the Queue."""
    
    def Contains(self, obj: NullableType[ObjectType]) -> BooleanType:
        """Determines whether an element is in the Queue."""
    
    def Dequeue(self) -> NullableType[ObjectType]:
        """Removes and returns the object at the beginning of the Queue."""
    
    def Enqueue(self, obj: NullableType[ObjectType]) -> VoidType:
        """Adds an object to the end of the Queue."""
    
    def Peek(self) -> NullableType[ObjectType]:
        """Returns the object at the beginning of the Queue without removing it."""
    
    @staticmethod
    def Synchronized(self, queue: Queue) -> Queue:
        """Returns a new Queue that wraps the original queue, and is thread safe."""
    
    def ToArray(self) -> ArrayType[NullableType[ObjectType]]:
        """Copies the Queue elements to a new array."""
    
    def TrimToSize(self) -> VoidType:
        """Sets the capacity to the actual number of elements in the Queue."""


class ReadOnlyCollectionBase(ABC, Object, ICollection):
    """Provides the abstract base class for a strongly typed non-generic
    read-only collection."""
    
    def __init__(self):
        """Initializes a new instance of the ReadOnlyCollectionBase class."""
    
    @property
    def InnerList(self) -> ArrayList:
        """Gets the list of elements contained in the ReadOnlyCollectionBase
        instance."""


class SortedList(Object, ICloneable, IDictionary):
    """Represents a collection of key/value pairs that are sorted by the keys
    and are accessible by key and by index."""
    
    @overload
    def __init__(self):
        """Initializes a new instance of the SortedList class that is empty,
        has the default initial capacity, and is sorted according to the
        IComparable interface implemented by each key added to the SortedList
        object."""
    
    @overload
    def __init__(self, comparer: NullableType[IComparer]):
        """Initializes a new instance of the SortedList class that is empty,
        has the default initial capacity, and is sorted according to the
        specified IComparer interface."""
    
    @overload
    def __init__(self, comparer: NullableType[IComparer], capacity: IntType):
        """Initializes a new instance of the SortedList class that is empty,
        has the specified initial capacity, and is sorted according to the
        specified IComparer interface."""
    
    @overload
    def __init__(self, d: IDictionary):
        """Initializes a new instance of the SortedList class that contains
        elements copied from the specified dictionary, has the same initial
        capacity as the number of elements copied, and is sorted according to
        the IComparable interface implemented by each key."""
    
    @overload
    def __init__(self, d: IDictionary, comparer: NullableType[IComparer]):
        """Initializes a new instance of the SortedList class that contains
        elements copied from the specified dictionary, has the same initial
        capacity as the number of elements copied, and is sorted according to
        the specified IComparer interface."""
    
    @overload
    def __init__(self, initialCapacity: IntType):
        """Initializes a new instance of the SortedList class that is empty,
        has the specified initial capacity, and is sorted according to the
        IComparable interface implemented by each key added to the SortedList
        object."""
    
    @property
    def Capacity(self) -> IntType:
        """Gets the capacity of a SortedList object."""
    
    @Capacity.setter
    def Capacity(self, value: IntType) -> VoidType:
        """Sets the capacity of a SortedList object."""
    
    def ContainsKey(self, key: ObjectType) -> BooleanType:
        """Determines whether a SortedList object contains a specific key."""
    
    def ContainsValue(self, value: NullableType[ObjectType]) -> BooleanType:
        """Determines whether a SortedList object contains a specific value."""
    
    def GetByIndex(self, index: IntType) -> NullableType[ObjectType]:
        """Gets the value at the specified index of a SortedList object."""
    
    def GetKey(self, index: IntType) -> ObjectType:
        """Gets the key at the specified index of a SortedList object."""
    
    def GetKeyList(self) -> IList:
        """Gets the keys in a SortedList object."""
    
    def GetValueList(self) -> IList:
        """Gets the values in a SortedList object."""
    
    def IndexOfKey(self, key: ObjectType) -> IntType:
        """Returns the zero-based index of the specified key in a
        SortedList object."""
    
    def IndexOfValue(self, value: NullableType[ObjectType]) -> IntType:
        """Returns the zero-based index of the first occurrence of the
        specified value in a SortedList object."""
    
    def RemoveAt(self, index: IntType) -> VoidType:
        """Removes the element at the specified index of a SortedList object."""
    
    def SetByIndex(self, index: IntType, value: NullableType[ObjectType]) -> VoidType:
        """Replaces the value at a specific index in a SortedList object."""
    
    @staticmethod
    def Synchronized(list: SortedList) -> SortedList:
        """Returns a synchronized (thread-safe) wrapper for a SortedList object."""
    
    def TrimToSize(self) -> VoidType:
        """Sets the capacity to the actual number of elements in a SortedList
        object."""


class Stack(Object, ICloneable, ICollection):
    """Represents a simple last-in-first-out (LIFO) non-generic collection
    of objects."""
    
    @overload
    def __init__(self):
        """Initializes a new instance of the Stack class that is empty and
        has the default initial capacity."""
    
    @overload
    def __init__(self, col: ICollection):
        """Initializes a new instance of the Stack class that contains
        elements copied from the specified collection and has the same
        initial capacity as the number of elements copied."""
    
    @overload
    def __init__(self, initialCapacity: IntType):
        """Initializes a new instance of the Stack class that is empty and
        has the specified initial capacity or the default initial capacity,
        whichever is greater."""
    
    def Clear(self) -> VoidType:
        """Removes all objects from the Stack."""
    
    def Contains(self, obj: NullableType[ObjectType]) -> BooleanType:
        """Determines whether an element is in the Stack."""
    
    def Peek(self) -> NullableType[ObjectType]:
        """Returns the object at the top of the Stack without removing it."""
    
    def Pop(self) -> NullableType[ObjectType]:
        """Removes and returns the object at the top of the Stack."""
    
    def Push(self, obj: NullableType[ObjectType]) -> VoidType:
        """Inserts an object at the top of the Stack."""
    
    @staticmethod
    def Synchronized(stack: Stack) -> Stack:
        """Returns a synchronized (thread safe) wrapper for the Stack."""
    
    def ToArray(self) -> ArrayType[NullableType[ObjectType]]:
        """Copies the Stack to a new array."""


class StructuralComparisons(Object):
    """Provides objects for performing a structural comparison of two
    collection objects."""
    
    @property
    def StructuralComparer(self) -> IComparer:
        """Gets a predefined object that performs a structural comparison
        of two objects."""
    
    @property
    def StructuralEqualityComparer(self) -> IEqualityComparer:
        """Gets a predefined object that compares two objects for structural
        equality."""


# ---------- STRUCTS ---------- #

class DictionaryEntry(ValueType):
    """Defines a dictionary key/value pair that can be set or retrieved."""
    
    def __init__(self, key: ObjectType, value: NullableType[ObjectType]):
        """Initializes an instance of the DictionaryEntry type with the
        specified key and value."""
    
    @property
    def Key(self) -> ObjectType:
        """Gets or sets the key in the key/value pair."""
    
    @Key.setter
    def Key(self, value: ObjectType) -> VoidType:
        """Gets or sets the key in the key/value pair."""
    
    @property
    def Value(self) -> NullableType[ObjectType]:
        """Gets or sets the value in the key/value pair."""
    
    @Value.setter
    def Value(self, value: NullableType[ObjectType]) -> VoidType:
        """Gets or sets the value in the key/value pair."""
    
    def Deconstruct(self, key: Object, value: NullableType[Object]) -> VoidType:
        """Deconstructs the current DictionaryEntry."""


# ---------- INTERFACES ---------- #

class ICollection(Protocol, IEnumerable):
    """Defines size, enumerators, and synchronization methods for all
    non-generic collections."""
    
    @property
    def Count(self) -> IntType:
        """Gets the number of elements contained in the ICollection."""
    
    @property
    def IsSynchronized(self) -> BooleanType:
        """Gets a value indicating whether access to the ICollection is
        synchronized (thread safe)."""
    
    @property
    def SyncRoot(self) -> ObjectType:
        """Gets an object that can be used to synchronize access to the
        ICollection."""
    
    def CopyTo(self, array: ArrayType, index: IntType) -> VoidType:
        """Copies the elements of the ICollection to an Array, starting at
        a particular Array index."""


class IComparer(Protocol):
    """Exposes a method that compares two objects."""
    
    def Compare(self, x: NullableType[ObjectType], y: NullableType[ObjectType]) -> IntType:
        """Compares two objects and returns a value indicating whether one
        is less than, equal to, or greater than the other."""


class IDictionary(Protocol, ICollection):
    """Represents a non-generic collection of key/value pairs."""
    
    @property
    def IsFixedSize(self) -> BooleanType:
        """Gets a value indicating whether the IDictionary object has a
        fixed size."""
    
    @property
    def IsReadOnly(self) -> BooleanType:
        """Gets a value indicating whether the IDictionary object is
        read-only."""
    
    @property
    def Item(self) -> Item[ObjectType, NullableType[ObjectType]]:
        """Gets or sets the element with the specified key."""
    
    def __getitem__(self, key: ObjectType) -> NullableType[ObjectType]: ...
    
    def __setitem__(self, key: ObjectType, value: NullableType[ObjectType]) -> VoidType: ...
    
    @property
    def Keys(self) -> ICollection:
        """Gets an ICollection object containing the keys of the IDictionary
        object."""
    
    @property
    def Values(self) -> ICollection:
        """Gets an ICollection object containing the values in the IDictionary
        object."""
    
    def Add(self, key: ObjectType, value: NullableType[ObjectType]) -> VoidType:
        """Adds an element with the provided key and value to the IDictionary
        object."""
    
    def Clear(self) -> VoidType:
        """Removes all elements from the IDictionary object."""
    
    def Contains(self, key: ObjectType) -> BooleanType:
        """Determines whether the IDictionary object contains an element
        with the specified key."""
    
    def GetEnumerator(self) -> IDictionaryEnumerator:
        """Returns an IDictionaryEnumerator object for the IDictionary
        object."""
    
    def Remove(self, key: ObjectType) -> VoidType:
        """Removes the element with the specified key from the IDictionary
        object."""


class IDictionaryEnumerator(Protocol, IEnumerator):
    """Enumerates the elements of a non-generic dictionary."""
    
    @property
    def Entry(self) -> DictionaryEntry:
        """Gets both the key and the value of the current dictionary entry."""
    
    @property
    def Key(self) -> ObjectType:
        """Gets the key of the current dictionary entry."""
    
    @property
    def Value(self) -> NullableType[ObjectType]:
        """Gets the value of the current dictionary entry."""


class IEnumerable(Protocol):
    """Exposes an enumerator, which supports a simple iteration over a
    non-generic collection."""
    
    def GetEnumerator(self) -> IEnumerator:
        """Returns an enumerator that iterates through a collection."""
    
    def Cast(self) -> Generic.IEnumerable[T]:
        """Casts the elements of an IEnumerable to the specified type."""
    
    def OfType(self) -> Generic.IEnumerable[T]:
        """Filters the elements of an IEnumerable based on a specified type."""
    
    def AsParallel(self) -> ParallelQuery:
        """Enables parallelization of a query."""
    
    def AsQueryable(self) -> IQueryable:
        """Converts an IEnumerable to an IQueryable."""


class IEnumerator(Protocol):
    """Supports a simple iteration over a non-generic collection."""
    
    @property
    def Current(self) -> ObjectType:
        """Gets the element in the collection at the current position of
        the enumerator."""
    
    def MoveNext(self) -> BooleanType:
        """Advances the enumerator to the next element of the collection."""
    
    def Reset(self) -> VoidType:
        """Sets the enumerator to its initial position, which is before the
        first element in the collection."""
    
    def __iter__(self) -> IEnumerator:
        return self
    
    def __next__(self) -> ObjectType: ...


class IEqualityComparer(Protocol):
    """Defines methods to support the comparison of objects for equality."""
    
    def Equals(self, x: NullableType[ObjectType], y: NullableType[ObjectType]) -> BooleanType:
        """Determines whether the specified objects are equal."""
    
    def GetHashCode(self, obj: ObjectType) -> IntType:
        """Returns a hash code for the specified object."""


class IHashCodeProvider(Protocol):
    """IHashCodeProvider has been deprecated. Use IEqualityComparer instead.
    
    Supplies a hash code for an object, using a custom hash function."""
    
    def __init__(self) -> Obsolete: ...
    
    def GetHashCode(self, obj: ObjectType) -> IntType:
        """Returns a hash code for the specified object."""


class IList(Protocol, ICollection):
    """Represents a non-generic collection of objects that can be
    individually accessed by index."""
    
    @property
    def IsFixedSize(self) -> BooleanType:
        """Gets a value indicating whether the IList has a fixed size."""
    
    @property
    def IsReadOnly(self) -> BooleanType:
        """Gets a value indicating whether the IList is read-only."""
    
    @property
    def Item(self) -> Item[IntType, NullableType[ObjectType]]:
        """Gets or sets the element at the specified index."""
    
    def __getitem__(self, key: IntType) -> NullableType[ObjectType]: ...
    
    def __setitem__(self, key: IntType, value: NullableType[ObjectType]) -> VoidType: ...
    
    def Add(self, value: NullableType[ObjectType]) -> IntType:
        """Adds an item to the IList."""
    
    def Clear(self) -> VoidType:
        """Removes all items from the IList."""
    
    def Contains(self, value: NullableType[ObjectType]) -> BooleanType:
        """Determines whether the IList contains a specific value."""
    
    def IndexOf(self, value: NullableType[ObjectType]) -> IntType:
        """Determines the index of a specific item in the IList."""
    
    def Insert(self, index: IntType, value: NullableType[ObjectType]) -> VoidType:
        """Inserts an item to the IList at the specified index."""
    
    def Remove(self, value: NullableType[ObjectType]) -> VoidType:
        """Removes the first occurrence of a specific object from the IList."""
    
    def RemoveAt(self, index: IntType) -> VoidType:
        """Removes the IList item at the specified index."""


class IStructuralComparable(Protocol):
    """Supports the structural comparison of collection objects."""
    
    def CompareTo(self, other: NullableType[ObjectType], comparer: IComparer) -> IntType:
        """Determines whether the current collection object precedes, occurs
        in the same position as, or follows another object in the sort
        order."""


class IStructuralEquatable(Protocol):
    """Defines methods to support the comparison of objects for structural
    equality."""
    
    def Equals(self, other: NullableType[ObjectType], comparer: IEqualityComparer) -> BooleanType:
        """Determines whether an object is structurally equal to the current
        instance."""
    
    def GetHashCode(self, comparer: IEqualityComparer) -> IntType:
        """Returns a hash code for the current instance."""
