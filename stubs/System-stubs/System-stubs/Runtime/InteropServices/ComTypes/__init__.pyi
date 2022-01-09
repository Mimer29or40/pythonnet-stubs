from __future__ import annotations

from typing import List, Protocol, Tuple, Union

from System import Array, Boolean, Enum, Int16, Int32, IntPtr, Object, ValueType, Void
from System.Runtime.InteropServices.ComTypes import IMoniker

# ---------- Types ---------- #

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
IntType = Union[int, Int32]
NIntType = Union[int, IntPtr]
ObjectType = Object
ShortType = Union[int, Int16]
VoidType = Union[None, Void]

# No Classes

# ---------- Structs ---------- #

class FORMATETC(ValueType):
    # ---------- Fields ---------- #
    
    @property
    def cfFormat(self) -> ShortType: ...
    
    @cfFormat.setter
    def cfFormat(self, value: ShortType) -> None: ...
    
    @property
    def dwAspect(self) -> DVASPECT: ...
    
    @dwAspect.setter
    def dwAspect(self, value: DVASPECT) -> None: ...
    
    @property
    def lindex(self) -> IntType: ...
    
    @lindex.setter
    def lindex(self, value: IntType) -> None: ...
    
    @property
    def ptd(self) -> NIntType: ...
    
    @ptd.setter
    def ptd(self, value: NIntType) -> None: ...
    
    @property
    def tymed(self) -> TYMED: ...
    
    @tymed.setter
    def tymed(self, value: TYMED) -> None: ...
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class STATDATA(ValueType):
    # ---------- Fields ---------- #
    
    @property
    def advSink(self) -> IAdviseSink: ...
    
    @advSink.setter
    def advSink(self, value: IAdviseSink) -> None: ...
    
    @property
    def advf(self) -> ADVF: ...
    
    @advf.setter
    def advf(self, value: ADVF) -> None: ...
    
    @property
    def connection(self) -> IntType: ...
    
    @connection.setter
    def connection(self, value: IntType) -> None: ...
    
    @property
    def formatetc(self) -> FORMATETC: ...
    
    @formatetc.setter
    def formatetc(self, value: FORMATETC) -> None: ...
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class STGMEDIUM(ValueType):
    # ---------- Fields ---------- #
    
    @property
    def pUnkForRelease(self) -> ObjectType: ...
    
    @pUnkForRelease.setter
    def pUnkForRelease(self, value: ObjectType) -> None: ...
    
    @property
    def tymed(self) -> TYMED: ...
    
    @tymed.setter
    def tymed(self, value: TYMED) -> None: ...
    
    @property
    def unionmember(self) -> NIntType: ...
    
    @unionmember.setter
    def unionmember(self, value: NIntType) -> None: ...
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# ---------- Interfaces ---------- #

class IAdviseSink(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def OnClose(self) -> VoidType: ...
    
    def OnDataChange(self, format: FORMATETC, stgmedium: STGMEDIUM) -> Tuple[VoidType, FORMATETC, STGMEDIUM]: ...
    
    def OnRename(self, moniker: IMoniker) -> VoidType: ...
    
    def OnSave(self) -> VoidType: ...
    
    def OnViewChange(self, aspect: IntType, index: IntType) -> VoidType: ...
    
    # No Events


class IDataObject(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def DAdvise(self, pFormatetc: FORMATETC, advf: ADVF, adviseSink: IAdviseSink, connection: IntType) -> Tuple[IntType, FORMATETC, IntType]: ...
    
    def DUnadvise(self, connection: IntType) -> VoidType: ...
    
    def EnumDAdvise(self, enumAdvise: IEnumSTATDATA) -> Tuple[IntType, IEnumSTATDATA]: ...
    
    def EnumFormatEtc(self, direction: DATADIR) -> IEnumFORMATETC: ...
    
    def GetCanonicalFormatEtc(self, formatIn: FORMATETC, formatOut: FORMATETC) -> Tuple[IntType, FORMATETC, FORMATETC]: ...
    
    def GetData(self, format: FORMATETC, medium: STGMEDIUM) -> Tuple[VoidType, FORMATETC, STGMEDIUM]: ...
    
    def GetDataHere(self, format: FORMATETC, medium: STGMEDIUM) -> Tuple[VoidType, FORMATETC, STGMEDIUM]: ...
    
    def QueryGetData(self, format: FORMATETC) -> Tuple[IntType, FORMATETC]: ...
    
    def SetData(self, formatIn: FORMATETC, medium: STGMEDIUM, release: BooleanType) -> Tuple[VoidType, FORMATETC, STGMEDIUM]: ...
    
    # No Events


class IEnumFORMATETC(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Clone(self, newEnum: IEnumFORMATETC) -> Tuple[VoidType, IEnumFORMATETC]: ...
    
    def Next(self, celt: IntType, rgelt: ArrayType[FORMATETC], pceltFetched: ArrayType[IntType]) -> Tuple[IntType, ArrayType[FORMATETC], ArrayType[IntType]]: ...
    
    def Reset(self) -> IntType: ...
    
    def Skip(self, celt: IntType) -> IntType: ...
    
    # No Events


class IEnumSTATDATA(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Clone(self, newEnum: IEnumSTATDATA) -> Tuple[VoidType, IEnumSTATDATA]: ...
    
    def Next(self, celt: IntType, rgelt: ArrayType[STATDATA], pceltFetched: ArrayType[IntType]) -> Tuple[IntType, ArrayType[STATDATA], ArrayType[IntType]]: ...
    
    def Reset(self) -> IntType: ...
    
    def Skip(self, celt: IntType) -> IntType: ...
    
    # No Events


# ---------- Enums ---------- #

class ADVF(Enum):
    ADVF_NODATA: IntType = 1
    ADVF_PRIMEFIRST: IntType = 2
    ADVF_ONLYONCE: IntType = 4
    ADVFCACHE_NOHANDLER: IntType = 8
    ADVFCACHE_FORCEBUILTIN: IntType = 16
    ADVFCACHE_ONSAVE: IntType = 32
    ADVF_DATAONSTOP: IntType = 64


class DATADIR(Enum):
    DATADIR_GET: IntType = 1
    DATADIR_SET: IntType = 2


class DVASPECT(Enum):
    DVASPECT_CONTENT: IntType = 1
    DVASPECT_THUMBNAIL: IntType = 2
    DVASPECT_ICON: IntType = 4
    DVASPECT_DOCPRINT: IntType = 8


class TYMED(Enum):
    TYMED_NULL: IntType = 0
    TYMED_HGLOBAL: IntType = 1
    TYMED_FILE: IntType = 2
    TYMED_ISTREAM: IntType = 4
    TYMED_ISTORAGE: IntType = 8
    TYMED_GDI: IntType = 16
    TYMED_MFPICT: IntType = 32
    TYMED_ENHMF: IntType = 64


# No Delegates

__all__ = [
    FORMATETC,
    STATDATA,
    STGMEDIUM,
    IAdviseSink,
    IDataObject,
    IEnumFORMATETC,
    IEnumSTATDATA,
    ADVF,
    DATADIR,
    DVASPECT,
    TYMED,
]
