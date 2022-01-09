from __future__ import annotations

from abc import ABC
from typing import List, Tuple, Union, overload

from System import Array, Boolean, Byte, Char, Enum, Exception, FormatException, Func, IDisposable, Int32, Int64, Object, String, StringComparison, Type, UInt32, UInt64, Void
from System.Collections import IComparer
from System.ComponentModel import CategoryAttribute, DescriptionAttribute, ITypeDescriptorContext, TypeConverter
from System.Diagnostics.Tracing import EventSource
from System.Globalization import CultureInfo
from System.Resources import ResourceManager
from System.Runtime.ConstrainedExecution import CriticalFinalizerObject
from System.Runtime.InteropServices import _Attribute, _Exception
from System.Runtime.Serialization import ISerializable
from System.Text import NormalizationForm

# ---------- Types ---------- #

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
ByteType = Union[int, Byte]
CharType = Union[str, Char]
IntType = Union[int, Int32]
LongType = Union[int, Int64]
ObjectType = Object
StringType = Union[str, String]
TypeType = Union[type, Type]
UIntType = Union[int, UInt32]
ULongType = Union[int, UInt64]
VoidType = Union[None, Void]

# ---------- Classes ---------- #

class AppContextDefaultValues(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def PopulateDefaultValues() -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ClientUtils(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def GetBitCount(x: UIntType) -> IntType: ...
    
    @staticmethod
    def IsCriticalException(ex: Exception) -> BooleanType: ...
    
    @staticmethod
    @overload
    def IsEnumValid(enumValue: Enum, value: IntType, minValue: IntType, maxValue: IntType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def IsEnumValid(enumValue: Enum, value: IntType, minValue: IntType, maxValue: IntType, maxNumberOfBitsOn: IntType) -> BooleanType: ...
    
    @staticmethod
    def IsEnumValid_Masked(enumValue: Enum, value: IntType, mask: UIntType) -> BooleanType: ...
    
    @staticmethod
    def IsEnumValid_NotSequential(enumValue: Enum, value: IntType, enumValues: ArrayType[IntType]) -> BooleanType: ...
    
    @staticmethod
    def IsSecurityOrCriticalException(ex: Exception) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DomainNameHelper(ObjectType):
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


class EnvironmentHelpers(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def IsAppContainerProcess() -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def get_IsAppContainerProcess() -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ExternDll(ABC, ObjectType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Activeds() -> StringType: ...
    
    @staticmethod
    @property
    def Advapi32() -> StringType: ...
    
    @staticmethod
    @property
    def Clr() -> StringType: ...
    
    @staticmethod
    @property
    def Comctl32() -> StringType: ...
    
    @staticmethod
    @property
    def Comdlg32() -> StringType: ...
    
    @staticmethod
    @property
    def Crypt32() -> StringType: ...
    
    @staticmethod
    @property
    def Fxassert() -> StringType: ...
    
    @staticmethod
    @property
    def Gdi32() -> StringType: ...
    
    @staticmethod
    @property
    def Gdiplus() -> StringType: ...
    
    @staticmethod
    @property
    def Hhctrl() -> StringType: ...
    
    @staticmethod
    @property
    def Imm32() -> StringType: ...
    
    @staticmethod
    @property
    def Kernel32() -> StringType: ...
    
    @staticmethod
    @property
    def Loadperf() -> StringType: ...
    
    @staticmethod
    @property
    def Mqrt() -> StringType: ...
    
    @staticmethod
    @property
    def Mscoree() -> StringType: ...
    
    @staticmethod
    @property
    def Msi() -> StringType: ...
    
    @staticmethod
    @property
    def Ntdll() -> StringType: ...
    
    @staticmethod
    @property
    def Ole32() -> StringType: ...
    
    @staticmethod
    @property
    def Oleacc() -> StringType: ...
    
    @staticmethod
    @property
    def Oleaut32() -> StringType: ...
    
    @staticmethod
    @property
    def Olepro32() -> StringType: ...
    
    @staticmethod
    @property
    def PerfCounter() -> StringType: ...
    
    @staticmethod
    @property
    def Powrprof() -> StringType: ...
    
    @staticmethod
    @property
    def Psapi() -> StringType: ...
    
    @staticmethod
    @property
    def ShCore() -> StringType: ...
    
    @staticmethod
    @property
    def Shell32() -> StringType: ...
    
    @staticmethod
    @property
    def Shlwapi() -> StringType: ...
    
    @staticmethod
    @property
    def User32() -> StringType: ...
    
    @staticmethod
    @property
    def Uxtheme() -> StringType: ...
    
    @staticmethod
    @property
    def Version() -> StringType: ...
    
    @staticmethod
    @property
    def Vsassert() -> StringType: ...
    
    @staticmethod
    @property
    def WinMM() -> StringType: ...
    
    @staticmethod
    @property
    def Winspool() -> StringType: ...
    
    @staticmethod
    @property
    def Wldp() -> StringType: ...
    
    @staticmethod
    @property
    def Wtsapi32() -> StringType: ...
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class FileStyleUriParser(UriParser):
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


class FtpStyleUriParser(UriParser):
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


class Gen2GcCallback(CriticalFinalizerObject):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def Register(callback: Func[ObjectType, BooleanType], targetObj: ObjectType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class GenericUriParser(UriParser):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, options: GenericUriParserOptions): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class GopherStyleUriParser(UriParser):
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


class HResults(ABC, ObjectType):
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


class HttpStyleUriParser(UriParser):
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


class IPv4AddressHelper(ABC, ObjectType):
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


class IPv6AddressHelper(ABC, ObjectType):
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


class InvariantComparer(ObjectType, IComparer):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Compare(self, a: ObjectType, b: ObjectType) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class IriHelper(ABC, ObjectType):
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


class LdapStyleUriParser(UriParser):
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


class LocalAppContext(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def IsSwitchEnabled(switchName: StringType) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class LocalAppContextSwitches(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def AllocateOverlappedOnDemand() -> BooleanType: ...
    
    @staticmethod
    @property
    def DisableEventLogRegistryKeysFiltering() -> BooleanType: ...
    
    @staticmethod
    @property
    def DisableTempFileCollectionDirectoryFeature() -> BooleanType: ...
    
    @staticmethod
    @property
    def DoNotCatchSerialStreamThreadExceptions() -> BooleanType: ...
    
    @staticmethod
    @property
    def DoNotUseNativeZipLibraryForDecompression() -> BooleanType: ...
    
    @staticmethod
    @property
    def DoNotValidateX509KeyStorageFlags() -> BooleanType: ...
    
    @staticmethod
    @property
    def DontCheckCertificateEKUs() -> BooleanType: ...
    
    @staticmethod
    @property
    def DontCheckCertificateRevocation() -> BooleanType: ...
    
    @staticmethod
    @property
    def DontEnableSchSendAuxRecord() -> BooleanType: ...
    
    @staticmethod
    @property
    def DontEnableSchUseStrongCrypto() -> BooleanType: ...
    
    @staticmethod
    @property
    def DontEnableStrictRFC3986ReservedCharacterSets() -> BooleanType: ...
    
    @staticmethod
    @property
    def DontEnableSystemDefaultTlsVersions() -> BooleanType: ...
    
    @staticmethod
    @property
    def DontEnableTls13() -> BooleanType: ...
    
    @staticmethod
    @property
    def DontEnableTlsAlerts() -> BooleanType: ...
    
    @staticmethod
    @property
    def DontKeepUnicodeBidiFormattingCharacters() -> BooleanType: ...
    
    @staticmethod
    @property
    def MemberDescriptorEqualsReturnsFalseIfEquivalent() -> BooleanType: ...
    
    @staticmethod
    @property
    def UseLegacyTimeoutCheck() -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def get_AllocateOverlappedOnDemand() -> BooleanType: ...
    
    @staticmethod
    def get_DisableEventLogRegistryKeysFiltering() -> BooleanType: ...
    
    @staticmethod
    def get_DisableTempFileCollectionDirectoryFeature() -> BooleanType: ...
    
    @staticmethod
    def get_DoNotCatchSerialStreamThreadExceptions() -> BooleanType: ...
    
    @staticmethod
    def get_DoNotUseNativeZipLibraryForDecompression() -> BooleanType: ...
    
    @staticmethod
    def get_DoNotValidateX509KeyStorageFlags() -> BooleanType: ...
    
    @staticmethod
    def get_DontCheckCertificateEKUs() -> BooleanType: ...
    
    @staticmethod
    def get_DontCheckCertificateRevocation() -> BooleanType: ...
    
    @staticmethod
    def get_DontEnableSchSendAuxRecord() -> BooleanType: ...
    
    @staticmethod
    def get_DontEnableSchUseStrongCrypto() -> BooleanType: ...
    
    @staticmethod
    def get_DontEnableStrictRFC3986ReservedCharacterSets() -> BooleanType: ...
    
    @staticmethod
    def get_DontEnableSystemDefaultTlsVersions() -> BooleanType: ...
    
    @staticmethod
    def get_DontEnableTls13() -> BooleanType: ...
    
    @staticmethod
    def get_DontEnableTlsAlerts() -> BooleanType: ...
    
    @staticmethod
    def get_DontKeepUnicodeBidiFormattingCharacters() -> BooleanType: ...
    
    @staticmethod
    def get_MemberDescriptorEqualsReturnsFalseIfEquivalent() -> BooleanType: ...
    
    @staticmethod
    def get_UseLegacyTimeoutCheck() -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class NetPipeStyleUriParser(UriParser):
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


class NetTcpStyleUriParser(UriParser):
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


class NewsStyleUriParser(UriParser):
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


class PinnableBufferCache(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, cacheName: StringType, numberOfElements: IntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def AllocateBuffer(self) -> ArrayType[ByteType]: ...
    
    def FreeBuffer(self, buffer: ArrayType[ByteType]) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PinnableBufferCacheEventSource(EventSource, IDisposable):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Log() -> PinnableBufferCacheEventSource: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def AgePendingBuffersResults(self, cacheName: StringType, promotedToFreeListCount: IntType, heldBackCount: IntType) -> VoidType: ...
    
    def AllocateBuffer(self, cacheName: StringType, objectId: ULongType, objectHash: IntType, objectGen: IntType, freeCountAfter: IntType) -> VoidType: ...
    
    def AllocateBufferAged(self, cacheName: StringType, agedCount: IntType) -> VoidType: ...
    
    def AllocateBufferCreatingNewBuffers(self, cacheName: StringType, totalBuffsBefore: IntType, objectCount: IntType) -> VoidType: ...
    
    def AllocateBufferFreeListEmpty(self, cacheName: StringType, notGen2CountBefore: IntType) -> VoidType: ...
    
    def AllocateBufferFromNotGen2(self, cacheName: StringType, notGen2CountAfter: IntType) -> VoidType: ...
    
    def Create(self, cacheName: StringType) -> VoidType: ...
    
    def DebugMessage(self, message: StringType) -> VoidType: ...
    
    def DebugMessage1(self, message: StringType, value: LongType) -> VoidType: ...
    
    def DebugMessage2(self, message: StringType, value1: LongType, value2: LongType) -> VoidType: ...
    
    def DebugMessage3(self, message: StringType, value1: LongType, value2: LongType, value3: LongType) -> VoidType: ...
    
    def FreeBuffer(self, cacheName: StringType, objectId: ULongType, objectHash: IntType, freeCountBefore: IntType) -> VoidType: ...
    
    def FreeBufferNull(self, cacheName: StringType, freeCountBefore: IntType) -> VoidType: ...
    
    def FreeBufferStillTooYoung(self, cacheName: StringType, notGen2CountBefore: IntType) -> VoidType: ...
    
    def TrimCheck(self, cacheName: StringType, totalBuffs: IntType, neededMoreThanFreeList: BooleanType, deltaMSec: IntType) -> VoidType: ...
    
    def TrimExperiment(self, cacheName: StringType, totalBuffs: IntType, freeListCount: IntType, numTrimTrial: IntType) -> VoidType: ...
    
    def TrimFlush(self, cacheName: StringType, totalBuffs: IntType, freeListCount: IntType, notGen2CountBefore: IntType) -> VoidType: ...
    
    def TrimFree(self, cacheName: StringType, totalBuffs: IntType, freeListCount: IntType, toBeFreed: IntType) -> VoidType: ...
    
    def TrimFreeSizeOK(self, cacheName: StringType, totalBuffs: IntType, freeListCount: IntType) -> VoidType: ...
    
    def WalkFreeListResult(self, cacheName: StringType, freeListCount: IntType, gen0BuffersInFreeList: IntType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SR(ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def Resources() -> ResourceManager: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def GetObject(name: StringType) -> ObjectType: ...
    
    @staticmethod
    @overload
    def GetString(name: StringType) -> StringType: ...
    
    @staticmethod
    @overload
    def GetString(name: StringType, args: ArrayType[ObjectType]) -> StringType: ...
    
    @staticmethod
    @overload
    def GetString(name: StringType, usedFallback: BooleanType) -> Tuple[StringType, BooleanType]: ...
    
    @staticmethod
    def get_Resources() -> ResourceManager: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SRCategoryAttribute(CategoryAttribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, category: StringType): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SRDescriptionAttribute(DescriptionAttribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, description: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Description(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_Description(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SecurityUtils(ABC, ObjectType):
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


class StringNormalizationExtensions(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    @overload
    def IsNormalized(value: StringType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def IsNormalized(value: StringType, normalizationForm: NormalizationForm) -> BooleanType: ...
    
    @staticmethod
    @overload
    def Normalize(value: StringType) -> StringType: ...
    
    @staticmethod
    @overload
    def Normalize(value: StringType, normalizationForm: NormalizationForm) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ThrowHelper(ABC, ObjectType):
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


class UncNameHelper(ObjectType):
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


class Uri(ObjectType, ISerializable):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def SchemeDelimiter() -> StringType: ...
    
    @staticmethod
    @property
    def UriSchemeFile() -> StringType: ...
    
    @staticmethod
    @property
    def UriSchemeFtp() -> StringType: ...
    
    @staticmethod
    @property
    def UriSchemeGopher() -> StringType: ...
    
    @staticmethod
    @property
    def UriSchemeHttp() -> StringType: ...
    
    @staticmethod
    @property
    def UriSchemeHttps() -> StringType: ...
    
    @staticmethod
    @property
    def UriSchemeMailto() -> StringType: ...
    
    @staticmethod
    @property
    def UriSchemeNetPipe() -> StringType: ...
    
    @staticmethod
    @property
    def UriSchemeNetTcp() -> StringType: ...
    
    @staticmethod
    @property
    def UriSchemeNews() -> StringType: ...
    
    @staticmethod
    @property
    def UriSchemeNntp() -> StringType: ...
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, uriString: StringType): ...
    
    @overload
    def __init__(self, uriString: StringType, dontEscape: BooleanType): ...
    
    @overload
    def __init__(self, baseUri: Uri, relativeUri: StringType, dontEscape: BooleanType): ...
    
    @overload
    def __init__(self, uriString: StringType, uriKind: UriKind): ...
    
    @overload
    def __init__(self, baseUri: Uri, relativeUri: StringType): ...
    
    @overload
    def __init__(self, baseUri: Uri, relativeUri: Uri): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AbsolutePath(self) -> StringType: ...
    
    @property
    def AbsoluteUri(self) -> StringType: ...
    
    @property
    def Authority(self) -> StringType: ...
    
    @property
    def DnsSafeHost(self) -> StringType: ...
    
    @property
    def Fragment(self) -> StringType: ...
    
    @property
    def Host(self) -> StringType: ...
    
    @property
    def HostNameType(self) -> UriHostNameType: ...
    
    @property
    def IdnHost(self) -> StringType: ...
    
    @property
    def IsAbsoluteUri(self) -> BooleanType: ...
    
    @property
    def IsDefaultPort(self) -> BooleanType: ...
    
    @property
    def IsFile(self) -> BooleanType: ...
    
    @property
    def IsLoopback(self) -> BooleanType: ...
    
    @property
    def IsUnc(self) -> BooleanType: ...
    
    @property
    def LocalPath(self) -> StringType: ...
    
    @property
    def OriginalString(self) -> StringType: ...
    
    @property
    def PathAndQuery(self) -> StringType: ...
    
    @property
    def Port(self) -> IntType: ...
    
    @property
    def Query(self) -> StringType: ...
    
    @property
    def Scheme(self) -> StringType: ...
    
    @property
    def Segments(self) -> ArrayType[StringType]: ...
    
    @property
    def UserEscaped(self) -> BooleanType: ...
    
    @property
    def UserInfo(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def CheckHostName(name: StringType) -> UriHostNameType: ...
    
    @staticmethod
    def CheckSchemeName(schemeName: StringType) -> BooleanType: ...
    
    @staticmethod
    def Compare(uri1: Uri, uri2: Uri, partsToCompare: UriComponents, compareFormat: UriFormat, comparisonType: StringComparison) -> IntType: ...
    
    def Equals(self, comparand: ObjectType) -> BooleanType: ...
    
    @staticmethod
    def EscapeDataString(stringToEscape: StringType) -> StringType: ...
    
    @staticmethod
    def EscapeUriString(stringToEscape: StringType) -> StringType: ...
    
    @staticmethod
    def FromHex(digit: CharType) -> IntType: ...
    
    def GetComponents(self, components: UriComponents, format: UriFormat) -> StringType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def GetLeftPart(self, part: UriPartial) -> StringType: ...
    
    @staticmethod
    def HexEscape(character: CharType) -> StringType: ...
    
    @staticmethod
    def HexUnescape(pattern: StringType, index: IntType) -> Tuple[CharType, IntType]: ...
    
    def IsBaseOf(self, uri: Uri) -> BooleanType: ...
    
    @staticmethod
    def IsHexDigit(character: CharType) -> BooleanType: ...
    
    @staticmethod
    def IsHexEncoding(pattern: StringType, index: IntType) -> BooleanType: ...
    
    def IsWellFormedOriginalString(self) -> BooleanType: ...
    
    @staticmethod
    def IsWellFormedUriString(uriString: StringType, uriKind: UriKind) -> BooleanType: ...
    
    def MakeRelative(self, toUri: Uri) -> StringType: ...
    
    def MakeRelativeUri(self, uri: Uri) -> Uri: ...
    
    def ToString(self) -> StringType: ...
    
    @staticmethod
    @overload
    def TryCreate(uriString: StringType, uriKind: UriKind, result: Uri) -> Tuple[BooleanType, Uri]: ...
    
    @staticmethod
    @overload
    def TryCreate(baseUri: Uri, relativeUri: StringType, result: Uri) -> Tuple[BooleanType, Uri]: ...
    
    @staticmethod
    @overload
    def TryCreate(baseUri: Uri, relativeUri: Uri, result: Uri) -> Tuple[BooleanType, Uri]: ...
    
    @staticmethod
    def UnescapeDataString(stringToUnescape: StringType) -> StringType: ...
    
    def get_AbsolutePath(self) -> StringType: ...
    
    def get_AbsoluteUri(self) -> StringType: ...
    
    def get_Authority(self) -> StringType: ...
    
    def get_DnsSafeHost(self) -> StringType: ...
    
    def get_Fragment(self) -> StringType: ...
    
    def get_Host(self) -> StringType: ...
    
    def get_HostNameType(self) -> UriHostNameType: ...
    
    def get_IdnHost(self) -> StringType: ...
    
    def get_IsAbsoluteUri(self) -> BooleanType: ...
    
    def get_IsDefaultPort(self) -> BooleanType: ...
    
    def get_IsFile(self) -> BooleanType: ...
    
    def get_IsLoopback(self) -> BooleanType: ...
    
    def get_IsUnc(self) -> BooleanType: ...
    
    def get_LocalPath(self) -> StringType: ...
    
    def get_OriginalString(self) -> StringType: ...
    
    def get_PathAndQuery(self) -> StringType: ...
    
    def get_Port(self) -> IntType: ...
    
    def get_Query(self) -> StringType: ...
    
    def get_Scheme(self) -> StringType: ...
    
    def get_Segments(self) -> ArrayType[StringType]: ...
    
    def get_UserEscaped(self) -> BooleanType: ...
    
    def get_UserInfo(self) -> StringType: ...
    
    @staticmethod
    def op_Equality(uri1: Uri, uri2: Uri) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(uri1: Uri, uri2: Uri) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UriBuilder(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, uri: StringType): ...
    
    @overload
    def __init__(self, uri: Uri): ...
    
    @overload
    def __init__(self, schemeName: StringType, hostName: StringType): ...
    
    @overload
    def __init__(self, scheme: StringType, host: StringType, portNumber: IntType): ...
    
    @overload
    def __init__(self, scheme: StringType, host: StringType, port: IntType, pathValue: StringType): ...
    
    @overload
    def __init__(self, scheme: StringType, host: StringType, port: IntType, path: StringType, extraValue: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Fragment(self) -> StringType: ...
    
    @Fragment.setter
    def Fragment(self, value: StringType) -> None: ...
    
    @property
    def Host(self) -> StringType: ...
    
    @Host.setter
    def Host(self, value: StringType) -> None: ...
    
    @property
    def Password(self) -> StringType: ...
    
    @Password.setter
    def Password(self, value: StringType) -> None: ...
    
    @property
    def Path(self) -> StringType: ...
    
    @Path.setter
    def Path(self, value: StringType) -> None: ...
    
    @property
    def Port(self) -> IntType: ...
    
    @Port.setter
    def Port(self, value: IntType) -> None: ...
    
    @property
    def Query(self) -> StringType: ...
    
    @Query.setter
    def Query(self, value: StringType) -> None: ...
    
    @property
    def Scheme(self) -> StringType: ...
    
    @Scheme.setter
    def Scheme(self, value: StringType) -> None: ...
    
    @property
    def Uri(self) -> Uri: ...
    
    @property
    def UserName(self) -> StringType: ...
    
    @UserName.setter
    def UserName(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, rparam: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Fragment(self) -> StringType: ...
    
    def get_Host(self) -> StringType: ...
    
    def get_Password(self) -> StringType: ...
    
    def get_Path(self) -> StringType: ...
    
    def get_Port(self) -> IntType: ...
    
    def get_Query(self) -> StringType: ...
    
    def get_Scheme(self) -> StringType: ...
    
    def get_Uri(self) -> Uri: ...
    
    def get_UserName(self) -> StringType: ...
    
    def set_Fragment(self, value: StringType) -> VoidType: ...
    
    def set_Host(self, value: StringType) -> VoidType: ...
    
    def set_Password(self, value: StringType) -> VoidType: ...
    
    def set_Path(self, value: StringType) -> VoidType: ...
    
    def set_Port(self, value: IntType) -> VoidType: ...
    
    def set_Query(self, value: StringType) -> VoidType: ...
    
    def set_Scheme(self, value: StringType) -> VoidType: ...
    
    def set_UserName(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UriFormatException(FormatException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, textString: StringType): ...
    
    @overload
    def __init__(self, textString: StringType, e: Exception): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UriHelper(ABC, ObjectType):
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


class UriParser(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def IsKnownScheme(schemeName: StringType) -> BooleanType: ...
    
    @staticmethod
    def Register(uriParser: UriParser, schemeName: StringType, defaultPort: IntType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UriTypeConverter(TypeConverter):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: TypeType) -> BooleanType: ...
    
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, destinationType: TypeType) -> BooleanType: ...
    
    @overload
    def ConvertFrom(self, context: ITypeDescriptorContext, culture: CultureInfo, value: ObjectType) -> ObjectType: ...
    
    @overload
    def ConvertTo(self, context: ITypeDescriptorContext, culture: CultureInfo, value: ObjectType, destinationType: TypeType) -> ObjectType: ...
    
    @overload
    def IsValid(self, context: ITypeDescriptorContext, value: ObjectType) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# No Structs

# No Interfaces

# ---------- Enums ---------- #

class ExceptionArgument(Enum):
    obj: IntType = 0
    dictionary: IntType = 1
    array: IntType = 2
    info: IntType = 3
    key: IntType = 4
    collection: IntType = 5
    match: IntType = 6
    converter: IntType = 7
    queue: IntType = 8
    stack: IntType = 9
    capacity: IntType = 10
    index: IntType = 11
    startIndex: IntType = 12
    value: IntType = 13
    count: IntType = 14
    arrayIndex: IntType = 15
    item: IntType = 16


class ExceptionResource(Enum):
    Argument_ImplementIComparable: IntType = 0
    ArgumentOutOfRange_NeedNonNegNum: IntType = 1
    ArgumentOutOfRange_NeedNonNegNumRequired: IntType = 2
    Arg_ArrayPlusOffTooSmall: IntType = 3
    Argument_AddingDuplicate: IntType = 4
    Serialization_InvalidOnDeser: IntType = 5
    Serialization_MismatchedCount: IntType = 6
    Serialization_MissingValues: IntType = 7
    Arg_RankMultiDimNotSupported: IntType = 8
    Arg_NonZeroLowerBound: IntType = 9
    Argument_InvalidArrayType: IntType = 10
    NotSupported_KeyCollectionSet: IntType = 11
    ArgumentOutOfRange_SmallCapacity: IntType = 12
    ArgumentOutOfRange_Index: IntType = 13
    Argument_InvalidOffLen: IntType = 14
    NotSupported_ReadOnlyCollection: IntType = 15
    InvalidOperation_CannotRemoveFromStackOrQueue: IntType = 16
    InvalidOperation_EmptyCollection: IntType = 17
    InvalidOperation_EmptyQueue: IntType = 18
    InvalidOperation_EnumOpCantHappen: IntType = 19
    InvalidOperation_EnumFailedVersion: IntType = 20
    InvalidOperation_EmptyStack: IntType = 21
    InvalidOperation_EnumNotStarted: IntType = 22
    InvalidOperation_EnumEnded: IntType = 23
    NotSupported_SortedListNestedWrite: IntType = 24
    NotSupported_ValueCollectionSet: IntType = 25


class GenericUriParserOptions(Enum):
    Default: IntType = 0
    GenericAuthority: IntType = 1
    AllowEmptyAuthority: IntType = 2
    NoUserInfo: IntType = 4
    NoPort: IntType = 8
    NoQuery: IntType = 16
    NoFragment: IntType = 32
    DontConvertPathBackslashes: IntType = 64
    DontCompressPath: IntType = 128
    DontUnescapePathDotsAndSlashes: IntType = 256
    Idn: IntType = 512
    IriParsing: IntType = 1024


class ParsingError(Enum):
    #None: IntType = 0
    BadFormat: IntType = 1
    BadScheme: IntType = 2
    BadAuthority: IntType = 3
    EmptyUriString: IntType = 4
    LastRelativeUriOkErrIndex: IntType = 4
    SchemeLimit: IntType = 5
    SizeLimit: IntType = 6
    MustRootedPath: IntType = 7
    BadHostName: IntType = 8
    NonEmptyHost: IntType = 9
    BadPort: IntType = 10
    BadAuthorityTerminator: IntType = 11
    CannotCreateRelative: IntType = 12


class UnescapeMode(Enum):
    CopyOnly: IntType = 0
    Escape: IntType = 1
    Unescape: IntType = 2
    EscapeUnescape: IntType = 3
    V1ToStringFlag: IntType = 4
    UnescapeAll: IntType = 8
    UnescapeAllOrThrow: IntType = 24


class UriComponents(Enum):
    SerializationInfoString: IntType = -2147483648
    Scheme: IntType = 1
    UserInfo: IntType = 2
    Host: IntType = 4
    Port: IntType = 8
    SchemeAndServer: IntType = 13
    Path: IntType = 16
    Query: IntType = 32
    PathAndQuery: IntType = 48
    HttpRequestUrl: IntType = 61
    Fragment: IntType = 64
    AbsoluteUri: IntType = 127
    StrongPort: IntType = 128
    HostAndPort: IntType = 132
    StrongAuthority: IntType = 134
    NormalizedHost: IntType = 256
    KeepDelimiter: IntType = 1073741824


class UriFormat(Enum):
    UriEscaped: IntType = 1
    Unescaped: IntType = 2
    SafeUnescaped: IntType = 3


class UriHostNameType(Enum):
    Unknown: IntType = 0
    Basic: IntType = 1
    Dns: IntType = 2
    IPv4: IntType = 3
    IPv6: IntType = 4


class UriIdnScope(Enum):
    #None: IntType = 0
    AllExceptIntranet: IntType = 1
    All: IntType = 2


class UriKind(Enum):
    RelativeOrAbsolute: IntType = 0
    Absolute: IntType = 1
    Relative: IntType = 2


class UriPartial(Enum):
    Scheme: IntType = 0
    Authority: IntType = 1
    Path: IntType = 2
    Query: IntType = 3


class UriSyntaxFlags(Enum):
    #None: IntType = 0
    MustHaveAuthority: IntType = 1
    OptionalAuthority: IntType = 2
    MayHaveUserInfo: IntType = 4
    MayHavePort: IntType = 8
    MayHavePath: IntType = 16
    MayHaveQuery: IntType = 32
    MayHaveFragment: IntType = 64
    AllowEmptyHost: IntType = 128
    AllowUncHost: IntType = 256
    AllowDnsHost: IntType = 512
    AllowIPv4Host: IntType = 1024
    AllowIPv6Host: IntType = 2048
    AllowAnInternetHost: IntType = 3584
    AllowAnyOtherHost: IntType = 4096
    FileLikeUri: IntType = 8192
    MailToLikeUri: IntType = 16384
    V1_UnknownUri: IntType = 65536
    SimpleUserSyntax: IntType = 131072
    BuiltInSyntax: IntType = 262144
    ParserSchemeOnly: IntType = 524288
    AllowDOSPath: IntType = 1048576
    PathIsRooted: IntType = 2097152
    ConvertPathSlashes: IntType = 4194304
    CompressPath: IntType = 8388608
    CanonicalizeAsFilePath: IntType = 16777216
    UnEscapeDotsAndSlashes: IntType = 33554432
    AllowIdn: IntType = 67108864
    AllowIriParsing: IntType = 268435456


# No Delegates

__all__ = [
    AppContextDefaultValues,
    ClientUtils,
    DomainNameHelper,
    EnvironmentHelpers,
    ExternDll,
    FileStyleUriParser,
    FtpStyleUriParser,
    Gen2GcCallback,
    GenericUriParser,
    GopherStyleUriParser,
    HResults,
    HttpStyleUriParser,
    IPv4AddressHelper,
    IPv6AddressHelper,
    InvariantComparer,
    IriHelper,
    LdapStyleUriParser,
    LocalAppContext,
    LocalAppContextSwitches,
    NetPipeStyleUriParser,
    NetTcpStyleUriParser,
    NewsStyleUriParser,
    PinnableBufferCache,
    PinnableBufferCacheEventSource,
    SR,
    SRCategoryAttribute,
    SRDescriptionAttribute,
    SecurityUtils,
    StringNormalizationExtensions,
    ThrowHelper,
    UncNameHelper,
    Uri,
    UriBuilder,
    UriFormatException,
    UriHelper,
    UriParser,
    UriTypeConverter,
    ExceptionArgument,
    ExceptionResource,
    GenericUriParserOptions,
    ParsingError,
    UnescapeMode,
    UriComponents,
    UriFormat,
    UriHostNameType,
    UriIdnScope,
    UriKind,
    UriPartial,
    UriSyntaxFlags,
]
