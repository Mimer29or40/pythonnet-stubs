from __future__ import annotations

from abc import ABC
from typing import List, Protocol, Tuple, Union, overload

from Microsoft.Win32.SafeHandles import SafeHandleZeroOrMinusOneIsInvalid, SafeRegistryHandle
from System import Array, Boolean, Enum, IDisposable, Int32, Int64, IntPtr, MarshalByRefObject, Object, String, UInt32, Void
from System.Collections import ArrayList
from System.Security.AccessControl import AccessControlSections, RegistryRights, RegistrySecurity

# ---------- Types ---------- #

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
IntType = Union[int, Int32]
LongType = Union[int, Int64]
NIntType = Union[int, IntPtr]
ObjectType = Object
StringType = Union[str, String]
UIntType = Union[int, UInt32]
VoidType = Union[None, Void]

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


class UnsafeNativeMethods(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def WaitNamedPipe(name: StringType, timeout: IntType) -> BooleanType: ...
    
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


class UnsafeNativeMethods(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def WaitNamedPipe(name: StringType, timeout: IntType) -> BooleanType: ...
    
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


# ---------- Enums ---------- #

class RegistryHive(Enum):
    ClassesRoot: IntType = -2147483648
    CurrentUser: IntType = -2147483647
    LocalMachine: IntType = -2147483646
    Users: IntType = -2147483645
    PerformanceData: IntType = -2147483644
    CurrentConfig: IntType = -2147483643
    DynData: IntType = -2147483642


class RegistryKeyPermissionCheck(Enum):
    Default: IntType = 0
    ReadSubTree: IntType = 1
    ReadWriteSubTree: IntType = 2


class RegistryOptions(Enum):
    #None: IntType = 0
    Volatile: IntType = 1


class RegistryValueKind(Enum):
    #None: IntType = -1
    Unknown: IntType = 0
    String: IntType = 1
    ExpandString: IntType = 2
    Binary: IntType = 3
    DWord: IntType = 4
    MultiString: IntType = 7
    QWord: IntType = 11


class RegistryValueOptions(Enum):
    #None: IntType = 0
    DoNotExpandEnvironmentNames: IntType = 1


class RegistryView(Enum):
    Default: IntType = 0
    Registry64: IntType = 256
    Registry32: IntType = 512


# No Delegates

__all__ = [
    ASM_CACHE,
    ASM_NAME,
    CANOF,
    Fusion,
    OAVariantLib,
    Registry,
    RegistryKey,
    SafeLibraryHandle,
    UnsafeNativeMethods,
    Win32Native,
    IApplicationContext,
    IAssemblyEnum,
    IAssemblyName,
    RegistryHive,
    RegistryKeyPermissionCheck,
    RegistryOptions,
    RegistryValueKind,
    RegistryValueOptions,
    RegistryView,
]
