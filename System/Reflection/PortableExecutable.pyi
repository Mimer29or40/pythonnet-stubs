__all__ = [
    'CoffHeader',
    'CorHeader',
    'DebugDirectoryBuilder',
    'ManagedPEBuilder',
    'PEBuilder',
    'PEDirectoriesBuilder',
    'PEHeader',
    'PEHeaderBuilder',
    'PEHeaders',
    'PEReader',
    'ResourceSectionBuilder',
    'CodeViewDebugDirectoryData',
    'DebugDirectoryEntry',
    'DirectoryEntry',
    'PdbChecksumDebugDirectoryData',
    'PEMemoryBlock',
    'SectionHeader',
    'SectionLocation',
    'Characteristics',
    'CorFlags',
    'DebugDirectoryEntryType',
    'DllCharacteristics',
    'Machine',
    'PEMagic',
    'PEStreamOptions',
    'SectionCharacteristics',
    'Subsystem',
]


# TODO

# ---------- CLASSES ---------- #

class CoffHeader:
    """Represents the header of a COFF file."""


class CorHeader:
    """"""


class DebugDirectoryBuilder:
    """"""


class ManagedPEBuilder:
    """"""


class PEBuilder:
    """"""
    
    # ---------- STRUCTS ---------- #
    
    class Section:
        """"""


class PEDirectoriesBuilder:
    """Builds PE directories."""


class PEHeader:
    """"""


class PEHeaderBuilder:
    """Defines the header for a portable executable (PE) file."""


class PEHeaders:
    """Defines a type that reads PE (Portable Executable) and COFF (Common Object File Format) headers from a stream."""


class PEReader:
    """Provides a reader for Portable Executable format (PE) files."""


class ResourceSectionBuilder:
    """Defines the base class for a PE resource section builder. Derive from ResourceSectionBuilder to provide serialization logic for native resources."""


# ---------- STRUCTS ---------- #

class CodeViewDebugDirectoryData:
    """Provides information about a Program Debug Database (PDB) file."""


class DebugDirectoryEntry:
    """Identifies the location, size and format of a block of debug information."""


class DirectoryEntry:
    """"""


class PdbChecksumDebugDirectoryData:
    """Represents a PDB Checksum debug directory entry."""


class PEMemoryBlock:
    """"""


class SectionHeader:
    """Provides information about the section header of a PE/COFF file."""


class SectionLocation:
    """"""


# ---------- ENUMS ---------- #

class Characteristics:
    """"""


class CorFlags:
    """COR20Flags."""


class DebugDirectoryEntryType:
    """An enumeration that describes the format of the debugging information of a DebugDirectoryEntry."""


class DllCharacteristics:
    """Describes the characteristics of a dynamic link library."""


class Machine:
    """Specifies the target machine's CPU architecture."""


class PEMagic:
    """"""


class PEStreamOptions:
    """Provides options that specify how sections of a PE image are read from a stream."""


class SectionCharacteristics:
    """"""


class Subsystem:
    """Describes the subsystem requirement for the image."""
