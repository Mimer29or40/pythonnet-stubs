from __future__ import annotations

from abc import ABC
from typing import List, Union, overload

from Microsoft.Win32.SafeHandles import SafeHandleZeroOrMinusOneIsInvalid
from System import Array, Boolean, Byte, Enum, IDisposable, Int32, IntPtr, Object, String, Void
from System.Collections import ICollection, IEnumerable, IEnumerator

# ---------- Types ---------- #

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
ByteType = Union[int, Byte]
IntType = Union[int, Int32]
NIntType = Union[int, IntPtr]
ObjectType = Object
StringType = Union[str, String]
VoidType = Union[None, Void]

# ---------- Classes ---------- #

class AsnEncodedData(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, rawData: ArrayType[ByteType]): ...
    
    @overload
    def __init__(self, oid: StringType, rawData: ArrayType[ByteType]): ...
    
    @overload
    def __init__(self, oid: Oid, rawData: ArrayType[ByteType]): ...
    
    @overload
    def __init__(self, asnEncodedData: AsnEncodedData): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Oid(self) -> Oid: ...
    
    @Oid.setter
    def Oid(self, value: Oid) -> None: ...
    
    @property
    def RawData(self) -> ArrayType[ByteType]: ...
    
    @RawData.setter
    def RawData(self, value: ArrayType[ByteType]) -> None: ...
    
    # ---------- Methods ---------- #
    
    def CopyFrom(self, asnEncodedData: AsnEncodedData) -> VoidType: ...
    
    def Format(self, multiLine: BooleanType) -> StringType: ...
    
    def get_Oid(self) -> Oid: ...
    
    def get_RawData(self) -> ArrayType[ByteType]: ...
    
    def set_Oid(self, value: Oid) -> VoidType: ...
    
    def set_RawData(self, value: ArrayType[ByteType]) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AsnEncodedDataCollection(ObjectType, ICollection, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, asnEncodedData: AsnEncodedData): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def IsSynchronized(self) -> BooleanType: ...
    
    @property
    def Item(self) -> AsnEncodedData: ...
    
    @property
    def SyncRoot(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def Add(self, asnEncodedData: AsnEncodedData) -> IntType: ...
    
    def CopyTo(self, array: ArrayType[AsnEncodedData], index: IntType) -> VoidType: ...
    
    def GetEnumerator(self) -> AsnEncodedDataEnumerator: ...
    
    def Remove(self, asnEncodedData: AsnEncodedData) -> VoidType: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_IsSynchronized(self) -> BooleanType: ...
    
    def get_Item(self, index: IntType) -> AsnEncodedData: ...
    
    def get_SyncRoot(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AsnEncodedDataEnumerator(ObjectType, IEnumerator):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Current(self) -> AsnEncodedData: ...
    
    # ---------- Methods ---------- #
    
    def MoveNext(self) -> BooleanType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Current(self) -> AsnEncodedData: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class BigInt(ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    @staticmethod
    def op_Equality(value1: BigInt, value2: BigInt) -> BooleanType: ...
    
    @staticmethod
    def op_GreaterThan(value1: BigInt, value2: BigInt) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(value1: BigInt, value2: BigInt) -> BooleanType: ...
    
    @staticmethod
    def op_LessThan(value1: BigInt, value2: BigInt) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CAPI(CAPIMethods):
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


class CAPIBase(ABC, ObjectType):
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


class CAPIMethods(ABC, CAPIUnsafe):
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


class CAPINative(ABC, CAPIBase):
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


class CAPISafe(ABC, CAPINative):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def FreeLibrary(hModule: NIntType) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CAPIUnsafe(ABC, CAPISafe):
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


class Oid(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, oid: StringType): ...
    
    @overload
    def __init__(self, value: StringType, friendlyName: StringType): ...
    
    @overload
    def __init__(self, oid: Oid): ...
    
    # ---------- Properties ---------- #
    
    @property
    def FriendlyName(self) -> StringType: ...
    
    @FriendlyName.setter
    def FriendlyName(self, value: StringType) -> None: ...
    
    @property
    def Value(self) -> StringType: ...
    
    @Value.setter
    def Value(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def FromFriendlyName(friendlyName: StringType, group: OidGroup) -> Oid: ...
    
    @staticmethod
    def FromOidValue(oidValue: StringType, group: OidGroup) -> Oid: ...
    
    def get_FriendlyName(self) -> StringType: ...
    
    def get_Value(self) -> StringType: ...
    
    def set_FriendlyName(self, value: StringType) -> VoidType: ...
    
    def set_Value(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class OidCollection(ObjectType, ICollection, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def IsSynchronized(self) -> BooleanType: ...
    
    @property
    def Item(self) -> Oid: ...
    
    @property
    def Item(self) -> Oid: ...
    
    @property
    def SyncRoot(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def Add(self, oid: Oid) -> IntType: ...
    
    def CopyTo(self, array: ArrayType[Oid], index: IntType) -> VoidType: ...
    
    def GetEnumerator(self) -> OidEnumerator: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_IsSynchronized(self) -> BooleanType: ...
    
    @overload
    def get_Item(self, index: IntType) -> Oid: ...
    
    @overload
    def get_Item(self, oid: StringType) -> Oid: ...
    
    def get_SyncRoot(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class OidEnumerator(ObjectType, IEnumerator):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Current(self) -> Oid: ...
    
    # ---------- Methods ---------- #
    
    def MoveNext(self) -> BooleanType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Current(self) -> Oid: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SafeCertContextHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
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


class SafeCertStoreHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
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


class SafeCryptMsgHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
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


class SafeCryptProvHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
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


class SafeLibraryHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
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


class SafeLocalAllocHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
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


# No Structs

# No Interfaces

# ---------- Enums ---------- #

class OidGroup(Enum):
    All: IntType = 0
    HashAlgorithm: IntType = 1
    EncryptionAlgorithm: IntType = 2
    PublicKeyAlgorithm: IntType = 3
    SignatureAlgorithm: IntType = 4
    Attribute: IntType = 5
    ExtensionOrAttribute: IntType = 6
    EnhancedKeyUsage: IntType = 7
    Policy: IntType = 8
    Template: IntType = 9
    KeyDerivationFunction: IntType = 10


# No Delegates

__all__ = [
    AsnEncodedData,
    AsnEncodedDataCollection,
    AsnEncodedDataEnumerator,
    BigInt,
    CAPI,
    CAPIBase,
    CAPIMethods,
    CAPINative,
    CAPISafe,
    CAPIUnsafe,
    Oid,
    OidCollection,
    OidEnumerator,
    SafeCertContextHandle,
    SafeCertStoreHandle,
    SafeCryptMsgHandle,
    SafeCryptProvHandle,
    SafeLibraryHandle,
    SafeLocalAllocHandle,
    OidGroup,
]
