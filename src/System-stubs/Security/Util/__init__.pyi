from __future__ import annotations

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

class Config(ABC, Object):
    """"""

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

class DirectoryString(SiteString):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, directory: str, checkForIllegalChars: bool):
        """

        :param directory:
        :param checkForIllegalChars:
        """
    def Copy(self) -> SiteString:
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
    def Intersect(self, operand: SiteString) -> SiteString:
        """

        :param operand:
        :return:
        """
    @overload
    def IsSubsetOf(self, operand: DirectoryString) -> bool:
        """

        :param operand:
        :return:
        """
    @overload
    def IsSubsetOf(self, operand: SiteString) -> bool:
        """

        :param operand:
        :return:
        """
    @overload
    def IsSubsetOf(self, operand: DirectoryString, ignoreCase: bool) -> bool:
        """

        :param operand:
        :param ignoreCase:
        :return:
        """
    @overload
    def IsSubsetOf(self, operand: SiteString, ignoreCase: bool) -> bool:
        """

        :param operand:
        :param ignoreCase:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Union(self, operand: SiteString) -> SiteString:
        """

        :param operand:
        :return:
        """

class Hex(ABC, Object):
    """"""

    @classmethod
    def ConvertHexDigit(cls, val: Char) -> int:
        """

        :param val:
        :return:
        """
    @classmethod
    def DecodeHexString(cls, hexString: str) -> Array[int]:
        """

        :param hexString:
        :return:
        """
    @classmethod
    def EncodeHexString(cls, sArray: Array[int]) -> str:
        """

        :param sArray:
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

class LocalSiteString(SiteString):
    """"""

    def __init__(self, site: str):
        """

        :param site:
        """
    def Copy(self) -> SiteString:
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
    def Intersect(self, operand: SiteString) -> SiteString:
        """

        :param operand:
        :return:
        """
    @overload
    def IsSubsetOf(self, operand: LocalSiteString) -> bool:
        """

        :param operand:
        :return:
        """
    @overload
    def IsSubsetOf(self, operand: SiteString) -> bool:
        """

        :param operand:
        :return:
        """
    @overload
    def IsSubsetOf(self, operand: LocalSiteString, ignoreCase: bool) -> bool:
        """

        :param operand:
        :param ignoreCase:
        :return:
        """
    @overload
    def IsSubsetOf(self, operand: SiteString, ignoreCase: bool) -> bool:
        """

        :param operand:
        :param ignoreCase:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Union(self, operand: SiteString) -> SiteString:
        """

        :param operand:
        :return:
        """

class Parser(Object):
    """"""

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

class SiteString(Object):
    """"""

    def __init__(self, site: str):
        """

        :param site:
        """
    def Copy(self) -> SiteString:
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
    def Intersect(self, operand: SiteString) -> SiteString:
        """

        :param operand:
        :return:
        """
    @overload
    def IsSubsetOf(self, operand: SiteString) -> bool:
        """

        :param operand:
        :return:
        """
    @overload
    def IsSubsetOf(self, operand: SiteString, ignoreCase: bool) -> bool:
        """

        :param operand:
        :param ignoreCase:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Union(self, operand: SiteString) -> SiteString:
        """

        :param operand:
        :return:
        """

class StringExpressionSet(Object):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, str: str):
        """

        :param str:
        """
    @overload
    def __init__(self, ignoreCase: bool, throwOnRelative: bool):
        """

        :param ignoreCase:
        :param throwOnRelative:
        """
    @overload
    def __init__(self, ignoreCase: bool, str: str, throwOnRelative: bool):
        """

        :param ignoreCase:
        :param str:
        :param throwOnRelative:
        """
    @overload
    def AddExpressions(self, str: str) -> None:
        """

        :param str:
        """
    @overload
    def AddExpressions(self, exprArrayList: ArrayList, checkForDuplicates: bool) -> None:
        """

        :param exprArrayList:
        :param checkForDuplicates:
        """
    @overload
    def AddExpressions(self, str: Array[str], checkForDuplicates: bool, needFullPath: bool) -> None:
        """

        :param str:
        :param checkForDuplicates:
        :param needFullPath:
        """
    def Copy(self) -> StringExpressionSet:
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
    def Intersect(self, ses: StringExpressionSet) -> StringExpressionSet:
        """

        :param ses:
        :return:
        """
    def IsEmpty(self) -> bool:
        """

        :return:
        """
    def IsSubsetOf(self, ses: StringExpressionSet) -> bool:
        """

        :param ses:
        :return:
        """
    def IsSubsetOfPathDiscovery(self, ses: StringExpressionSet) -> bool:
        """

        :param ses:
        :return:
        """
    def SetThrowOnRelative(self, throwOnRelative: bool) -> None:
        """

        :param throwOnRelative:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Union(self, ses: StringExpressionSet) -> StringExpressionSet:
        """

        :param ses:
        :return:
        """
    def UnsafeToString(self) -> str:
        """

        :return:
        """
    def UnsafeToStringArray(self) -> Array[str]:
        """

        :return:
        """

class TokenBasedSet(Object):
    """"""

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

class TokenBasedSetEnumerator(ValueType):
    """"""

    Current: Final[object] = ...
    """
    
    :return: 
    """
    Index: Final[int] = ...
    """
    
    :return: 
    """
    def __init__(self, tb: TokenBasedSet):
        """

        :param tb:
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
    def MoveNext(self) -> bool:
        """

        :return:
        """
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class Tokenizer(Object):
    """"""

    LineNo: Final[int] = ...
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
    def Recycle(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class TokenizerShortBlock(Object):
    """"""

    def __init__(self):
        """"""
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

class TokenizerStream(Object):
    """"""

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

class TokenizerStringBlock(Object):
    """"""

    def __init__(self):
        """"""
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

class URLString(SiteString):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, url: str):
        """

        :param url:
        """
    @overload
    def __init__(self, url: str, parsed: bool):
        """

        :param url:
        :param parsed:
        """
    @property
    def Directory(self) -> str:
        """

        :return:
        """
    @property
    def Host(self) -> str:
        """

        :return:
        """
    @property
    def IsRelativeFileUrl(self) -> bool:
        """

        :return:
        """
    @property
    def Port(self) -> str:
        """

        :return:
        """
    @property
    def Scheme(self) -> str:
        """

        :return:
        """
    @classmethod
    def CompareUrls(cls, url1: URLString, url2: URLString) -> bool:
        """

        :param url1:
        :param url2:
        :return:
        """
    def Copy(self) -> SiteString:
        """

        :return:
        """
    @overload
    def Equals(self, url: URLString) -> bool:
        """

        :param url:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetDirectoryName(self) -> str:
        """

        :return:
        """
    def GetFileName(self) -> str:
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
    def Intersect(self, operand: SiteString) -> SiteString:
        """

        :param operand:
        :return:
        """
    @overload
    def IsSubsetOf(self, operand: SiteString) -> bool:
        """

        :param operand:
        :return:
        """
    @overload
    def IsSubsetOf(self, operand: SiteString, ignoreCase: bool) -> bool:
        """

        :param operand:
        :param ignoreCase:
        :return:
        """
    def OnDeserialized(self, ctx: StreamingContext) -> None:
        """

        :param ctx:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Union(self, operand: SiteString) -> SiteString:
        """

        :param operand:
        :return:
        """

class XMLUtil(ABC, Object):
    """"""

    @classmethod
    def AddClassAttribute(cls, element: SecurityElement, type: Type, typename: str) -> None:
        """

        :param element:
        :param type:
        :param typename:
        """
    @classmethod
    def BitFieldEnumToString(cls, type: Type, value: object) -> str:
        """

        :param type:
        :param value:
        :return:
        """
    @classmethod
    def CreateCodeGroup(cls, el: SecurityElement) -> CodeGroup:
        """

        :param el:
        :return:
        """
    @classmethod
    def CreatePermission(
        cls, el: SecurityElement, permState: PermissionState, ignoreTypeLoadFailures: bool
    ) -> IPermission:
        """

        :param el:
        :param permState:
        :param ignoreTypeLoadFailures:
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
    @classmethod
    def IsPermissionElement(cls, ip: IPermission, el: SecurityElement) -> bool:
        """

        :param ip:
        :param el:
        :return:
        """
    @classmethod
    def IsUnrestricted(cls, el: SecurityElement) -> bool:
        """

        :param el:
        :return:
        """
    @classmethod
    @overload
    def NewPermissionElement(cls, ip: IPermission) -> SecurityElement:
        """

        :param ip:
        :return:
        """
    @classmethod
    @overload
    def NewPermissionElement(cls, name: str) -> SecurityElement:
        """

        :param name:
        :return:
        """
    @classmethod
    def SecurityObjectToXmlString(cls, ob: object) -> str:
        """

        :param ob:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @classmethod
    def XmlStringToSecurityObject(cls, s: str) -> object:
        """

        :param s:
        :return:
        """
