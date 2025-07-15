from abc import ABC
from collections.abc import Callable
from typing import ClassVar
from typing import Final
from typing import Generic
from typing import TypeVar
from typing import overload

from Microsoft.Win32.SafeHandles import SafeFileHandle
from Microsoft.Win32.SafeHandles import SafeHandleZeroOrMinusOneIsInvalid
from Microsoft.Win32.SafeHandles import SafeLibraryHandle
from Microsoft.Win32.SafeHandles import SafeProcessHandle
from Microsoft.Win32.SafeHandles import SafeRegistryHandle
from Microsoft.Win32.SafeHandles import SafeThreadHandle
from Microsoft.Win32.SafeHandles import SafeWaitHandle
from System import Array
from System import Delegate
from System import Enum
from System import EventArgs
from System import EventHandler
from System import IDisposable
from System import IntPtr
from System import MarshalByRefObject
from System import Object
from System import Type
from System import Uri
from System import ValueType
from System import __ComObject
from System.Collections import ArrayList
from System.Net import IAuthenticationModule
from System.Net import ICredentialPolicy
from System.Net import NetworkCredential
from System.Net import WebRequest
from System.Net.Cache import RequestCache
from System.Runtime.InteropServices import HandleRef
from System.Runtime.InteropServices import SafeHandle
from System.Runtime.Remoting import ObjRef
from System.Security.AccessControl import AccessControlSections
from System.Security.AccessControl import RegistryRights
from System.Security.AccessControl import RegistrySecurity
from System.Text import StringBuilder
from System.Threading import NativeOverlapped

T = TypeVar("T")

class EventType(Generic[T]):
    def __iadd__(self, other: T): ...
    def __isub__(self, other: T): ...

class ASM_CACHE(ABC, Object):
    """"""

    DOWNLOAD: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    GAC: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    ZAP: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class ASM_NAME(ABC, Object):
    """"""

    ALIAS: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    BUILD_NUMBER: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    CODEBASE_LASTMOD: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    CODEBASE_URL: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    CULTURE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    CUSTOM: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    HASH_ALGID: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    HASH_VALUE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    MAJOR_VERSION: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    MAX_PARAMS: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    MINOR_VERSION: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    MVID: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    NAME: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    NULL_CUSTOM: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    NULL_PUBLIC_KEY: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    NULL_PUBLIC_KEY_TOKEN: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    OSINFO_ARRAY: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PROCESSOR_ID_ARRAY: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PUBLIC_KEY: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PUBLIC_KEY_TOKEN: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    REVISION_NUMBER: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    _32_BIT_ONLY: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class CANOF(ABC, Object):
    """"""

    PARSE_DISPLAY_NAME: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SET_DEFAULT_VALUES: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class Fusion(ABC, Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    @classmethod
    def ReadCache(cls, alAssems: ArrayList, name: str, nFlag: int) -> None:
        """:param alAssems:
        :param name:
        :param nFlag:
        """
    def ToString(self) -> str:
        """:return:"""

class IApplicationContext:
    """"""

    def Get(self, szName: str, pvValue: int, pcbValue: int, dwFlags: int) -> tuple[None, int]:
        """:param szName:
        :param pvValue:
        :param pcbValue:
        :param dwFlags:
        """
    def GetContextNameObject(self, ppName: IAssemblyName) -> tuple[None, IAssemblyName]:
        """:param ppName:"""
    def GetDynamicDirectory(self, wzDynamicDir: int, pdwSize: int) -> tuple[None, int]:
        """:param wzDynamicDir:
        :param pdwSize:
        """
    def Set(self, szName: str, pvValue: int, cbValue: int, dwFlags: int) -> None:
        """:param szName:
        :param pvValue:
        :param cbValue:
        :param dwFlags:
        """
    def SetContextNameObject(self, pName: IAssemblyName) -> None:
        """:param pName:"""

class IAssemblyEnum:
    """"""

    def Clone(self, ppEnum: IAssemblyEnum) -> tuple[int, IAssemblyEnum]:
        """:param ppEnum:
        :return:
        """
    def GetNextAssembly(
        self, ppAppCtx: IApplicationContext, ppName: IAssemblyName, dwFlags: int
    ) -> tuple[int, IApplicationContext, IAssemblyName]:
        """:param ppAppCtx:
        :param ppName:
        :param dwFlags:
        :return:
        """
    def Reset(self) -> int:
        """:return:"""

class IAssemblyName:
    """"""

    def BindToObject(
        self,
        refIID: object,
        pAsmBindSink: object,
        pApplicationContext: IApplicationContext,
        szCodeBase: str,
        llFlags: int,
        pvReserved: int,
        cbReserved: int,
        ppv: int,
    ) -> tuple[int, int]:
        """:param refIID:
        :param pAsmBindSink:
        :param pApplicationContext:
        :param szCodeBase:
        :param llFlags:
        :param pvReserved:
        :param cbReserved:
        :param ppv:
        :return:
        """
    def Clone(self, pName: IAssemblyName) -> tuple[int, IAssemblyName]:
        """:param pName:
        :return:
        """
    def Finalize(self) -> int:
        """:return:"""
    def GetDisplayName(
        self, szDisplayName: IntPtr, pccDisplayName: int, dwDisplayFlags: int
    ) -> int:
        """:param szDisplayName:
        :param pccDisplayName:
        :param dwDisplayFlags:
        :return:
        """
    def GetName(self, lpcwBuffer: int, pwzName: int) -> tuple[int, int, int]:
        """:param lpcwBuffer:
        :param pwzName:
        :return:
        """
    def GetProperty(self, PropertyId: int, pvProperty: IntPtr, pcbProperty: int) -> int:
        """:param PropertyId:
        :param pvProperty:
        :param pcbProperty:
        :return:
        """
    def GetVersion(self, pdwVersionHi: int, pdwVersionLow: int) -> tuple[int, int, int]:
        """:param pdwVersionHi:
        :param pdwVersionLow:
        :return:
        """
    def IsEqual(self, pName: IAssemblyName, dwCmpFlags: int) -> int:
        """:param pName:
        :param dwCmpFlags:
        :return:
        """
    def SetProperty(self, PropertyId: int, pvProperty: IntPtr, cbProperty: int) -> int:
        """:param PropertyId:
        :param pvProperty:
        :param cbProperty:
        :return:
        """

class IInternetSecurityManager:
    """"""

    def GetSecurityId(
        self, pwszUrl: str, pbSecurityId: int, pcbSecurityId: int, dwReserved: int
    ) -> None:
        """:param pwszUrl:
        :param pbSecurityId:
        :param pcbSecurityId:
        :param dwReserved:
        """
    def GetSecuritySite(self, ppSite: None) -> None:
        """:param ppSite:"""
    def GetZoneMappings(self, dwZone: int, ppenumString: None, dwFlags: int) -> None:
        """:param dwZone:
        :param ppenumString:
        :param dwFlags:
        """
    def MapUrlToZone(self, pwszUrl: str, pdwZone: int, dwFlags: int) -> tuple[None, int]:
        """:param pwszUrl:
        :param pdwZone:
        :param dwFlags:
        """
    def ProcessUrlAction(
        self,
        pwszUrl: str,
        dwAction: int,
        pPolicy: int,
        cbPolicy: int,
        pContext: int,
        cbContext: int,
        dwFlags: int,
        dwReserved: int,
    ) -> None:
        """:param pwszUrl:
        :param dwAction:
        :param pPolicy:
        :param cbPolicy:
        :param pContext:
        :param cbContext:
        :param dwFlags:
        :param dwReserved:
        """
    def QueryCustomPolicy(
        self,
        pwszUrl: str,
        guidKey: None,
        ppPolicy: int,
        pcbPolicy: int,
        pContext: int,
        cbContext: int,
        dwReserved: int,
    ) -> None:
        """:param pwszUrl:
        :param guidKey:
        :param ppPolicy:
        :param pcbPolicy:
        :param pContext:
        :param cbContext:
        :param dwReserved:
        """
    def SetSecuritySite(self, pSite: None) -> None:
        """:param pSite:"""
    def SetZoneMapping(self, dwZone: int, lpszPattern: str, dwFlags: int) -> None:
        """:param dwZone:
        :param lpszPattern:
        :param dwFlags:
        """

class InternetSecurityManager(__ComObject):
    """"""

    def __init__(self):
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """:param requestedType:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetLifetimeService(self) -> object:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def InitializeLifetimeService(self) -> object:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class IntranetZoneCredentialPolicy(Object, ICredentialPolicy):
    """"""

    def __init__(self):
        """"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ShouldSendCredential(
        self,
        challengeUri: Uri,
        request: WebRequest,
        credential: NetworkCredential,
        authenticationModule: IAuthenticationModule,
    ) -> bool:
        """:param challengeUri:
        :param request:
        :param credential:
        :param authenticationModule:
        :return:
        """
    def ToString(self) -> str:
        """:return:"""

class NativeMethods(ABC, Object):
    """"""

    BACKWARDS_READ: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    COLOR_WINDOW: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    CREATE_ALWAYS: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    CREATE_NO_WINDOW: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    CREATE_SUSPENDED: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    CREATE_UNICODE_ENVIRONMENT: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    CTRL_BREAK_EVENT: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    CTRL_CLOSE_EVENT: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    CTRL_C_EVENT: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    CTRL_LOGOFF_EVENT: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    CTRL_SHUTDOWN_EVENT: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    DEFAULT_GUI_FONT: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    DUPLICATE_CLOSE_SOURCE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    DUPLICATE_SAME_ACCESS: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    DWORD_SIZE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    ENDSESSION_LOGOFF: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    ERROR_ACCESS_DENIED: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    ERROR_ALREADY_EXISTS: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    ERROR_BAD_COMMAND: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    ERROR_BAD_EXE_FORMAT: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    ERROR_BROKEN_PIPE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    ERROR_BUSY: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    ERROR_CANCELLED: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    ERROR_CLASS_ALREADY_EXISTS: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    ERROR_COUNTER_TIMEOUT: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    ERROR_DDE_FAIL: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    ERROR_DLL_NOT_FOUND: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    ERROR_EVENTLOG_FILE_CHANGED: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    ERROR_EXE_MACHINE_TYPE_MISMATCH: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    ERROR_FILENAME_EXCED_RANGE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    ERROR_FILE_EXISTS: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    ERROR_FILE_NOT_FOUND: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    ERROR_HANDLE_EOF: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    ERROR_INSUFFICIENT_BUFFER: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    ERROR_INVALID_HANDLE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    ERROR_INVALID_NAME: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    ERROR_INVALID_PARAMETER: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    ERROR_IO_INCOMPLETE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    ERROR_IO_PENDING: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    ERROR_LOCK_FAILED: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    ERROR_MORE_DATA: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    ERROR_NONE_MAPPED: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    ERROR_NOT_ENOUGH_MEMORY: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    ERROR_NOT_READY: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    ERROR_NO_ASSOCIATION: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    ERROR_NO_DATA: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    ERROR_OPERATION_ABORTED: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    ERROR_PARTIAL_COPY: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    ERROR_PATH_NOT_FOUND: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    ERROR_PROC_NOT_FOUND: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    ERROR_SHARING_VIOLATION: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    ERROR_SUCCESS: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    E_ABORT: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    E_NOTIMPL: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FILE_ATTRIBUTE_NORMAL: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FILE_FLAG_OVERLAPPED: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FILE_MAP_READ: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FILE_MAP_WRITE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FILE_SHARE_DELETE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FILE_SHARE_READ: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FILE_SHARE_WRITE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FORMAT_MESSAGE_ALLOCATE_BUFFER: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FORMAT_MESSAGE_ARGUMENT_ARRAY: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FORMAT_MESSAGE_FROM_HMODULE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FORMAT_MESSAGE_FROM_STRING: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FORMAT_MESSAGE_FROM_SYSTEM: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FORMAT_MESSAGE_IGNORE_INSERTS: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FORMAT_MESSAGE_MAX_WIDTH_MASK: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FORWARDS_READ: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    GCL_WNDPROC: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    GENERIC_ALL: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    GENERIC_EXECUTE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    GENERIC_READ: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    GENERIC_WRITE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    GHND: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    GMEM_DDESHARE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    GMEM_DISCARDABLE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    GMEM_DISCARDED: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    GMEM_FIXED: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    GMEM_INVALID_HANDLE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    GMEM_LOCKCOUNT: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    GMEM_LOWER: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    GMEM_MODIFY: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    GMEM_MOVEABLE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    GMEM_NOCOMPACT: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    GMEM_NODISCARD: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    GMEM_NOTIFY: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    GMEM_NOT_BANKED: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    GMEM_SHARE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    GMEM_VALID_FLAGS: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    GMEM_ZEROINIT: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    GPTR: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    GWL_STYLE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    GWL_WNDPROC: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    GW_OWNER: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    HKEY_LOCAL_MACHINE: Final[ClassVar[IntPtr]] = ...
    """
    
    :return: 
    """
    HKEY_PERFORMANCE_DATA: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    IMPERSONATION_LEVEL_SecurityAnonymous: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    IMPERSONATION_LEVEL_SecurityDelegation: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    IMPERSONATION_LEVEL_SecurityIdentification: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    IMPERSONATION_LEVEL_SecurityImpersonation: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    INVALID_HANDLE_VALUE: Final[ClassVar[IntPtr]] = ...
    """
    
    :return: 
    """
    KEY_ENUMERATE_SUB_KEYS: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    KEY_NOTIFY: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    KEY_QUERY_VALUE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    KEY_READ: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    LARGE_INTEGER_SIZE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    LOAD_LIBRARY_AS_DATAFILE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    LOAD_WITH_ALTERED_SEARCH_PATH: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    LOGON32_LOGON_BATCH: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    LOGON32_LOGON_INTERACTIVE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    LOGON32_PROVIDER_DEFAULT: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    MAX_PATH: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    MOVEFILE_REPLACE_EXISTING: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    MWMO_INPUTAVAILABLE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    NOTIFY_FOR_THIS_SESSION: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    NtPerfCounterSizeDword: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    NtPerfCounterSizeLarge: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    NtQueryProcessBasicInfo: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    NtQuerySystemProcessInformation: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    NullHandleRef: Final[ClassVar[HandleRef]] = ...
    """
    
    :return: 
    """
    PAGE_READWRITE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PBT_APMBATTERYLOW: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PBT_APMOEMEVENT: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PBT_APMPOWERSTATUSCHANGE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PBT_APMQUERYSTANDBY: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PBT_APMQUERYSTANDBYFAILED: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PBT_APMQUERYSUSPEND: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PBT_APMQUERYSUSPENDFAILED: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PBT_APMRESUMECRITICAL: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PBT_APMRESUMESTANDBY: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PBT_APMRESUMESUSPEND: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PBT_APMSTANDBY: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PBT_APMSUSPEND: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PDH_CALC_NEGATIVE_DENOMINATOR: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PDH_CALC_NEGATIVE_VALUE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PDH_FMT_DOUBLE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PDH_FMT_NOCAP100: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PDH_FMT_NOSCALE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PDH_NO_DATA: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PERF_100NSEC_MULTI_TIMER: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PERF_100NSEC_MULTI_TIMER_INV: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PERF_100NSEC_TIMER: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PERF_100NSEC_TIMER_INV: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PERF_AVERAGE_BASE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PERF_AVERAGE_BULK: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PERF_AVERAGE_TIMER: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PERF_COUNTER_100NS_QUEUELEN_TYPE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PERF_COUNTER_BASE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PERF_COUNTER_BULK_COUNT: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PERF_COUNTER_COUNTER: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PERF_COUNTER_DELTA: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PERF_COUNTER_ELAPSED: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PERF_COUNTER_FRACTION: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PERF_COUNTER_HISTOGRAM: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PERF_COUNTER_LARGE_DELTA: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PERF_COUNTER_LARGE_QUEUELEN_TYPE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PERF_COUNTER_LARGE_RAWCOUNT: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PERF_COUNTER_LARGE_RAWCOUNT_HEX: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PERF_COUNTER_MULTI_BASE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PERF_COUNTER_MULTI_TIMER: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PERF_COUNTER_MULTI_TIMER_INV: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PERF_COUNTER_NODATA: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PERF_COUNTER_OBJ_TIME_QUEUELEN_TYPE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PERF_COUNTER_PRECISION: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PERF_COUNTER_QUEUELEN: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PERF_COUNTER_QUEUELEN_TYPE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PERF_COUNTER_RATE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PERF_COUNTER_RAWCOUNT: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PERF_COUNTER_RAWCOUNT_HEX: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PERF_COUNTER_TEXT: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PERF_COUNTER_TIMER: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PERF_COUNTER_TIMER_INV: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PERF_COUNTER_VALUE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PERF_DELTA_BASE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PERF_DELTA_COUNTER: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PERF_DETAIL_ADVANCED: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PERF_DETAIL_EXPERT: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PERF_DETAIL_NOVICE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PERF_DETAIL_WIZARD: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PERF_DISPLAY_NOSHOW: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PERF_DISPLAY_NO_SUFFIX: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PERF_DISPLAY_PERCENT: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PERF_DISPLAY_PER_SEC: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PERF_DISPLAY_SECONDS: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PERF_ELAPSED_TIME: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PERF_INVERSE_COUNTER: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PERF_LARGE_RAW_BASE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PERF_LARGE_RAW_FRACTION: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PERF_MULTI_COUNTER: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PERF_NO_INSTANCES: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PERF_NO_UNIQUE_ID: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PERF_NUMBER_DECIMAL: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PERF_NUMBER_DEC_1000: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PERF_NUMBER_HEX: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PERF_OBJECT_TIMER: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PERF_OBJ_TIME_TIME: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PERF_OBJ_TIME_TIMER: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PERF_PRECISION_100NS_TIMER: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PERF_PRECISION_OBJECT_TIMER: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PERF_PRECISION_SYSTEM_TIMER: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PERF_RAW_BASE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PERF_RAW_FRACTION: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PERF_SAMPLE_BASE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PERF_SAMPLE_COUNTER: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PERF_SAMPLE_FRACTION: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PERF_SIZE_DWORD: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PERF_SIZE_LARGE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PERF_SIZE_VARIABLE_LEN: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PERF_SIZE_ZERO: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PERF_TEXT_ASCII: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PERF_TEXT_UNICODE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PERF_TIMER_100NS: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PERF_TIMER_TICK: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PERF_TYPE_COUNTER: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PERF_TYPE_NUMBER: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PERF_TYPE_TEXT: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PERF_TYPE_ZERO: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PIPE_ACCESS_DUPLEX: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PIPE_ACCESS_INBOUND: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PIPE_ACCESS_OUTBOUND: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PIPE_NOWAIT: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PIPE_READMODE_BYTE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PIPE_READMODE_MESSAGE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PIPE_SINGLE_INSTANCES: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PIPE_TYPE_BYTE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PIPE_TYPE_MESSAGE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PIPE_UNLIMITED_INSTANCES: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PIPE_WAIT: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PM_REMOVE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PROCESS_ALL_ACCESS: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PROCESS_CREATE_PROCESS: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PROCESS_CREATE_THREAD: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PROCESS_DUP_HANDLE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PROCESS_QUERY_INFORMATION: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PROCESS_QUERY_LIMITED_INFORMATION: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PROCESS_SET_INFORMATION: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PROCESS_SET_QUOTA: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PROCESS_SET_SESSIONID: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PROCESS_TERMINATE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PROCESS_VM_OPERATION: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PROCESS_VM_READ: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    PROCESS_VM_WRITE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    QS_ALLEVENTS: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    QS_ALLINPUT: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    QS_ALLPOSTMESSAGE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    QS_HOTKEY: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    QS_INPUT: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    QS_KEY: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    QS_MOUSE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    QS_MOUSEBUTTON: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    QS_MOUSEMOVE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    QS_PAINT: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    QS_POSTMESSAGE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    QS_SENDMESSAGE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    QS_TIMER: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    READ_CONTROL: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    REG_BINARY: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    REG_MULTI_SZ: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    RPC_S_CALL_FAILED: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    RPC_S_SERVER_UNAVAILABLE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SECURITY_DESCRIPTOR_REVISION: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SEEK_READ: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SEE_MASK_ASYNCOK: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SEE_MASK_CLASSKEY: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SEE_MASK_CLASSNAME: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SEE_MASK_CONNECTNETDRV: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SEE_MASK_DOENVSUBST: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SEE_MASK_FLAG_DDEWAIT: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SEE_MASK_FLAG_NO_UI: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SEE_MASK_HOTKEY: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SEE_MASK_ICON: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SEE_MASK_IDLIST: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SEE_MASK_INVOKEIDLIST: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SEE_MASK_NOCLOSEPROCESS: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SEE_MASK_NO_CONSOLE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SEE_MASK_UNICODE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SE_ERR_ACCESSDENIED: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SE_ERR_ASSOCINCOMPLETE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SE_ERR_DDEBUSY: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SE_ERR_DDEFAIL: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SE_ERR_DDETIMEOUT: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SE_ERR_DLLNOTFOUND: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SE_ERR_FNF: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SE_ERR_NOASSOC: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SE_ERR_OOM: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SE_ERR_PNF: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SE_ERR_SHARE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SE_PRIVILEGE_ENABLED: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SHGFI_TYPENAME: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SHGFI_USEFILEATTRIBUTES: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SMTO_ABORTIFHUNG: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SM_CYSCREEN: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_GETACCESSTIMEOUT: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_GETACTIVEWINDOWTRACKING: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_GETACTIVEWNDTRKTIMEOUT: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_GETACTIVEWNDTRKZORDER: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_GETANIMATION: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_GETBEEP: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_GETBORDER: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_GETCARETWIDTH: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_GETCOMBOBOXANIMATION: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_GETCURSORSHADOW: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_GETDEFAULTINPUTLANG: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_GETDESKWALLPAPER: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_GETDRAGFULLWINDOWS: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_GETFASTTASKSWITCH: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_GETFILTERKEYS: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_GETFONTSMOOTHING: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_GETFOREGROUNDFLASHCOUNT: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_GETFOREGROUNDLOCKTIMEOUT: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_GETGRADIENTCAPTIONS: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_GETGRIDGRANULARITY: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_GETHIGHCONTRAST: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_GETHOTTRACKING: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_GETICONMETRICS: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_GETICONTITLELOGFONT: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_GETICONTITLEWRAP: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_GETKEYBOARDCUES: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_GETKEYBOARDDELAY: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_GETKEYBOARDPREF: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_GETKEYBOARDSPEED: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_GETLISTBOXSMOOTHSCROLLING: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_GETLOWPOWERACTIVE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_GETLOWPOWERTIMEOUT: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_GETMENUANIMATION: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_GETMENUDROPALIGNMENT: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_GETMENUFADE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_GETMENUSHOWDELAY: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_GETMENUUNDERLINES: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_GETMINIMIZEDMETRICS: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_GETMOUSE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_GETMOUSEHOVERHEIGHT: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_GETMOUSEHOVERTIME: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_GETMOUSEHOVERWIDTH: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_GETMOUSEKEYS: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_GETMOUSESPEED: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_GETMOUSETRAILS: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_GETNONCLIENTMETRICS: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_GETPOWEROFFACTIVE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_GETPOWEROFFTIMEOUT: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_GETSCREENREADER: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_GETSCREENSAVEACTIVE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_GETSCREENSAVERRUNNING: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_GETSCREENSAVETIMEOUT: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_GETSELECTIONFADE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_GETSERIALKEYS: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_GETSHOWIMEUI: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_GETSHOWSOUNDS: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_GETSNAPTODEFBUTTON: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_GETSOUNDSENTRY: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_GETSTICKYKEYS: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_GETTOGGLEKEYS: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_GETTOOLTIPANIMATION: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_GETTOOLTIPFADE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_GETUIEFFECTS: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_GETWHEELSCROLLLINES: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_GETWINDOWSEXTENSION: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_GETWORKAREA: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_ICONHORIZONTALSPACING: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_ICONVERTICALSPACING: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_LANGDRIVER: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_SCREENSAVERRUNNING: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_SETACCESSTIMEOUT: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_SETACTIVEWINDOWTRACKING: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_SETACTIVEWNDTRKTIMEOUT: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_SETACTIVEWNDTRKZORDER: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_SETANIMATION: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_SETBEEP: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_SETBORDER: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_SETCARETWIDTH: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_SETCOMBOBOXANIMATION: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_SETCURSORS: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_SETCURSORSHADOW: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_SETDEFAULTINPUTLANG: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_SETDESKPATTERN: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_SETDESKWALLPAPER: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_SETDOUBLECLICKTIME: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_SETDOUBLECLKHEIGHT: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_SETDOUBLECLKWIDTH: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_SETDRAGFULLWINDOWS: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_SETDRAGHEIGHT: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_SETDRAGWIDTH: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_SETFASTTASKSWITCH: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_SETFILTERKEYS: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_SETFONTSMOOTHING: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_SETFOREGROUNDFLASHCOUNT: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_SETFOREGROUNDLOCKTIMEOUT: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_SETGRADIENTCAPTIONS: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_SETGRIDGRANULARITY: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_SETHANDHELD: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_SETHIGHCONTRAST: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_SETHOTTRACKING: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_SETICONMETRICS: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_SETICONS: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_SETICONTITLELOGFONT: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_SETICONTITLEWRAP: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_SETKEYBOARDCUES: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_SETKEYBOARDDELAY: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_SETKEYBOARDPREF: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_SETKEYBOARDSPEED: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_SETLANGTOGGLE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_SETLISTBOXSMOOTHSCROLLING: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_SETLOWPOWERACTIVE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_SETLOWPOWERTIMEOUT: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_SETMENUANIMATION: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_SETMENUDROPALIGNMENT: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_SETMENUFADE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_SETMENUSHOWDELAY: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_SETMENUUNDERLINES: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_SETMINIMIZEDMETRICS: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_SETMOUSE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_SETMOUSEBUTTONSWAP: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_SETMOUSEHOVERHEIGHT: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_SETMOUSEHOVERTIME: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_SETMOUSEHOVERWIDTH: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_SETMOUSEKEYS: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_SETMOUSESPEED: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_SETMOUSETRAILS: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_SETNONCLIENTMETRICS: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_SETPENWINDOWS: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_SETPOWEROFFACTIVE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_SETPOWEROFFTIMEOUT: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_SETSCREENREADER: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_SETSCREENSAVEACTIVE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_SETSCREENSAVERRUNNING: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_SETSCREENSAVETIMEOUT: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_SETSELECTIONFADE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_SETSERIALKEYS: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_SETSHOWIMEUI: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_SETSHOWSOUNDS: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_SETSNAPTODEFBUTTON: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_SETSOUNDSENTRY: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_SETSTICKYKEYS: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_SETTOGGLEKEYS: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_SETTOOLTIPANIMATION: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_SETTOOLTIPFADE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_SETUIEFFECTS: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_SETWHEELSCROLLLINES: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SPI_SETWORKAREA: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    STANDARD_RIGHTS_READ: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    STANDARD_RIGHTS_REQUIRED: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    STARTF_USESHOWWINDOW: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    STARTF_USESTDHANDLES: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    STATUS_INFO_LENGTH_MISMATCH: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    STD_ERROR_HANDLE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    STD_INPUT_HANDLE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    STD_OUTPUT_HANDLE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    STILL_ACTIVE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SW_HIDE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SW_MAX: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SW_MAXIMIZE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SW_MINIMIZE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SW_NORMAL: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SW_RESTORE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SW_SHOW: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SW_SHOWDEFAULT: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SW_SHOWMAXIMIZED: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SW_SHOWMINIMIZED: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SW_SHOWMINNOACTIVE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SW_SHOWNA: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SW_SHOWNOACTIVATE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SW_SHOWNORMAL: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SYNCHRONIZE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    S_OK: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    TH32CS_INHERIT: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    TH32CS_SNAPHEAPLIST: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    TH32CS_SNAPMODULE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    TH32CS_SNAPPROCESS: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    TH32CS_SNAPTHREAD: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    THREAD_DIRECT_IMPERSONATION: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    THREAD_GET_CONTEXT: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    THREAD_IMPERSONATE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    THREAD_QUERY_INFORMATION: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    THREAD_SET_CONTEXT: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    THREAD_SET_INFORMATION: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    THREAD_SET_THREAD_TOKEN: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    THREAD_SUSPEND_RESUME: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    THREAD_TERMINATE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    TOKEN_ADJUST_PRIVILEGES: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    TOKEN_ALL_ACCESS: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    TOKEN_EXECUTE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    TOKEN_IMPERSONATE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    TOKEN_QUERY: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    TOKEN_READ: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    TOKEN_TYPE_TokenImpersonation: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    TOKEN_TYPE_TokenPrimary: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    UISF_HIDEACCEL: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    UISF_HIDEFOCUS: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    UIS_CLEAR: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    UIS_SET: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    UOI_FLAGS: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    UOI_NAME: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    UOI_TYPE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    UOI_USER_SID: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    USERCLASSTYPE_FULL: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    VER_PLATFORM_WIN32_NT: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    VFT2_DRV_COMM: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    VFT2_DRV_DISPLAY: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    VFT2_DRV_INPUTMETHOD: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    VFT2_DRV_INSTALLABLE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    VFT2_DRV_KEYBOARD: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    VFT2_DRV_LANGUAGE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    VFT2_DRV_MOUSE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    VFT2_DRV_NETWORK: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    VFT2_DRV_PRINTER: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    VFT2_DRV_SOUND: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    VFT2_DRV_SYSTEM: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    VFT2_FONT_RASTER: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    VFT2_FONT_TRUETYPE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    VFT2_FONT_VECTOR: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    VFT2_UNKNOWN: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    VFT_APP: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    VFT_DLL: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    VFT_DRV: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    VFT_FONT: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    VFT_STATIC_LIB: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    VFT_UNKNOWN: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    VFT_VXD: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    VS_FFI_FILEFLAGSMASK: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    VS_FFI_SIGNATURE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    VS_FFI_STRUCVERSION: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    VS_FF_DEBUG: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    VS_FF_INFOINFERRED: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    VS_FF_PATCHED: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    VS_FF_PRERELEASE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    VS_FF_PRIVATEBUILD: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    VS_FF_SPECIALBUILD: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    VS_FILE_INFO: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    VS_USER_DEFINED: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    VS_VERSION_INFO: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    WAIT_ABANDONED: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    WAIT_ABANDONED_0: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    WAIT_FAILED: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    WAIT_OBJECT_0: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    WAIT_TIMEOUT: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    WHITENESS: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    WM_CLOSE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    WM_COMPACTING: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    WM_CREATETIMER: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    WM_DISPLAYCHANGE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    WM_ENDSESSION: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    WM_FONTCHANGE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    WM_KILLTIMER: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    WM_NULL: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    WM_PALETTECHANGED: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    WM_POWERBROADCAST: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    WM_QUERYENDSESSION: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    WM_QUIT: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    WM_REFLECT: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    WM_SETTINGCHANGE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    WM_SYSCOLORCHANGE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    WM_THEMECHANGED: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    WM_TIMECHANGE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    WM_TIMER: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    WM_USER: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    WM_WTSSESSION_CHANGE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    WSF_VISIBLE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    WS_DISABLED: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    WS_POPUP: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    WS_VISIBLE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    WTS_CONSOLE_CONNECT: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    WTS_CONSOLE_DISCONNECT: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    WTS_REMOTE_CONNECT: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    WTS_REMOTE_DISCONNECT: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    WTS_SESSION_LOCK: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    WTS_SESSION_LOGOFF: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    WTS_SESSION_LOGON: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    WTS_SESSION_REMOTE_CONTROL: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    WTS_SESSION_UNLOCK: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    @classmethod
    def AdjustTokenPrivileges(
        cls,
        TokenHandle: HandleRef,
        DisableAllPrivileges: bool,
        NewState: NativeMethods.TokenPrivileges,
        BufferLength: int,
        PreviousState: IntPtr,
        ReturnLength: IntPtr,
    ) -> bool:
        """:param TokenHandle:
        :param DisableAllPrivileges:
        :param NewState:
        :param BufferLength:
        :param PreviousState:
        :param ReturnLength:
        :return:
        """
    @classmethod
    def CreateFile(
        cls,
        lpFileName: str,
        dwDesiredAccess: int,
        dwShareMode: int,
        lpSecurityAttributes: NativeMethods.SECURITY_ATTRIBUTES,
        dwCreationDisposition: int,
        dwFlagsAndAttributes: int,
        hTemplateFile: SafeFileHandle,
    ) -> SafeFileHandle:
        """:param lpFileName:
        :param dwDesiredAccess:
        :param dwShareMode:
        :param lpSecurityAttributes:
        :param dwCreationDisposition:
        :param dwFlagsAndAttributes:
        :param hTemplateFile:
        :return:
        """
    @classmethod
    def CreatePipe(
        cls,
        hReadPipe: SafeFileHandle,
        hWritePipe: SafeFileHandle,
        lpPipeAttributes: NativeMethods.SECURITY_ATTRIBUTES,
        nSize: int,
    ) -> tuple[bool, SafeFileHandle, SafeFileHandle]:
        """:param hReadPipe:
        :param hWritePipe:
        :param lpPipeAttributes:
        :param nSize:
        :return:
        """
    @classmethod
    def CreateProcess(
        cls,
        lpApplicationName: str,
        lpCommandLine: StringBuilder,
        lpProcessAttributes: NativeMethods.SECURITY_ATTRIBUTES,
        lpThreadAttributes: NativeMethods.SECURITY_ATTRIBUTES,
        bInheritHandles: bool,
        dwCreationFlags: int,
        lpEnvironment: IntPtr,
        lpCurrentDirectory: str,
        lpStartupInfo: NativeMethods.STARTUPINFO,
        lpProcessInformation: SafeNativeMethods.PROCESS_INFORMATION,
    ) -> bool:
        """:param lpApplicationName:
        :param lpCommandLine:
        :param lpProcessAttributes:
        :param lpThreadAttributes:
        :param bInheritHandles:
        :param dwCreationFlags:
        :param lpEnvironment:
        :param lpCurrentDirectory:
        :param lpStartupInfo:
        :param lpProcessInformation:
        :return:
        """
    @classmethod
    def CreateProcessAsUser(
        cls,
        hToken: SafeHandle,
        lpApplicationName: str,
        lpCommandLine: str,
        lpProcessAttributes: NativeMethods.SECURITY_ATTRIBUTES,
        lpThreadAttributes: NativeMethods.SECURITY_ATTRIBUTES,
        bInheritHandles: bool,
        dwCreationFlags: int,
        lpEnvironment: HandleRef,
        lpCurrentDirectory: str,
        lpStartupInfo: NativeMethods.STARTUPINFO,
        lpProcessInformation: SafeNativeMethods.PROCESS_INFORMATION,
    ) -> bool:
        """:param hToken:
        :param lpApplicationName:
        :param lpCommandLine:
        :param lpProcessAttributes:
        :param lpThreadAttributes:
        :param bInheritHandles:
        :param dwCreationFlags:
        :param lpEnvironment:
        :param lpCurrentDirectory:
        :param lpStartupInfo:
        :param lpProcessInformation:
        :return:
        """
    @classmethod
    def CreateToolhelp32Snapshot(cls, flags: int, processId: int) -> IntPtr:
        """:param flags:
        :param processId:
        :return:
        """
    @classmethod
    @overload
    def DuplicateHandle(
        cls,
        hSourceProcessHandle: HandleRef,
        hSourceHandle: SafeHandle,
        hTargetProcess: HandleRef,
        targetHandle: SafeFileHandle,
        dwDesiredAccess: int,
        bInheritHandle: bool,
        dwOptions: int,
    ) -> tuple[bool, SafeFileHandle]:
        """:param hSourceProcessHandle:
        :param hSourceHandle:
        :param hTargetProcess:
        :param targetHandle:
        :param dwDesiredAccess:
        :param bInheritHandle:
        :param dwOptions:
        :return:
        """
    @classmethod
    @overload
    def DuplicateHandle(
        cls,
        hSourceProcessHandle: HandleRef,
        hSourceHandle: SafeHandle,
        hTargetProcess: HandleRef,
        targetHandle: SafeWaitHandle,
        dwDesiredAccess: int,
        bInheritHandle: bool,
        dwOptions: int,
    ) -> tuple[bool, SafeWaitHandle]:
        """:param hSourceProcessHandle:
        :param hSourceHandle:
        :param hTargetProcess:
        :param targetHandle:
        :param dwDesiredAccess:
        :param bInheritHandle:
        :param dwOptions:
        :return:
        """
    @classmethod
    def EnumProcessModules(
        cls, handle: SafeProcessHandle, modules: IntPtr, size: int, needed: int
    ) -> bool:
        """:param handle:
        :param modules:
        :param size:
        :param needed:
        :return:
        """
    @classmethod
    def EnumProcesses(cls, processIds: Array[int], size: int, needed: int) -> tuple[bool, int]:
        """:param processIds:
        :param size:
        :param needed:
        :return:
        """
    @classmethod
    def EnumWindows(
        cls, callback: NativeMethods.EnumThreadWindowsCallback, extraData: IntPtr
    ) -> bool:
        """:param callback:
        :param extraData:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @classmethod
    def GetCurrentProcess(cls) -> IntPtr:
        """:return:"""
    @classmethod
    def GetCurrentProcessId(cls) -> int:
        """:return:"""
    @classmethod
    def GetExitCodeProcess(
        cls, processHandle: SafeProcessHandle, exitCode: int
    ) -> tuple[bool, int]:
        """:param processHandle:
        :param exitCode:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    @classmethod
    def GetModuleBaseName(
        cls,
        processHandle: SafeProcessHandle,
        moduleHandle: HandleRef,
        baseName: StringBuilder,
        size: int,
    ) -> int:
        """:param processHandle:
        :param moduleHandle:
        :param baseName:
        :param size:
        :return:
        """
    @classmethod
    @overload
    def GetModuleFileNameEx(
        cls,
        processHandle: SafeProcessHandle,
        moduleHandle: HandleRef,
        baseName: StringBuilder,
        size: int,
    ) -> int:
        """:param processHandle:
        :param moduleHandle:
        :param baseName:
        :param size:
        :return:
        """
    @classmethod
    @overload
    def GetModuleFileNameEx(
        cls,
        processHandle: HandleRef,
        moduleHandle: HandleRef,
        baseName: StringBuilder,
        size: int,
    ) -> int:
        """:param processHandle:
        :param moduleHandle:
        :param baseName:
        :param size:
        :return:
        """
    @classmethod
    def GetModuleInformation(
        cls,
        processHandle: SafeProcessHandle,
        moduleHandle: HandleRef,
        ntModuleInfo: NativeMethods.NtModuleInfo,
        size: int,
    ) -> bool:
        """:param processHandle:
        :param moduleHandle:
        :param ntModuleInfo:
        :param size:
        :return:
        """
    @classmethod
    def GetPriorityClass(cls, handle: SafeProcessHandle) -> int:
        """:param handle:
        :return:
        """
    @classmethod
    def GetProcessAffinityMask(
        cls, handle: SafeProcessHandle, processMask: IntPtr, systemMask: IntPtr
    ) -> tuple[bool, IntPtr, IntPtr]:
        """:param handle:
        :param processMask:
        :param systemMask:
        :return:
        """
    @classmethod
    def GetProcessPriorityBoost(
        cls, handle: SafeProcessHandle, disabled: bool
    ) -> tuple[bool, bool]:
        """:param handle:
        :param disabled:
        :return:
        """
    @classmethod
    def GetProcessTimes(
        cls, handle: SafeProcessHandle, creation: int, exit: int, kernel: int, user: int
    ) -> tuple[bool, int, int, int, int]:
        """:param handle:
        :param creation:
        :param exit:
        :param kernel:
        :param user:
        :return:
        """
    @classmethod
    def GetProcessWorkingSetSize(
        cls, handle: SafeProcessHandle, min: IntPtr, max: IntPtr
    ) -> tuple[bool, IntPtr, IntPtr]:
        """:param handle:
        :param min:
        :param max:
        :return:
        """
    @classmethod
    def GetStdHandle(cls, whichHandle: int) -> IntPtr:
        """:param whichHandle:
        :return:
        """
    @classmethod
    def GetThreadPriority(cls, handle: SafeThreadHandle) -> int:
        """:param handle:
        :return:
        """
    @classmethod
    def GetThreadPriorityBoost(cls, handle: SafeThreadHandle, disabled: bool) -> tuple[bool, bool]:
        """:param handle:
        :param disabled:
        :return:
        """
    @classmethod
    def GetThreadTimes(
        cls, handle: SafeThreadHandle, creation: int, exit: int, kernel: int, user: int
    ) -> tuple[bool, int, int, int, int]:
        """:param handle:
        :param creation:
        :param exit:
        :param kernel:
        :param user:
        :return:
        """
    def GetType(self) -> Type:
        """:return:"""
    @classmethod
    def GetWindow(cls, hWnd: HandleRef, uCmd: int) -> IntPtr:
        """:param hWnd:
        :param uCmd:
        :return:
        """
    @classmethod
    def GetWindowLong(cls, hWnd: HandleRef, nIndex: int) -> int:
        """:param hWnd:
        :param nIndex:
        :return:
        """
    @classmethod
    def GetWindowText(cls, hWnd: HandleRef, lpString: StringBuilder, nMaxCount: int) -> int:
        """:param hWnd:
        :param lpString:
        :param nMaxCount:
        :return:
        """
    @classmethod
    def GetWindowTextLength(cls, hWnd: HandleRef) -> int:
        """:param hWnd:
        :return:
        """
    @classmethod
    def GetWindowThreadProcessId(cls, handle: HandleRef, processId: int) -> tuple[int, int]:
        """:param handle:
        :param processId:
        :return:
        """
    @classmethod
    def IsWindowVisible(cls, hWnd: HandleRef) -> bool:
        """:param hWnd:
        :return:
        """
    @classmethod
    def LookupPrivilegeValue(
        cls, lpSystemName: str, lpName: str, lpLuid: LUID
    ) -> tuple[bool, LUID]:
        """:param lpSystemName:
        :param lpName:
        :param lpLuid:
        :return:
        """
    @classmethod
    def Module32First(cls, handle: HandleRef, entry: IntPtr) -> bool:
        """:param handle:
        :param entry:
        :return:
        """
    @classmethod
    def Module32Next(cls, handle: HandleRef, entry: IntPtr) -> bool:
        """:param handle:
        :param entry:
        :return:
        """
    @classmethod
    def NtQueryInformationProcess(
        cls,
        processHandle: SafeProcessHandle,
        query: int,
        info: NativeMethods.NtProcessBasicInfo,
        size: int,
        returnedSize: Array[int],
    ) -> int:
        """:param processHandle:
        :param query:
        :param info:
        :param size:
        :param returnedSize:
        :return:
        """
    @classmethod
    def NtQuerySystemInformation(
        cls, query: int, dataPtr: IntPtr, size: int, returnedSize: int
    ) -> tuple[int, int]:
        """:param query:
        :param dataPtr:
        :param size:
        :param returnedSize:
        :return:
        """
    @classmethod
    def OpenProcess(cls, access: int, inherit: bool, processId: int) -> SafeProcessHandle:
        """:param access:
        :param inherit:
        :param processId:
        :return:
        """
    @classmethod
    def OpenProcessToken(
        cls, ProcessHandle: HandleRef, DesiredAccess: int, TokenHandle: IntPtr
    ) -> tuple[bool, IntPtr]:
        """:param ProcessHandle:
        :param DesiredAccess:
        :param TokenHandle:
        :return:
        """
    @classmethod
    def OpenThread(cls, access: int, inherit: bool, threadId: int) -> SafeThreadHandle:
        """:param access:
        :param inherit:
        :param threadId:
        :return:
        """
    @classmethod
    def PostMessage(cls, hwnd: HandleRef, msg: int, wparam: IntPtr, lparam: IntPtr) -> int:
        """:param hwnd:
        :param msg:
        :param wparam:
        :param lparam:
        :return:
        """
    @classmethod
    def Process32First(cls, handle: HandleRef, entry: IntPtr) -> bool:
        """:param handle:
        :param entry:
        :return:
        """
    @classmethod
    def Process32Next(cls, handle: HandleRef, entry: IntPtr) -> bool:
        """:param handle:
        :param entry:
        :return:
        """
    @classmethod
    def RtlGetVersion(
        cls, lpVersionInformation: RTL_OSVERSIONINFOEX
    ) -> tuple[int, RTL_OSVERSIONINFOEX]:
        """:param lpVersionInformation:
        :return:
        """
    @classmethod
    def SendMessageTimeout(
        cls,
        hWnd: HandleRef,
        msg: int,
        wParam: IntPtr,
        lParam: IntPtr,
        flags: int,
        timeout: int,
        pdwResult: IntPtr,
    ) -> tuple[IntPtr, IntPtr]:
        """:param hWnd:
        :param msg:
        :param wParam:
        :param lParam:
        :param flags:
        :param timeout:
        :param pdwResult:
        :return:
        """
    @classmethod
    def SetPriorityClass(cls, handle: SafeProcessHandle, priorityClass: int) -> bool:
        """:param handle:
        :param priorityClass:
        :return:
        """
    @classmethod
    def SetProcessAffinityMask(cls, handle: SafeProcessHandle, mask: IntPtr) -> bool:
        """:param handle:
        :param mask:
        :return:
        """
    @classmethod
    def SetProcessPriorityBoost(cls, handle: SafeProcessHandle, disabled: bool) -> bool:
        """:param handle:
        :param disabled:
        :return:
        """
    @classmethod
    def SetProcessWorkingSetSize(cls, handle: SafeProcessHandle, min: IntPtr, max: IntPtr) -> bool:
        """:param handle:
        :param min:
        :param max:
        :return:
        """
    @classmethod
    def SetThreadAffinityMask(cls, handle: SafeThreadHandle, mask: HandleRef) -> IntPtr:
        """:param handle:
        :param mask:
        :return:
        """
    @classmethod
    def SetThreadIdealProcessor(cls, handle: SafeThreadHandle, processor: int) -> int:
        """:param handle:
        :param processor:
        :return:
        """
    @classmethod
    def SetThreadPriority(cls, handle: SafeThreadHandle, priority: int) -> bool:
        """:param handle:
        :param priority:
        :return:
        """
    @classmethod
    def SetThreadPriorityBoost(cls, handle: SafeThreadHandle, disabled: bool) -> bool:
        """:param handle:
        :param disabled:
        :return:
        """
    @classmethod
    def ShellExecuteEx(cls, info: NativeMethods.ShellExecuteInfo) -> bool:
        """:param info:
        :return:
        """
    @classmethod
    def TerminateProcess(cls, processHandle: SafeProcessHandle, exitCode: int) -> bool:
        """:param processHandle:
        :param exitCode:
        :return:
        """
    @classmethod
    def Thread32First(cls, handle: HandleRef, entry: NativeMethods.WinThreadEntry) -> bool:
        """:param handle:
        :param entry:
        :return:
        """
    @classmethod
    def Thread32Next(cls, handle: HandleRef, entry: NativeMethods.WinThreadEntry) -> bool:
        """:param handle:
        :param entry:
        :return:
        """
    def ToString(self) -> str:
        """:return:"""
    @classmethod
    def WaitForInputIdle(cls, handle: SafeProcessHandle, milliseconds: int) -> int:
        """:param handle:
        :param milliseconds:
        :return:
        """
    ConHndlr: Callable[[int], int] = ...
    """
    
    :param signalType: 
    :return: 
    """

    class MSG(ValueType):
        """"""

        hwnd: Final[IntPtr] = ...
        """"""
        lParam: Final[IntPtr] = ...
        """"""
        message: Final[int] = ...
        """"""
        pt_x: Final[int] = ...
        """"""
        pt_y: Final[int] = ...
        """"""
        time: Final[int] = ...
        """"""
        wParam: Final[IntPtr] = ...
        """"""
        def Equals(self, obj: object) -> bool:
            """:param obj:
            :return:
            """
        def GetHashCode(self) -> int:
            """:return:"""
        def GetType(self) -> Type:
            """:return:"""
        def ToString(self) -> str:
            """:return:"""

    class PDH_FMT_COUNTERVALUE(Object):
        """"""

        CStatus: Final[int] = ...
        """"""
        data: Final[float] = ...
        """"""
        def __init__(self):
            """"""
        def Equals(self, obj: object) -> bool:
            """:param obj:
            :return:
            """
        def GetHashCode(self) -> int:
            """:return:"""
        def GetType(self) -> Type:
            """:return:"""
        def ToString(self) -> str:
            """:return:"""

    class PDH_RAW_COUNTER(Object):
        """"""

        CStatus: Final[int] = ...
        """"""
        FirstValue: Final[int] = ...
        """"""
        MultiCount: Final[int] = ...
        """"""
        SecondValue: Final[int] = ...
        """"""
        TimeStamp: Final[int] = ...
        """"""
        def __init__(self):
            """"""
        def Equals(self, obj: object) -> bool:
            """:param obj:
            :return:
            """
        def GetHashCode(self) -> int:
            """:return:"""
        def GetType(self) -> Type:
            """:return:"""
        def ToString(self) -> str:
            """:return:"""

    class RTL_OSVERSIONINFOEX(ValueType):
        """"""

        def Equals(self, obj: object) -> bool:
            """:param obj:
            :return:
            """
        def GetHashCode(self) -> int:
            """:return:"""
        def GetType(self) -> Type:
            """:return:"""
        def ToString(self) -> str:
            """:return:"""

    class StructFormat(Enum):
        """"""

        Ansi: StructFormat = ...
        """"""
        Unicode: StructFormat = ...
        """"""
        Auto: StructFormat = ...
        """"""

    class StructFormatEnum(Enum):
        """"""

        Ansi: StructFormatEnum = ...
        """"""
        Unicode: StructFormatEnum = ...
        """"""
        Auto: StructFormatEnum = ...
        """"""

    WndProc: Callable[[IntPtr, int, IntPtr, IntPtr], IntPtr] = ...
    """
    
    :param hWnd: 
    :param msg: 
    :param wParam: 
    :param lParam: 
    :return: 
    """

class OAVariantLib(ABC, Object):
    """"""

    AlphaBool: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    CalendarHijri: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    LocalBool: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    NoUserOverride: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    NoValueProp: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class PowerModeChangedEventArgs(EventArgs):
    """"""

    def __init__(self, mode: PowerModes):
        """:param mode:"""
    @property
    def Mode(self) -> PowerModes:
        """:return:"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

PowerModeChangedEventHandler: Callable[[object, PowerModeChangedEventArgs], None] = ...
"""

:param sender: 
:param e: 
"""

class PowerModes(Enum):
    """"""

    Resume: PowerModes = ...
    """"""
    StatusChange: PowerModes = ...
    """"""
    Suspend: PowerModes = ...
    """"""

class Registry(ABC, Object):
    """"""

    ClassesRoot: Final[ClassVar[RegistryKey]] = ...
    """
    
    :return: 
    """
    CurrentConfig: Final[ClassVar[RegistryKey]] = ...
    """
    
    :return: 
    """
    CurrentUser: Final[ClassVar[RegistryKey]] = ...
    """
    
    :return: 
    """
    DynData: Final[ClassVar[RegistryKey]] = ...
    """
    
    :return: 
    """
    LocalMachine: Final[ClassVar[RegistryKey]] = ...
    """
    
    :return: 
    """
    PerformanceData: Final[ClassVar[RegistryKey]] = ...
    """
    
    :return: 
    """
    Users: Final[ClassVar[RegistryKey]] = ...
    """
    
    :return: 
    """
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    @classmethod
    def GetValue(cls, keyName: str, valueName: str, defaultValue: object) -> object:
        """:param keyName:
        :param valueName:
        :param defaultValue:
        :return:
        """
    @classmethod
    @overload
    def SetValue(cls, keyName: str, valueName: str, value: object) -> None:
        """:param keyName:
        :param valueName:
        :param value:
        """
    @classmethod
    @overload
    def SetValue(
        cls, keyName: str, valueName: str, value: object, valueKind: RegistryValueKind
    ) -> None:
        """:param keyName:
        :param valueName:
        :param value:
        :param valueKind:
        """
    def ToString(self) -> str:
        """:return:"""

class RegistryHive(Enum):
    """"""

    ClassesRoot: RegistryHive = ...
    """"""
    CurrentUser: RegistryHive = ...
    """"""
    LocalMachine: RegistryHive = ...
    """"""
    Users: RegistryHive = ...
    """"""
    PerformanceData: RegistryHive = ...
    """"""
    CurrentConfig: RegistryHive = ...
    """"""
    DynData: RegistryHive = ...
    """"""

class RegistryKey(MarshalByRefObject, IDisposable):
    """"""

    @property
    def Handle(self) -> SafeRegistryHandle:
        """:return:"""
    @property
    def Name(self) -> str:
        """:return:"""
    @property
    def SubKeyCount(self) -> int:
        """:return:"""
    @property
    def ValueCount(self) -> int:
        """:return:"""
    @property
    def View(self) -> RegistryView:
        """:return:"""
    def Close(self) -> None:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """:param requestedType:
        :return:
        """
    @overload
    def CreateSubKey(self, subkey: str) -> RegistryKey:
        """:param subkey:
        :return:
        """
    @overload
    def CreateSubKey(self, subkey: str, permissionCheck: RegistryKeyPermissionCheck) -> RegistryKey:
        """:param subkey:
        :param permissionCheck:
        :return:
        """
    @overload
    def CreateSubKey(self, subkey: str, writable: bool) -> RegistryKey:
        """:param subkey:
        :param writable:
        :return:
        """
    @overload
    def CreateSubKey(
        self,
        subkey: str,
        permissionCheck: RegistryKeyPermissionCheck,
        options: RegistryOptions,
    ) -> RegistryKey:
        """:param subkey:
        :param permissionCheck:
        :param options:
        :return:
        """
    @overload
    def CreateSubKey(
        self,
        subkey: str,
        permissionCheck: RegistryKeyPermissionCheck,
        registrySecurity: RegistrySecurity,
    ) -> RegistryKey:
        """:param subkey:
        :param permissionCheck:
        :param registrySecurity:
        :return:
        """
    @overload
    def CreateSubKey(self, subkey: str, writable: bool, options: RegistryOptions) -> RegistryKey:
        """:param subkey:
        :param writable:
        :param options:
        :return:
        """
    @overload
    def CreateSubKey(
        self,
        subkey: str,
        permissionCheck: RegistryKeyPermissionCheck,
        registryOptions: RegistryOptions,
        registrySecurity: RegistrySecurity,
    ) -> RegistryKey:
        """:param subkey:
        :param permissionCheck:
        :param registryOptions:
        :param registrySecurity:
        :return:
        """
    @overload
    def DeleteSubKey(self, subkey: str) -> None:
        """:param subkey:"""
    @overload
    def DeleteSubKey(self, subkey: str, throwOnMissingSubKey: bool) -> None:
        """:param subkey:
        :param throwOnMissingSubKey:
        """
    @overload
    def DeleteSubKeyTree(self, subkey: str) -> None:
        """:param subkey:"""
    @overload
    def DeleteSubKeyTree(self, subkey: str, throwOnMissingSubKey: bool) -> None:
        """:param subkey:
        :param throwOnMissingSubKey:
        """
    @overload
    def DeleteValue(self, name: str) -> None:
        """:param name:"""
    @overload
    def DeleteValue(self, name: str, throwOnMissingValue: bool) -> None:
        """:param name:
        :param throwOnMissingValue:
        """
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def Flush(self) -> None:
        """"""
    @classmethod
    @overload
    def FromHandle(cls, handle: SafeRegistryHandle) -> RegistryKey:
        """:param handle:
        :return:
        """
    @classmethod
    @overload
    def FromHandle(cls, handle: SafeRegistryHandle, view: RegistryView) -> RegistryKey:
        """:param handle:
        :param view:
        :return:
        """
    @overload
    def GetAccessControl(self) -> RegistrySecurity:
        """:return:"""
    @overload
    def GetAccessControl(self, includeSections: AccessControlSections) -> RegistrySecurity:
        """:param includeSections:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetLifetimeService(self) -> object:
        """:return:"""
    def GetSubKeyNames(self) -> Array[str]:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def GetValue(self, name: str) -> object:
        """:param name:
        :return:
        """
    @overload
    def GetValue(self, name: str, defaultValue: object) -> object:
        """:param name:
        :param defaultValue:
        :return:
        """
    @overload
    def GetValue(self, name: str, defaultValue: object, options: RegistryValueOptions) -> object:
        """:param name:
        :param defaultValue:
        :param options:
        :return:
        """
    def GetValueKind(self, name: str) -> RegistryValueKind:
        """:param name:
        :return:
        """
    def GetValueNames(self) -> Array[str]:
        """:return:"""
    def InitializeLifetimeService(self) -> object:
        """:return:"""
    @classmethod
    def OpenBaseKey(cls, hKey: RegistryHive, view: RegistryView) -> RegistryKey:
        """:param hKey:
        :param view:
        :return:
        """
    @classmethod
    @overload
    def OpenRemoteBaseKey(cls, hKey: RegistryHive, machineName: str) -> RegistryKey:
        """:param hKey:
        :param machineName:
        :return:
        """
    @classmethod
    @overload
    def OpenRemoteBaseKey(
        cls, hKey: RegistryHive, machineName: str, view: RegistryView
    ) -> RegistryKey:
        """:param hKey:
        :param machineName:
        :param view:
        :return:
        """
    @overload
    def OpenSubKey(self, name: str) -> RegistryKey:
        """:param name:
        :return:
        """
    @overload
    def OpenSubKey(self, name: str, permissionCheck: RegistryKeyPermissionCheck) -> RegistryKey:
        """:param name:
        :param permissionCheck:
        :return:
        """
    @overload
    def OpenSubKey(self, name: str, rights: RegistryRights) -> RegistryKey:
        """:param name:
        :param rights:
        :return:
        """
    @overload
    def OpenSubKey(self, name: str, writable: bool) -> RegistryKey:
        """:param name:
        :param writable:
        :return:
        """
    @overload
    def OpenSubKey(
        self,
        name: str,
        permissionCheck: RegistryKeyPermissionCheck,
        rights: RegistryRights,
    ) -> RegistryKey:
        """:param name:
        :param permissionCheck:
        :param rights:
        :return:
        """
    def SetAccessControl(self, registrySecurity: RegistrySecurity) -> None:
        """:param registrySecurity:"""
    @overload
    def SetValue(self, name: str, value: object) -> None:
        """:param name:
        :param value:
        """
    @overload
    def SetValue(self, name: str, value: object, valueKind: RegistryValueKind) -> None:
        """:param name:
        :param value:
        :param valueKind:
        """
    def ToString(self) -> str:
        """:return:"""

class RegistryKeyPermissionCheck(Enum):
    """"""

    Default: RegistryKeyPermissionCheck = ...
    """"""
    ReadSubTree: RegistryKeyPermissionCheck = ...
    """"""
    ReadWriteSubTree: RegistryKeyPermissionCheck = ...
    """"""

class RegistryOptions(Enum):
    """"""

    _None: RegistryOptions = ...
    """"""
    Volatile: RegistryOptions = ...
    """"""

class RegistryValueKind(Enum):
    """"""

    Unknown: RegistryValueKind = ...
    """"""
    String: RegistryValueKind = ...
    """"""
    ExpandString: RegistryValueKind = ...
    """"""
    Binary: RegistryValueKind = ...
    """"""
    DWord: RegistryValueKind = ...
    """"""
    MultiString: RegistryValueKind = ...
    """"""
    QWord: RegistryValueKind = ...
    """"""
    _None: RegistryValueKind = ...
    """"""

class RegistryValueOptions(Enum):
    """"""

    _None: RegistryValueOptions = ...
    """"""
    DoNotExpandEnvironmentNames: RegistryValueOptions = ...
    """"""

class RegistryView(Enum):
    """"""

    Default: RegistryView = ...
    """"""
    Registry64: RegistryView = ...
    """"""
    Registry32: RegistryView = ...
    """"""

class SafeLibraryHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
    """"""

    @property
    def IsClosed(self) -> bool:
        """:return:"""
    @property
    def IsInvalid(self) -> bool:
        """:return:"""
    def Close(self) -> None:
        """"""
    def DangerousAddRef(self, success: bool) -> None:
        """:param success:"""
    def DangerousGetHandle(self) -> IntPtr:
        """:return:"""
    def DangerousRelease(self) -> None:
        """"""
    def SetHandleAsInvalid(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class SafeNativeMethods(ABC, Object):
    """"""

    ERROR_INSUFFICIENT_BUFFER: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FORMAT_MESSAGE_ALLOCATE_BUFFER: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FORMAT_MESSAGE_ARGUMENT_ARRAY: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FORMAT_MESSAGE_FROM_HMODULE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FORMAT_MESSAGE_FROM_STRING: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FORMAT_MESSAGE_FROM_SYSTEM: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FORMAT_MESSAGE_IGNORE_INSERTS: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FORMAT_MESSAGE_MAX_WIDTH_MASK: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    MB_RIGHT: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    MB_RTLREADING: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    @classmethod
    def CloseHandle(cls, handle: IntPtr) -> bool:
        """:param handle:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @classmethod
    def FormatFromRawValue(
        cls,
        dwCounterType: int,
        dwFormat: int,
        pTimeBase: int,
        pRawValue1: NativeMethods.PDH_RAW_COUNTER,
        pRawValue2: NativeMethods.PDH_RAW_COUNTER,
        pFmtValue: NativeMethods.PDH_FMT_COUNTERVALUE,
    ) -> int:
        """:param dwCounterType:
        :param dwFormat:
        :param pTimeBase:
        :param pRawValue1:
        :param pRawValue2:
        :param pFmtValue:
        :return:
        """
    @classmethod
    @overload
    def FormatMessage(
        cls,
        dwFlags: int,
        lpSource: SafeLibraryHandle,
        dwMessageId: int,
        dwLanguageId: int,
        lpBuffer: StringBuilder,
        nSize: int,
        arguments: Array[IntPtr],
    ) -> int:
        """:param dwFlags:
        :param lpSource:
        :param dwMessageId:
        :param dwLanguageId:
        :param lpBuffer:
        :param nSize:
        :param arguments:
        :return:
        """
    @classmethod
    @overload
    def FormatMessage(
        cls,
        dwFlags: int,
        lpSource_mustBeNull: IntPtr,
        dwMessageId: int,
        dwLanguageId: int,
        lpBuffer: StringBuilder,
        nSize: int,
        arguments: Array[IntPtr],
    ) -> int:
        """:param dwFlags:
        :param lpSource_mustBeNull:
        :param dwMessageId:
        :param dwLanguageId:
        :param lpBuffer:
        :param nSize:
        :param arguments:
        :return:
        """
    @classmethod
    def FreeLibrary(cls, hModule: HandleRef) -> bool:
        """:param hModule:
        :return:
        """
    @classmethod
    def GetComputerName(cls, lpBuffer: StringBuilder, nSize: Array[int]) -> bool:
        """:param lpBuffer:
        :param nSize:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    @classmethod
    def GetStockObject(cls, nIndex: int) -> IntPtr:
        """:param nIndex:
        :return:
        """
    @classmethod
    def GetTextMetrics(
        cls, hDC: IntPtr, tm: NativeMethods.TEXTMETRIC
    ) -> tuple[bool, NativeMethods.TEXTMETRIC]:
        """:param hDC:
        :param tm:
        :return:
        """
    def GetType(self) -> Type:
        """:return:"""
    @classmethod
    def InterlockedCompareExchange(cls, pDestination: IntPtr, exchange: int, compare: int) -> int:
        """:param pDestination:
        :param exchange:
        :param compare:
        :return:
        """
    @classmethod
    def IsWow64Process(cls, hProcess: SafeProcessHandle, Wow64Process: bool) -> bool:
        """:param hProcess:
        :param Wow64Process:
        :return:
        """
    @classmethod
    def LoadLibrary(cls, libFilename: str) -> IntPtr:
        """:param libFilename:
        :return:
        """
    @classmethod
    def MessageBox(cls, hWnd: IntPtr, text: str, caption: str, type: int) -> int:
        """:param hWnd:
        :param text:
        :param caption:
        :param type:
        :return:
        """
    @classmethod
    def OutputDebugString(cls, message: str) -> None:
        """:param message:"""
    @classmethod
    def QueryPerformanceCounter(cls, value: int) -> tuple[bool, int]:
        """:param value:
        :return:
        """
    @classmethod
    def QueryPerformanceFrequency(cls, value: int) -> tuple[bool, int]:
        """:param value:
        :return:
        """
    @classmethod
    def RegisterWindowMessage(cls, msg: str) -> int:
        """:param msg:
        :return:
        """
    def ToString(self) -> str:
        """:return:"""

class SessionEndReasons(Enum):
    """"""

    Logoff: SessionEndReasons = ...
    """"""
    SystemShutdown: SessionEndReasons = ...
    """"""

class SessionEndedEventArgs(EventArgs):
    """"""

    def __init__(self, reason: SessionEndReasons):
        """:param reason:"""
    @property
    def Reason(self) -> SessionEndReasons:
        """:return:"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

SessionEndedEventHandler: Callable[[object, SessionEndedEventArgs], None] = ...
"""

:param sender: 
:param e: 
"""

class SessionEndingEventArgs(EventArgs):
    """"""

    def __init__(self, reason: SessionEndReasons):
        """:param reason:"""
    @property
    def Cancel(self) -> bool:
        """:return:"""
    @Cancel.setter
    def Cancel(self, value: bool) -> None: ...
    @property
    def Reason(self) -> SessionEndReasons:
        """:return:"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

SessionEndingEventHandler: Callable[[object, SessionEndingEventArgs], None] = ...
"""

:param sender: 
:param e: 
"""

class SessionSwitchEventArgs(EventArgs):
    """"""

    def __init__(self, reason: SessionSwitchReason):
        """:param reason:"""
    @property
    def Reason(self) -> SessionSwitchReason:
        """:return:"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

SessionSwitchEventHandler: Callable[[object, SessionSwitchEventArgs], None] = ...
"""

:param sender: 
:param e: 
"""

class SessionSwitchReason(Enum):
    """"""

    ConsoleConnect: SessionSwitchReason = ...
    """"""
    ConsoleDisconnect: SessionSwitchReason = ...
    """"""
    RemoteConnect: SessionSwitchReason = ...
    """"""
    RemoteDisconnect: SessionSwitchReason = ...
    """"""
    SessionLogon: SessionSwitchReason = ...
    """"""
    SessionLogoff: SessionSwitchReason = ...
    """"""
    SessionLock: SessionSwitchReason = ...
    """"""
    SessionUnlock: SessionSwitchReason = ...
    """"""
    SessionRemoteControl: SessionSwitchReason = ...
    """"""

class SystemEvents(Object):
    """"""

    @classmethod
    def CreateTimer(cls, interval: int) -> IntPtr:
        """:param interval:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    @classmethod
    def InvokeOnEventsThread(cls, method: Delegate) -> None:
        """:param method:"""
    @classmethod
    def KillTimer(cls, timerId: IntPtr) -> None:
        """:param timerId:"""
    def ToString(self) -> str:
        """:return:"""
    DisplaySettingsChanged: EventType[EventHandler] = ...
    """"""
    DisplaySettingsChanging: EventType[EventHandler] = ...
    """"""
    EventsThreadShutdown: EventType[EventHandler] = ...
    """"""
    InstalledFontsChanged: EventType[EventHandler] = ...
    """"""
    LowMemory: EventType[EventHandler] = ...
    """"""
    PaletteChanged: EventType[EventHandler] = ...
    """"""
    PowerModeChanged: EventType[PowerModeChangedEventHandler] = ...
    """"""
    SessionEnded: EventType[SessionEndedEventHandler] = ...
    """"""
    SessionEnding: EventType[SessionEndingEventHandler] = ...
    """"""
    SessionSwitch: EventType[SessionSwitchEventHandler] = ...
    """"""
    TimeChanged: EventType[EventHandler] = ...
    """"""
    TimerElapsed: EventType[TimerElapsedEventHandler] = ...
    """"""
    UserPreferenceChanged: EventType[UserPreferenceChangedEventHandler] = ...
    """"""
    UserPreferenceChanging: EventType[UserPreferenceChangingEventHandler] = ...
    """"""

class TimerElapsedEventArgs(EventArgs):
    """"""

    def __init__(self, timerId: IntPtr):
        """:param timerId:"""
    @property
    def TimerId(self) -> IntPtr:
        """:return:"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

TimerElapsedEventHandler: Callable[[object, TimerElapsedEventArgs], None] = ...
"""

:param sender: 
:param e: 
"""

class UnsafeNativeMethods(ABC, Object):
    """"""

    FILE_ACTION_ADDED: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FILE_ACTION_MODIFIED: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FILE_ACTION_REMOVED: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FILE_ACTION_RENAMED_NEW_NAME: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FILE_ACTION_RENAMED_OLD_NAME: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FILE_ADD_FILE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FILE_ADD_SUBDIRECTORY: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FILE_APPEND_DATA: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FILE_ATTRIBUTE_ARCHIVE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FILE_ATTRIBUTE_COMPRESSED: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FILE_ATTRIBUTE_DIRECTORY: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FILE_ATTRIBUTE_HIDDEN: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FILE_ATTRIBUTE_NORMAL: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FILE_ATTRIBUTE_OFFLINE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FILE_ATTRIBUTE_READONLY: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FILE_ATTRIBUTE_SYSTEM: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FILE_ATTRIBUTE_TEMPORARY: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FILE_CASE_PRESERVED_NAMES: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FILE_CASE_SENSITIVE_SEARCH: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FILE_CREATE_PIPE_INSTANCE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FILE_DELETE_CHILD: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FILE_EXECUTE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FILE_FILE_COMPRESSION: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FILE_FLAG_BACKUP_SEMANTICS: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FILE_FLAG_DELETE_ON_CLOSE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FILE_FLAG_NO_BUFFERING: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FILE_FLAG_OVERLAPPED: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FILE_FLAG_POSIX_SEMANTICS: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FILE_FLAG_RANDOM_ACCESS: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FILE_FLAG_SEQUENTIAL_SCAN: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FILE_FLAG_WRITE_THROUGH: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FILE_LIST_DIRECTORY: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FILE_NOTIFY_CHANGE_ATTRIBUTES: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FILE_NOTIFY_CHANGE_CREATION: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FILE_NOTIFY_CHANGE_DIR_NAME: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FILE_NOTIFY_CHANGE_FILE_NAME: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FILE_NOTIFY_CHANGE_LAST_ACCESS: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FILE_NOTIFY_CHANGE_LAST_WRITE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FILE_NOTIFY_CHANGE_SECURITY: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FILE_NOTIFY_CHANGE_SIZE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FILE_PERSISTENT_ACLS: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FILE_READ_ATTRIBUTES: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FILE_READ_DATA: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FILE_READ_EA: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FILE_SHARE_DELETE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FILE_SHARE_READ: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FILE_SHARE_WRITE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FILE_TRAVERSE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FILE_TYPE_CHAR: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FILE_TYPE_DISK: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FILE_TYPE_PIPE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FILE_TYPE_REMOTE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FILE_TYPE_UNKNOWN: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FILE_UNICODE_ON_DISK: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FILE_VOLUME_IS_COMPRESSED: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FILE_WRITE_ATTRIBUTES: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FILE_WRITE_DATA: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FILE_WRITE_EA: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    GetFileExInfoStandard: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    OPEN_ALWAYS: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    OPEN_EXISTING: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    @classmethod
    def ClearEventLog(cls, hEventLog: SafeHandle, lpctstrBackupFileName: HandleRef) -> bool:
        """:param hEventLog:
        :param lpctstrBackupFileName:
        :return:
        """
    @classmethod
    def CreateWindowEx(
        cls,
        exStyle: int,
        lpszClassName: str,
        lpszWindowName: str,
        style: int,
        x: int,
        y: int,
        width: int,
        height: int,
        hWndParent: HandleRef,
        hMenu: HandleRef,
        hInst: HandleRef,
        pvParam: object,
    ) -> IntPtr:
        """:param exStyle:
        :param lpszClassName:
        :param lpszWindowName:
        :param style:
        :param x:
        :param y:
        :param width:
        :param height:
        :param hWndParent:
        :param hMenu:
        :param hInst:
        :param pvParam:
        :return:
        """
    @classmethod
    def DefWindowProc(cls, hWnd: IntPtr, msg: int, wParam: IntPtr, lParam: IntPtr) -> IntPtr:
        """:param hWnd:
        :param msg:
        :param wParam:
        :param lParam:
        :return:
        """
    @classmethod
    def DestroyWindow(cls, hWnd: HandleRef) -> bool:
        """:param hWnd:
        :return:
        """
    @classmethod
    def DispatchMessage(cls, msg: MSG) -> int:
        """:param msg:
        :return:
        """
    @classmethod
    def GetClassInfo(
        cls, hInst: HandleRef, lpszClass: str, wc: NativeMethods.WNDCLASS_I
    ) -> tuple[bool, NativeMethods.WNDCLASS_I]:
        """:param hInst:
        :param lpszClass:
        :param wc:
        :return:
        """
    @classmethod
    def GetDC(cls, hWnd: IntPtr) -> IntPtr:
        """:param hWnd:
        :return:
        """
    @classmethod
    def GetFileVersionInfo(
        cls, lptstrFilename: str, dwHandle: int, dwLen: int, lpData: HandleRef
    ) -> bool:
        """:param lptstrFilename:
        :param dwHandle:
        :param dwLen:
        :param lpData:
        :return:
        """
    @classmethod
    def GetFileVersionInfoSize(cls, lptstrFilename: str, handle: int) -> tuple[int, int]:
        """:param lptstrFilename:
        :param handle:
        :return:
        """
    @classmethod
    def GetModuleFileName(cls, hModule: HandleRef, buffer: StringBuilder, length: int) -> int:
        """:param hModule:
        :param buffer:
        :param length:
        :return:
        """
    @classmethod
    def GetModuleHandle(cls, modName: str) -> IntPtr:
        """:param modName:
        :return:
        """
    @classmethod
    def GetNumberOfEventLogRecords(cls, hEventLog: SafeHandle, count: int) -> tuple[bool, int]:
        """:param hEventLog:
        :param count:
        :return:
        """
    @classmethod
    def GetOldestEventLogRecord(cls, hEventLog: SafeHandle, number: int) -> tuple[bool, int]:
        """:param hEventLog:
        :param number:
        :return:
        """
    @classmethod
    @overload
    def GetProcAddress(cls, hModule: HandleRef, lpProcName: str) -> IntPtr:
        """:param hModule:
        :param lpProcName:
        :return:
        """
    @classmethod
    @overload
    def GetProcAddress(cls, hModule: IntPtr, methodName: str) -> IntPtr:
        """:param hModule:
        :param methodName:
        :return:
        """
    @classmethod
    def GetProcessWindowStation(cls) -> IntPtr:
        """:return:"""
    @classmethod
    def GetStdHandle(cls, type: int) -> IntPtr:
        """:param type:
        :return:
        """
    @classmethod
    def GetSystemMetrics(cls, nIndex: int) -> int:
        """:param nIndex:
        :return:
        """
    @classmethod
    def GetUserObjectInformation(
        cls,
        hObj: HandleRef,
        nIndex: int,
        pvBuffer: NativeMethods.USEROBJECTFLAGS,
        nLength: int,
        lpnLengthNeeded: int,
    ) -> bool:
        """:param hObj:
        :param nIndex:
        :param pvBuffer:
        :param nLength:
        :param lpnLengthNeeded:
        :return:
        """
    @classmethod
    def IsWindow(cls, hWnd: HandleRef) -> bool:
        """:param hWnd:
        :return:
        """
    @classmethod
    def KillTimer(cls, hwnd: HandleRef, idEvent: HandleRef) -> bool:
        """:param hwnd:
        :param idEvent:
        :return:
        """
    @classmethod
    def LookupAccountSid(
        cls,
        systemName: str,
        pSid: Array[int],
        szUserName: StringBuilder,
        userNameSize: int,
        szDomainName: StringBuilder,
        domainNameSize: int,
        eUse: int,
    ) -> int:
        """:param systemName:
        :param pSid:
        :param szUserName:
        :param userNameSize:
        :param szDomainName:
        :param domainNameSize:
        :param eUse:
        :return:
        """
    @classmethod
    def MsgWaitForMultipleObjectsEx(
        cls,
        nCount: int,
        pHandles: IntPtr,
        dwMilliseconds: int,
        dwWakeMask: int,
        dwFlags: int,
    ) -> int:
        """:param nCount:
        :param pHandles:
        :param dwMilliseconds:
        :param dwWakeMask:
        :param dwFlags:
        :return:
        """
    @classmethod
    def NotifyChangeEventLog(cls, hEventLog: SafeHandle, hEvent: SafeWaitHandle) -> bool:
        """:param hEventLog:
        :param hEvent:
        :return:
        """
    @classmethod
    def PeekMessage(
        cls, msg: MSG, hwnd: HandleRef, msgMin: int, msgMax: int, remove: int
    ) -> tuple[bool, MSG]:
        """:param msg:
        :param hwnd:
        :param msgMin:
        :param msgMax:
        :param remove:
        :return:
        """
    @classmethod
    def PostMessage(cls, hwnd: HandleRef, msg: int, wparam: IntPtr, lparam: IntPtr) -> bool:
        """:param hwnd:
        :param msg:
        :param wparam:
        :param lparam:
        :return:
        """
    @classmethod
    def ReadDirectoryChangesW(
        cls,
        hDirectory: SafeFileHandle,
        lpBuffer: HandleRef,
        nBufferLength: int,
        bWatchSubtree: int,
        dwNotifyFilter: int,
        lpBytesReturned: int,
        overlappedPointer: NativeOverlapped,
        lpCompletionRoutine: HandleRef,
    ) -> tuple[bool, int]:
        """:param hDirectory:
        :param lpBuffer:
        :param nBufferLength:
        :param bWatchSubtree:
        :param dwNotifyFilter:
        :param lpBytesReturned:
        :param overlappedPointer:
        :param lpCompletionRoutine:
        :return:
        """
    @classmethod
    def ReadEventLog(
        cls,
        hEventLog: SafeHandle,
        dwReadFlags: int,
        dwRecordOffset: int,
        buffer: Array[int],
        numberOfBytesToRead: int,
        bytesRead: int,
        minNumOfBytesNeeded: int,
    ) -> tuple[bool, int, int]:
        """:param hEventLog:
        :param dwReadFlags:
        :param dwRecordOffset:
        :param buffer:
        :param numberOfBytesToRead:
        :param bytesRead:
        :param minNumOfBytesNeeded:
        :return:
        """
    @classmethod
    def RegisterClass(cls, wc: NativeMethods.WNDCLASS) -> int:
        """:param wc:
        :return:
        """
    @classmethod
    def ReleaseDC(cls, hWnd: IntPtr, hDC: IntPtr) -> int:
        """:param hWnd:
        :param hDC:
        :return:
        """
    @classmethod
    def ReportEvent(
        cls,
        hEventLog: SafeHandle,
        type: int,
        category: int,
        eventID: int,
        userSID: Array[int],
        numStrings: int,
        dataLen: int,
        strings: HandleRef,
        rawData: Array[int],
    ) -> bool:
        """:param hEventLog:
        :param type:
        :param category:
        :param eventID:
        :param userSID:
        :param numStrings:
        :param dataLen:
        :param strings:
        :param rawData:
        :return:
        """
    @classmethod
    def SelectObject(cls, hDC: IntPtr, hObject: IntPtr) -> IntPtr:
        """:param hDC:
        :param hObject:
        :return:
        """
    @classmethod
    def SendMessage(cls, hWnd: HandleRef, msg: int, wParam: IntPtr, lParam: IntPtr) -> IntPtr:
        """:param hWnd:
        :param msg:
        :param wParam:
        :param lParam:
        :return:
        """
    @classmethod
    def SetClassLong(cls, hWnd: HandleRef, nIndex: int, dwNewLong: IntPtr) -> IntPtr:
        """:param hWnd:
        :param nIndex:
        :param dwNewLong:
        :return:
        """
    @classmethod
    def SetClassLongPtr32(cls, hwnd: HandleRef, nIndex: int, dwNewLong: IntPtr) -> IntPtr:
        """:param hwnd:
        :param nIndex:
        :param dwNewLong:
        :return:
        """
    @classmethod
    def SetClassLongPtr64(cls, hwnd: HandleRef, nIndex: int, dwNewLong: IntPtr) -> IntPtr:
        """:param hwnd:
        :param nIndex:
        :param dwNewLong:
        :return:
        """
    @classmethod
    def SetConsoleCtrlHandler(cls, handler: NativeMethods.ConHndlr, add: int) -> bool:
        """:param handler:
        :param add:
        :return:
        """
    @classmethod
    def SetTimer(
        cls, hWnd: HandleRef, nIDEvent: HandleRef, uElapse: int, lpTimerProc: HandleRef
    ) -> IntPtr:
        """:param hWnd:
        :param nIDEvent:
        :param uElapse:
        :param lpTimerProc:
        :return:
        """
    @classmethod
    def SetWindowLong(cls, hWnd: HandleRef, nIndex: int, dwNewLong: HandleRef) -> IntPtr:
        """:param hWnd:
        :param nIndex:
        :param dwNewLong:
        :return:
        """
    @classmethod
    def SetWindowLongPtr32(cls, hWnd: HandleRef, nIndex: int, dwNewLong: HandleRef) -> IntPtr:
        """:param hWnd:
        :param nIndex:
        :param dwNewLong:
        :return:
        """
    @classmethod
    def SetWindowLongPtr64(cls, hWnd: HandleRef, nIndex: int, dwNewLong: HandleRef) -> IntPtr:
        """:param hWnd:
        :param nIndex:
        :param dwNewLong:
        :return:
        """
    @classmethod
    def TranslateMessage(cls, msg: MSG) -> tuple[bool, MSG]:
        """:param msg:
        :return:
        """
    @classmethod
    def UnregisterClass(cls, lpClassName: str, hInstance: HandleRef) -> int:
        """:param lpClassName:
        :param hInstance:
        :return:
        """
    @classmethod
    def VerLanguageName(cls, langID: int, lpBuffer: StringBuilder, nSize: int) -> int:
        """:param langID:
        :param lpBuffer:
        :param nSize:
        :return:
        """
    @classmethod
    def VerQueryValue(
        cls, pBlock: HandleRef, lpSubBlock: str, lplpBuffer: IntPtr, len: int
    ) -> tuple[bool, IntPtr, int]:
        """:param pBlock:
        :param lpSubBlock:
        :param lplpBuffer:
        :param len:
        :return:
        """
    @classmethod
    def WTSRegisterSessionNotification(cls, hWnd: HandleRef, dwFlags: int) -> bool:
        """:param hWnd:
        :param dwFlags:
        :return:
        """
    @classmethod
    def WTSUnRegisterSessionNotification(cls, hWnd: HandleRef) -> bool:
        """:param hWnd:
        :return:
        """
    @classmethod
    def WaitNamedPipe(cls, name: str, timeout: int) -> bool:
        """:param name:
        :param timeout:
        :return:
        """
    @classmethod
    def WldpIsDynamicCodePolicyEnabled(cls, enabled: int) -> tuple[int, int]:
        """:param enabled:
        :return:
        """
    @classmethod
    def WldpQueryDynamicCodeTrust(
        cls, fileHandle: SafeFileHandle, image: IntPtr, imageSize: int
    ) -> int:
        """:param fileHandle:
        :param image:
        :param imageSize:
        :return:
        """
    @classmethod
    def WldpSetDynamicCodeTrust(cls, fileHandle: SafeFileHandle) -> int:
        """:param fileHandle:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

    class WIN32_FILE_ATTRIBUTE_DATA(ValueType):
        """"""

        def Equals(self, obj: object) -> bool:
            """:param obj:
            :return:
            """
        def GetHashCode(self) -> int:
            """:return:"""
        def GetType(self) -> Type:
            """:return:"""
        def ToString(self) -> str:
            """:return:"""

class UserPreferenceCategory(Enum):
    """"""

    Accessibility: UserPreferenceCategory = ...
    """"""
    Color: UserPreferenceCategory = ...
    """"""
    Desktop: UserPreferenceCategory = ...
    """"""
    General: UserPreferenceCategory = ...
    """"""
    Icon: UserPreferenceCategory = ...
    """"""
    Keyboard: UserPreferenceCategory = ...
    """"""
    Menu: UserPreferenceCategory = ...
    """"""
    Mouse: UserPreferenceCategory = ...
    """"""
    Policy: UserPreferenceCategory = ...
    """"""
    Power: UserPreferenceCategory = ...
    """"""
    Screensaver: UserPreferenceCategory = ...
    """"""
    Window: UserPreferenceCategory = ...
    """"""
    Locale: UserPreferenceCategory = ...
    """"""
    VisualStyle: UserPreferenceCategory = ...
    """"""

class UserPreferenceChangedEventArgs(EventArgs):
    """"""

    def __init__(self, category: UserPreferenceCategory):
        """:param category:"""
    @property
    def Category(self) -> UserPreferenceCategory:
        """:return:"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

UserPreferenceChangedEventHandler: Callable[[object, UserPreferenceChangedEventArgs], None] = ...
"""

:param sender: 
:param e: 
"""

class UserPreferenceChangingEventArgs(EventArgs):
    """"""

    def __init__(self, category: UserPreferenceCategory):
        """:param category:"""
    @property
    def Category(self) -> UserPreferenceCategory:
        """:return:"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

UserPreferenceChangingEventHandler: Callable[[object, UserPreferenceChangingEventArgs], None] = ...
"""

:param sender: 
:param e: 
"""

class Win32Native(ABC, Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class WinInetCache(RequestCache):
    """"""

    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""
