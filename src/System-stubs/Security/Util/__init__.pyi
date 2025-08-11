"""Automatically generated stubs for C# namespace: System.Security.Util."""

from abc import ABC
from typing import Final
from typing import overload

from System import Array
from System import Char
from System import Enum
from System import Object
from System import Type
from System import ValueType
from System.Collections import ArrayList
from System.Runtime.Serialization import StreamingContext
from System.Security import IPermission
from System.Security import SecurityElement
from System.Security.Permissions import PermissionState
from System.Security.Policy import CodeGroup

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class Config(ABC, Object):
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
class DirectoryString(SiteString):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, directory: str, checkForIllegalChars: bool) -> None:
        """"""
    def Copy(self) -> SiteString:
        """"""
    def Equals(self, o: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Intersect(self, operand: SiteString) -> SiteString:
        """"""
    @overload
    def IsSubsetOf(self, operand: DirectoryString) -> bool:
        """"""
    @overload
    def IsSubsetOf(self, operand: DirectoryString, ignoreCase: bool) -> bool:
        """"""
    @overload
    def IsSubsetOf(self, operand: SiteString) -> bool:
        """"""
    @overload
    def IsSubsetOf(self, operand: SiteString, ignoreCase: bool) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    def Union(self, operand: SiteString) -> SiteString:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class Hex(ABC, Object):
    """"""
    @classmethod
    def ConvertHexDigit(cls, val: Char) -> int:
        """"""
    @classmethod
    def DecodeHexString(cls, hexString: str) -> Array[int]:
        """"""
    @classmethod
    def EncodeHexString(cls, sArray: Array[int]) -> str:
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
class LocalSiteString(SiteString):
    """"""
    def __init__(self, site: str) -> None:
        """"""
    def Copy(self) -> SiteString:
        """"""
    def Equals(self, o: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Intersect(self, operand: SiteString) -> SiteString:
        """"""
    @overload
    def IsSubsetOf(self, operand: LocalSiteString) -> bool:
        """"""
    @overload
    def IsSubsetOf(self, operand: LocalSiteString, ignoreCase: bool) -> bool:
        """"""
    @overload
    def IsSubsetOf(self, operand: SiteString) -> bool:
        """"""
    @overload
    def IsSubsetOf(self, operand: SiteString, ignoreCase: bool) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    def Union(self, operand: SiteString) -> SiteString:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class Parser(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class QuickCacheEntryType(Enum):
    """"""

    FullTrustZoneMyComputer: QuickCacheEntryType = ...
    """"""
    FullTrustZoneIntranet: QuickCacheEntryType = ...
    """"""
    FullTrustZoneInternet: QuickCacheEntryType = ...
    """"""
    FullTrustZoneTrusted: QuickCacheEntryType = ...
    """"""
    FullTrustZoneUntrusted: QuickCacheEntryType = ...
    """"""
    FullTrustAll: QuickCacheEntryType = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SiteString(Object):
    """"""
    def __init__(self, site: str) -> None:
        """"""
    def Copy(self) -> SiteString:
        """"""
    def Equals(self, o: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Intersect(self, operand: SiteString) -> SiteString:
        """"""
    @overload
    def IsSubsetOf(self, operand: SiteString) -> bool:
        """"""
    @overload
    def IsSubsetOf(self, operand: SiteString, ignoreCase: bool) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    def Union(self, operand: SiteString) -> SiteString:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class StringExpressionSet(Object):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, str: str) -> None:
        """"""
    @overload
    def __init__(self, ignoreCase: bool, throwOnRelative: bool) -> None:
        """"""
    @overload
    def __init__(self, ignoreCase: bool, str: str, throwOnRelative: bool) -> None:
        """"""
    @overload
    def AddExpressions(self, exprArrayList: ArrayList, checkForDuplicates: bool) -> None:
        """"""
    @overload
    def AddExpressions(self, str: Array[str], checkForDuplicates: bool, needFullPath: bool) -> None:
        """"""
    @overload
    def AddExpressions(self, str: str) -> None:
        """"""
    def Copy(self) -> StringExpressionSet:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Intersect(self, ses: StringExpressionSet) -> StringExpressionSet:
        """"""
    def IsEmpty(self) -> bool:
        """"""
    def IsSubsetOf(self, ses: StringExpressionSet) -> bool:
        """"""
    def IsSubsetOfPathDiscovery(self, ses: StringExpressionSet) -> bool:
        """"""
    def SetThrowOnRelative(self, throwOnRelative: bool) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def Union(self, ses: StringExpressionSet) -> StringExpressionSet:
        """"""
    def UnsafeToString(self) -> str:
        """"""
    def UnsafeToStringArray(self) -> Array[str]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class TokenBasedSet(Object):
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
class TokenBasedSetEnumerator(ValueType):
    """"""

    Current: Final[object]
    """"""
    Index: Final[int]
    """"""
    def __init__(self, tb: TokenBasedSet) -> None:
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
class Tokenizer(Object):
    """"""

    LineNo: Final[int]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Recycle(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class TokenizerShortBlock(Object):
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
class TokenizerStream(Object):
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
class TokenizerStringBlock(Object):
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
class URLString(SiteString):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, url: str) -> None:
        """"""
    @overload
    def __init__(self, url: str, parsed: bool) -> None:
        """"""
    @property
    def Directory(self) -> str:
        """"""
    @property
    def Host(self) -> str:
        """"""
    @property
    def IsRelativeFileUrl(self) -> bool:
        """"""
    @property
    def Port(self) -> str:
        """"""
    @property
    def Scheme(self) -> str:
        """"""
    @classmethod
    def CompareUrls(cls, url1: URLString, url2: URLString) -> bool:
        """"""
    def Copy(self) -> SiteString:
        """"""
    @overload
    def Equals(self, url: URLString) -> bool:
        """"""
    @overload
    def Equals(self, o: object) -> bool:
        """"""
    def GetDirectoryName(self) -> str:
        """"""
    def GetFileName(self) -> str:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Intersect(self, operand: SiteString) -> SiteString:
        """"""
    @overload
    def IsSubsetOf(self, site: SiteString) -> bool:
        """"""
    @overload
    def IsSubsetOf(self, operand: SiteString, ignoreCase: bool) -> bool:
        """"""
    def OnDeserialized(self, ctx: StreamingContext) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def Union(self, operand: SiteString) -> SiteString:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class XMLUtil(ABC, Object):
    """"""
    @classmethod
    def AddClassAttribute(cls, element: SecurityElement, type: Type, typename: str) -> None:
        """"""
    @classmethod
    def BitFieldEnumToString(cls, type: Type, value: object) -> str:
        """"""
    @classmethod
    def CreateCodeGroup(cls, el: SecurityElement) -> CodeGroup:
        """"""
    @classmethod
    def CreatePermission(
        cls, el: SecurityElement, permState: PermissionState, ignoreTypeLoadFailures: bool
    ) -> IPermission:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def IsPermissionElement(cls, ip: IPermission, el: SecurityElement) -> bool:
        """"""
    @classmethod
    def IsUnrestricted(cls, el: SecurityElement) -> bool:
        """"""
    @classmethod
    @overload
    def NewPermissionElement(cls, ip: IPermission) -> SecurityElement:
        """"""
    @classmethod
    @overload
    def NewPermissionElement(cls, name: str) -> SecurityElement:
        """"""
    @classmethod
    def SecurityObjectToXmlString(cls, ob: object) -> str:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def XmlStringToSecurityObject(cls, s: str) -> object:
        """"""
