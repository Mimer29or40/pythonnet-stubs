"""Automatically generated stubs for C# namespace: System.Runtime.InteropServices.ComTypes."""

from collections.abc import Iterator
from typing import ClassVar
from typing import Final
from typing import overload

from System import Array
from System import Delegate
from System import Enum
from System import Guid
from System import Int16
from System import Int32
from System import Int64
from System import IntPtr
from System import Object
from System import String
from System import Type
from System import ValueType
from System.Collections import IEnumerator
from System.Globalization import CultureInfo
from System.Reflection import Binder
from System.Reflection import BindingFlags
from System.Reflection import FieldInfo
from System.Reflection import MemberInfo
from System.Reflection import MethodInfo
from System.Reflection import ParameterModifier
from System.Reflection import PropertyInfo

class ADVF(Enum):
    """"""

    ADVF_NODATA: ADVF = ...
    """"""
    ADVF_PRIMEFIRST: ADVF = ...
    """"""
    ADVF_ONLYONCE: ADVF = ...
    """"""
    ADVFCACHE_NOHANDLER: ADVF = ...
    """"""
    ADVFCACHE_FORCEBUILTIN: ADVF = ...
    """"""
    ADVFCACHE_ONSAVE: ADVF = ...
    """"""
    ADVF_DATAONSTOP: ADVF = ...
    """"""

class BINDPTR(ValueType):
    """"""

    lpfuncdesc: Final[IntPtr]
    """"""
    lptcomp: Final[IntPtr]
    """"""
    lpvardesc: Final[IntPtr]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class BIND_OPTS(ValueType):
    """"""

    cbStruct: Final[int]
    """"""
    dwTickCountDeadline: Final[int]
    """"""
    grfFlags: Final[int]
    """"""
    grfMode: Final[int]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class CALLCONV(Enum):
    """"""

    CC_CDECL: CALLCONV = ...
    """"""
    CC_MSCPASCAL: CALLCONV = ...
    """"""
    CC_PASCAL: CALLCONV = ...
    """"""
    CC_MACPASCAL: CALLCONV = ...
    """"""
    CC_STDCALL: CALLCONV = ...
    """"""
    CC_RESERVED: CALLCONV = ...
    """"""
    CC_SYSCALL: CALLCONV = ...
    """"""
    CC_MPWCDECL: CALLCONV = ...
    """"""
    CC_MPWPASCAL: CALLCONV = ...
    """"""
    CC_MAX: CALLCONV = ...
    """"""

class CONNECTDATA(ValueType):
    """"""

    dwCookie: Final[int]
    """"""
    pUnk: Final[object]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class DATADIR(Enum):
    """"""

    DATADIR_GET: DATADIR = ...
    """"""
    DATADIR_SET: DATADIR = ...
    """"""

class DESCKIND(Enum):
    """"""

    DESCKIND_NONE: DESCKIND = ...
    """"""
    DESCKIND_FUNCDESC: DESCKIND = ...
    """"""
    DESCKIND_VARDESC: DESCKIND = ...
    """"""
    DESCKIND_TYPECOMP: DESCKIND = ...
    """"""
    DESCKIND_IMPLICITAPPOBJ: DESCKIND = ...
    """"""
    DESCKIND_MAX: DESCKIND = ...
    """"""

class DISPPARAMS(ValueType):
    """"""

    cArgs: Final[int]
    """"""
    cNamedArgs: Final[int]
    """"""
    rgdispidNamedArgs: Final[IntPtr]
    """"""
    rgvarg: Final[IntPtr]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class DVASPECT(Enum):
    """"""

    DVASPECT_CONTENT: DVASPECT = ...
    """"""
    DVASPECT_THUMBNAIL: DVASPECT = ...
    """"""
    DVASPECT_ICON: DVASPECT = ...
    """"""
    DVASPECT_DOCPRINT: DVASPECT = ...
    """"""

class ELEMDESC(ValueType):
    """"""

    desc: Final[ELEMDESC.DESCUNION]
    """"""
    tdesc: Final[TYPEDESC]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    class DESCUNION(ValueType):
        """"""

        idldesc: Final[IDLDESC]
        """"""
        paramdesc: Final[PARAMDESC]
        """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def ToString(self) -> str:
            """"""

class EXCEPINFO(ValueType):
    """"""

    bstrDescription: Final[str]
    """"""
    bstrHelpFile: Final[str]
    """"""
    bstrSource: Final[str]
    """"""
    dwHelpContext: Final[int]
    """"""
    pfnDeferredFillIn: Final[IntPtr]
    """"""
    pvReserved: Final[IntPtr]
    """"""
    scode: Final[int]
    """"""
    wCode: Final[int]
    """"""
    wReserved: Final[int]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class FILETIME(ValueType):
    """"""

    dwHighDateTime: Final[int]
    """"""
    dwLowDateTime: Final[int]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class FORMATETC(ValueType):
    """"""

    cfFormat: Final[int]
    """"""
    dwAspect: Final[DVASPECT]
    """"""
    lindex: Final[int]
    """"""
    ptd: Final[IntPtr]
    """"""
    tymed: Final[TYMED]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class FUNCDESC(ValueType):
    """"""

    cParams: Final[int]
    """"""
    cParamsOpt: Final[int]
    """"""
    cScodes: Final[int]
    """"""
    callconv: Final[CALLCONV]
    """"""
    elemdescFunc: Final[ELEMDESC]
    """"""
    funckind: Final[FUNCKIND]
    """"""
    invkind: Final[INVOKEKIND]
    """"""
    lprgelemdescParam: Final[IntPtr]
    """"""
    lprgscode: Final[IntPtr]
    """"""
    memid: Final[int]
    """"""
    oVft: Final[int]
    """"""
    wFuncFlags: Final[int]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class FUNCFLAGS(Enum):
    """"""

    FUNCFLAG_FRESTRICTED: FUNCFLAGS = ...
    """"""
    FUNCFLAG_FSOURCE: FUNCFLAGS = ...
    """"""
    FUNCFLAG_FBINDABLE: FUNCFLAGS = ...
    """"""
    FUNCFLAG_FREQUESTEDIT: FUNCFLAGS = ...
    """"""
    FUNCFLAG_FDISPLAYBIND: FUNCFLAGS = ...
    """"""
    FUNCFLAG_FDEFAULTBIND: FUNCFLAGS = ...
    """"""
    FUNCFLAG_FHIDDEN: FUNCFLAGS = ...
    """"""
    FUNCFLAG_FUSESGETLASTERROR: FUNCFLAGS = ...
    """"""
    FUNCFLAG_FDEFAULTCOLLELEM: FUNCFLAGS = ...
    """"""
    FUNCFLAG_FUIDEFAULT: FUNCFLAGS = ...
    """"""
    FUNCFLAG_FNONBROWSABLE: FUNCFLAGS = ...
    """"""
    FUNCFLAG_FREPLACEABLE: FUNCFLAGS = ...
    """"""
    FUNCFLAG_FIMMEDIATEBIND: FUNCFLAGS = ...
    """"""

class FUNCKIND(Enum):
    """"""

    FUNC_VIRTUAL: FUNCKIND = ...
    """"""
    FUNC_PUREVIRTUAL: FUNCKIND = ...
    """"""
    FUNC_NONVIRTUAL: FUNCKIND = ...
    """"""
    FUNC_STATIC: FUNCKIND = ...
    """"""
    FUNC_DISPATCH: FUNCKIND = ...
    """"""

class IAdviseSink:
    """"""
    def OnClose(self) -> None:
        """"""
    def OnDataChange(self, format: FORMATETC, stgmedium: STGMEDIUM) -> None:
        """"""
    def OnRename(self, moniker: IMoniker) -> None:
        """"""
    def OnSave(self) -> None:
        """"""
    def OnViewChange(self, aspect: int, index: int) -> None:
        """"""

class IBindCtx:
    """"""
    def EnumObjectParam(self, ppenum: IEnumString) -> tuple[None, IEnumString]:
        """"""
    def GetBindOptions(self, pbindopts: BIND_OPTS) -> None:
        """"""
    def GetObjectParam(self, pszKey: str, ppunk: Object) -> tuple[None, Object]:
        """"""
    def GetRunningObjectTable(self, pprot: IRunningObjectTable) -> tuple[None, IRunningObjectTable]:
        """"""
    def RegisterObjectBound(self, punk: object) -> None:
        """"""
    def RegisterObjectParam(self, pszKey: str, punk: object) -> None:
        """"""
    def ReleaseBoundObjects(self) -> None:
        """"""
    def RevokeObjectBound(self, punk: object) -> None:
        """"""
    def RevokeObjectParam(self, pszKey: str) -> int:
        """"""
    def SetBindOptions(self, pbindopts: BIND_OPTS) -> None:
        """"""

class IConnectionPoint:
    """"""
    def Advise(self, pUnkSink: object, pdwCookie: Int32) -> tuple[None, Int32]:
        """"""
    def EnumConnections(self, ppEnum: IEnumConnections) -> tuple[None, IEnumConnections]:
        """"""
    def GetConnectionInterface(self, pIID: Guid) -> tuple[None, Guid]:
        """"""
    def GetConnectionPointContainer(
        self, ppCPC: IConnectionPointContainer
    ) -> tuple[None, IConnectionPointContainer]:
        """"""
    def Unadvise(self, dwCookie: int) -> None:
        """"""

class IConnectionPointContainer:
    """"""
    def EnumConnectionPoints(
        self, ppEnum: IEnumConnectionPoints
    ) -> tuple[None, IEnumConnectionPoints]:
        """"""
    def FindConnectionPoint(
        self, riid: Guid, ppCP: IConnectionPoint
    ) -> tuple[None, IConnectionPoint]:
        """"""

class IDLDESC(ValueType):
    """"""

    dwReserved: Final[IntPtr]
    """"""
    wIDLFlags: Final[IDLFLAG]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class IDLFLAG(Enum):
    """"""

    IDLFLAG_NONE: IDLFLAG = ...
    """"""
    IDLFLAG_FIN: IDLFLAG = ...
    """"""
    IDLFLAG_FOUT: IDLFLAG = ...
    """"""
    IDLFLAG_FLCID: IDLFLAG = ...
    """"""
    IDLFLAG_FRETVAL: IDLFLAG = ...
    """"""

class IDataObject:
    """"""
    def DAdvise(
        self, pFormatetc: FORMATETC, advf: ADVF, adviseSink: IAdviseSink, connection: Int32
    ) -> tuple[int, Int32]:
        """"""
    def DUnadvise(self, connection: int) -> None:
        """"""
    def EnumDAdvise(self, enumAdvise: IEnumSTATDATA) -> tuple[int, IEnumSTATDATA]:
        """"""
    def EnumFormatEtc(self, direction: DATADIR) -> IEnumFORMATETC:
        """"""
    def GetCanonicalFormatEtc(
        self, formatIn: FORMATETC, formatOut: FORMATETC
    ) -> tuple[int, FORMATETC]:
        """"""
    def GetData(self, format: FORMATETC, medium: STGMEDIUM) -> tuple[None, STGMEDIUM]:
        """"""
    def GetDataHere(self, format: FORMATETC, medium: STGMEDIUM) -> None:
        """"""
    def QueryGetData(self, format: FORMATETC) -> int:
        """"""
    def SetData(self, formatIn: FORMATETC, medium: STGMEDIUM, release: bool) -> None:
        """"""

class IEnumConnectionPoints:
    """"""
    def Clone(self, ppenum: IEnumConnectionPoints) -> tuple[None, IEnumConnectionPoints]:
        """"""
    def Next(
        self, celt: int, rgelt: Array[IConnectionPoint], pceltFetched: IntPtr
    ) -> tuple[int, Array[IConnectionPoint]]:
        """"""
    def Reset(self) -> None:
        """"""
    def Skip(self, celt: int) -> int:
        """"""

class IEnumConnections:
    """"""
    def Clone(self, ppenum: IEnumConnections) -> tuple[None, IEnumConnections]:
        """"""
    def Next(
        self, celt: int, rgelt: Array[CONNECTDATA], pceltFetched: IntPtr
    ) -> tuple[int, Array[CONNECTDATA]]:
        """"""
    def Reset(self) -> None:
        """"""
    def Skip(self, celt: int) -> int:
        """"""

class IEnumFORMATETC:
    """"""
    def Clone(self, newEnum: IEnumFORMATETC) -> tuple[None, IEnumFORMATETC]:
        """"""
    def Next(
        self, celt: int, rgelt: Array[FORMATETC], pceltFetched: Array[int]
    ) -> tuple[int, Array[FORMATETC], Array[int]]:
        """"""
    def Reset(self) -> int:
        """"""
    def Skip(self, celt: int) -> int:
        """"""

class IEnumMoniker:
    """"""
    def Clone(self, ppenum: IEnumMoniker) -> tuple[None, IEnumMoniker]:
        """"""
    def Next(
        self, celt: int, rgelt: Array[IMoniker], pceltFetched: IntPtr
    ) -> tuple[int, Array[IMoniker]]:
        """"""
    def Reset(self) -> None:
        """"""
    def Skip(self, celt: int) -> int:
        """"""

class IEnumSTATDATA:
    """"""
    def Clone(self, newEnum: IEnumSTATDATA) -> tuple[None, IEnumSTATDATA]:
        """"""
    def Next(
        self, celt: int, rgelt: Array[STATDATA], pceltFetched: Array[int]
    ) -> tuple[int, Array[STATDATA], Array[int]]:
        """"""
    def Reset(self) -> int:
        """"""
    def Skip(self, celt: int) -> int:
        """"""

class IEnumString:
    """"""
    def Clone(self, ppenum: IEnumString) -> tuple[None, IEnumString]:
        """"""
    def Next(self, celt: int, rgelt: Array[str], pceltFetched: IntPtr) -> tuple[int, Array[str]]:
        """"""
    def Reset(self) -> None:
        """"""
    def Skip(self, celt: int) -> int:
        """"""

class IEnumVARIANT:
    """"""
    def Clone(self) -> IEnumVARIANT:
        """"""
    def Next(
        self, celt: int, rgVar: Array[object], pceltFetched: IntPtr
    ) -> tuple[int, Array[object]]:
        """"""
    def Reset(self) -> int:
        """"""
    def Skip(self, celt: int) -> int:
        """"""

class IEnumerable:
    """"""
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def __iter__(self) -> Iterator:
        """"""

class IEnumerator:
    """"""
    @property
    def Current(self) -> object:
        """"""
    def MoveNext(self) -> bool:
        """"""
    def Reset(self) -> None:
        """"""

class IExpando(IReflect):
    """"""
    @property
    def UnderlyingSystemType(self) -> Type:
        """"""
    def AddField(self, name: str) -> FieldInfo:
        """"""
    def AddMethod(self, name: str, method: Delegate) -> MethodInfo:
        """"""
    def AddProperty(self, name: str) -> PropertyInfo:
        """"""
    def GetField(self, name: str, bindingAttr: BindingFlags) -> FieldInfo:
        """"""
    def GetFields(self, bindingAttr: BindingFlags) -> Array[FieldInfo]:
        """"""
    def GetMember(self, name: str, bindingAttr: BindingFlags) -> Array[MemberInfo]:
        """"""
    def GetMembers(self, bindingAttr: BindingFlags) -> Array[MemberInfo]:
        """"""
    @overload
    def GetMethod(self, name: str, bindingAttr: BindingFlags) -> MethodInfo:
        """"""
    @overload
    def GetMethod(
        self,
        name: str,
        bindingAttr: BindingFlags,
        binder: Binder,
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> MethodInfo:
        """"""
    def GetMethods(self, bindingAttr: BindingFlags) -> Array[MethodInfo]:
        """"""
    def GetProperties(self, bindingAttr: BindingFlags) -> Array[PropertyInfo]:
        """"""
    @overload
    def GetProperty(self, name: str, bindingAttr: BindingFlags) -> PropertyInfo:
        """"""
    @overload
    def GetProperty(
        self,
        name: str,
        bindingAttr: BindingFlags,
        binder: Binder,
        returnType: Type,
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> PropertyInfo:
        """"""
    def InvokeMember(
        self,
        name: str,
        invokeAttr: BindingFlags,
        binder: Binder,
        target: object,
        args: Array[object],
        modifiers: Array[ParameterModifier],
        culture: CultureInfo,
        namedParameters: Array[str],
    ) -> object:
        """"""
    def RemoveMember(self, m: MemberInfo) -> None:
        """"""

class IMPLTYPEFLAGS(Enum):
    """"""

    IMPLTYPEFLAG_FDEFAULT: IMPLTYPEFLAGS = ...
    """"""
    IMPLTYPEFLAG_FSOURCE: IMPLTYPEFLAGS = ...
    """"""
    IMPLTYPEFLAG_FRESTRICTED: IMPLTYPEFLAGS = ...
    """"""
    IMPLTYPEFLAG_FDEFAULTVTABLE: IMPLTYPEFLAGS = ...
    """"""

class IMoniker:
    """"""
    def BindToObject(
        self, pbc: IBindCtx, pmkToLeft: IMoniker, riidResult: Guid, ppvResult: Object
    ) -> tuple[None, Object]:
        """"""
    def BindToStorage(
        self, pbc: IBindCtx, pmkToLeft: IMoniker, riid: Guid, ppvObj: Object
    ) -> tuple[None, Object]:
        """"""
    def CommonPrefixWith(self, pmkOther: IMoniker, ppmkPrefix: IMoniker) -> tuple[None, IMoniker]:
        """"""
    def ComposeWith(
        self, pmkRight: IMoniker, fOnlyIfNotGeneric: bool, ppmkComposite: IMoniker
    ) -> tuple[None, IMoniker]:
        """"""
    def Enum(self, fForward: bool, ppenumMoniker: IEnumMoniker) -> tuple[None, IEnumMoniker]:
        """"""
    def GetClassID(self, pClassID: Guid) -> tuple[None, Guid]:
        """"""
    def GetDisplayName(
        self, pbc: IBindCtx, pmkToLeft: IMoniker, ppszDisplayName: String
    ) -> tuple[None, String]:
        """"""
    def GetSizeMax(self, pcbSize: Int64) -> tuple[None, Int64]:
        """"""
    def GetTimeOfLastChange(
        self, pbc: IBindCtx, pmkToLeft: IMoniker, pFileTime: FILETIME
    ) -> tuple[None, FILETIME]:
        """"""
    def Hash(self, pdwHash: Int32) -> tuple[None, Int32]:
        """"""
    def Inverse(self, ppmk: IMoniker) -> tuple[None, IMoniker]:
        """"""
    def IsDirty(self) -> int:
        """"""
    def IsEqual(self, pmkOtherMoniker: IMoniker) -> int:
        """"""
    def IsRunning(self, pbc: IBindCtx, pmkToLeft: IMoniker, pmkNewlyRunning: IMoniker) -> int:
        """"""
    def IsSystemMoniker(self, pdwMksys: Int32) -> tuple[int, Int32]:
        """"""
    def Load(self, pStm: IStream) -> None:
        """"""
    def ParseDisplayName(
        self,
        pbc: IBindCtx,
        pmkToLeft: IMoniker,
        pszDisplayName: str,
        pchEaten: Int32,
        ppmkOut: IMoniker,
    ) -> tuple[None, Int32, IMoniker]:
        """"""
    def Reduce(
        self, pbc: IBindCtx, dwReduceHowFar: int, ppmkToLeft: IMoniker, ppmkReduced: IMoniker
    ) -> tuple[None, IMoniker]:
        """"""
    def RelativePathTo(self, pmkOther: IMoniker, ppmkRelPath: IMoniker) -> tuple[None, IMoniker]:
        """"""
    def Save(self, pStm: IStream, fClearDirty: bool) -> None:
        """"""

class INVOKEKIND(Enum):
    """"""

    INVOKE_FUNC: INVOKEKIND = ...
    """"""
    INVOKE_PROPERTYGET: INVOKEKIND = ...
    """"""
    INVOKE_PROPERTYPUT: INVOKEKIND = ...
    """"""
    INVOKE_PROPERTYPUTREF: INVOKEKIND = ...
    """"""

class IPersistFile:
    """"""
    def GetClassID(self, pClassID: Guid) -> tuple[None, Guid]:
        """"""
    def GetCurFile(self, ppszFileName: String) -> tuple[None, String]:
        """"""
    def IsDirty(self) -> int:
        """"""
    def Load(self, pszFileName: str, dwMode: int) -> None:
        """"""
    def Save(self, pszFileName: str, fRemember: bool) -> None:
        """"""
    def SaveCompleted(self, pszFileName: str) -> None:
        """"""

class IReflect:
    """"""
    @property
    def UnderlyingSystemType(self) -> Type:
        """"""
    def GetField(self, name: str, bindingAttr: BindingFlags) -> FieldInfo:
        """"""
    def GetFields(self, bindingAttr: BindingFlags) -> Array[FieldInfo]:
        """"""
    def GetMember(self, name: str, bindingAttr: BindingFlags) -> Array[MemberInfo]:
        """"""
    def GetMembers(self, bindingAttr: BindingFlags) -> Array[MemberInfo]:
        """"""
    @overload
    def GetMethod(self, name: str, bindingAttr: BindingFlags) -> MethodInfo:
        """"""
    @overload
    def GetMethod(
        self,
        name: str,
        bindingAttr: BindingFlags,
        binder: Binder,
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> MethodInfo:
        """"""
    def GetMethods(self, bindingAttr: BindingFlags) -> Array[MethodInfo]:
        """"""
    def GetProperties(self, bindingAttr: BindingFlags) -> Array[PropertyInfo]:
        """"""
    @overload
    def GetProperty(self, name: str, bindingAttr: BindingFlags) -> PropertyInfo:
        """"""
    @overload
    def GetProperty(
        self,
        name: str,
        bindingAttr: BindingFlags,
        binder: Binder,
        returnType: Type,
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> PropertyInfo:
        """"""
    def InvokeMember(
        self,
        name: str,
        invokeAttr: BindingFlags,
        binder: Binder,
        target: object,
        args: Array[object],
        modifiers: Array[ParameterModifier],
        culture: CultureInfo,
        namedParameters: Array[str],
    ) -> object:
        """"""

class IRunningObjectTable:
    """"""
    def EnumRunning(self, ppenumMoniker: IEnumMoniker) -> tuple[None, IEnumMoniker]:
        """"""
    def GetObject(self, pmkObjectName: IMoniker, ppunkObject: Object) -> tuple[int, Object]:
        """"""
    def GetTimeOfLastChange(
        self, pmkObjectName: IMoniker, pfiletime: FILETIME
    ) -> tuple[int, FILETIME]:
        """"""
    def IsRunning(self, pmkObjectName: IMoniker) -> int:
        """"""
    def NoteChangeTime(self, dwRegister: int, pfiletime: FILETIME) -> None:
        """"""
    def Register(self, grfFlags: int, punkObject: object, pmkObjectName: IMoniker) -> int:
        """"""
    def Revoke(self, dwRegister: int) -> None:
        """"""

class IStream:
    """"""
    def Clone(self, ppstm: IStream) -> tuple[None, IStream]:
        """"""
    def Commit(self, grfCommitFlags: int) -> None:
        """"""
    def CopyTo(self, pstm: IStream, cb: int, pcbRead: IntPtr, pcbWritten: IntPtr) -> None:
        """"""
    def LockRegion(self, libOffset: int, cb: int, dwLockType: int) -> None:
        """"""
    def Read(self, pv: Array[int], cb: int, pcbRead: IntPtr) -> tuple[None, Array[int]]:
        """"""
    def Revert(self) -> None:
        """"""
    def Seek(self, dlibMove: int, dwOrigin: int, plibNewPosition: IntPtr) -> None:
        """"""
    def SetSize(self, libNewSize: int) -> None:
        """"""
    def Stat(self, pstatstg: STATSTG, grfStatFlag: int) -> tuple[None, STATSTG]:
        """"""
    def UnlockRegion(self, libOffset: int, cb: int, dwLockType: int) -> None:
        """"""
    def Write(self, pv: Array[int], cb: int, pcbWritten: IntPtr) -> None:
        """"""

class ITypeComp:
    """"""
    def Bind(
        self,
        szName: str,
        lHashVal: int,
        wFlags: int,
        ppTInfo: ITypeInfo,
        pDescKind: DESCKIND,
        pBindPtr: BINDPTR,
    ) -> tuple[None, ITypeInfo, DESCKIND, BINDPTR]:
        """"""
    def BindType(
        self, szName: str, lHashVal: int, ppTInfo: ITypeInfo, ppTComp: ITypeComp
    ) -> tuple[None, ITypeInfo, ITypeComp]:
        """"""

class ITypeInfo:
    """"""
    def AddressOfMember(self, memid: int, invKind: INVOKEKIND, ppv: IntPtr) -> tuple[None, IntPtr]:
        """"""
    def CreateInstance(self, pUnkOuter: object, riid: Guid, ppvObj: Object) -> tuple[None, Object]:
        """"""
    def GetContainingTypeLib(self, ppTLB: ITypeLib, pIndex: Int32) -> tuple[None, ITypeLib, Int32]:
        """"""
    def GetDllEntry(
        self,
        memid: int,
        invKind: INVOKEKIND,
        pBstrDllName: IntPtr,
        pBstrName: IntPtr,
        pwOrdinal: IntPtr,
    ) -> None:
        """"""
    def GetDocumentation(
        self,
        index: int,
        strName: String,
        strDocString: String,
        dwHelpContext: Int32,
        strHelpFile: String,
    ) -> tuple[None, String, String, Int32, String]:
        """"""
    def GetFuncDesc(self, index: int, ppFuncDesc: IntPtr) -> tuple[None, IntPtr]:
        """"""
    def GetIDsOfNames(
        self, rgszNames: Array[str], cNames: int, pMemId: Array[int]
    ) -> tuple[None, Array[int]]:
        """"""
    def GetImplTypeFlags(
        self, index: int, pImplTypeFlags: IMPLTYPEFLAGS
    ) -> tuple[None, IMPLTYPEFLAGS]:
        """"""
    def GetMops(self, memid: int, pBstrMops: String) -> tuple[None, String]:
        """"""
    def GetNames(
        self, memid: int, rgBstrNames: Array[str], cMaxNames: int, pcNames: Int32
    ) -> tuple[None, Array[str], Int32]:
        """"""
    def GetRefTypeInfo(self, hRef: int, ppTI: ITypeInfo) -> tuple[None, ITypeInfo]:
        """"""
    def GetRefTypeOfImplType(self, index: int, href: Int32) -> tuple[None, Int32]:
        """"""
    def GetTypeAttr(self, ppTypeAttr: IntPtr) -> tuple[None, IntPtr]:
        """"""
    def GetTypeComp(self, ppTComp: ITypeComp) -> tuple[None, ITypeComp]:
        """"""
    def GetVarDesc(self, index: int, ppVarDesc: IntPtr) -> tuple[None, IntPtr]:
        """"""
    def Invoke(
        self,
        pvInstance: object,
        memid: int,
        wFlags: int,
        pDispParams: DISPPARAMS,
        pVarResult: IntPtr,
        pExcepInfo: IntPtr,
        puArgErr: Int32,
    ) -> tuple[None, Int32]:
        """"""
    def ReleaseFuncDesc(self, pFuncDesc: IntPtr) -> None:
        """"""
    def ReleaseTypeAttr(self, pTypeAttr: IntPtr) -> None:
        """"""
    def ReleaseVarDesc(self, pVarDesc: IntPtr) -> None:
        """"""

class ITypeInfo2(ITypeInfo):
    """"""
    def AddressOfMember(self, memid: int, invKind: INVOKEKIND, ppv: IntPtr) -> tuple[None, IntPtr]:
        """"""
    def CreateInstance(self, pUnkOuter: object, riid: Guid, ppvObj: Object) -> tuple[None, Object]:
        """"""
    def GetAllCustData(self, pCustData: IntPtr) -> None:
        """"""
    def GetAllFuncCustData(self, index: int, pCustData: IntPtr) -> None:
        """"""
    def GetAllImplTypeCustData(self, index: int, pCustData: IntPtr) -> None:
        """"""
    def GetAllParamCustData(self, indexFunc: int, indexParam: int, pCustData: IntPtr) -> None:
        """"""
    def GetAllVarCustData(self, index: int, pCustData: IntPtr) -> None:
        """"""
    def GetContainingTypeLib(self, ppTLB: ITypeLib, pIndex: Int32) -> tuple[None, ITypeLib, Int32]:
        """"""
    def GetCustData(self, guid: Guid, pVarVal: Object) -> tuple[None, Object]:
        """"""
    def GetDllEntry(
        self,
        memid: int,
        invKind: INVOKEKIND,
        pBstrDllName: IntPtr,
        pBstrName: IntPtr,
        pwOrdinal: IntPtr,
    ) -> None:
        """"""
    def GetDocumentation(
        self,
        index: int,
        strName: String,
        strDocString: String,
        dwHelpContext: Int32,
        strHelpFile: String,
    ) -> tuple[None, String, String, Int32, String]:
        """"""
    def GetDocumentation2(
        self,
        memid: int,
        pbstrHelpString: String,
        pdwHelpStringContext: Int32,
        pbstrHelpStringDll: String,
    ) -> tuple[None, String, Int32, String]:
        """"""
    def GetFuncCustData(self, index: int, guid: Guid, pVarVal: Object) -> tuple[None, Object]:
        """"""
    def GetFuncDesc(self, index: int, ppFuncDesc: IntPtr) -> tuple[None, IntPtr]:
        """"""
    def GetFuncIndexOfMemId(
        self, memid: int, invKind: INVOKEKIND, pFuncIndex: Int32
    ) -> tuple[None, Int32]:
        """"""
    def GetIDsOfNames(
        self, rgszNames: Array[str], cNames: int, pMemId: Array[int]
    ) -> tuple[None, Array[int]]:
        """"""
    def GetImplTypeCustData(self, index: int, guid: Guid, pVarVal: Object) -> tuple[None, Object]:
        """"""
    def GetImplTypeFlags(
        self, index: int, pImplTypeFlags: IMPLTYPEFLAGS
    ) -> tuple[None, IMPLTYPEFLAGS]:
        """"""
    def GetMops(self, memid: int, pBstrMops: String) -> tuple[None, String]:
        """"""
    def GetNames(
        self, memid: int, rgBstrNames: Array[str], cMaxNames: int, pcNames: Int32
    ) -> tuple[None, Array[str], Int32]:
        """"""
    def GetParamCustData(
        self, indexFunc: int, indexParam: int, guid: Guid, pVarVal: Object
    ) -> tuple[None, Object]:
        """"""
    def GetRefTypeInfo(self, hRef: int, ppTI: ITypeInfo) -> tuple[None, ITypeInfo]:
        """"""
    def GetRefTypeOfImplType(self, index: int, href: Int32) -> tuple[None, Int32]:
        """"""
    def GetTypeAttr(self, ppTypeAttr: IntPtr) -> tuple[None, IntPtr]:
        """"""
    def GetTypeComp(self, ppTComp: ITypeComp) -> tuple[None, ITypeComp]:
        """"""
    def GetTypeFlags(self, pTypeFlags: Int32) -> tuple[None, Int32]:
        """"""
    def GetTypeKind(self, pTypeKind: TYPEKIND) -> tuple[None, TYPEKIND]:
        """"""
    def GetVarCustData(self, index: int, guid: Guid, pVarVal: Object) -> tuple[None, Object]:
        """"""
    def GetVarDesc(self, index: int, ppVarDesc: IntPtr) -> tuple[None, IntPtr]:
        """"""
    def GetVarIndexOfMemId(self, memid: int, pVarIndex: Int32) -> tuple[None, Int32]:
        """"""
    def Invoke(
        self,
        pvInstance: object,
        memid: int,
        wFlags: int,
        pDispParams: DISPPARAMS,
        pVarResult: IntPtr,
        pExcepInfo: IntPtr,
        puArgErr: Int32,
    ) -> tuple[None, Int32]:
        """"""
    def ReleaseFuncDesc(self, pFuncDesc: IntPtr) -> None:
        """"""
    def ReleaseTypeAttr(self, pTypeAttr: IntPtr) -> None:
        """"""
    def ReleaseVarDesc(self, pVarDesc: IntPtr) -> None:
        """"""

class ITypeLib:
    """"""
    def FindName(
        self,
        szNameBuf: str,
        lHashVal: int,
        ppTInfo: Array[ITypeInfo],
        rgMemId: Array[int],
        pcFound: Int16,
    ) -> tuple[None, Array[ITypeInfo], Array[int]]:
        """"""
    def GetDocumentation(
        self,
        index: int,
        strName: String,
        strDocString: String,
        dwHelpContext: Int32,
        strHelpFile: String,
    ) -> tuple[None, String, String, Int32, String]:
        """"""
    def GetLibAttr(self, ppTLibAttr: IntPtr) -> tuple[None, IntPtr]:
        """"""
    def GetTypeComp(self, ppTComp: ITypeComp) -> tuple[None, ITypeComp]:
        """"""
    def GetTypeInfo(self, index: int, ppTI: ITypeInfo) -> tuple[None, ITypeInfo]:
        """"""
    def GetTypeInfoCount(self) -> int:
        """"""
    def GetTypeInfoOfGuid(self, guid: Guid, ppTInfo: ITypeInfo) -> tuple[None, ITypeInfo]:
        """"""
    def GetTypeInfoType(self, index: int, pTKind: TYPEKIND) -> tuple[None, TYPEKIND]:
        """"""
    def IsName(self, szNameBuf: str, lHashVal: int) -> bool:
        """"""
    def ReleaseTLibAttr(self, pTLibAttr: IntPtr) -> None:
        """"""

class ITypeLib2(ITypeLib):
    """"""
    def FindName(
        self,
        szNameBuf: str,
        lHashVal: int,
        ppTInfo: Array[ITypeInfo],
        rgMemId: Array[int],
        pcFound: Int16,
    ) -> tuple[None, Array[ITypeInfo], Array[int]]:
        """"""
    def GetAllCustData(self, pCustData: IntPtr) -> None:
        """"""
    def GetCustData(self, guid: Guid, pVarVal: Object) -> tuple[None, Object]:
        """"""
    def GetDocumentation(
        self,
        index: int,
        strName: String,
        strDocString: String,
        dwHelpContext: Int32,
        strHelpFile: String,
    ) -> tuple[None, String, String, Int32, String]:
        """"""
    def GetDocumentation2(
        self,
        index: int,
        pbstrHelpString: String,
        pdwHelpStringContext: Int32,
        pbstrHelpStringDll: String,
    ) -> tuple[None, String, Int32, String]:
        """"""
    def GetLibAttr(self, ppTLibAttr: IntPtr) -> tuple[None, IntPtr]:
        """"""
    def GetLibStatistics(self, pcUniqueNames: IntPtr, pcchUniqueNames: Int32) -> tuple[None, Int32]:
        """"""
    def GetTypeComp(self, ppTComp: ITypeComp) -> tuple[None, ITypeComp]:
        """"""
    def GetTypeInfo(self, index: int, ppTI: ITypeInfo) -> tuple[None, ITypeInfo]:
        """"""
    def GetTypeInfoCount(self) -> int:
        """"""
    def GetTypeInfoOfGuid(self, guid: Guid, ppTInfo: ITypeInfo) -> tuple[None, ITypeInfo]:
        """"""
    def GetTypeInfoType(self, index: int, pTKind: TYPEKIND) -> tuple[None, TYPEKIND]:
        """"""
    def IsName(self, szNameBuf: str, lHashVal: int) -> bool:
        """"""
    def ReleaseTLibAttr(self, pTLibAttr: IntPtr) -> None:
        """"""

class LIBFLAGS(Enum):
    """"""

    LIBFLAG_FRESTRICTED: LIBFLAGS = ...
    """"""
    LIBFLAG_FCONTROL: LIBFLAGS = ...
    """"""
    LIBFLAG_FHIDDEN: LIBFLAGS = ...
    """"""
    LIBFLAG_FHASDISKIMAGE: LIBFLAGS = ...
    """"""

class PARAMDESC(ValueType):
    """"""

    lpVarValue: Final[IntPtr]
    """"""
    wParamFlags: Final[PARAMFLAG]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class PARAMFLAG(Enum):
    """"""

    PARAMFLAG_NONE: PARAMFLAG = ...
    """"""
    PARAMFLAG_FIN: PARAMFLAG = ...
    """"""
    PARAMFLAG_FOUT: PARAMFLAG = ...
    """"""
    PARAMFLAG_FLCID: PARAMFLAG = ...
    """"""
    PARAMFLAG_FRETVAL: PARAMFLAG = ...
    """"""
    PARAMFLAG_FOPT: PARAMFLAG = ...
    """"""
    PARAMFLAG_FHASDEFAULT: PARAMFLAG = ...
    """"""
    PARAMFLAG_FHASCUSTDATA: PARAMFLAG = ...
    """"""

class STATDATA(ValueType):
    """"""

    advSink: Final[IAdviseSink]
    """"""
    advf: Final[ADVF]
    """"""
    connection: Final[int]
    """"""
    formatetc: Final[FORMATETC]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class STATSTG(ValueType):
    """"""

    atime: Final[FILETIME]
    """"""
    cbSize: Final[int]
    """"""
    clsid: Final[Guid]
    """"""
    ctime: Final[FILETIME]
    """"""
    grfLocksSupported: Final[int]
    """"""
    grfMode: Final[int]
    """"""
    grfStateBits: Final[int]
    """"""
    mtime: Final[FILETIME]
    """"""
    pwcsName: Final[str]
    """"""
    reserved: Final[int]
    """"""
    type: Final[int]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class STGMEDIUM(ValueType):
    """"""

    pUnkForRelease: Final[object]
    """"""
    tymed: Final[TYMED]
    """"""
    unionmember: Final[IntPtr]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SYSKIND(Enum):
    """"""

    SYS_WIN16: SYSKIND = ...
    """"""
    SYS_WIN32: SYSKIND = ...
    """"""
    SYS_MAC: SYSKIND = ...
    """"""
    SYS_WIN64: SYSKIND = ...
    """"""

class TYMED(Enum):
    """"""

    TYMED_NULL: TYMED = ...
    """"""
    TYMED_HGLOBAL: TYMED = ...
    """"""
    TYMED_FILE: TYMED = ...
    """"""
    TYMED_ISTREAM: TYMED = ...
    """"""
    TYMED_ISTORAGE: TYMED = ...
    """"""
    TYMED_GDI: TYMED = ...
    """"""
    TYMED_MFPICT: TYMED = ...
    """"""
    TYMED_ENHMF: TYMED = ...
    """"""

class TYPEATTR(ValueType):
    """"""

    MEMBER_ID_NIL: ClassVar[int]
    """"""
    cFuncs: Final[int]
    """"""
    cImplTypes: Final[int]
    """"""
    cVars: Final[int]
    """"""
    cbAlignment: Final[int]
    """"""
    cbSizeInstance: Final[int]
    """"""
    cbSizeVft: Final[int]
    """"""
    dwReserved: Final[int]
    """"""
    guid: Final[Guid]
    """"""
    idldescType: Final[IDLDESC]
    """"""
    lcid: Final[int]
    """"""
    lpstrSchema: Final[IntPtr]
    """"""
    memidConstructor: Final[int]
    """"""
    memidDestructor: Final[int]
    """"""
    tdescAlias: Final[TYPEDESC]
    """"""
    typekind: Final[TYPEKIND]
    """"""
    wMajorVerNum: Final[int]
    """"""
    wMinorVerNum: Final[int]
    """"""
    wTypeFlags: Final[TYPEFLAGS]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class TYPEDESC(ValueType):
    """"""

    lpValue: Final[IntPtr]
    """"""
    vt: Final[int]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class TYPEFLAGS(Enum):
    """"""

    TYPEFLAG_FAPPOBJECT: TYPEFLAGS = ...
    """"""
    TYPEFLAG_FCANCREATE: TYPEFLAGS = ...
    """"""
    TYPEFLAG_FLICENSED: TYPEFLAGS = ...
    """"""
    TYPEFLAG_FPREDECLID: TYPEFLAGS = ...
    """"""
    TYPEFLAG_FHIDDEN: TYPEFLAGS = ...
    """"""
    TYPEFLAG_FCONTROL: TYPEFLAGS = ...
    """"""
    TYPEFLAG_FDUAL: TYPEFLAGS = ...
    """"""
    TYPEFLAG_FNONEXTENSIBLE: TYPEFLAGS = ...
    """"""
    TYPEFLAG_FOLEAUTOMATION: TYPEFLAGS = ...
    """"""
    TYPEFLAG_FRESTRICTED: TYPEFLAGS = ...
    """"""
    TYPEFLAG_FAGGREGATABLE: TYPEFLAGS = ...
    """"""
    TYPEFLAG_FREPLACEABLE: TYPEFLAGS = ...
    """"""
    TYPEFLAG_FDISPATCHABLE: TYPEFLAGS = ...
    """"""
    TYPEFLAG_FREVERSEBIND: TYPEFLAGS = ...
    """"""
    TYPEFLAG_FPROXY: TYPEFLAGS = ...
    """"""

class TYPEKIND(Enum):
    """"""

    TKIND_ENUM: TYPEKIND = ...
    """"""
    TKIND_RECORD: TYPEKIND = ...
    """"""
    TKIND_MODULE: TYPEKIND = ...
    """"""
    TKIND_INTERFACE: TYPEKIND = ...
    """"""
    TKIND_DISPATCH: TYPEKIND = ...
    """"""
    TKIND_COCLASS: TYPEKIND = ...
    """"""
    TKIND_ALIAS: TYPEKIND = ...
    """"""
    TKIND_UNION: TYPEKIND = ...
    """"""
    TKIND_MAX: TYPEKIND = ...
    """"""

class TYPELIBATTR(ValueType):
    """"""

    guid: Final[Guid]
    """"""
    lcid: Final[int]
    """"""
    syskind: Final[SYSKIND]
    """"""
    wLibFlags: Final[LIBFLAGS]
    """"""
    wMajorVerNum: Final[int]
    """"""
    wMinorVerNum: Final[int]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class VARDESC(ValueType):
    """"""

    desc: Final[VARDESC.DESCUNION]
    """"""
    elemdescVar: Final[ELEMDESC]
    """"""
    lpstrSchema: Final[str]
    """"""
    memid: Final[int]
    """"""
    varkind: Final[VARKIND]
    """"""
    wVarFlags: Final[int]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    class DESCUNION(ValueType):
        """"""

        lpvarValue: Final[IntPtr]
        """"""
        oInst: Final[int]
        """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def ToString(self) -> str:
            """"""

class VARFLAGS(Enum):
    """"""

    VARFLAG_FREADONLY: VARFLAGS = ...
    """"""
    VARFLAG_FSOURCE: VARFLAGS = ...
    """"""
    VARFLAG_FBINDABLE: VARFLAGS = ...
    """"""
    VARFLAG_FREQUESTEDIT: VARFLAGS = ...
    """"""
    VARFLAG_FDISPLAYBIND: VARFLAGS = ...
    """"""
    VARFLAG_FDEFAULTBIND: VARFLAGS = ...
    """"""
    VARFLAG_FHIDDEN: VARFLAGS = ...
    """"""
    VARFLAG_FRESTRICTED: VARFLAGS = ...
    """"""
    VARFLAG_FDEFAULTCOLLELEM: VARFLAGS = ...
    """"""
    VARFLAG_FUIDEFAULT: VARFLAGS = ...
    """"""
    VARFLAG_FNONBROWSABLE: VARFLAGS = ...
    """"""
    VARFLAG_FREPLACEABLE: VARFLAGS = ...
    """"""
    VARFLAG_FIMMEDIATEBIND: VARFLAGS = ...
    """"""

class VARKIND(Enum):
    """"""

    VAR_PERINSTANCE: VARKIND = ...
    """"""
    VAR_STATIC: VARKIND = ...
    """"""
    VAR_CONST: VARKIND = ...
    """"""
    VAR_DISPATCH: VARKIND = ...
    """"""
