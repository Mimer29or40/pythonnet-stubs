"""Automatically generated stubs for C# namespace: Microsoft.Win32."""

from abc import ABC
from collections.abc import Callable
from typing import ClassVar
from typing import Final
from typing import Self
from typing import overload

from Microsoft.Win32.SafeHandles import SafeFileHandle
from Microsoft.Win32.SafeHandles import SafeHandleZeroOrMinusOneIsInvalid
from Microsoft.Win32.SafeHandles import SafeLibraryHandle
from Microsoft.Win32.SafeHandles import SafeProcessHandle
from Microsoft.Win32.SafeHandles import SafeRegistryHandle
from Microsoft.Win32.SafeHandles import SafeThreadHandle
from Microsoft.Win32.SafeHandles import SafeWaitHandle
from System import Array
from System import Boolean
from System import Delegate
from System import Enum
from System import EventArgs
from System import EventHandler
from System import IDisposable
from System import Int32
from System import Int64
from System import IntPtr
from System import MarshalByRefObject
from System import Object
from System import Type
from System import UInt32
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

class EventType[T]:
    def __iadd__(self, other: T) -> Self: ...
    def __isub__(self, other: T) -> Self: ...

class ASM_CACHE(ABC, Object):
    """"""

    DOWNLOAD: ClassVar[int]
    """"""
    GAC: ClassVar[int]
    """"""
    ZAP: ClassVar[int]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ASM_NAME(ABC, Object):
    """"""

    ALIAS: ClassVar[int]
    """"""
    BUILD_NUMBER: ClassVar[int]
    """"""
    CODEBASE_LASTMOD: ClassVar[int]
    """"""
    CODEBASE_URL: ClassVar[int]
    """"""
    CULTURE: ClassVar[int]
    """"""
    CUSTOM: ClassVar[int]
    """"""
    HASH_ALGID: ClassVar[int]
    """"""
    HASH_VALUE: ClassVar[int]
    """"""
    MAJOR_VERSION: ClassVar[int]
    """"""
    MAX_PARAMS: ClassVar[int]
    """"""
    MINOR_VERSION: ClassVar[int]
    """"""
    MVID: ClassVar[int]
    """"""
    NAME: ClassVar[int]
    """"""
    NULL_CUSTOM: ClassVar[int]
    """"""
    NULL_PUBLIC_KEY: ClassVar[int]
    """"""
    NULL_PUBLIC_KEY_TOKEN: ClassVar[int]
    """"""
    OSINFO_ARRAY: ClassVar[int]
    """"""
    PROCESSOR_ID_ARRAY: ClassVar[int]
    """"""
    PUBLIC_KEY: ClassVar[int]
    """"""
    PUBLIC_KEY_TOKEN: ClassVar[int]
    """"""
    REVISION_NUMBER: ClassVar[int]
    """"""
    _32_BIT_ONLY: ClassVar[int]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class CANOF(ABC, Object):
    """"""

    PARSE_DISPLAY_NAME: ClassVar[int]
    """"""
    SET_DEFAULT_VALUES: ClassVar[int]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class Fusion(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def ReadCache(cls, alAssems: ArrayList, name: str, nFlag: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class IApplicationContext:
    """"""
    def Get(
        self, szName: str, pvValue: Int32, pcbValue: UInt32, dwFlags: int
    ) -> tuple[None, Int32]:
        """"""
    def GetContextNameObject(self, ppName: IAssemblyName) -> tuple[None, IAssemblyName]:
        """"""
    def GetDynamicDirectory(self, wzDynamicDir: Int32, pdwSize: UInt32) -> tuple[None, Int32]:
        """"""
    def Set(self, szName: str, pvValue: int, cbValue: int, dwFlags: int) -> None:
        """"""
    def SetContextNameObject(self, pName: IAssemblyName) -> None:
        """"""

class IAssemblyEnum:
    """"""
    def Clone(self, ppEnum: IAssemblyEnum) -> tuple[int, IAssemblyEnum]:
        """"""
    def GetNextAssembly(
        self, ppAppCtx: IApplicationContext, ppName: IAssemblyName, dwFlags: int
    ) -> tuple[int, IApplicationContext, IAssemblyName]:
        """"""
    def Reset(self) -> int:
        """"""

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
        ppv: Int32,
    ) -> tuple[int, Int32]:
        """"""
    def Clone(self, pName: IAssemblyName) -> tuple[int, IAssemblyName]:
        """"""
    def Finalize(self) -> int:
        """"""
    def GetDisplayName(
        self, szDisplayName: IntPtr, pccDisplayName: UInt32, dwDisplayFlags: int
    ) -> int:
        """"""
    def GetName(self, lpcwBuffer: UInt32, pwzName: Int32) -> tuple[int, UInt32, Int32]:
        """"""
    def GetProperty(self, PropertyId: int, pvProperty: IntPtr, pcbProperty: UInt32) -> int:
        """"""
    def GetVersion(self, pdwVersionHi: UInt32, pdwVersionLow: UInt32) -> tuple[int, UInt32, UInt32]:
        """"""
    def IsEqual(self, pName: IAssemblyName, dwCmpFlags: int) -> int:
        """"""
    def SetProperty(self, PropertyId: int, pvProperty: IntPtr, cbProperty: int) -> int:
        """"""

class IInternetSecurityManager:
    """"""
    def GetSecurityId(
        self, pwszUrl: str, pbSecurityId: int, pcbSecurityId: int, dwReserved: int
    ) -> None:
        """"""
    def GetSecuritySite(self, ppSite: None) -> None:
        """"""
    def GetZoneMappings(self, dwZone: int, ppenumString: None, dwFlags: int) -> None:
        """"""
    def MapUrlToZone(self, pwszUrl: str, pdwZone: Int32, dwFlags: int) -> tuple[None, Int32]:
        """"""
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
        """"""
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
        """"""
    def SetSecuritySite(self, pSite: None) -> None:
        """"""
    def SetZoneMapping(self, dwZone: int, lpszPattern: str, dwFlags: int) -> None:
        """"""

class InternetSecurityManager(__ComObject):
    """"""
    def __init__(self) -> None:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetLifetimeService(self) -> object:
        """"""
    def GetType(self) -> Type:
        """"""
    def InitializeLifetimeService(self) -> object:
        """"""
    def ToString(self) -> str:
        """"""

class IntranetZoneCredentialPolicy(Object, ICredentialPolicy):
    """"""
    def __init__(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ShouldSendCredential(
        self,
        challengeUri: Uri,
        request: WebRequest,
        credential: NetworkCredential,
        authModule: IAuthenticationModule,
    ) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

class NativeMethods(ABC, Object):
    """"""

    BACKWARDS_READ: ClassVar[int]
    """"""
    COLOR_WINDOW: ClassVar[int]
    """"""
    CREATE_ALWAYS: ClassVar[int]
    """"""
    CREATE_NO_WINDOW: ClassVar[int]
    """"""
    CREATE_SUSPENDED: ClassVar[int]
    """"""
    CREATE_UNICODE_ENVIRONMENT: ClassVar[int]
    """"""
    CTRL_BREAK_EVENT: ClassVar[int]
    """"""
    CTRL_CLOSE_EVENT: ClassVar[int]
    """"""
    CTRL_C_EVENT: ClassVar[int]
    """"""
    CTRL_LOGOFF_EVENT: ClassVar[int]
    """"""
    CTRL_SHUTDOWN_EVENT: ClassVar[int]
    """"""
    DEFAULT_GUI_FONT: ClassVar[int]
    """"""
    DUPLICATE_CLOSE_SOURCE: ClassVar[int]
    """"""
    DUPLICATE_SAME_ACCESS: ClassVar[int]
    """"""
    DWORD_SIZE: ClassVar[int]
    """"""
    ENDSESSION_LOGOFF: ClassVar[int]
    """"""
    ERROR_ACCESS_DENIED: ClassVar[int]
    """"""
    ERROR_ALREADY_EXISTS: ClassVar[int]
    """"""
    ERROR_BAD_COMMAND: ClassVar[int]
    """"""
    ERROR_BAD_EXE_FORMAT: ClassVar[int]
    """"""
    ERROR_BROKEN_PIPE: ClassVar[int]
    """"""
    ERROR_BUSY: ClassVar[int]
    """"""
    ERROR_CANCELLED: ClassVar[int]
    """"""
    ERROR_CLASS_ALREADY_EXISTS: ClassVar[int]
    """"""
    ERROR_COUNTER_TIMEOUT: ClassVar[int]
    """"""
    ERROR_DDE_FAIL: ClassVar[int]
    """"""
    ERROR_DLL_NOT_FOUND: ClassVar[int]
    """"""
    ERROR_EVENTLOG_FILE_CHANGED: ClassVar[int]
    """"""
    ERROR_EXE_MACHINE_TYPE_MISMATCH: ClassVar[int]
    """"""
    ERROR_FILENAME_EXCED_RANGE: ClassVar[int]
    """"""
    ERROR_FILE_EXISTS: ClassVar[int]
    """"""
    ERROR_FILE_NOT_FOUND: ClassVar[int]
    """"""
    ERROR_HANDLE_EOF: ClassVar[int]
    """"""
    ERROR_INSUFFICIENT_BUFFER: ClassVar[int]
    """"""
    ERROR_INVALID_HANDLE: ClassVar[int]
    """"""
    ERROR_INVALID_NAME: ClassVar[int]
    """"""
    ERROR_INVALID_PARAMETER: ClassVar[int]
    """"""
    ERROR_IO_INCOMPLETE: ClassVar[int]
    """"""
    ERROR_IO_PENDING: ClassVar[int]
    """"""
    ERROR_LOCK_FAILED: ClassVar[int]
    """"""
    ERROR_MORE_DATA: ClassVar[int]
    """"""
    ERROR_NONE_MAPPED: ClassVar[int]
    """"""
    ERROR_NOT_ENOUGH_MEMORY: ClassVar[int]
    """"""
    ERROR_NOT_READY: ClassVar[int]
    """"""
    ERROR_NO_ASSOCIATION: ClassVar[int]
    """"""
    ERROR_NO_DATA: ClassVar[int]
    """"""
    ERROR_OPERATION_ABORTED: ClassVar[int]
    """"""
    ERROR_PARTIAL_COPY: ClassVar[int]
    """"""
    ERROR_PATH_NOT_FOUND: ClassVar[int]
    """"""
    ERROR_PROC_NOT_FOUND: ClassVar[int]
    """"""
    ERROR_SHARING_VIOLATION: ClassVar[int]
    """"""
    ERROR_SUCCESS: ClassVar[int]
    """"""
    E_ABORT: ClassVar[int]
    """"""
    E_NOTIMPL: ClassVar[int]
    """"""
    FILE_ATTRIBUTE_NORMAL: ClassVar[int]
    """"""
    FILE_FLAG_OVERLAPPED: ClassVar[int]
    """"""
    FILE_MAP_READ: ClassVar[int]
    """"""
    FILE_MAP_WRITE: ClassVar[int]
    """"""
    FILE_SHARE_DELETE: ClassVar[int]
    """"""
    FILE_SHARE_READ: ClassVar[int]
    """"""
    FILE_SHARE_WRITE: ClassVar[int]
    """"""
    FORMAT_MESSAGE_ALLOCATE_BUFFER: ClassVar[int]
    """"""
    FORMAT_MESSAGE_ARGUMENT_ARRAY: ClassVar[int]
    """"""
    FORMAT_MESSAGE_FROM_HMODULE: ClassVar[int]
    """"""
    FORMAT_MESSAGE_FROM_STRING: ClassVar[int]
    """"""
    FORMAT_MESSAGE_FROM_SYSTEM: ClassVar[int]
    """"""
    FORMAT_MESSAGE_IGNORE_INSERTS: ClassVar[int]
    """"""
    FORMAT_MESSAGE_MAX_WIDTH_MASK: ClassVar[int]
    """"""
    FORWARDS_READ: ClassVar[int]
    """"""
    GCL_WNDPROC: ClassVar[int]
    """"""
    GENERIC_ALL: ClassVar[int]
    """"""
    GENERIC_EXECUTE: ClassVar[int]
    """"""
    GENERIC_READ: ClassVar[int]
    """"""
    GENERIC_WRITE: ClassVar[int]
    """"""
    GHND: ClassVar[int]
    """"""
    GMEM_DDESHARE: ClassVar[int]
    """"""
    GMEM_DISCARDABLE: ClassVar[int]
    """"""
    GMEM_DISCARDED: ClassVar[int]
    """"""
    GMEM_FIXED: ClassVar[int]
    """"""
    GMEM_INVALID_HANDLE: ClassVar[int]
    """"""
    GMEM_LOCKCOUNT: ClassVar[int]
    """"""
    GMEM_LOWER: ClassVar[int]
    """"""
    GMEM_MODIFY: ClassVar[int]
    """"""
    GMEM_MOVEABLE: ClassVar[int]
    """"""
    GMEM_NOCOMPACT: ClassVar[int]
    """"""
    GMEM_NODISCARD: ClassVar[int]
    """"""
    GMEM_NOTIFY: ClassVar[int]
    """"""
    GMEM_NOT_BANKED: ClassVar[int]
    """"""
    GMEM_SHARE: ClassVar[int]
    """"""
    GMEM_VALID_FLAGS: ClassVar[int]
    """"""
    GMEM_ZEROINIT: ClassVar[int]
    """"""
    GPTR: ClassVar[int]
    """"""
    GWL_STYLE: ClassVar[int]
    """"""
    GWL_WNDPROC: ClassVar[int]
    """"""
    GW_OWNER: ClassVar[int]
    """"""
    HKEY_LOCAL_MACHINE: ClassVar[IntPtr]
    """"""
    HKEY_PERFORMANCE_DATA: ClassVar[int]
    """"""
    IMPERSONATION_LEVEL_SecurityAnonymous: ClassVar[int]
    """"""
    IMPERSONATION_LEVEL_SecurityDelegation: ClassVar[int]
    """"""
    IMPERSONATION_LEVEL_SecurityIdentification: ClassVar[int]
    """"""
    IMPERSONATION_LEVEL_SecurityImpersonation: ClassVar[int]
    """"""
    INVALID_HANDLE_VALUE: ClassVar[IntPtr]
    """"""
    KEY_ENUMERATE_SUB_KEYS: ClassVar[int]
    """"""
    KEY_NOTIFY: ClassVar[int]
    """"""
    KEY_QUERY_VALUE: ClassVar[int]
    """"""
    KEY_READ: ClassVar[int]
    """"""
    LARGE_INTEGER_SIZE: ClassVar[int]
    """"""
    LOAD_LIBRARY_AS_DATAFILE: ClassVar[int]
    """"""
    LOAD_WITH_ALTERED_SEARCH_PATH: ClassVar[int]
    """"""
    LOGON32_LOGON_BATCH: ClassVar[int]
    """"""
    LOGON32_LOGON_INTERACTIVE: ClassVar[int]
    """"""
    LOGON32_PROVIDER_DEFAULT: ClassVar[int]
    """"""
    MAX_PATH: ClassVar[int]
    """"""
    MOVEFILE_REPLACE_EXISTING: ClassVar[int]
    """"""
    MWMO_INPUTAVAILABLE: ClassVar[int]
    """"""
    NOTIFY_FOR_THIS_SESSION: ClassVar[int]
    """"""
    NtPerfCounterSizeDword: ClassVar[int]
    """"""
    NtPerfCounterSizeLarge: ClassVar[int]
    """"""
    NtQueryProcessBasicInfo: ClassVar[int]
    """"""
    NtQuerySystemProcessInformation: ClassVar[int]
    """"""
    NullHandleRef: ClassVar[HandleRef]
    """"""
    PAGE_READWRITE: ClassVar[int]
    """"""
    PBT_APMBATTERYLOW: ClassVar[int]
    """"""
    PBT_APMOEMEVENT: ClassVar[int]
    """"""
    PBT_APMPOWERSTATUSCHANGE: ClassVar[int]
    """"""
    PBT_APMQUERYSTANDBY: ClassVar[int]
    """"""
    PBT_APMQUERYSTANDBYFAILED: ClassVar[int]
    """"""
    PBT_APMQUERYSUSPEND: ClassVar[int]
    """"""
    PBT_APMQUERYSUSPENDFAILED: ClassVar[int]
    """"""
    PBT_APMRESUMECRITICAL: ClassVar[int]
    """"""
    PBT_APMRESUMESTANDBY: ClassVar[int]
    """"""
    PBT_APMRESUMESUSPEND: ClassVar[int]
    """"""
    PBT_APMSTANDBY: ClassVar[int]
    """"""
    PBT_APMSUSPEND: ClassVar[int]
    """"""
    PDH_CALC_NEGATIVE_DENOMINATOR: ClassVar[int]
    """"""
    PDH_CALC_NEGATIVE_VALUE: ClassVar[int]
    """"""
    PDH_FMT_DOUBLE: ClassVar[int]
    """"""
    PDH_FMT_NOCAP100: ClassVar[int]
    """"""
    PDH_FMT_NOSCALE: ClassVar[int]
    """"""
    PDH_NO_DATA: ClassVar[int]
    """"""
    PERF_100NSEC_MULTI_TIMER: ClassVar[int]
    """"""
    PERF_100NSEC_MULTI_TIMER_INV: ClassVar[int]
    """"""
    PERF_100NSEC_TIMER: ClassVar[int]
    """"""
    PERF_100NSEC_TIMER_INV: ClassVar[int]
    """"""
    PERF_AVERAGE_BASE: ClassVar[int]
    """"""
    PERF_AVERAGE_BULK: ClassVar[int]
    """"""
    PERF_AVERAGE_TIMER: ClassVar[int]
    """"""
    PERF_COUNTER_100NS_QUEUELEN_TYPE: ClassVar[int]
    """"""
    PERF_COUNTER_BASE: ClassVar[int]
    """"""
    PERF_COUNTER_BULK_COUNT: ClassVar[int]
    """"""
    PERF_COUNTER_COUNTER: ClassVar[int]
    """"""
    PERF_COUNTER_DELTA: ClassVar[int]
    """"""
    PERF_COUNTER_ELAPSED: ClassVar[int]
    """"""
    PERF_COUNTER_FRACTION: ClassVar[int]
    """"""
    PERF_COUNTER_HISTOGRAM: ClassVar[int]
    """"""
    PERF_COUNTER_LARGE_DELTA: ClassVar[int]
    """"""
    PERF_COUNTER_LARGE_QUEUELEN_TYPE: ClassVar[int]
    """"""
    PERF_COUNTER_LARGE_RAWCOUNT: ClassVar[int]
    """"""
    PERF_COUNTER_LARGE_RAWCOUNT_HEX: ClassVar[int]
    """"""
    PERF_COUNTER_MULTI_BASE: ClassVar[int]
    """"""
    PERF_COUNTER_MULTI_TIMER: ClassVar[int]
    """"""
    PERF_COUNTER_MULTI_TIMER_INV: ClassVar[int]
    """"""
    PERF_COUNTER_NODATA: ClassVar[int]
    """"""
    PERF_COUNTER_OBJ_TIME_QUEUELEN_TYPE: ClassVar[int]
    """"""
    PERF_COUNTER_PRECISION: ClassVar[int]
    """"""
    PERF_COUNTER_QUEUELEN: ClassVar[int]
    """"""
    PERF_COUNTER_QUEUELEN_TYPE: ClassVar[int]
    """"""
    PERF_COUNTER_RATE: ClassVar[int]
    """"""
    PERF_COUNTER_RAWCOUNT: ClassVar[int]
    """"""
    PERF_COUNTER_RAWCOUNT_HEX: ClassVar[int]
    """"""
    PERF_COUNTER_TEXT: ClassVar[int]
    """"""
    PERF_COUNTER_TIMER: ClassVar[int]
    """"""
    PERF_COUNTER_TIMER_INV: ClassVar[int]
    """"""
    PERF_COUNTER_VALUE: ClassVar[int]
    """"""
    PERF_DELTA_BASE: ClassVar[int]
    """"""
    PERF_DELTA_COUNTER: ClassVar[int]
    """"""
    PERF_DETAIL_ADVANCED: ClassVar[int]
    """"""
    PERF_DETAIL_EXPERT: ClassVar[int]
    """"""
    PERF_DETAIL_NOVICE: ClassVar[int]
    """"""
    PERF_DETAIL_WIZARD: ClassVar[int]
    """"""
    PERF_DISPLAY_NOSHOW: ClassVar[int]
    """"""
    PERF_DISPLAY_NO_SUFFIX: ClassVar[int]
    """"""
    PERF_DISPLAY_PERCENT: ClassVar[int]
    """"""
    PERF_DISPLAY_PER_SEC: ClassVar[int]
    """"""
    PERF_DISPLAY_SECONDS: ClassVar[int]
    """"""
    PERF_ELAPSED_TIME: ClassVar[int]
    """"""
    PERF_INVERSE_COUNTER: ClassVar[int]
    """"""
    PERF_LARGE_RAW_BASE: ClassVar[int]
    """"""
    PERF_LARGE_RAW_FRACTION: ClassVar[int]
    """"""
    PERF_MULTI_COUNTER: ClassVar[int]
    """"""
    PERF_NO_INSTANCES: ClassVar[int]
    """"""
    PERF_NO_UNIQUE_ID: ClassVar[int]
    """"""
    PERF_NUMBER_DECIMAL: ClassVar[int]
    """"""
    PERF_NUMBER_DEC_1000: ClassVar[int]
    """"""
    PERF_NUMBER_HEX: ClassVar[int]
    """"""
    PERF_OBJECT_TIMER: ClassVar[int]
    """"""
    PERF_OBJ_TIME_TIME: ClassVar[int]
    """"""
    PERF_OBJ_TIME_TIMER: ClassVar[int]
    """"""
    PERF_PRECISION_100NS_TIMER: ClassVar[int]
    """"""
    PERF_PRECISION_OBJECT_TIMER: ClassVar[int]
    """"""
    PERF_PRECISION_SYSTEM_TIMER: ClassVar[int]
    """"""
    PERF_RAW_BASE: ClassVar[int]
    """"""
    PERF_RAW_FRACTION: ClassVar[int]
    """"""
    PERF_SAMPLE_BASE: ClassVar[int]
    """"""
    PERF_SAMPLE_COUNTER: ClassVar[int]
    """"""
    PERF_SAMPLE_FRACTION: ClassVar[int]
    """"""
    PERF_SIZE_DWORD: ClassVar[int]
    """"""
    PERF_SIZE_LARGE: ClassVar[int]
    """"""
    PERF_SIZE_VARIABLE_LEN: ClassVar[int]
    """"""
    PERF_SIZE_ZERO: ClassVar[int]
    """"""
    PERF_TEXT_ASCII: ClassVar[int]
    """"""
    PERF_TEXT_UNICODE: ClassVar[int]
    """"""
    PERF_TIMER_100NS: ClassVar[int]
    """"""
    PERF_TIMER_TICK: ClassVar[int]
    """"""
    PERF_TYPE_COUNTER: ClassVar[int]
    """"""
    PERF_TYPE_NUMBER: ClassVar[int]
    """"""
    PERF_TYPE_TEXT: ClassVar[int]
    """"""
    PERF_TYPE_ZERO: ClassVar[int]
    """"""
    PIPE_ACCESS_DUPLEX: ClassVar[int]
    """"""
    PIPE_ACCESS_INBOUND: ClassVar[int]
    """"""
    PIPE_ACCESS_OUTBOUND: ClassVar[int]
    """"""
    PIPE_NOWAIT: ClassVar[int]
    """"""
    PIPE_READMODE_BYTE: ClassVar[int]
    """"""
    PIPE_READMODE_MESSAGE: ClassVar[int]
    """"""
    PIPE_SINGLE_INSTANCES: ClassVar[int]
    """"""
    PIPE_TYPE_BYTE: ClassVar[int]
    """"""
    PIPE_TYPE_MESSAGE: ClassVar[int]
    """"""
    PIPE_UNLIMITED_INSTANCES: ClassVar[int]
    """"""
    PIPE_WAIT: ClassVar[int]
    """"""
    PM_REMOVE: ClassVar[int]
    """"""
    PROCESS_ALL_ACCESS: ClassVar[int]
    """"""
    PROCESS_CREATE_PROCESS: ClassVar[int]
    """"""
    PROCESS_CREATE_THREAD: ClassVar[int]
    """"""
    PROCESS_DUP_HANDLE: ClassVar[int]
    """"""
    PROCESS_QUERY_INFORMATION: ClassVar[int]
    """"""
    PROCESS_QUERY_LIMITED_INFORMATION: ClassVar[int]
    """"""
    PROCESS_SET_INFORMATION: ClassVar[int]
    """"""
    PROCESS_SET_QUOTA: ClassVar[int]
    """"""
    PROCESS_SET_SESSIONID: ClassVar[int]
    """"""
    PROCESS_TERMINATE: ClassVar[int]
    """"""
    PROCESS_VM_OPERATION: ClassVar[int]
    """"""
    PROCESS_VM_READ: ClassVar[int]
    """"""
    PROCESS_VM_WRITE: ClassVar[int]
    """"""
    QS_ALLEVENTS: ClassVar[int]
    """"""
    QS_ALLINPUT: ClassVar[int]
    """"""
    QS_ALLPOSTMESSAGE: ClassVar[int]
    """"""
    QS_HOTKEY: ClassVar[int]
    """"""
    QS_INPUT: ClassVar[int]
    """"""
    QS_KEY: ClassVar[int]
    """"""
    QS_MOUSE: ClassVar[int]
    """"""
    QS_MOUSEBUTTON: ClassVar[int]
    """"""
    QS_MOUSEMOVE: ClassVar[int]
    """"""
    QS_PAINT: ClassVar[int]
    """"""
    QS_POSTMESSAGE: ClassVar[int]
    """"""
    QS_SENDMESSAGE: ClassVar[int]
    """"""
    QS_TIMER: ClassVar[int]
    """"""
    READ_CONTROL: ClassVar[int]
    """"""
    REG_BINARY: ClassVar[int]
    """"""
    REG_MULTI_SZ: ClassVar[int]
    """"""
    RPC_S_CALL_FAILED: ClassVar[int]
    """"""
    RPC_S_SERVER_UNAVAILABLE: ClassVar[int]
    """"""
    SECURITY_DESCRIPTOR_REVISION: ClassVar[int]
    """"""
    SEEK_READ: ClassVar[int]
    """"""
    SEE_MASK_ASYNCOK: ClassVar[int]
    """"""
    SEE_MASK_CLASSKEY: ClassVar[int]
    """"""
    SEE_MASK_CLASSNAME: ClassVar[int]
    """"""
    SEE_MASK_CONNECTNETDRV: ClassVar[int]
    """"""
    SEE_MASK_DOENVSUBST: ClassVar[int]
    """"""
    SEE_MASK_FLAG_DDEWAIT: ClassVar[int]
    """"""
    SEE_MASK_FLAG_NO_UI: ClassVar[int]
    """"""
    SEE_MASK_HOTKEY: ClassVar[int]
    """"""
    SEE_MASK_ICON: ClassVar[int]
    """"""
    SEE_MASK_IDLIST: ClassVar[int]
    """"""
    SEE_MASK_INVOKEIDLIST: ClassVar[int]
    """"""
    SEE_MASK_NOCLOSEPROCESS: ClassVar[int]
    """"""
    SEE_MASK_NO_CONSOLE: ClassVar[int]
    """"""
    SEE_MASK_UNICODE: ClassVar[int]
    """"""
    SE_ERR_ACCESSDENIED: ClassVar[int]
    """"""
    SE_ERR_ASSOCINCOMPLETE: ClassVar[int]
    """"""
    SE_ERR_DDEBUSY: ClassVar[int]
    """"""
    SE_ERR_DDEFAIL: ClassVar[int]
    """"""
    SE_ERR_DDETIMEOUT: ClassVar[int]
    """"""
    SE_ERR_DLLNOTFOUND: ClassVar[int]
    """"""
    SE_ERR_FNF: ClassVar[int]
    """"""
    SE_ERR_NOASSOC: ClassVar[int]
    """"""
    SE_ERR_OOM: ClassVar[int]
    """"""
    SE_ERR_PNF: ClassVar[int]
    """"""
    SE_ERR_SHARE: ClassVar[int]
    """"""
    SE_PRIVILEGE_ENABLED: ClassVar[int]
    """"""
    SHGFI_TYPENAME: ClassVar[int]
    """"""
    SHGFI_USEFILEATTRIBUTES: ClassVar[int]
    """"""
    SMTO_ABORTIFHUNG: ClassVar[int]
    """"""
    SM_CYSCREEN: ClassVar[int]
    """"""
    SPI_GETACCESSTIMEOUT: ClassVar[int]
    """"""
    SPI_GETACTIVEWINDOWTRACKING: ClassVar[int]
    """"""
    SPI_GETACTIVEWNDTRKTIMEOUT: ClassVar[int]
    """"""
    SPI_GETACTIVEWNDTRKZORDER: ClassVar[int]
    """"""
    SPI_GETANIMATION: ClassVar[int]
    """"""
    SPI_GETBEEP: ClassVar[int]
    """"""
    SPI_GETBORDER: ClassVar[int]
    """"""
    SPI_GETCARETWIDTH: ClassVar[int]
    """"""
    SPI_GETCOMBOBOXANIMATION: ClassVar[int]
    """"""
    SPI_GETCURSORSHADOW: ClassVar[int]
    """"""
    SPI_GETDEFAULTINPUTLANG: ClassVar[int]
    """"""
    SPI_GETDESKWALLPAPER: ClassVar[int]
    """"""
    SPI_GETDRAGFULLWINDOWS: ClassVar[int]
    """"""
    SPI_GETFASTTASKSWITCH: ClassVar[int]
    """"""
    SPI_GETFILTERKEYS: ClassVar[int]
    """"""
    SPI_GETFONTSMOOTHING: ClassVar[int]
    """"""
    SPI_GETFOREGROUNDFLASHCOUNT: ClassVar[int]
    """"""
    SPI_GETFOREGROUNDLOCKTIMEOUT: ClassVar[int]
    """"""
    SPI_GETGRADIENTCAPTIONS: ClassVar[int]
    """"""
    SPI_GETGRIDGRANULARITY: ClassVar[int]
    """"""
    SPI_GETHIGHCONTRAST: ClassVar[int]
    """"""
    SPI_GETHOTTRACKING: ClassVar[int]
    """"""
    SPI_GETICONMETRICS: ClassVar[int]
    """"""
    SPI_GETICONTITLELOGFONT: ClassVar[int]
    """"""
    SPI_GETICONTITLEWRAP: ClassVar[int]
    """"""
    SPI_GETKEYBOARDCUES: ClassVar[int]
    """"""
    SPI_GETKEYBOARDDELAY: ClassVar[int]
    """"""
    SPI_GETKEYBOARDPREF: ClassVar[int]
    """"""
    SPI_GETKEYBOARDSPEED: ClassVar[int]
    """"""
    SPI_GETLISTBOXSMOOTHSCROLLING: ClassVar[int]
    """"""
    SPI_GETLOWPOWERACTIVE: ClassVar[int]
    """"""
    SPI_GETLOWPOWERTIMEOUT: ClassVar[int]
    """"""
    SPI_GETMENUANIMATION: ClassVar[int]
    """"""
    SPI_GETMENUDROPALIGNMENT: ClassVar[int]
    """"""
    SPI_GETMENUFADE: ClassVar[int]
    """"""
    SPI_GETMENUSHOWDELAY: ClassVar[int]
    """"""
    SPI_GETMENUUNDERLINES: ClassVar[int]
    """"""
    SPI_GETMINIMIZEDMETRICS: ClassVar[int]
    """"""
    SPI_GETMOUSE: ClassVar[int]
    """"""
    SPI_GETMOUSEHOVERHEIGHT: ClassVar[int]
    """"""
    SPI_GETMOUSEHOVERTIME: ClassVar[int]
    """"""
    SPI_GETMOUSEHOVERWIDTH: ClassVar[int]
    """"""
    SPI_GETMOUSEKEYS: ClassVar[int]
    """"""
    SPI_GETMOUSESPEED: ClassVar[int]
    """"""
    SPI_GETMOUSETRAILS: ClassVar[int]
    """"""
    SPI_GETNONCLIENTMETRICS: ClassVar[int]
    """"""
    SPI_GETPOWEROFFACTIVE: ClassVar[int]
    """"""
    SPI_GETPOWEROFFTIMEOUT: ClassVar[int]
    """"""
    SPI_GETSCREENREADER: ClassVar[int]
    """"""
    SPI_GETSCREENSAVEACTIVE: ClassVar[int]
    """"""
    SPI_GETSCREENSAVERRUNNING: ClassVar[int]
    """"""
    SPI_GETSCREENSAVETIMEOUT: ClassVar[int]
    """"""
    SPI_GETSELECTIONFADE: ClassVar[int]
    """"""
    SPI_GETSERIALKEYS: ClassVar[int]
    """"""
    SPI_GETSHOWIMEUI: ClassVar[int]
    """"""
    SPI_GETSHOWSOUNDS: ClassVar[int]
    """"""
    SPI_GETSNAPTODEFBUTTON: ClassVar[int]
    """"""
    SPI_GETSOUNDSENTRY: ClassVar[int]
    """"""
    SPI_GETSTICKYKEYS: ClassVar[int]
    """"""
    SPI_GETTOGGLEKEYS: ClassVar[int]
    """"""
    SPI_GETTOOLTIPANIMATION: ClassVar[int]
    """"""
    SPI_GETTOOLTIPFADE: ClassVar[int]
    """"""
    SPI_GETUIEFFECTS: ClassVar[int]
    """"""
    SPI_GETWHEELSCROLLLINES: ClassVar[int]
    """"""
    SPI_GETWINDOWSEXTENSION: ClassVar[int]
    """"""
    SPI_GETWORKAREA: ClassVar[int]
    """"""
    SPI_ICONHORIZONTALSPACING: ClassVar[int]
    """"""
    SPI_ICONVERTICALSPACING: ClassVar[int]
    """"""
    SPI_LANGDRIVER: ClassVar[int]
    """"""
    SPI_SCREENSAVERRUNNING: ClassVar[int]
    """"""
    SPI_SETACCESSTIMEOUT: ClassVar[int]
    """"""
    SPI_SETACTIVEWINDOWTRACKING: ClassVar[int]
    """"""
    SPI_SETACTIVEWNDTRKTIMEOUT: ClassVar[int]
    """"""
    SPI_SETACTIVEWNDTRKZORDER: ClassVar[int]
    """"""
    SPI_SETANIMATION: ClassVar[int]
    """"""
    SPI_SETBEEP: ClassVar[int]
    """"""
    SPI_SETBORDER: ClassVar[int]
    """"""
    SPI_SETCARETWIDTH: ClassVar[int]
    """"""
    SPI_SETCOMBOBOXANIMATION: ClassVar[int]
    """"""
    SPI_SETCURSORS: ClassVar[int]
    """"""
    SPI_SETCURSORSHADOW: ClassVar[int]
    """"""
    SPI_SETDEFAULTINPUTLANG: ClassVar[int]
    """"""
    SPI_SETDESKPATTERN: ClassVar[int]
    """"""
    SPI_SETDESKWALLPAPER: ClassVar[int]
    """"""
    SPI_SETDOUBLECLICKTIME: ClassVar[int]
    """"""
    SPI_SETDOUBLECLKHEIGHT: ClassVar[int]
    """"""
    SPI_SETDOUBLECLKWIDTH: ClassVar[int]
    """"""
    SPI_SETDRAGFULLWINDOWS: ClassVar[int]
    """"""
    SPI_SETDRAGHEIGHT: ClassVar[int]
    """"""
    SPI_SETDRAGWIDTH: ClassVar[int]
    """"""
    SPI_SETFASTTASKSWITCH: ClassVar[int]
    """"""
    SPI_SETFILTERKEYS: ClassVar[int]
    """"""
    SPI_SETFONTSMOOTHING: ClassVar[int]
    """"""
    SPI_SETFOREGROUNDFLASHCOUNT: ClassVar[int]
    """"""
    SPI_SETFOREGROUNDLOCKTIMEOUT: ClassVar[int]
    """"""
    SPI_SETGRADIENTCAPTIONS: ClassVar[int]
    """"""
    SPI_SETGRIDGRANULARITY: ClassVar[int]
    """"""
    SPI_SETHANDHELD: ClassVar[int]
    """"""
    SPI_SETHIGHCONTRAST: ClassVar[int]
    """"""
    SPI_SETHOTTRACKING: ClassVar[int]
    """"""
    SPI_SETICONMETRICS: ClassVar[int]
    """"""
    SPI_SETICONS: ClassVar[int]
    """"""
    SPI_SETICONTITLELOGFONT: ClassVar[int]
    """"""
    SPI_SETICONTITLEWRAP: ClassVar[int]
    """"""
    SPI_SETKEYBOARDCUES: ClassVar[int]
    """"""
    SPI_SETKEYBOARDDELAY: ClassVar[int]
    """"""
    SPI_SETKEYBOARDPREF: ClassVar[int]
    """"""
    SPI_SETKEYBOARDSPEED: ClassVar[int]
    """"""
    SPI_SETLANGTOGGLE: ClassVar[int]
    """"""
    SPI_SETLISTBOXSMOOTHSCROLLING: ClassVar[int]
    """"""
    SPI_SETLOWPOWERACTIVE: ClassVar[int]
    """"""
    SPI_SETLOWPOWERTIMEOUT: ClassVar[int]
    """"""
    SPI_SETMENUANIMATION: ClassVar[int]
    """"""
    SPI_SETMENUDROPALIGNMENT: ClassVar[int]
    """"""
    SPI_SETMENUFADE: ClassVar[int]
    """"""
    SPI_SETMENUSHOWDELAY: ClassVar[int]
    """"""
    SPI_SETMENUUNDERLINES: ClassVar[int]
    """"""
    SPI_SETMINIMIZEDMETRICS: ClassVar[int]
    """"""
    SPI_SETMOUSE: ClassVar[int]
    """"""
    SPI_SETMOUSEBUTTONSWAP: ClassVar[int]
    """"""
    SPI_SETMOUSEHOVERHEIGHT: ClassVar[int]
    """"""
    SPI_SETMOUSEHOVERTIME: ClassVar[int]
    """"""
    SPI_SETMOUSEHOVERWIDTH: ClassVar[int]
    """"""
    SPI_SETMOUSEKEYS: ClassVar[int]
    """"""
    SPI_SETMOUSESPEED: ClassVar[int]
    """"""
    SPI_SETMOUSETRAILS: ClassVar[int]
    """"""
    SPI_SETNONCLIENTMETRICS: ClassVar[int]
    """"""
    SPI_SETPENWINDOWS: ClassVar[int]
    """"""
    SPI_SETPOWEROFFACTIVE: ClassVar[int]
    """"""
    SPI_SETPOWEROFFTIMEOUT: ClassVar[int]
    """"""
    SPI_SETSCREENREADER: ClassVar[int]
    """"""
    SPI_SETSCREENSAVEACTIVE: ClassVar[int]
    """"""
    SPI_SETSCREENSAVERRUNNING: ClassVar[int]
    """"""
    SPI_SETSCREENSAVETIMEOUT: ClassVar[int]
    """"""
    SPI_SETSELECTIONFADE: ClassVar[int]
    """"""
    SPI_SETSERIALKEYS: ClassVar[int]
    """"""
    SPI_SETSHOWIMEUI: ClassVar[int]
    """"""
    SPI_SETSHOWSOUNDS: ClassVar[int]
    """"""
    SPI_SETSNAPTODEFBUTTON: ClassVar[int]
    """"""
    SPI_SETSOUNDSENTRY: ClassVar[int]
    """"""
    SPI_SETSTICKYKEYS: ClassVar[int]
    """"""
    SPI_SETTOGGLEKEYS: ClassVar[int]
    """"""
    SPI_SETTOOLTIPANIMATION: ClassVar[int]
    """"""
    SPI_SETTOOLTIPFADE: ClassVar[int]
    """"""
    SPI_SETUIEFFECTS: ClassVar[int]
    """"""
    SPI_SETWHEELSCROLLLINES: ClassVar[int]
    """"""
    SPI_SETWORKAREA: ClassVar[int]
    """"""
    STANDARD_RIGHTS_READ: ClassVar[int]
    """"""
    STANDARD_RIGHTS_REQUIRED: ClassVar[int]
    """"""
    STARTF_USESHOWWINDOW: ClassVar[int]
    """"""
    STARTF_USESTDHANDLES: ClassVar[int]
    """"""
    STATUS_INFO_LENGTH_MISMATCH: ClassVar[int]
    """"""
    STD_ERROR_HANDLE: ClassVar[int]
    """"""
    STD_INPUT_HANDLE: ClassVar[int]
    """"""
    STD_OUTPUT_HANDLE: ClassVar[int]
    """"""
    STILL_ACTIVE: ClassVar[int]
    """"""
    SW_HIDE: ClassVar[int]
    """"""
    SW_MAX: ClassVar[int]
    """"""
    SW_MAXIMIZE: ClassVar[int]
    """"""
    SW_MINIMIZE: ClassVar[int]
    """"""
    SW_NORMAL: ClassVar[int]
    """"""
    SW_RESTORE: ClassVar[int]
    """"""
    SW_SHOW: ClassVar[int]
    """"""
    SW_SHOWDEFAULT: ClassVar[int]
    """"""
    SW_SHOWMAXIMIZED: ClassVar[int]
    """"""
    SW_SHOWMINIMIZED: ClassVar[int]
    """"""
    SW_SHOWMINNOACTIVE: ClassVar[int]
    """"""
    SW_SHOWNA: ClassVar[int]
    """"""
    SW_SHOWNOACTIVATE: ClassVar[int]
    """"""
    SW_SHOWNORMAL: ClassVar[int]
    """"""
    SYNCHRONIZE: ClassVar[int]
    """"""
    S_OK: ClassVar[int]
    """"""
    TH32CS_INHERIT: ClassVar[int]
    """"""
    TH32CS_SNAPHEAPLIST: ClassVar[int]
    """"""
    TH32CS_SNAPMODULE: ClassVar[int]
    """"""
    TH32CS_SNAPPROCESS: ClassVar[int]
    """"""
    TH32CS_SNAPTHREAD: ClassVar[int]
    """"""
    THREAD_DIRECT_IMPERSONATION: ClassVar[int]
    """"""
    THREAD_GET_CONTEXT: ClassVar[int]
    """"""
    THREAD_IMPERSONATE: ClassVar[int]
    """"""
    THREAD_QUERY_INFORMATION: ClassVar[int]
    """"""
    THREAD_SET_CONTEXT: ClassVar[int]
    """"""
    THREAD_SET_INFORMATION: ClassVar[int]
    """"""
    THREAD_SET_THREAD_TOKEN: ClassVar[int]
    """"""
    THREAD_SUSPEND_RESUME: ClassVar[int]
    """"""
    THREAD_TERMINATE: ClassVar[int]
    """"""
    TOKEN_ADJUST_PRIVILEGES: ClassVar[int]
    """"""
    TOKEN_ALL_ACCESS: ClassVar[int]
    """"""
    TOKEN_EXECUTE: ClassVar[int]
    """"""
    TOKEN_IMPERSONATE: ClassVar[int]
    """"""
    TOKEN_QUERY: ClassVar[int]
    """"""
    TOKEN_READ: ClassVar[int]
    """"""
    TOKEN_TYPE_TokenImpersonation: ClassVar[int]
    """"""
    TOKEN_TYPE_TokenPrimary: ClassVar[int]
    """"""
    UISF_HIDEACCEL: ClassVar[int]
    """"""
    UISF_HIDEFOCUS: ClassVar[int]
    """"""
    UIS_CLEAR: ClassVar[int]
    """"""
    UIS_SET: ClassVar[int]
    """"""
    UOI_FLAGS: ClassVar[int]
    """"""
    UOI_NAME: ClassVar[int]
    """"""
    UOI_TYPE: ClassVar[int]
    """"""
    UOI_USER_SID: ClassVar[int]
    """"""
    USERCLASSTYPE_FULL: ClassVar[int]
    """"""
    VER_PLATFORM_WIN32_NT: ClassVar[int]
    """"""
    VFT2_DRV_COMM: ClassVar[int]
    """"""
    VFT2_DRV_DISPLAY: ClassVar[int]
    """"""
    VFT2_DRV_INPUTMETHOD: ClassVar[int]
    """"""
    VFT2_DRV_INSTALLABLE: ClassVar[int]
    """"""
    VFT2_DRV_KEYBOARD: ClassVar[int]
    """"""
    VFT2_DRV_LANGUAGE: ClassVar[int]
    """"""
    VFT2_DRV_MOUSE: ClassVar[int]
    """"""
    VFT2_DRV_NETWORK: ClassVar[int]
    """"""
    VFT2_DRV_PRINTER: ClassVar[int]
    """"""
    VFT2_DRV_SOUND: ClassVar[int]
    """"""
    VFT2_DRV_SYSTEM: ClassVar[int]
    """"""
    VFT2_FONT_RASTER: ClassVar[int]
    """"""
    VFT2_FONT_TRUETYPE: ClassVar[int]
    """"""
    VFT2_FONT_VECTOR: ClassVar[int]
    """"""
    VFT2_UNKNOWN: ClassVar[int]
    """"""
    VFT_APP: ClassVar[int]
    """"""
    VFT_DLL: ClassVar[int]
    """"""
    VFT_DRV: ClassVar[int]
    """"""
    VFT_FONT: ClassVar[int]
    """"""
    VFT_STATIC_LIB: ClassVar[int]
    """"""
    VFT_UNKNOWN: ClassVar[int]
    """"""
    VFT_VXD: ClassVar[int]
    """"""
    VS_FFI_FILEFLAGSMASK: ClassVar[int]
    """"""
    VS_FFI_SIGNATURE: ClassVar[int]
    """"""
    VS_FFI_STRUCVERSION: ClassVar[int]
    """"""
    VS_FF_DEBUG: ClassVar[int]
    """"""
    VS_FF_INFOINFERRED: ClassVar[int]
    """"""
    VS_FF_PATCHED: ClassVar[int]
    """"""
    VS_FF_PRERELEASE: ClassVar[int]
    """"""
    VS_FF_PRIVATEBUILD: ClassVar[int]
    """"""
    VS_FF_SPECIALBUILD: ClassVar[int]
    """"""
    VS_FILE_INFO: ClassVar[int]
    """"""
    VS_USER_DEFINED: ClassVar[int]
    """"""
    VS_VERSION_INFO: ClassVar[int]
    """"""
    WAIT_ABANDONED: ClassVar[int]
    """"""
    WAIT_ABANDONED_0: ClassVar[int]
    """"""
    WAIT_FAILED: ClassVar[int]
    """"""
    WAIT_OBJECT_0: ClassVar[int]
    """"""
    WAIT_TIMEOUT: ClassVar[int]
    """"""
    WHITENESS: ClassVar[int]
    """"""
    WM_CLOSE: ClassVar[int]
    """"""
    WM_COMPACTING: ClassVar[int]
    """"""
    WM_CREATETIMER: ClassVar[int]
    """"""
    WM_DISPLAYCHANGE: ClassVar[int]
    """"""
    WM_ENDSESSION: ClassVar[int]
    """"""
    WM_FONTCHANGE: ClassVar[int]
    """"""
    WM_KILLTIMER: ClassVar[int]
    """"""
    WM_NULL: ClassVar[int]
    """"""
    WM_PALETTECHANGED: ClassVar[int]
    """"""
    WM_POWERBROADCAST: ClassVar[int]
    """"""
    WM_QUERYENDSESSION: ClassVar[int]
    """"""
    WM_QUIT: ClassVar[int]
    """"""
    WM_REFLECT: ClassVar[int]
    """"""
    WM_SETTINGCHANGE: ClassVar[int]
    """"""
    WM_SYSCOLORCHANGE: ClassVar[int]
    """"""
    WM_THEMECHANGED: ClassVar[int]
    """"""
    WM_TIMECHANGE: ClassVar[int]
    """"""
    WM_TIMER: ClassVar[int]
    """"""
    WM_USER: ClassVar[int]
    """"""
    WM_WTSSESSION_CHANGE: ClassVar[int]
    """"""
    WSF_VISIBLE: ClassVar[int]
    """"""
    WS_DISABLED: ClassVar[int]
    """"""
    WS_POPUP: ClassVar[int]
    """"""
    WS_VISIBLE: ClassVar[int]
    """"""
    WTS_CONSOLE_CONNECT: ClassVar[int]
    """"""
    WTS_CONSOLE_DISCONNECT: ClassVar[int]
    """"""
    WTS_REMOTE_CONNECT: ClassVar[int]
    """"""
    WTS_REMOTE_DISCONNECT: ClassVar[int]
    """"""
    WTS_SESSION_LOCK: ClassVar[int]
    """"""
    WTS_SESSION_LOGOFF: ClassVar[int]
    """"""
    WTS_SESSION_LOGON: ClassVar[int]
    """"""
    WTS_SESSION_REMOTE_CONTROL: ClassVar[int]
    """"""
    WTS_SESSION_UNLOCK: ClassVar[int]
    """"""
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
        """"""
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
        """"""
    @classmethod
    def CreatePipe(
        cls,
        hReadPipe: SafeFileHandle,
        hWritePipe: SafeFileHandle,
        lpPipeAttributes: NativeMethods.SECURITY_ATTRIBUTES,
        nSize: int,
    ) -> tuple[bool, SafeFileHandle, SafeFileHandle]:
        """"""
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
        """"""
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
        """"""
    @classmethod
    def CreateToolhelp32Snapshot(cls, flags: int, processId: int) -> IntPtr:
        """"""
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
        """"""
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
        """"""
    @classmethod
    def EnumProcessModules(
        cls, handle: SafeProcessHandle, modules: IntPtr, size: int, needed: Int32
    ) -> bool:
        """"""
    @classmethod
    def EnumProcesses(cls, processIds: Array[int], size: int, needed: Int32) -> tuple[bool, Int32]:
        """"""
    @classmethod
    def EnumWindows(
        cls, callback: NativeMethods.EnumThreadWindowsCallback, extraData: IntPtr
    ) -> bool:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def GetCurrentProcess(cls) -> IntPtr:
        """"""
    @classmethod
    def GetCurrentProcessId(cls) -> int:
        """"""
    @classmethod
    def GetExitCodeProcess(
        cls, processHandle: SafeProcessHandle, exitCode: Int32
    ) -> tuple[bool, Int32]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @classmethod
    def GetModuleBaseName(
        cls,
        processHandle: SafeProcessHandle,
        moduleHandle: HandleRef,
        baseName: StringBuilder,
        size: int,
    ) -> int:
        """"""
    @classmethod
    @overload
    def GetModuleFileNameEx(
        cls,
        processHandle: SafeProcessHandle,
        moduleHandle: HandleRef,
        baseName: StringBuilder,
        size: int,
    ) -> int:
        """"""
    @classmethod
    @overload
    def GetModuleFileNameEx(
        cls, processHandle: HandleRef, moduleHandle: HandleRef, baseName: StringBuilder, size: int
    ) -> int:
        """"""
    @classmethod
    def GetModuleInformation(
        cls,
        processHandle: SafeProcessHandle,
        moduleHandle: HandleRef,
        ntModuleInfo: NativeMethods.NtModuleInfo,
        size: int,
    ) -> bool:
        """"""
    @classmethod
    def GetPriorityClass(cls, handle: SafeProcessHandle) -> int:
        """"""
    @classmethod
    def GetProcessAffinityMask(
        cls, handle: SafeProcessHandle, processMask: IntPtr, systemMask: IntPtr
    ) -> tuple[bool, IntPtr, IntPtr]:
        """"""
    @classmethod
    def GetProcessPriorityBoost(
        cls, handle: SafeProcessHandle, disabled: Boolean
    ) -> tuple[bool, Boolean]:
        """"""
    @classmethod
    def GetProcessTimes(
        cls, handle: SafeProcessHandle, creation: Int64, exit: Int64, kernel: Int64, user: Int64
    ) -> tuple[bool, Int64, Int64, Int64, Int64]:
        """"""
    @classmethod
    def GetProcessWorkingSetSize(
        cls, handle: SafeProcessHandle, min: IntPtr, max: IntPtr
    ) -> tuple[bool, IntPtr, IntPtr]:
        """"""
    @classmethod
    def GetStdHandle(cls, whichHandle: int) -> IntPtr:
        """"""
    @classmethod
    def GetThreadPriority(cls, handle: SafeThreadHandle) -> int:
        """"""
    @classmethod
    def GetThreadPriorityBoost(
        cls, handle: SafeThreadHandle, disabled: Boolean
    ) -> tuple[bool, Boolean]:
        """"""
    @classmethod
    def GetThreadTimes(
        cls, handle: SafeThreadHandle, creation: Int64, exit: Int64, kernel: Int64, user: Int64
    ) -> tuple[bool, Int64, Int64, Int64, Int64]:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def GetWindow(cls, hWnd: HandleRef, uCmd: int) -> IntPtr:
        """"""
    @classmethod
    def GetWindowLong(cls, hWnd: HandleRef, nIndex: int) -> int:
        """"""
    @classmethod
    def GetWindowText(cls, hWnd: HandleRef, lpString: StringBuilder, nMaxCount: int) -> int:
        """"""
    @classmethod
    def GetWindowTextLength(cls, hWnd: HandleRef) -> int:
        """"""
    @classmethod
    def GetWindowThreadProcessId(cls, handle: HandleRef, processId: Int32) -> tuple[int, Int32]:
        """"""
    @classmethod
    def IsWindowVisible(cls, hWnd: HandleRef) -> bool:
        """"""
    @classmethod
    def LookupPrivilegeValue(
        cls, lpSystemName: str, lpName: str, lpLuid: LUID
    ) -> tuple[bool, LUID]:
        """"""
    @classmethod
    def Module32First(cls, handle: HandleRef, entry: IntPtr) -> bool:
        """"""
    @classmethod
    def Module32Next(cls, handle: HandleRef, entry: IntPtr) -> bool:
        """"""
    @classmethod
    def NtQueryInformationProcess(
        cls,
        processHandle: SafeProcessHandle,
        query: int,
        info: NativeMethods.NtProcessBasicInfo,
        size: int,
        returnedSize: Array[int],
    ) -> int:
        """"""
    @classmethod
    def NtQuerySystemInformation(
        cls, query: int, dataPtr: IntPtr, size: int, returnedSize: Int32
    ) -> tuple[int, Int32]:
        """"""
    @classmethod
    def OpenProcess(cls, access: int, inherit: bool, processId: int) -> SafeProcessHandle:
        """"""
    @classmethod
    def OpenProcessToken(
        cls, ProcessHandle: HandleRef, DesiredAccess: int, TokenHandle: IntPtr
    ) -> tuple[bool, IntPtr]:
        """"""
    @classmethod
    def OpenThread(cls, access: int, inherit: bool, threadId: int) -> SafeThreadHandle:
        """"""
    @classmethod
    def PostMessage(cls, hwnd: HandleRef, msg: int, wparam: IntPtr, lparam: IntPtr) -> int:
        """"""
    @classmethod
    def Process32First(cls, handle: HandleRef, entry: IntPtr) -> bool:
        """"""
    @classmethod
    def Process32Next(cls, handle: HandleRef, entry: IntPtr) -> bool:
        """"""
    @classmethod
    def RtlGetVersion(
        cls, lpVersionInformation: RTL_OSVERSIONINFOEX
    ) -> tuple[int, RTL_OSVERSIONINFOEX]:
        """"""
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
        """"""
    @classmethod
    def SetPriorityClass(cls, handle: SafeProcessHandle, priorityClass: int) -> bool:
        """"""
    @classmethod
    def SetProcessAffinityMask(cls, handle: SafeProcessHandle, mask: IntPtr) -> bool:
        """"""
    @classmethod
    def SetProcessPriorityBoost(cls, handle: SafeProcessHandle, disabled: bool) -> bool:
        """"""
    @classmethod
    def SetProcessWorkingSetSize(cls, handle: SafeProcessHandle, min: IntPtr, max: IntPtr) -> bool:
        """"""
    @classmethod
    def SetThreadAffinityMask(cls, handle: SafeThreadHandle, mask: HandleRef) -> IntPtr:
        """"""
    @classmethod
    def SetThreadIdealProcessor(cls, handle: SafeThreadHandle, processor: int) -> int:
        """"""
    @classmethod
    def SetThreadPriority(cls, handle: SafeThreadHandle, priority: int) -> bool:
        """"""
    @classmethod
    def SetThreadPriorityBoost(cls, handle: SafeThreadHandle, disabled: bool) -> bool:
        """"""
    @classmethod
    def ShellExecuteEx(cls, info: NativeMethods.ShellExecuteInfo) -> bool:
        """"""
    @classmethod
    def TerminateProcess(cls, processHandle: SafeProcessHandle, exitCode: int) -> bool:
        """"""
    @classmethod
    def Thread32First(cls, handle: HandleRef, entry: NativeMethods.WinThreadEntry) -> bool:
        """"""
    @classmethod
    def Thread32Next(cls, handle: HandleRef, entry: NativeMethods.WinThreadEntry) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def WaitForInputIdle(cls, handle: SafeProcessHandle, milliseconds: int) -> int:
        """"""
    ConHndlr: Callable[[int], int] = ...
    """"""
    class MSG(ValueType):
        """"""

        hwnd: Final[IntPtr]
        """"""
        lParam: Final[IntPtr]
        """"""
        message: Final[int]
        """"""
        pt_x: Final[int]
        """"""
        pt_y: Final[int]
        """"""
        time: Final[int]
        """"""
        wParam: Final[IntPtr]
        """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def ToString(self) -> str:
            """"""

    class PDH_FMT_COUNTERVALUE(Object):
        """"""

        CStatus: Final[int]
        """"""
        data: Final[float]
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

    class PDH_RAW_COUNTER(Object):
        """"""

        CStatus: Final[int]
        """"""
        FirstValue: Final[int]
        """"""
        MultiCount: Final[int]
        """"""
        SecondValue: Final[int]
        """"""
        TimeStamp: Final[int]
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

    class RTL_OSVERSIONINFOEX(ValueType):
        """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def ToString(self) -> str:
            """"""

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
    """"""

class OAVariantLib(ABC, Object):
    """"""

    AlphaBool: ClassVar[int]
    """"""
    CalendarHijri: ClassVar[int]
    """"""
    LocalBool: ClassVar[int]
    """"""
    NoUserOverride: ClassVar[int]
    """"""
    NoValueProp: ClassVar[int]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class PowerModeChangedEventArgs(EventArgs):
    """"""
    def __init__(self, mode: PowerModes) -> None:
        """"""
    @property
    def Mode(self) -> PowerModes:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

PowerModeChangedEventHandler: Callable[[object, PowerModeChangedEventArgs], None] = ...
""""""

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

    ClassesRoot: ClassVar[RegistryKey]
    """"""
    CurrentConfig: ClassVar[RegistryKey]
    """"""
    CurrentUser: ClassVar[RegistryKey]
    """"""
    DynData: ClassVar[RegistryKey]
    """"""
    LocalMachine: ClassVar[RegistryKey]
    """"""
    PerformanceData: ClassVar[RegistryKey]
    """"""
    Users: ClassVar[RegistryKey]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def GetValue(cls, keyName: str, valueName: str, defaultValue: object) -> object:
        """"""
    @classmethod
    @overload
    def SetValue(cls, keyName: str, valueName: str, value: object) -> None:
        """"""
    @classmethod
    @overload
    def SetValue(
        cls, keyName: str, valueName: str, value: object, valueKind: RegistryValueKind
    ) -> None:
        """"""
    def ToString(self) -> str:
        """"""

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
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def SubKeyCount(self) -> int:
        """"""
    @property
    def ValueCount(self) -> int:
        """"""
    @property
    def View(self) -> RegistryView:
        """"""
    def Close(self) -> None:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    @overload
    def CreateSubKey(self, subkey: str) -> RegistryKey:
        """"""
    @overload
    def CreateSubKey(self, subkey: str, permissionCheck: RegistryKeyPermissionCheck) -> RegistryKey:
        """"""
    @overload
    def CreateSubKey(
        self, subkey: str, permissionCheck: RegistryKeyPermissionCheck, options: RegistryOptions
    ) -> RegistryKey:
        """"""
    @overload
    def CreateSubKey(
        self,
        subkey: str,
        permissionCheck: RegistryKeyPermissionCheck,
        registryOptions: RegistryOptions,
        registrySecurity: RegistrySecurity,
    ) -> RegistryKey:
        """"""
    @overload
    def CreateSubKey(
        self,
        subkey: str,
        permissionCheck: RegistryKeyPermissionCheck,
        registrySecurity: RegistrySecurity,
    ) -> RegistryKey:
        """"""
    @overload
    def CreateSubKey(self, subkey: str, writable: bool) -> RegistryKey:
        """"""
    @overload
    def CreateSubKey(self, subkey: str, writable: bool, options: RegistryOptions) -> RegistryKey:
        """"""
    @overload
    def DeleteSubKey(self, subkey: str) -> None:
        """"""
    @overload
    def DeleteSubKey(self, subkey: str, throwOnMissingSubKey: bool) -> None:
        """"""
    @overload
    def DeleteSubKeyTree(self, subkey: str) -> None:
        """"""
    @overload
    def DeleteSubKeyTree(self, subkey: str, throwOnMissingSubKey: bool) -> None:
        """"""
    @overload
    def DeleteValue(self, name: str) -> None:
        """"""
    @overload
    def DeleteValue(self, name: str, throwOnMissingValue: bool) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Flush(self) -> None:
        """"""
    @classmethod
    @overload
    def FromHandle(cls, handle: SafeRegistryHandle) -> RegistryKey:
        """"""
    @classmethod
    @overload
    def FromHandle(cls, handle: SafeRegistryHandle, view: RegistryView) -> RegistryKey:
        """"""
    @overload
    def GetAccessControl(self) -> RegistrySecurity:
        """"""
    @overload
    def GetAccessControl(self, includeSections: AccessControlSections) -> RegistrySecurity:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetLifetimeService(self) -> object:
        """"""
    def GetSubKeyNames(self) -> Array[str]:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def GetValue(self, name: str) -> object:
        """"""
    @overload
    def GetValue(self, name: str, defaultValue: object) -> object:
        """"""
    @overload
    def GetValue(self, name: str, defaultValue: object, options: RegistryValueOptions) -> object:
        """"""
    def GetValueKind(self, name: str) -> RegistryValueKind:
        """"""
    def GetValueNames(self) -> Array[str]:
        """"""
    def InitializeLifetimeService(self) -> object:
        """"""
    @classmethod
    def OpenBaseKey(cls, hKey: RegistryHive, view: RegistryView) -> RegistryKey:
        """"""
    @classmethod
    @overload
    def OpenRemoteBaseKey(cls, hKey: RegistryHive, machineName: str) -> RegistryKey:
        """"""
    @classmethod
    @overload
    def OpenRemoteBaseKey(
        cls, hKey: RegistryHive, machineName: str, view: RegistryView
    ) -> RegistryKey:
        """"""
    @overload
    def OpenSubKey(self, name: str) -> RegistryKey:
        """"""
    @overload
    def OpenSubKey(self, name: str, permissionCheck: RegistryKeyPermissionCheck) -> RegistryKey:
        """"""
    @overload
    def OpenSubKey(
        self, name: str, permissionCheck: RegistryKeyPermissionCheck, rights: RegistryRights
    ) -> RegistryKey:
        """"""
    @overload
    def OpenSubKey(self, name: str, rights: RegistryRights) -> RegistryKey:
        """"""
    @overload
    def OpenSubKey(self, name: str, writable: bool) -> RegistryKey:
        """"""
    def SetAccessControl(self, registrySecurity: RegistrySecurity) -> None:
        """"""
    @overload
    def SetValue(self, name: str, value: object) -> None:
        """"""
    @overload
    def SetValue(self, name: str, value: object, valueKind: RegistryValueKind) -> None:
        """"""
    def ToString(self) -> str:
        """"""

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
        """"""
    @property
    def IsInvalid(self) -> bool:
        """"""
    def Close(self) -> None:
        """"""
    def DangerousAddRef(self, success: Boolean) -> None:
        """"""
    def DangerousGetHandle(self) -> IntPtr:
        """"""
    def DangerousRelease(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def SetHandleAsInvalid(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class SafeNativeMethods(ABC, Object):
    """"""

    ERROR_INSUFFICIENT_BUFFER: ClassVar[int]
    """"""
    FORMAT_MESSAGE_ALLOCATE_BUFFER: ClassVar[int]
    """"""
    FORMAT_MESSAGE_ARGUMENT_ARRAY: ClassVar[int]
    """"""
    FORMAT_MESSAGE_FROM_HMODULE: ClassVar[int]
    """"""
    FORMAT_MESSAGE_FROM_STRING: ClassVar[int]
    """"""
    FORMAT_MESSAGE_FROM_SYSTEM: ClassVar[int]
    """"""
    FORMAT_MESSAGE_IGNORE_INSERTS: ClassVar[int]
    """"""
    FORMAT_MESSAGE_MAX_WIDTH_MASK: ClassVar[int]
    """"""
    MB_RIGHT: ClassVar[int]
    """"""
    MB_RTLREADING: ClassVar[int]
    """"""
    @classmethod
    def CloseHandle(cls, handle: IntPtr) -> bool:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def FormatFromRawValue(
        cls,
        dwCounterType: int,
        dwFormat: int,
        pTimeBase: Int64,
        pRawValue1: NativeMethods.PDH_RAW_COUNTER,
        pRawValue2: NativeMethods.PDH_RAW_COUNTER,
        pFmtValue: NativeMethods.PDH_FMT_COUNTERVALUE,
    ) -> int:
        """"""
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
        """"""
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
        """"""
    @classmethod
    def FreeLibrary(cls, hModule: HandleRef) -> bool:
        """"""
    @classmethod
    def GetComputerName(cls, lpBuffer: StringBuilder, nSize: Array[int]) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @classmethod
    def GetStockObject(cls, nIndex: int) -> IntPtr:
        """"""
    @classmethod
    def GetTextMetrics(
        cls, hDC: IntPtr, tm: NativeMethods.TEXTMETRIC
    ) -> tuple[bool, NativeMethods.TEXTMETRIC]:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def InterlockedCompareExchange(cls, pDestination: IntPtr, exchange: int, compare: int) -> int:
        """"""
    @classmethod
    def IsWow64Process(cls, hProcess: SafeProcessHandle, Wow64Process: Boolean) -> bool:
        """"""
    @classmethod
    def LoadLibrary(cls, libFilename: str) -> IntPtr:
        """"""
    @classmethod
    def MessageBox(cls, hWnd: IntPtr, text: str, caption: str, type: int) -> int:
        """"""
    @classmethod
    def OutputDebugString(cls, message: str) -> None:
        """"""
    @classmethod
    def QueryPerformanceCounter(cls, value: Int64) -> tuple[bool, Int64]:
        """"""
    @classmethod
    def QueryPerformanceFrequency(cls, value: Int64) -> tuple[bool, Int64]:
        """"""
    @classmethod
    def RegisterWindowMessage(cls, msg: str) -> int:
        """"""
    def ToString(self) -> str:
        """"""

class SessionEndReasons(Enum):
    """"""

    Logoff: SessionEndReasons = ...
    """"""
    SystemShutdown: SessionEndReasons = ...
    """"""

class SessionEndedEventArgs(EventArgs):
    """"""
    def __init__(self, reason: SessionEndReasons) -> None:
        """"""
    @property
    def Reason(self) -> SessionEndReasons:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

SessionEndedEventHandler: Callable[[object, SessionEndedEventArgs], None] = ...
""""""

class SessionEndingEventArgs(EventArgs):
    """"""
    def __init__(self, reason: SessionEndReasons) -> None:
        """"""
    @property
    def Cancel(self) -> bool:
        """"""
    @Cancel.setter
    def Cancel(self, value: bool) -> None: ...
    @property
    def Reason(self) -> SessionEndReasons:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

SessionEndingEventHandler: Callable[[object, SessionEndingEventArgs], None] = ...
""""""

class SessionSwitchEventArgs(EventArgs):
    """"""
    def __init__(self, reason: SessionSwitchReason) -> None:
        """"""
    @property
    def Reason(self) -> SessionSwitchReason:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

SessionSwitchEventHandler: Callable[[object, SessionSwitchEventArgs], None] = ...
""""""

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
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def InvokeOnEventsThread(cls, method: Delegate) -> None:
        """"""
    @classmethod
    def KillTimer(cls, timerId: IntPtr) -> None:
        """"""
    def ToString(self) -> str:
        """"""
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
    def __init__(self, timerId: IntPtr) -> None:
        """"""
    @property
    def TimerId(self) -> IntPtr:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

TimerElapsedEventHandler: Callable[[object, TimerElapsedEventArgs], None] = ...
""""""

class UnsafeNativeMethods(ABC, Object):
    """"""

    FILE_ACTION_ADDED: ClassVar[int]
    """"""
    FILE_ACTION_MODIFIED: ClassVar[int]
    """"""
    FILE_ACTION_REMOVED: ClassVar[int]
    """"""
    FILE_ACTION_RENAMED_NEW_NAME: ClassVar[int]
    """"""
    FILE_ACTION_RENAMED_OLD_NAME: ClassVar[int]
    """"""
    FILE_ADD_FILE: ClassVar[int]
    """"""
    FILE_ADD_SUBDIRECTORY: ClassVar[int]
    """"""
    FILE_APPEND_DATA: ClassVar[int]
    """"""
    FILE_ATTRIBUTE_ARCHIVE: ClassVar[int]
    """"""
    FILE_ATTRIBUTE_COMPRESSED: ClassVar[int]
    """"""
    FILE_ATTRIBUTE_DIRECTORY: ClassVar[int]
    """"""
    FILE_ATTRIBUTE_HIDDEN: ClassVar[int]
    """"""
    FILE_ATTRIBUTE_NORMAL: ClassVar[int]
    """"""
    FILE_ATTRIBUTE_OFFLINE: ClassVar[int]
    """"""
    FILE_ATTRIBUTE_READONLY: ClassVar[int]
    """"""
    FILE_ATTRIBUTE_SYSTEM: ClassVar[int]
    """"""
    FILE_ATTRIBUTE_TEMPORARY: ClassVar[int]
    """"""
    FILE_CASE_PRESERVED_NAMES: ClassVar[int]
    """"""
    FILE_CASE_SENSITIVE_SEARCH: ClassVar[int]
    """"""
    FILE_CREATE_PIPE_INSTANCE: ClassVar[int]
    """"""
    FILE_DELETE_CHILD: ClassVar[int]
    """"""
    FILE_EXECUTE: ClassVar[int]
    """"""
    FILE_FILE_COMPRESSION: ClassVar[int]
    """"""
    FILE_FLAG_BACKUP_SEMANTICS: ClassVar[int]
    """"""
    FILE_FLAG_DELETE_ON_CLOSE: ClassVar[int]
    """"""
    FILE_FLAG_NO_BUFFERING: ClassVar[int]
    """"""
    FILE_FLAG_OVERLAPPED: ClassVar[int]
    """"""
    FILE_FLAG_POSIX_SEMANTICS: ClassVar[int]
    """"""
    FILE_FLAG_RANDOM_ACCESS: ClassVar[int]
    """"""
    FILE_FLAG_SEQUENTIAL_SCAN: ClassVar[int]
    """"""
    FILE_FLAG_WRITE_THROUGH: ClassVar[int]
    """"""
    FILE_LIST_DIRECTORY: ClassVar[int]
    """"""
    FILE_NOTIFY_CHANGE_ATTRIBUTES: ClassVar[int]
    """"""
    FILE_NOTIFY_CHANGE_CREATION: ClassVar[int]
    """"""
    FILE_NOTIFY_CHANGE_DIR_NAME: ClassVar[int]
    """"""
    FILE_NOTIFY_CHANGE_FILE_NAME: ClassVar[int]
    """"""
    FILE_NOTIFY_CHANGE_LAST_ACCESS: ClassVar[int]
    """"""
    FILE_NOTIFY_CHANGE_LAST_WRITE: ClassVar[int]
    """"""
    FILE_NOTIFY_CHANGE_SECURITY: ClassVar[int]
    """"""
    FILE_NOTIFY_CHANGE_SIZE: ClassVar[int]
    """"""
    FILE_PERSISTENT_ACLS: ClassVar[int]
    """"""
    FILE_READ_ATTRIBUTES: ClassVar[int]
    """"""
    FILE_READ_DATA: ClassVar[int]
    """"""
    FILE_READ_EA: ClassVar[int]
    """"""
    FILE_SHARE_DELETE: ClassVar[int]
    """"""
    FILE_SHARE_READ: ClassVar[int]
    """"""
    FILE_SHARE_WRITE: ClassVar[int]
    """"""
    FILE_TRAVERSE: ClassVar[int]
    """"""
    FILE_TYPE_CHAR: ClassVar[int]
    """"""
    FILE_TYPE_DISK: ClassVar[int]
    """"""
    FILE_TYPE_PIPE: ClassVar[int]
    """"""
    FILE_TYPE_REMOTE: ClassVar[int]
    """"""
    FILE_TYPE_UNKNOWN: ClassVar[int]
    """"""
    FILE_UNICODE_ON_DISK: ClassVar[int]
    """"""
    FILE_VOLUME_IS_COMPRESSED: ClassVar[int]
    """"""
    FILE_WRITE_ATTRIBUTES: ClassVar[int]
    """"""
    FILE_WRITE_DATA: ClassVar[int]
    """"""
    FILE_WRITE_EA: ClassVar[int]
    """"""
    GetFileExInfoStandard: ClassVar[int]
    """"""
    OPEN_ALWAYS: ClassVar[int]
    """"""
    OPEN_EXISTING: ClassVar[int]
    """"""
    @classmethod
    def ClearEventLog(cls, hEventLog: SafeHandle, lpctstrBackupFileName: HandleRef) -> bool:
        """"""
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
        """"""
    @classmethod
    def DefWindowProc(cls, hWnd: IntPtr, msg: int, wParam: IntPtr, lParam: IntPtr) -> IntPtr:
        """"""
    @classmethod
    def DestroyWindow(cls, hWnd: HandleRef) -> bool:
        """"""
    @classmethod
    def DispatchMessage(cls, msg: MSG) -> int:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def GetClassInfo(
        cls, hInst: HandleRef, lpszClass: str, wc: NativeMethods.WNDCLASS_I
    ) -> tuple[bool, NativeMethods.WNDCLASS_I]:
        """"""
    @classmethod
    def GetDC(cls, hWnd: IntPtr) -> IntPtr:
        """"""
    @classmethod
    def GetFileVersionInfo(
        cls, lptstrFilename: str, dwHandle: int, dwLen: int, lpData: HandleRef
    ) -> bool:
        """"""
    @classmethod
    def GetFileVersionInfoSize(cls, lptstrFilename: str, handle: Int32) -> tuple[int, Int32]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @classmethod
    def GetModuleFileName(cls, hModule: HandleRef, buffer: StringBuilder, length: int) -> int:
        """"""
    @classmethod
    def GetModuleHandle(cls, modName: str) -> IntPtr:
        """"""
    @classmethod
    def GetNumberOfEventLogRecords(cls, hEventLog: SafeHandle, count: Int32) -> tuple[bool, Int32]:
        """"""
    @classmethod
    def GetOldestEventLogRecord(cls, hEventLog: SafeHandle, number: Int32) -> tuple[bool, Int32]:
        """"""
    @classmethod
    @overload
    def GetProcAddress(cls, hModule: HandleRef, lpProcName: str) -> IntPtr:
        """"""
    @classmethod
    @overload
    def GetProcAddress(cls, hModule: IntPtr, methodName: str) -> IntPtr:
        """"""
    @classmethod
    def GetProcessWindowStation(cls) -> IntPtr:
        """"""
    @classmethod
    def GetStdHandle(cls, type: int) -> IntPtr:
        """"""
    @classmethod
    def GetSystemMetrics(cls, nIndex: int) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def GetUserObjectInformation(
        cls,
        hObj: HandleRef,
        nIndex: int,
        pvBuffer: NativeMethods.USEROBJECTFLAGS,
        nLength: int,
        lpnLengthNeeded: Int32,
    ) -> bool:
        """"""
    @classmethod
    def IsWindow(cls, hWnd: HandleRef) -> bool:
        """"""
    @classmethod
    def KillTimer(cls, hwnd: HandleRef, idEvent: HandleRef) -> bool:
        """"""
    @classmethod
    def LookupAccountSid(
        cls,
        systemName: str,
        pSid: Array[int],
        szUserName: StringBuilder,
        userNameSize: Int32,
        szDomainName: StringBuilder,
        domainNameSize: Int32,
        eUse: Int32,
    ) -> int:
        """"""
    @classmethod
    def MsgWaitForMultipleObjectsEx(
        cls, nCount: int, pHandles: IntPtr, dwMilliseconds: int, dwWakeMask: int, dwFlags: int
    ) -> int:
        """"""
    @classmethod
    def NotifyChangeEventLog(cls, hEventLog: SafeHandle, hEvent: SafeWaitHandle) -> bool:
        """"""
    @classmethod
    def PeekMessage(
        cls, msg: MSG, hwnd: HandleRef, msgMin: int, msgMax: int, remove: int
    ) -> tuple[bool, MSG]:
        """"""
    @classmethod
    def PostMessage(cls, hwnd: HandleRef, msg: int, wparam: IntPtr, lparam: IntPtr) -> bool:
        """"""
    @classmethod
    def ReadDirectoryChangesW(
        cls,
        hDirectory: SafeFileHandle,
        lpBuffer: HandleRef,
        nBufferLength: int,
        bWatchSubtree: int,
        dwNotifyFilter: int,
        lpBytesReturned: Int32,
        overlappedPointer: NativeOverlapped,
        lpCompletionRoutine: HandleRef,
    ) -> tuple[bool, Int32]:
        """"""
    @classmethod
    def ReadEventLog(
        cls,
        hEventLog: SafeHandle,
        dwReadFlags: int,
        dwRecordOffset: int,
        buffer: Array[int],
        numberOfBytesToRead: int,
        bytesRead: Int32,
        minNumOfBytesNeeded: Int32,
    ) -> tuple[bool, Int32, Int32]:
        """"""
    @classmethod
    def RegisterClass(cls, wc: NativeMethods.WNDCLASS) -> int:
        """"""
    @classmethod
    def ReleaseDC(cls, hWnd: IntPtr, hDC: IntPtr) -> int:
        """"""
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
        """"""
    @classmethod
    def SelectObject(cls, hDC: IntPtr, hObject: IntPtr) -> IntPtr:
        """"""
    @classmethod
    def SendMessage(cls, hWnd: HandleRef, msg: int, wParam: IntPtr, lParam: IntPtr) -> IntPtr:
        """"""
    @classmethod
    def SetClassLong(cls, hWnd: HandleRef, nIndex: int, dwNewLong: IntPtr) -> IntPtr:
        """"""
    @classmethod
    def SetClassLongPtr32(cls, hwnd: HandleRef, nIndex: int, dwNewLong: IntPtr) -> IntPtr:
        """"""
    @classmethod
    def SetClassLongPtr64(cls, hwnd: HandleRef, nIndex: int, dwNewLong: IntPtr) -> IntPtr:
        """"""
    @classmethod
    def SetConsoleCtrlHandler(cls, handler: NativeMethods.ConHndlr, add: int) -> bool:
        """"""
    @classmethod
    def SetTimer(
        cls, hWnd: HandleRef, nIDEvent: HandleRef, uElapse: int, lpTimerProc: HandleRef
    ) -> IntPtr:
        """"""
    @classmethod
    def SetWindowLong(cls, hWnd: HandleRef, nIndex: int, dwNewLong: HandleRef) -> IntPtr:
        """"""
    @classmethod
    def SetWindowLongPtr32(cls, hWnd: HandleRef, nIndex: int, dwNewLong: HandleRef) -> IntPtr:
        """"""
    @classmethod
    def SetWindowLongPtr64(cls, hWnd: HandleRef, nIndex: int, dwNewLong: HandleRef) -> IntPtr:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def TranslateMessage(cls, msg: MSG) -> tuple[bool, MSG]:
        """"""
    @classmethod
    def UnregisterClass(cls, lpClassName: str, hInstance: HandleRef) -> int:
        """"""
    @classmethod
    def VerLanguageName(cls, langID: int, lpBuffer: StringBuilder, nSize: int) -> int:
        """"""
    @classmethod
    def VerQueryValue(
        cls, pBlock: HandleRef, lpSubBlock: str, lplpBuffer: IntPtr, len: Int32
    ) -> tuple[bool, IntPtr, Int32]:
        """"""
    @classmethod
    def WTSRegisterSessionNotification(cls, hWnd: HandleRef, dwFlags: int) -> bool:
        """"""
    @classmethod
    def WTSUnRegisterSessionNotification(cls, hWnd: HandleRef) -> bool:
        """"""
    @classmethod
    def WaitNamedPipe(cls, name: str, timeout: int) -> bool:
        """"""
    @classmethod
    def WldpIsDynamicCodePolicyEnabled(cls, enabled: Int32) -> tuple[int, Int32]:
        """"""
    @classmethod
    def WldpQueryDynamicCodeTrust(
        cls, fileHandle: SafeFileHandle, image: IntPtr, imageSize: int
    ) -> int:
        """"""
    @classmethod
    def WldpSetDynamicCodeTrust(cls, fileHandle: SafeFileHandle) -> int:
        """"""
    class WIN32_FILE_ATTRIBUTE_DATA(ValueType):
        """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def ToString(self) -> str:
            """"""

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
    def __init__(self, category: UserPreferenceCategory) -> None:
        """"""
    @property
    def Category(self) -> UserPreferenceCategory:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

UserPreferenceChangedEventHandler: Callable[[object, UserPreferenceChangedEventArgs], None] = ...
""""""

class UserPreferenceChangingEventArgs(EventArgs):
    """"""
    def __init__(self, category: UserPreferenceCategory) -> None:
        """"""
    @property
    def Category(self) -> UserPreferenceCategory:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

UserPreferenceChangingEventHandler: Callable[[object, UserPreferenceChangingEventArgs], None] = ...
""""""

class Win32Native(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class WinInetCache(RequestCache):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
