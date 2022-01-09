from __future__ import annotations

from abc import ABC
from typing import Generic, List, Protocol, Tuple, TypeVar, Union, overload

from Microsoft.Win32.SafeHandles import SafeFileHandle
from System import Array, ArraySegment, AsyncCallback, Boolean, Byte, Char, DateTime, Decimal, Double, Enum, Exception, IAsyncResult, IDisposable, IFormatProvider, Int16, Int32, Int64, IntPtr, MarshalByRefObject, Object, SByte, Single, String, SystemException, UInt16, UInt32, UInt64, ValueType, Void
from System.Collections import IEnumerable, IEnumerator
from System.Collections.Generic import IEnumerable, IEnumerator
from System.Runtime.InteropServices import SafeBuffer, _Exception
from System.Runtime.Serialization import ISerializable, SerializationInfo, StreamingContext
from System.Security.AccessControl import AccessControlSections, DirectorySecurity, FileSecurity, FileSystemRights
from System.Text import Encoding, StringBuilder
from System.Threading import CancellationToken, WaitHandle
from System.Threading.Tasks import Task

# ---------- Types ---------- #

TSource = TypeVar('TSource')

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
ByteType = Union[int, Byte]
CharType = Union[str, Char]
DecimalType = Union[float, Decimal]
DoubleType = Union[float, Double]
FloatType = Union[float, Single]
IntType = Union[int, Int32]
LongType = Union[int, Int64]
NIntType = Union[int, IntPtr]
ObjectType = Object
SByteType = Union[int, SByte]
ShortType = Union[int, Int16]
StringType = Union[str, String]
UIntType = Union[int, UInt32]
ULongType = Union[int, UInt64]
UShortType = Union[int, UInt16]
VoidType = Union[None, Void]

# ---------- Classes ---------- #

class BinaryReader(ObjectType, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, input: Stream): ...
    
    @overload
    def __init__(self, input: Stream, encoding: Encoding): ...
    
    @overload
    def __init__(self, input: Stream, encoding: Encoding, leaveOpen: BooleanType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def BaseStream(self) -> Stream: ...
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    def Dispose(self) -> VoidType: ...
    
    def PeekChar(self) -> IntType: ...
    
    @overload
    def Read(self) -> IntType: ...
    
    @overload
    def Read(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> IntType: ...
    
    @overload
    def Read(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadBoolean(self) -> BooleanType: ...
    
    def ReadByte(self) -> ByteType: ...
    
    def ReadBytes(self, count: IntType) -> ArrayType[ByteType]: ...
    
    def ReadChar(self) -> CharType: ...
    
    def ReadChars(self, count: IntType) -> ArrayType[CharType]: ...
    
    def ReadDecimal(self) -> DecimalType: ...
    
    def ReadDouble(self) -> DoubleType: ...
    
    def ReadInt16(self) -> ShortType: ...
    
    def ReadInt32(self) -> IntType: ...
    
    def ReadInt64(self) -> LongType: ...
    
    def ReadSByte(self) -> SByteType: ...
    
    def ReadSingle(self) -> FloatType: ...
    
    def ReadString(self) -> StringType: ...
    
    def ReadUInt16(self) -> UShortType: ...
    
    def ReadUInt32(self) -> UIntType: ...
    
    def ReadUInt64(self) -> ULongType: ...
    
    def get_BaseStream(self) -> Stream: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class BinaryWriter(ObjectType, IDisposable):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Null() -> BinaryWriter: ...
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, output: Stream): ...
    
    @overload
    def __init__(self, output: Stream, encoding: Encoding): ...
    
    @overload
    def __init__(self, output: Stream, encoding: Encoding, leaveOpen: BooleanType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def BaseStream(self) -> Stream: ...
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    def Dispose(self) -> VoidType: ...
    
    def Flush(self) -> VoidType: ...
    
    def Seek(self, offset: IntType, origin: SeekOrigin) -> LongType: ...
    
    @overload
    def Write(self, value: BooleanType) -> VoidType: ...
    
    @overload
    def Write(self, value: ByteType) -> VoidType: ...
    
    @overload
    def Write(self, value: SByteType) -> VoidType: ...
    
    @overload
    def Write(self, buffer: ArrayType[ByteType]) -> VoidType: ...
    
    @overload
    def Write(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> VoidType: ...
    
    @overload
    def Write(self, ch: CharType) -> VoidType: ...
    
    @overload
    def Write(self, chars: ArrayType[CharType]) -> VoidType: ...
    
    @overload
    def Write(self, chars: ArrayType[CharType], index: IntType, count: IntType) -> VoidType: ...
    
    @overload
    def Write(self, value: DoubleType) -> VoidType: ...
    
    @overload
    def Write(self, value: DecimalType) -> VoidType: ...
    
    @overload
    def Write(self, value: ShortType) -> VoidType: ...
    
    @overload
    def Write(self, value: UShortType) -> VoidType: ...
    
    @overload
    def Write(self, value: IntType) -> VoidType: ...
    
    @overload
    def Write(self, value: UIntType) -> VoidType: ...
    
    @overload
    def Write(self, value: LongType) -> VoidType: ...
    
    @overload
    def Write(self, value: ULongType) -> VoidType: ...
    
    @overload
    def Write(self, value: FloatType) -> VoidType: ...
    
    @overload
    def Write(self, value: StringType) -> VoidType: ...
    
    def get_BaseStream(self) -> Stream: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class BufferedStream(Stream, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, stream: Stream): ...
    
    @overload
    def __init__(self, stream: Stream, bufferSize: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CanRead(self) -> BooleanType: ...
    
    @property
    def CanSeek(self) -> BooleanType: ...
    
    @property
    def CanWrite(self) -> BooleanType: ...
    
    @property
    def Length(self) -> LongType: ...
    
    @property
    def Position(self) -> LongType: ...
    
    @Position.setter
    def Position(self, value: LongType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def BeginRead(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType, callback: AsyncCallback, state: ObjectType) -> IAsyncResult: ...
    
    def BeginWrite(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType, callback: AsyncCallback, state: ObjectType) -> IAsyncResult: ...
    
    def EndRead(self, asyncResult: IAsyncResult) -> IntType: ...
    
    def EndWrite(self, asyncResult: IAsyncResult) -> VoidType: ...
    
    def Flush(self) -> VoidType: ...
    
    @overload
    def FlushAsync(self, cancellationToken: CancellationToken) -> Task: ...
    
    def Read(self, array: ArrayType[ByteType], offset: IntType, count: IntType) -> Tuple[IntType, ArrayType[ByteType]]: ...
    
    @overload
    def ReadAsync(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType, cancellationToken: CancellationToken) -> Task[IntType]: ...
    
    def ReadByte(self) -> IntType: ...
    
    def Seek(self, offset: LongType, origin: SeekOrigin) -> LongType: ...
    
    def SetLength(self, value: LongType) -> VoidType: ...
    
    def Write(self, array: ArrayType[ByteType], offset: IntType, count: IntType) -> VoidType: ...
    
    @overload
    def WriteAsync(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType, cancellationToken: CancellationToken) -> Task: ...
    
    def WriteByte(self, value: ByteType) -> VoidType: ...
    
    def get_CanRead(self) -> BooleanType: ...
    
    def get_CanSeek(self) -> BooleanType: ...
    
    def get_CanWrite(self) -> BooleanType: ...
    
    def get_Length(self) -> LongType: ...
    
    def get_Position(self) -> LongType: ...
    
    def set_Position(self, value: LongType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Directory(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    @overload
    def CreateDirectory(path: StringType) -> DirectoryInfo: ...
    
    @staticmethod
    @overload
    def CreateDirectory(path: StringType, directorySecurity: DirectorySecurity) -> DirectoryInfo: ...
    
    @staticmethod
    @overload
    def Delete(path: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Delete(path: StringType, recursive: BooleanType) -> VoidType: ...
    
    @staticmethod
    @overload
    def EnumerateDirectories(path: StringType, searchPattern: StringType) -> IEnumerable[StringType]: ...
    
    @staticmethod
    @overload
    def EnumerateDirectories(path: StringType, searchPattern: StringType, searchOption: SearchOption) -> IEnumerable[StringType]: ...
    
    @staticmethod
    @overload
    def EnumerateDirectories(path: StringType) -> IEnumerable[StringType]: ...
    
    @staticmethod
    @overload
    def EnumerateFileSystemEntries(path: StringType, searchPattern: StringType) -> IEnumerable[StringType]: ...
    
    @staticmethod
    @overload
    def EnumerateFileSystemEntries(path: StringType, searchPattern: StringType, searchOption: SearchOption) -> IEnumerable[StringType]: ...
    
    @staticmethod
    @overload
    def EnumerateFileSystemEntries(path: StringType) -> IEnumerable[StringType]: ...
    
    @staticmethod
    @overload
    def EnumerateFiles(path: StringType, searchPattern: StringType) -> IEnumerable[StringType]: ...
    
    @staticmethod
    @overload
    def EnumerateFiles(path: StringType, searchPattern: StringType, searchOption: SearchOption) -> IEnumerable[StringType]: ...
    
    @staticmethod
    @overload
    def EnumerateFiles(path: StringType) -> IEnumerable[StringType]: ...
    
    @staticmethod
    def Exists(path: StringType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def GetAccessControl(path: StringType) -> DirectorySecurity: ...
    
    @staticmethod
    @overload
    def GetAccessControl(path: StringType, includeSections: AccessControlSections) -> DirectorySecurity: ...
    
    @staticmethod
    def GetCreationTime(path: StringType) -> DateTime: ...
    
    @staticmethod
    def GetCreationTimeUtc(path: StringType) -> DateTime: ...
    
    @staticmethod
    def GetCurrentDirectory() -> StringType: ...
    
    @staticmethod
    @overload
    def GetDirectories(path: StringType, searchPattern: StringType) -> ArrayType[StringType]: ...
    
    @staticmethod
    @overload
    def GetDirectories(path: StringType, searchPattern: StringType, searchOption: SearchOption) -> ArrayType[StringType]: ...
    
    @staticmethod
    @overload
    def GetDirectories(path: StringType) -> ArrayType[StringType]: ...
    
    @staticmethod
    def GetDirectoryRoot(path: StringType) -> StringType: ...
    
    @staticmethod
    @overload
    def GetFileSystemEntries(path: StringType, searchPattern: StringType) -> ArrayType[StringType]: ...
    
    @staticmethod
    @overload
    def GetFileSystemEntries(path: StringType, searchPattern: StringType, searchOption: SearchOption) -> ArrayType[StringType]: ...
    
    @staticmethod
    @overload
    def GetFileSystemEntries(path: StringType) -> ArrayType[StringType]: ...
    
    @staticmethod
    @overload
    def GetFiles(path: StringType, searchPattern: StringType) -> ArrayType[StringType]: ...
    
    @staticmethod
    @overload
    def GetFiles(path: StringType, searchPattern: StringType, searchOption: SearchOption) -> ArrayType[StringType]: ...
    
    @staticmethod
    @overload
    def GetFiles(path: StringType) -> ArrayType[StringType]: ...
    
    @staticmethod
    def GetLastAccessTime(path: StringType) -> DateTime: ...
    
    @staticmethod
    def GetLastAccessTimeUtc(path: StringType) -> DateTime: ...
    
    @staticmethod
    def GetLastWriteTime(path: StringType) -> DateTime: ...
    
    @staticmethod
    def GetLastWriteTimeUtc(path: StringType) -> DateTime: ...
    
    @staticmethod
    def GetLogicalDrives() -> ArrayType[StringType]: ...
    
    @staticmethod
    def GetParent(path: StringType) -> DirectoryInfo: ...
    
    @staticmethod
    def Move(sourceDirName: StringType, destDirName: StringType) -> VoidType: ...
    
    @staticmethod
    def SetAccessControl(path: StringType, directorySecurity: DirectorySecurity) -> VoidType: ...
    
    @staticmethod
    def SetCreationTime(path: StringType, creationTime: DateTime) -> VoidType: ...
    
    @staticmethod
    def SetCreationTimeUtc(path: StringType, creationTimeUtc: DateTime) -> VoidType: ...
    
    @staticmethod
    def SetCurrentDirectory(path: StringType) -> VoidType: ...
    
    @staticmethod
    def SetLastAccessTime(path: StringType, lastAccessTime: DateTime) -> VoidType: ...
    
    @staticmethod
    def SetLastAccessTimeUtc(path: StringType, lastAccessTimeUtc: DateTime) -> VoidType: ...
    
    @staticmethod
    def SetLastWriteTime(path: StringType, lastWriteTime: DateTime) -> VoidType: ...
    
    @staticmethod
    def SetLastWriteTimeUtc(path: StringType, lastWriteTimeUtc: DateTime) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DirectoryInfo(FileSystemInfo, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, path: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Exists(self) -> BooleanType: ...
    
    @property
    def FullName(self) -> StringType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def Parent(self) -> DirectoryInfo: ...
    
    @property
    def Root(self) -> DirectoryInfo: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Create(self) -> VoidType: ...
    
    @overload
    def Create(self, directorySecurity: DirectorySecurity) -> VoidType: ...
    
    @overload
    def CreateSubdirectory(self, path: StringType) -> DirectoryInfo: ...
    
    @overload
    def CreateSubdirectory(self, path: StringType, directorySecurity: DirectorySecurity) -> DirectoryInfo: ...
    
    @overload
    def Delete(self) -> VoidType: ...
    
    @overload
    def Delete(self, recursive: BooleanType) -> VoidType: ...
    
    @overload
    def EnumerateDirectories(self) -> IEnumerable[DirectoryInfo]: ...
    
    @overload
    def EnumerateDirectories(self, searchPattern: StringType) -> IEnumerable[DirectoryInfo]: ...
    
    @overload
    def EnumerateDirectories(self, searchPattern: StringType, searchOption: SearchOption) -> IEnumerable[DirectoryInfo]: ...
    
    @overload
    def EnumerateFileSystemInfos(self) -> IEnumerable[FileSystemInfo]: ...
    
    @overload
    def EnumerateFileSystemInfos(self, searchPattern: StringType) -> IEnumerable[FileSystemInfo]: ...
    
    @overload
    def EnumerateFileSystemInfos(self, searchPattern: StringType, searchOption: SearchOption) -> IEnumerable[FileSystemInfo]: ...
    
    @overload
    def EnumerateFiles(self) -> IEnumerable[FileInfo]: ...
    
    @overload
    def EnumerateFiles(self, searchPattern: StringType) -> IEnumerable[FileInfo]: ...
    
    @overload
    def EnumerateFiles(self, searchPattern: StringType, searchOption: SearchOption) -> IEnumerable[FileInfo]: ...
    
    @overload
    def GetAccessControl(self) -> DirectorySecurity: ...
    
    @overload
    def GetAccessControl(self, includeSections: AccessControlSections) -> DirectorySecurity: ...
    
    @overload
    def GetDirectories(self) -> ArrayType[DirectoryInfo]: ...
    
    @overload
    def GetDirectories(self, searchPattern: StringType) -> ArrayType[DirectoryInfo]: ...
    
    @overload
    def GetDirectories(self, searchPattern: StringType, searchOption: SearchOption) -> ArrayType[DirectoryInfo]: ...
    
    @overload
    def GetFileSystemInfos(self, searchPattern: StringType) -> ArrayType[FileSystemInfo]: ...
    
    @overload
    def GetFileSystemInfos(self, searchPattern: StringType, searchOption: SearchOption) -> ArrayType[FileSystemInfo]: ...
    
    @overload
    def GetFileSystemInfos(self) -> ArrayType[FileSystemInfo]: ...
    
    @overload
    def GetFiles(self, searchPattern: StringType) -> ArrayType[FileInfo]: ...
    
    @overload
    def GetFiles(self, searchPattern: StringType, searchOption: SearchOption) -> ArrayType[FileInfo]: ...
    
    @overload
    def GetFiles(self) -> ArrayType[FileInfo]: ...
    
    def MoveTo(self, destDirName: StringType) -> VoidType: ...
    
    def SetAccessControl(self, directorySecurity: DirectorySecurity) -> VoidType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Exists(self) -> BooleanType: ...
    
    def get_FullName(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_Parent(self) -> DirectoryInfo: ...
    
    def get_Root(self) -> DirectoryInfo: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DirectoryInfoResultHandler(SearchResultHandler[DirectoryInfo]):
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


class DirectoryNotFoundException(IOException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DriveInfo(ObjectType, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, driveName: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AvailableFreeSpace(self) -> LongType: ...
    
    @property
    def DriveFormat(self) -> StringType: ...
    
    @property
    def DriveType(self) -> DriveType: ...
    
    @property
    def IsReady(self) -> BooleanType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def RootDirectory(self) -> DirectoryInfo: ...
    
    @property
    def TotalFreeSpace(self) -> LongType: ...
    
    @property
    def TotalSize(self) -> LongType: ...
    
    @property
    def VolumeLabel(self) -> StringType: ...
    
    @VolumeLabel.setter
    def VolumeLabel(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def GetDrives() -> ArrayType[DriveInfo]: ...
    
    def ToString(self) -> StringType: ...
    
    def get_AvailableFreeSpace(self) -> LongType: ...
    
    def get_DriveFormat(self) -> StringType: ...
    
    def get_DriveType(self) -> DriveType: ...
    
    def get_IsReady(self) -> BooleanType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_RootDirectory(self) -> DirectoryInfo: ...
    
    def get_TotalFreeSpace(self) -> LongType: ...
    
    def get_TotalSize(self) -> LongType: ...
    
    def get_VolumeLabel(self) -> StringType: ...
    
    def set_VolumeLabel(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DriveNotFoundException(IOException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EndOfStreamException(IOException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class File(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    @overload
    def AppendAllLines(path: StringType, contents: IEnumerable[StringType]) -> VoidType: ...
    
    @staticmethod
    @overload
    def AppendAllLines(path: StringType, contents: IEnumerable[StringType], encoding: Encoding) -> VoidType: ...
    
    @staticmethod
    @overload
    def AppendAllText(path: StringType, contents: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def AppendAllText(path: StringType, contents: StringType, encoding: Encoding) -> VoidType: ...
    
    @staticmethod
    def AppendText(path: StringType) -> StreamWriter: ...
    
    @staticmethod
    @overload
    def Copy(sourceFileName: StringType, destFileName: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Copy(sourceFileName: StringType, destFileName: StringType, overwrite: BooleanType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Create(path: StringType) -> FileStream: ...
    
    @staticmethod
    @overload
    def Create(path: StringType, bufferSize: IntType) -> FileStream: ...
    
    @staticmethod
    @overload
    def Create(path: StringType, bufferSize: IntType, options: FileOptions) -> FileStream: ...
    
    @staticmethod
    @overload
    def Create(path: StringType, bufferSize: IntType, options: FileOptions, fileSecurity: FileSecurity) -> FileStream: ...
    
    @staticmethod
    def CreateText(path: StringType) -> StreamWriter: ...
    
    @staticmethod
    def Decrypt(path: StringType) -> VoidType: ...
    
    @staticmethod
    def Delete(path: StringType) -> VoidType: ...
    
    @staticmethod
    def Encrypt(path: StringType) -> VoidType: ...
    
    @staticmethod
    def Exists(path: StringType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def GetAccessControl(path: StringType) -> FileSecurity: ...
    
    @staticmethod
    @overload
    def GetAccessControl(path: StringType, includeSections: AccessControlSections) -> FileSecurity: ...
    
    @staticmethod
    def GetAttributes(path: StringType) -> FileAttributes: ...
    
    @staticmethod
    def GetCreationTime(path: StringType) -> DateTime: ...
    
    @staticmethod
    def GetCreationTimeUtc(path: StringType) -> DateTime: ...
    
    @staticmethod
    def GetLastAccessTime(path: StringType) -> DateTime: ...
    
    @staticmethod
    def GetLastAccessTimeUtc(path: StringType) -> DateTime: ...
    
    @staticmethod
    def GetLastWriteTime(path: StringType) -> DateTime: ...
    
    @staticmethod
    def GetLastWriteTimeUtc(path: StringType) -> DateTime: ...
    
    @staticmethod
    def Move(sourceFileName: StringType, destFileName: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Open(path: StringType, mode: FileMode) -> FileStream: ...
    
    @staticmethod
    @overload
    def Open(path: StringType, mode: FileMode, access: FileAccess) -> FileStream: ...
    
    @staticmethod
    @overload
    def Open(path: StringType, mode: FileMode, access: FileAccess, share: FileShare) -> FileStream: ...
    
    @staticmethod
    def OpenRead(path: StringType) -> FileStream: ...
    
    @staticmethod
    def OpenText(path: StringType) -> StreamReader: ...
    
    @staticmethod
    def OpenWrite(path: StringType) -> FileStream: ...
    
    @staticmethod
    def ReadAllBytes(path: StringType) -> ArrayType[ByteType]: ...
    
    @staticmethod
    @overload
    def ReadAllLines(path: StringType) -> ArrayType[StringType]: ...
    
    @staticmethod
    @overload
    def ReadAllLines(path: StringType, encoding: Encoding) -> ArrayType[StringType]: ...
    
    @staticmethod
    @overload
    def ReadAllText(path: StringType) -> StringType: ...
    
    @staticmethod
    @overload
    def ReadAllText(path: StringType, encoding: Encoding) -> StringType: ...
    
    @staticmethod
    @overload
    def ReadLines(path: StringType) -> IEnumerable[StringType]: ...
    
    @staticmethod
    @overload
    def ReadLines(path: StringType, encoding: Encoding) -> IEnumerable[StringType]: ...
    
    @staticmethod
    @overload
    def Replace(sourceFileName: StringType, destinationFileName: StringType, destinationBackupFileName: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Replace(sourceFileName: StringType, destinationFileName: StringType, destinationBackupFileName: StringType, ignoreMetadataErrors: BooleanType) -> VoidType: ...
    
    @staticmethod
    def SetAccessControl(path: StringType, fileSecurity: FileSecurity) -> VoidType: ...
    
    @staticmethod
    def SetAttributes(path: StringType, fileAttributes: FileAttributes) -> VoidType: ...
    
    @staticmethod
    def SetCreationTime(path: StringType, creationTime: DateTime) -> VoidType: ...
    
    @staticmethod
    def SetCreationTimeUtc(path: StringType, creationTimeUtc: DateTime) -> VoidType: ...
    
    @staticmethod
    def SetLastAccessTime(path: StringType, lastAccessTime: DateTime) -> VoidType: ...
    
    @staticmethod
    def SetLastAccessTimeUtc(path: StringType, lastAccessTimeUtc: DateTime) -> VoidType: ...
    
    @staticmethod
    def SetLastWriteTime(path: StringType, lastWriteTime: DateTime) -> VoidType: ...
    
    @staticmethod
    def SetLastWriteTimeUtc(path: StringType, lastWriteTimeUtc: DateTime) -> VoidType: ...
    
    @staticmethod
    def WriteAllBytes(path: StringType, bytes: ArrayType[ByteType]) -> VoidType: ...
    
    @staticmethod
    @overload
    def WriteAllLines(path: StringType, contents: ArrayType[StringType]) -> VoidType: ...
    
    @staticmethod
    @overload
    def WriteAllLines(path: StringType, contents: ArrayType[StringType], encoding: Encoding) -> VoidType: ...
    
    @staticmethod
    @overload
    def WriteAllLines(path: StringType, contents: IEnumerable[StringType]) -> VoidType: ...
    
    @staticmethod
    @overload
    def WriteAllLines(path: StringType, contents: IEnumerable[StringType], encoding: Encoding) -> VoidType: ...
    
    @staticmethod
    @overload
    def WriteAllText(path: StringType, contents: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def WriteAllText(path: StringType, contents: StringType, encoding: Encoding) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class FileInfo(FileSystemInfo, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, fileName: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Directory(self) -> DirectoryInfo: ...
    
    @property
    def DirectoryName(self) -> StringType: ...
    
    @property
    def Exists(self) -> BooleanType: ...
    
    @property
    def IsReadOnly(self) -> BooleanType: ...
    
    @IsReadOnly.setter
    def IsReadOnly(self, value: BooleanType) -> None: ...
    
    @property
    def Length(self) -> LongType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def AppendText(self) -> StreamWriter: ...
    
    @overload
    def CopyTo(self, destFileName: StringType) -> FileInfo: ...
    
    @overload
    def CopyTo(self, destFileName: StringType, overwrite: BooleanType) -> FileInfo: ...
    
    def Create(self) -> FileStream: ...
    
    def CreateText(self) -> StreamWriter: ...
    
    def Decrypt(self) -> VoidType: ...
    
    def Delete(self) -> VoidType: ...
    
    def Encrypt(self) -> VoidType: ...
    
    @overload
    def GetAccessControl(self) -> FileSecurity: ...
    
    @overload
    def GetAccessControl(self, includeSections: AccessControlSections) -> FileSecurity: ...
    
    def MoveTo(self, destFileName: StringType) -> VoidType: ...
    
    @overload
    def Open(self, mode: FileMode) -> FileStream: ...
    
    @overload
    def Open(self, mode: FileMode, access: FileAccess) -> FileStream: ...
    
    @overload
    def Open(self, mode: FileMode, access: FileAccess, share: FileShare) -> FileStream: ...
    
    def OpenRead(self) -> FileStream: ...
    
    def OpenText(self) -> StreamReader: ...
    
    def OpenWrite(self) -> FileStream: ...
    
    @overload
    def Replace(self, destinationFileName: StringType, destinationBackupFileName: StringType) -> FileInfo: ...
    
    @overload
    def Replace(self, destinationFileName: StringType, destinationBackupFileName: StringType, ignoreMetadataErrors: BooleanType) -> FileInfo: ...
    
    def SetAccessControl(self, fileSecurity: FileSecurity) -> VoidType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Directory(self) -> DirectoryInfo: ...
    
    def get_DirectoryName(self) -> StringType: ...
    
    def get_Exists(self) -> BooleanType: ...
    
    def get_IsReadOnly(self) -> BooleanType: ...
    
    def get_Length(self) -> LongType: ...
    
    def get_Name(self) -> StringType: ...
    
    def set_IsReadOnly(self, value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class FileInfoResultHandler(SearchResultHandler[FileInfo]):
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


class FileLoadException(IOException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, inner: Exception): ...
    
    @overload
    def __init__(self, message: StringType, fileName: StringType): ...
    
    @overload
    def __init__(self, message: StringType, fileName: StringType, inner: Exception): ...
    
    # ---------- Properties ---------- #
    
    @property
    def FileName(self) -> StringType: ...
    
    @property
    def FusionLog(self) -> StringType: ...
    
    @property
    def Message(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_FileName(self) -> StringType: ...
    
    def get_FusionLog(self) -> StringType: ...
    
    def get_Message(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class FileNotFoundException(IOException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    @overload
    def __init__(self, message: StringType, fileName: StringType): ...
    
    @overload
    def __init__(self, message: StringType, fileName: StringType, innerException: Exception): ...
    
    # ---------- Properties ---------- #
    
    @property
    def FileName(self) -> StringType: ...
    
    @property
    def FusionLog(self) -> StringType: ...
    
    @property
    def Message(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_FileName(self) -> StringType: ...
    
    def get_FusionLog(self) -> StringType: ...
    
    def get_Message(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class FileStream(Stream, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, path: StringType, mode: FileMode): ...
    
    @overload
    def __init__(self, path: StringType, mode: FileMode, access: FileAccess): ...
    
    @overload
    def __init__(self, path: StringType, mode: FileMode, access: FileAccess, share: FileShare): ...
    
    @overload
    def __init__(self, path: StringType, mode: FileMode, access: FileAccess, share: FileShare, bufferSize: IntType): ...
    
    @overload
    def __init__(self, path: StringType, mode: FileMode, access: FileAccess, share: FileShare, bufferSize: IntType, options: FileOptions): ...
    
    @overload
    def __init__(self, path: StringType, mode: FileMode, access: FileAccess, share: FileShare, bufferSize: IntType, useAsync: BooleanType): ...
    
    @overload
    def __init__(self, path: StringType, mode: FileMode, rights: FileSystemRights, share: FileShare, bufferSize: IntType, options: FileOptions, fileSecurity: FileSecurity): ...
    
    @overload
    def __init__(self, path: StringType, mode: FileMode, rights: FileSystemRights, share: FileShare, bufferSize: IntType, options: FileOptions): ...
    
    @overload
    def __init__(self, handle: NIntType, access: FileAccess): ...
    
    @overload
    def __init__(self, handle: NIntType, access: FileAccess, ownsHandle: BooleanType): ...
    
    @overload
    def __init__(self, handle: NIntType, access: FileAccess, ownsHandle: BooleanType, bufferSize: IntType): ...
    
    @overload
    def __init__(self, handle: NIntType, access: FileAccess, ownsHandle: BooleanType, bufferSize: IntType, isAsync: BooleanType): ...
    
    @overload
    def __init__(self, handle: SafeFileHandle, access: FileAccess): ...
    
    @overload
    def __init__(self, handle: SafeFileHandle, access: FileAccess, bufferSize: IntType): ...
    
    @overload
    def __init__(self, handle: SafeFileHandle, access: FileAccess, bufferSize: IntType, isAsync: BooleanType): ...
    
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
    def Name(self) -> StringType: ...
    
    @property
    def Position(self) -> LongType: ...
    
    @Position.setter
    def Position(self, value: LongType) -> None: ...
    
    @property
    def SafeFileHandle(self) -> SafeFileHandle: ...
    
    # ---------- Methods ---------- #
    
    def BeginRead(self, array: ArrayType[ByteType], offset: IntType, numBytes: IntType, userCallback: AsyncCallback, stateObject: ObjectType) -> IAsyncResult: ...
    
    def BeginWrite(self, array: ArrayType[ByteType], offset: IntType, numBytes: IntType, userCallback: AsyncCallback, stateObject: ObjectType) -> IAsyncResult: ...
    
    def EndRead(self, asyncResult: IAsyncResult) -> IntType: ...
    
    def EndWrite(self, asyncResult: IAsyncResult) -> VoidType: ...
    
    @overload
    def Flush(self) -> VoidType: ...
    
    @overload
    def Flush(self, flushToDisk: BooleanType) -> VoidType: ...
    
    @overload
    def FlushAsync(self, cancellationToken: CancellationToken) -> Task: ...
    
    def GetAccessControl(self) -> FileSecurity: ...
    
    def Lock(self, position: LongType, length: LongType) -> VoidType: ...
    
    def Read(self, array: ArrayType[ByteType], offset: IntType, count: IntType) -> Tuple[IntType, ArrayType[ByteType]]: ...
    
    @overload
    def ReadAsync(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType, cancellationToken: CancellationToken) -> Task[IntType]: ...
    
    def ReadByte(self) -> IntType: ...
    
    def Seek(self, offset: LongType, origin: SeekOrigin) -> LongType: ...
    
    def SetAccessControl(self, fileSecurity: FileSecurity) -> VoidType: ...
    
    def SetLength(self, value: LongType) -> VoidType: ...
    
    def Unlock(self, position: LongType, length: LongType) -> VoidType: ...
    
    def Write(self, array: ArrayType[ByteType], offset: IntType, count: IntType) -> VoidType: ...
    
    @overload
    def WriteAsync(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType, cancellationToken: CancellationToken) -> Task: ...
    
    def WriteByte(self, value: ByteType) -> VoidType: ...
    
    def get_CanRead(self) -> BooleanType: ...
    
    def get_CanSeek(self) -> BooleanType: ...
    
    def get_CanWrite(self) -> BooleanType: ...
    
    def get_Handle(self) -> NIntType: ...
    
    def get_IsAsync(self) -> BooleanType: ...
    
    def get_Length(self) -> LongType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_Position(self) -> LongType: ...
    
    def get_SafeFileHandle(self) -> SafeFileHandle: ...
    
    def set_Position(self, value: LongType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class FileStreamAsyncResult(ObjectType, IAsyncResult):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def AsyncState(self) -> ObjectType: ...
    
    @property
    def AsyncWaitHandle(self) -> WaitHandle: ...
    
    @property
    def CompletedSynchronously(self) -> BooleanType: ...
    
    @property
    def IsCompleted(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def get_AsyncState(self) -> ObjectType: ...
    
    def get_AsyncWaitHandle(self) -> WaitHandle: ...
    
    def get_CompletedSynchronously(self) -> BooleanType: ...
    
    def get_IsCompleted(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class FileSystemEnumerableFactory(ABC, ObjectType):
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


class FileSystemEnumerableIterator(Generic[TSource], Iterator[TSource], IEnumerable[TSource], IEnumerable, IEnumerator[TSource], IDisposable, IEnumerator):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def MoveNext(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class FileSystemInfo(ABC, MarshalByRefObject, ISerializable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Attributes(self) -> FileAttributes: ...
    
    @Attributes.setter
    def Attributes(self, value: FileAttributes) -> None: ...
    
    @property
    def CreationTime(self) -> DateTime: ...
    
    @CreationTime.setter
    def CreationTime(self, value: DateTime) -> None: ...
    
    @property
    def CreationTimeUtc(self) -> DateTime: ...
    
    @CreationTimeUtc.setter
    def CreationTimeUtc(self, value: DateTime) -> None: ...
    
    @property
    def Exists(self) -> BooleanType: ...
    
    @property
    def Extension(self) -> StringType: ...
    
    @property
    def FullName(self) -> StringType: ...
    
    @property
    def LastAccessTime(self) -> DateTime: ...
    
    @LastAccessTime.setter
    def LastAccessTime(self, value: DateTime) -> None: ...
    
    @property
    def LastAccessTimeUtc(self) -> DateTime: ...
    
    @LastAccessTimeUtc.setter
    def LastAccessTimeUtc(self, value: DateTime) -> None: ...
    
    @property
    def LastWriteTime(self) -> DateTime: ...
    
    @LastWriteTime.setter
    def LastWriteTime(self, value: DateTime) -> None: ...
    
    @property
    def LastWriteTimeUtc(self) -> DateTime: ...
    
    @LastWriteTimeUtc.setter
    def LastWriteTimeUtc(self, value: DateTime) -> None: ...
    
    @property
    def Name(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def Delete(self) -> VoidType: ...
    
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    
    def Refresh(self) -> VoidType: ...
    
    def get_Attributes(self) -> FileAttributes: ...
    
    def get_CreationTime(self) -> DateTime: ...
    
    def get_CreationTimeUtc(self) -> DateTime: ...
    
    def get_Exists(self) -> BooleanType: ...
    
    def get_Extension(self) -> StringType: ...
    
    def get_FullName(self) -> StringType: ...
    
    def get_LastAccessTime(self) -> DateTime: ...
    
    def get_LastAccessTimeUtc(self) -> DateTime: ...
    
    def get_LastWriteTime(self) -> DateTime: ...
    
    def get_LastWriteTimeUtc(self) -> DateTime: ...
    
    def get_Name(self) -> StringType: ...
    
    def set_Attributes(self, value: FileAttributes) -> VoidType: ...
    
    def set_CreationTime(self, value: DateTime) -> VoidType: ...
    
    def set_CreationTimeUtc(self, value: DateTime) -> VoidType: ...
    
    def set_LastAccessTime(self, value: DateTime) -> VoidType: ...
    
    def set_LastAccessTimeUtc(self, value: DateTime) -> VoidType: ...
    
    def set_LastWriteTime(self, value: DateTime) -> VoidType: ...
    
    def set_LastWriteTimeUtc(self, value: DateTime) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class FileSystemInfoResultHandler(SearchResultHandler[FileSystemInfo]):
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


class IOException(SystemException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, hresult: IntType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Iterator(Protocol[TSource], ObjectType, IEnumerable[TSource], IEnumerable, IEnumerator[TSource], IDisposable, IEnumerator):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Current(self) -> TSource: ...
    
    # ---------- Methods ---------- #
    
    def Dispose(self) -> VoidType: ...
    
    def GetEnumerator(self) -> IEnumerator[TSource]: ...
    
    def MoveNext(self) -> BooleanType: ...
    
    def get_Current(self) -> TSource: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class LongPath(ABC, ObjectType):
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


class LongPathDirectory(ABC, ObjectType):
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


class LongPathFile(ABC, ObjectType):
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


class LongPathHelper(ObjectType):
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


class MemoryStream(Stream, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, capacity: IntType): ...
    
    @overload
    def __init__(self, buffer: ArrayType[ByteType]): ...
    
    @overload
    def __init__(self, buffer: ArrayType[ByteType], writable: BooleanType): ...
    
    @overload
    def __init__(self, buffer: ArrayType[ByteType], index: IntType, count: IntType): ...
    
    @overload
    def __init__(self, buffer: ArrayType[ByteType], index: IntType, count: IntType, writable: BooleanType): ...
    
    @overload
    def __init__(self, buffer: ArrayType[ByteType], index: IntType, count: IntType, writable: BooleanType, publiclyVisible: BooleanType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CanRead(self) -> BooleanType: ...
    
    @property
    def CanSeek(self) -> BooleanType: ...
    
    @property
    def CanWrite(self) -> BooleanType: ...
    
    @property
    def Capacity(self) -> IntType: ...
    
    @Capacity.setter
    def Capacity(self, value: IntType) -> None: ...
    
    @property
    def Length(self) -> LongType: ...
    
    @property
    def Position(self) -> LongType: ...
    
    @Position.setter
    def Position(self, value: LongType) -> None: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def CopyToAsync(self, destination: Stream, bufferSize: IntType, cancellationToken: CancellationToken) -> Task: ...
    
    def Flush(self) -> VoidType: ...
    
    @overload
    def FlushAsync(self, cancellationToken: CancellationToken) -> Task: ...
    
    def GetBuffer(self) -> ArrayType[ByteType]: ...
    
    def Read(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType) -> Tuple[IntType, ArrayType[ByteType]]: ...
    
    @overload
    def ReadAsync(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType, cancellationToken: CancellationToken) -> Task[IntType]: ...
    
    def ReadByte(self) -> IntType: ...
    
    def Seek(self, offset: LongType, loc: SeekOrigin) -> LongType: ...
    
    def SetLength(self, value: LongType) -> VoidType: ...
    
    def ToArray(self) -> ArrayType[ByteType]: ...
    
    def TryGetBuffer(self, buffer: ArraySegment[ByteType]) -> Tuple[BooleanType, ArraySegment[ByteType]]: ...
    
    def Write(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType) -> VoidType: ...
    
    @overload
    def WriteAsync(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType, cancellationToken: CancellationToken) -> Task: ...
    
    def WriteByte(self, value: ByteType) -> VoidType: ...
    
    def WriteTo(self, stream: Stream) -> VoidType: ...
    
    def get_CanRead(self) -> BooleanType: ...
    
    def get_CanSeek(self) -> BooleanType: ...
    
    def get_CanWrite(self) -> BooleanType: ...
    
    def get_Capacity(self) -> IntType: ...
    
    def get_Length(self) -> LongType: ...
    
    def get_Position(self) -> LongType: ...
    
    def set_Capacity(self, value: IntType) -> VoidType: ...
    
    def set_Position(self, value: LongType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Path(ABC, ObjectType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def AltDirectorySeparatorChar() -> CharType: ...
    
    @staticmethod
    @property
    def DirectorySeparatorChar() -> CharType: ...
    
    @staticmethod
    @property
    def InvalidPathChars() -> ArrayType[CharType]: ...
    
    @staticmethod
    @property
    def PathSeparator() -> CharType: ...
    
    @staticmethod
    @property
    def VolumeSeparatorChar() -> CharType: ...
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def ChangeExtension(path: StringType, extension: StringType) -> StringType: ...
    
    @staticmethod
    @overload
    def Combine(paths: ArrayType[StringType]) -> StringType: ...
    
    @staticmethod
    @overload
    def Combine(path1: StringType, path2: StringType, path3: StringType) -> StringType: ...
    
    @staticmethod
    @overload
    def Combine(path1: StringType, path2: StringType, path3: StringType, path4: StringType) -> StringType: ...
    
    @staticmethod
    @overload
    def Combine(path1: StringType, path2: StringType) -> StringType: ...
    
    @staticmethod
    def GetDirectoryName(path: StringType) -> StringType: ...
    
    @staticmethod
    def GetExtension(path: StringType) -> StringType: ...
    
    @staticmethod
    def GetFileName(path: StringType) -> StringType: ...
    
    @staticmethod
    def GetFileNameWithoutExtension(path: StringType) -> StringType: ...
    
    @staticmethod
    def GetFullPath(path: StringType) -> StringType: ...
    
    @staticmethod
    def GetInvalidFileNameChars() -> ArrayType[CharType]: ...
    
    @staticmethod
    def GetInvalidPathChars() -> ArrayType[CharType]: ...
    
    @staticmethod
    def GetPathRoot(path: StringType) -> StringType: ...
    
    @staticmethod
    def GetRandomFileName() -> StringType: ...
    
    @staticmethod
    def GetTempFileName() -> StringType: ...
    
    @staticmethod
    def GetTempPath() -> StringType: ...
    
    @staticmethod
    def HasExtension(path: StringType) -> BooleanType: ...
    
    @staticmethod
    def IsPathRooted(path: StringType) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PathInternal(ABC, ObjectType):
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


class PathTooLongException(IOException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PinnedBufferMemoryStream(UnmanagedMemoryStream, IDisposable):
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


class ReadLinesIterator(Iterator[StringType], IEnumerable[StringType], IEnumerable, IEnumerator[StringType], IDisposable, IEnumerator):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def MoveNext(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SearchResultHandler(Protocol[TSource], ObjectType):
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


class Stream(ABC, MarshalByRefObject, IDisposable):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Null() -> Stream: ...
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def CanRead(self) -> BooleanType: ...
    
    @property
    def CanSeek(self) -> BooleanType: ...
    
    @property
    def CanTimeout(self) -> BooleanType: ...
    
    @property
    def CanWrite(self) -> BooleanType: ...
    
    @property
    def Length(self) -> LongType: ...
    
    @property
    def Position(self) -> LongType: ...
    
    @Position.setter
    def Position(self, value: LongType) -> None: ...
    
    @property
    def ReadTimeout(self) -> IntType: ...
    
    @ReadTimeout.setter
    def ReadTimeout(self, value: IntType) -> None: ...
    
    @property
    def WriteTimeout(self) -> IntType: ...
    
    @WriteTimeout.setter
    def WriteTimeout(self, value: IntType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def BeginRead(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType, callback: AsyncCallback, state: ObjectType) -> IAsyncResult: ...
    
    def BeginWrite(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType, callback: AsyncCallback, state: ObjectType) -> IAsyncResult: ...
    
    def Close(self) -> VoidType: ...
    
    @overload
    def CopyTo(self, destination: Stream) -> VoidType: ...
    
    @overload
    def CopyTo(self, destination: Stream, bufferSize: IntType) -> VoidType: ...
    
    @overload
    def CopyToAsync(self, destination: Stream, bufferSize: IntType, cancellationToken: CancellationToken) -> Task: ...
    
    @overload
    def CopyToAsync(self, destination: Stream) -> Task: ...
    
    @overload
    def CopyToAsync(self, destination: Stream, bufferSize: IntType) -> Task: ...
    
    def Dispose(self) -> VoidType: ...
    
    def EndRead(self, asyncResult: IAsyncResult) -> IntType: ...
    
    def EndWrite(self, asyncResult: IAsyncResult) -> VoidType: ...
    
    def Flush(self) -> VoidType: ...
    
    @overload
    def FlushAsync(self) -> Task: ...
    
    @overload
    def FlushAsync(self, cancellationToken: CancellationToken) -> Task: ...
    
    def Read(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType) -> Tuple[IntType, ArrayType[ByteType]]: ...
    
    @overload
    def ReadAsync(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType, cancellationToken: CancellationToken) -> Task[IntType]: ...
    
    @overload
    def ReadAsync(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType) -> Task[IntType]: ...
    
    def ReadByte(self) -> IntType: ...
    
    def Seek(self, offset: LongType, origin: SeekOrigin) -> LongType: ...
    
    def SetLength(self, value: LongType) -> VoidType: ...
    
    @staticmethod
    def Synchronized(stream: Stream) -> Stream: ...
    
    def Write(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType) -> VoidType: ...
    
    @overload
    def WriteAsync(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType, cancellationToken: CancellationToken) -> Task: ...
    
    @overload
    def WriteAsync(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType) -> Task: ...
    
    def WriteByte(self, value: ByteType) -> VoidType: ...
    
    def get_CanRead(self) -> BooleanType: ...
    
    def get_CanSeek(self) -> BooleanType: ...
    
    def get_CanTimeout(self) -> BooleanType: ...
    
    def get_CanWrite(self) -> BooleanType: ...
    
    def get_Length(self) -> LongType: ...
    
    def get_Position(self) -> LongType: ...
    
    def get_ReadTimeout(self) -> IntType: ...
    
    def get_WriteTimeout(self) -> IntType: ...
    
    def set_Position(self, value: LongType) -> VoidType: ...
    
    def set_ReadTimeout(self, value: IntType) -> VoidType: ...
    
    def set_WriteTimeout(self, value: IntType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class StreamReader(TextReader, IDisposable):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Null() -> StreamReader: ...
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, stream: Stream): ...
    
    @overload
    def __init__(self, stream: Stream, detectEncodingFromByteOrderMarks: BooleanType): ...
    
    @overload
    def __init__(self, stream: Stream, encoding: Encoding): ...
    
    @overload
    def __init__(self, stream: Stream, encoding: Encoding, detectEncodingFromByteOrderMarks: BooleanType): ...
    
    @overload
    def __init__(self, stream: Stream, encoding: Encoding, detectEncodingFromByteOrderMarks: BooleanType, bufferSize: IntType): ...
    
    @overload
    def __init__(self, stream: Stream, encoding: Encoding, detectEncodingFromByteOrderMarks: BooleanType, bufferSize: IntType, leaveOpen: BooleanType): ...
    
    @overload
    def __init__(self, path: StringType): ...
    
    @overload
    def __init__(self, path: StringType, detectEncodingFromByteOrderMarks: BooleanType): ...
    
    @overload
    def __init__(self, path: StringType, encoding: Encoding): ...
    
    @overload
    def __init__(self, path: StringType, encoding: Encoding, detectEncodingFromByteOrderMarks: BooleanType): ...
    
    @overload
    def __init__(self, path: StringType, encoding: Encoding, detectEncodingFromByteOrderMarks: BooleanType, bufferSize: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def BaseStream(self) -> Stream: ...
    
    @property
    def CurrentEncoding(self) -> Encoding: ...
    
    @property
    def EndOfStream(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    def DiscardBufferedData(self) -> VoidType: ...
    
    def Peek(self) -> IntType: ...
    
    @overload
    def Read(self) -> IntType: ...
    
    @overload
    def Read(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> Tuple[IntType, ArrayType[CharType]]: ...
    
    def ReadAsync(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> Task[IntType]: ...
    
    def ReadBlock(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> Tuple[IntType, ArrayType[CharType]]: ...
    
    def ReadBlockAsync(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> Task[IntType]: ...
    
    def ReadLine(self) -> StringType: ...
    
    def ReadLineAsync(self) -> Task[StringType]: ...
    
    def ReadToEnd(self) -> StringType: ...
    
    def ReadToEndAsync(self) -> Task[StringType]: ...
    
    def get_BaseStream(self) -> Stream: ...
    
    def get_CurrentEncoding(self) -> Encoding: ...
    
    def get_EndOfStream(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class StreamWriter(TextWriter, IDisposable):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Null() -> StreamWriter: ...
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, stream: Stream): ...
    
    @overload
    def __init__(self, stream: Stream, encoding: Encoding): ...
    
    @overload
    def __init__(self, stream: Stream, encoding: Encoding, bufferSize: IntType): ...
    
    @overload
    def __init__(self, stream: Stream, encoding: Encoding, bufferSize: IntType, leaveOpen: BooleanType): ...
    
    @overload
    def __init__(self, path: StringType): ...
    
    @overload
    def __init__(self, path: StringType, append: BooleanType): ...
    
    @overload
    def __init__(self, path: StringType, append: BooleanType, encoding: Encoding): ...
    
    @overload
    def __init__(self, path: StringType, append: BooleanType, encoding: Encoding, bufferSize: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AutoFlush(self) -> BooleanType: ...
    
    @AutoFlush.setter
    def AutoFlush(self, value: BooleanType) -> None: ...
    
    @property
    def BaseStream(self) -> Stream: ...
    
    @property
    def Encoding(self) -> Encoding: ...
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    def Flush(self) -> VoidType: ...
    
    def FlushAsync(self) -> Task: ...
    
    @overload
    def Write(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> VoidType: ...
    
    @overload
    def Write(self, value: CharType) -> VoidType: ...
    
    @overload
    def Write(self, buffer: ArrayType[CharType]) -> VoidType: ...
    
    @overload
    def Write(self, value: StringType) -> VoidType: ...
    
    @overload
    def WriteAsync(self, value: CharType) -> Task: ...
    
    @overload
    def WriteAsync(self, value: StringType) -> Task: ...
    
    @overload
    def WriteAsync(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> Task: ...
    
    @overload
    def WriteLineAsync(self) -> Task: ...
    
    @overload
    def WriteLineAsync(self, value: CharType) -> Task: ...
    
    @overload
    def WriteLineAsync(self, value: StringType) -> Task: ...
    
    @overload
    def WriteLineAsync(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> Task: ...
    
    def get_AutoFlush(self) -> BooleanType: ...
    
    def get_BaseStream(self) -> Stream: ...
    
    def get_Encoding(self) -> Encoding: ...
    
    def set_AutoFlush(self, value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class StringReader(TextReader, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, s: StringType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    def Peek(self) -> IntType: ...
    
    @overload
    def Read(self) -> IntType: ...
    
    @overload
    def Read(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> Tuple[IntType, ArrayType[CharType]]: ...
    
    def ReadAsync(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> Task[IntType]: ...
    
    def ReadBlockAsync(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> Task[IntType]: ...
    
    def ReadLine(self) -> StringType: ...
    
    def ReadLineAsync(self) -> Task[StringType]: ...
    
    def ReadToEnd(self) -> StringType: ...
    
    def ReadToEndAsync(self) -> Task[StringType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class StringResultHandler(SearchResultHandler[StringType]):
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


class StringWriter(TextWriter, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, formatProvider: IFormatProvider): ...
    
    @overload
    def __init__(self, sb: StringBuilder): ...
    
    @overload
    def __init__(self, sb: StringBuilder, formatProvider: IFormatProvider): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Encoding(self) -> Encoding: ...
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    def FlushAsync(self) -> Task: ...
    
    def GetStringBuilder(self) -> StringBuilder: ...
    
    def ToString(self) -> StringType: ...
    
    @overload
    def Write(self, value: CharType) -> VoidType: ...
    
    @overload
    def Write(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> VoidType: ...
    
    @overload
    def Write(self, value: StringType) -> VoidType: ...
    
    @overload
    def WriteAsync(self, value: CharType) -> Task: ...
    
    @overload
    def WriteAsync(self, value: StringType) -> Task: ...
    
    @overload
    def WriteAsync(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> Task: ...
    
    @overload
    def WriteLineAsync(self, value: CharType) -> Task: ...
    
    @overload
    def WriteLineAsync(self, value: StringType) -> Task: ...
    
    @overload
    def WriteLineAsync(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> Task: ...
    
    def get_Encoding(self) -> Encoding: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TextReader(ABC, MarshalByRefObject, IDisposable):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Null() -> TextReader: ...
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    def Dispose(self) -> VoidType: ...
    
    def Peek(self) -> IntType: ...
    
    @overload
    def Read(self) -> IntType: ...
    
    @overload
    def Read(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> Tuple[IntType, ArrayType[CharType]]: ...
    
    def ReadAsync(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> Task[IntType]: ...
    
    def ReadBlock(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> Tuple[IntType, ArrayType[CharType]]: ...
    
    def ReadBlockAsync(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> Task[IntType]: ...
    
    def ReadLine(self) -> StringType: ...
    
    def ReadLineAsync(self) -> Task[StringType]: ...
    
    def ReadToEnd(self) -> StringType: ...
    
    def ReadToEndAsync(self) -> Task[StringType]: ...
    
    @staticmethod
    def Synchronized(reader: TextReader) -> TextReader: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TextWriter(ABC, MarshalByRefObject, IDisposable):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Null() -> TextWriter: ...
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Encoding(self) -> Encoding: ...
    
    @property
    def FormatProvider(self) -> IFormatProvider: ...
    
    @property
    def NewLine(self) -> StringType: ...
    
    @NewLine.setter
    def NewLine(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    def Dispose(self) -> VoidType: ...
    
    def Flush(self) -> VoidType: ...
    
    def FlushAsync(self) -> Task: ...
    
    @staticmethod
    def Synchronized(writer: TextWriter) -> TextWriter: ...
    
    @overload
    def Write(self, value: CharType) -> VoidType: ...
    
    @overload
    def Write(self, buffer: ArrayType[CharType]) -> VoidType: ...
    
    @overload
    def Write(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> VoidType: ...
    
    @overload
    def Write(self, value: IntType) -> VoidType: ...
    
    @overload
    def Write(self, value: UIntType) -> VoidType: ...
    
    @overload
    def Write(self, value: LongType) -> VoidType: ...
    
    @overload
    def Write(self, value: ULongType) -> VoidType: ...
    
    @overload
    def Write(self, value: FloatType) -> VoidType: ...
    
    @overload
    def Write(self, value: DoubleType) -> VoidType: ...
    
    @overload
    def Write(self, value: DecimalType) -> VoidType: ...
    
    @overload
    def Write(self, value: StringType) -> VoidType: ...
    
    @overload
    def Write(self, value: ObjectType) -> VoidType: ...
    
    @overload
    def Write(self, format: StringType, arg0: ObjectType) -> VoidType: ...
    
    @overload
    def Write(self, format: StringType, arg0: ObjectType, arg1: ObjectType) -> VoidType: ...
    
    @overload
    def Write(self, format: StringType, arg0: ObjectType, arg1: ObjectType, arg2: ObjectType) -> VoidType: ...
    
    @overload
    def Write(self, format: StringType, arg: ArrayType[ObjectType]) -> VoidType: ...
    
    @overload
    def Write(self, value: BooleanType) -> VoidType: ...
    
    @overload
    def WriteAsync(self, value: CharType) -> Task: ...
    
    @overload
    def WriteAsync(self, value: StringType) -> Task: ...
    
    @overload
    def WriteAsync(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> Task: ...
    
    @overload
    def WriteAsync(self, buffer: ArrayType[CharType]) -> Task: ...
    
    @overload
    def WriteLine(self) -> VoidType: ...
    
    @overload
    def WriteLine(self, value: CharType) -> VoidType: ...
    
    @overload
    def WriteLine(self, buffer: ArrayType[CharType]) -> VoidType: ...
    
    @overload
    def WriteLine(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> VoidType: ...
    
    @overload
    def WriteLine(self, value: BooleanType) -> VoidType: ...
    
    @overload
    def WriteLine(self, value: IntType) -> VoidType: ...
    
    @overload
    def WriteLine(self, value: UIntType) -> VoidType: ...
    
    @overload
    def WriteLine(self, value: LongType) -> VoidType: ...
    
    @overload
    def WriteLine(self, value: ULongType) -> VoidType: ...
    
    @overload
    def WriteLine(self, value: FloatType) -> VoidType: ...
    
    @overload
    def WriteLine(self, value: DoubleType) -> VoidType: ...
    
    @overload
    def WriteLine(self, value: DecimalType) -> VoidType: ...
    
    @overload
    def WriteLine(self, value: StringType) -> VoidType: ...
    
    @overload
    def WriteLine(self, value: ObjectType) -> VoidType: ...
    
    @overload
    def WriteLine(self, format: StringType, arg0: ObjectType) -> VoidType: ...
    
    @overload
    def WriteLine(self, format: StringType, arg0: ObjectType, arg1: ObjectType) -> VoidType: ...
    
    @overload
    def WriteLine(self, format: StringType, arg0: ObjectType, arg1: ObjectType, arg2: ObjectType) -> VoidType: ...
    
    @overload
    def WriteLine(self, format: StringType, arg: ArrayType[ObjectType]) -> VoidType: ...
    
    @overload
    def WriteLineAsync(self, value: CharType) -> Task: ...
    
    @overload
    def WriteLineAsync(self, value: StringType) -> Task: ...
    
    @overload
    def WriteLineAsync(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> Task: ...
    
    @overload
    def WriteLineAsync(self) -> Task: ...
    
    @overload
    def WriteLineAsync(self, buffer: ArrayType[CharType]) -> Task: ...
    
    def get_Encoding(self) -> Encoding: ...
    
    def get_FormatProvider(self) -> IFormatProvider: ...
    
    def get_NewLine(self) -> StringType: ...
    
    def set_NewLine(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UnmanagedMemoryAccessor(ObjectType, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, buffer: SafeBuffer, offset: LongType, capacity: LongType): ...
    
    @overload
    def __init__(self, buffer: SafeBuffer, offset: LongType, capacity: LongType, access: FileAccess): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CanRead(self) -> BooleanType: ...
    
    @property
    def CanWrite(self) -> BooleanType: ...
    
    @property
    def Capacity(self) -> LongType: ...
    
    # ---------- Methods ---------- #
    
    def Dispose(self) -> VoidType: ...
    
    def Read(self, position: LongType, structure: T) -> Tuple[VoidType, T]: ...
    
    def ReadArray(self, position: LongType, array: ArrayType[T], offset: IntType, count: IntType) -> IntType: ...
    
    def ReadBoolean(self, position: LongType) -> BooleanType: ...
    
    def ReadByte(self, position: LongType) -> ByteType: ...
    
    def ReadChar(self, position: LongType) -> CharType: ...
    
    def ReadDecimal(self, position: LongType) -> DecimalType: ...
    
    def ReadDouble(self, position: LongType) -> DoubleType: ...
    
    def ReadInt16(self, position: LongType) -> ShortType: ...
    
    def ReadInt32(self, position: LongType) -> IntType: ...
    
    def ReadInt64(self, position: LongType) -> LongType: ...
    
    def ReadSByte(self, position: LongType) -> SByteType: ...
    
    def ReadSingle(self, position: LongType) -> FloatType: ...
    
    def ReadUInt16(self, position: LongType) -> UShortType: ...
    
    def ReadUInt32(self, position: LongType) -> UIntType: ...
    
    def ReadUInt64(self, position: LongType) -> ULongType: ...
    
    @overload
    def Write(self, position: LongType, value: BooleanType) -> VoidType: ...
    
    @overload
    def Write(self, position: LongType, value: ByteType) -> VoidType: ...
    
    @overload
    def Write(self, position: LongType, value: DecimalType) -> VoidType: ...
    
    @overload
    def Write(self, position: LongType, value: CharType) -> VoidType: ...
    
    @overload
    def Write(self, position: LongType, value: ShortType) -> VoidType: ...
    
    @overload
    def Write(self, position: LongType, value: IntType) -> VoidType: ...
    
    @overload
    def Write(self, position: LongType, value: LongType) -> VoidType: ...
    
    @overload
    def Write(self, position: LongType, value: FloatType) -> VoidType: ...
    
    @overload
    def Write(self, position: LongType, value: DoubleType) -> VoidType: ...
    
    @overload
    def Write(self, position: LongType, value: SByteType) -> VoidType: ...
    
    @overload
    def Write(self, position: LongType, value: UShortType) -> VoidType: ...
    
    @overload
    def Write(self, position: LongType, value: UIntType) -> VoidType: ...
    
    @overload
    def Write(self, position: LongType, value: ULongType) -> VoidType: ...
    
    @overload
    def Write(self, position: LongType, structure: T) -> Tuple[VoidType, T]: ...
    
    def WriteArray(self, position: LongType, array: ArrayType[T], offset: IntType, count: IntType) -> VoidType: ...
    
    def get_CanRead(self) -> BooleanType: ...
    
    def get_CanWrite(self) -> BooleanType: ...
    
    def get_Capacity(self) -> LongType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UnmanagedMemoryStream(Stream, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, buffer: SafeBuffer, offset: LongType, length: LongType): ...
    
    @overload
    def __init__(self, buffer: SafeBuffer, offset: LongType, length: LongType, access: FileAccess): ...
    
    @overload
    def __init__(self, pointer: ByteType, length: LongType): ...
    
    @overload
    def __init__(self, pointer: ByteType, length: LongType, capacity: LongType, access: FileAccess): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CanRead(self) -> BooleanType: ...
    
    @property
    def CanSeek(self) -> BooleanType: ...
    
    @property
    def CanWrite(self) -> BooleanType: ...
    
    @property
    def Capacity(self) -> LongType: ...
    
    @property
    def Length(self) -> LongType: ...
    
    @property
    def Position(self) -> LongType: ...
    
    @Position.setter
    def Position(self, value: LongType) -> None: ...
    
    @property
    def PositionPointer(self) -> ByteType: ...
    
    @PositionPointer.setter
    def PositionPointer(self, value: ByteType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Flush(self) -> VoidType: ...
    
    @overload
    def FlushAsync(self, cancellationToken: CancellationToken) -> Task: ...
    
    def Read(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType) -> Tuple[IntType, ArrayType[ByteType]]: ...
    
    @overload
    def ReadAsync(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType, cancellationToken: CancellationToken) -> Task[IntType]: ...
    
    def ReadByte(self) -> IntType: ...
    
    def Seek(self, offset: LongType, loc: SeekOrigin) -> LongType: ...
    
    def SetLength(self, value: LongType) -> VoidType: ...
    
    def Write(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType) -> VoidType: ...
    
    @overload
    def WriteAsync(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType, cancellationToken: CancellationToken) -> Task: ...
    
    def WriteByte(self, value: ByteType) -> VoidType: ...
    
    def get_CanRead(self) -> BooleanType: ...
    
    def get_CanSeek(self) -> BooleanType: ...
    
    def get_CanWrite(self) -> BooleanType: ...
    
    def get_Capacity(self) -> LongType: ...
    
    def get_Length(self) -> LongType: ...
    
    def get_Position(self) -> LongType: ...
    
    def get_PositionPointer(self) -> ByteType: ...
    
    def set_Position(self, value: LongType) -> VoidType: ...
    
    def set_PositionPointer(self, value: ByteType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UnmanagedMemoryStreamWrapper(MemoryStream, IDisposable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def CanRead(self) -> BooleanType: ...
    
    @property
    def CanSeek(self) -> BooleanType: ...
    
    @property
    def CanWrite(self) -> BooleanType: ...
    
    @property
    def Capacity(self) -> IntType: ...
    
    @Capacity.setter
    def Capacity(self, value: IntType) -> None: ...
    
    @property
    def Length(self) -> LongType: ...
    
    @property
    def Position(self) -> LongType: ...
    
    @Position.setter
    def Position(self, value: LongType) -> None: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def CopyToAsync(self, destination: Stream, bufferSize: IntType, cancellationToken: CancellationToken) -> Task: ...
    
    def Flush(self) -> VoidType: ...
    
    @overload
    def FlushAsync(self, cancellationToken: CancellationToken) -> Task: ...
    
    def GetBuffer(self) -> ArrayType[ByteType]: ...
    
    def Read(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType) -> Tuple[IntType, ArrayType[ByteType]]: ...
    
    @overload
    def ReadAsync(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType, cancellationToken: CancellationToken) -> Task[IntType]: ...
    
    def ReadByte(self) -> IntType: ...
    
    def Seek(self, offset: LongType, loc: SeekOrigin) -> LongType: ...
    
    def SetLength(self, value: LongType) -> VoidType: ...
    
    def ToArray(self) -> ArrayType[ByteType]: ...
    
    def TryGetBuffer(self, buffer: ArraySegment[ByteType]) -> Tuple[BooleanType, ArraySegment[ByteType]]: ...
    
    def Write(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType) -> VoidType: ...
    
    @overload
    def WriteAsync(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType, cancellationToken: CancellationToken) -> Task: ...
    
    def WriteByte(self, value: ByteType) -> VoidType: ...
    
    def WriteTo(self, stream: Stream) -> VoidType: ...
    
    def get_CanRead(self) -> BooleanType: ...
    
    def get_CanSeek(self) -> BooleanType: ...
    
    def get_CanWrite(self) -> BooleanType: ...
    
    def get_Capacity(self) -> IntType: ...
    
    def get_Length(self) -> LongType: ...
    
    def get_Position(self) -> LongType: ...
    
    def set_Capacity(self, value: IntType) -> VoidType: ...
    
    def set_Position(self, value: LongType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class __ConsoleStream(Stream, IDisposable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def CanRead(self) -> BooleanType: ...
    
    @property
    def CanSeek(self) -> BooleanType: ...
    
    @property
    def CanWrite(self) -> BooleanType: ...
    
    @property
    def Length(self) -> LongType: ...
    
    @property
    def Position(self) -> LongType: ...
    
    @Position.setter
    def Position(self, value: LongType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Flush(self) -> VoidType: ...
    
    def Read(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType) -> Tuple[IntType, ArrayType[ByteType]]: ...
    
    def Seek(self, offset: LongType, origin: SeekOrigin) -> LongType: ...
    
    def SetLength(self, value: LongType) -> VoidType: ...
    
    def Write(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType) -> VoidType: ...
    
    def get_CanRead(self) -> BooleanType: ...
    
    def get_CanSeek(self) -> BooleanType: ...
    
    def get_CanWrite(self) -> BooleanType: ...
    
    def get_Length(self) -> LongType: ...
    
    def get_Position(self) -> LongType: ...
    
    def set_Position(self, value: LongType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class __Error(ABC, ObjectType):
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


class __HResults(ABC, ObjectType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def COR_E_DIRECTORYNOTFOUND() -> IntType: ...
    
    @staticmethod
    @property
    def COR_E_ENDOFSTREAM() -> IntType: ...
    
    @staticmethod
    @property
    def COR_E_FILELOAD() -> IntType: ...
    
    @staticmethod
    @property
    def COR_E_FILENOTFOUND() -> IntType: ...
    
    @staticmethod
    @property
    def COR_E_IO() -> IntType: ...
    
    @staticmethod
    @property
    def COR_E_PATHTOOLONG() -> IntType: ...
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# ---------- Structs ---------- #

class PathHelper(ValueType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def ToString(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# No Interfaces

# ---------- Enums ---------- #

class DriveType(Enum):
    Unknown: IntType = 0
    NoRootDirectory: IntType = 1
    Removable: IntType = 2
    Fixed: IntType = 3
    Network: IntType = 4
    CDRom: IntType = 5
    Ram: IntType = 6


class FileAccess(Enum):
    Read: IntType = 1
    Write: IntType = 2
    ReadWrite: IntType = 3


class FileAttributes(Enum):
    ReadOnly: IntType = 1
    Hidden: IntType = 2
    System: IntType = 4
    Directory: IntType = 16
    Archive: IntType = 32
    Device: IntType = 64
    Normal: IntType = 128
    Temporary: IntType = 256
    SparseFile: IntType = 512
    ReparsePoint: IntType = 1024
    Compressed: IntType = 2048
    Offline: IntType = 4096
    NotContentIndexed: IntType = 8192
    Encrypted: IntType = 16384
    IntegrityStream: IntType = 32768
    NoScrubData: IntType = 131072


class FileMode(Enum):
    CreateNew: IntType = 1
    Create: IntType = 2
    Open: IntType = 3
    OpenOrCreate: IntType = 4
    Truncate: IntType = 5
    Append: IntType = 6


class FileOptions(Enum):
    WriteThrough: IntType = -2147483648
    #None: IntType = 0
    Encrypted: IntType = 16384
    DeleteOnClose: IntType = 67108864
    SequentialScan: IntType = 134217728
    RandomAccess: IntType = 268435456
    Asynchronous: IntType = 1073741824


class FileSecurityStateAccess(Enum):
    NoAccess: IntType = 0
    Read: IntType = 1
    Write: IntType = 2
    Append: IntType = 4
    PathDiscovery: IntType = 8
    AllAccess: IntType = 15


class FileShare(Enum):
    #None: IntType = 0
    Read: IntType = 1
    Write: IntType = 2
    ReadWrite: IntType = 3
    Delete: IntType = 4
    Inheritable: IntType = 16


class SearchOption(Enum):
    TopDirectoryOnly: IntType = 0
    AllDirectories: IntType = 1


class SeekOrigin(Enum):
    Begin: IntType = 0
    Current: IntType = 1
    End: IntType = 2


# No Delegates

__all__ = [
    BinaryReader,
    BinaryWriter,
    BufferedStream,
    Directory,
    DirectoryInfo,
    DirectoryInfoResultHandler,
    DirectoryNotFoundException,
    DriveInfo,
    DriveNotFoundException,
    EndOfStreamException,
    File,
    FileInfo,
    FileInfoResultHandler,
    FileLoadException,
    FileNotFoundException,
    FileStream,
    FileStreamAsyncResult,
    FileSystemEnumerableFactory,
    FileSystemEnumerableIterator,
    FileSystemInfo,
    FileSystemInfoResultHandler,
    IOException,
    Iterator,
    LongPath,
    LongPathDirectory,
    LongPathFile,
    LongPathHelper,
    MemoryStream,
    Path,
    PathInternal,
    PathTooLongException,
    PinnedBufferMemoryStream,
    ReadLinesIterator,
    SearchResultHandler,
    Stream,
    StreamReader,
    StreamWriter,
    StringReader,
    StringResultHandler,
    StringWriter,
    TextReader,
    TextWriter,
    UnmanagedMemoryAccessor,
    UnmanagedMemoryStream,
    UnmanagedMemoryStreamWrapper,
    __ConsoleStream,
    __Error,
    __HResults,
    PathHelper,
    DriveType,
    FileAccess,
    FileAttributes,
    FileMode,
    FileOptions,
    FileSecurityStateAccess,
    FileShare,
    SearchOption,
    SeekOrigin,
]
