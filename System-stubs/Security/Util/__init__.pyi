from __future__ import annotations

from abc import ABC
from typing import List, Union, overload

from System import Array, Boolean, Byte, Char, Enum, Int32, Object, String, Type, ValueType, Void
from System.Collections import ArrayList
from System.Runtime.Serialization import StreamingContext
from System.Security import IPermission, SecurityElement
from System.Security.Permissions import PermissionState
from System.Security.Policy import CodeGroup

# ---------- Types ---------- #

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
ByteType = Union[int, Byte]
CharType = Union[str, Char]
IntType = Union[int, Int32]
ObjectType = Object
StringType = Union[str, String]
TypeType = Union[type, Type]
VoidType = Union[None, Void]

# ---------- Classes ---------- #

class Config(ABC, ObjectType):
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


class Config(ABC, ObjectType):
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


class Config(ABC, ObjectType):
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


class DirectoryString(SiteString):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, directory: StringType, checkForIllegalChars: BooleanType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def IsSubsetOf(self, operand: DirectoryString) -> BooleanType: ...
    
    @overload
    def IsSubsetOf(self, operand: DirectoryString, ignoreCase: BooleanType) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DirectoryString(SiteString):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, directory: StringType, checkForIllegalChars: BooleanType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def IsSubsetOf(self, operand: DirectoryString) -> BooleanType: ...
    
    @overload
    def IsSubsetOf(self, operand: DirectoryString, ignoreCase: BooleanType) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DirectoryString(SiteString):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, directory: StringType, checkForIllegalChars: BooleanType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def IsSubsetOf(self, operand: DirectoryString) -> BooleanType: ...
    
    @overload
    def IsSubsetOf(self, operand: DirectoryString, ignoreCase: BooleanType) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Hex(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def ConvertHexDigit(val: CharType) -> IntType: ...
    
    @staticmethod
    def DecodeHexString(hexString: StringType) -> ArrayType[ByteType]: ...
    
    @staticmethod
    def EncodeHexString(sArray: ArrayType[ByteType]) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Hex(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def ConvertHexDigit(val: CharType) -> IntType: ...
    
    @staticmethod
    def DecodeHexString(hexString: StringType) -> ArrayType[ByteType]: ...
    
    @staticmethod
    def EncodeHexString(sArray: ArrayType[ByteType]) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Hex(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def ConvertHexDigit(val: CharType) -> IntType: ...
    
    @staticmethod
    def DecodeHexString(hexString: StringType) -> ArrayType[ByteType]: ...
    
    @staticmethod
    def EncodeHexString(sArray: ArrayType[ByteType]) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class LocalSiteString(SiteString):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, site: StringType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def IsSubsetOf(self, operand: LocalSiteString) -> BooleanType: ...
    
    @overload
    def IsSubsetOf(self, operand: LocalSiteString, ignoreCase: BooleanType) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class LocalSiteString(SiteString):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, site: StringType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def IsSubsetOf(self, operand: LocalSiteString) -> BooleanType: ...
    
    @overload
    def IsSubsetOf(self, operand: LocalSiteString, ignoreCase: BooleanType) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class LocalSiteString(SiteString):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, site: StringType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def IsSubsetOf(self, operand: LocalSiteString) -> BooleanType: ...
    
    @overload
    def IsSubsetOf(self, operand: LocalSiteString, ignoreCase: BooleanType) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Parser(ObjectType):
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


class Parser(ObjectType):
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


class Parser(ObjectType):
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


class SiteString(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, site: StringType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Copy(self) -> SiteString: ...
    
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def Intersect(self, operand: SiteString) -> SiteString: ...
    
    @overload
    def IsSubsetOf(self, operand: SiteString) -> BooleanType: ...
    
    @overload
    def IsSubsetOf(self, operand: SiteString, ignoreCase: BooleanType) -> BooleanType: ...
    
    def ToString(self) -> StringType: ...
    
    def Union(self, operand: SiteString) -> SiteString: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SiteString(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, site: StringType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Copy(self) -> SiteString: ...
    
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def Intersect(self, operand: SiteString) -> SiteString: ...
    
    @overload
    def IsSubsetOf(self, operand: SiteString) -> BooleanType: ...
    
    @overload
    def IsSubsetOf(self, operand: SiteString, ignoreCase: BooleanType) -> BooleanType: ...
    
    def ToString(self) -> StringType: ...
    
    def Union(self, operand: SiteString) -> SiteString: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SiteString(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, site: StringType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Copy(self) -> SiteString: ...
    
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def Intersect(self, operand: SiteString) -> SiteString: ...
    
    @overload
    def IsSubsetOf(self, operand: SiteString) -> BooleanType: ...
    
    @overload
    def IsSubsetOf(self, operand: SiteString, ignoreCase: BooleanType) -> BooleanType: ...
    
    def ToString(self) -> StringType: ...
    
    def Union(self, operand: SiteString) -> SiteString: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class StringExpressionSet(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, str: StringType): ...
    
    @overload
    def __init__(self, ignoreCase: BooleanType, throwOnRelative: BooleanType): ...
    
    @overload
    def __init__(self, ignoreCase: BooleanType, str: StringType, throwOnRelative: BooleanType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def AddExpressions(self, str: StringType) -> VoidType: ...
    
    @overload
    def AddExpressions(self, str: ArrayType[StringType], checkForDuplicates: BooleanType, needFullPath: BooleanType) -> VoidType: ...
    
    @overload
    def AddExpressions(self, exprArrayList: ArrayList, checkForDuplicates: BooleanType) -> VoidType: ...
    
    def Copy(self) -> StringExpressionSet: ...
    
    def Intersect(self, ses: StringExpressionSet) -> StringExpressionSet: ...
    
    def IsEmpty(self) -> BooleanType: ...
    
    def IsSubsetOf(self, ses: StringExpressionSet) -> BooleanType: ...
    
    def IsSubsetOfPathDiscovery(self, ses: StringExpressionSet) -> BooleanType: ...
    
    def SetThrowOnRelative(self, throwOnRelative: BooleanType) -> VoidType: ...
    
    def Union(self, ses: StringExpressionSet) -> StringExpressionSet: ...
    
    def UnsafeToString(self) -> StringType: ...
    
    def UnsafeToStringArray(self) -> ArrayType[StringType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class StringExpressionSet(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, str: StringType): ...
    
    @overload
    def __init__(self, ignoreCase: BooleanType, throwOnRelative: BooleanType): ...
    
    @overload
    def __init__(self, ignoreCase: BooleanType, str: StringType, throwOnRelative: BooleanType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def AddExpressions(self, str: StringType) -> VoidType: ...
    
    @overload
    def AddExpressions(self, str: ArrayType[StringType], checkForDuplicates: BooleanType, needFullPath: BooleanType) -> VoidType: ...
    
    @overload
    def AddExpressions(self, exprArrayList: ArrayList, checkForDuplicates: BooleanType) -> VoidType: ...
    
    def Copy(self) -> StringExpressionSet: ...
    
    def Intersect(self, ses: StringExpressionSet) -> StringExpressionSet: ...
    
    def IsEmpty(self) -> BooleanType: ...
    
    def IsSubsetOf(self, ses: StringExpressionSet) -> BooleanType: ...
    
    def IsSubsetOfPathDiscovery(self, ses: StringExpressionSet) -> BooleanType: ...
    
    def SetThrowOnRelative(self, throwOnRelative: BooleanType) -> VoidType: ...
    
    def Union(self, ses: StringExpressionSet) -> StringExpressionSet: ...
    
    def UnsafeToString(self) -> StringType: ...
    
    def UnsafeToStringArray(self) -> ArrayType[StringType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class StringExpressionSet(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, str: StringType): ...
    
    @overload
    def __init__(self, ignoreCase: BooleanType, throwOnRelative: BooleanType): ...
    
    @overload
    def __init__(self, ignoreCase: BooleanType, str: StringType, throwOnRelative: BooleanType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def AddExpressions(self, str: StringType) -> VoidType: ...
    
    @overload
    def AddExpressions(self, str: ArrayType[StringType], checkForDuplicates: BooleanType, needFullPath: BooleanType) -> VoidType: ...
    
    @overload
    def AddExpressions(self, exprArrayList: ArrayList, checkForDuplicates: BooleanType) -> VoidType: ...
    
    def Copy(self) -> StringExpressionSet: ...
    
    def Intersect(self, ses: StringExpressionSet) -> StringExpressionSet: ...
    
    def IsEmpty(self) -> BooleanType: ...
    
    def IsSubsetOf(self, ses: StringExpressionSet) -> BooleanType: ...
    
    def IsSubsetOfPathDiscovery(self, ses: StringExpressionSet) -> BooleanType: ...
    
    def SetThrowOnRelative(self, throwOnRelative: BooleanType) -> VoidType: ...
    
    def Union(self, ses: StringExpressionSet) -> StringExpressionSet: ...
    
    def UnsafeToString(self) -> StringType: ...
    
    def UnsafeToStringArray(self) -> ArrayType[StringType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TokenBasedSet(ObjectType):
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


class TokenBasedSet(ObjectType):
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


class TokenBasedSet(ObjectType):
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


class Tokenizer(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def LineNo(self) -> IntType: ...
    
    @LineNo.setter
    def LineNo(self, value: IntType) -> None: ...
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Recycle(self) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Tokenizer(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def LineNo(self) -> IntType: ...
    
    @LineNo.setter
    def LineNo(self, value: IntType) -> None: ...
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Recycle(self) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Tokenizer(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def LineNo(self) -> IntType: ...
    
    @LineNo.setter
    def LineNo(self, value: IntType) -> None: ...
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Recycle(self) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TokenizerShortBlock(ObjectType):
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


class TokenizerShortBlock(ObjectType):
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


class TokenizerShortBlock(ObjectType):
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


class TokenizerStream(ObjectType):
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


class TokenizerStream(ObjectType):
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


class TokenizerStream(ObjectType):
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


class TokenizerStringBlock(ObjectType):
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


class TokenizerStringBlock(ObjectType):
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


class TokenizerStringBlock(ObjectType):
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


class URLString(SiteString):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, url: StringType): ...
    
    @overload
    def __init__(self, url: StringType, parsed: BooleanType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Directory(self) -> StringType: ...
    
    @property
    def Host(self) -> StringType: ...
    
    @property
    def IsRelativeFileUrl(self) -> BooleanType: ...
    
    @property
    def Port(self) -> StringType: ...
    
    @property
    def Scheme(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def CompareUrls(url1: URLString, url2: URLString) -> BooleanType: ...
    
    def Copy(self) -> SiteString: ...
    
    @overload
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, url: URLString) -> BooleanType: ...
    
    def GetDirectoryName(self) -> StringType: ...
    
    def GetFileName(self) -> StringType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    @overload
    def IsSubsetOf(self, site: SiteString) -> BooleanType: ...
    
    def OnDeserialized(self, ctx: StreamingContext) -> VoidType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Directory(self) -> StringType: ...
    
    def get_Host(self) -> StringType: ...
    
    def get_IsRelativeFileUrl(self) -> BooleanType: ...
    
    def get_Port(self) -> StringType: ...
    
    def get_Scheme(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class URLString(SiteString):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, url: StringType): ...
    
    @overload
    def __init__(self, url: StringType, parsed: BooleanType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Directory(self) -> StringType: ...
    
    @property
    def Host(self) -> StringType: ...
    
    @property
    def IsRelativeFileUrl(self) -> BooleanType: ...
    
    @property
    def Port(self) -> StringType: ...
    
    @property
    def Scheme(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def CompareUrls(url1: URLString, url2: URLString) -> BooleanType: ...
    
    def Copy(self) -> SiteString: ...
    
    @overload
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, url: URLString) -> BooleanType: ...
    
    def GetDirectoryName(self) -> StringType: ...
    
    def GetFileName(self) -> StringType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    @overload
    def IsSubsetOf(self, site: SiteString) -> BooleanType: ...
    
    def OnDeserialized(self, ctx: StreamingContext) -> VoidType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Directory(self) -> StringType: ...
    
    def get_Host(self) -> StringType: ...
    
    def get_IsRelativeFileUrl(self) -> BooleanType: ...
    
    def get_Port(self) -> StringType: ...
    
    def get_Scheme(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class URLString(SiteString):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, url: StringType): ...
    
    @overload
    def __init__(self, url: StringType, parsed: BooleanType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Directory(self) -> StringType: ...
    
    @property
    def Host(self) -> StringType: ...
    
    @property
    def IsRelativeFileUrl(self) -> BooleanType: ...
    
    @property
    def Port(self) -> StringType: ...
    
    @property
    def Scheme(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def CompareUrls(url1: URLString, url2: URLString) -> BooleanType: ...
    
    def Copy(self) -> SiteString: ...
    
    @overload
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, url: URLString) -> BooleanType: ...
    
    def GetDirectoryName(self) -> StringType: ...
    
    def GetFileName(self) -> StringType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    @overload
    def IsSubsetOf(self, site: SiteString) -> BooleanType: ...
    
    def OnDeserialized(self, ctx: StreamingContext) -> VoidType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Directory(self) -> StringType: ...
    
    def get_Host(self) -> StringType: ...
    
    def get_IsRelativeFileUrl(self) -> BooleanType: ...
    
    def get_Port(self) -> StringType: ...
    
    def get_Scheme(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XMLUtil(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def AddClassAttribute(element: SecurityElement, type: TypeType, typename: StringType) -> VoidType: ...
    
    @staticmethod
    def BitFieldEnumToString(type: TypeType, value: ObjectType) -> StringType: ...
    
    @staticmethod
    def CreateCodeGroup(el: SecurityElement) -> CodeGroup: ...
    
    @staticmethod
    def CreatePermission(el: SecurityElement, permState: PermissionState, ignoreTypeLoadFailures: BooleanType) -> IPermission: ...
    
    @staticmethod
    def IsPermissionElement(ip: IPermission, el: SecurityElement) -> BooleanType: ...
    
    @staticmethod
    def IsUnrestricted(el: SecurityElement) -> BooleanType: ...
    
    @staticmethod
    @overload
    def NewPermissionElement(ip: IPermission) -> SecurityElement: ...
    
    @staticmethod
    @overload
    def NewPermissionElement(name: StringType) -> SecurityElement: ...
    
    @staticmethod
    def SecurityObjectToXmlString(ob: ObjectType) -> StringType: ...
    
    @staticmethod
    def XmlStringToSecurityObject(s: StringType) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XMLUtil(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def AddClassAttribute(element: SecurityElement, type: TypeType, typename: StringType) -> VoidType: ...
    
    @staticmethod
    def BitFieldEnumToString(type: TypeType, value: ObjectType) -> StringType: ...
    
    @staticmethod
    def CreateCodeGroup(el: SecurityElement) -> CodeGroup: ...
    
    @staticmethod
    def CreatePermission(el: SecurityElement, permState: PermissionState, ignoreTypeLoadFailures: BooleanType) -> IPermission: ...
    
    @staticmethod
    def IsPermissionElement(ip: IPermission, el: SecurityElement) -> BooleanType: ...
    
    @staticmethod
    def IsUnrestricted(el: SecurityElement) -> BooleanType: ...
    
    @staticmethod
    @overload
    def NewPermissionElement(ip: IPermission) -> SecurityElement: ...
    
    @staticmethod
    @overload
    def NewPermissionElement(name: StringType) -> SecurityElement: ...
    
    @staticmethod
    def SecurityObjectToXmlString(ob: ObjectType) -> StringType: ...
    
    @staticmethod
    def XmlStringToSecurityObject(s: StringType) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XMLUtil(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def AddClassAttribute(element: SecurityElement, type: TypeType, typename: StringType) -> VoidType: ...
    
    @staticmethod
    def BitFieldEnumToString(type: TypeType, value: ObjectType) -> StringType: ...
    
    @staticmethod
    def CreateCodeGroup(el: SecurityElement) -> CodeGroup: ...
    
    @staticmethod
    def CreatePermission(el: SecurityElement, permState: PermissionState, ignoreTypeLoadFailures: BooleanType) -> IPermission: ...
    
    @staticmethod
    def IsPermissionElement(ip: IPermission, el: SecurityElement) -> BooleanType: ...
    
    @staticmethod
    def IsUnrestricted(el: SecurityElement) -> BooleanType: ...
    
    @staticmethod
    @overload
    def NewPermissionElement(ip: IPermission) -> SecurityElement: ...
    
    @staticmethod
    @overload
    def NewPermissionElement(name: StringType) -> SecurityElement: ...
    
    @staticmethod
    def SecurityObjectToXmlString(ob: ObjectType) -> StringType: ...
    
    @staticmethod
    def XmlStringToSecurityObject(s: StringType) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# ---------- Structs ---------- #

class TokenBasedSetEnumerator(ValueType):
    # ---------- Fields ---------- #
    
    @property
    def Current(self) -> ObjectType: ...
    
    @Current.setter
    def Current(self, value: ObjectType) -> None: ...
    
    @property
    def Index(self) -> IntType: ...
    
    @Index.setter
    def Index(self, value: IntType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self, tb: TokenBasedSet): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def MoveNext(self) -> BooleanType: ...
    
    def Reset(self) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TokenBasedSetEnumerator(ValueType):
    # ---------- Fields ---------- #
    
    @property
    def Current(self) -> ObjectType: ...
    
    @Current.setter
    def Current(self, value: ObjectType) -> None: ...
    
    @property
    def Index(self) -> IntType: ...
    
    @Index.setter
    def Index(self, value: IntType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self, tb: TokenBasedSet): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def MoveNext(self) -> BooleanType: ...
    
    def Reset(self) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TokenBasedSetEnumerator(ValueType):
    # ---------- Fields ---------- #
    
    @property
    def Current(self) -> ObjectType: ...
    
    @Current.setter
    def Current(self, value: ObjectType) -> None: ...
    
    @property
    def Index(self) -> IntType: ...
    
    @Index.setter
    def Index(self, value: IntType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self, tb: TokenBasedSet): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def MoveNext(self) -> BooleanType: ...
    
    def Reset(self) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# No Interfaces

# ---------- Enums ---------- #

class QuickCacheEntryType(Enum):
    FullTrustZoneMyComputer: IntType = 16777216
    FullTrustZoneIntranet: IntType = 33554432
    FullTrustZoneInternet: IntType = 67108864
    FullTrustZoneTrusted: IntType = 134217728
    FullTrustZoneUntrusted: IntType = 268435456
    FullTrustAll: IntType = 536870912


class QuickCacheEntryType(Enum):
    FullTrustZoneMyComputer: IntType = 16777216
    FullTrustZoneIntranet: IntType = 33554432
    FullTrustZoneInternet: IntType = 67108864
    FullTrustZoneTrusted: IntType = 134217728
    FullTrustZoneUntrusted: IntType = 268435456
    FullTrustAll: IntType = 536870912


class QuickCacheEntryType(Enum):
    FullTrustZoneMyComputer: IntType = 16777216
    FullTrustZoneIntranet: IntType = 33554432
    FullTrustZoneInternet: IntType = 67108864
    FullTrustZoneTrusted: IntType = 134217728
    FullTrustZoneUntrusted: IntType = 268435456
    FullTrustAll: IntType = 536870912


# No Delegates

__all__ = [
    Config,
    DirectoryString,
    Hex,
    LocalSiteString,
    Parser,
    SiteString,
    StringExpressionSet,
    TokenBasedSet,
    Tokenizer,
    TokenizerShortBlock,
    TokenizerStream,
    TokenizerStringBlock,
    URLString,
    XMLUtil,
    TokenBasedSetEnumerator,
    QuickCacheEntryType,
]
