"""Automatically generated stubs for C# namespace: System.Reflection.PortableExecutable."""

from abc import ABC
from typing import Final
from typing import overload

from System import Array
from System import Enum
from System import Func
from System import Guid
from System import IDisposable
from System import Int32
from System import Object
from System import String
from System import Type
from System import ValueType
from System.Collections.Immutable import ImmutableArray
from System.IO import Stream
from System.Reflection.Metadata import BlobReader
from System.Reflection.Metadata import MetadataReaderProvider

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class Characteristics(Enum):
    """"""

    RelocsStripped: Characteristics = ...
    """"""
    ExecutableImage: Characteristics = ...
    """"""
    LineNumsStripped: Characteristics = ...
    """"""
    LocalSymsStripped: Characteristics = ...
    """"""
    AggressiveWSTrim: Characteristics = ...
    """"""
    LargeAddressAware: Characteristics = ...
    """"""
    BytesReversedLo: Characteristics = ...
    """"""
    Bit32Machine: Characteristics = ...
    """"""
    DebugStripped: Characteristics = ...
    """"""
    RemovableRunFromSwap: Characteristics = ...
    """"""
    NetRunFromSwap: Characteristics = ...
    """"""
    System: Characteristics = ...
    """"""
    Dll: Characteristics = ...
    """"""
    UpSystemOnly: Characteristics = ...
    """"""
    BytesReversedHi: Characteristics = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CodeViewDebugDirectoryData(ValueType):
    """"""
    @property
    def Age(self) -> int:
        """"""
    @property
    def Guid(self) -> Guid:
        """"""
    @property
    def Path(self) -> str:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CoffHeader(Object):
    """"""
    @property
    def Characteristics(self) -> Characteristics:
        """"""
    @property
    def Machine(self) -> Machine:
        """"""
    @property
    def NumberOfSections(self) -> int:
        """"""
    @property
    def NumberOfSymbols(self) -> int:
        """"""
    @property
    def PointerToSymbolTable(self) -> int:
        """"""
    @property
    def SizeOfOptionalHeader(self) -> int:
        """"""
    @property
    def TimeDateStamp(self) -> int:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class CorFlags(Enum):
    """"""

    ILOnly: CorFlags = ...
    """"""
    Requires32Bit: CorFlags = ...
    """"""
    ILLibrary: CorFlags = ...
    """"""
    StrongNameSigned: CorFlags = ...
    """"""
    NativeEntryPoint: CorFlags = ...
    """"""
    TrackDebugData: CorFlags = ...
    """"""
    Prefers32Bit: CorFlags = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CorHeader(Object):
    """"""
    @property
    def CodeManagerTableDirectory(self) -> DirectoryEntry:
        """"""
    @property
    def EntryPointTokenOrRelativeVirtualAddress(self) -> int:
        """"""
    @property
    def ExportAddressTableJumpsDirectory(self) -> DirectoryEntry:
        """"""
    @property
    def Flags(self) -> CorFlags:
        """"""
    @property
    def MajorRuntimeVersion(self) -> int:
        """"""
    @property
    def ManagedNativeHeaderDirectory(self) -> DirectoryEntry:
        """"""
    @property
    def MetadataDirectory(self) -> DirectoryEntry:
        """"""
    @property
    def MinorRuntimeVersion(self) -> int:
        """"""
    @property
    def ResourcesDirectory(self) -> DirectoryEntry:
        """"""
    @property
    def StrongNameSignatureDirectory(self) -> DirectoryEntry:
        """"""
    @property
    def VtableFixupsDirectory(self) -> DirectoryEntry:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class DebugDirectoryEntry(ValueType):
    """"""
    def __init__(
        self,
        stamp: int,
        majorVersion: int,
        minorVersion: int,
        type: DebugDirectoryEntryType,
        dataSize: int,
        dataRelativeVirtualAddress: int,
        dataPointer: int,
    ) -> None:
        """"""
    @property
    def DataPointer(self) -> int:
        """"""
    @property
    def DataRelativeVirtualAddress(self) -> int:
        """"""
    @property
    def DataSize(self) -> int:
        """"""
    @property
    def IsPortableCodeView(self) -> bool:
        """"""
    @property
    def MajorVersion(self) -> int:
        """"""
    @property
    def MinorVersion(self) -> int:
        """"""
    @property
    def Stamp(self) -> int:
        """"""
    @property
    def Type(self) -> DebugDirectoryEntryType:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class DebugDirectoryEntryType(Enum):
    """"""

    Unknown: DebugDirectoryEntryType = ...
    """"""
    Coff: DebugDirectoryEntryType = ...
    """"""
    CodeView: DebugDirectoryEntryType = ...
    """"""
    Reproducible: DebugDirectoryEntryType = ...
    """"""
    EmbeddedPortablePdb: DebugDirectoryEntryType = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class DirectoryEntry(ValueType):
    """"""

    RelativeVirtualAddress: Final[int]
    """"""
    Size: Final[int]
    """"""
    def __init__(self, relativeVirtualAddress: int, size: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class DllCharacteristics(Enum):
    """"""

    ProcessInit: DllCharacteristics = ...
    """"""
    ProcessTerm: DllCharacteristics = ...
    """"""
    ThreadInit: DllCharacteristics = ...
    """"""
    ThreadTerm: DllCharacteristics = ...
    """"""
    HighEntropyVirtualAddressSpace: DllCharacteristics = ...
    """"""
    DynamicBase: DllCharacteristics = ...
    """"""
    NxCompatible: DllCharacteristics = ...
    """"""
    NoIsolation: DllCharacteristics = ...
    """"""
    NoSeh: DllCharacteristics = ...
    """"""
    NoBind: DllCharacteristics = ...
    """"""
    AppContainer: DllCharacteristics = ...
    """"""
    WdmDriver: DllCharacteristics = ...
    """"""
    TerminalServerAware: DllCharacteristics = ...
    """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class Machine(Enum):
    """"""

    Unknown: Machine = ...
    """"""
    I386: Machine = ...
    """"""
    WceMipsV2: Machine = ...
    """"""
    Alpha: Machine = ...
    """"""
    SH3: Machine = ...
    """"""
    SH3Dsp: Machine = ...
    """"""
    SH3E: Machine = ...
    """"""
    SH4: Machine = ...
    """"""
    SH5: Machine = ...
    """"""
    Arm: Machine = ...
    """"""
    Thumb: Machine = ...
    """"""
    ArmThumb2: Machine = ...
    """"""
    AM33: Machine = ...
    """"""
    PowerPC: Machine = ...
    """"""
    PowerPCFP: Machine = ...
    """"""
    IA64: Machine = ...
    """"""
    MIPS16: Machine = ...
    """"""
    Alpha64: Machine = ...
    """"""
    MipsFpu: Machine = ...
    """"""
    MipsFpu16: Machine = ...
    """"""
    Tricore: Machine = ...
    """"""
    Ebc: Machine = ...
    """"""
    Amd64: Machine = ...
    """"""
    M32R: Machine = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class PEBinaryReader(ValueType):
    """"""
    def __init__(self, stream: Stream, size: int) -> None:
        """"""
    @property
    def CurrentOffset(self) -> int:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ReadByte(self) -> int:
        """"""
    def ReadBytes(self, count: int) -> Array[int]:
        """"""
    def ReadInt16(self) -> int:
        """"""
    def ReadInt32(self) -> int:
        """"""
    def ReadNullPaddedUTF8(self, byteCount: int) -> str:
        """"""
    def ReadUInt16(self) -> int:
        """"""
    def ReadUInt32(self) -> int:
        """"""
    def ReadUInt64(self) -> int:
        """"""
    def Seek(self, offset: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class PEHeader(Object):
    """"""
    @property
    def AddressOfEntryPoint(self) -> int:
        """"""
    @property
    def BaseOfCode(self) -> int:
        """"""
    @property
    def BaseOfData(self) -> int:
        """"""
    @property
    def BaseRelocationTableDirectory(self) -> DirectoryEntry:
        """"""
    @property
    def BoundImportTableDirectory(self) -> DirectoryEntry:
        """"""
    @property
    def CertificateTableDirectory(self) -> DirectoryEntry:
        """"""
    @property
    def CheckSum(self) -> int:
        """"""
    @property
    def CopyrightTableDirectory(self) -> DirectoryEntry:
        """"""
    @property
    def CorHeaderTableDirectory(self) -> DirectoryEntry:
        """"""
    @property
    def DebugTableDirectory(self) -> DirectoryEntry:
        """"""
    @property
    def DelayImportTableDirectory(self) -> DirectoryEntry:
        """"""
    @property
    def DllCharacteristics(self) -> DllCharacteristics:
        """"""
    @property
    def ExceptionTableDirectory(self) -> DirectoryEntry:
        """"""
    @property
    def ExportTableDirectory(self) -> DirectoryEntry:
        """"""
    @property
    def FileAlignment(self) -> int:
        """"""
    @property
    def GlobalPointerTableDirectory(self) -> DirectoryEntry:
        """"""
    @property
    def ImageBase(self) -> int:
        """"""
    @property
    def ImportAddressTableDirectory(self) -> DirectoryEntry:
        """"""
    @property
    def ImportTableDirectory(self) -> DirectoryEntry:
        """"""
    @property
    def LoadConfigTableDirectory(self) -> DirectoryEntry:
        """"""
    @property
    def Magic(self) -> PEMagic:
        """"""
    @property
    def MajorImageVersion(self) -> int:
        """"""
    @property
    def MajorLinkerVersion(self) -> int:
        """"""
    @property
    def MajorOperatingSystemVersion(self) -> int:
        """"""
    @property
    def MajorSubsystemVersion(self) -> int:
        """"""
    @property
    def MinorImageVersion(self) -> int:
        """"""
    @property
    def MinorLinkerVersion(self) -> int:
        """"""
    @property
    def MinorOperatingSystemVersion(self) -> int:
        """"""
    @property
    def MinorSubsystemVersion(self) -> int:
        """"""
    @property
    def NumberOfRvaAndSizes(self) -> int:
        """"""
    @property
    def ResourceTableDirectory(self) -> DirectoryEntry:
        """"""
    @property
    def SectionAlignment(self) -> int:
        """"""
    @property
    def SizeOfCode(self) -> int:
        """"""
    @property
    def SizeOfHeaders(self) -> int:
        """"""
    @property
    def SizeOfHeapCommit(self) -> int:
        """"""
    @property
    def SizeOfHeapReserve(self) -> int:
        """"""
    @property
    def SizeOfImage(self) -> int:
        """"""
    @property
    def SizeOfInitializedData(self) -> int:
        """"""
    @property
    def SizeOfStackCommit(self) -> int:
        """"""
    @property
    def SizeOfStackReserve(self) -> int:
        """"""
    @property
    def SizeOfUninitializedData(self) -> int:
        """"""
    @property
    def Subsystem(self) -> Subsystem:
        """"""
    @property
    def ThreadLocalStorageTableDirectory(self) -> DirectoryEntry:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class PEHeaders(Object):
    """"""
    @overload
    def __init__(self, peStream: Stream) -> None:
        """"""
    @overload
    def __init__(self, peStream: Stream, size: int) -> None:
        """"""
    @overload
    def __init__(self, peStream: Stream, size: int, isLoadedImage: bool) -> None:
        """"""
    @property
    def CoffHeader(self) -> CoffHeader:
        """"""
    @property
    def CoffHeaderStartOffset(self) -> int:
        """"""
    @property
    def CorHeader(self) -> CorHeader:
        """"""
    @property
    def CorHeaderStartOffset(self) -> int:
        """"""
    @property
    def IsCoffOnly(self) -> bool:
        """"""
    @property
    def IsConsoleApplication(self) -> bool:
        """"""
    @property
    def IsDll(self) -> bool:
        """"""
    @property
    def IsExe(self) -> bool:
        """"""
    @property
    def MetadataSize(self) -> int:
        """"""
    @property
    def MetadataStartOffset(self) -> int:
        """"""
    @property
    def PEHeader(self) -> PEHeader:
        """"""
    @property
    def PEHeaderStartOffset(self) -> int:
        """"""
    @property
    def SectionHeaders(self) -> ImmutableArray[SectionHeader]:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetContainingSectionIndex(self, relativeVirtualAddress: int) -> int:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def TryGetDirectoryOffset(self, directory: DirectoryEntry, offset: Int32) -> tuple[bool, Int32]:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class PEMagic(Enum):
    """"""

    PE32: PEMagic = ...
    """"""
    PE32Plus: PEMagic = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class PEMemoryBlock(ValueType):
    """"""
    @property
    def Length(self) -> int:
        """"""
    @property
    def Pointer(self) -> int:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetReader(self) -> BlobReader:
        """"""
    @overload
    def GetReader(self, start: int, length: int) -> BlobReader:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class PEReader(Object, IDisposable):
    """"""
    @overload
    def __init__(self, peImage: int, size: int) -> None:
        """"""
    @overload
    def __init__(self, peImage: int, size: int, isLoadedImage: bool) -> None:
        """"""
    @overload
    def __init__(self, peStream: Stream) -> None:
        """"""
    @overload
    def __init__(self, peStream: Stream, options: PEStreamOptions) -> None:
        """"""
    @overload
    def __init__(self, peStream: Stream, options: PEStreamOptions, size: int) -> None:
        """"""
    @overload
    def __init__(self, peImage: ImmutableArray[int]) -> None:
        """"""
    @property
    def HasMetadata(self) -> bool:
        """"""
    @property
    def IsEntireImageAvailable(self) -> bool:
        """"""
    @property
    def IsLoadedImage(self) -> bool:
        """"""
    @property
    def PEHeaders(self) -> PEHeaders:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEntireImage(self) -> PEMemoryBlock:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetMetadata(self) -> PEMemoryBlock:
        """"""
    @overload
    def GetSectionData(self, relativeVirtualAddress: int) -> PEMemoryBlock:
        """"""
    @overload
    def GetSectionData(self, sectionName: str) -> PEMemoryBlock:
        """"""
    def GetType(self) -> Type:
        """"""
    def ReadCodeViewDebugDirectoryData(
        self, entry: DebugDirectoryEntry
    ) -> CodeViewDebugDirectoryData:
        """"""
    def ReadDebugDirectory(self) -> ImmutableArray[DebugDirectoryEntry]:
        """"""
    def ReadEmbeddedPortablePdbDebugDirectoryData(
        self, entry: DebugDirectoryEntry
    ) -> MetadataReaderProvider:
        """"""
    def ToString(self) -> str:
        """"""
    def TryOpenAssociatedPortablePdb(
        self,
        peImagePath: str,
        pdbFileStreamProvider: Func[str, Stream],
        pdbReaderProvider: MetadataReaderProvider,
        pdbPath: String,
    ) -> tuple[bool, MetadataReaderProvider, String]:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class PEStreamOptions(Enum):
    """"""

    Default: PEStreamOptions = ...
    """"""
    LeaveOpen: PEStreamOptions = ...
    """"""
    PrefetchMetadata: PEStreamOptions = ...
    """"""
    PrefetchEntireImage: PEStreamOptions = ...
    """"""
    IsLoadedImage: PEStreamOptions = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class PEStreamOptionsExtensions(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def IsValid(cls, options: PEStreamOptions) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class SectionCharacteristics(Enum):
    """"""

    TypeReg: SectionCharacteristics = ...
    """"""
    TypeDSect: SectionCharacteristics = ...
    """"""
    TypeNoLoad: SectionCharacteristics = ...
    """"""
    TypeGroup: SectionCharacteristics = ...
    """"""
    TypeNoPad: SectionCharacteristics = ...
    """"""
    TypeCopy: SectionCharacteristics = ...
    """"""
    ContainsCode: SectionCharacteristics = ...
    """"""
    ContainsInitializedData: SectionCharacteristics = ...
    """"""
    ContainsUninitializedData: SectionCharacteristics = ...
    """"""
    LinkerOther: SectionCharacteristics = ...
    """"""
    LinkerInfo: SectionCharacteristics = ...
    """"""
    TypeOver: SectionCharacteristics = ...
    """"""
    LinkerRemove: SectionCharacteristics = ...
    """"""
    LinkerComdat: SectionCharacteristics = ...
    """"""
    MemProtected: SectionCharacteristics = ...
    """"""
    NoDeferSpecExc: SectionCharacteristics = ...
    """"""
    GPRel: SectionCharacteristics = ...
    """"""
    MemFardata: SectionCharacteristics = ...
    """"""
    MemSysheap: SectionCharacteristics = ...
    """"""
    MemPurgeable: SectionCharacteristics = ...
    """"""
    Mem16Bit: SectionCharacteristics = ...
    """"""
    MemLocked: SectionCharacteristics = ...
    """"""
    MemPreload: SectionCharacteristics = ...
    """"""
    Align1Bytes: SectionCharacteristics = ...
    """"""
    Align2Bytes: SectionCharacteristics = ...
    """"""
    Align4Bytes: SectionCharacteristics = ...
    """"""
    Align8Bytes: SectionCharacteristics = ...
    """"""
    Align16Bytes: SectionCharacteristics = ...
    """"""
    Align32Bytes: SectionCharacteristics = ...
    """"""
    Align64Bytes: SectionCharacteristics = ...
    """"""
    Align128Bytes: SectionCharacteristics = ...
    """"""
    Align256Bytes: SectionCharacteristics = ...
    """"""
    Align512Bytes: SectionCharacteristics = ...
    """"""
    Align1024Bytes: SectionCharacteristics = ...
    """"""
    Align2048Bytes: SectionCharacteristics = ...
    """"""
    Align4096Bytes: SectionCharacteristics = ...
    """"""
    Align8192Bytes: SectionCharacteristics = ...
    """"""
    AlignMask: SectionCharacteristics = ...
    """"""
    LinkerNRelocOvfl: SectionCharacteristics = ...
    """"""
    MemDiscardable: SectionCharacteristics = ...
    """"""
    MemNotCached: SectionCharacteristics = ...
    """"""
    MemNotPaged: SectionCharacteristics = ...
    """"""
    MemShared: SectionCharacteristics = ...
    """"""
    MemExecute: SectionCharacteristics = ...
    """"""
    MemRead: SectionCharacteristics = ...
    """"""
    MemWrite: SectionCharacteristics = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SectionHeader(ValueType):
    """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def NumberOfLineNumbers(self) -> int:
        """"""
    @property
    def NumberOfRelocations(self) -> int:
        """"""
    @property
    def PointerToLineNumbers(self) -> int:
        """"""
    @property
    def PointerToRawData(self) -> int:
        """"""
    @property
    def PointerToRelocations(self) -> int:
        """"""
    @property
    def SectionCharacteristics(self) -> SectionCharacteristics:
        """"""
    @property
    def SizeOfRawData(self) -> int:
        """"""
    @property
    def VirtualAddress(self) -> int:
        """"""
    @property
    def VirtualSize(self) -> int:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class Subsystem(Enum):
    """"""

    Unknown: Subsystem = ...
    """"""
    Native: Subsystem = ...
    """"""
    WindowsGui: Subsystem = ...
    """"""
    WindowsCui: Subsystem = ...
    """"""
    OS2Cui: Subsystem = ...
    """"""
    PosixCui: Subsystem = ...
    """"""
    NativeWindows: Subsystem = ...
    """"""
    WindowsCEGui: Subsystem = ...
    """"""
    EfiApplication: Subsystem = ...
    """"""
    EfiBootServiceDriver: Subsystem = ...
    """"""
    EfiRuntimeDriver: Subsystem = ...
    """"""
    EfiRom: Subsystem = ...
    """"""
    Xbox: Subsystem = ...
    """"""
    WindowsBootApplication: Subsystem = ...
    """"""
