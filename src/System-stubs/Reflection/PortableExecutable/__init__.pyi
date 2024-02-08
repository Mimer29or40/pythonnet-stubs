from __future__ import annotations

from abc import ABC
from typing import Final
from typing import Tuple
from typing import overload

from System import Array
from System import Enum
from System import Func
from System import Guid
from System import IDisposable
from System import Object
from System import Type
from System import ValueType
from System.Collections.Immutable import ImmutableArray
from System.IO import Stream
from System.Reflection.Metadata import BlobReader
from System.Reflection.Metadata import MetadataReaderProvider

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

class CodeViewDebugDirectoryData(ValueType):
    """"""

    @property
    def Age(self) -> int:
        """

        :return:
        """
    @property
    def Guid(self) -> Guid:
        """

        :return:
        """
    @property
    def Path(self) -> str:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CoffHeader(Object):
    """"""

    @property
    def Characteristics(self) -> Characteristics:
        """

        :return:
        """
    @property
    def Machine(self) -> Machine:
        """

        :return:
        """
    @property
    def NumberOfSections(self) -> int:
        """

        :return:
        """
    @property
    def NumberOfSymbols(self) -> int:
        """

        :return:
        """
    @property
    def PointerToSymbolTable(self) -> int:
        """

        :return:
        """
    @property
    def SizeOfOptionalHeader(self) -> int:
        """

        :return:
        """
    @property
    def TimeDateStamp(self) -> int:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

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

class CorHeader(Object):
    """"""

    @property
    def CodeManagerTableDirectory(self) -> DirectoryEntry:
        """

        :return:
        """
    @property
    def EntryPointTokenOrRelativeVirtualAddress(self) -> int:
        """

        :return:
        """
    @property
    def ExportAddressTableJumpsDirectory(self) -> DirectoryEntry:
        """

        :return:
        """
    @property
    def Flags(self) -> CorFlags:
        """

        :return:
        """
    @property
    def MajorRuntimeVersion(self) -> int:
        """

        :return:
        """
    @property
    def ManagedNativeHeaderDirectory(self) -> DirectoryEntry:
        """

        :return:
        """
    @property
    def MetadataDirectory(self) -> DirectoryEntry:
        """

        :return:
        """
    @property
    def MinorRuntimeVersion(self) -> int:
        """

        :return:
        """
    @property
    def ResourcesDirectory(self) -> DirectoryEntry:
        """

        :return:
        """
    @property
    def StrongNameSignatureDirectory(self) -> DirectoryEntry:
        """

        :return:
        """
    @property
    def VtableFixupsDirectory(self) -> DirectoryEntry:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

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
    ):
        """

        :param stamp:
        :param majorVersion:
        :param minorVersion:
        :param type:
        :param dataSize:
        :param dataRelativeVirtualAddress:
        :param dataPointer:
        """
    @property
    def DataPointer(self) -> int:
        """

        :return:
        """
    @property
    def DataRelativeVirtualAddress(self) -> int:
        """

        :return:
        """
    @property
    def DataSize(self) -> int:
        """

        :return:
        """
    @property
    def IsPortableCodeView(self) -> bool:
        """

        :return:
        """
    @property
    def MajorVersion(self) -> int:
        """

        :return:
        """
    @property
    def MinorVersion(self) -> int:
        """

        :return:
        """
    @property
    def Stamp(self) -> int:
        """

        :return:
        """
    @property
    def Type(self) -> DebugDirectoryEntryType:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

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

class DirectoryEntry(ValueType):
    """"""

    RelativeVirtualAddress: Final[int] = ...
    """
    
    :return: 
    """
    Size: Final[int] = ...
    """
    
    :return: 
    """
    def __init__(self, relativeVirtualAddress: int, size: int):
        """

        :param relativeVirtualAddress:
        :param size:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

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

class PEBinaryReader(ValueType):
    """"""

    def __init__(self, stream: Stream, size: int):
        """

        :param stream:
        :param size:
        """
    @property
    def CurrentOffset(self) -> int:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ReadByte(self) -> int:
        """

        :return:
        """
    def ReadBytes(self, count: int) -> Array[int]:
        """

        :param count:
        :return:
        """
    def ReadInt16(self) -> int:
        """

        :return:
        """
    def ReadInt32(self) -> int:
        """

        :return:
        """
    def ReadNullPaddedUTF8(self, byteCount: int) -> str:
        """

        :param byteCount:
        :return:
        """
    def ReadUInt16(self) -> int:
        """

        :return:
        """
    def ReadUInt32(self) -> int:
        """

        :return:
        """
    def ReadUInt64(self) -> int:
        """

        :return:
        """
    def Seek(self, offset: int) -> None:
        """

        :param offset:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class PEHeader(Object):
    """"""

    @property
    def AddressOfEntryPoint(self) -> int:
        """

        :return:
        """
    @property
    def BaseOfCode(self) -> int:
        """

        :return:
        """
    @property
    def BaseOfData(self) -> int:
        """

        :return:
        """
    @property
    def BaseRelocationTableDirectory(self) -> DirectoryEntry:
        """

        :return:
        """
    @property
    def BoundImportTableDirectory(self) -> DirectoryEntry:
        """

        :return:
        """
    @property
    def CertificateTableDirectory(self) -> DirectoryEntry:
        """

        :return:
        """
    @property
    def CheckSum(self) -> int:
        """

        :return:
        """
    @property
    def CopyrightTableDirectory(self) -> DirectoryEntry:
        """

        :return:
        """
    @property
    def CorHeaderTableDirectory(self) -> DirectoryEntry:
        """

        :return:
        """
    @property
    def DebugTableDirectory(self) -> DirectoryEntry:
        """

        :return:
        """
    @property
    def DelayImportTableDirectory(self) -> DirectoryEntry:
        """

        :return:
        """
    @property
    def DllCharacteristics(self) -> DllCharacteristics:
        """

        :return:
        """
    @property
    def ExceptionTableDirectory(self) -> DirectoryEntry:
        """

        :return:
        """
    @property
    def ExportTableDirectory(self) -> DirectoryEntry:
        """

        :return:
        """
    @property
    def FileAlignment(self) -> int:
        """

        :return:
        """
    @property
    def GlobalPointerTableDirectory(self) -> DirectoryEntry:
        """

        :return:
        """
    @property
    def ImageBase(self) -> int:
        """

        :return:
        """
    @property
    def ImportAddressTableDirectory(self) -> DirectoryEntry:
        """

        :return:
        """
    @property
    def ImportTableDirectory(self) -> DirectoryEntry:
        """

        :return:
        """
    @property
    def LoadConfigTableDirectory(self) -> DirectoryEntry:
        """

        :return:
        """
    @property
    def Magic(self) -> PEMagic:
        """

        :return:
        """
    @property
    def MajorImageVersion(self) -> int:
        """

        :return:
        """
    @property
    def MajorLinkerVersion(self) -> int:
        """

        :return:
        """
    @property
    def MajorOperatingSystemVersion(self) -> int:
        """

        :return:
        """
    @property
    def MajorSubsystemVersion(self) -> int:
        """

        :return:
        """
    @property
    def MinorImageVersion(self) -> int:
        """

        :return:
        """
    @property
    def MinorLinkerVersion(self) -> int:
        """

        :return:
        """
    @property
    def MinorOperatingSystemVersion(self) -> int:
        """

        :return:
        """
    @property
    def MinorSubsystemVersion(self) -> int:
        """

        :return:
        """
    @property
    def NumberOfRvaAndSizes(self) -> int:
        """

        :return:
        """
    @property
    def ResourceTableDirectory(self) -> DirectoryEntry:
        """

        :return:
        """
    @property
    def SectionAlignment(self) -> int:
        """

        :return:
        """
    @property
    def SizeOfCode(self) -> int:
        """

        :return:
        """
    @property
    def SizeOfHeaders(self) -> int:
        """

        :return:
        """
    @property
    def SizeOfHeapCommit(self) -> int:
        """

        :return:
        """
    @property
    def SizeOfHeapReserve(self) -> int:
        """

        :return:
        """
    @property
    def SizeOfImage(self) -> int:
        """

        :return:
        """
    @property
    def SizeOfInitializedData(self) -> int:
        """

        :return:
        """
    @property
    def SizeOfStackCommit(self) -> int:
        """

        :return:
        """
    @property
    def SizeOfStackReserve(self) -> int:
        """

        :return:
        """
    @property
    def SizeOfUninitializedData(self) -> int:
        """

        :return:
        """
    @property
    def Subsystem(self) -> Subsystem:
        """

        :return:
        """
    @property
    def ThreadLocalStorageTableDirectory(self) -> DirectoryEntry:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class PEHeaders(Object):
    """"""

    @overload
    def __init__(self, peStream: Stream):
        """

        :param peStream:
        """
    @overload
    def __init__(self, peStream: Stream, size: int):
        """

        :param peStream:
        :param size:
        """
    @overload
    def __init__(self, peStream: Stream, size: int, isLoadedImage: bool):
        """

        :param peStream:
        :param size:
        :param isLoadedImage:
        """
    @property
    def CoffHeader(self) -> CoffHeader:
        """

        :return:
        """
    @property
    def CoffHeaderStartOffset(self) -> int:
        """

        :return:
        """
    @property
    def CorHeader(self) -> CorHeader:
        """

        :return:
        """
    @property
    def CorHeaderStartOffset(self) -> int:
        """

        :return:
        """
    @property
    def IsCoffOnly(self) -> bool:
        """

        :return:
        """
    @property
    def IsConsoleApplication(self) -> bool:
        """

        :return:
        """
    @property
    def IsDll(self) -> bool:
        """

        :return:
        """
    @property
    def IsExe(self) -> bool:
        """

        :return:
        """
    @property
    def MetadataSize(self) -> int:
        """

        :return:
        """
    @property
    def MetadataStartOffset(self) -> int:
        """

        :return:
        """
    @property
    def PEHeader(self) -> PEHeader:
        """

        :return:
        """
    @property
    def PEHeaderStartOffset(self) -> int:
        """

        :return:
        """
    @property
    def SectionHeaders(self) -> ImmutableArray[SectionHeader]:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetContainingSectionIndex(self, relativeVirtualAddress: int) -> int:
        """

        :param relativeVirtualAddress:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def TryGetDirectoryOffset(self, directory: DirectoryEntry, offset: int) -> Tuple[bool, int]:
        """

        :param directory:
        :param offset:
        :return:
        """

class PEMagic(Enum):
    """"""

    PE32: PEMagic = ...
    """"""
    PE32Plus: PEMagic = ...
    """"""

class PEMemoryBlock(ValueType):
    """"""

    @property
    def Length(self) -> int:
        """

        :return:
        """
    @property
    def Pointer(self) -> int:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetReader(self) -> BlobReader:
        """

        :return:
        """
    @overload
    def GetReader(self, start: int, length: int) -> BlobReader:
        """

        :param start:
        :param length:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class PEReader(Object, IDisposable):
    """"""

    @overload
    def __init__(self, peImage: ImmutableArray[int]):
        """

        :param peImage:
        """
    @overload
    def __init__(self, peStream: Stream):
        """

        :param peStream:
        """
    @overload
    def __init__(self, peStream: Stream, options: PEStreamOptions):
        """

        :param peStream:
        :param options:
        """
    @overload
    def __init__(self, peImage: int, size: int):
        """

        :param peImage:
        :param size:
        """
    @overload
    def __init__(self, peStream: Stream, options: PEStreamOptions, size: int):
        """

        :param peStream:
        :param options:
        :param size:
        """
    @overload
    def __init__(self, peImage: int, size: int, isLoadedImage: bool):
        """

        :param peImage:
        :param size:
        :param isLoadedImage:
        """
    @property
    def HasMetadata(self) -> bool:
        """

        :return:
        """
    @property
    def IsEntireImageAvailable(self) -> bool:
        """

        :return:
        """
    @property
    def IsLoadedImage(self) -> bool:
        """

        :return:
        """
    @property
    def PEHeaders(self) -> PEHeaders:
        """

        :return:
        """
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetEntireImage(self) -> PEMemoryBlock:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetMetadata(self) -> PEMemoryBlock:
        """

        :return:
        """
    @overload
    def GetSectionData(self, relativeVirtualAddress: int) -> PEMemoryBlock:
        """

        :param relativeVirtualAddress:
        :return:
        """
    @overload
    def GetSectionData(self, sectionName: str) -> PEMemoryBlock:
        """

        :param sectionName:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ReadCodeViewDebugDirectoryData(
        self, entry: DebugDirectoryEntry
    ) -> CodeViewDebugDirectoryData:
        """

        :param entry:
        :return:
        """
    def ReadDebugDirectory(self) -> ImmutableArray[DebugDirectoryEntry]:
        """

        :return:
        """
    def ReadEmbeddedPortablePdbDebugDirectoryData(
        self, entry: DebugDirectoryEntry
    ) -> MetadataReaderProvider:
        """

        :param entry:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def TryOpenAssociatedPortablePdb(
        self,
        peImagePath: str,
        pdbFileStreamProvider: Func[str, Stream],
        pdbReaderProvider: MetadataReaderProvider,
        pdbPath: str,
    ) -> Tuple[bool, MetadataReaderProvider, str]:
        """

        :param peImagePath:
        :param pdbFileStreamProvider:
        :param pdbReaderProvider:
        :param pdbPath:
        :return:
        """

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

class PEStreamOptionsExtensions(ABC, Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @classmethod
    def IsValid(cls, options: PEStreamOptions) -> bool:
        """

        :param options:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

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

class SectionHeader(ValueType):
    """"""

    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def NumberOfLineNumbers(self) -> int:
        """

        :return:
        """
    @property
    def NumberOfRelocations(self) -> int:
        """

        :return:
        """
    @property
    def PointerToLineNumbers(self) -> int:
        """

        :return:
        """
    @property
    def PointerToRawData(self) -> int:
        """

        :return:
        """
    @property
    def PointerToRelocations(self) -> int:
        """

        :return:
        """
    @property
    def SectionCharacteristics(self) -> SectionCharacteristics:
        """

        :return:
        """
    @property
    def SizeOfRawData(self) -> int:
        """

        :return:
        """
    @property
    def VirtualAddress(self) -> int:
        """

        :return:
        """
    @property
    def VirtualSize(self) -> int:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

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
