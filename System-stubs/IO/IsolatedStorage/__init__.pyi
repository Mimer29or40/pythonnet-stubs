from __future__ import annotations

from abc import ABC
from typing import List, Protocol, Union, overload

from Microsoft.Win32.SafeHandles import SafeFileHandle, SafeHandleZeroOrMinusOneIsInvalid
from System import Array, AsyncCallback, Boolean, Byte, DateTimeOffset, Enum, Exception, IAsyncResult, IDisposable, Int32, Int64, IntPtr, MarshalByRefObject, Object, String, Type, UInt64, Void
from System.Collections import IEnumerator
from System.IO import FileAccess, FileMode, FileShare, FileStream, SeekOrigin
from System.Runtime.InteropServices import _Exception
from System.Runtime.Serialization import ISerializable
from System.Security import SecurityState
from System.Security.Policy import Evidence

# ---------- Types ---------- #

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
ByteType = Union[int, Byte]
IntType = Union[int, Int32]
LongType = Union[int, Int64]
NIntType = Union[int, IntPtr]
ObjectType = Object
StringType = Union[str, String]
TypeType = Union[type, Type]
ULongType = Union[int, UInt64]
VoidType = Union[None, Void]

# ---------- Classes ---------- #

class IsolatedStorage(ABC, MarshalByRefObject):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def ApplicationIdentity(self) -> ObjectType: ...
    
    @property
    def AssemblyIdentity(self) -> ObjectType: ...
    
    @property
    def AvailableFreeSpace(self) -> LongType: ...
    
    @property
    def CurrentSize(self) -> ULongType: ...
    
    @property
    def DomainIdentity(self) -> ObjectType: ...
    
    @property
    def MaximumSize(self) -> ULongType: ...
    
    @property
    def Quota(self) -> LongType: ...
    
    @property
    def Scope(self) -> IsolatedStorageScope: ...
    
    @property
    def UsedSize(self) -> LongType: ...
    
    # ---------- Methods ---------- #
    
    def IncreaseQuotaTo(self, newQuotaSize: LongType) -> BooleanType: ...
    
    def Remove(self) -> VoidType: ...
    
    def get_ApplicationIdentity(self) -> ObjectType: ...
    
    def get_AssemblyIdentity(self) -> ObjectType: ...
    
    def get_AvailableFreeSpace(self) -> LongType: ...
    
    def get_CurrentSize(self) -> ULongType: ...
    
    def get_DomainIdentity(self) -> ObjectType: ...
    
    def get_MaximumSize(self) -> ULongType: ...
    
    def get_Quota(self) -> LongType: ...
    
    def get_Scope(self) -> IsolatedStorageScope: ...
    
    def get_UsedSize(self) -> LongType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class IsolatedStorage(ABC, MarshalByRefObject):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def ApplicationIdentity(self) -> ObjectType: ...
    
    @property
    def AssemblyIdentity(self) -> ObjectType: ...
    
    @property
    def AvailableFreeSpace(self) -> LongType: ...
    
    @property
    def CurrentSize(self) -> ULongType: ...
    
    @property
    def DomainIdentity(self) -> ObjectType: ...
    
    @property
    def MaximumSize(self) -> ULongType: ...
    
    @property
    def Quota(self) -> LongType: ...
    
    @property
    def Scope(self) -> IsolatedStorageScope: ...
    
    @property
    def UsedSize(self) -> LongType: ...
    
    # ---------- Methods ---------- #
    
    def IncreaseQuotaTo(self, newQuotaSize: LongType) -> BooleanType: ...
    
    def Remove(self) -> VoidType: ...
    
    def get_ApplicationIdentity(self) -> ObjectType: ...
    
    def get_AssemblyIdentity(self) -> ObjectType: ...
    
    def get_AvailableFreeSpace(self) -> LongType: ...
    
    def get_CurrentSize(self) -> ULongType: ...
    
    def get_DomainIdentity(self) -> ObjectType: ...
    
    def get_MaximumSize(self) -> ULongType: ...
    
    def get_Quota(self) -> LongType: ...
    
    def get_Scope(self) -> IsolatedStorageScope: ...
    
    def get_UsedSize(self) -> LongType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class IsolatedStorage(ABC, MarshalByRefObject):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def ApplicationIdentity(self) -> ObjectType: ...
    
    @property
    def AssemblyIdentity(self) -> ObjectType: ...
    
    @property
    def AvailableFreeSpace(self) -> LongType: ...
    
    @property
    def CurrentSize(self) -> ULongType: ...
    
    @property
    def DomainIdentity(self) -> ObjectType: ...
    
    @property
    def MaximumSize(self) -> ULongType: ...
    
    @property
    def Quota(self) -> LongType: ...
    
    @property
    def Scope(self) -> IsolatedStorageScope: ...
    
    @property
    def UsedSize(self) -> LongType: ...
    
    # ---------- Methods ---------- #
    
    def IncreaseQuotaTo(self, newQuotaSize: LongType) -> BooleanType: ...
    
    def Remove(self) -> VoidType: ...
    
    def get_ApplicationIdentity(self) -> ObjectType: ...
    
    def get_AssemblyIdentity(self) -> ObjectType: ...
    
    def get_AvailableFreeSpace(self) -> LongType: ...
    
    def get_CurrentSize(self) -> ULongType: ...
    
    def get_DomainIdentity(self) -> ObjectType: ...
    
    def get_MaximumSize(self) -> ULongType: ...
    
    def get_Quota(self) -> LongType: ...
    
    def get_Scope(self) -> IsolatedStorageScope: ...
    
    def get_UsedSize(self) -> LongType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class IsolatedStorageException(Exception, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, inner: Exception): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class IsolatedStorageException(Exception, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, inner: Exception): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class IsolatedStorageException(Exception, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, inner: Exception): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class IsolatedStorageFile(IsolatedStorage, IDisposable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def AvailableFreeSpace(self) -> LongType: ...
    
    @property
    def CurrentSize(self) -> ULongType: ...
    
    @staticmethod
    @property
    def IsEnabled() -> BooleanType: ...
    
    @property
    def MaximumSize(self) -> ULongType: ...
    
    @property
    def Quota(self) -> LongType: ...
    
    @property
    def UsedSize(self) -> LongType: ...
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    @overload
    def CopyFile(self, sourceFileName: StringType, destinationFileName: StringType) -> VoidType: ...
    
    @overload
    def CopyFile(self, sourceFileName: StringType, destinationFileName: StringType, overwrite: BooleanType) -> VoidType: ...
    
    def CreateDirectory(self, dir: StringType) -> VoidType: ...
    
    def CreateFile(self, path: StringType) -> IsolatedStorageFileStream: ...
    
    def DeleteDirectory(self, dir: StringType) -> VoidType: ...
    
    def DeleteFile(self, file: StringType) -> VoidType: ...
    
    def DirectoryExists(self, path: StringType) -> BooleanType: ...
    
    def Dispose(self) -> VoidType: ...
    
    def FileExists(self, path: StringType) -> BooleanType: ...
    
    def GetCreationTime(self, path: StringType) -> DateTimeOffset: ...
    
    @overload
    def GetDirectoryNames(self) -> ArrayType[StringType]: ...
    
    @overload
    def GetDirectoryNames(self, searchPattern: StringType) -> ArrayType[StringType]: ...
    
    @staticmethod
    def GetEnumerator(scope: IsolatedStorageScope) -> IEnumerator: ...
    
    @overload
    def GetFileNames(self) -> ArrayType[StringType]: ...
    
    @overload
    def GetFileNames(self, searchPattern: StringType) -> ArrayType[StringType]: ...
    
    def GetLastAccessTime(self, path: StringType) -> DateTimeOffset: ...
    
    def GetLastWriteTime(self, path: StringType) -> DateTimeOffset: ...
    
    @staticmethod
    def GetMachineStoreForApplication() -> IsolatedStorageFile: ...
    
    @staticmethod
    def GetMachineStoreForAssembly() -> IsolatedStorageFile: ...
    
    @staticmethod
    def GetMachineStoreForDomain() -> IsolatedStorageFile: ...
    
    @staticmethod
    @overload
    def GetStore(scope: IsolatedStorageScope, domainEvidenceType: TypeType, assemblyEvidenceType: TypeType) -> IsolatedStorageFile: ...
    
    @staticmethod
    @overload
    def GetStore(scope: IsolatedStorageScope, domainIdentity: ObjectType, assemblyIdentity: ObjectType) -> IsolatedStorageFile: ...
    
    @staticmethod
    @overload
    def GetStore(scope: IsolatedStorageScope, domainEvidence: Evidence, domainEvidenceType: TypeType, assemblyEvidence: Evidence, assemblyEvidenceType: TypeType) -> IsolatedStorageFile: ...
    
    @staticmethod
    @overload
    def GetStore(scope: IsolatedStorageScope, applicationEvidenceType: TypeType) -> IsolatedStorageFile: ...
    
    @staticmethod
    @overload
    def GetStore(scope: IsolatedStorageScope, applicationIdentity: ObjectType) -> IsolatedStorageFile: ...
    
    @staticmethod
    def GetUserStoreForApplication() -> IsolatedStorageFile: ...
    
    @staticmethod
    def GetUserStoreForAssembly() -> IsolatedStorageFile: ...
    
    @staticmethod
    def GetUserStoreForDomain() -> IsolatedStorageFile: ...
    
    @staticmethod
    def GetUserStoreForSite() -> IsolatedStorageFile: ...
    
    def IncreaseQuotaTo(self, newQuotaSize: LongType) -> BooleanType: ...
    
    def MoveDirectory(self, sourceDirectoryName: StringType, destinationDirectoryName: StringType) -> VoidType: ...
    
    def MoveFile(self, sourceFileName: StringType, destinationFileName: StringType) -> VoidType: ...
    
    @overload
    def OpenFile(self, path: StringType, mode: FileMode) -> IsolatedStorageFileStream: ...
    
    @overload
    def OpenFile(self, path: StringType, mode: FileMode, access: FileAccess) -> IsolatedStorageFileStream: ...
    
    @overload
    def OpenFile(self, path: StringType, mode: FileMode, access: FileAccess, share: FileShare) -> IsolatedStorageFileStream: ...
    
    @overload
    def Remove(self) -> VoidType: ...
    
    @staticmethod
    @overload
    def Remove(scope: IsolatedStorageScope) -> VoidType: ...
    
    def get_AvailableFreeSpace(self) -> LongType: ...
    
    def get_CurrentSize(self) -> ULongType: ...
    
    @staticmethod
    def get_IsEnabled() -> BooleanType: ...
    
    def get_MaximumSize(self) -> ULongType: ...
    
    def get_Quota(self) -> LongType: ...
    
    def get_UsedSize(self) -> LongType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class IsolatedStorageFile(IsolatedStorage, IDisposable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def AvailableFreeSpace(self) -> LongType: ...
    
    @property
    def CurrentSize(self) -> ULongType: ...
    
    @staticmethod
    @property
    def IsEnabled() -> BooleanType: ...
    
    @property
    def MaximumSize(self) -> ULongType: ...
    
    @property
    def Quota(self) -> LongType: ...
    
    @property
    def UsedSize(self) -> LongType: ...
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    @overload
    def CopyFile(self, sourceFileName: StringType, destinationFileName: StringType) -> VoidType: ...
    
    @overload
    def CopyFile(self, sourceFileName: StringType, destinationFileName: StringType, overwrite: BooleanType) -> VoidType: ...
    
    def CreateDirectory(self, dir: StringType) -> VoidType: ...
    
    def CreateFile(self, path: StringType) -> IsolatedStorageFileStream: ...
    
    def DeleteDirectory(self, dir: StringType) -> VoidType: ...
    
    def DeleteFile(self, file: StringType) -> VoidType: ...
    
    def DirectoryExists(self, path: StringType) -> BooleanType: ...
    
    def Dispose(self) -> VoidType: ...
    
    def FileExists(self, path: StringType) -> BooleanType: ...
    
    def GetCreationTime(self, path: StringType) -> DateTimeOffset: ...
    
    @overload
    def GetDirectoryNames(self) -> ArrayType[StringType]: ...
    
    @overload
    def GetDirectoryNames(self, searchPattern: StringType) -> ArrayType[StringType]: ...
    
    @staticmethod
    def GetEnumerator(scope: IsolatedStorageScope) -> IEnumerator: ...
    
    @overload
    def GetFileNames(self) -> ArrayType[StringType]: ...
    
    @overload
    def GetFileNames(self, searchPattern: StringType) -> ArrayType[StringType]: ...
    
    def GetLastAccessTime(self, path: StringType) -> DateTimeOffset: ...
    
    def GetLastWriteTime(self, path: StringType) -> DateTimeOffset: ...
    
    @staticmethod
    def GetMachineStoreForApplication() -> IsolatedStorageFile: ...
    
    @staticmethod
    def GetMachineStoreForAssembly() -> IsolatedStorageFile: ...
    
    @staticmethod
    def GetMachineStoreForDomain() -> IsolatedStorageFile: ...
    
    @staticmethod
    @overload
    def GetStore(scope: IsolatedStorageScope, domainEvidenceType: TypeType, assemblyEvidenceType: TypeType) -> IsolatedStorageFile: ...
    
    @staticmethod
    @overload
    def GetStore(scope: IsolatedStorageScope, domainIdentity: ObjectType, assemblyIdentity: ObjectType) -> IsolatedStorageFile: ...
    
    @staticmethod
    @overload
    def GetStore(scope: IsolatedStorageScope, domainEvidence: Evidence, domainEvidenceType: TypeType, assemblyEvidence: Evidence, assemblyEvidenceType: TypeType) -> IsolatedStorageFile: ...
    
    @staticmethod
    @overload
    def GetStore(scope: IsolatedStorageScope, applicationEvidenceType: TypeType) -> IsolatedStorageFile: ...
    
    @staticmethod
    @overload
    def GetStore(scope: IsolatedStorageScope, applicationIdentity: ObjectType) -> IsolatedStorageFile: ...
    
    @staticmethod
    def GetUserStoreForApplication() -> IsolatedStorageFile: ...
    
    @staticmethod
    def GetUserStoreForAssembly() -> IsolatedStorageFile: ...
    
    @staticmethod
    def GetUserStoreForDomain() -> IsolatedStorageFile: ...
    
    @staticmethod
    def GetUserStoreForSite() -> IsolatedStorageFile: ...
    
    def IncreaseQuotaTo(self, newQuotaSize: LongType) -> BooleanType: ...
    
    def MoveDirectory(self, sourceDirectoryName: StringType, destinationDirectoryName: StringType) -> VoidType: ...
    
    def MoveFile(self, sourceFileName: StringType, destinationFileName: StringType) -> VoidType: ...
    
    @overload
    def OpenFile(self, path: StringType, mode: FileMode) -> IsolatedStorageFileStream: ...
    
    @overload
    def OpenFile(self, path: StringType, mode: FileMode, access: FileAccess) -> IsolatedStorageFileStream: ...
    
    @overload
    def OpenFile(self, path: StringType, mode: FileMode, access: FileAccess, share: FileShare) -> IsolatedStorageFileStream: ...
    
    @overload
    def Remove(self) -> VoidType: ...
    
    @staticmethod
    @overload
    def Remove(scope: IsolatedStorageScope) -> VoidType: ...
    
    def get_AvailableFreeSpace(self) -> LongType: ...
    
    def get_CurrentSize(self) -> ULongType: ...
    
    @staticmethod
    def get_IsEnabled() -> BooleanType: ...
    
    def get_MaximumSize(self) -> ULongType: ...
    
    def get_Quota(self) -> LongType: ...
    
    def get_UsedSize(self) -> LongType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class IsolatedStorageFile(IsolatedStorage, IDisposable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def AvailableFreeSpace(self) -> LongType: ...
    
    @property
    def CurrentSize(self) -> ULongType: ...
    
    @staticmethod
    @property
    def IsEnabled() -> BooleanType: ...
    
    @property
    def MaximumSize(self) -> ULongType: ...
    
    @property
    def Quota(self) -> LongType: ...
    
    @property
    def UsedSize(self) -> LongType: ...
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    @overload
    def CopyFile(self, sourceFileName: StringType, destinationFileName: StringType) -> VoidType: ...
    
    @overload
    def CopyFile(self, sourceFileName: StringType, destinationFileName: StringType, overwrite: BooleanType) -> VoidType: ...
    
    def CreateDirectory(self, dir: StringType) -> VoidType: ...
    
    def CreateFile(self, path: StringType) -> IsolatedStorageFileStream: ...
    
    def DeleteDirectory(self, dir: StringType) -> VoidType: ...
    
    def DeleteFile(self, file: StringType) -> VoidType: ...
    
    def DirectoryExists(self, path: StringType) -> BooleanType: ...
    
    def Dispose(self) -> VoidType: ...
    
    def FileExists(self, path: StringType) -> BooleanType: ...
    
    def GetCreationTime(self, path: StringType) -> DateTimeOffset: ...
    
    @overload
    def GetDirectoryNames(self) -> ArrayType[StringType]: ...
    
    @overload
    def GetDirectoryNames(self, searchPattern: StringType) -> ArrayType[StringType]: ...
    
    @staticmethod
    def GetEnumerator(scope: IsolatedStorageScope) -> IEnumerator: ...
    
    @overload
    def GetFileNames(self) -> ArrayType[StringType]: ...
    
    @overload
    def GetFileNames(self, searchPattern: StringType) -> ArrayType[StringType]: ...
    
    def GetLastAccessTime(self, path: StringType) -> DateTimeOffset: ...
    
    def GetLastWriteTime(self, path: StringType) -> DateTimeOffset: ...
    
    @staticmethod
    def GetMachineStoreForApplication() -> IsolatedStorageFile: ...
    
    @staticmethod
    def GetMachineStoreForAssembly() -> IsolatedStorageFile: ...
    
    @staticmethod
    def GetMachineStoreForDomain() -> IsolatedStorageFile: ...
    
    @staticmethod
    @overload
    def GetStore(scope: IsolatedStorageScope, domainEvidenceType: TypeType, assemblyEvidenceType: TypeType) -> IsolatedStorageFile: ...
    
    @staticmethod
    @overload
    def GetStore(scope: IsolatedStorageScope, domainIdentity: ObjectType, assemblyIdentity: ObjectType) -> IsolatedStorageFile: ...
    
    @staticmethod
    @overload
    def GetStore(scope: IsolatedStorageScope, domainEvidence: Evidence, domainEvidenceType: TypeType, assemblyEvidence: Evidence, assemblyEvidenceType: TypeType) -> IsolatedStorageFile: ...
    
    @staticmethod
    @overload
    def GetStore(scope: IsolatedStorageScope, applicationEvidenceType: TypeType) -> IsolatedStorageFile: ...
    
    @staticmethod
    @overload
    def GetStore(scope: IsolatedStorageScope, applicationIdentity: ObjectType) -> IsolatedStorageFile: ...
    
    @staticmethod
    def GetUserStoreForApplication() -> IsolatedStorageFile: ...
    
    @staticmethod
    def GetUserStoreForAssembly() -> IsolatedStorageFile: ...
    
    @staticmethod
    def GetUserStoreForDomain() -> IsolatedStorageFile: ...
    
    @staticmethod
    def GetUserStoreForSite() -> IsolatedStorageFile: ...
    
    def IncreaseQuotaTo(self, newQuotaSize: LongType) -> BooleanType: ...
    
    def MoveDirectory(self, sourceDirectoryName: StringType, destinationDirectoryName: StringType) -> VoidType: ...
    
    def MoveFile(self, sourceFileName: StringType, destinationFileName: StringType) -> VoidType: ...
    
    @overload
    def OpenFile(self, path: StringType, mode: FileMode) -> IsolatedStorageFileStream: ...
    
    @overload
    def OpenFile(self, path: StringType, mode: FileMode, access: FileAccess) -> IsolatedStorageFileStream: ...
    
    @overload
    def OpenFile(self, path: StringType, mode: FileMode, access: FileAccess, share: FileShare) -> IsolatedStorageFileStream: ...
    
    @overload
    def Remove(self) -> VoidType: ...
    
    @staticmethod
    @overload
    def Remove(scope: IsolatedStorageScope) -> VoidType: ...
    
    def get_AvailableFreeSpace(self) -> LongType: ...
    
    def get_CurrentSize(self) -> ULongType: ...
    
    @staticmethod
    def get_IsEnabled() -> BooleanType: ...
    
    def get_MaximumSize(self) -> ULongType: ...
    
    def get_Quota(self) -> LongType: ...
    
    def get_UsedSize(self) -> LongType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class IsolatedStorageFileEnumerator(ObjectType, IEnumerator):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Current(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def MoveNext(self) -> BooleanType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Current(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class IsolatedStorageFileEnumerator(ObjectType, IEnumerator):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Current(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def MoveNext(self) -> BooleanType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Current(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class IsolatedStorageFileEnumerator(ObjectType, IEnumerator):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Current(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def MoveNext(self) -> BooleanType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Current(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class IsolatedStorageFileStream(FileStream, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, path: StringType, mode: FileMode): ...
    
    @overload
    def __init__(self, path: StringType, mode: FileMode, isf: IsolatedStorageFile): ...
    
    @overload
    def __init__(self, path: StringType, mode: FileMode, access: FileAccess): ...
    
    @overload
    def __init__(self, path: StringType, mode: FileMode, access: FileAccess, isf: IsolatedStorageFile): ...
    
    @overload
    def __init__(self, path: StringType, mode: FileMode, access: FileAccess, share: FileShare): ...
    
    @overload
    def __init__(self, path: StringType, mode: FileMode, access: FileAccess, share: FileShare, isf: IsolatedStorageFile): ...
    
    @overload
    def __init__(self, path: StringType, mode: FileMode, access: FileAccess, share: FileShare, bufferSize: IntType): ...
    
    @overload
    def __init__(self, path: StringType, mode: FileMode, access: FileAccess, share: FileShare, bufferSize: IntType, isf: IsolatedStorageFile): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CanRead(self) -> BooleanType: ...
    
    @property
    def CanSeek(self) -> BooleanType: ...
    
    @property
    def CanWrite(self) -> BooleanType: ...
    
    @property
    def Handle(self) -> NIntType: ...
    
    @property
    def IsAsync(self) -> BooleanType: ...
    
    @property
    def Length(self) -> LongType: ...
    
    @property
    def Position(self) -> LongType: ...
    
    @Position.setter
    def Position(self, value: LongType) -> None: ...
    
    @property
    def SafeFileHandle(self) -> SafeFileHandle: ...
    
    # ---------- Methods ---------- #
    
    def BeginRead(self, buffer: ArrayType[ByteType], offset: IntType, numBytes: IntType, userCallback: AsyncCallback, stateObject: ObjectType) -> IAsyncResult: ...
    
    def BeginWrite(self, buffer: ArrayType[ByteType], offset: IntType, numBytes: IntType, userCallback: AsyncCallback, stateObject: ObjectType) -> IAsyncResult: ...
    
    def EndRead(self, asyncResult: IAsyncResult) -> IntType: ...
    
    def EndWrite(self, asyncResult: IAsyncResult) -> VoidType: ...
    
    @overload
    def Flush(self) -> VoidType: ...
    
    @overload
    def Flush(self, flushToDisk: BooleanType) -> VoidType: ...
    
    def Lock(self, position: LongType, length: LongType) -> VoidType: ...
    
    def Read(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType) -> IntType: ...
    
    def ReadByte(self) -> IntType: ...
    
    def Seek(self, offset: LongType, origin: SeekOrigin) -> LongType: ...
    
    def SetLength(self, value: LongType) -> VoidType: ...
    
    def Unlock(self, position: LongType, length: LongType) -> VoidType: ...
    
    def Write(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType) -> VoidType: ...
    
    def WriteByte(self, value: ByteType) -> VoidType: ...
    
    def get_CanRead(self) -> BooleanType: ...
    
    def get_CanSeek(self) -> BooleanType: ...
    
    def get_CanWrite(self) -> BooleanType: ...
    
    def get_Handle(self) -> NIntType: ...
    
    def get_IsAsync(self) -> BooleanType: ...
    
    def get_Length(self) -> LongType: ...
    
    def get_Position(self) -> LongType: ...
    
    def get_SafeFileHandle(self) -> SafeFileHandle: ...
    
    def set_Position(self, value: LongType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class IsolatedStorageFileStream(FileStream, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, path: StringType, mode: FileMode): ...
    
    @overload
    def __init__(self, path: StringType, mode: FileMode, isf: IsolatedStorageFile): ...
    
    @overload
    def __init__(self, path: StringType, mode: FileMode, access: FileAccess): ...
    
    @overload
    def __init__(self, path: StringType, mode: FileMode, access: FileAccess, isf: IsolatedStorageFile): ...
    
    @overload
    def __init__(self, path: StringType, mode: FileMode, access: FileAccess, share: FileShare): ...
    
    @overload
    def __init__(self, path: StringType, mode: FileMode, access: FileAccess, share: FileShare, isf: IsolatedStorageFile): ...
    
    @overload
    def __init__(self, path: StringType, mode: FileMode, access: FileAccess, share: FileShare, bufferSize: IntType): ...
    
    @overload
    def __init__(self, path: StringType, mode: FileMode, access: FileAccess, share: FileShare, bufferSize: IntType, isf: IsolatedStorageFile): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CanRead(self) -> BooleanType: ...
    
    @property
    def CanSeek(self) -> BooleanType: ...
    
    @property
    def CanWrite(self) -> BooleanType: ...
    
    @property
    def Handle(self) -> NIntType: ...
    
    @property
    def IsAsync(self) -> BooleanType: ...
    
    @property
    def Length(self) -> LongType: ...
    
    @property
    def Position(self) -> LongType: ...
    
    @Position.setter
    def Position(self, value: LongType) -> None: ...
    
    @property
    def SafeFileHandle(self) -> SafeFileHandle: ...
    
    # ---------- Methods ---------- #
    
    def BeginRead(self, buffer: ArrayType[ByteType], offset: IntType, numBytes: IntType, userCallback: AsyncCallback, stateObject: ObjectType) -> IAsyncResult: ...
    
    def BeginWrite(self, buffer: ArrayType[ByteType], offset: IntType, numBytes: IntType, userCallback: AsyncCallback, stateObject: ObjectType) -> IAsyncResult: ...
    
    def EndRead(self, asyncResult: IAsyncResult) -> IntType: ...
    
    def EndWrite(self, asyncResult: IAsyncResult) -> VoidType: ...
    
    @overload
    def Flush(self) -> VoidType: ...
    
    @overload
    def Flush(self, flushToDisk: BooleanType) -> VoidType: ...
    
    def Lock(self, position: LongType, length: LongType) -> VoidType: ...
    
    def Read(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType) -> IntType: ...
    
    def ReadByte(self) -> IntType: ...
    
    def Seek(self, offset: LongType, origin: SeekOrigin) -> LongType: ...
    
    def SetLength(self, value: LongType) -> VoidType: ...
    
    def Unlock(self, position: LongType, length: LongType) -> VoidType: ...
    
    def Write(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType) -> VoidType: ...
    
    def WriteByte(self, value: ByteType) -> VoidType: ...
    
    def get_CanRead(self) -> BooleanType: ...
    
    def get_CanSeek(self) -> BooleanType: ...
    
    def get_CanWrite(self) -> BooleanType: ...
    
    def get_Handle(self) -> NIntType: ...
    
    def get_IsAsync(self) -> BooleanType: ...
    
    def get_Length(self) -> LongType: ...
    
    def get_Position(self) -> LongType: ...
    
    def get_SafeFileHandle(self) -> SafeFileHandle: ...
    
    def set_Position(self, value: LongType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class IsolatedStorageFileStream(FileStream, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, path: StringType, mode: FileMode): ...
    
    @overload
    def __init__(self, path: StringType, mode: FileMode, isf: IsolatedStorageFile): ...
    
    @overload
    def __init__(self, path: StringType, mode: FileMode, access: FileAccess): ...
    
    @overload
    def __init__(self, path: StringType, mode: FileMode, access: FileAccess, isf: IsolatedStorageFile): ...
    
    @overload
    def __init__(self, path: StringType, mode: FileMode, access: FileAccess, share: FileShare): ...
    
    @overload
    def __init__(self, path: StringType, mode: FileMode, access: FileAccess, share: FileShare, isf: IsolatedStorageFile): ...
    
    @overload
    def __init__(self, path: StringType, mode: FileMode, access: FileAccess, share: FileShare, bufferSize: IntType): ...
    
    @overload
    def __init__(self, path: StringType, mode: FileMode, access: FileAccess, share: FileShare, bufferSize: IntType, isf: IsolatedStorageFile): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CanRead(self) -> BooleanType: ...
    
    @property
    def CanSeek(self) -> BooleanType: ...
    
    @property
    def CanWrite(self) -> BooleanType: ...
    
    @property
    def Handle(self) -> NIntType: ...
    
    @property
    def IsAsync(self) -> BooleanType: ...
    
    @property
    def Length(self) -> LongType: ...
    
    @property
    def Position(self) -> LongType: ...
    
    @Position.setter
    def Position(self, value: LongType) -> None: ...
    
    @property
    def SafeFileHandle(self) -> SafeFileHandle: ...
    
    # ---------- Methods ---------- #
    
    def BeginRead(self, buffer: ArrayType[ByteType], offset: IntType, numBytes: IntType, userCallback: AsyncCallback, stateObject: ObjectType) -> IAsyncResult: ...
    
    def BeginWrite(self, buffer: ArrayType[ByteType], offset: IntType, numBytes: IntType, userCallback: AsyncCallback, stateObject: ObjectType) -> IAsyncResult: ...
    
    def EndRead(self, asyncResult: IAsyncResult) -> IntType: ...
    
    def EndWrite(self, asyncResult: IAsyncResult) -> VoidType: ...
    
    @overload
    def Flush(self) -> VoidType: ...
    
    @overload
    def Flush(self, flushToDisk: BooleanType) -> VoidType: ...
    
    def Lock(self, position: LongType, length: LongType) -> VoidType: ...
    
    def Read(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType) -> IntType: ...
    
    def ReadByte(self) -> IntType: ...
    
    def Seek(self, offset: LongType, origin: SeekOrigin) -> LongType: ...
    
    def SetLength(self, value: LongType) -> VoidType: ...
    
    def Unlock(self, position: LongType, length: LongType) -> VoidType: ...
    
    def Write(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType) -> VoidType: ...
    
    def WriteByte(self, value: ByteType) -> VoidType: ...
    
    def get_CanRead(self) -> BooleanType: ...
    
    def get_CanSeek(self) -> BooleanType: ...
    
    def get_CanWrite(self) -> BooleanType: ...
    
    def get_Handle(self) -> NIntType: ...
    
    def get_IsAsync(self) -> BooleanType: ...
    
    def get_Length(self) -> LongType: ...
    
    def get_Position(self) -> LongType: ...
    
    def get_SafeFileHandle(self) -> SafeFileHandle: ...
    
    def set_Position(self, value: LongType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class IsolatedStorageSecurityState(SecurityState):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Options(self) -> IsolatedStorageSecurityOptions: ...
    
    @property
    def Quota(self) -> LongType: ...
    
    @Quota.setter
    def Quota(self, value: LongType) -> None: ...
    
    @property
    def UsedSize(self) -> LongType: ...
    
    # ---------- Methods ---------- #
    
    def EnsureState(self) -> VoidType: ...
    
    def get_Options(self) -> IsolatedStorageSecurityOptions: ...
    
    def get_Quota(self) -> LongType: ...
    
    def get_UsedSize(self) -> LongType: ...
    
    def set_Quota(self, value: LongType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class IsolatedStorageSecurityState(SecurityState):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Options(self) -> IsolatedStorageSecurityOptions: ...
    
    @property
    def Quota(self) -> LongType: ...
    
    @Quota.setter
    def Quota(self, value: LongType) -> None: ...
    
    @property
    def UsedSize(self) -> LongType: ...
    
    # ---------- Methods ---------- #
    
    def EnsureState(self) -> VoidType: ...
    
    def get_Options(self) -> IsolatedStorageSecurityOptions: ...
    
    def get_Quota(self) -> LongType: ...
    
    def get_UsedSize(self) -> LongType: ...
    
    def set_Quota(self, value: LongType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class IsolatedStorageSecurityState(SecurityState):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Options(self) -> IsolatedStorageSecurityOptions: ...
    
    @property
    def Quota(self) -> LongType: ...
    
    @Quota.setter
    def Quota(self, value: LongType) -> None: ...
    
    @property
    def UsedSize(self) -> LongType: ...
    
    # ---------- Methods ---------- #
    
    def EnsureState(self) -> VoidType: ...
    
    def get_Options(self) -> IsolatedStorageSecurityOptions: ...
    
    def get_Quota(self) -> LongType: ...
    
    def get_UsedSize(self) -> LongType: ...
    
    def set_Quota(self, value: LongType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SafeIsolatedStorageFileHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
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


class SafeIsolatedStorageFileHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
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


class SafeIsolatedStorageFileHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
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


class TwoLevelFileEnumerator(ObjectType, IEnumerator):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, root: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Current(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def MoveNext(self) -> BooleanType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Current(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TwoLevelFileEnumerator(ObjectType, IEnumerator):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, root: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Current(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def MoveNext(self) -> BooleanType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Current(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TwoLevelFileEnumerator(ObjectType, IEnumerator):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, root: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Current(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def MoveNext(self) -> BooleanType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Current(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TwoPaths(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def Path1(self) -> StringType: ...
    
    @Path1.setter
    def Path1(self, value: StringType) -> None: ...
    
    @property
    def Path2(self) -> StringType: ...
    
    @Path2.setter
    def Path2(self, value: StringType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TwoPaths(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def Path1(self) -> StringType: ...
    
    @Path1.setter
    def Path1(self, value: StringType) -> None: ...
    
    @property
    def Path2(self) -> StringType: ...
    
    @Path2.setter
    def Path2(self, value: StringType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TwoPaths(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def Path1(self) -> StringType: ...
    
    @Path1.setter
    def Path1(self, value: StringType) -> None: ...
    
    @property
    def Path2(self) -> StringType: ...
    
    @Path2.setter
    def Path2(self, value: StringType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class __HResults(ABC, ObjectType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def COR_E_ISOSTORE() -> IntType: ...
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class __HResults(ABC, ObjectType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def COR_E_ISOSTORE() -> IntType: ...
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class __HResults(ABC, ObjectType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def COR_E_ISOSTORE() -> IntType: ...
    
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

class INormalizeForIsolatedStorage(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Normalize(self) -> ObjectType: ...
    
    # No Events


class INormalizeForIsolatedStorage(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Normalize(self) -> ObjectType: ...
    
    # No Events


class INormalizeForIsolatedStorage(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Normalize(self) -> ObjectType: ...
    
    # No Events


# ---------- Enums ---------- #

class IsolatedStorageScope(Enum):
    #None: IntType = 0
    User: IntType = 1
    Domain: IntType = 2
    Assembly: IntType = 4
    Roaming: IntType = 8
    Machine: IntType = 16
    Application: IntType = 32


class IsolatedStorageScope(Enum):
    #None: IntType = 0
    User: IntType = 1
    Domain: IntType = 2
    Assembly: IntType = 4
    Roaming: IntType = 8
    Machine: IntType = 16
    Application: IntType = 32


class IsolatedStorageScope(Enum):
    #None: IntType = 0
    User: IntType = 1
    Domain: IntType = 2
    Assembly: IntType = 4
    Roaming: IntType = 8
    Machine: IntType = 16
    Application: IntType = 32


class IsolatedStorageSecurityOptions(Enum):
    IncreaseQuotaForApplication: IntType = 4


class IsolatedStorageSecurityOptions(Enum):
    IncreaseQuotaForApplication: IntType = 4


class IsolatedStorageSecurityOptions(Enum):
    IncreaseQuotaForApplication: IntType = 4


# No Delegates

__all__ = [
    IsolatedStorage,
    IsolatedStorageException,
    IsolatedStorageFile,
    IsolatedStorageFileEnumerator,
    IsolatedStorageFileStream,
    IsolatedStorageSecurityState,
    SafeIsolatedStorageFileHandle,
    TwoLevelFileEnumerator,
    TwoPaths,
    __HResults,
    INormalizeForIsolatedStorage,
    IsolatedStorageScope,
    IsolatedStorageSecurityOptions,
]
