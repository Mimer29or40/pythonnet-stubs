from __future__ import annotations

from abc import ABC
from typing import List, Protocol, TypeVar, Union, overload

from Microsoft.Win32.SafeHandles import SafeAccessTokenHandle
from System import Action, Array, Boolean, Byte, Enum, Exception, Func, IComparable, IDisposable, Int32, Int64, IntPtr, Object, String, SystemException, Type, Void
from System.Collections import IEnumerable, IEnumerator
from System.Collections.Generic import ICollection, IEnumerable, IEnumerator
from System.Runtime.InteropServices import _Exception
from System.Runtime.Serialization import IDeserializationCallback, ISerializable, SerializationInfo, StreamingContext
from System.Security.Claims import Claim, ClaimsIdentity, ClaimsPrincipal

# ---------- Types ---------- #

T = TypeVar('T')

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
ByteType = Union[int, Byte]
IntType = Union[int, Int32]
LongType = Union[int, Int64]
NIntType = Union[int, IntPtr]
ObjectType = Object
StringType = Union[str, String]
TypeType = Union[type, Type]
VoidType = Union[None, Void]


# ---------- Classes ---------- #

class GenericIdentity(ClaimsIdentity, IIdentity):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, name: StringType): ...
    
    @overload
    def __init__(self, name: StringType, type: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AuthenticationType(self) -> StringType: ...
    
    @property
    def Claims(self) -> IEnumerable[Claim]: ...
    
    @property
    def IsAuthenticated(self) -> BooleanType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> ClaimsIdentity: ...
    
    def get_AuthenticationType(self) -> StringType: ...
    
    def get_Claims(self) -> IEnumerable[Claim]: ...
    
    def get_IsAuthenticated(self) -> BooleanType: ...
    
    def get_Name(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class GenericIdentity(ClaimsIdentity, IIdentity):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, name: StringType): ...
    
    @overload
    def __init__(self, name: StringType, type: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AuthenticationType(self) -> StringType: ...
    
    @property
    def Claims(self) -> IEnumerable[Claim]: ...
    
    @property
    def IsAuthenticated(self) -> BooleanType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> ClaimsIdentity: ...
    
    def get_AuthenticationType(self) -> StringType: ...
    
    def get_Claims(self) -> IEnumerable[Claim]: ...
    
    def get_IsAuthenticated(self) -> BooleanType: ...
    
    def get_Name(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class GenericIdentity(ClaimsIdentity, IIdentity):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, name: StringType): ...
    
    @overload
    def __init__(self, name: StringType, type: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AuthenticationType(self) -> StringType: ...
    
    @property
    def Claims(self) -> IEnumerable[Claim]: ...
    
    @property
    def IsAuthenticated(self) -> BooleanType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> ClaimsIdentity: ...
    
    def get_AuthenticationType(self) -> StringType: ...
    
    def get_Claims(self) -> IEnumerable[Claim]: ...
    
    def get_IsAuthenticated(self) -> BooleanType: ...
    
    def get_Name(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class GenericPrincipal(ClaimsPrincipal, IPrincipal):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, identity: IIdentity, roles: ArrayType[StringType]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Identity(self) -> IIdentity: ...
    
    # ---------- Methods ---------- #
    
    def IsInRole(self, role: StringType) -> BooleanType: ...
    
    def get_Identity(self) -> IIdentity: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class GenericPrincipal(ClaimsPrincipal, IPrincipal):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, identity: IIdentity, roles: ArrayType[StringType]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Identity(self) -> IIdentity: ...
    
    # ---------- Methods ---------- #
    
    def IsInRole(self, role: StringType) -> BooleanType: ...
    
    def get_Identity(self) -> IIdentity: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class GenericPrincipal(ClaimsPrincipal, IPrincipal):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, identity: IIdentity, roles: ArrayType[StringType]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Identity(self) -> IIdentity: ...
    
    # ---------- Methods ---------- #
    
    def IsInRole(self, role: StringType) -> BooleanType: ...
    
    def get_Identity(self) -> IIdentity: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class IdentityNotMappedException(SystemException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, inner: Exception): ...
    
    # ---------- Properties ---------- #
    
    @property
    def UnmappedIdentities(self) -> IdentityReferenceCollection: ...
    
    # ---------- Methods ---------- #
    
    def GetObjectData(self, serializationInfo: SerializationInfo, streamingContext: StreamingContext) -> VoidType: ...
    
    def get_UnmappedIdentities(self) -> IdentityReferenceCollection: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class IdentityNotMappedException(SystemException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, inner: Exception): ...
    
    # ---------- Properties ---------- #
    
    @property
    def UnmappedIdentities(self) -> IdentityReferenceCollection: ...
    
    # ---------- Methods ---------- #
    
    def GetObjectData(self, serializationInfo: SerializationInfo, streamingContext: StreamingContext) -> VoidType: ...
    
    def get_UnmappedIdentities(self) -> IdentityReferenceCollection: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class IdentityNotMappedException(SystemException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, inner: Exception): ...
    
    # ---------- Properties ---------- #
    
    @property
    def UnmappedIdentities(self) -> IdentityReferenceCollection: ...
    
    # ---------- Methods ---------- #
    
    def GetObjectData(self, serializationInfo: SerializationInfo, streamingContext: StreamingContext) -> VoidType: ...
    
    def get_UnmappedIdentities(self) -> IdentityReferenceCollection: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class IdentityReference(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def IsValidTargetType(self, targetType: TypeType) -> BooleanType: ...
    
    def ToString(self) -> StringType: ...
    
    def Translate(self, targetType: TypeType) -> IdentityReference: ...
    
    def get_Value(self) -> StringType: ...
    
    @staticmethod
    def op_Equality(left: IdentityReference, right: IdentityReference) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(left: IdentityReference, right: IdentityReference) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class IdentityReference(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def IsValidTargetType(self, targetType: TypeType) -> BooleanType: ...
    
    def ToString(self) -> StringType: ...
    
    def Translate(self, targetType: TypeType) -> IdentityReference: ...
    
    def get_Value(self) -> StringType: ...
    
    @staticmethod
    def op_Equality(left: IdentityReference, right: IdentityReference) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(left: IdentityReference, right: IdentityReference) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class IdentityReference(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def IsValidTargetType(self, targetType: TypeType) -> BooleanType: ...
    
    def ToString(self) -> StringType: ...
    
    def Translate(self, targetType: TypeType) -> IdentityReference: ...
    
    def get_Value(self) -> StringType: ...
    
    @staticmethod
    def op_Equality(left: IdentityReference, right: IdentityReference) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(left: IdentityReference, right: IdentityReference) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class IdentityReferenceCollection(ObjectType, ICollection[IdentityReference], IEnumerable[IdentityReference], IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, capacity: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def IsReadOnly(self) -> BooleanType: ...
    
    def __getitem__(self, key: IntType) -> IdentityReference: ...
    
    def __setitem__(self, key: IntType, value: IdentityReference) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Add(self, identity: IdentityReference) -> VoidType: ...
    
    def Clear(self) -> VoidType: ...
    
    def Contains(self, identity: IdentityReference) -> BooleanType: ...
    
    def CopyTo(self, array: ArrayType[IdentityReference], offset: IntType) -> VoidType: ...
    
    def GetEnumerator(self) -> IEnumerator[IdentityReference]: ...
    
    def Remove(self, identity: IdentityReference) -> BooleanType: ...
    
    @overload
    def Translate(self, targetType: TypeType) -> IdentityReferenceCollection: ...
    
    @overload
    def Translate(self, targetType: TypeType, forceSuccess: BooleanType) -> IdentityReferenceCollection: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_IsReadOnly(self) -> BooleanType: ...
    
    def get_Item(self, index: IntType) -> IdentityReference: ...
    
    def set_Item(self, index: IntType, value: IdentityReference) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class IdentityReferenceCollection(ObjectType, ICollection[IdentityReference], IEnumerable[IdentityReference], IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, capacity: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def IsReadOnly(self) -> BooleanType: ...
    
    def __getitem__(self, key: IntType) -> IdentityReference: ...
    
    def __setitem__(self, key: IntType, value: IdentityReference) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Add(self, identity: IdentityReference) -> VoidType: ...
    
    def Clear(self) -> VoidType: ...
    
    def Contains(self, identity: IdentityReference) -> BooleanType: ...
    
    def CopyTo(self, array: ArrayType[IdentityReference], offset: IntType) -> VoidType: ...
    
    def GetEnumerator(self) -> IEnumerator[IdentityReference]: ...
    
    def Remove(self, identity: IdentityReference) -> BooleanType: ...
    
    @overload
    def Translate(self, targetType: TypeType) -> IdentityReferenceCollection: ...
    
    @overload
    def Translate(self, targetType: TypeType, forceSuccess: BooleanType) -> IdentityReferenceCollection: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_IsReadOnly(self) -> BooleanType: ...
    
    def get_Item(self, index: IntType) -> IdentityReference: ...
    
    def set_Item(self, index: IntType, value: IdentityReference) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class IdentityReferenceCollection(ObjectType, ICollection[IdentityReference], IEnumerable[IdentityReference], IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, capacity: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def IsReadOnly(self) -> BooleanType: ...
    
    def __getitem__(self, key: IntType) -> IdentityReference: ...
    
    def __setitem__(self, key: IntType, value: IdentityReference) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Add(self, identity: IdentityReference) -> VoidType: ...
    
    def Clear(self) -> VoidType: ...
    
    def Contains(self, identity: IdentityReference) -> BooleanType: ...
    
    def CopyTo(self, array: ArrayType[IdentityReference], offset: IntType) -> VoidType: ...
    
    def GetEnumerator(self) -> IEnumerator[IdentityReference]: ...
    
    def Remove(self, identity: IdentityReference) -> BooleanType: ...
    
    @overload
    def Translate(self, targetType: TypeType) -> IdentityReferenceCollection: ...
    
    @overload
    def Translate(self, targetType: TypeType, forceSuccess: BooleanType) -> IdentityReferenceCollection: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_IsReadOnly(self) -> BooleanType: ...
    
    def get_Item(self, index: IntType) -> IdentityReference: ...
    
    def set_Item(self, index: IntType, value: IdentityReference) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class IdentityReferenceEnumerator(ObjectType, IEnumerator[IdentityReference], IDisposable, IEnumerator):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Current(self) -> IdentityReference: ...
    
    # ---------- Methods ---------- #
    
    def Dispose(self) -> VoidType: ...
    
    def MoveNext(self) -> BooleanType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Current(self) -> IdentityReference: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class IdentityReferenceEnumerator(ObjectType, IEnumerator[IdentityReference], IDisposable, IEnumerator):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Current(self) -> IdentityReference: ...
    
    # ---------- Methods ---------- #
    
    def Dispose(self) -> VoidType: ...
    
    def MoveNext(self) -> BooleanType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Current(self) -> IdentityReference: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class IdentityReferenceEnumerator(ObjectType, IEnumerator[IdentityReference], IDisposable, IEnumerator):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Current(self) -> IdentityReference: ...
    
    # ---------- Methods ---------- #
    
    def Dispose(self) -> VoidType: ...
    
    def MoveNext(self) -> BooleanType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Current(self) -> IdentityReference: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class NTAccount(IdentityReference):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, domainName: StringType, accountName: StringType): ...
    
    @overload
    def __init__(self, name: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def IsValidTargetType(self, targetType: TypeType) -> BooleanType: ...
    
    def ToString(self) -> StringType: ...
    
    def Translate(self, targetType: TypeType) -> IdentityReference: ...
    
    def get_Value(self) -> StringType: ...
    
    @staticmethod
    def op_Equality(left: NTAccount, right: NTAccount) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(left: NTAccount, right: NTAccount) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class NTAccount(IdentityReference):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, domainName: StringType, accountName: StringType): ...
    
    @overload
    def __init__(self, name: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def IsValidTargetType(self, targetType: TypeType) -> BooleanType: ...
    
    def ToString(self) -> StringType: ...
    
    def Translate(self, targetType: TypeType) -> IdentityReference: ...
    
    def get_Value(self) -> StringType: ...
    
    @staticmethod
    def op_Equality(left: NTAccount, right: NTAccount) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(left: NTAccount, right: NTAccount) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class NTAccount(IdentityReference):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, domainName: StringType, accountName: StringType): ...
    
    @overload
    def __init__(self, name: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def IsValidTargetType(self, targetType: TypeType) -> BooleanType: ...
    
    def ToString(self) -> StringType: ...
    
    def Translate(self, targetType: TypeType) -> IdentityReference: ...
    
    def get_Value(self) -> StringType: ...
    
    @staticmethod
    def op_Equality(left: NTAccount, right: NTAccount) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(left: NTAccount, right: NTAccount) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SecurityIdentifier(IdentityReference, IComparable[SecurityIdentifier]):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def MaxBinaryLength() -> IntType: ...
    
    @staticmethod
    @property
    def MinBinaryLength() -> IntType: ...
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, sddlForm: StringType): ...
    
    @overload
    def __init__(self, binaryForm: ArrayType[ByteType], offset: IntType): ...
    
    @overload
    def __init__(self, binaryForm: NIntType): ...
    
    @overload
    def __init__(self, sidType: WellKnownSidType, domainSid: SecurityIdentifier): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AccountDomainSid(self) -> SecurityIdentifier: ...
    
    @property
    def BinaryLength(self) -> IntType: ...
    
    @property
    def Value(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def CompareTo(self, sid: SecurityIdentifier) -> IntType: ...
    
    @overload
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, sid: SecurityIdentifier) -> BooleanType: ...
    
    def GetBinaryForm(self, binaryForm: ArrayType[ByteType], offset: IntType) -> VoidType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def IsAccountSid(self) -> BooleanType: ...
    
    def IsEqualDomainSid(self, sid: SecurityIdentifier) -> BooleanType: ...
    
    def IsValidTargetType(self, targetType: TypeType) -> BooleanType: ...
    
    def IsWellKnown(self, type: WellKnownSidType) -> BooleanType: ...
    
    def ToString(self) -> StringType: ...
    
    def Translate(self, targetType: TypeType) -> IdentityReference: ...
    
    def get_AccountDomainSid(self) -> SecurityIdentifier: ...
    
    def get_BinaryLength(self) -> IntType: ...
    
    def get_Value(self) -> StringType: ...
    
    @staticmethod
    def op_Equality(left: SecurityIdentifier, right: SecurityIdentifier) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(left: SecurityIdentifier, right: SecurityIdentifier) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SecurityIdentifier(IdentityReference, IComparable[SecurityIdentifier]):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def MaxBinaryLength() -> IntType: ...
    
    @staticmethod
    @property
    def MinBinaryLength() -> IntType: ...
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, sddlForm: StringType): ...
    
    @overload
    def __init__(self, binaryForm: ArrayType[ByteType], offset: IntType): ...
    
    @overload
    def __init__(self, binaryForm: NIntType): ...
    
    @overload
    def __init__(self, sidType: WellKnownSidType, domainSid: SecurityIdentifier): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AccountDomainSid(self) -> SecurityIdentifier: ...
    
    @property
    def BinaryLength(self) -> IntType: ...
    
    @property
    def Value(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def CompareTo(self, sid: SecurityIdentifier) -> IntType: ...
    
    @overload
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, sid: SecurityIdentifier) -> BooleanType: ...
    
    def GetBinaryForm(self, binaryForm: ArrayType[ByteType], offset: IntType) -> VoidType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def IsAccountSid(self) -> BooleanType: ...
    
    def IsEqualDomainSid(self, sid: SecurityIdentifier) -> BooleanType: ...
    
    def IsValidTargetType(self, targetType: TypeType) -> BooleanType: ...
    
    def IsWellKnown(self, type: WellKnownSidType) -> BooleanType: ...
    
    def ToString(self) -> StringType: ...
    
    def Translate(self, targetType: TypeType) -> IdentityReference: ...
    
    def get_AccountDomainSid(self) -> SecurityIdentifier: ...
    
    def get_BinaryLength(self) -> IntType: ...
    
    def get_Value(self) -> StringType: ...
    
    @staticmethod
    def op_Equality(left: SecurityIdentifier, right: SecurityIdentifier) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(left: SecurityIdentifier, right: SecurityIdentifier) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SecurityIdentifier(IdentityReference, IComparable[SecurityIdentifier]):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def MaxBinaryLength() -> IntType: ...
    
    @staticmethod
    @property
    def MinBinaryLength() -> IntType: ...
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, sddlForm: StringType): ...
    
    @overload
    def __init__(self, binaryForm: ArrayType[ByteType], offset: IntType): ...
    
    @overload
    def __init__(self, binaryForm: NIntType): ...
    
    @overload
    def __init__(self, sidType: WellKnownSidType, domainSid: SecurityIdentifier): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AccountDomainSid(self) -> SecurityIdentifier: ...
    
    @property
    def BinaryLength(self) -> IntType: ...
    
    @property
    def Value(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def CompareTo(self, sid: SecurityIdentifier) -> IntType: ...
    
    @overload
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, sid: SecurityIdentifier) -> BooleanType: ...
    
    def GetBinaryForm(self, binaryForm: ArrayType[ByteType], offset: IntType) -> VoidType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def IsAccountSid(self) -> BooleanType: ...
    
    def IsEqualDomainSid(self, sid: SecurityIdentifier) -> BooleanType: ...
    
    def IsValidTargetType(self, targetType: TypeType) -> BooleanType: ...
    
    def IsWellKnown(self, type: WellKnownSidType) -> BooleanType: ...
    
    def ToString(self) -> StringType: ...
    
    def Translate(self, targetType: TypeType) -> IdentityReference: ...
    
    def get_AccountDomainSid(self) -> SecurityIdentifier: ...
    
    def get_BinaryLength(self) -> IntType: ...
    
    def get_Value(self) -> StringType: ...
    
    @staticmethod
    def op_Equality(left: SecurityIdentifier, right: SecurityIdentifier) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(left: SecurityIdentifier, right: SecurityIdentifier) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Win32(ABC, ObjectType):
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


class Win32(ABC, ObjectType):
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


class Win32(ABC, ObjectType):
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


class WindowsIdentity(ClaimsIdentity, IIdentity, ISerializable, IDeserializationCallback, IDisposable):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def DefaultIssuer() -> StringType: ...
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, userToken: NIntType): ...
    
    @overload
    def __init__(self, userToken: NIntType, type: StringType): ...
    
    @overload
    def __init__(self, userToken: NIntType, type: StringType, acctType: WindowsAccountType): ...
    
    @overload
    def __init__(self, userToken: NIntType, type: StringType, acctType: WindowsAccountType, isAuthenticated: BooleanType): ...
    
    @overload
    def __init__(self, sUserPrincipalName: StringType): ...
    
    @overload
    def __init__(self, sUserPrincipalName: StringType, type: StringType): ...
    
    @overload
    def __init__(self, info: SerializationInfo, context: StreamingContext): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AccessToken(self) -> SafeAccessTokenHandle: ...
    
    @property
    def AuthenticationType(self) -> StringType: ...
    
    @property
    def Claims(self) -> IEnumerable[Claim]: ...
    
    @property
    def DeviceClaims(self) -> IEnumerable[Claim]: ...
    
    @property
    def Groups(self) -> IdentityReferenceCollection: ...
    
    @property
    def ImpersonationLevel(self) -> TokenImpersonationLevel: ...
    
    @property
    def IsAnonymous(self) -> BooleanType: ...
    
    @property
    def IsAuthenticated(self) -> BooleanType: ...
    
    @property
    def IsGuest(self) -> BooleanType: ...
    
    @property
    def IsSystem(self) -> BooleanType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def Owner(self) -> SecurityIdentifier: ...
    
    @property
    def Token(self) -> NIntType: ...
    
    @property
    def User(self) -> SecurityIdentifier: ...
    
    @property
    def UserClaims(self) -> IEnumerable[Claim]: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> ClaimsIdentity: ...
    
    def Dispose(self) -> VoidType: ...
    
    @staticmethod
    def GetAnonymous() -> WindowsIdentity: ...
    
    @staticmethod
    @overload
    def GetCurrent() -> WindowsIdentity: ...
    
    @staticmethod
    @overload
    def GetCurrent(ifImpersonating: BooleanType) -> WindowsIdentity: ...
    
    @staticmethod
    @overload
    def GetCurrent(desiredAccess: TokenAccessLevels) -> WindowsIdentity: ...
    
    @overload
    def Impersonate(self) -> WindowsImpersonationContext: ...
    
    @staticmethod
    @overload
    def Impersonate(userToken: NIntType) -> WindowsImpersonationContext: ...
    
    @staticmethod
    @overload
    def RunImpersonated(safeAccessTokenHandle: SafeAccessTokenHandle, action: Action) -> VoidType: ...
    
    @staticmethod
    @overload
    def RunImpersonated(safeAccessTokenHandle: SafeAccessTokenHandle, func: Func[T]) -> T: ...
    
    def get_AccessToken(self) -> SafeAccessTokenHandle: ...
    
    def get_AuthenticationType(self) -> StringType: ...
    
    def get_Claims(self) -> IEnumerable[Claim]: ...
    
    def get_DeviceClaims(self) -> IEnumerable[Claim]: ...
    
    def get_Groups(self) -> IdentityReferenceCollection: ...
    
    def get_ImpersonationLevel(self) -> TokenImpersonationLevel: ...
    
    def get_IsAnonymous(self) -> BooleanType: ...
    
    def get_IsAuthenticated(self) -> BooleanType: ...
    
    def get_IsGuest(self) -> BooleanType: ...
    
    def get_IsSystem(self) -> BooleanType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_Owner(self) -> SecurityIdentifier: ...
    
    def get_Token(self) -> NIntType: ...
    
    def get_User(self) -> SecurityIdentifier: ...
    
    def get_UserClaims(self) -> IEnumerable[Claim]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class WindowsIdentity(ClaimsIdentity, IIdentity, ISerializable, IDeserializationCallback, IDisposable):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def DefaultIssuer() -> StringType: ...
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, userToken: NIntType): ...
    
    @overload
    def __init__(self, userToken: NIntType, type: StringType): ...
    
    @overload
    def __init__(self, userToken: NIntType, type: StringType, acctType: WindowsAccountType): ...
    
    @overload
    def __init__(self, userToken: NIntType, type: StringType, acctType: WindowsAccountType, isAuthenticated: BooleanType): ...
    
    @overload
    def __init__(self, sUserPrincipalName: StringType): ...
    
    @overload
    def __init__(self, sUserPrincipalName: StringType, type: StringType): ...
    
    @overload
    def __init__(self, info: SerializationInfo, context: StreamingContext): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AccessToken(self) -> SafeAccessTokenHandle: ...
    
    @property
    def AuthenticationType(self) -> StringType: ...
    
    @property
    def Claims(self) -> IEnumerable[Claim]: ...
    
    @property
    def DeviceClaims(self) -> IEnumerable[Claim]: ...
    
    @property
    def Groups(self) -> IdentityReferenceCollection: ...
    
    @property
    def ImpersonationLevel(self) -> TokenImpersonationLevel: ...
    
    @property
    def IsAnonymous(self) -> BooleanType: ...
    
    @property
    def IsAuthenticated(self) -> BooleanType: ...
    
    @property
    def IsGuest(self) -> BooleanType: ...
    
    @property
    def IsSystem(self) -> BooleanType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def Owner(self) -> SecurityIdentifier: ...
    
    @property
    def Token(self) -> NIntType: ...
    
    @property
    def User(self) -> SecurityIdentifier: ...
    
    @property
    def UserClaims(self) -> IEnumerable[Claim]: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> ClaimsIdentity: ...
    
    def Dispose(self) -> VoidType: ...
    
    @staticmethod
    def GetAnonymous() -> WindowsIdentity: ...
    
    @staticmethod
    @overload
    def GetCurrent() -> WindowsIdentity: ...
    
    @staticmethod
    @overload
    def GetCurrent(ifImpersonating: BooleanType) -> WindowsIdentity: ...
    
    @staticmethod
    @overload
    def GetCurrent(desiredAccess: TokenAccessLevels) -> WindowsIdentity: ...
    
    @overload
    def Impersonate(self) -> WindowsImpersonationContext: ...
    
    @staticmethod
    @overload
    def Impersonate(userToken: NIntType) -> WindowsImpersonationContext: ...
    
    @staticmethod
    @overload
    def RunImpersonated(safeAccessTokenHandle: SafeAccessTokenHandle, action: Action) -> VoidType: ...
    
    @staticmethod
    @overload
    def RunImpersonated(safeAccessTokenHandle: SafeAccessTokenHandle, func: Func[T]) -> T: ...
    
    def get_AccessToken(self) -> SafeAccessTokenHandle: ...
    
    def get_AuthenticationType(self) -> StringType: ...
    
    def get_Claims(self) -> IEnumerable[Claim]: ...
    
    def get_DeviceClaims(self) -> IEnumerable[Claim]: ...
    
    def get_Groups(self) -> IdentityReferenceCollection: ...
    
    def get_ImpersonationLevel(self) -> TokenImpersonationLevel: ...
    
    def get_IsAnonymous(self) -> BooleanType: ...
    
    def get_IsAuthenticated(self) -> BooleanType: ...
    
    def get_IsGuest(self) -> BooleanType: ...
    
    def get_IsSystem(self) -> BooleanType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_Owner(self) -> SecurityIdentifier: ...
    
    def get_Token(self) -> NIntType: ...
    
    def get_User(self) -> SecurityIdentifier: ...
    
    def get_UserClaims(self) -> IEnumerable[Claim]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class WindowsIdentity(ClaimsIdentity, IIdentity, ISerializable, IDeserializationCallback, IDisposable):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def DefaultIssuer() -> StringType: ...
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, userToken: NIntType): ...
    
    @overload
    def __init__(self, userToken: NIntType, type: StringType): ...
    
    @overload
    def __init__(self, userToken: NIntType, type: StringType, acctType: WindowsAccountType): ...
    
    @overload
    def __init__(self, userToken: NIntType, type: StringType, acctType: WindowsAccountType, isAuthenticated: BooleanType): ...
    
    @overload
    def __init__(self, sUserPrincipalName: StringType): ...
    
    @overload
    def __init__(self, sUserPrincipalName: StringType, type: StringType): ...
    
    @overload
    def __init__(self, info: SerializationInfo, context: StreamingContext): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AccessToken(self) -> SafeAccessTokenHandle: ...
    
    @property
    def AuthenticationType(self) -> StringType: ...
    
    @property
    def Claims(self) -> IEnumerable[Claim]: ...
    
    @property
    def DeviceClaims(self) -> IEnumerable[Claim]: ...
    
    @property
    def Groups(self) -> IdentityReferenceCollection: ...
    
    @property
    def ImpersonationLevel(self) -> TokenImpersonationLevel: ...
    
    @property
    def IsAnonymous(self) -> BooleanType: ...
    
    @property
    def IsAuthenticated(self) -> BooleanType: ...
    
    @property
    def IsGuest(self) -> BooleanType: ...
    
    @property
    def IsSystem(self) -> BooleanType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def Owner(self) -> SecurityIdentifier: ...
    
    @property
    def Token(self) -> NIntType: ...
    
    @property
    def User(self) -> SecurityIdentifier: ...
    
    @property
    def UserClaims(self) -> IEnumerable[Claim]: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> ClaimsIdentity: ...
    
    def Dispose(self) -> VoidType: ...
    
    @staticmethod
    def GetAnonymous() -> WindowsIdentity: ...
    
    @staticmethod
    @overload
    def GetCurrent() -> WindowsIdentity: ...
    
    @staticmethod
    @overload
    def GetCurrent(ifImpersonating: BooleanType) -> WindowsIdentity: ...
    
    @staticmethod
    @overload
    def GetCurrent(desiredAccess: TokenAccessLevels) -> WindowsIdentity: ...
    
    @overload
    def Impersonate(self) -> WindowsImpersonationContext: ...
    
    @staticmethod
    @overload
    def Impersonate(userToken: NIntType) -> WindowsImpersonationContext: ...
    
    @staticmethod
    @overload
    def RunImpersonated(safeAccessTokenHandle: SafeAccessTokenHandle, action: Action) -> VoidType: ...
    
    @staticmethod
    @overload
    def RunImpersonated(safeAccessTokenHandle: SafeAccessTokenHandle, func: Func[T]) -> T: ...
    
    def get_AccessToken(self) -> SafeAccessTokenHandle: ...
    
    def get_AuthenticationType(self) -> StringType: ...
    
    def get_Claims(self) -> IEnumerable[Claim]: ...
    
    def get_DeviceClaims(self) -> IEnumerable[Claim]: ...
    
    def get_Groups(self) -> IdentityReferenceCollection: ...
    
    def get_ImpersonationLevel(self) -> TokenImpersonationLevel: ...
    
    def get_IsAnonymous(self) -> BooleanType: ...
    
    def get_IsAuthenticated(self) -> BooleanType: ...
    
    def get_IsGuest(self) -> BooleanType: ...
    
    def get_IsSystem(self) -> BooleanType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_Owner(self) -> SecurityIdentifier: ...
    
    def get_Token(self) -> NIntType: ...
    
    def get_User(self) -> SecurityIdentifier: ...
    
    def get_UserClaims(self) -> IEnumerable[Claim]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class WindowsImpersonationContext(ObjectType, IDisposable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Dispose(self) -> VoidType: ...
    
    def Undo(self) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class WindowsImpersonationContext(ObjectType, IDisposable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Dispose(self) -> VoidType: ...
    
    def Undo(self) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class WindowsImpersonationContext(ObjectType, IDisposable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Dispose(self) -> VoidType: ...
    
    def Undo(self) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class WindowsPrincipal(ClaimsPrincipal, IPrincipal):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, ntIdentity: WindowsIdentity): ...
    
    # ---------- Properties ---------- #
    
    @property
    def DeviceClaims(self) -> IEnumerable[Claim]: ...
    
    @property
    def Identity(self) -> IIdentity: ...
    
    @property
    def UserClaims(self) -> IEnumerable[Claim]: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def IsInRole(self, role: StringType) -> BooleanType: ...
    
    @overload
    def IsInRole(self, role: WindowsBuiltInRole) -> BooleanType: ...
    
    @overload
    def IsInRole(self, rid: IntType) -> BooleanType: ...
    
    @overload
    def IsInRole(self, sid: SecurityIdentifier) -> BooleanType: ...
    
    def get_DeviceClaims(self) -> IEnumerable[Claim]: ...
    
    def get_Identity(self) -> IIdentity: ...
    
    def get_UserClaims(self) -> IEnumerable[Claim]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class WindowsPrincipal(ClaimsPrincipal, IPrincipal):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, ntIdentity: WindowsIdentity): ...
    
    # ---------- Properties ---------- #
    
    @property
    def DeviceClaims(self) -> IEnumerable[Claim]: ...
    
    @property
    def Identity(self) -> IIdentity: ...
    
    @property
    def UserClaims(self) -> IEnumerable[Claim]: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def IsInRole(self, role: StringType) -> BooleanType: ...
    
    @overload
    def IsInRole(self, role: WindowsBuiltInRole) -> BooleanType: ...
    
    @overload
    def IsInRole(self, rid: IntType) -> BooleanType: ...
    
    @overload
    def IsInRole(self, sid: SecurityIdentifier) -> BooleanType: ...
    
    def get_DeviceClaims(self) -> IEnumerable[Claim]: ...
    
    def get_Identity(self) -> IIdentity: ...
    
    def get_UserClaims(self) -> IEnumerable[Claim]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class WindowsPrincipal(ClaimsPrincipal, IPrincipal):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, ntIdentity: WindowsIdentity): ...
    
    # ---------- Properties ---------- #
    
    @property
    def DeviceClaims(self) -> IEnumerable[Claim]: ...
    
    @property
    def Identity(self) -> IIdentity: ...
    
    @property
    def UserClaims(self) -> IEnumerable[Claim]: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def IsInRole(self, role: StringType) -> BooleanType: ...
    
    @overload
    def IsInRole(self, role: WindowsBuiltInRole) -> BooleanType: ...
    
    @overload
    def IsInRole(self, rid: IntType) -> BooleanType: ...
    
    @overload
    def IsInRole(self, sid: SecurityIdentifier) -> BooleanType: ...
    
    def get_DeviceClaims(self) -> IEnumerable[Claim]: ...
    
    def get_Identity(self) -> IIdentity: ...
    
    def get_UserClaims(self) -> IEnumerable[Claim]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# No Structs

# ---------- Interfaces ---------- #

class IIdentity(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def AuthenticationType(self) -> StringType: ...
    
    @property
    def IsAuthenticated(self) -> BooleanType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_AuthenticationType(self) -> StringType: ...
    
    def get_IsAuthenticated(self) -> BooleanType: ...
    
    def get_Name(self) -> StringType: ...
    
    # No Events


class IIdentity(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def AuthenticationType(self) -> StringType: ...
    
    @property
    def IsAuthenticated(self) -> BooleanType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_AuthenticationType(self) -> StringType: ...
    
    def get_IsAuthenticated(self) -> BooleanType: ...
    
    def get_Name(self) -> StringType: ...
    
    # No Events


class IIdentity(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def AuthenticationType(self) -> StringType: ...
    
    @property
    def IsAuthenticated(self) -> BooleanType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_AuthenticationType(self) -> StringType: ...
    
    def get_IsAuthenticated(self) -> BooleanType: ...
    
    def get_Name(self) -> StringType: ...
    
    # No Events


class IPrincipal(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def Identity(self) -> IIdentity: ...
    
    # ---------- Methods ---------- #
    
    def IsInRole(self, role: StringType) -> BooleanType: ...
    
    def get_Identity(self) -> IIdentity: ...
    
    # No Events


class IPrincipal(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def Identity(self) -> IIdentity: ...
    
    # ---------- Methods ---------- #
    
    def IsInRole(self, role: StringType) -> BooleanType: ...
    
    def get_Identity(self) -> IIdentity: ...
    
    # No Events


class IPrincipal(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def Identity(self) -> IIdentity: ...
    
    # ---------- Methods ---------- #
    
    def IsInRole(self, role: StringType) -> BooleanType: ...
    
    def get_Identity(self) -> IIdentity: ...
    
    # No Events


# ---------- Enums ---------- #

class IdentifierAuthority(Enum):
    NullAuthority: LongType = 0
    WorldAuthority: LongType = 1
    LocalAuthority: LongType = 2
    CreatorAuthority: LongType = 3
    NonUniqueAuthority: LongType = 4
    NTAuthority: LongType = 5
    SiteServerAuthority: LongType = 6
    InternetSiteAuthority: LongType = 7
    ExchangeAuthority: LongType = 8
    ResourceManagerAuthority: LongType = 9


class IdentifierAuthority(Enum):
    NullAuthority: LongType = 0
    WorldAuthority: LongType = 1
    LocalAuthority: LongType = 2
    CreatorAuthority: LongType = 3
    NonUniqueAuthority: LongType = 4
    NTAuthority: LongType = 5
    SiteServerAuthority: LongType = 6
    InternetSiteAuthority: LongType = 7
    ExchangeAuthority: LongType = 8
    ResourceManagerAuthority: LongType = 9


class IdentifierAuthority(Enum):
    NullAuthority: LongType = 0
    WorldAuthority: LongType = 1
    LocalAuthority: LongType = 2
    CreatorAuthority: LongType = 3
    NonUniqueAuthority: LongType = 4
    NTAuthority: LongType = 5
    SiteServerAuthority: LongType = 6
    InternetSiteAuthority: LongType = 7
    ExchangeAuthority: LongType = 8
    ResourceManagerAuthority: LongType = 9


class ImpersonationQueryResult(Enum):
    Impersonated: IntType = 0
    NotImpersonated: IntType = 1
    Failed: IntType = 2


class ImpersonationQueryResult(Enum):
    Impersonated: IntType = 0
    NotImpersonated: IntType = 1
    Failed: IntType = 2


class ImpersonationQueryResult(Enum):
    Impersonated: IntType = 0
    NotImpersonated: IntType = 1
    Failed: IntType = 2


class KerbLogonSubmitType(Enum):
    KerbInteractiveLogon: IntType = 2
    KerbSmartCardLogon: IntType = 6
    KerbWorkstationUnlockLogon: IntType = 7
    KerbSmartCardUnlockLogon: IntType = 8
    KerbProxyLogon: IntType = 9
    KerbTicketLogon: IntType = 10
    KerbTicketUnlockLogon: IntType = 11
    KerbS4ULogon: IntType = 12


class KerbLogonSubmitType(Enum):
    KerbInteractiveLogon: IntType = 2
    KerbSmartCardLogon: IntType = 6
    KerbWorkstationUnlockLogon: IntType = 7
    KerbSmartCardUnlockLogon: IntType = 8
    KerbProxyLogon: IntType = 9
    KerbTicketLogon: IntType = 10
    KerbTicketUnlockLogon: IntType = 11
    KerbS4ULogon: IntType = 12


class KerbLogonSubmitType(Enum):
    KerbInteractiveLogon: IntType = 2
    KerbSmartCardLogon: IntType = 6
    KerbWorkstationUnlockLogon: IntType = 7
    KerbSmartCardUnlockLogon: IntType = 8
    KerbProxyLogon: IntType = 9
    KerbTicketLogon: IntType = 10
    KerbTicketUnlockLogon: IntType = 11
    KerbS4ULogon: IntType = 12


class PolicyRights(Enum):
    POLICY_VIEW_LOCAL_INFORMATION: IntType = 1
    POLICY_VIEW_AUDIT_INFORMATION: IntType = 2
    POLICY_GET_PRIVATE_INFORMATION: IntType = 4
    POLICY_TRUST_ADMIN: IntType = 8
    POLICY_CREATE_ACCOUNT: IntType = 16
    POLICY_CREATE_SECRET: IntType = 32
    POLICY_CREATE_PRIVILEGE: IntType = 64
    POLICY_SET_DEFAULT_QUOTA_LIMITS: IntType = 128
    POLICY_SET_AUDIT_REQUIREMENTS: IntType = 256
    POLICY_AUDIT_LOG_ADMIN: IntType = 512
    POLICY_SERVER_ADMIN: IntType = 1024
    POLICY_LOOKUP_NAMES: IntType = 2048
    POLICY_NOTIFICATION: IntType = 4096


class PolicyRights(Enum):
    POLICY_VIEW_LOCAL_INFORMATION: IntType = 1
    POLICY_VIEW_AUDIT_INFORMATION: IntType = 2
    POLICY_GET_PRIVATE_INFORMATION: IntType = 4
    POLICY_TRUST_ADMIN: IntType = 8
    POLICY_CREATE_ACCOUNT: IntType = 16
    POLICY_CREATE_SECRET: IntType = 32
    POLICY_CREATE_PRIVILEGE: IntType = 64
    POLICY_SET_DEFAULT_QUOTA_LIMITS: IntType = 128
    POLICY_SET_AUDIT_REQUIREMENTS: IntType = 256
    POLICY_AUDIT_LOG_ADMIN: IntType = 512
    POLICY_SERVER_ADMIN: IntType = 1024
    POLICY_LOOKUP_NAMES: IntType = 2048
    POLICY_NOTIFICATION: IntType = 4096


class PolicyRights(Enum):
    POLICY_VIEW_LOCAL_INFORMATION: IntType = 1
    POLICY_VIEW_AUDIT_INFORMATION: IntType = 2
    POLICY_GET_PRIVATE_INFORMATION: IntType = 4
    POLICY_TRUST_ADMIN: IntType = 8
    POLICY_CREATE_ACCOUNT: IntType = 16
    POLICY_CREATE_SECRET: IntType = 32
    POLICY_CREATE_PRIVILEGE: IntType = 64
    POLICY_SET_DEFAULT_QUOTA_LIMITS: IntType = 128
    POLICY_SET_AUDIT_REQUIREMENTS: IntType = 256
    POLICY_AUDIT_LOG_ADMIN: IntType = 512
    POLICY_SERVER_ADMIN: IntType = 1024
    POLICY_LOOKUP_NAMES: IntType = 2048
    POLICY_NOTIFICATION: IntType = 4096


class PrincipalPolicy(Enum):
    UnauthenticatedPrincipal: IntType = 0
    NoPrincipal: IntType = 1
    WindowsPrincipal: IntType = 2


class PrincipalPolicy(Enum):
    UnauthenticatedPrincipal: IntType = 0
    NoPrincipal: IntType = 1
    WindowsPrincipal: IntType = 2


class PrincipalPolicy(Enum):
    UnauthenticatedPrincipal: IntType = 0
    NoPrincipal: IntType = 1
    WindowsPrincipal: IntType = 2


class SecurityLogonType(Enum):
    Interactive: IntType = 2
    Network: IntType = 3
    Batch: IntType = 4
    Service: IntType = 5
    Proxy: IntType = 6
    Unlock: IntType = 7


class SecurityLogonType(Enum):
    Interactive: IntType = 2
    Network: IntType = 3
    Batch: IntType = 4
    Service: IntType = 5
    Proxy: IntType = 6
    Unlock: IntType = 7


class SecurityLogonType(Enum):
    Interactive: IntType = 2
    Network: IntType = 3
    Batch: IntType = 4
    Service: IntType = 5
    Proxy: IntType = 6
    Unlock: IntType = 7


class SidNameUse(Enum):
    User: IntType = 1
    Group: IntType = 2
    Domain: IntType = 3
    Alias: IntType = 4
    WellKnownGroup: IntType = 5
    DeletedAccount: IntType = 6
    Invalid: IntType = 7
    Unknown: IntType = 8
    Computer: IntType = 9


class SidNameUse(Enum):
    User: IntType = 1
    Group: IntType = 2
    Domain: IntType = 3
    Alias: IntType = 4
    WellKnownGroup: IntType = 5
    DeletedAccount: IntType = 6
    Invalid: IntType = 7
    Unknown: IntType = 8
    Computer: IntType = 9


class SidNameUse(Enum):
    User: IntType = 1
    Group: IntType = 2
    Domain: IntType = 3
    Alias: IntType = 4
    WellKnownGroup: IntType = 5
    DeletedAccount: IntType = 6
    Invalid: IntType = 7
    Unknown: IntType = 8
    Computer: IntType = 9


class TokenAccessLevels(Enum):
    AssignPrimary: IntType = 1
    Duplicate: IntType = 2
    Impersonate: IntType = 4
    Query: IntType = 8
    QuerySource: IntType = 16
    AdjustPrivileges: IntType = 32
    AdjustGroups: IntType = 64
    AdjustDefault: IntType = 128
    AdjustSessionId: IntType = 256
    Read: IntType = 131080
    Write: IntType = 131296
    AllAccess: IntType = 983551
    MaximumAllowed: IntType = 33554432


class TokenAccessLevels(Enum):
    AssignPrimary: IntType = 1
    Duplicate: IntType = 2
    Impersonate: IntType = 4
    Query: IntType = 8
    QuerySource: IntType = 16
    AdjustPrivileges: IntType = 32
    AdjustGroups: IntType = 64
    AdjustDefault: IntType = 128
    AdjustSessionId: IntType = 256
    Read: IntType = 131080
    Write: IntType = 131296
    AllAccess: IntType = 983551
    MaximumAllowed: IntType = 33554432


class TokenAccessLevels(Enum):
    AssignPrimary: IntType = 1
    Duplicate: IntType = 2
    Impersonate: IntType = 4
    Query: IntType = 8
    QuerySource: IntType = 16
    AdjustPrivileges: IntType = 32
    AdjustGroups: IntType = 64
    AdjustDefault: IntType = 128
    AdjustSessionId: IntType = 256
    Read: IntType = 131080
    Write: IntType = 131296
    AllAccess: IntType = 983551
    MaximumAllowed: IntType = 33554432


class TokenImpersonationLevel(Enum):
    #None: IntType = 0
    Anonymous: IntType = 1
    Identification: IntType = 2
    Impersonation: IntType = 3
    Delegation: IntType = 4


class TokenImpersonationLevel(Enum):
    #None: IntType = 0
    Anonymous: IntType = 1
    Identification: IntType = 2
    Impersonation: IntType = 3
    Delegation: IntType = 4


class TokenImpersonationLevel(Enum):
    #None: IntType = 0
    Anonymous: IntType = 1
    Identification: IntType = 2
    Impersonation: IntType = 3
    Delegation: IntType = 4


class TokenInformationClass(Enum):
    TokenUser: IntType = 1
    TokenGroups: IntType = 2
    TokenPrivileges: IntType = 3
    TokenOwner: IntType = 4
    TokenPrimaryGroup: IntType = 5
    TokenDefaultDacl: IntType = 6
    TokenSource: IntType = 7
    TokenType: IntType = 8
    TokenImpersonationLevel: IntType = 9
    TokenStatistics: IntType = 10
    TokenRestrictedSids: IntType = 11
    TokenSessionId: IntType = 12
    TokenGroupsAndPrivileges: IntType = 13
    TokenSessionReference: IntType = 14
    TokenSandBoxInert: IntType = 15
    TokenAuditPolicy: IntType = 16
    TokenOrigin: IntType = 17
    TokenElevationType: IntType = 18
    TokenLinkedToken: IntType = 19
    TokenElevation: IntType = 20
    TokenHasRestrictions: IntType = 21
    TokenAccessInformation: IntType = 22
    TokenVirtualizationAllowed: IntType = 23
    TokenVirtualizationEnabled: IntType = 24
    TokenIntegrityLevel: IntType = 25
    TokenUIAccess: IntType = 26
    TokenMandatoryPolicy: IntType = 27
    TokenLogonSid: IntType = 28
    TokenIsAppContainer: IntType = 29
    TokenCapabilities: IntType = 30
    TokenAppContainerSid: IntType = 31
    TokenAppContainerNumber: IntType = 32
    TokenUserClaimAttributes: IntType = 33
    TokenDeviceClaimAttributes: IntType = 34
    TokenRestrictedUserClaimAttributes: IntType = 35
    TokenRestrictedDeviceClaimAttributes: IntType = 36
    TokenDeviceGroups: IntType = 37
    TokenRestrictedDeviceGroups: IntType = 38
    MaxTokenInfoClass: IntType = 39


class TokenInformationClass(Enum):
    TokenUser: IntType = 1
    TokenGroups: IntType = 2
    TokenPrivileges: IntType = 3
    TokenOwner: IntType = 4
    TokenPrimaryGroup: IntType = 5
    TokenDefaultDacl: IntType = 6
    TokenSource: IntType = 7
    TokenType: IntType = 8
    TokenImpersonationLevel: IntType = 9
    TokenStatistics: IntType = 10
    TokenRestrictedSids: IntType = 11
    TokenSessionId: IntType = 12
    TokenGroupsAndPrivileges: IntType = 13
    TokenSessionReference: IntType = 14
    TokenSandBoxInert: IntType = 15
    TokenAuditPolicy: IntType = 16
    TokenOrigin: IntType = 17
    TokenElevationType: IntType = 18
    TokenLinkedToken: IntType = 19
    TokenElevation: IntType = 20
    TokenHasRestrictions: IntType = 21
    TokenAccessInformation: IntType = 22
    TokenVirtualizationAllowed: IntType = 23
    TokenVirtualizationEnabled: IntType = 24
    TokenIntegrityLevel: IntType = 25
    TokenUIAccess: IntType = 26
    TokenMandatoryPolicy: IntType = 27
    TokenLogonSid: IntType = 28
    TokenIsAppContainer: IntType = 29
    TokenCapabilities: IntType = 30
    TokenAppContainerSid: IntType = 31
    TokenAppContainerNumber: IntType = 32
    TokenUserClaimAttributes: IntType = 33
    TokenDeviceClaimAttributes: IntType = 34
    TokenRestrictedUserClaimAttributes: IntType = 35
    TokenRestrictedDeviceClaimAttributes: IntType = 36
    TokenDeviceGroups: IntType = 37
    TokenRestrictedDeviceGroups: IntType = 38
    MaxTokenInfoClass: IntType = 39


class TokenInformationClass(Enum):
    TokenUser: IntType = 1
    TokenGroups: IntType = 2
    TokenPrivileges: IntType = 3
    TokenOwner: IntType = 4
    TokenPrimaryGroup: IntType = 5
    TokenDefaultDacl: IntType = 6
    TokenSource: IntType = 7
    TokenType: IntType = 8
    TokenImpersonationLevel: IntType = 9
    TokenStatistics: IntType = 10
    TokenRestrictedSids: IntType = 11
    TokenSessionId: IntType = 12
    TokenGroupsAndPrivileges: IntType = 13
    TokenSessionReference: IntType = 14
    TokenSandBoxInert: IntType = 15
    TokenAuditPolicy: IntType = 16
    TokenOrigin: IntType = 17
    TokenElevationType: IntType = 18
    TokenLinkedToken: IntType = 19
    TokenElevation: IntType = 20
    TokenHasRestrictions: IntType = 21
    TokenAccessInformation: IntType = 22
    TokenVirtualizationAllowed: IntType = 23
    TokenVirtualizationEnabled: IntType = 24
    TokenIntegrityLevel: IntType = 25
    TokenUIAccess: IntType = 26
    TokenMandatoryPolicy: IntType = 27
    TokenLogonSid: IntType = 28
    TokenIsAppContainer: IntType = 29
    TokenCapabilities: IntType = 30
    TokenAppContainerSid: IntType = 31
    TokenAppContainerNumber: IntType = 32
    TokenUserClaimAttributes: IntType = 33
    TokenDeviceClaimAttributes: IntType = 34
    TokenRestrictedUserClaimAttributes: IntType = 35
    TokenRestrictedDeviceClaimAttributes: IntType = 36
    TokenDeviceGroups: IntType = 37
    TokenRestrictedDeviceGroups: IntType = 38
    MaxTokenInfoClass: IntType = 39


class TokenType(Enum):
    TokenPrimary: IntType = 1
    TokenImpersonation: IntType = 2


class TokenType(Enum):
    TokenPrimary: IntType = 1
    TokenImpersonation: IntType = 2


class TokenType(Enum):
    TokenPrimary: IntType = 1
    TokenImpersonation: IntType = 2


class WellKnownSidType(Enum):
    NullSid: IntType = 0
    WorldSid: IntType = 1
    LocalSid: IntType = 2
    CreatorOwnerSid: IntType = 3
    CreatorGroupSid: IntType = 4
    CreatorOwnerServerSid: IntType = 5
    CreatorGroupServerSid: IntType = 6
    NTAuthoritySid: IntType = 7
    DialupSid: IntType = 8
    NetworkSid: IntType = 9
    BatchSid: IntType = 10
    InteractiveSid: IntType = 11
    ServiceSid: IntType = 12
    AnonymousSid: IntType = 13
    ProxySid: IntType = 14
    EnterpriseControllersSid: IntType = 15
    SelfSid: IntType = 16
    AuthenticatedUserSid: IntType = 17
    RestrictedCodeSid: IntType = 18
    TerminalServerSid: IntType = 19
    RemoteLogonIdSid: IntType = 20
    LogonIdsSid: IntType = 21
    LocalSystemSid: IntType = 22
    LocalServiceSid: IntType = 23
    NetworkServiceSid: IntType = 24
    BuiltinDomainSid: IntType = 25
    BuiltinAdministratorsSid: IntType = 26
    BuiltinUsersSid: IntType = 27
    BuiltinGuestsSid: IntType = 28
    BuiltinPowerUsersSid: IntType = 29
    BuiltinAccountOperatorsSid: IntType = 30
    BuiltinSystemOperatorsSid: IntType = 31
    BuiltinPrintOperatorsSid: IntType = 32
    BuiltinBackupOperatorsSid: IntType = 33
    BuiltinReplicatorSid: IntType = 34
    BuiltinPreWindows2000CompatibleAccessSid: IntType = 35
    BuiltinRemoteDesktopUsersSid: IntType = 36
    BuiltinNetworkConfigurationOperatorsSid: IntType = 37
    AccountAdministratorSid: IntType = 38
    AccountGuestSid: IntType = 39
    AccountKrbtgtSid: IntType = 40
    AccountDomainAdminsSid: IntType = 41
    AccountDomainUsersSid: IntType = 42
    AccountDomainGuestsSid: IntType = 43
    AccountComputersSid: IntType = 44
    AccountControllersSid: IntType = 45
    AccountCertAdminsSid: IntType = 46
    AccountSchemaAdminsSid: IntType = 47
    AccountEnterpriseAdminsSid: IntType = 48
    AccountPolicyAdminsSid: IntType = 49
    AccountRasAndIasServersSid: IntType = 50
    NtlmAuthenticationSid: IntType = 51
    DigestAuthenticationSid: IntType = 52
    SChannelAuthenticationSid: IntType = 53
    ThisOrganizationSid: IntType = 54
    OtherOrganizationSid: IntType = 55
    BuiltinIncomingForestTrustBuildersSid: IntType = 56
    BuiltinPerformanceMonitoringUsersSid: IntType = 57
    BuiltinPerformanceLoggingUsersSid: IntType = 58
    BuiltinAuthorizationAccessSid: IntType = 59
    WinBuiltinTerminalServerLicenseServersSid: IntType = 60
    MaxDefined: IntType = 60


class WellKnownSidType(Enum):
    NullSid: IntType = 0
    WorldSid: IntType = 1
    LocalSid: IntType = 2
    CreatorOwnerSid: IntType = 3
    CreatorGroupSid: IntType = 4
    CreatorOwnerServerSid: IntType = 5
    CreatorGroupServerSid: IntType = 6
    NTAuthoritySid: IntType = 7
    DialupSid: IntType = 8
    NetworkSid: IntType = 9
    BatchSid: IntType = 10
    InteractiveSid: IntType = 11
    ServiceSid: IntType = 12
    AnonymousSid: IntType = 13
    ProxySid: IntType = 14
    EnterpriseControllersSid: IntType = 15
    SelfSid: IntType = 16
    AuthenticatedUserSid: IntType = 17
    RestrictedCodeSid: IntType = 18
    TerminalServerSid: IntType = 19
    RemoteLogonIdSid: IntType = 20
    LogonIdsSid: IntType = 21
    LocalSystemSid: IntType = 22
    LocalServiceSid: IntType = 23
    NetworkServiceSid: IntType = 24
    BuiltinDomainSid: IntType = 25
    BuiltinAdministratorsSid: IntType = 26
    BuiltinUsersSid: IntType = 27
    BuiltinGuestsSid: IntType = 28
    BuiltinPowerUsersSid: IntType = 29
    BuiltinAccountOperatorsSid: IntType = 30
    BuiltinSystemOperatorsSid: IntType = 31
    BuiltinPrintOperatorsSid: IntType = 32
    BuiltinBackupOperatorsSid: IntType = 33
    BuiltinReplicatorSid: IntType = 34
    BuiltinPreWindows2000CompatibleAccessSid: IntType = 35
    BuiltinRemoteDesktopUsersSid: IntType = 36
    BuiltinNetworkConfigurationOperatorsSid: IntType = 37
    AccountAdministratorSid: IntType = 38
    AccountGuestSid: IntType = 39
    AccountKrbtgtSid: IntType = 40
    AccountDomainAdminsSid: IntType = 41
    AccountDomainUsersSid: IntType = 42
    AccountDomainGuestsSid: IntType = 43
    AccountComputersSid: IntType = 44
    AccountControllersSid: IntType = 45
    AccountCertAdminsSid: IntType = 46
    AccountSchemaAdminsSid: IntType = 47
    AccountEnterpriseAdminsSid: IntType = 48
    AccountPolicyAdminsSid: IntType = 49
    AccountRasAndIasServersSid: IntType = 50
    NtlmAuthenticationSid: IntType = 51
    DigestAuthenticationSid: IntType = 52
    SChannelAuthenticationSid: IntType = 53
    ThisOrganizationSid: IntType = 54
    OtherOrganizationSid: IntType = 55
    BuiltinIncomingForestTrustBuildersSid: IntType = 56
    BuiltinPerformanceMonitoringUsersSid: IntType = 57
    BuiltinPerformanceLoggingUsersSid: IntType = 58
    BuiltinAuthorizationAccessSid: IntType = 59
    WinBuiltinTerminalServerLicenseServersSid: IntType = 60
    MaxDefined: IntType = 60


class WellKnownSidType(Enum):
    NullSid: IntType = 0
    WorldSid: IntType = 1
    LocalSid: IntType = 2
    CreatorOwnerSid: IntType = 3
    CreatorGroupSid: IntType = 4
    CreatorOwnerServerSid: IntType = 5
    CreatorGroupServerSid: IntType = 6
    NTAuthoritySid: IntType = 7
    DialupSid: IntType = 8
    NetworkSid: IntType = 9
    BatchSid: IntType = 10
    InteractiveSid: IntType = 11
    ServiceSid: IntType = 12
    AnonymousSid: IntType = 13
    ProxySid: IntType = 14
    EnterpriseControllersSid: IntType = 15
    SelfSid: IntType = 16
    AuthenticatedUserSid: IntType = 17
    RestrictedCodeSid: IntType = 18
    TerminalServerSid: IntType = 19
    RemoteLogonIdSid: IntType = 20
    LogonIdsSid: IntType = 21
    LocalSystemSid: IntType = 22
    LocalServiceSid: IntType = 23
    NetworkServiceSid: IntType = 24
    BuiltinDomainSid: IntType = 25
    BuiltinAdministratorsSid: IntType = 26
    BuiltinUsersSid: IntType = 27
    BuiltinGuestsSid: IntType = 28
    BuiltinPowerUsersSid: IntType = 29
    BuiltinAccountOperatorsSid: IntType = 30
    BuiltinSystemOperatorsSid: IntType = 31
    BuiltinPrintOperatorsSid: IntType = 32
    BuiltinBackupOperatorsSid: IntType = 33
    BuiltinReplicatorSid: IntType = 34
    BuiltinPreWindows2000CompatibleAccessSid: IntType = 35
    BuiltinRemoteDesktopUsersSid: IntType = 36
    BuiltinNetworkConfigurationOperatorsSid: IntType = 37
    AccountAdministratorSid: IntType = 38
    AccountGuestSid: IntType = 39
    AccountKrbtgtSid: IntType = 40
    AccountDomainAdminsSid: IntType = 41
    AccountDomainUsersSid: IntType = 42
    AccountDomainGuestsSid: IntType = 43
    AccountComputersSid: IntType = 44
    AccountControllersSid: IntType = 45
    AccountCertAdminsSid: IntType = 46
    AccountSchemaAdminsSid: IntType = 47
    AccountEnterpriseAdminsSid: IntType = 48
    AccountPolicyAdminsSid: IntType = 49
    AccountRasAndIasServersSid: IntType = 50
    NtlmAuthenticationSid: IntType = 51
    DigestAuthenticationSid: IntType = 52
    SChannelAuthenticationSid: IntType = 53
    ThisOrganizationSid: IntType = 54
    OtherOrganizationSid: IntType = 55
    BuiltinIncomingForestTrustBuildersSid: IntType = 56
    BuiltinPerformanceMonitoringUsersSid: IntType = 57
    BuiltinPerformanceLoggingUsersSid: IntType = 58
    BuiltinAuthorizationAccessSid: IntType = 59
    WinBuiltinTerminalServerLicenseServersSid: IntType = 60
    MaxDefined: IntType = 60


class WinSecurityContext(Enum):
    Thread: IntType = 1
    Process: IntType = 2
    Both: IntType = 3


class WinSecurityContext(Enum):
    Thread: IntType = 1
    Process: IntType = 2
    Both: IntType = 3


class WinSecurityContext(Enum):
    Thread: IntType = 1
    Process: IntType = 2
    Both: IntType = 3


class WindowsAccountType(Enum):
    Normal: IntType = 0
    Guest: IntType = 1
    System: IntType = 2
    Anonymous: IntType = 3


class WindowsAccountType(Enum):
    Normal: IntType = 0
    Guest: IntType = 1
    System: IntType = 2
    Anonymous: IntType = 3


class WindowsAccountType(Enum):
    Normal: IntType = 0
    Guest: IntType = 1
    System: IntType = 2
    Anonymous: IntType = 3


class WindowsBuiltInRole(Enum):
    Administrator: IntType = 544
    User: IntType = 545
    Guest: IntType = 546
    PowerUser: IntType = 547
    AccountOperator: IntType = 548
    SystemOperator: IntType = 549
    PrintOperator: IntType = 550
    BackupOperator: IntType = 551
    Replicator: IntType = 552


class WindowsBuiltInRole(Enum):
    Administrator: IntType = 544
    User: IntType = 545
    Guest: IntType = 546
    PowerUser: IntType = 547
    AccountOperator: IntType = 548
    SystemOperator: IntType = 549
    PrintOperator: IntType = 550
    BackupOperator: IntType = 551
    Replicator: IntType = 552


class WindowsBuiltInRole(Enum):
    Administrator: IntType = 544
    User: IntType = 545
    Guest: IntType = 546
    PowerUser: IntType = 547
    AccountOperator: IntType = 548
    SystemOperator: IntType = 549
    PrintOperator: IntType = 550
    BackupOperator: IntType = 551
    Replicator: IntType = 552


# No Delegates

__all__ = [
    GenericIdentity,
    GenericPrincipal,
    IdentityNotMappedException,
    IdentityReference,
    IdentityReferenceCollection,
    IdentityReferenceEnumerator,
    NTAccount,
    SecurityIdentifier,
    Win32,
    WindowsIdentity,
    WindowsImpersonationContext,
    WindowsPrincipal,
    IIdentity,
    IPrincipal,
    IdentifierAuthority,
    ImpersonationQueryResult,
    KerbLogonSubmitType,
    PolicyRights,
    PrincipalPolicy,
    SecurityLogonType,
    SidNameUse,
    TokenAccessLevels,
    TokenImpersonationLevel,
    TokenInformationClass,
    TokenType,
    WellKnownSidType,
    WinSecurityContext,
    WindowsAccountType,
    WindowsBuiltInRole,
]
