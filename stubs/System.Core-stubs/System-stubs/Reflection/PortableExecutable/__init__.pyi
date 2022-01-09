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
    RelocsStripped: UShortType = 1
    ExecutableImage: UShortType = 2
    LineNumsStripped: UShortType = 4
    LocalSymsStripped: UShortType = 8
    AggressiveWSTrim: UShortType = 16
    LargeAddressAware: UShortType = 32
    BytesReversedLo: UShortType = 128
    Bit32Machine: UShortType = 256
    DebugStripped: UShortType = 512
    RemovableRunFromSwap: UShortType = 1024
    NetRunFromSwap: UShortType = 2048
    System: UShortType = 4096
    Dll: UShortType = 8192
    UpSystemOnly: UShortType = 16384
    BytesReversedHi: UShortType = 32768


class CorFlags(Enum):
    ILOnly: IntType = 1
    Requires32Bit: IntType = 2
    ILLibrary: IntType = 4
    StrongNameSigned: IntType = 8
    NativeEntryPoint: IntType = 16
    TrackDebugData: IntType = 65536
    Prefers32Bit: IntType = 131072


class DebugDirectoryEntryType(Enum):
    Unknown: IntType = 0
    Coff: IntType = 1
    CodeView: IntType = 2
    Reproducible: IntType = 16
    EmbeddedPortablePdb: IntType = 17


class DllCharacteristics(Enum):
    ProcessInit: UShortType = 1
    ProcessTerm: UShortType = 2
    ThreadInit: UShortType = 4
    ThreadTerm: UShortType = 8
    HighEntropyVirtualAddressSpace: UShortType = 32
    DynamicBase: UShortType = 64
    NxCompatible: UShortType = 256
    NoIsolation: UShortType = 512
    NoSeh: UShortType = 1024
    NoBind: UShortType = 2048
    AppContainer: UShortType = 4096
    WdmDriver: UShortType = 8192
    TerminalServerAware: UShortType = 32768


class Machine(Enum):
    Unknown: UShortType = 0
    I386: UShortType = 332
    WceMipsV2: UShortType = 361
    Alpha: UShortType = 388
    SH3: UShortType = 418
    SH3Dsp: UShortType = 419
    SH3E: UShortType = 420
    SH4: UShortType = 422
    SH5: UShortType = 424
    Arm: UShortType = 448
    Thumb: UShortType = 450
    ArmThumb2: UShortType = 452
    AM33: UShortType = 467
    PowerPC: UShortType = 496
    PowerPCFP: UShortType = 497
    IA64: UShortType = 512
    MIPS16: UShortType = 614
    Alpha64: UShortType = 644
    MipsFpu: UShortType = 870
    MipsFpu16: UShortType = 1126
    Tricore: UShortType = 1312
    Ebc: UShortType = 3772
    Amd64: UShortType = 34404
    M32R: UShortType = 36929


class PEMagic(Enum):
    PE32: UShortType = 267
    PE32Plus: UShortType = 523


class PEStreamOptions(Enum):
    Default: IntType = 0
    LeaveOpen: IntType = 1
    PrefetchMetadata: IntType = 2
    PrefetchEntireImage: IntType = 4
    IsLoadedImage: IntType = 8


class SectionCharacteristics(Enum):
    TypeReg: UIntType = 0
    TypeDSect: UIntType = 1
    TypeNoLoad: UIntType = 2
    TypeGroup: UIntType = 4
    TypeNoPad: UIntType = 8
    TypeCopy: UIntType = 16
    ContainsCode: UIntType = 32
    ContainsInitializedData: UIntType = 64
    ContainsUninitializedData: UIntType = 128
    LinkerOther: UIntType = 256
    LinkerInfo: UIntType = 512
    TypeOver: UIntType = 1024
    LinkerRemove: UIntType = 2048
    LinkerComdat: UIntType = 4096
    MemProtected: UIntType = 16384
    NoDeferSpecExc: UIntType = 16384
    GPRel: UIntType = 32768
    MemFardata: UIntType = 32768
    MemSysheap: UIntType = 65536
    MemPurgeable: UIntType = 131072
    Mem16Bit: UIntType = 131072
    MemLocked: UIntType = 262144
    MemPreload: UIntType = 524288
    Align1Bytes: UIntType = 1048576
    Align2Bytes: UIntType = 2097152
    Align4Bytes: UIntType = 3145728
    Align8Bytes: UIntType = 4194304
    Align16Bytes: UIntType = 5242880
    Align32Bytes: UIntType = 6291456
    Align64Bytes: UIntType = 7340032
    Align128Bytes: UIntType = 8388608
    Align256Bytes: UIntType = 9437184
    Align512Bytes: UIntType = 10485760
    Align1024Bytes: UIntType = 11534336
    Align2048Bytes: UIntType = 12582912
    Align4096Bytes: UIntType = 13631488
    Align8192Bytes: UIntType = 14680064
    AlignMask: UIntType = 15728640
    LinkerNRelocOvfl: UIntType = 16777216
    MemDiscardable: UIntType = 33554432
    MemNotCached: UIntType = 67108864
    MemNotPaged: UIntType = 134217728
    MemShared: UIntType = 268435456
    MemExecute: UIntType = 536870912
    MemRead: UIntType = 1073741824
    MemWrite: UIntType = 2147483648


class Subsystem(Enum):
    Unknown: UShortType = 0
    Native: UShortType = 1
    WindowsGui: UShortType = 2
    WindowsCui: UShortType = 3
    OS2Cui: UShortType = 5
    PosixCui: UShortType = 7
    NativeWindows: UShortType = 8
    WindowsCEGui: UShortType = 9
    EfiApplication: UShortType = 10
    EfiBootServiceDriver: UShortType = 11
    EfiRuntimeDriver: UShortType = 12
    EfiRom: UShortType = 13
    Xbox: UShortType = 14
    WindowsBootApplication: UShortType = 16


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
