from __future__ import annotations

from abc import ABC
from typing import Callable, Generic, List, Protocol, Tuple, TypeVar, Union, overload

from Microsoft.Win32.SafeHandles import SafeFileHandle, SafeHandleZeroOrMinusOneIsInvalid, SafeProcessHandle, SafeRegistryHandle, SafeThreadHandle, SafeWaitHandle
from System import Array, AsyncCallback, Boolean, Byte, Delegate, Double, Enum, EventArgs, EventHandler, IAsyncResult, ICloneable, IDisposable, Int16, Int32, Int64, IntPtr, MarshalByRefObject, MulticastDelegate, Object, String, UInt16, UInt32, Uri, ValueType, Void, __ComObject
from System.Collections import ArrayList
from System.Net import IAuthenticationModule, ICredentialPolicy, NetworkCredential, WebRequest
from System.Net.Cache import RequestCache
from System.Runtime.InteropServices import HandleRef, SafeHandle
from System.Runtime.Serialization import ISerializable
from System.Security.AccessControl import AccessControlSections, RegistryRights, RegistrySecurity
from System.Text import StringBuilder
from System.Threading import NativeOverlapped

# ---------- Types ---------- #

T = TypeVar('T')

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
ByteType = Union[int, Byte]
DoubleType = Union[float, Double]
IntType = Union[int, Int32]
LongType = Union[int, Int64]
NIntType = Union[int, IntPtr]
ObjectType = Object
ShortType = Union[int, Int16]
StringType = Union[str, String]
UIntType = Union[int, UInt32]
UShortType = Union[int, UInt16]
VoidType = Union[None, Void]


class EventType(Generic[T]):
    def __iadd__(self, other: T): ...
    
    def __isub__(self, other: T): ...



# ---------- Classes ---------- #

class ASM_CACHE(ABC, ObjectType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def DOWNLOAD() -> UIntType: ...
    
    @staticmethod
    @property
    def GAC() -> UIntType: ...
    
    @staticmethod
    @property
    def ZAP() -> UIntType: ...
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ASM_NAME(ABC, ObjectType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def ALIAS() -> UIntType: ...
    
    @staticmethod
    @property
    def BUILD_NUMBER() -> UIntType: ...
    
    @staticmethod
    @property
    def CODEBASE_LASTMOD() -> UIntType: ...
    
    @staticmethod
    @property
    def CODEBASE_URL() -> UIntType: ...
    
    @staticmethod
    @property
    def CULTURE() -> UIntType: ...
    
    @staticmethod
    @property
    def CUSTOM() -> UIntType: ...
    
    @staticmethod
    @property
    def HASH_ALGID() -> UIntType: ...
    
    @staticmethod
    @property
    def HASH_VALUE() -> UIntType: ...
    
    @staticmethod
    @property
    def MAJOR_VERSION() -> UIntType: ...
    
    @staticmethod
    @property
    def MAX_PARAMS() -> UIntType: ...
    
    @staticmethod
    @property
    def MINOR_VERSION() -> UIntType: ...
    
    @staticmethod
    @property
    def MVID() -> UIntType: ...
    
    @staticmethod
    @property
    def NAME() -> UIntType: ...
    
    @staticmethod
    @property
    def NULL_CUSTOM() -> UIntType: ...
    
    @staticmethod
    @property
    def NULL_PUBLIC_KEY() -> UIntType: ...
    
    @staticmethod
    @property
    def NULL_PUBLIC_KEY_TOKEN() -> UIntType: ...
    
    @staticmethod
    @property
    def OSINFO_ARRAY() -> UIntType: ...
    
    @staticmethod
    @property
    def PROCESSOR_ID_ARRAY() -> UIntType: ...
    
    @staticmethod
    @property
    def PUBLIC_KEY() -> UIntType: ...
    
    @staticmethod
    @property
    def PUBLIC_KEY_TOKEN() -> UIntType: ...
    
    @staticmethod
    @property
    def REVISION_NUMBER() -> UIntType: ...
    
    @staticmethod
    @property
    def _32_BIT_ONLY() -> UIntType: ...
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CANOF(ABC, ObjectType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def PARSE_DISPLAY_NAME() -> UIntType: ...
    
    @staticmethod
    @property
    def SET_DEFAULT_VALUES() -> UIntType: ...
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Fusion(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def ReadCache(alAssems: ArrayList, name: StringType, nFlag: UIntType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class InternetSecurityManager(__ComObject):
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


class IntranetZoneCredentialPolicy(ObjectType, ICredentialPolicy):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def ShouldSendCredential(self, challengeUri: Uri, request: WebRequest, credential: NetworkCredential, authModule: IAuthenticationModule) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class NativeMethods(ABC, ObjectType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def BACKWARDS_READ() -> IntType: ...
    
    @staticmethod
    @property
    def COLOR_WINDOW() -> IntType: ...
    
    @staticmethod
    @property
    def CREATE_ALWAYS() -> IntType: ...
    
    @staticmethod
    @property
    def CREATE_NO_WINDOW() -> IntType: ...
    
    @staticmethod
    @property
    def CREATE_SUSPENDED() -> IntType: ...
    
    @staticmethod
    @property
    def CREATE_UNICODE_ENVIRONMENT() -> IntType: ...
    
    @staticmethod
    @property
    def CTRL_BREAK_EVENT() -> IntType: ...
    
    @staticmethod
    @property
    def CTRL_CLOSE_EVENT() -> IntType: ...
    
    @staticmethod
    @property
    def CTRL_C_EVENT() -> IntType: ...
    
    @staticmethod
    @property
    def CTRL_LOGOFF_EVENT() -> IntType: ...
    
    @staticmethod
    @property
    def CTRL_SHUTDOWN_EVENT() -> IntType: ...
    
    @staticmethod
    @property
    def DEFAULT_GUI_FONT() -> IntType: ...
    
    @staticmethod
    @property
    def DUPLICATE_CLOSE_SOURCE() -> IntType: ...
    
    @staticmethod
    @property
    def DUPLICATE_SAME_ACCESS() -> IntType: ...
    
    @staticmethod
    @property
    def DWORD_SIZE() -> IntType: ...
    
    @staticmethod
    @property
    def ENDSESSION_LOGOFF() -> IntType: ...
    
    @staticmethod
    @property
    def ERROR_ACCESS_DENIED() -> IntType: ...
    
    @staticmethod
    @property
    def ERROR_ALREADY_EXISTS() -> IntType: ...
    
    @staticmethod
    @property
    def ERROR_BAD_COMMAND() -> IntType: ...
    
    @staticmethod
    @property
    def ERROR_BAD_EXE_FORMAT() -> IntType: ...
    
    @staticmethod
    @property
    def ERROR_BROKEN_PIPE() -> IntType: ...
    
    @staticmethod
    @property
    def ERROR_BUSY() -> IntType: ...
    
    @staticmethod
    @property
    def ERROR_CANCELLED() -> IntType: ...
    
    @staticmethod
    @property
    def ERROR_CLASS_ALREADY_EXISTS() -> IntType: ...
    
    @staticmethod
    @property
    def ERROR_COUNTER_TIMEOUT() -> IntType: ...
    
    @staticmethod
    @property
    def ERROR_DDE_FAIL() -> IntType: ...
    
    @staticmethod
    @property
    def ERROR_DLL_NOT_FOUND() -> IntType: ...
    
    @staticmethod
    @property
    def ERROR_EVENTLOG_FILE_CHANGED() -> IntType: ...
    
    @staticmethod
    @property
    def ERROR_EXE_MACHINE_TYPE_MISMATCH() -> IntType: ...
    
    @staticmethod
    @property
    def ERROR_FILENAME_EXCED_RANGE() -> IntType: ...
    
    @staticmethod
    @property
    def ERROR_FILE_EXISTS() -> IntType: ...
    
    @staticmethod
    @property
    def ERROR_FILE_NOT_FOUND() -> IntType: ...
    
    @staticmethod
    @property
    def ERROR_HANDLE_EOF() -> IntType: ...
    
    @staticmethod
    @property
    def ERROR_INSUFFICIENT_BUFFER() -> IntType: ...
    
    @staticmethod
    @property
    def ERROR_INVALID_HANDLE() -> IntType: ...
    
    @staticmethod
    @property
    def ERROR_INVALID_NAME() -> IntType: ...
    
    @staticmethod
    @property
    def ERROR_INVALID_PARAMETER() -> IntType: ...
    
    @staticmethod
    @property
    def ERROR_IO_INCOMPLETE() -> IntType: ...
    
    @staticmethod
    @property
    def ERROR_IO_PENDING() -> IntType: ...
    
    @staticmethod
    @property
    def ERROR_LOCK_FAILED() -> IntType: ...
    
    @staticmethod
    @property
    def ERROR_MORE_DATA() -> IntType: ...
    
    @staticmethod
    @property
    def ERROR_NONE_MAPPED() -> IntType: ...
    
    @staticmethod
    @property
    def ERROR_NOT_ENOUGH_MEMORY() -> IntType: ...
    
    @staticmethod
    @property
    def ERROR_NOT_READY() -> IntType: ...
    
    @staticmethod
    @property
    def ERROR_NO_ASSOCIATION() -> IntType: ...
    
    @staticmethod
    @property
    def ERROR_NO_DATA() -> IntType: ...
    
    @staticmethod
    @property
    def ERROR_OPERATION_ABORTED() -> IntType: ...
    
    @staticmethod
    @property
    def ERROR_PARTIAL_COPY() -> IntType: ...
    
    @staticmethod
    @property
    def ERROR_PATH_NOT_FOUND() -> IntType: ...
    
    @staticmethod
    @property
    def ERROR_PROC_NOT_FOUND() -> IntType: ...
    
    @staticmethod
    @property
    def ERROR_SHARING_VIOLATION() -> IntType: ...
    
    @staticmethod
    @property
    def ERROR_SUCCESS() -> IntType: ...
    
    @staticmethod
    @property
    def E_ABORT() -> IntType: ...
    
    @staticmethod
    @property
    def E_NOTIMPL() -> IntType: ...
    
    @staticmethod
    @property
    def FILE_ATTRIBUTE_NORMAL() -> IntType: ...
    
    @staticmethod
    @property
    def FILE_FLAG_OVERLAPPED() -> IntType: ...
    
    @staticmethod
    @property
    def FILE_MAP_READ() -> IntType: ...
    
    @staticmethod
    @property
    def FILE_MAP_WRITE() -> IntType: ...
    
    @staticmethod
    @property
    def FILE_SHARE_DELETE() -> IntType: ...
    
    @staticmethod
    @property
    def FILE_SHARE_READ() -> IntType: ...
    
    @staticmethod
    @property
    def FILE_SHARE_WRITE() -> IntType: ...
    
    @staticmethod
    @property
    def FORMAT_MESSAGE_ALLOCATE_BUFFER() -> IntType: ...
    
    @staticmethod
    @property
    def FORMAT_MESSAGE_ARGUMENT_ARRAY() -> IntType: ...
    
    @staticmethod
    @property
    def FORMAT_MESSAGE_FROM_HMODULE() -> IntType: ...
    
    @staticmethod
    @property
    def FORMAT_MESSAGE_FROM_STRING() -> IntType: ...
    
    @staticmethod
    @property
    def FORMAT_MESSAGE_FROM_SYSTEM() -> IntType: ...
    
    @staticmethod
    @property
    def FORMAT_MESSAGE_IGNORE_INSERTS() -> IntType: ...
    
    @staticmethod
    @property
    def FORMAT_MESSAGE_MAX_WIDTH_MASK() -> IntType: ...
    
    @staticmethod
    @property
    def FORWARDS_READ() -> IntType: ...
    
    @staticmethod
    @property
    def GCL_WNDPROC() -> IntType: ...
    
    @staticmethod
    @property
    def GENERIC_ALL() -> IntType: ...
    
    @staticmethod
    @property
    def GENERIC_EXECUTE() -> IntType: ...
    
    @staticmethod
    @property
    def GENERIC_READ() -> IntType: ...
    
    @staticmethod
    @property
    def GENERIC_WRITE() -> IntType: ...
    
    @staticmethod
    @property
    def GHND() -> IntType: ...
    
    @staticmethod
    @property
    def GMEM_DDESHARE() -> IntType: ...
    
    @staticmethod
    @property
    def GMEM_DISCARDABLE() -> IntType: ...
    
    @staticmethod
    @property
    def GMEM_DISCARDED() -> IntType: ...
    
    @staticmethod
    @property
    def GMEM_FIXED() -> IntType: ...
    
    @staticmethod
    @property
    def GMEM_INVALID_HANDLE() -> IntType: ...
    
    @staticmethod
    @property
    def GMEM_LOCKCOUNT() -> IntType: ...
    
    @staticmethod
    @property
    def GMEM_LOWER() -> IntType: ...
    
    @staticmethod
    @property
    def GMEM_MODIFY() -> IntType: ...
    
    @staticmethod
    @property
    def GMEM_MOVEABLE() -> IntType: ...
    
    @staticmethod
    @property
    def GMEM_NOCOMPACT() -> IntType: ...
    
    @staticmethod
    @property
    def GMEM_NODISCARD() -> IntType: ...
    
    @staticmethod
    @property
    def GMEM_NOTIFY() -> IntType: ...
    
    @staticmethod
    @property
    def GMEM_NOT_BANKED() -> IntType: ...
    
    @staticmethod
    @property
    def GMEM_SHARE() -> IntType: ...
    
    @staticmethod
    @property
    def GMEM_VALID_FLAGS() -> IntType: ...
    
    @staticmethod
    @property
    def GMEM_ZEROINIT() -> IntType: ...
    
    @staticmethod
    @property
    def GPTR() -> IntType: ...
    
    @staticmethod
    @property
    def GWL_STYLE() -> IntType: ...
    
    @staticmethod
    @property
    def GWL_WNDPROC() -> IntType: ...
    
    @staticmethod
    @property
    def GW_OWNER() -> IntType: ...
    
    @staticmethod
    @property
    def HKEY_LOCAL_MACHINE() -> NIntType: ...
    
    @staticmethod
    @property
    def HKEY_PERFORMANCE_DATA() -> IntType: ...
    
    @staticmethod
    @property
    def IMPERSONATION_LEVEL_SecurityAnonymous() -> IntType: ...
    
    @staticmethod
    @property
    def IMPERSONATION_LEVEL_SecurityDelegation() -> IntType: ...
    
    @staticmethod
    @property
    def IMPERSONATION_LEVEL_SecurityIdentification() -> IntType: ...
    
    @staticmethod
    @property
    def IMPERSONATION_LEVEL_SecurityImpersonation() -> IntType: ...
    
    @staticmethod
    @property
    def INVALID_HANDLE_VALUE() -> NIntType: ...
    
    @staticmethod
    @property
    def KEY_ENUMERATE_SUB_KEYS() -> IntType: ...
    
    @staticmethod
    @property
    def KEY_NOTIFY() -> IntType: ...
    
    @staticmethod
    @property
    def KEY_QUERY_VALUE() -> IntType: ...
    
    @staticmethod
    @property
    def KEY_READ() -> IntType: ...
    
    @staticmethod
    @property
    def LARGE_INTEGER_SIZE() -> IntType: ...
    
    @staticmethod
    @property
    def LOAD_LIBRARY_AS_DATAFILE() -> IntType: ...
    
    @staticmethod
    @property
    def LOAD_WITH_ALTERED_SEARCH_PATH() -> IntType: ...
    
    @staticmethod
    @property
    def LOGON32_LOGON_BATCH() -> IntType: ...
    
    @staticmethod
    @property
    def LOGON32_LOGON_INTERACTIVE() -> IntType: ...
    
    @staticmethod
    @property
    def LOGON32_PROVIDER_DEFAULT() -> IntType: ...
    
    @staticmethod
    @property
    def MAX_PATH() -> IntType: ...
    
    @staticmethod
    @property
    def MOVEFILE_REPLACE_EXISTING() -> IntType: ...
    
    @staticmethod
    @property
    def MWMO_INPUTAVAILABLE() -> IntType: ...
    
    @staticmethod
    @property
    def NOTIFY_FOR_THIS_SESSION() -> IntType: ...
    
    @staticmethod
    @property
    def NtPerfCounterSizeDword() -> IntType: ...
    
    @staticmethod
    @property
    def NtPerfCounterSizeLarge() -> IntType: ...
    
    @staticmethod
    @property
    def NtQueryProcessBasicInfo() -> IntType: ...
    
    @staticmethod
    @property
    def NtQuerySystemProcessInformation() -> IntType: ...
    
    @staticmethod
    @property
    def NullHandleRef() -> HandleRef: ...
    
    @staticmethod
    @property
    def PAGE_READWRITE() -> IntType: ...
    
    @staticmethod
    @property
    def PBT_APMBATTERYLOW() -> IntType: ...
    
    @staticmethod
    @property
    def PBT_APMOEMEVENT() -> IntType: ...
    
    @staticmethod
    @property
    def PBT_APMPOWERSTATUSCHANGE() -> IntType: ...
    
    @staticmethod
    @property
    def PBT_APMQUERYSTANDBY() -> IntType: ...
    
    @staticmethod
    @property
    def PBT_APMQUERYSTANDBYFAILED() -> IntType: ...
    
    @staticmethod
    @property
    def PBT_APMQUERYSUSPEND() -> IntType: ...
    
    @staticmethod
    @property
    def PBT_APMQUERYSUSPENDFAILED() -> IntType: ...
    
    @staticmethod
    @property
    def PBT_APMRESUMECRITICAL() -> IntType: ...
    
    @staticmethod
    @property
    def PBT_APMRESUMESTANDBY() -> IntType: ...
    
    @staticmethod
    @property
    def PBT_APMRESUMESUSPEND() -> IntType: ...
    
    @staticmethod
    @property
    def PBT_APMSTANDBY() -> IntType: ...
    
    @staticmethod
    @property
    def PBT_APMSUSPEND() -> IntType: ...
    
    @staticmethod
    @property
    def PDH_CALC_NEGATIVE_DENOMINATOR() -> IntType: ...
    
    @staticmethod
    @property
    def PDH_CALC_NEGATIVE_VALUE() -> IntType: ...
    
    @staticmethod
    @property
    def PDH_FMT_DOUBLE() -> UIntType: ...
    
    @staticmethod
    @property
    def PDH_FMT_NOCAP100() -> UIntType: ...
    
    @staticmethod
    @property
    def PDH_FMT_NOSCALE() -> UIntType: ...
    
    @staticmethod
    @property
    def PDH_NO_DATA() -> IntType: ...
    
    @staticmethod
    @property
    def PERF_100NSEC_MULTI_TIMER() -> IntType: ...
    
    @staticmethod
    @property
    def PERF_100NSEC_MULTI_TIMER_INV() -> IntType: ...
    
    @staticmethod
    @property
    def PERF_100NSEC_TIMER() -> IntType: ...
    
    @staticmethod
    @property
    def PERF_100NSEC_TIMER_INV() -> IntType: ...
    
    @staticmethod
    @property
    def PERF_AVERAGE_BASE() -> IntType: ...
    
    @staticmethod
    @property
    def PERF_AVERAGE_BULK() -> IntType: ...
    
    @staticmethod
    @property
    def PERF_AVERAGE_TIMER() -> IntType: ...
    
    @staticmethod
    @property
    def PERF_COUNTER_100NS_QUEUELEN_TYPE() -> IntType: ...
    
    @staticmethod
    @property
    def PERF_COUNTER_BASE() -> IntType: ...
    
    @staticmethod
    @property
    def PERF_COUNTER_BULK_COUNT() -> IntType: ...
    
    @staticmethod
    @property
    def PERF_COUNTER_COUNTER() -> IntType: ...
    
    @staticmethod
    @property
    def PERF_COUNTER_DELTA() -> IntType: ...
    
    @staticmethod
    @property
    def PERF_COUNTER_ELAPSED() -> IntType: ...
    
    @staticmethod
    @property
    def PERF_COUNTER_FRACTION() -> IntType: ...
    
    @staticmethod
    @property
    def PERF_COUNTER_HISTOGRAM() -> IntType: ...
    
    @staticmethod
    @property
    def PERF_COUNTER_LARGE_DELTA() -> IntType: ...
    
    @staticmethod
    @property
    def PERF_COUNTER_LARGE_QUEUELEN_TYPE() -> IntType: ...
    
    @staticmethod
    @property
    def PERF_COUNTER_LARGE_RAWCOUNT() -> IntType: ...
    
    @staticmethod
    @property
    def PERF_COUNTER_LARGE_RAWCOUNT_HEX() -> IntType: ...
    
    @staticmethod
    @property
    def PERF_COUNTER_MULTI_BASE() -> IntType: ...
    
    @staticmethod
    @property
    def PERF_COUNTER_MULTI_TIMER() -> IntType: ...
    
    @staticmethod
    @property
    def PERF_COUNTER_MULTI_TIMER_INV() -> IntType: ...
    
    @staticmethod
    @property
    def PERF_COUNTER_NODATA() -> IntType: ...
    
    @staticmethod
    @property
    def PERF_COUNTER_OBJ_TIME_QUEUELEN_TYPE() -> IntType: ...
    
    @staticmethod
    @property
    def PERF_COUNTER_PRECISION() -> IntType: ...
    
    @staticmethod
    @property
    def PERF_COUNTER_QUEUELEN() -> IntType: ...
    
    @staticmethod
    @property
    def PERF_COUNTER_QUEUELEN_TYPE() -> IntType: ...
    
    @staticmethod
    @property
    def PERF_COUNTER_RATE() -> IntType: ...
    
    @staticmethod
    @property
    def PERF_COUNTER_RAWCOUNT() -> IntType: ...
    
    @staticmethod
    @property
    def PERF_COUNTER_RAWCOUNT_HEX() -> IntType: ...
    
    @staticmethod
    @property
    def PERF_COUNTER_TEXT() -> IntType: ...
    
    @staticmethod
    @property
    def PERF_COUNTER_TIMER() -> IntType: ...
    
    @staticmethod
    @property
    def PERF_COUNTER_TIMER_INV() -> IntType: ...
    
    @staticmethod
    @property
    def PERF_COUNTER_VALUE() -> IntType: ...
    
    @staticmethod
    @property
    def PERF_DELTA_BASE() -> IntType: ...
    
    @staticmethod
    @property
    def PERF_DELTA_COUNTER() -> IntType: ...
    
    @staticmethod
    @property
    def PERF_DETAIL_ADVANCED() -> IntType: ...
    
    @staticmethod
    @property
    def PERF_DETAIL_EXPERT() -> IntType: ...
    
    @staticmethod
    @property
    def PERF_DETAIL_NOVICE() -> IntType: ...
    
    @staticmethod
    @property
    def PERF_DETAIL_WIZARD() -> IntType: ...
    
    @staticmethod
    @property
    def PERF_DISPLAY_NOSHOW() -> IntType: ...
    
    @staticmethod
    @property
    def PERF_DISPLAY_NO_SUFFIX() -> IntType: ...
    
    @staticmethod
    @property
    def PERF_DISPLAY_PERCENT() -> IntType: ...
    
    @staticmethod
    @property
    def PERF_DISPLAY_PER_SEC() -> IntType: ...
    
    @staticmethod
    @property
    def PERF_DISPLAY_SECONDS() -> IntType: ...
    
    @staticmethod
    @property
    def PERF_ELAPSED_TIME() -> IntType: ...
    
    @staticmethod
    @property
    def PERF_INVERSE_COUNTER() -> IntType: ...
    
    @staticmethod
    @property
    def PERF_LARGE_RAW_BASE() -> IntType: ...
    
    @staticmethod
    @property
    def PERF_LARGE_RAW_FRACTION() -> IntType: ...
    
    @staticmethod
    @property
    def PERF_MULTI_COUNTER() -> IntType: ...
    
    @staticmethod
    @property
    def PERF_NO_INSTANCES() -> IntType: ...
    
    @staticmethod
    @property
    def PERF_NO_UNIQUE_ID() -> IntType: ...
    
    @staticmethod
    @property
    def PERF_NUMBER_DECIMAL() -> IntType: ...
    
    @staticmethod
    @property
    def PERF_NUMBER_DEC_1000() -> IntType: ...
    
    @staticmethod
    @property
    def PERF_NUMBER_HEX() -> IntType: ...
    
    @staticmethod
    @property
    def PERF_OBJECT_TIMER() -> IntType: ...
    
    @staticmethod
    @property
    def PERF_OBJ_TIME_TIME() -> IntType: ...
    
    @staticmethod
    @property
    def PERF_OBJ_TIME_TIMER() -> IntType: ...
    
    @staticmethod
    @property
    def PERF_PRECISION_100NS_TIMER() -> IntType: ...
    
    @staticmethod
    @property
    def PERF_PRECISION_OBJECT_TIMER() -> IntType: ...
    
    @staticmethod
    @property
    def PERF_PRECISION_SYSTEM_TIMER() -> IntType: ...
    
    @staticmethod
    @property
    def PERF_RAW_BASE() -> IntType: ...
    
    @staticmethod
    @property
    def PERF_RAW_FRACTION() -> IntType: ...
    
    @staticmethod
    @property
    def PERF_SAMPLE_BASE() -> IntType: ...
    
    @staticmethod
    @property
    def PERF_SAMPLE_COUNTER() -> IntType: ...
    
    @staticmethod
    @property
    def PERF_SAMPLE_FRACTION() -> IntType: ...
    
    @staticmethod
    @property
    def PERF_SIZE_DWORD() -> IntType: ...
    
    @staticmethod
    @property
    def PERF_SIZE_LARGE() -> IntType: ...
    
    @staticmethod
    @property
    def PERF_SIZE_VARIABLE_LEN() -> IntType: ...
    
    @staticmethod
    @property
    def PERF_SIZE_ZERO() -> IntType: ...
    
    @staticmethod
    @property
    def PERF_TEXT_ASCII() -> IntType: ...
    
    @staticmethod
    @property
    def PERF_TEXT_UNICODE() -> IntType: ...
    
    @staticmethod
    @property
    def PERF_TIMER_100NS() -> IntType: ...
    
    @staticmethod
    @property
    def PERF_TIMER_TICK() -> IntType: ...
    
    @staticmethod
    @property
    def PERF_TYPE_COUNTER() -> IntType: ...
    
    @staticmethod
    @property
    def PERF_TYPE_NUMBER() -> IntType: ...
    
    @staticmethod
    @property
    def PERF_TYPE_TEXT() -> IntType: ...
    
    @staticmethod
    @property
    def PERF_TYPE_ZERO() -> IntType: ...
    
    @staticmethod
    @property
    def PIPE_ACCESS_DUPLEX() -> IntType: ...
    
    @staticmethod
    @property
    def PIPE_ACCESS_INBOUND() -> IntType: ...
    
    @staticmethod
    @property
    def PIPE_ACCESS_OUTBOUND() -> IntType: ...
    
    @staticmethod
    @property
    def PIPE_NOWAIT() -> IntType: ...
    
    @staticmethod
    @property
    def PIPE_READMODE_BYTE() -> IntType: ...
    
    @staticmethod
    @property
    def PIPE_READMODE_MESSAGE() -> IntType: ...
    
    @staticmethod
    @property
    def PIPE_SINGLE_INSTANCES() -> IntType: ...
    
    @staticmethod
    @property
    def PIPE_TYPE_BYTE() -> IntType: ...
    
    @staticmethod
    @property
    def PIPE_TYPE_MESSAGE() -> IntType: ...
    
    @staticmethod
    @property
    def PIPE_UNLIMITED_INSTANCES() -> IntType: ...
    
    @staticmethod
    @property
    def PIPE_WAIT() -> IntType: ...
    
    @staticmethod
    @property
    def PM_REMOVE() -> IntType: ...
    
    @staticmethod
    @property
    def PROCESS_ALL_ACCESS() -> IntType: ...
    
    @staticmethod
    @property
    def PROCESS_CREATE_PROCESS() -> IntType: ...
    
    @staticmethod
    @property
    def PROCESS_CREATE_THREAD() -> IntType: ...
    
    @staticmethod
    @property
    def PROCESS_DUP_HANDLE() -> IntType: ...
    
    @staticmethod
    @property
    def PROCESS_QUERY_INFORMATION() -> IntType: ...
    
    @staticmethod
    @property
    def PROCESS_QUERY_LIMITED_INFORMATION() -> IntType: ...
    
    @staticmethod
    @property
    def PROCESS_SET_INFORMATION() -> IntType: ...
    
    @staticmethod
    @property
    def PROCESS_SET_QUOTA() -> IntType: ...
    
    @staticmethod
    @property
    def PROCESS_SET_SESSIONID() -> IntType: ...
    
    @staticmethod
    @property
    def PROCESS_TERMINATE() -> IntType: ...
    
    @staticmethod
    @property
    def PROCESS_VM_OPERATION() -> IntType: ...
    
    @staticmethod
    @property
    def PROCESS_VM_READ() -> IntType: ...
    
    @staticmethod
    @property
    def PROCESS_VM_WRITE() -> IntType: ...
    
    @staticmethod
    @property
    def QS_ALLEVENTS() -> IntType: ...
    
    @staticmethod
    @property
    def QS_ALLINPUT() -> IntType: ...
    
    @staticmethod
    @property
    def QS_ALLPOSTMESSAGE() -> IntType: ...
    
    @staticmethod
    @property
    def QS_HOTKEY() -> IntType: ...
    
    @staticmethod
    @property
    def QS_INPUT() -> IntType: ...
    
    @staticmethod
    @property
    def QS_KEY() -> IntType: ...
    
    @staticmethod
    @property
    def QS_MOUSE() -> IntType: ...
    
    @staticmethod
    @property
    def QS_MOUSEBUTTON() -> IntType: ...
    
    @staticmethod
    @property
    def QS_MOUSEMOVE() -> IntType: ...
    
    @staticmethod
    @property
    def QS_PAINT() -> IntType: ...
    
    @staticmethod
    @property
    def QS_POSTMESSAGE() -> IntType: ...
    
    @staticmethod
    @property
    def QS_SENDMESSAGE() -> IntType: ...
    
    @staticmethod
    @property
    def QS_TIMER() -> IntType: ...
    
    @staticmethod
    @property
    def READ_CONTROL() -> IntType: ...
    
    @staticmethod
    @property
    def REG_BINARY() -> IntType: ...
    
    @staticmethod
    @property
    def REG_MULTI_SZ() -> IntType: ...
    
    @staticmethod
    @property
    def RPC_S_CALL_FAILED() -> IntType: ...
    
    @staticmethod
    @property
    def RPC_S_SERVER_UNAVAILABLE() -> IntType: ...
    
    @staticmethod
    @property
    def SECURITY_DESCRIPTOR_REVISION() -> IntType: ...
    
    @staticmethod
    @property
    def SEEK_READ() -> IntType: ...
    
    @staticmethod
    @property
    def SEE_MASK_ASYNCOK() -> IntType: ...
    
    @staticmethod
    @property
    def SEE_MASK_CLASSKEY() -> IntType: ...
    
    @staticmethod
    @property
    def SEE_MASK_CLASSNAME() -> IntType: ...
    
    @staticmethod
    @property
    def SEE_MASK_CONNECTNETDRV() -> IntType: ...
    
    @staticmethod
    @property
    def SEE_MASK_DOENVSUBST() -> IntType: ...
    
    @staticmethod
    @property
    def SEE_MASK_FLAG_DDEWAIT() -> IntType: ...
    
    @staticmethod
    @property
    def SEE_MASK_FLAG_NO_UI() -> IntType: ...
    
    @staticmethod
    @property
    def SEE_MASK_HOTKEY() -> IntType: ...
    
    @staticmethod
    @property
    def SEE_MASK_ICON() -> IntType: ...
    
    @staticmethod
    @property
    def SEE_MASK_IDLIST() -> IntType: ...
    
    @staticmethod
    @property
    def SEE_MASK_INVOKEIDLIST() -> IntType: ...
    
    @staticmethod
    @property
    def SEE_MASK_NOCLOSEPROCESS() -> IntType: ...
    
    @staticmethod
    @property
    def SEE_MASK_NO_CONSOLE() -> IntType: ...
    
    @staticmethod
    @property
    def SEE_MASK_UNICODE() -> IntType: ...
    
    @staticmethod
    @property
    def SE_ERR_ACCESSDENIED() -> IntType: ...
    
    @staticmethod
    @property
    def SE_ERR_ASSOCINCOMPLETE() -> IntType: ...
    
    @staticmethod
    @property
    def SE_ERR_DDEBUSY() -> IntType: ...
    
    @staticmethod
    @property
    def SE_ERR_DDEFAIL() -> IntType: ...
    
    @staticmethod
    @property
    def SE_ERR_DDETIMEOUT() -> IntType: ...
    
    @staticmethod
    @property
    def SE_ERR_DLLNOTFOUND() -> IntType: ...
    
    @staticmethod
    @property
    def SE_ERR_FNF() -> IntType: ...
    
    @staticmethod
    @property
    def SE_ERR_NOASSOC() -> IntType: ...
    
    @staticmethod
    @property
    def SE_ERR_OOM() -> IntType: ...
    
    @staticmethod
    @property
    def SE_ERR_PNF() -> IntType: ...
    
    @staticmethod
    @property
    def SE_ERR_SHARE() -> IntType: ...
    
    @staticmethod
    @property
    def SE_PRIVILEGE_ENABLED() -> IntType: ...
    
    @staticmethod
    @property
    def SHGFI_TYPENAME() -> IntType: ...
    
    @staticmethod
    @property
    def SHGFI_USEFILEATTRIBUTES() -> IntType: ...
    
    @staticmethod
    @property
    def SMTO_ABORTIFHUNG() -> IntType: ...
    
    @staticmethod
    @property
    def SM_CYSCREEN() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_GETACCESSTIMEOUT() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_GETACTIVEWINDOWTRACKING() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_GETACTIVEWNDTRKTIMEOUT() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_GETACTIVEWNDTRKZORDER() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_GETANIMATION() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_GETBEEP() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_GETBORDER() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_GETCARETWIDTH() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_GETCOMBOBOXANIMATION() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_GETCURSORSHADOW() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_GETDEFAULTINPUTLANG() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_GETDESKWALLPAPER() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_GETDRAGFULLWINDOWS() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_GETFASTTASKSWITCH() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_GETFILTERKEYS() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_GETFONTSMOOTHING() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_GETFOREGROUNDFLASHCOUNT() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_GETFOREGROUNDLOCKTIMEOUT() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_GETGRADIENTCAPTIONS() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_GETGRIDGRANULARITY() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_GETHIGHCONTRAST() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_GETHOTTRACKING() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_GETICONMETRICS() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_GETICONTITLELOGFONT() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_GETICONTITLEWRAP() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_GETKEYBOARDCUES() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_GETKEYBOARDDELAY() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_GETKEYBOARDPREF() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_GETKEYBOARDSPEED() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_GETLISTBOXSMOOTHSCROLLING() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_GETLOWPOWERACTIVE() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_GETLOWPOWERTIMEOUT() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_GETMENUANIMATION() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_GETMENUDROPALIGNMENT() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_GETMENUFADE() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_GETMENUSHOWDELAY() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_GETMENUUNDERLINES() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_GETMINIMIZEDMETRICS() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_GETMOUSE() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_GETMOUSEHOVERHEIGHT() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_GETMOUSEHOVERTIME() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_GETMOUSEHOVERWIDTH() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_GETMOUSEKEYS() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_GETMOUSESPEED() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_GETMOUSETRAILS() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_GETNONCLIENTMETRICS() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_GETPOWEROFFACTIVE() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_GETPOWEROFFTIMEOUT() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_GETSCREENREADER() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_GETSCREENSAVEACTIVE() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_GETSCREENSAVERRUNNING() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_GETSCREENSAVETIMEOUT() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_GETSELECTIONFADE() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_GETSERIALKEYS() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_GETSHOWIMEUI() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_GETSHOWSOUNDS() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_GETSNAPTODEFBUTTON() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_GETSOUNDSENTRY() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_GETSTICKYKEYS() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_GETTOGGLEKEYS() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_GETTOOLTIPANIMATION() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_GETTOOLTIPFADE() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_GETUIEFFECTS() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_GETWHEELSCROLLLINES() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_GETWINDOWSEXTENSION() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_GETWORKAREA() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_ICONHORIZONTALSPACING() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_ICONVERTICALSPACING() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_LANGDRIVER() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_SCREENSAVERRUNNING() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_SETACCESSTIMEOUT() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_SETACTIVEWINDOWTRACKING() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_SETACTIVEWNDTRKTIMEOUT() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_SETACTIVEWNDTRKZORDER() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_SETANIMATION() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_SETBEEP() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_SETBORDER() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_SETCARETWIDTH() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_SETCOMBOBOXANIMATION() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_SETCURSORS() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_SETCURSORSHADOW() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_SETDEFAULTINPUTLANG() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_SETDESKPATTERN() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_SETDESKWALLPAPER() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_SETDOUBLECLICKTIME() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_SETDOUBLECLKHEIGHT() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_SETDOUBLECLKWIDTH() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_SETDRAGFULLWINDOWS() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_SETDRAGHEIGHT() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_SETDRAGWIDTH() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_SETFASTTASKSWITCH() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_SETFILTERKEYS() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_SETFONTSMOOTHING() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_SETFOREGROUNDFLASHCOUNT() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_SETFOREGROUNDLOCKTIMEOUT() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_SETGRADIENTCAPTIONS() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_SETGRIDGRANULARITY() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_SETHANDHELD() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_SETHIGHCONTRAST() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_SETHOTTRACKING() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_SETICONMETRICS() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_SETICONS() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_SETICONTITLELOGFONT() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_SETICONTITLEWRAP() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_SETKEYBOARDCUES() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_SETKEYBOARDDELAY() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_SETKEYBOARDPREF() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_SETKEYBOARDSPEED() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_SETLANGTOGGLE() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_SETLISTBOXSMOOTHSCROLLING() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_SETLOWPOWERACTIVE() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_SETLOWPOWERTIMEOUT() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_SETMENUANIMATION() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_SETMENUDROPALIGNMENT() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_SETMENUFADE() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_SETMENUSHOWDELAY() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_SETMENUUNDERLINES() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_SETMINIMIZEDMETRICS() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_SETMOUSE() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_SETMOUSEBUTTONSWAP() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_SETMOUSEHOVERHEIGHT() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_SETMOUSEHOVERTIME() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_SETMOUSEHOVERWIDTH() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_SETMOUSEKEYS() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_SETMOUSESPEED() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_SETMOUSETRAILS() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_SETNONCLIENTMETRICS() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_SETPENWINDOWS() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_SETPOWEROFFACTIVE() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_SETPOWEROFFTIMEOUT() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_SETSCREENREADER() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_SETSCREENSAVEACTIVE() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_SETSCREENSAVERRUNNING() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_SETSCREENSAVETIMEOUT() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_SETSELECTIONFADE() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_SETSERIALKEYS() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_SETSHOWIMEUI() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_SETSHOWSOUNDS() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_SETSNAPTODEFBUTTON() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_SETSOUNDSENTRY() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_SETSTICKYKEYS() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_SETTOGGLEKEYS() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_SETTOOLTIPANIMATION() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_SETTOOLTIPFADE() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_SETUIEFFECTS() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_SETWHEELSCROLLLINES() -> IntType: ...
    
    @staticmethod
    @property
    def SPI_SETWORKAREA() -> IntType: ...
    
    @staticmethod
    @property
    def STANDARD_RIGHTS_READ() -> IntType: ...
    
    @staticmethod
    @property
    def STANDARD_RIGHTS_REQUIRED() -> IntType: ...
    
    @staticmethod
    @property
    def STARTF_USESHOWWINDOW() -> IntType: ...
    
    @staticmethod
    @property
    def STARTF_USESTDHANDLES() -> IntType: ...
    
    @staticmethod
    @property
    def STATUS_INFO_LENGTH_MISMATCH() -> UIntType: ...
    
    @staticmethod
    @property
    def STD_ERROR_HANDLE() -> IntType: ...
    
    @staticmethod
    @property
    def STD_INPUT_HANDLE() -> IntType: ...
    
    @staticmethod
    @property
    def STD_OUTPUT_HANDLE() -> IntType: ...
    
    @staticmethod
    @property
    def STILL_ACTIVE() -> IntType: ...
    
    @staticmethod
    @property
    def SW_HIDE() -> IntType: ...
    
    @staticmethod
    @property
    def SW_MAX() -> IntType: ...
    
    @staticmethod
    @property
    def SW_MAXIMIZE() -> IntType: ...
    
    @staticmethod
    @property
    def SW_MINIMIZE() -> IntType: ...
    
    @staticmethod
    @property
    def SW_NORMAL() -> IntType: ...
    
    @staticmethod
    @property
    def SW_RESTORE() -> IntType: ...
    
    @staticmethod
    @property
    def SW_SHOW() -> IntType: ...
    
    @staticmethod
    @property
    def SW_SHOWDEFAULT() -> IntType: ...
    
    @staticmethod
    @property
    def SW_SHOWMAXIMIZED() -> IntType: ...
    
    @staticmethod
    @property
    def SW_SHOWMINIMIZED() -> IntType: ...
    
    @staticmethod
    @property
    def SW_SHOWMINNOACTIVE() -> IntType: ...
    
    @staticmethod
    @property
    def SW_SHOWNA() -> IntType: ...
    
    @staticmethod
    @property
    def SW_SHOWNOACTIVATE() -> IntType: ...
    
    @staticmethod
    @property
    def SW_SHOWNORMAL() -> IntType: ...
    
    @staticmethod
    @property
    def SYNCHRONIZE() -> IntType: ...
    
    @staticmethod
    @property
    def S_OK() -> IntType: ...
    
    @staticmethod
    @property
    def TH32CS_INHERIT() -> IntType: ...
    
    @staticmethod
    @property
    def TH32CS_SNAPHEAPLIST() -> IntType: ...
    
    @staticmethod
    @property
    def TH32CS_SNAPMODULE() -> IntType: ...
    
    @staticmethod
    @property
    def TH32CS_SNAPPROCESS() -> IntType: ...
    
    @staticmethod
    @property
    def TH32CS_SNAPTHREAD() -> IntType: ...
    
    @staticmethod
    @property
    def THREAD_DIRECT_IMPERSONATION() -> IntType: ...
    
    @staticmethod
    @property
    def THREAD_GET_CONTEXT() -> IntType: ...
    
    @staticmethod
    @property
    def THREAD_IMPERSONATE() -> IntType: ...
    
    @staticmethod
    @property
    def THREAD_QUERY_INFORMATION() -> IntType: ...
    
    @staticmethod
    @property
    def THREAD_SET_CONTEXT() -> IntType: ...
    
    @staticmethod
    @property
    def THREAD_SET_INFORMATION() -> IntType: ...
    
    @staticmethod
    @property
    def THREAD_SET_THREAD_TOKEN() -> IntType: ...
    
    @staticmethod
    @property
    def THREAD_SUSPEND_RESUME() -> IntType: ...
    
    @staticmethod
    @property
    def THREAD_TERMINATE() -> IntType: ...
    
    @staticmethod
    @property
    def TOKEN_ADJUST_PRIVILEGES() -> IntType: ...
    
    @staticmethod
    @property
    def TOKEN_ALL_ACCESS() -> IntType: ...
    
    @staticmethod
    @property
    def TOKEN_EXECUTE() -> IntType: ...
    
    @staticmethod
    @property
    def TOKEN_IMPERSONATE() -> IntType: ...
    
    @staticmethod
    @property
    def TOKEN_QUERY() -> IntType: ...
    
    @staticmethod
    @property
    def TOKEN_READ() -> IntType: ...
    
    @staticmethod
    @property
    def TOKEN_TYPE_TokenImpersonation() -> IntType: ...
    
    @staticmethod
    @property
    def TOKEN_TYPE_TokenPrimary() -> IntType: ...
    
    @staticmethod
    @property
    def UISF_HIDEACCEL() -> IntType: ...
    
    @staticmethod
    @property
    def UISF_HIDEFOCUS() -> IntType: ...
    
    @staticmethod
    @property
    def UIS_CLEAR() -> IntType: ...
    
    @staticmethod
    @property
    def UIS_SET() -> IntType: ...
    
    @staticmethod
    @property
    def UOI_FLAGS() -> IntType: ...
    
    @staticmethod
    @property
    def UOI_NAME() -> IntType: ...
    
    @staticmethod
    @property
    def UOI_TYPE() -> IntType: ...
    
    @staticmethod
    @property
    def UOI_USER_SID() -> IntType: ...
    
    @staticmethod
    @property
    def USERCLASSTYPE_FULL() -> IntType: ...
    
    @staticmethod
    @property
    def VER_PLATFORM_WIN32_NT() -> IntType: ...
    
    @staticmethod
    @property
    def VFT2_DRV_COMM() -> IntType: ...
    
    @staticmethod
    @property
    def VFT2_DRV_DISPLAY() -> IntType: ...
    
    @staticmethod
    @property
    def VFT2_DRV_INPUTMETHOD() -> IntType: ...
    
    @staticmethod
    @property
    def VFT2_DRV_INSTALLABLE() -> IntType: ...
    
    @staticmethod
    @property
    def VFT2_DRV_KEYBOARD() -> IntType: ...
    
    @staticmethod
    @property
    def VFT2_DRV_LANGUAGE() -> IntType: ...
    
    @staticmethod
    @property
    def VFT2_DRV_MOUSE() -> IntType: ...
    
    @staticmethod
    @property
    def VFT2_DRV_NETWORK() -> IntType: ...
    
    @staticmethod
    @property
    def VFT2_DRV_PRINTER() -> IntType: ...
    
    @staticmethod
    @property
    def VFT2_DRV_SOUND() -> IntType: ...
    
    @staticmethod
    @property
    def VFT2_DRV_SYSTEM() -> IntType: ...
    
    @staticmethod
    @property
    def VFT2_FONT_RASTER() -> IntType: ...
    
    @staticmethod
    @property
    def VFT2_FONT_TRUETYPE() -> IntType: ...
    
    @staticmethod
    @property
    def VFT2_FONT_VECTOR() -> IntType: ...
    
    @staticmethod
    @property
    def VFT2_UNKNOWN() -> IntType: ...
    
    @staticmethod
    @property
    def VFT_APP() -> IntType: ...
    
    @staticmethod
    @property
    def VFT_DLL() -> IntType: ...
    
    @staticmethod
    @property
    def VFT_DRV() -> IntType: ...
    
    @staticmethod
    @property
    def VFT_FONT() -> IntType: ...
    
    @staticmethod
    @property
    def VFT_STATIC_LIB() -> IntType: ...
    
    @staticmethod
    @property
    def VFT_UNKNOWN() -> IntType: ...
    
    @staticmethod
    @property
    def VFT_VXD() -> IntType: ...
    
    @staticmethod
    @property
    def VS_FFI_FILEFLAGSMASK() -> IntType: ...
    
    @staticmethod
    @property
    def VS_FFI_SIGNATURE() -> IntType: ...
    
    @staticmethod
    @property
    def VS_FFI_STRUCVERSION() -> IntType: ...
    
    @staticmethod
    @property
    def VS_FF_DEBUG() -> IntType: ...
    
    @staticmethod
    @property
    def VS_FF_INFOINFERRED() -> IntType: ...
    
    @staticmethod
    @property
    def VS_FF_PATCHED() -> IntType: ...
    
    @staticmethod
    @property
    def VS_FF_PRERELEASE() -> IntType: ...
    
    @staticmethod
    @property
    def VS_FF_PRIVATEBUILD() -> IntType: ...
    
    @staticmethod
    @property
    def VS_FF_SPECIALBUILD() -> IntType: ...
    
    @staticmethod
    @property
    def VS_FILE_INFO() -> IntType: ...
    
    @staticmethod
    @property
    def VS_USER_DEFINED() -> IntType: ...
    
    @staticmethod
    @property
    def VS_VERSION_INFO() -> IntType: ...
    
    @staticmethod
    @property
    def WAIT_ABANDONED() -> IntType: ...
    
    @staticmethod
    @property
    def WAIT_ABANDONED_0() -> IntType: ...
    
    @staticmethod
    @property
    def WAIT_FAILED() -> IntType: ...
    
    @staticmethod
    @property
    def WAIT_OBJECT_0() -> IntType: ...
    
    @staticmethod
    @property
    def WAIT_TIMEOUT() -> IntType: ...
    
    @staticmethod
    @property
    def WHITENESS() -> IntType: ...
    
    @staticmethod
    @property
    def WM_CLOSE() -> IntType: ...
    
    @staticmethod
    @property
    def WM_COMPACTING() -> IntType: ...
    
    @staticmethod
    @property
    def WM_CREATETIMER() -> IntType: ...
    
    @staticmethod
    @property
    def WM_DISPLAYCHANGE() -> IntType: ...
    
    @staticmethod
    @property
    def WM_ENDSESSION() -> IntType: ...
    
    @staticmethod
    @property
    def WM_FONTCHANGE() -> IntType: ...
    
    @staticmethod
    @property
    def WM_KILLTIMER() -> IntType: ...
    
    @staticmethod
    @property
    def WM_NULL() -> IntType: ...
    
    @staticmethod
    @property
    def WM_PALETTECHANGED() -> IntType: ...
    
    @staticmethod
    @property
    def WM_POWERBROADCAST() -> IntType: ...
    
    @staticmethod
    @property
    def WM_QUERYENDSESSION() -> IntType: ...
    
    @staticmethod
    @property
    def WM_QUIT() -> IntType: ...
    
    @staticmethod
    @property
    def WM_REFLECT() -> IntType: ...
    
    @staticmethod
    @property
    def WM_SETTINGCHANGE() -> IntType: ...
    
    @staticmethod
    @property
    def WM_SYSCOLORCHANGE() -> IntType: ...
    
    @staticmethod
    @property
    def WM_THEMECHANGED() -> IntType: ...
    
    @staticmethod
    @property
    def WM_TIMECHANGE() -> IntType: ...
    
    @staticmethod
    @property
    def WM_TIMER() -> IntType: ...
    
    @staticmethod
    @property
    def WM_USER() -> IntType: ...
    
    @staticmethod
    @property
    def WM_WTSSESSION_CHANGE() -> IntType: ...
    
    @staticmethod
    @property
    def WSF_VISIBLE() -> IntType: ...
    
    @staticmethod
    @property
    def WS_DISABLED() -> IntType: ...
    
    @staticmethod
    @property
    def WS_POPUP() -> IntType: ...
    
    @staticmethod
    @property
    def WS_VISIBLE() -> IntType: ...
    
    @staticmethod
    @property
    def WTS_CONSOLE_CONNECT() -> IntType: ...
    
    @staticmethod
    @property
    def WTS_CONSOLE_DISCONNECT() -> IntType: ...
    
    @staticmethod
    @property
    def WTS_REMOTE_CONNECT() -> IntType: ...
    
    @staticmethod
    @property
    def WTS_REMOTE_DISCONNECT() -> IntType: ...
    
    @staticmethod
    @property
    def WTS_SESSION_LOCK() -> IntType: ...
    
    @staticmethod
    @property
    def WTS_SESSION_LOGOFF() -> IntType: ...
    
    @staticmethod
    @property
    def WTS_SESSION_LOGON() -> IntType: ...
    
    @staticmethod
    @property
    def WTS_SESSION_REMOTE_CONTROL() -> IntType: ...
    
    @staticmethod
    @property
    def WTS_SESSION_UNLOCK() -> IntType: ...
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def AdjustTokenPrivileges(TokenHandle: HandleRef, DisableAllPrivileges: BooleanType, NewState: TokenPrivileges, BufferLength: IntType, PreviousState: NIntType, ReturnLength: NIntType) -> BooleanType: ...
    
    @staticmethod
    def CreateFile(lpFileName: StringType, dwDesiredAccess: IntType, dwShareMode: IntType, lpSecurityAttributes: SECURITY_ATTRIBUTES, dwCreationDisposition: IntType, dwFlagsAndAttributes: IntType, hTemplateFile: SafeFileHandle) -> SafeFileHandle: ...
    
    @staticmethod
    def CreatePipe(hReadPipe: SafeFileHandle, hWritePipe: SafeFileHandle, lpPipeAttributes: SECURITY_ATTRIBUTES, nSize: IntType) -> Tuple[BooleanType, SafeFileHandle, SafeFileHandle]: ...
    
    @staticmethod
    def CreateProcess(lpApplicationName: StringType, lpCommandLine: StringBuilder, lpProcessAttributes: SECURITY_ATTRIBUTES, lpThreadAttributes: SECURITY_ATTRIBUTES, bInheritHandles: BooleanType, dwCreationFlags: IntType, lpEnvironment: NIntType, lpCurrentDirectory: StringType, lpStartupInfo: STARTUPINFO, lpProcessInformation: PROCESS_INFORMATION) -> BooleanType: ...
    
    @staticmethod
    def CreateProcessAsUser(hToken: SafeHandle, lpApplicationName: StringType, lpCommandLine: StringType, lpProcessAttributes: SECURITY_ATTRIBUTES, lpThreadAttributes: SECURITY_ATTRIBUTES, bInheritHandles: BooleanType, dwCreationFlags: IntType, lpEnvironment: HandleRef, lpCurrentDirectory: StringType, lpStartupInfo: STARTUPINFO, lpProcessInformation: PROCESS_INFORMATION) -> BooleanType: ...
    
    @staticmethod
    def CreateToolhelp32Snapshot(flags: IntType, processId: IntType) -> NIntType: ...
    
    @staticmethod
    @overload
    def DuplicateHandle(hSourceProcessHandle: HandleRef, hSourceHandle: SafeHandle, hTargetProcess: HandleRef, targetHandle: SafeWaitHandle, dwDesiredAccess: IntType, bInheritHandle: BooleanType, dwOptions: IntType) -> Tuple[BooleanType, SafeWaitHandle]: ...
    
    @staticmethod
    @overload
    def DuplicateHandle(hSourceProcessHandle: HandleRef, hSourceHandle: SafeHandle, hTargetProcess: HandleRef, targetHandle: SafeFileHandle, dwDesiredAccess: IntType, bInheritHandle: BooleanType, dwOptions: IntType) -> Tuple[BooleanType, SafeFileHandle]: ...
    
    @staticmethod
    def EnumProcessModules(handle: SafeProcessHandle, modules: NIntType, size: IntType, needed: IntType) -> Tuple[BooleanType, IntType]: ...
    
    @staticmethod
    def EnumProcesses(processIds: ArrayType[IntType], size: IntType, needed: IntType) -> Tuple[BooleanType, IntType]: ...
    
    @staticmethod
    def EnumWindows(callback: EnumThreadWindowsCallback, extraData: NIntType) -> BooleanType: ...
    
    @staticmethod
    def GetCurrentProcess() -> NIntType: ...
    
    @staticmethod
    def GetCurrentProcessId() -> IntType: ...
    
    @staticmethod
    def GetExitCodeProcess(processHandle: SafeProcessHandle, exitCode: IntType) -> Tuple[BooleanType, IntType]: ...
    
    @staticmethod
    def GetModuleBaseName(processHandle: SafeProcessHandle, moduleHandle: HandleRef, baseName: StringBuilder, size: IntType) -> IntType: ...
    
    @staticmethod
    @overload
    def GetModuleFileNameEx(processHandle: SafeProcessHandle, moduleHandle: HandleRef, baseName: StringBuilder, size: IntType) -> IntType: ...
    
    @staticmethod
    @overload
    def GetModuleFileNameEx(processHandle: HandleRef, moduleHandle: HandleRef, baseName: StringBuilder, size: IntType) -> IntType: ...
    
    @staticmethod
    def GetModuleInformation(processHandle: SafeProcessHandle, moduleHandle: HandleRef, ntModuleInfo: NtModuleInfo, size: IntType) -> BooleanType: ...
    
    @staticmethod
    def GetPriorityClass(handle: SafeProcessHandle) -> IntType: ...
    
    @staticmethod
    def GetProcessAffinityMask(handle: SafeProcessHandle, processMask: NIntType, systemMask: NIntType) -> Tuple[BooleanType, NIntType, NIntType]: ...
    
    @staticmethod
    def GetProcessPriorityBoost(handle: SafeProcessHandle, disabled: BooleanType) -> Tuple[BooleanType, BooleanType]: ...
    
    @staticmethod
    def GetProcessTimes(handle: SafeProcessHandle, creation: LongType, exit: LongType, kernel: LongType, user: LongType) -> Tuple[BooleanType, LongType, LongType, LongType, LongType]: ...
    
    @staticmethod
    def GetProcessWorkingSetSize(handle: SafeProcessHandle, min: NIntType, max: NIntType) -> Tuple[BooleanType, NIntType, NIntType]: ...
    
    @staticmethod
    def GetStdHandle(whichHandle: IntType) -> NIntType: ...
    
    @staticmethod
    def GetThreadPriority(handle: SafeThreadHandle) -> IntType: ...
    
    @staticmethod
    def GetThreadPriorityBoost(handle: SafeThreadHandle, disabled: BooleanType) -> Tuple[BooleanType, BooleanType]: ...
    
    @staticmethod
    def GetThreadTimes(handle: SafeThreadHandle, creation: LongType, exit: LongType, kernel: LongType, user: LongType) -> Tuple[BooleanType, LongType, LongType, LongType, LongType]: ...
    
    @staticmethod
    def GetWindow(hWnd: HandleRef, uCmd: IntType) -> NIntType: ...
    
    @staticmethod
    def GetWindowLong(hWnd: HandleRef, nIndex: IntType) -> IntType: ...
    
    @staticmethod
    def GetWindowText(hWnd: HandleRef, lpString: StringBuilder, nMaxCount: IntType) -> IntType: ...
    
    @staticmethod
    def GetWindowTextLength(hWnd: HandleRef) -> IntType: ...
    
    @staticmethod
    def GetWindowThreadProcessId(handle: HandleRef, processId: IntType) -> Tuple[IntType, IntType]: ...
    
    @staticmethod
    def IsWindowVisible(hWnd: HandleRef) -> BooleanType: ...
    
    @staticmethod
    def LookupPrivilegeValue(lpSystemName: StringType, lpName: StringType, lpLuid: LUID) -> Tuple[BooleanType, LUID]: ...
    
    @staticmethod
    def Module32First(handle: HandleRef, entry: NIntType) -> BooleanType: ...
    
    @staticmethod
    def Module32Next(handle: HandleRef, entry: NIntType) -> BooleanType: ...
    
    @staticmethod
    def NtQueryInformationProcess(processHandle: SafeProcessHandle, query: IntType, info: NtProcessBasicInfo, size: IntType, returnedSize: ArrayType[IntType]) -> IntType: ...
    
    @staticmethod
    def NtQuerySystemInformation(query: IntType, dataPtr: NIntType, size: IntType, returnedSize: IntType) -> Tuple[IntType, IntType]: ...
    
    @staticmethod
    def OpenProcess(access: IntType, inherit: BooleanType, processId: IntType) -> SafeProcessHandle: ...
    
    @staticmethod
    def OpenProcessToken(ProcessHandle: HandleRef, DesiredAccess: IntType, TokenHandle: NIntType) -> Tuple[BooleanType, NIntType]: ...
    
    @staticmethod
    def OpenThread(access: IntType, inherit: BooleanType, threadId: IntType) -> SafeThreadHandle: ...
    
    @staticmethod
    def PostMessage(hwnd: HandleRef, msg: IntType, wparam: NIntType, lparam: NIntType) -> IntType: ...
    
    @staticmethod
    def Process32First(handle: HandleRef, entry: NIntType) -> BooleanType: ...
    
    @staticmethod
    def Process32Next(handle: HandleRef, entry: NIntType) -> BooleanType: ...
    
    @staticmethod
    def RtlGetVersion(lpVersionInformation: RTL_OSVERSIONINFOEX) -> Tuple[IntType, RTL_OSVERSIONINFOEX]: ...
    
    @staticmethod
    def SendMessageTimeout(hWnd: HandleRef, msg: IntType, wParam: NIntType, lParam: NIntType, flags: IntType, timeout: IntType, pdwResult: NIntType) -> Tuple[NIntType, NIntType]: ...
    
    @staticmethod
    def SetPriorityClass(handle: SafeProcessHandle, priorityClass: IntType) -> BooleanType: ...
    
    @staticmethod
    def SetProcessAffinityMask(handle: SafeProcessHandle, mask: NIntType) -> BooleanType: ...
    
    @staticmethod
    def SetProcessPriorityBoost(handle: SafeProcessHandle, disabled: BooleanType) -> BooleanType: ...
    
    @staticmethod
    def SetProcessWorkingSetSize(handle: SafeProcessHandle, min: NIntType, max: NIntType) -> BooleanType: ...
    
    @staticmethod
    def SetThreadAffinityMask(handle: SafeThreadHandle, mask: HandleRef) -> NIntType: ...
    
    @staticmethod
    def SetThreadIdealProcessor(handle: SafeThreadHandle, processor: IntType) -> IntType: ...
    
    @staticmethod
    def SetThreadPriority(handle: SafeThreadHandle, priority: IntType) -> BooleanType: ...
    
    @staticmethod
    def SetThreadPriorityBoost(handle: SafeThreadHandle, disabled: BooleanType) -> BooleanType: ...
    
    @staticmethod
    def ShellExecuteEx(info: ShellExecuteInfo) -> BooleanType: ...
    
    @staticmethod
    def TerminateProcess(processHandle: SafeProcessHandle, exitCode: IntType) -> BooleanType: ...
    
    @staticmethod
    def Thread32First(handle: HandleRef, entry: WinThreadEntry) -> BooleanType: ...
    
    @staticmethod
    def Thread32Next(handle: HandleRef, entry: WinThreadEntry) -> BooleanType: ...
    
    @staticmethod
    def WaitForInputIdle(handle: SafeProcessHandle, milliseconds: IntType) -> IntType: ...
    
    # No Events
    
    
    # ---------- Sub Classes ---------- #
    
    class WndProc(MulticastDelegate, ICloneable, ISerializable):
        # No Fields
        
        # ---------- Constructors ---------- #
        
        def __init__(self, object: ObjectType, method: NIntType): ...
        
        # No Properties
        
        # ---------- Methods ---------- #
        
        def BeginInvoke(self, hWnd: NIntType, msg: IntType, wParam: NIntType, lParam: NIntType, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
        
        def EndInvoke(self, result: IAsyncResult) -> NIntType: ...
        
        def Invoke(self, hWnd: NIntType, msg: IntType, wParam: NIntType, lParam: NIntType) -> NIntType: ...
        
        # No Events
        
        # No Sub Classes
        
        # No Sub Structs
        
        # No Sub Interfaces
        
        # No Sub Enums
    
    
    class ConHndlr(MulticastDelegate, ICloneable, ISerializable):
        # No Fields
        
        # ---------- Constructors ---------- #
        
        def __init__(self, object: ObjectType, method: NIntType): ...
        
        # No Properties
        
        # ---------- Methods ---------- #
        
        def BeginInvoke(self, signalType: IntType, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
        
        def EndInvoke(self, result: IAsyncResult) -> IntType: ...
        
        def Invoke(self, signalType: IntType) -> IntType: ...
        
        # No Events
        
        # No Sub Classes
        
        # No Sub Structs
        
        # No Sub Interfaces
        
        # No Sub Enums
    
    
    class PDH_RAW_COUNTER(ObjectType):
        # ---------- Fields ---------- #
        
        @property
        def CStatus(self) -> IntType: ...
        
        @CStatus.setter
        def CStatus(self, value: IntType) -> None: ...
        
        @property
        def FirstValue(self) -> LongType: ...
        
        @FirstValue.setter
        def FirstValue(self, value: LongType) -> None: ...
        
        @property
        def MultiCount(self) -> IntType: ...
        
        @MultiCount.setter
        def MultiCount(self, value: IntType) -> None: ...
        
        @property
        def SecondValue(self) -> LongType: ...
        
        @SecondValue.setter
        def SecondValue(self, value: LongType) -> None: ...
        
        @property
        def TimeStamp(self) -> LongType: ...
        
        @TimeStamp.setter
        def TimeStamp(self, value: LongType) -> None: ...
        
        # ---------- Constructors ---------- #
        
        def __init__(self): ...
        
        # No Properties
        
        # No Methods
        
        # No Events
        
        # No Sub Classes
        
        # No Sub Structs
        
        # No Sub Interfaces
        
        # No Sub Enums
    
    
    class PDH_FMT_COUNTERVALUE(ObjectType):
        # ---------- Fields ---------- #
        
        @property
        def CStatus(self) -> IntType: ...
        
        @CStatus.setter
        def CStatus(self, value: IntType) -> None: ...
        
        @property
        def data(self) -> DoubleType: ...
        
        @data.setter
        def data(self, value: DoubleType) -> None: ...
        
        # ---------- Constructors ---------- #
        
        def __init__(self): ...
        
        # No Properties
        
        # No Methods
        
        # No Events
        
        # No Sub Classes
        
        # No Sub Structs
        
        # No Sub Interfaces
        
        # No Sub Enums
    
    
    # ---------- Sub Structs ---------- #
    
    class MSG(ValueType):
        # ---------- Fields ---------- #
        
        @property
        def hwnd(self) -> NIntType: ...
        
        @hwnd.setter
        def hwnd(self, value: NIntType) -> None: ...
        
        @property
        def lParam(self) -> NIntType: ...
        
        @lParam.setter
        def lParam(self, value: NIntType) -> None: ...
        
        @property
        def message(self) -> IntType: ...
        
        @message.setter
        def message(self, value: IntType) -> None: ...
        
        @property
        def pt_x(self) -> IntType: ...
        
        @pt_x.setter
        def pt_x(self, value: IntType) -> None: ...
        
        @property
        def pt_y(self) -> IntType: ...
        
        @pt_y.setter
        def pt_y(self, value: IntType) -> None: ...
        
        @property
        def time(self) -> IntType: ...
        
        @time.setter
        def time(self, value: IntType) -> None: ...
        
        @property
        def wParam(self) -> NIntType: ...
        
        @wParam.setter
        def wParam(self, value: NIntType) -> None: ...
        
        # No Constructors
        
        # No Properties
        
        # No Methods
        
        # No Events
        
        # No Sub Classes
        
        # No Sub Structs
        
        # No Sub Interfaces
        
        # No Sub Enums
    
    
    class RTL_OSVERSIONINFOEX(ValueType):
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
    
    
    # No Sub Interfaces
    
    # ---------- Sub Enums ---------- #
    
    class StructFormatEnum(Enum):
        Ansi = 1
        Unicode = 2
        Auto = 3
    
    
    class StructFormat(Enum):
        Ansi = 1
        Unicode = 2
        Auto = 3
    


class OAVariantLib(ABC, ObjectType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def AlphaBool() -> IntType: ...
    
    @staticmethod
    @property
    def CalendarHijri() -> IntType: ...
    
    @staticmethod
    @property
    def LocalBool() -> IntType: ...
    
    @staticmethod
    @property
    def NoUserOverride() -> IntType: ...
    
    @staticmethod
    @property
    def NoValueProp() -> IntType: ...
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PowerModeChangedEventArgs(EventArgs):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, mode: PowerModes): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Mode(self) -> PowerModes: ...
    
    # ---------- Methods ---------- #
    
    def get_Mode(self) -> PowerModes: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PowerModeChangedEventHandler(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, sender: ObjectType, e: PowerModeChangedEventArgs, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, sender: ObjectType, e: PowerModeChangedEventArgs) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Registry(ABC, ObjectType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def ClassesRoot() -> RegistryKey: ...
    
    @staticmethod
    @property
    def CurrentConfig() -> RegistryKey: ...
    
    @staticmethod
    @property
    def CurrentUser() -> RegistryKey: ...
    
    @staticmethod
    @property
    def DynData() -> RegistryKey: ...
    
    @staticmethod
    @property
    def LocalMachine() -> RegistryKey: ...
    
    @staticmethod
    @property
    def PerformanceData() -> RegistryKey: ...
    
    @staticmethod
    @property
    def Users() -> RegistryKey: ...
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def GetValue(keyName: StringType, valueName: StringType, defaultValue: ObjectType) -> ObjectType: ...
    
    @staticmethod
    @overload
    def SetValue(keyName: StringType, valueName: StringType, value: ObjectType, valueKind: RegistryValueKind) -> VoidType: ...
    
    @staticmethod
    @overload
    def SetValue(keyName: StringType, valueName: StringType, value: ObjectType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RegistryKey(MarshalByRefObject, IDisposable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Handle(self) -> SafeRegistryHandle: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def SubKeyCount(self) -> IntType: ...
    
    @property
    def ValueCount(self) -> IntType: ...
    
    @property
    def View(self) -> RegistryView: ...
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    @overload
    def CreateSubKey(self, subkey: StringType) -> RegistryKey: ...
    
    @overload
    def CreateSubKey(self, subkey: StringType, permissionCheck: RegistryKeyPermissionCheck) -> RegistryKey: ...
    
    @overload
    def CreateSubKey(self, subkey: StringType, permissionCheck: RegistryKeyPermissionCheck, options: RegistryOptions) -> RegistryKey: ...
    
    @overload
    def CreateSubKey(self, subkey: StringType, writable: BooleanType) -> RegistryKey: ...
    
    @overload
    def CreateSubKey(self, subkey: StringType, writable: BooleanType, options: RegistryOptions) -> RegistryKey: ...
    
    @overload
    def CreateSubKey(self, subkey: StringType, permissionCheck: RegistryKeyPermissionCheck, registrySecurity: RegistrySecurity) -> RegistryKey: ...
    
    @overload
    def CreateSubKey(self, subkey: StringType, permissionCheck: RegistryKeyPermissionCheck, registryOptions: RegistryOptions, registrySecurity: RegistrySecurity) -> RegistryKey: ...
    
    @overload
    def DeleteSubKey(self, subkey: StringType) -> VoidType: ...
    
    @overload
    def DeleteSubKey(self, subkey: StringType, throwOnMissingSubKey: BooleanType) -> VoidType: ...
    
    @overload
    def DeleteSubKeyTree(self, subkey: StringType) -> VoidType: ...
    
    @overload
    def DeleteSubKeyTree(self, subkey: StringType, throwOnMissingSubKey: BooleanType) -> VoidType: ...
    
    @overload
    def DeleteValue(self, name: StringType) -> VoidType: ...
    
    @overload
    def DeleteValue(self, name: StringType, throwOnMissingValue: BooleanType) -> VoidType: ...
    
    def Dispose(self) -> VoidType: ...
    
    def Flush(self) -> VoidType: ...
    
    @staticmethod
    @overload
    def FromHandle(handle: SafeRegistryHandle) -> RegistryKey: ...
    
    @staticmethod
    @overload
    def FromHandle(handle: SafeRegistryHandle, view: RegistryView) -> RegistryKey: ...
    
    @overload
    def GetAccessControl(self) -> RegistrySecurity: ...
    
    @overload
    def GetAccessControl(self, includeSections: AccessControlSections) -> RegistrySecurity: ...
    
    def GetSubKeyNames(self) -> ArrayType[StringType]: ...
    
    @overload
    def GetValue(self, name: StringType) -> ObjectType: ...
    
    @overload
    def GetValue(self, name: StringType, defaultValue: ObjectType) -> ObjectType: ...
    
    @overload
    def GetValue(self, name: StringType, defaultValue: ObjectType, options: RegistryValueOptions) -> ObjectType: ...
    
    def GetValueKind(self, name: StringType) -> RegistryValueKind: ...
    
    def GetValueNames(self) -> ArrayType[StringType]: ...
    
    @staticmethod
    def OpenBaseKey(hKey: RegistryHive, view: RegistryView) -> RegistryKey: ...
    
    @staticmethod
    @overload
    def OpenRemoteBaseKey(hKey: RegistryHive, machineName: StringType) -> RegistryKey: ...
    
    @staticmethod
    @overload
    def OpenRemoteBaseKey(hKey: RegistryHive, machineName: StringType, view: RegistryView) -> RegistryKey: ...
    
    @overload
    def OpenSubKey(self, name: StringType, writable: BooleanType) -> RegistryKey: ...
    
    @overload
    def OpenSubKey(self, name: StringType, permissionCheck: RegistryKeyPermissionCheck) -> RegistryKey: ...
    
    @overload
    def OpenSubKey(self, name: StringType, rights: RegistryRights) -> RegistryKey: ...
    
    @overload
    def OpenSubKey(self, name: StringType, permissionCheck: RegistryKeyPermissionCheck, rights: RegistryRights) -> RegistryKey: ...
    
    @overload
    def OpenSubKey(self, name: StringType) -> RegistryKey: ...
    
    def SetAccessControl(self, registrySecurity: RegistrySecurity) -> VoidType: ...
    
    @overload
    def SetValue(self, name: StringType, value: ObjectType) -> VoidType: ...
    
    @overload
    def SetValue(self, name: StringType, value: ObjectType, valueKind: RegistryValueKind) -> VoidType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Handle(self) -> SafeRegistryHandle: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_SubKeyCount(self) -> IntType: ...
    
    def get_ValueCount(self) -> IntType: ...
    
    def get_View(self) -> RegistryView: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SafeCryptContextHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
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


class SafeNativeMemoryHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
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


class SafeNativeMethods(ABC, ObjectType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def ERROR_INSUFFICIENT_BUFFER() -> IntType: ...
    
    @staticmethod
    @property
    def FORMAT_MESSAGE_ALLOCATE_BUFFER() -> IntType: ...
    
    @staticmethod
    @property
    def FORMAT_MESSAGE_ARGUMENT_ARRAY() -> IntType: ...
    
    @staticmethod
    @property
    def FORMAT_MESSAGE_FROM_HMODULE() -> IntType: ...
    
    @staticmethod
    @property
    def FORMAT_MESSAGE_FROM_STRING() -> IntType: ...
    
    @staticmethod
    @property
    def FORMAT_MESSAGE_FROM_SYSTEM() -> IntType: ...
    
    @staticmethod
    @property
    def FORMAT_MESSAGE_IGNORE_INSERTS() -> IntType: ...
    
    @staticmethod
    @property
    def FORMAT_MESSAGE_MAX_WIDTH_MASK() -> IntType: ...
    
    @staticmethod
    @property
    def MB_RIGHT() -> IntType: ...
    
    @staticmethod
    @property
    def MB_RTLREADING() -> IntType: ...
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def CloseHandle(handle: NIntType) -> BooleanType: ...
    
    @staticmethod
    def FormatFromRawValue(dwCounterType: UIntType, dwFormat: UIntType, pTimeBase: LongType, pRawValue1: PDH_RAW_COUNTER, pRawValue2: PDH_RAW_COUNTER, pFmtValue: PDH_FMT_COUNTERVALUE) -> Tuple[IntType, LongType]: ...
    
    @staticmethod
    @overload
    def FormatMessage(dwFlags: IntType, lpSource_mustBeNull: NIntType, dwMessageId: UIntType, dwLanguageId: IntType, lpBuffer: StringBuilder, nSize: IntType, arguments: ArrayType[NIntType]) -> IntType: ...
    
    @staticmethod
    @overload
    def FormatMessage(dwFlags: IntType, lpSource: SafeLibraryHandle, dwMessageId: UIntType, dwLanguageId: IntType, lpBuffer: StringBuilder, nSize: IntType, arguments: ArrayType[NIntType]) -> IntType: ...
    
    @staticmethod
    def FreeLibrary(hModule: HandleRef) -> BooleanType: ...
    
    @staticmethod
    def GetComputerName(lpBuffer: StringBuilder, nSize: ArrayType[IntType]) -> BooleanType: ...
    
    @staticmethod
    def GetStockObject(nIndex: IntType) -> NIntType: ...
    
    @staticmethod
    def GetTextMetrics(hDC: NIntType, tm: TEXTMETRIC) -> Tuple[BooleanType, TEXTMETRIC]: ...
    
    @staticmethod
    def InterlockedCompareExchange(pDestination: NIntType, exchange: IntType, compare: IntType) -> IntType: ...
    
    @staticmethod
    def IsWow64Process(hProcess: SafeProcessHandle, Wow64Process: BooleanType) -> Tuple[BooleanType, BooleanType]: ...
    
    @staticmethod
    def LoadLibrary(libFilename: StringType) -> NIntType: ...
    
    @staticmethod
    def MessageBox(hWnd: NIntType, text: StringType, caption: StringType, type: IntType) -> IntType: ...
    
    @staticmethod
    def OutputDebugString(message: StringType) -> VoidType: ...
    
    @staticmethod
    def QueryPerformanceCounter(value: LongType) -> Tuple[BooleanType, LongType]: ...
    
    @staticmethod
    def QueryPerformanceFrequency(value: LongType) -> Tuple[BooleanType, LongType]: ...
    
    @staticmethod
    def RegisterWindowMessage(msg: StringType) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SessionEndedEventArgs(EventArgs):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, reason: SessionEndReasons): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Reason(self) -> SessionEndReasons: ...
    
    # ---------- Methods ---------- #
    
    def get_Reason(self) -> SessionEndReasons: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SessionEndedEventHandler(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, sender: ObjectType, e: SessionEndedEventArgs, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, sender: ObjectType, e: SessionEndedEventArgs) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SessionEndingEventArgs(EventArgs):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, reason: SessionEndReasons): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Cancel(self) -> BooleanType: ...
    
    @Cancel.setter
    def Cancel(self, value: BooleanType) -> None: ...
    
    @property
    def Reason(self) -> SessionEndReasons: ...
    
    # ---------- Methods ---------- #
    
    def get_Cancel(self) -> BooleanType: ...
    
    def get_Reason(self) -> SessionEndReasons: ...
    
    def set_Cancel(self, value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SessionEndingEventHandler(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, sender: ObjectType, e: SessionEndingEventArgs, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, sender: ObjectType, e: SessionEndingEventArgs) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SessionSwitchEventArgs(EventArgs):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, reason: SessionSwitchReason): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Reason(self) -> SessionSwitchReason: ...
    
    # ---------- Methods ---------- #
    
    def get_Reason(self) -> SessionSwitchReason: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SessionSwitchEventHandler(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, sender: ObjectType, e: SessionSwitchEventArgs, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, sender: ObjectType, e: SessionSwitchEventArgs) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SystemEvents(ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def CreateTimer(interval: IntType) -> NIntType: ...
    
    @staticmethod
    def InvokeOnEventsThread(method: Delegate) -> VoidType: ...
    
    @staticmethod
    def KillTimer(timerId: NIntType) -> VoidType: ...
    
    @staticmethod
    def add_DisplaySettingsChanged(value: EventHandler) -> VoidType: ...
    
    @staticmethod
    def add_DisplaySettingsChanging(value: EventHandler) -> VoidType: ...
    
    @staticmethod
    def add_EventsThreadShutdown(value: EventHandler) -> VoidType: ...
    
    @staticmethod
    def add_InstalledFontsChanged(value: EventHandler) -> VoidType: ...
    
    @staticmethod
    def add_LowMemory(value: EventHandler) -> VoidType: ...
    
    @staticmethod
    def add_PaletteChanged(value: EventHandler) -> VoidType: ...
    
    @staticmethod
    def add_PowerModeChanged(value: PowerModeChangedEventHandler) -> VoidType: ...
    
    @staticmethod
    def add_SessionEnded(value: SessionEndedEventHandler) -> VoidType: ...
    
    @staticmethod
    def add_SessionEnding(value: SessionEndingEventHandler) -> VoidType: ...
    
    @staticmethod
    def add_SessionSwitch(value: SessionSwitchEventHandler) -> VoidType: ...
    
    @staticmethod
    def add_TimeChanged(value: EventHandler) -> VoidType: ...
    
    @staticmethod
    def add_TimerElapsed(value: TimerElapsedEventHandler) -> VoidType: ...
    
    @staticmethod
    def add_UserPreferenceChanged(value: UserPreferenceChangedEventHandler) -> VoidType: ...
    
    @staticmethod
    def add_UserPreferenceChanging(value: UserPreferenceChangingEventHandler) -> VoidType: ...
    
    @staticmethod
    def remove_DisplaySettingsChanged(value: EventHandler) -> VoidType: ...
    
    @staticmethod
    def remove_DisplaySettingsChanging(value: EventHandler) -> VoidType: ...
    
    @staticmethod
    def remove_EventsThreadShutdown(value: EventHandler) -> VoidType: ...
    
    @staticmethod
    def remove_InstalledFontsChanged(value: EventHandler) -> VoidType: ...
    
    @staticmethod
    def remove_LowMemory(value: EventHandler) -> VoidType: ...
    
    @staticmethod
    def remove_PaletteChanged(value: EventHandler) -> VoidType: ...
    
    @staticmethod
    def remove_PowerModeChanged(value: PowerModeChangedEventHandler) -> VoidType: ...
    
    @staticmethod
    def remove_SessionEnded(value: SessionEndedEventHandler) -> VoidType: ...
    
    @staticmethod
    def remove_SessionEnding(value: SessionEndingEventHandler) -> VoidType: ...
    
    @staticmethod
    def remove_SessionSwitch(value: SessionSwitchEventHandler) -> VoidType: ...
    
    @staticmethod
    def remove_TimeChanged(value: EventHandler) -> VoidType: ...
    
    @staticmethod
    def remove_TimerElapsed(value: TimerElapsedEventHandler) -> VoidType: ...
    
    @staticmethod
    def remove_UserPreferenceChanged(value: UserPreferenceChangedEventHandler) -> VoidType: ...
    
    @staticmethod
    def remove_UserPreferenceChanging(value: UserPreferenceChangingEventHandler) -> VoidType: ...
    
    # ---------- Events ---------- #
    
    DisplaySettingsChanged: EventType[EventHandler] = ...
    
    DisplaySettingsChanging: EventType[EventHandler] = ...
    
    EventsThreadShutdown: EventType[EventHandler] = ...
    
    InstalledFontsChanged: EventType[EventHandler] = ...
    
    LowMemory: EventType[EventHandler] = ...
    
    PaletteChanged: EventType[EventHandler] = ...
    
    PowerModeChanged: EventType[PowerModeChangedEventHandler] = ...
    
    SessionEnded: EventType[SessionEndedEventHandler] = ...
    
    SessionEnding: EventType[SessionEndingEventHandler] = ...
    
    SessionSwitch: EventType[SessionSwitchEventHandler] = ...
    
    TimeChanged: EventType[EventHandler] = ...
    
    TimerElapsed: EventType[TimerElapsedEventHandler] = ...
    
    UserPreferenceChanged: EventType[UserPreferenceChangedEventHandler] = ...
    
    UserPreferenceChanging: EventType[UserPreferenceChangingEventHandler] = ...
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TimerElapsedEventArgs(EventArgs):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, timerId: NIntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def TimerId(self) -> NIntType: ...
    
    # ---------- Methods ---------- #
    
    def get_TimerId(self) -> NIntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TimerElapsedEventHandler(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, sender: ObjectType, e: TimerElapsedEventArgs, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, sender: ObjectType, e: TimerElapsedEventArgs) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UnsafeNativeMethods(ABC, ObjectType):
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


class UserPreferenceChangedEventArgs(EventArgs):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, category: UserPreferenceCategory): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Category(self) -> UserPreferenceCategory: ...
    
    # ---------- Methods ---------- #
    
    def get_Category(self) -> UserPreferenceCategory: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UserPreferenceChangedEventHandler(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, sender: ObjectType, e: UserPreferenceChangedEventArgs, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, sender: ObjectType, e: UserPreferenceChangedEventArgs) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UserPreferenceChangingEventArgs(EventArgs):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, category: UserPreferenceCategory): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Category(self) -> UserPreferenceCategory: ...
    
    # ---------- Methods ---------- #
    
    def get_Category(self) -> UserPreferenceCategory: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UserPreferenceChangingEventHandler(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, sender: ObjectType, e: UserPreferenceChangingEventArgs, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, sender: ObjectType, e: UserPreferenceChangingEventArgs) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Win32Native(ABC, ObjectType):
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


class WinInetCache(RequestCache):
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

# ---------- Interfaces ---------- #

class IApplicationContext(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Get(self, szName: StringType, pvValue: IntType, pcbValue: UIntType, dwFlags: UIntType) -> Tuple[VoidType, IntType, UIntType]: ...
    
    def GetContextNameObject(self, ppName: IAssemblyName) -> Tuple[VoidType, IAssemblyName]: ...
    
    def GetDynamicDirectory(self, wzDynamicDir: IntType, pdwSize: UIntType) -> Tuple[VoidType, IntType, UIntType]: ...
    
    def Set(self, szName: StringType, pvValue: IntType, cbValue: UIntType, dwFlags: UIntType) -> VoidType: ...
    
    def SetContextNameObject(self, pName: IAssemblyName) -> VoidType: ...
    
    # No Events


class IAssemblyEnum(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Clone(self, ppEnum: IAssemblyEnum) -> Tuple[IntType, IAssemblyEnum]: ...
    
    def GetNextAssembly(self, ppAppCtx: IApplicationContext, ppName: IAssemblyName, dwFlags: UIntType) -> Tuple[IntType, IApplicationContext, IAssemblyName]: ...
    
    def Reset(self) -> IntType: ...
    
    # No Events


class IAssemblyName(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BindToObject(self, refIID: ObjectType, pAsmBindSink: ObjectType, pApplicationContext: IApplicationContext, szCodeBase: StringType, llFlags: LongType, pvReserved: IntType, cbReserved: UIntType, ppv: IntType) -> Tuple[IntType, IntType]: ...
    
    def Clone(self, pName: IAssemblyName) -> Tuple[IntType, IAssemblyName]: ...
    
    def Finalize(self) -> IntType: ...
    
    def GetDisplayName(self, szDisplayName: NIntType, pccDisplayName: UIntType, dwDisplayFlags: UIntType) -> Tuple[IntType, UIntType]: ...
    
    def GetName(self, lpcwBuffer: UIntType, pwzName: IntType) -> Tuple[IntType, UIntType, IntType]: ...
    
    def GetProperty(self, PropertyId: UIntType, pvProperty: NIntType, pcbProperty: UIntType) -> Tuple[IntType, UIntType]: ...
    
    def GetVersion(self, pdwVersionHi: UIntType, pdwVersionLow: UIntType) -> Tuple[IntType, UIntType, UIntType]: ...
    
    def IsEqual(self, pName: IAssemblyName, dwCmpFlags: UIntType) -> IntType: ...
    
    def SetProperty(self, PropertyId: UIntType, pvProperty: NIntType, cbProperty: UIntType) -> IntType: ...
    
    # No Events


class IInternetSecurityManager(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetSecurityId(self, pwszUrl: StringType, pbSecurityId: ByteType, pcbSecurityId: IntType, dwReserved: IntType) -> VoidType: ...
    
    def GetSecuritySite(self, ppSite: VoidType) -> VoidType: ...
    
    def GetZoneMappings(self, dwZone: IntType, ppenumString: VoidType, dwFlags: IntType) -> VoidType: ...
    
    def MapUrlToZone(self, pwszUrl: StringType, pdwZone: IntType, dwFlags: IntType) -> Tuple[VoidType, IntType]: ...
    
    def ProcessUrlAction(self, pwszUrl: StringType, dwAction: IntType, pPolicy: ByteType, cbPolicy: IntType, pContext: ByteType, cbContext: IntType, dwFlags: IntType, dwReserved: IntType) -> VoidType: ...
    
    def QueryCustomPolicy(self, pwszUrl: StringType, guidKey: VoidType, ppPolicy: ByteType, pcbPolicy: IntType, pContext: ByteType, cbContext: IntType, dwReserved: IntType) -> VoidType: ...
    
    def SetSecuritySite(self, pSite: VoidType) -> VoidType: ...
    
    def SetZoneMapping(self, dwZone: IntType, lpszPattern: StringType, dwFlags: IntType) -> VoidType: ...
    
    # No Events


# ---------- Enums ---------- #

class PowerModes(Enum):
    Resume = 1
    StatusChange = 2
    Suspend = 3


class RegistryHive(Enum):
    ClassesRoot = -2147483648
    CurrentUser = -2147483647
    LocalMachine = -2147483646
    Users = -2147483645
    PerformanceData = -2147483644
    CurrentConfig = -2147483643
    DynData = -2147483642


class RegistryKeyPermissionCheck(Enum):
    Default = 0
    ReadSubTree = 1
    ReadWriteSubTree = 2


class RegistryOptions(Enum):
    #None = 0
    Volatile = 1


class RegistryValueKind(Enum):
    #None = -1
    Unknown = 0
    String = 1
    ExpandString = 2
    Binary = 3
    DWord = 4
    MultiString = 7
    QWord = 11


class RegistryValueOptions(Enum):
    #None = 0
    DoNotExpandEnvironmentNames = 1


class RegistryView(Enum):
    Default = 0
    Registry64 = 256
    Registry32 = 512


class SessionEndReasons(Enum):
    Logoff = 1
    SystemShutdown = 2


class SessionSwitchReason(Enum):
    ConsoleConnect = 1
    ConsoleDisconnect = 2
    RemoteConnect = 3
    RemoteDisconnect = 4
    SessionLogon = 5
    SessionLogoff = 6
    SessionLock = 7
    SessionUnlock = 8
    SessionRemoteControl = 9


class UserPreferenceCategory(Enum):
    Accessibility = 1
    Color = 2
    Desktop = 3
    General = 4
    Icon = 5
    Keyboard = 6
    Menu = 7
    Mouse = 8
    Policy = 9
    Power = 10
    Screensaver = 11
    Window = 12
    Locale = 13
    VisualStyle = 14


# ---------- Delegates ---------- #

PowerModeChangedEventHandler = Callable[[ObjectType, PowerModeChangedEventArgs], VoidType]

SessionEndedEventHandler = Callable[[ObjectType, SessionEndedEventArgs], VoidType]

SessionEndingEventHandler = Callable[[ObjectType, SessionEndingEventArgs], VoidType]

SessionSwitchEventHandler = Callable[[ObjectType, SessionSwitchEventArgs], VoidType]

TimerElapsedEventHandler = Callable[[ObjectType, TimerElapsedEventArgs], VoidType]

UserPreferenceChangedEventHandler = Callable[[ObjectType, UserPreferenceChangedEventArgs], VoidType]

UserPreferenceChangingEventHandler = Callable[[ObjectType, UserPreferenceChangingEventArgs], VoidType]

__all__ = [
    ASM_CACHE,
    ASM_NAME,
    CANOF,
    Fusion,
    InternetSecurityManager,
    IntranetZoneCredentialPolicy,
    NativeMethods,
    OAVariantLib,
    PowerModeChangedEventArgs,
    PowerModeChangedEventHandler,
    Registry,
    RegistryKey,
    SafeCryptContextHandle,
    SafeLibraryHandle,
    SafeNativeMemoryHandle,
    SafeNativeMethods,
    SessionEndedEventArgs,
    SessionEndedEventHandler,
    SessionEndingEventArgs,
    SessionEndingEventHandler,
    SessionSwitchEventArgs,
    SessionSwitchEventHandler,
    SystemEvents,
    TimerElapsedEventArgs,
    TimerElapsedEventHandler,
    UnsafeNativeMethods,
    UserPreferenceChangedEventArgs,
    UserPreferenceChangedEventHandler,
    UserPreferenceChangingEventArgs,
    UserPreferenceChangingEventHandler,
    Win32Native,
    WinInetCache,
    IApplicationContext,
    IAssemblyEnum,
    IAssemblyName,
    IInternetSecurityManager,
    PowerModes,
    RegistryHive,
    RegistryKeyPermissionCheck,
    RegistryOptions,
    RegistryValueKind,
    RegistryValueOptions,
    RegistryView,
    SessionEndReasons,
    SessionSwitchReason,
    UserPreferenceCategory,
    PowerModeChangedEventHandler,
    SessionEndedEventHandler,
    SessionEndingEventHandler,
    SessionSwitchEventHandler,
    TimerElapsedEventHandler,
    UserPreferenceChangedEventHandler,
    UserPreferenceChangingEventHandler,
]
