from __future__ import annotations

from abc import ABC
from typing import List, Tuple, Union, overload

from System import Array, Boolean, Byte, Enum, Func, Guid, IDisposable, Int16, Int32, Object, String, UInt16, UInt32, UInt64, ValueType, Void
from System.Collections.Immutable import ImmutableArray
from System.IO import Stream
from System.Reflection.Metadata import BlobReader, MetadataReaderProvider

# ---------- Types ---------- #

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
ByteType = Union[int, Byte]
IntType = Union[int, Int32]
ObjectType = Object
ShortType = Union[int, Int16]
StringType = Union[str, String]
UIntType = Union[int, UInt32]
ULongType = Union[int, UInt64]
UShortType = Union[int, UInt16]
VoidType = Union[None, Void]


# ---------- Classes ---------- #

class CoffHeader(ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Characteristics(self) -> Characteristics: ...
    
    @property
    def Machine(self) -> Machine: ...
    
    @property
    def NumberOfSections(self) -> ShortType: ...
    
    @property
    def NumberOfSymbols(self) -> IntType: ...
    
    @property
    def PointerToSymbolTable(self) -> IntType: ...
    
    @property
    def SizeOfOptionalHeader(self) -> ShortType: ...
    
    @property
    def TimeDateStamp(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def get_Characteristics(self) -> Characteristics: ...
    
    def get_Machine(self) -> Machine: ...
    
    def get_NumberOfSections(self) -> ShortType: ...
    
    def get_NumberOfSymbols(self) -> IntType: ...
    
    def get_PointerToSymbolTable(self) -> IntType: ...
    
    def get_SizeOfOptionalHeader(self) -> ShortType: ...
    
    def get_TimeDateStamp(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CorHeader(ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def CodeManagerTableDirectory(self) -> DirectoryEntry: ...
    
    @property
    def EntryPointTokenOrRelativeVirtualAddress(self) -> IntType: ...
    
    @property
    def ExportAddressTableJumpsDirectory(self) -> DirectoryEntry: ...
    
    @property
    def Flags(self) -> CorFlags: ...
    
    @property
    def MajorRuntimeVersion(self) -> UShortType: ...
    
    @property
    def ManagedNativeHeaderDirectory(self) -> DirectoryEntry: ...
    
    @property
    def MetadataDirectory(self) -> DirectoryEntry: ...
    
    @property
    def MinorRuntimeVersion(self) -> UShortType: ...
    
    @property
    def ResourcesDirectory(self) -> DirectoryEntry: ...
    
    @property
    def StrongNameSignatureDirectory(self) -> DirectoryEntry: ...
    
    @property
    def VtableFixupsDirectory(self) -> DirectoryEntry: ...
    
    # ---------- Methods ---------- #
    
    def get_CodeManagerTableDirectory(self) -> DirectoryEntry: ...
    
    def get_EntryPointTokenOrRelativeVirtualAddress(self) -> IntType: ...
    
    def get_ExportAddressTableJumpsDirectory(self) -> DirectoryEntry: ...
    
    def get_Flags(self) -> CorFlags: ...
    
    def get_MajorRuntimeVersion(self) -> UShortType: ...
    
    def get_ManagedNativeHeaderDirectory(self) -> DirectoryEntry: ...
    
    def get_MetadataDirectory(self) -> DirectoryEntry: ...
    
    def get_MinorRuntimeVersion(self) -> UShortType: ...
    
    def get_ResourcesDirectory(self) -> DirectoryEntry: ...
    
    def get_StrongNameSignatureDirectory(self) -> DirectoryEntry: ...
    
    def get_VtableFixupsDirectory(self) -> DirectoryEntry: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PEHeader(ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def AddressOfEntryPoint(self) -> IntType: ...
    
    @property
    def BaseOfCode(self) -> IntType: ...
    
    @property
    def BaseOfData(self) -> IntType: ...
    
    @property
    def BaseRelocationTableDirectory(self) -> DirectoryEntry: ...
    
    @property
    def BoundImportTableDirectory(self) -> DirectoryEntry: ...
    
    @property
    def CertificateTableDirectory(self) -> DirectoryEntry: ...
    
    @property
    def CheckSum(self) -> UIntType: ...
    
    @property
    def CopyrightTableDirectory(self) -> DirectoryEntry: ...
    
    @property
    def CorHeaderTableDirectory(self) -> DirectoryEntry: ...
    
    @property
    def DebugTableDirectory(self) -> DirectoryEntry: ...
    
    @property
    def DelayImportTableDirectory(self) -> DirectoryEntry: ...
    
    @property
    def DllCharacteristics(self) -> DllCharacteristics: ...
    
    @property
    def ExceptionTableDirectory(self) -> DirectoryEntry: ...
    
    @property
    def ExportTableDirectory(self) -> DirectoryEntry: ...
    
    @property
    def FileAlignment(self) -> IntType: ...
    
    @property
    def GlobalPointerTableDirectory(self) -> DirectoryEntry: ...
    
    @property
    def ImageBase(self) -> ULongType: ...
    
    @property
    def ImportAddressTableDirectory(self) -> DirectoryEntry: ...
    
    @property
    def ImportTableDirectory(self) -> DirectoryEntry: ...
    
    @property
    def LoadConfigTableDirectory(self) -> DirectoryEntry: ...
    
    @property
    def Magic(self) -> PEMagic: ...
    
    @property
    def MajorImageVersion(self) -> UShortType: ...
    
    @property
    def MajorLinkerVersion(self) -> ByteType: ...
    
    @property
    def MajorOperatingSystemVersion(self) -> UShortType: ...
    
    @property
    def MajorSubsystemVersion(self) -> UShortType: ...
    
    @property
    def MinorImageVersion(self) -> UShortType: ...
    
    @property
    def MinorLinkerVersion(self) -> ByteType: ...
    
    @property
    def MinorOperatingSystemVersion(self) -> UShortType: ...
    
    @property
    def MinorSubsystemVersion(self) -> UShortType: ...
    
    @property
    def NumberOfRvaAndSizes(self) -> IntType: ...
    
    @property
    def ResourceTableDirectory(self) -> DirectoryEntry: ...
    
    @property
    def SectionAlignment(self) -> IntType: ...
    
    @property
    def SizeOfCode(self) -> IntType: ...
    
    @property
    def SizeOfHeaders(self) -> IntType: ...
    
    @property
    def SizeOfHeapCommit(self) -> ULongType: ...
    
    @property
    def SizeOfHeapReserve(self) -> ULongType: ...
    
    @property
    def SizeOfImage(self) -> IntType: ...
    
    @property
    def SizeOfInitializedData(self) -> IntType: ...
    
    @property
    def SizeOfStackCommit(self) -> ULongType: ...
    
    @property
    def SizeOfStackReserve(self) -> ULongType: ...
    
    @property
    def SizeOfUninitializedData(self) -> IntType: ...
    
    @property
    def Subsystem(self) -> Subsystem: ...
    
    @property
    def ThreadLocalStorageTableDirectory(self) -> DirectoryEntry: ...
    
    # ---------- Methods ---------- #
    
    def get_AddressOfEntryPoint(self) -> IntType: ...
    
    def get_BaseOfCode(self) -> IntType: ...
    
    def get_BaseOfData(self) -> IntType: ...
    
    def get_BaseRelocationTableDirectory(self) -> DirectoryEntry: ...
    
    def get_BoundImportTableDirectory(self) -> DirectoryEntry: ...
    
    def get_CertificateTableDirectory(self) -> DirectoryEntry: ...
    
    def get_CheckSum(self) -> UIntType: ...
    
    def get_CopyrightTableDirectory(self) -> DirectoryEntry: ...
    
    def get_CorHeaderTableDirectory(self) -> DirectoryEntry: ...
    
    def get_DebugTableDirectory(self) -> DirectoryEntry: ...
    
    def get_DelayImportTableDirectory(self) -> DirectoryEntry: ...
    
    def get_DllCharacteristics(self) -> DllCharacteristics: ...
    
    def get_ExceptionTableDirectory(self) -> DirectoryEntry: ...
    
    def get_ExportTableDirectory(self) -> DirectoryEntry: ...
    
    def get_FileAlignment(self) -> IntType: ...
    
    def get_GlobalPointerTableDirectory(self) -> DirectoryEntry: ...
    
    def get_ImageBase(self) -> ULongType: ...
    
    def get_ImportAddressTableDirectory(self) -> DirectoryEntry: ...
    
    def get_ImportTableDirectory(self) -> DirectoryEntry: ...
    
    def get_LoadConfigTableDirectory(self) -> DirectoryEntry: ...
    
    def get_Magic(self) -> PEMagic: ...
    
    def get_MajorImageVersion(self) -> UShortType: ...
    
    def get_MajorLinkerVersion(self) -> ByteType: ...
    
    def get_MajorOperatingSystemVersion(self) -> UShortType: ...
    
    def get_MajorSubsystemVersion(self) -> UShortType: ...
    
    def get_MinorImageVersion(self) -> UShortType: ...
    
    def get_MinorLinkerVersion(self) -> ByteType: ...
    
    def get_MinorOperatingSystemVersion(self) -> UShortType: ...
    
    def get_MinorSubsystemVersion(self) -> UShortType: ...
    
    def get_NumberOfRvaAndSizes(self) -> IntType: ...
    
    def get_ResourceTableDirectory(self) -> DirectoryEntry: ...
    
    def get_SectionAlignment(self) -> IntType: ...
    
    def get_SizeOfCode(self) -> IntType: ...
    
    def get_SizeOfHeaders(self) -> IntType: ...
    
    def get_SizeOfHeapCommit(self) -> ULongType: ...
    
    def get_SizeOfHeapReserve(self) -> ULongType: ...
    
    def get_SizeOfImage(self) -> IntType: ...
    
    def get_SizeOfInitializedData(self) -> IntType: ...
    
    def get_SizeOfStackCommit(self) -> ULongType: ...
    
    def get_SizeOfStackReserve(self) -> ULongType: ...
    
    def get_SizeOfUninitializedData(self) -> IntType: ...
    
    def get_Subsystem(self) -> Subsystem: ...
    
    def get_ThreadLocalStorageTableDirectory(self) -> DirectoryEntry: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PEHeaders(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, peStream: Stream): ...
    
    @overload
    def __init__(self, peStream: Stream, size: IntType): ...
    
    @overload
    def __init__(self, peStream: Stream, size: IntType, isLoadedImage: BooleanType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CoffHeader(self) -> CoffHeader: ...
    
    @property
    def CoffHeaderStartOffset(self) -> IntType: ...
    
    @property
    def CorHeader(self) -> CorHeader: ...
    
    @property
    def CorHeaderStartOffset(self) -> IntType: ...
    
    @property
    def IsCoffOnly(self) -> BooleanType: ...
    
    @property
    def IsConsoleApplication(self) -> BooleanType: ...
    
    @property
    def IsDll(self) -> BooleanType: ...
    
    @property
    def IsExe(self) -> BooleanType: ...
    
    @property
    def MetadataSize(self) -> IntType: ...
    
    @property
    def MetadataStartOffset(self) -> IntType: ...
    
    @property
    def PEHeader(self) -> PEHeader: ...
    
    @property
    def PEHeaderStartOffset(self) -> IntType: ...
    
    @property
    def SectionHeaders(self) -> ImmutableArray[SectionHeader]: ...
    
    # ---------- Methods ---------- #
    
    def GetContainingSectionIndex(self, relativeVirtualAddress: IntType) -> IntType: ...
    
    def TryGetDirectoryOffset(self, directory: DirectoryEntry, offset: IntType) -> Tuple[BooleanType, IntType]: ...
    
    def get_CoffHeader(self) -> CoffHeader: ...
    
    def get_CoffHeaderStartOffset(self) -> IntType: ...
    
    def get_CorHeader(self) -> CorHeader: ...
    
    def get_CorHeaderStartOffset(self) -> IntType: ...
    
    def get_IsCoffOnly(self) -> BooleanType: ...
    
    def get_IsConsoleApplication(self) -> BooleanType: ...
    
    def get_IsDll(self) -> BooleanType: ...
    
    def get_IsExe(self) -> BooleanType: ...
    
    def get_MetadataSize(self) -> IntType: ...
    
    def get_MetadataStartOffset(self) -> IntType: ...
    
    def get_PEHeader(self) -> PEHeader: ...
    
    def get_PEHeaderStartOffset(self) -> IntType: ...
    
    def get_SectionHeaders(self) -> ImmutableArray[SectionHeader]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PEReader(ObjectType, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, peImage: ByteType, size: IntType): ...
    
    @overload
    def __init__(self, peImage: ByteType, size: IntType, isLoadedImage: BooleanType): ...
    
    @overload
    def __init__(self, peStream: Stream): ...
    
    @overload
    def __init__(self, peStream: Stream, options: PEStreamOptions): ...
    
    @overload
    def __init__(self, peStream: Stream, options: PEStreamOptions, size: IntType): ...
    
    @overload
    def __init__(self, peImage: ImmutableArray[ByteType]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def HasMetadata(self) -> BooleanType: ...
    
    @property
    def IsEntireImageAvailable(self) -> BooleanType: ...
    
    @property
    def IsLoadedImage(self) -> BooleanType: ...
    
    @property
    def PEHeaders(self) -> PEHeaders: ...
    
    # ---------- Methods ---------- #
    
    def Dispose(self) -> VoidType: ...
    
    def GetEntireImage(self) -> PEMemoryBlock: ...
    
    def GetMetadata(self) -> PEMemoryBlock: ...
    
    @overload
    def GetSectionData(self, relativeVirtualAddress: IntType) -> PEMemoryBlock: ...
    
    @overload
    def GetSectionData(self, sectionName: StringType) -> PEMemoryBlock: ...
    
    def ReadCodeViewDebugDirectoryData(self, entry: DebugDirectoryEntry) -> CodeViewDebugDirectoryData: ...
    
    def ReadDebugDirectory(self) -> ImmutableArray[DebugDirectoryEntry]: ...
    
    def ReadEmbeddedPortablePdbDebugDirectoryData(self, entry: DebugDirectoryEntry) -> MetadataReaderProvider: ...
    
    def TryOpenAssociatedPortablePdb(self, peImagePath: StringType, pdbFileStreamProvider: Func[StringType, Stream], pdbReaderProvider: MetadataReaderProvider, pdbPath: StringType) -> Tuple[BooleanType, MetadataReaderProvider, StringType]: ...
    
    def get_HasMetadata(self) -> BooleanType: ...
    
    def get_IsEntireImageAvailable(self) -> BooleanType: ...
    
    def get_IsLoadedImage(self) -> BooleanType: ...
    
    def get_PEHeaders(self) -> PEHeaders: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PEStreamOptionsExtensions(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def IsValid(options: PEStreamOptions) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# ---------- Structs ---------- #

class CodeViewDebugDirectoryData(ValueType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Age(self) -> IntType: ...
    
    @property
    def Guid(self) -> Guid: ...
    
    @property
    def Path(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_Age(self) -> IntType: ...
    
    def get_Guid(self) -> Guid: ...
    
    def get_Path(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DebugDirectoryEntry(ValueType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, stamp: UIntType, majorVersion: UShortType, minorVersion: UShortType, type: DebugDirectoryEntryType, dataSize: IntType, dataRelativeVirtualAddress: IntType, dataPointer: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def DataPointer(self) -> IntType: ...
    
    @property
    def DataRelativeVirtualAddress(self) -> IntType: ...
    
    @property
    def DataSize(self) -> IntType: ...
    
    @property
    def IsPortableCodeView(self) -> BooleanType: ...
    
    @property
    def MajorVersion(self) -> UShortType: ...
    
    @property
    def MinorVersion(self) -> UShortType: ...
    
    @property
    def Stamp(self) -> UIntType: ...
    
    @property
    def Type(self) -> DebugDirectoryEntryType: ...
    
    # ---------- Methods ---------- #
    
    def get_DataPointer(self) -> IntType: ...
    
    def get_DataRelativeVirtualAddress(self) -> IntType: ...
    
    def get_DataSize(self) -> IntType: ...
    
    def get_IsPortableCodeView(self) -> BooleanType: ...
    
    def get_MajorVersion(self) -> UShortType: ...
    
    def get_MinorVersion(self) -> UShortType: ...
    
    def get_Stamp(self) -> UIntType: ...
    
    def get_Type(self) -> DebugDirectoryEntryType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DirectoryEntry(ValueType):
    # ---------- Fields ---------- #
    
    @property
    def RelativeVirtualAddress(self) -> IntType: ...
    
    @property
    def Size(self) -> IntType: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self, relativeVirtualAddress: IntType, size: IntType): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PEBinaryReader(ValueType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, stream: Stream, size: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CurrentOffset(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def ReadByte(self) -> ByteType: ...
    
    def ReadBytes(self, count: IntType) -> ArrayType[ByteType]: ...
    
    def ReadInt16(self) -> ShortType: ...
    
    def ReadInt32(self) -> IntType: ...
    
    def ReadNullPaddedUTF8(self, byteCount: IntType) -> StringType: ...
    
    def ReadUInt16(self) -> UShortType: ...
    
    def ReadUInt32(self) -> UIntType: ...
    
    def ReadUInt64(self) -> ULongType: ...
    
    def Seek(self, offset: IntType) -> VoidType: ...
    
    def get_CurrentOffset(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PEMemoryBlock(ValueType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Length(self) -> IntType: ...
    
    @property
    def Pointer(self) -> ByteType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def GetReader(self) -> BlobReader: ...
    
    @overload
    def GetReader(self, start: IntType, length: IntType) -> BlobReader: ...
    
    def get_Length(self) -> IntType: ...
    
    def get_Pointer(self) -> ByteType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SectionHeader(ValueType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def NumberOfLineNumbers(self) -> UShortType: ...
    
    @property
    def NumberOfRelocations(self) -> UShortType: ...
    
    @property
    def PointerToLineNumbers(self) -> IntType: ...
    
    @property
    def PointerToRawData(self) -> IntType: ...
    
    @property
    def PointerToRelocations(self) -> IntType: ...
    
    @property
    def SectionCharacteristics(self) -> SectionCharacteristics: ...
    
    @property
    def SizeOfRawData(self) -> IntType: ...
    
    @property
    def VirtualAddress(self) -> IntType: ...
    
    @property
    def VirtualSize(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def get_Name(self) -> StringType: ...
    
    def get_NumberOfLineNumbers(self) -> UShortType: ...
    
    def get_NumberOfRelocations(self) -> UShortType: ...
    
    def get_PointerToLineNumbers(self) -> IntType: ...
    
    def get_PointerToRawData(self) -> IntType: ...
    
    def get_PointerToRelocations(self) -> IntType: ...
    
    def get_SectionCharacteristics(self) -> SectionCharacteristics: ...
    
    def get_SizeOfRawData(self) -> IntType: ...
    
    def get_VirtualAddress(self) -> IntType: ...
    
    def get_VirtualSize(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# No Interfaces

# ---------- Enums ---------- #

class Characteristics(Enum):
    RelocsStripped = 1
    ExecutableImage = 2
    LineNumsStripped = 4
    LocalSymsStripped = 8
    AggressiveWSTrim = 16
    LargeAddressAware = 32
    BytesReversedLo = 128
    Bit32Machine = 256
    DebugStripped = 512
    RemovableRunFromSwap = 1024
    NetRunFromSwap = 2048
    System = 4096
    Dll = 8192
    UpSystemOnly = 16384
    BytesReversedHi = 32768


class CorFlags(Enum):
    ILOnly = 1
    Requires32Bit = 2
    ILLibrary = 4
    StrongNameSigned = 8
    NativeEntryPoint = 16
    TrackDebugData = 65536
    Prefers32Bit = 131072


class DebugDirectoryEntryType(Enum):
    Unknown = 0
    Coff = 1
    CodeView = 2
    Reproducible = 16
    EmbeddedPortablePdb = 17


class DllCharacteristics(Enum):
    ProcessInit = 1
    ProcessTerm = 2
    ThreadInit = 4
    ThreadTerm = 8
    HighEntropyVirtualAddressSpace = 32
    DynamicBase = 64
    NxCompatible = 256
    NoIsolation = 512
    NoSeh = 1024
    NoBind = 2048
    AppContainer = 4096
    WdmDriver = 8192
    TerminalServerAware = 32768


class Machine(Enum):
    Unknown = 0
    I386 = 332
    WceMipsV2 = 361
    Alpha = 388
    SH3 = 418
    SH3Dsp = 419
    SH3E = 420
    SH4 = 422
    SH5 = 424
    Arm = 448
    Thumb = 450
    ArmThumb2 = 452
    AM33 = 467
    PowerPC = 496
    PowerPCFP = 497
    IA64 = 512
    MIPS16 = 614
    Alpha64 = 644
    MipsFpu = 870
    MipsFpu16 = 1126
    Tricore = 1312
    Ebc = 3772
    Amd64 = 34404
    M32R = 36929


class PEMagic(Enum):
    PE32 = 267
    PE32Plus = 523


class PEStreamOptions(Enum):
    Default = 0
    LeaveOpen = 1
    PrefetchMetadata = 2
    PrefetchEntireImage = 4
    IsLoadedImage = 8


class SectionCharacteristics(Enum):
    TypeReg = 0
    TypeDSect = 1
    TypeNoLoad = 2
    TypeGroup = 4
    TypeNoPad = 8
    TypeCopy = 16
    ContainsCode = 32
    ContainsInitializedData = 64
    ContainsUninitializedData = 128
    LinkerOther = 256
    LinkerInfo = 512
    TypeOver = 1024
    LinkerRemove = 2048
    LinkerComdat = 4096
    MemProtected = 16384
    NoDeferSpecExc = 16384
    GPRel = 32768
    MemFardata = 32768
    MemSysheap = 65536
    MemPurgeable = 131072
    Mem16Bit = 131072
    MemLocked = 262144
    MemPreload = 524288
    Align1Bytes = 1048576
    Align2Bytes = 2097152
    Align4Bytes = 3145728
    Align8Bytes = 4194304
    Align16Bytes = 5242880
    Align32Bytes = 6291456
    Align64Bytes = 7340032
    Align128Bytes = 8388608
    Align256Bytes = 9437184
    Align512Bytes = 10485760
    Align1024Bytes = 11534336
    Align2048Bytes = 12582912
    Align4096Bytes = 13631488
    Align8192Bytes = 14680064
    AlignMask = 15728640
    LinkerNRelocOvfl = 16777216
    MemDiscardable = 33554432
    MemNotCached = 67108864
    MemNotPaged = 134217728
    MemShared = 268435456
    MemExecute = 536870912
    MemRead = 1073741824
    MemWrite = 2147483648


class Subsystem(Enum):
    Unknown = 0
    Native = 1
    WindowsGui = 2
    WindowsCui = 3
    OS2Cui = 5
    PosixCui = 7
    NativeWindows = 8
    WindowsCEGui = 9
    EfiApplication = 10
    EfiBootServiceDriver = 11
    EfiRuntimeDriver = 12
    EfiRom = 13
    Xbox = 14
    WindowsBootApplication = 16


# No Delegates

__all__ = [
    CoffHeader,
    CorHeader,
    PEHeader,
    PEHeaders,
    PEReader,
    PEStreamOptionsExtensions,
    CodeViewDebugDirectoryData,
    DebugDirectoryEntry,
    DirectoryEntry,
    PEBinaryReader,
    PEMemoryBlock,
    SectionHeader,
    Characteristics,
    CorFlags,
    DebugDirectoryEntryType,
    DllCharacteristics,
    Machine,
    PEMagic,
    PEStreamOptions,
    SectionCharacteristics,
    Subsystem,
]
