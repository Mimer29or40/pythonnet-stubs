from __future__ import annotations

from typing import ClassVar
from typing import Final
from typing import Iterator
from typing import Tuple
from typing import overload

from System import Array
from System import Delegate
from System import Enum
from System import Guid
from System import IntPtr
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
from System.Runtime.InteropServices.ComTypes.ELEMDESC import DESCUNION
from System.Runtime.InteropServices.ComTypes.VARDESC import DESCUNION

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

    lpfuncdesc: Final[IntPtr] = ...
    """
    
    :return: 
    """
    lptcomp: Final[IntPtr] = ...
    """
    
    :return: 
    """
    lpvardesc: Final[IntPtr] = ...
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

class BIND_OPTS(ValueType):
    """"""

    cbStruct: Final[int] = ...
    """
    
    :return: 
    """
    dwTickCountDeadline: Final[int] = ...
    """
    
    :return: 
    """
    grfFlags: Final[int] = ...
    """
    
    :return: 
    """
    grfMode: Final[int] = ...
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

    dwCookie: Final[int] = ...
    """
    
    :return: 
    """
    pUnk: Final[object] = ...
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

    cArgs: Final[int] = ...
    """
    
    :return: 
    """
    cNamedArgs: Final[int] = ...
    """
    
    :return: 
    """
    rgdispidNamedArgs: Final[IntPtr] = ...
    """
    
    :return: 
    """
    rgvarg: Final[IntPtr] = ...
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

    desc: Final[ELEMDESC.DESCUNION] = ...
    """
    
    :return: 
    """
    tdesc: Final[TYPEDESC] = ...
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

    class DESCUNION(ValueType):
        """"""

        idldesc: Final[IDLDESC] = ...
        """"""
        paramdesc: Final[PARAMDESC] = ...
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
        def ToString(self) -> str:
            """

            :return:
            """

class EXCEPINFO(ValueType):
    """"""

    bstrDescription: Final[str] = ...
    """
    
    :return: 
    """
    bstrHelpFile: Final[str] = ...
    """
    
    :return: 
    """
    bstrSource: Final[str] = ...
    """
    
    :return: 
    """
    dwHelpContext: Final[int] = ...
    """
    
    :return: 
    """
    pfnDeferredFillIn: Final[IntPtr] = ...
    """
    
    :return: 
    """
    pvReserved: Final[IntPtr] = ...
    """
    
    :return: 
    """
    scode: Final[int] = ...
    """
    
    :return: 
    """
    wCode: Final[int] = ...
    """
    
    :return: 
    """
    wReserved: Final[int] = ...
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

class FILETIME(ValueType):
    """"""

    dwHighDateTime: Final[int] = ...
    """
    
    :return: 
    """
    dwLowDateTime: Final[int] = ...
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

class FORMATETC(ValueType):
    """"""

    cfFormat: Final[int] = ...
    """
    
    :return: 
    """
    dwAspect: Final[DVASPECT] = ...
    """
    
    :return: 
    """
    lindex: Final[int] = ...
    """
    
    :return: 
    """
    ptd: Final[IntPtr] = ...
    """
    
    :return: 
    """
    tymed: Final[TYMED] = ...
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

class FUNCDESC(ValueType):
    """"""

    cParams: Final[int] = ...
    """
    
    :return: 
    """
    cParamsOpt: Final[int] = ...
    """
    
    :return: 
    """
    cScodes: Final[int] = ...
    """
    
    :return: 
    """
    callconv: Final[CALLCONV] = ...
    """
    
    :return: 
    """
    elemdescFunc: Final[ELEMDESC] = ...
    """
    
    :return: 
    """
    funckind: Final[FUNCKIND] = ...
    """
    
    :return: 
    """
    invkind: Final[INVOKEKIND] = ...
    """
    
    :return: 
    """
    lprgelemdescParam: Final[IntPtr] = ...
    """
    
    :return: 
    """
    lprgscode: Final[IntPtr] = ...
    """
    
    :return: 
    """
    memid: Final[int] = ...
    """
    
    :return: 
    """
    oVft: Final[int] = ...
    """
    
    :return: 
    """
    wFuncFlags: Final[int] = ...
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
        """

        :param format:
        :param stgmedium:
        """
    def OnRename(self, moniker: IMoniker) -> None:
        """

        :param moniker:
        """
    def OnSave(self) -> None:
        """"""
    def OnViewChange(self, aspect: int, index: int) -> None:
        """

        :param aspect:
        :param index:
        """

class IBindCtx:
    """"""

    def EnumObjectParam(self, ppenum: IEnumString) -> Tuple[None, IEnumString]:
        """

        :param ppenum:
        """
    def GetBindOptions(self, pbindopts: BIND_OPTS) -> None:
        """

        :param pbindopts:
        """
    def GetObjectParam(self, pszKey: str, ppunk: object) -> Tuple[None, object]:
        """

        :param pszKey:
        :param ppunk:
        """
    def GetRunningObjectTable(self, pprot: IRunningObjectTable) -> Tuple[None, IRunningObjectTable]:
        """

        :param pprot:
        """
    def RegisterObjectBound(self, punk: object) -> None:
        """

        :param punk:
        """
    def RegisterObjectParam(self, pszKey: str, punk: object) -> None:
        """

        :param pszKey:
        :param punk:
        """
    def ReleaseBoundObjects(self) -> None:
        """"""
    def RevokeObjectBound(self, punk: object) -> None:
        """

        :param punk:
        """
    def RevokeObjectParam(self, pszKey: str) -> int:
        """

        :param pszKey:
        :return:
        """
    def SetBindOptions(self, pbindopts: BIND_OPTS) -> None:
        """

        :param pbindopts:
        """

class IConnectionPoint:
    """"""

    def Advise(self, pUnkSink: object, pdwCookie: int) -> Tuple[None, int]:
        """

        :param pUnkSink:
        :param pdwCookie:
        """
    def EnumConnections(self, ppEnum: IEnumConnections) -> Tuple[None, IEnumConnections]:
        """

        :param ppEnum:
        """
    def GetConnectionInterface(self, pIID: Guid) -> Tuple[None, Guid]:
        """

        :param pIID:
        """
    def GetConnectionPointContainer(
        self, ppCPC: IConnectionPointContainer
    ) -> Tuple[None, IConnectionPointContainer]:
        """

        :param ppCPC:
        """
    def Unadvise(self, dwCookie: int) -> None:
        """

        :param dwCookie:
        """

class IConnectionPointContainer:
    """"""

    def EnumConnectionPoints(
        self, ppEnum: IEnumConnectionPoints
    ) -> Tuple[None, IEnumConnectionPoints]:
        """

        :param ppEnum:
        """
    def FindConnectionPoint(
        self, riid: Guid, ppCP: IConnectionPoint
    ) -> Tuple[None, IConnectionPoint]:
        """

        :param riid:
        :param ppCP:
        """

class IDLDESC(ValueType):
    """"""

    dwReserved: Final[IntPtr] = ...
    """
    
    :return: 
    """
    wIDLFlags: Final[IDLFLAG] = ...
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
        self, pFormatetc: FORMATETC, advf: ADVF, adviseSink: IAdviseSink, connection: int
    ) -> Tuple[int, int]:
        """

        :param pFormatetc:
        :param advf:
        :param adviseSink:
        :param connection:
        :return:
        """
    def DUnadvise(self, connection: int) -> None:
        """

        :param connection:
        """
    def EnumDAdvise(self, enumAdvise: IEnumSTATDATA) -> Tuple[int, IEnumSTATDATA]:
        """

        :param enumAdvise:
        :return:
        """
    def EnumFormatEtc(self, direction: DATADIR) -> IEnumFORMATETC:
        """

        :param direction:
        :return:
        """
    def GetCanonicalFormatEtc(
        self, formatIn: FORMATETC, formatOut: FORMATETC
    ) -> Tuple[int, FORMATETC]:
        """

        :param formatIn:
        :param formatOut:
        :return:
        """
    def GetData(self, format: FORMATETC, medium: STGMEDIUM) -> Tuple[None, STGMEDIUM]:
        """

        :param format:
        :param medium:
        """
    def GetDataHere(self, format: FORMATETC, medium: STGMEDIUM) -> None:
        """

        :param format:
        :param medium:
        """
    def QueryGetData(self, format: FORMATETC) -> int:
        """

        :param format:
        :return:
        """
    def SetData(self, formatIn: FORMATETC, medium: STGMEDIUM, release: bool) -> None:
        """

        :param formatIn:
        :param medium:
        :param release:
        """

class IEnumConnectionPoints:
    """"""

    def Clone(self, ppenum: IEnumConnectionPoints) -> Tuple[None, IEnumConnectionPoints]:
        """

        :param ppenum:
        """
    def Next(
        self, celt: int, rgelt: Array[IConnectionPoint], pceltFetched: IntPtr
    ) -> Tuple[int, Array[IConnectionPoint]]:
        """

        :param celt:
        :param rgelt:
        :param pceltFetched:
        :return:
        """
    def Reset(self) -> None:
        """"""
    def Skip(self, celt: int) -> int:
        """

        :param celt:
        :return:
        """

class IEnumConnections:
    """"""

    def Clone(self, ppenum: IEnumConnections) -> Tuple[None, IEnumConnections]:
        """

        :param ppenum:
        """
    def Next(
        self, celt: int, rgelt: Array[CONNECTDATA], pceltFetched: IntPtr
    ) -> Tuple[int, Array[CONNECTDATA]]:
        """

        :param celt:
        :param rgelt:
        :param pceltFetched:
        :return:
        """
    def Reset(self) -> None:
        """"""
    def Skip(self, celt: int) -> int:
        """

        :param celt:
        :return:
        """

class IEnumFORMATETC:
    """"""

    def Clone(self, newEnum: IEnumFORMATETC) -> Tuple[None, IEnumFORMATETC]:
        """

        :param newEnum:
        """
    def Next(
        self, celt: int, rgelt: Array[FORMATETC], pceltFetched: Array[int]
    ) -> Tuple[int, Array[FORMATETC], Array[int]]:
        """

        :param celt:
        :param rgelt:
        :param pceltFetched:
        :return:
        """
    def Reset(self) -> int:
        """

        :return:
        """
    def Skip(self, celt: int) -> int:
        """

        :param celt:
        :return:
        """

class IEnumMoniker:
    """"""

    def Clone(self, ppenum: IEnumMoniker) -> Tuple[None, IEnumMoniker]:
        """

        :param ppenum:
        """
    def Next(
        self, celt: int, rgelt: Array[IMoniker], pceltFetched: IntPtr
    ) -> Tuple[int, Array[IMoniker]]:
        """

        :param celt:
        :param rgelt:
        :param pceltFetched:
        :return:
        """
    def Reset(self) -> None:
        """"""
    def Skip(self, celt: int) -> int:
        """

        :param celt:
        :return:
        """

class IEnumSTATDATA:
    """"""

    def Clone(self, newEnum: IEnumSTATDATA) -> Tuple[None, IEnumSTATDATA]:
        """

        :param newEnum:
        """
    def Next(
        self, celt: int, rgelt: Array[STATDATA], pceltFetched: Array[int]
    ) -> Tuple[int, Array[STATDATA], Array[int]]:
        """

        :param celt:
        :param rgelt:
        :param pceltFetched:
        :return:
        """
    def Reset(self) -> int:
        """

        :return:
        """
    def Skip(self, celt: int) -> int:
        """

        :param celt:
        :return:
        """

class IEnumString:
    """"""

    def Clone(self, ppenum: IEnumString) -> Tuple[None, IEnumString]:
        """

        :param ppenum:
        """
    def Next(self, celt: int, rgelt: Array[str], pceltFetched: IntPtr) -> Tuple[int, Array[str]]:
        """

        :param celt:
        :param rgelt:
        :param pceltFetched:
        :return:
        """
    def Reset(self) -> None:
        """"""
    def Skip(self, celt: int) -> int:
        """

        :param celt:
        :return:
        """

class IEnumVARIANT:
    """"""

    def Clone(self) -> IEnumVARIANT:
        """

        :return:
        """
    def Next(
        self, celt: int, rgVar: Array[object], pceltFetched: IntPtr
    ) -> Tuple[int, Array[object]]:
        """

        :param celt:
        :param rgVar:
        :param pceltFetched:
        :return:
        """
    def Reset(self) -> int:
        """

        :return:
        """
    def Skip(self, celt: int) -> int:
        """

        :param celt:
        :return:
        """

class IEnumerable:
    """"""

    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """

class IEnumerator:
    """"""

    @property
    def Current(self) -> object:
        """

        :return:
        """
    def MoveNext(self) -> bool:
        """

        :return:
        """
    def Reset(self) -> None:
        """"""

class IExpando(IReflect):
    """"""

    @property
    def UnderlyingSystemType(self) -> Type:
        """

        :return:
        """
    def AddField(self, name: str) -> FieldInfo:
        """

        :param name:
        :return:
        """
    def AddMethod(self, name: str, method: Delegate) -> MethodInfo:
        """

        :param name:
        :param method:
        :return:
        """
    def AddProperty(self, name: str) -> PropertyInfo:
        """

        :param name:
        :return:
        """
    def GetField(self, name: str, bindingAttr: BindingFlags) -> FieldInfo:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    def GetFields(self, bindingAttr: BindingFlags) -> Array[FieldInfo]:
        """

        :param bindingAttr:
        :return:
        """
    def GetMember(self, name: str, bindingAttr: BindingFlags) -> Array[MemberInfo]:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    def GetMembers(self, bindingAttr: BindingFlags) -> Array[MemberInfo]:
        """

        :param bindingAttr:
        :return:
        """
    @overload
    def GetMethod(self, name: str, bindingAttr: BindingFlags) -> MethodInfo:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetMethod(
        self,
        name: str,
        bindingAttr: BindingFlags,
        binder: Binder,
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> MethodInfo:
        """

        :param name:
        :param bindingAttr:
        :param binder:
        :param types:
        :param modifiers:
        :return:
        """
    def GetMethods(self, bindingAttr: BindingFlags) -> Array[MethodInfo]:
        """

        :param bindingAttr:
        :return:
        """
    def GetProperties(self, bindingAttr: BindingFlags) -> Array[PropertyInfo]:
        """

        :param bindingAttr:
        :return:
        """
    @overload
    def GetProperty(self, name: str, bindingAttr: BindingFlags) -> PropertyInfo:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
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
        """

        :param name:
        :param bindingAttr:
        :param binder:
        :param returnType:
        :param types:
        :param modifiers:
        :return:
        """
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
        """

        :param name:
        :param invokeAttr:
        :param binder:
        :param target:
        :param args:
        :param modifiers:
        :param culture:
        :param namedParameters:
        :return:
        """
    def RemoveMember(self, m: MemberInfo) -> None:
        """

        :param m:
        """

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
        self, pbc: IBindCtx, pmkToLeft: IMoniker, riidResult: Guid, ppvResult: object
    ) -> Tuple[None, object]:
        """

        :param pbc:
        :param pmkToLeft:
        :param riidResult:
        :param ppvResult:
        """
    def BindToStorage(
        self, pbc: IBindCtx, pmkToLeft: IMoniker, riid: Guid, ppvObj: object
    ) -> Tuple[None, object]:
        """

        :param pbc:
        :param pmkToLeft:
        :param riid:
        :param ppvObj:
        """
    def CommonPrefixWith(self, pmkOther: IMoniker, ppmkPrefix: IMoniker) -> Tuple[None, IMoniker]:
        """

        :param pmkOther:
        :param ppmkPrefix:
        """
    def ComposeWith(
        self, pmkRight: IMoniker, fOnlyIfNotGeneric: bool, ppmkComposite: IMoniker
    ) -> Tuple[None, IMoniker]:
        """

        :param pmkRight:
        :param fOnlyIfNotGeneric:
        :param ppmkComposite:
        """
    def Enum(self, fForward: bool, ppenumMoniker: IEnumMoniker) -> Tuple[None, IEnumMoniker]:
        """

        :param fForward:
        :param ppenumMoniker:
        """
    def GetClassID(self, pClassID: Guid) -> Tuple[None, Guid]:
        """

        :param pClassID:
        """
    def GetDisplayName(
        self, pbc: IBindCtx, pmkToLeft: IMoniker, ppszDisplayName: str
    ) -> Tuple[None, str]:
        """

        :param pbc:
        :param pmkToLeft:
        :param ppszDisplayName:
        """
    def GetSizeMax(self, pcbSize: int) -> Tuple[None, int]:
        """

        :param pcbSize:
        """
    def GetTimeOfLastChange(
        self, pbc: IBindCtx, pmkToLeft: IMoniker, pFileTime: FILETIME
    ) -> Tuple[None, FILETIME]:
        """

        :param pbc:
        :param pmkToLeft:
        :param pFileTime:
        """
    def Hash(self, pdwHash: int) -> Tuple[None, int]:
        """

        :param pdwHash:
        """
    def Inverse(self, ppmk: IMoniker) -> Tuple[None, IMoniker]:
        """

        :param ppmk:
        """
    def IsDirty(self) -> int:
        """

        :return:
        """
    def IsEqual(self, pmkOtherMoniker: IMoniker) -> int:
        """

        :param pmkOtherMoniker:
        :return:
        """
    def IsRunning(self, pbc: IBindCtx, pmkToLeft: IMoniker, pmkNewlyRunning: IMoniker) -> int:
        """

        :param pbc:
        :param pmkToLeft:
        :param pmkNewlyRunning:
        :return:
        """
    def IsSystemMoniker(self, pdwMksys: int) -> Tuple[int, int]:
        """

        :param pdwMksys:
        :return:
        """
    def Load(self, pStm: IStream) -> None:
        """

        :param pStm:
        """
    def ParseDisplayName(
        self,
        pbc: IBindCtx,
        pmkToLeft: IMoniker,
        pszDisplayName: str,
        pchEaten: int,
        ppmkOut: IMoniker,
    ) -> Tuple[None, int, IMoniker]:
        """

        :param pbc:
        :param pmkToLeft:
        :param pszDisplayName:
        :param pchEaten:
        :param ppmkOut:
        """
    def Reduce(
        self, pbc: IBindCtx, dwReduceHowFar: int, ppmkToLeft: IMoniker, ppmkReduced: IMoniker
    ) -> Tuple[None, IMoniker]:
        """

        :param pbc:
        :param dwReduceHowFar:
        :param ppmkToLeft:
        :param ppmkReduced:
        """
    def RelativePathTo(self, pmkOther: IMoniker, ppmkRelPath: IMoniker) -> Tuple[None, IMoniker]:
        """

        :param pmkOther:
        :param ppmkRelPath:
        """
    def Save(self, pStm: IStream, fClearDirty: bool) -> None:
        """

        :param pStm:
        :param fClearDirty:
        """

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

    def GetClassID(self, pClassID: Guid) -> Tuple[None, Guid]:
        """

        :param pClassID:
        """
    def GetCurFile(self, ppszFileName: str) -> Tuple[None, str]:
        """

        :param ppszFileName:
        """
    def IsDirty(self) -> int:
        """

        :return:
        """
    def Load(self, pszFileName: str, dwMode: int) -> None:
        """

        :param pszFileName:
        :param dwMode:
        """
    def Save(self, pszFileName: str, fRemember: bool) -> None:
        """

        :param pszFileName:
        :param fRemember:
        """
    def SaveCompleted(self, pszFileName: str) -> None:
        """

        :param pszFileName:
        """

class IReflect:
    """"""

    @property
    def UnderlyingSystemType(self) -> Type:
        """

        :return:
        """
    def GetField(self, name: str, bindingAttr: BindingFlags) -> FieldInfo:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    def GetFields(self, bindingAttr: BindingFlags) -> Array[FieldInfo]:
        """

        :param bindingAttr:
        :return:
        """
    def GetMember(self, name: str, bindingAttr: BindingFlags) -> Array[MemberInfo]:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    def GetMembers(self, bindingAttr: BindingFlags) -> Array[MemberInfo]:
        """

        :param bindingAttr:
        :return:
        """
    @overload
    def GetMethod(self, name: str, bindingAttr: BindingFlags) -> MethodInfo:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetMethod(
        self,
        name: str,
        bindingAttr: BindingFlags,
        binder: Binder,
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> MethodInfo:
        """

        :param name:
        :param bindingAttr:
        :param binder:
        :param types:
        :param modifiers:
        :return:
        """
    def GetMethods(self, bindingAttr: BindingFlags) -> Array[MethodInfo]:
        """

        :param bindingAttr:
        :return:
        """
    def GetProperties(self, bindingAttr: BindingFlags) -> Array[PropertyInfo]:
        """

        :param bindingAttr:
        :return:
        """
    @overload
    def GetProperty(self, name: str, bindingAttr: BindingFlags) -> PropertyInfo:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
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
        """

        :param name:
        :param bindingAttr:
        :param binder:
        :param returnType:
        :param types:
        :param modifiers:
        :return:
        """
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
        """

        :param name:
        :param invokeAttr:
        :param binder:
        :param target:
        :param args:
        :param modifiers:
        :param culture:
        :param namedParameters:
        :return:
        """

class IRunningObjectTable:
    """"""

    def EnumRunning(self, ppenumMoniker: IEnumMoniker) -> Tuple[None, IEnumMoniker]:
        """

        :param ppenumMoniker:
        """
    def GetObject(self, pmkObjectName: IMoniker, ppunkObject: object) -> Tuple[int, object]:
        """

        :param pmkObjectName:
        :param ppunkObject:
        :return:
        """
    def GetTimeOfLastChange(
        self, pmkObjectName: IMoniker, pfiletime: FILETIME
    ) -> Tuple[int, FILETIME]:
        """

        :param pmkObjectName:
        :param pfiletime:
        :return:
        """
    def IsRunning(self, pmkObjectName: IMoniker) -> int:
        """

        :param pmkObjectName:
        :return:
        """
    def NoteChangeTime(self, dwRegister: int, pfiletime: FILETIME) -> None:
        """

        :param dwRegister:
        :param pfiletime:
        """
    def Register(self, grfFlags: int, punkObject: object, pmkObjectName: IMoniker) -> int:
        """

        :param grfFlags:
        :param punkObject:
        :param pmkObjectName:
        :return:
        """
    def Revoke(self, dwRegister: int) -> None:
        """

        :param dwRegister:
        """

class IStream:
    """"""

    def Clone(self, ppstm: IStream) -> Tuple[None, IStream]:
        """

        :param ppstm:
        """
    def Commit(self, grfCommitFlags: int) -> None:
        """

        :param grfCommitFlags:
        """
    def CopyTo(self, pstm: IStream, cb: int, pcbRead: IntPtr, pcbWritten: IntPtr) -> None:
        """

        :param pstm:
        :param cb:
        :param pcbRead:
        :param pcbWritten:
        """
    def LockRegion(self, libOffset: int, cb: int, dwLockType: int) -> None:
        """

        :param libOffset:
        :param cb:
        :param dwLockType:
        """
    def Read(self, pv: Array[int], cb: int, pcbRead: IntPtr) -> Tuple[None, Array[int]]:
        """

        :param pv:
        :param cb:
        :param pcbRead:
        """
    def Revert(self) -> None:
        """"""
    def Seek(self, dlibMove: int, dwOrigin: int, plibNewPosition: IntPtr) -> None:
        """

        :param dlibMove:
        :param dwOrigin:
        :param plibNewPosition:
        """
    def SetSize(self, libNewSize: int) -> None:
        """

        :param libNewSize:
        """
    def Stat(self, pstatstg: STATSTG, grfStatFlag: int) -> Tuple[None, STATSTG]:
        """

        :param pstatstg:
        :param grfStatFlag:
        """
    def UnlockRegion(self, libOffset: int, cb: int, dwLockType: int) -> None:
        """

        :param libOffset:
        :param cb:
        :param dwLockType:
        """
    def Write(self, pv: Array[int], cb: int, pcbWritten: IntPtr) -> None:
        """

        :param pv:
        :param cb:
        :param pcbWritten:
        """

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
    ) -> Tuple[None, ITypeInfo, DESCKIND, BINDPTR]:
        """

        :param szName:
        :param lHashVal:
        :param wFlags:
        :param ppTInfo:
        :param pDescKind:
        :param pBindPtr:
        """
    def BindType(
        self, szName: str, lHashVal: int, ppTInfo: ITypeInfo, ppTComp: ITypeComp
    ) -> Tuple[None, ITypeInfo, ITypeComp]:
        """

        :param szName:
        :param lHashVal:
        :param ppTInfo:
        :param ppTComp:
        """

class ITypeInfo:
    """"""

    def AddressOfMember(self, memid: int, invKind: INVOKEKIND, ppv: IntPtr) -> Tuple[None, IntPtr]:
        """

        :param memid:
        :param invKind:
        :param ppv:
        """
    def CreateInstance(self, pUnkOuter: object, riid: Guid, ppvObj: object) -> Tuple[None, object]:
        """

        :param pUnkOuter:
        :param riid:
        :param ppvObj:
        """
    def GetContainingTypeLib(self, ppTLB: ITypeLib, pIndex: int) -> Tuple[None, ITypeLib, int]:
        """

        :param ppTLB:
        :param pIndex:
        """
    def GetDllEntry(
        self,
        memid: int,
        invKind: INVOKEKIND,
        pBstrDllName: IntPtr,
        pBstrName: IntPtr,
        pwOrdinal: IntPtr,
    ) -> None:
        """

        :param memid:
        :param invKind:
        :param pBstrDllName:
        :param pBstrName:
        :param pwOrdinal:
        """
    def GetDocumentation(
        self, index: int, strName: str, strDocString: str, dwHelpContext: int, strHelpFile: str
    ) -> Tuple[None, str, str, int, str]:
        """

        :param index:
        :param strName:
        :param strDocString:
        :param dwHelpContext:
        :param strHelpFile:
        """
    def GetFuncDesc(self, index: int, ppFuncDesc: IntPtr) -> Tuple[None, IntPtr]:
        """

        :param index:
        :param ppFuncDesc:
        """
    def GetIDsOfNames(
        self, rgszNames: Array[str], cNames: int, pMemId: Array[int]
    ) -> Tuple[None, Array[int]]:
        """

        :param rgszNames:
        :param cNames:
        :param pMemId:
        """
    def GetImplTypeFlags(
        self, index: int, pImplTypeFlags: IMPLTYPEFLAGS
    ) -> Tuple[None, IMPLTYPEFLAGS]:
        """

        :param index:
        :param pImplTypeFlags:
        """
    def GetMops(self, memid: int, pBstrMops: str) -> Tuple[None, str]:
        """

        :param memid:
        :param pBstrMops:
        """
    def GetNames(
        self, memid: int, rgBstrNames: Array[str], cMaxNames: int, pcNames: int
    ) -> Tuple[None, Array[str], int]:
        """

        :param memid:
        :param rgBstrNames:
        :param cMaxNames:
        :param pcNames:
        """
    def GetRefTypeInfo(self, hRef: int, ppTI: ITypeInfo) -> Tuple[None, ITypeInfo]:
        """

        :param hRef:
        :param ppTI:
        """
    def GetRefTypeOfImplType(self, index: int, href: int) -> Tuple[None, int]:
        """

        :param index:
        :param href:
        """
    def GetTypeAttr(self, ppTypeAttr: IntPtr) -> Tuple[None, IntPtr]:
        """

        :param ppTypeAttr:
        """
    def GetTypeComp(self, ppTComp: ITypeComp) -> Tuple[None, ITypeComp]:
        """

        :param ppTComp:
        """
    def GetVarDesc(self, index: int, ppVarDesc: IntPtr) -> Tuple[None, IntPtr]:
        """

        :param index:
        :param ppVarDesc:
        """
    def Invoke(
        self,
        pvInstance: object,
        memid: int,
        wFlags: int,
        pDispParams: DISPPARAMS,
        pVarResult: IntPtr,
        pExcepInfo: IntPtr,
        puArgErr: int,
    ) -> Tuple[None, int]:
        """

        :param pvInstance:
        :param memid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def ReleaseFuncDesc(self, pFuncDesc: IntPtr) -> None:
        """

        :param pFuncDesc:
        """
    def ReleaseTypeAttr(self, pTypeAttr: IntPtr) -> None:
        """

        :param pTypeAttr:
        """
    def ReleaseVarDesc(self, pVarDesc: IntPtr) -> None:
        """

        :param pVarDesc:
        """

class ITypeInfo2(ITypeInfo):
    """"""

    def AddressOfMember(self, memid: int, invKind: INVOKEKIND, ppv: IntPtr) -> Tuple[None, IntPtr]:
        """

        :param memid:
        :param invKind:
        :param ppv:
        """
    def CreateInstance(self, pUnkOuter: object, riid: Guid, ppvObj: object) -> Tuple[None, object]:
        """

        :param pUnkOuter:
        :param riid:
        :param ppvObj:
        """
    def GetAllCustData(self, pCustData: IntPtr) -> None:
        """

        :param pCustData:
        """
    def GetAllFuncCustData(self, index: int, pCustData: IntPtr) -> None:
        """

        :param index:
        :param pCustData:
        """
    def GetAllImplTypeCustData(self, index: int, pCustData: IntPtr) -> None:
        """

        :param index:
        :param pCustData:
        """
    def GetAllParamCustData(self, indexFunc: int, indexParam: int, pCustData: IntPtr) -> None:
        """

        :param indexFunc:
        :param indexParam:
        :param pCustData:
        """
    def GetAllVarCustData(self, index: int, pCustData: IntPtr) -> None:
        """

        :param index:
        :param pCustData:
        """
    def GetContainingTypeLib(self, ppTLB: ITypeLib, pIndex: int) -> Tuple[None, ITypeLib, int]:
        """

        :param ppTLB:
        :param pIndex:
        """
    def GetCustData(self, guid: Guid, pVarVal: object) -> Tuple[None, object]:
        """

        :param guid:
        :param pVarVal:
        """
    def GetDllEntry(
        self,
        memid: int,
        invKind: INVOKEKIND,
        pBstrDllName: IntPtr,
        pBstrName: IntPtr,
        pwOrdinal: IntPtr,
    ) -> None:
        """

        :param memid:
        :param invKind:
        :param pBstrDllName:
        :param pBstrName:
        :param pwOrdinal:
        """
    def GetDocumentation(
        self, index: int, strName: str, strDocString: str, dwHelpContext: int, strHelpFile: str
    ) -> Tuple[None, str, str, int, str]:
        """

        :param index:
        :param strName:
        :param strDocString:
        :param dwHelpContext:
        :param strHelpFile:
        """
    def GetDocumentation2(
        self, memid: int, pbstrHelpString: str, pdwHelpStringContext: int, pbstrHelpStringDll: str
    ) -> Tuple[None, str, int, str]:
        """

        :param memid:
        :param pbstrHelpString:
        :param pdwHelpStringContext:
        :param pbstrHelpStringDll:
        """
    def GetFuncCustData(self, index: int, guid: Guid, pVarVal: object) -> Tuple[None, object]:
        """

        :param index:
        :param guid:
        :param pVarVal:
        """
    def GetFuncDesc(self, index: int, ppFuncDesc: IntPtr) -> Tuple[None, IntPtr]:
        """

        :param index:
        :param ppFuncDesc:
        """
    def GetFuncIndexOfMemId(
        self, memid: int, invKind: INVOKEKIND, pFuncIndex: int
    ) -> Tuple[None, int]:
        """

        :param memid:
        :param invKind:
        :param pFuncIndex:
        """
    def GetIDsOfNames(
        self, rgszNames: Array[str], cNames: int, pMemId: Array[int]
    ) -> Tuple[None, Array[int]]:
        """

        :param rgszNames:
        :param cNames:
        :param pMemId:
        """
    def GetImplTypeCustData(self, index: int, guid: Guid, pVarVal: object) -> Tuple[None, object]:
        """

        :param index:
        :param guid:
        :param pVarVal:
        """
    def GetImplTypeFlags(
        self, index: int, pImplTypeFlags: IMPLTYPEFLAGS
    ) -> Tuple[None, IMPLTYPEFLAGS]:
        """

        :param index:
        :param pImplTypeFlags:
        """
    def GetMops(self, memid: int, pBstrMops: str) -> Tuple[None, str]:
        """

        :param memid:
        :param pBstrMops:
        """
    def GetNames(
        self, memid: int, rgBstrNames: Array[str], cMaxNames: int, pcNames: int
    ) -> Tuple[None, Array[str], int]:
        """

        :param memid:
        :param rgBstrNames:
        :param cMaxNames:
        :param pcNames:
        """
    def GetParamCustData(
        self, indexFunc: int, indexParam: int, guid: Guid, pVarVal: object
    ) -> Tuple[None, object]:
        """

        :param indexFunc:
        :param indexParam:
        :param guid:
        :param pVarVal:
        """
    def GetRefTypeInfo(self, hRef: int, ppTI: ITypeInfo) -> Tuple[None, ITypeInfo]:
        """

        :param hRef:
        :param ppTI:
        """
    def GetRefTypeOfImplType(self, index: int, href: int) -> Tuple[None, int]:
        """

        :param index:
        :param href:
        """
    def GetTypeAttr(self, ppTypeAttr: IntPtr) -> Tuple[None, IntPtr]:
        """

        :param ppTypeAttr:
        """
    def GetTypeComp(self, ppTComp: ITypeComp) -> Tuple[None, ITypeComp]:
        """

        :param ppTComp:
        """
    def GetTypeFlags(self, pTypeFlags: int) -> Tuple[None, int]:
        """

        :param pTypeFlags:
        """
    def GetTypeKind(self, pTypeKind: TYPEKIND) -> Tuple[None, TYPEKIND]:
        """

        :param pTypeKind:
        """
    def GetVarCustData(self, index: int, guid: Guid, pVarVal: object) -> Tuple[None, object]:
        """

        :param index:
        :param guid:
        :param pVarVal:
        """
    def GetVarDesc(self, index: int, ppVarDesc: IntPtr) -> Tuple[None, IntPtr]:
        """

        :param index:
        :param ppVarDesc:
        """
    def GetVarIndexOfMemId(self, memid: int, pVarIndex: int) -> Tuple[None, int]:
        """

        :param memid:
        :param pVarIndex:
        """
    def Invoke(
        self,
        pvInstance: object,
        memid: int,
        wFlags: int,
        pDispParams: DISPPARAMS,
        pVarResult: IntPtr,
        pExcepInfo: IntPtr,
        puArgErr: int,
    ) -> Tuple[None, int]:
        """

        :param pvInstance:
        :param memid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def ReleaseFuncDesc(self, pFuncDesc: IntPtr) -> None:
        """

        :param pFuncDesc:
        """
    def ReleaseTypeAttr(self, pTypeAttr: IntPtr) -> None:
        """

        :param pTypeAttr:
        """
    def ReleaseVarDesc(self, pVarDesc: IntPtr) -> None:
        """

        :param pVarDesc:
        """

class ITypeLib:
    """"""

    def FindName(
        self,
        szNameBuf: str,
        lHashVal: int,
        ppTInfo: Array[ITypeInfo],
        rgMemId: Array[int],
        pcFound: int,
    ) -> Tuple[None, Array[ITypeInfo], Array[int]]:
        """

        :param szNameBuf:
        :param lHashVal:
        :param ppTInfo:
        :param rgMemId:
        :param pcFound:
        """
    def GetDocumentation(
        self, index: int, strName: str, strDocString: str, dwHelpContext: int, strHelpFile: str
    ) -> Tuple[None, str, str, int, str]:
        """

        :param index:
        :param strName:
        :param strDocString:
        :param dwHelpContext:
        :param strHelpFile:
        """
    def GetLibAttr(self, ppTLibAttr: IntPtr) -> Tuple[None, IntPtr]:
        """

        :param ppTLibAttr:
        """
    def GetTypeComp(self, ppTComp: ITypeComp) -> Tuple[None, ITypeComp]:
        """

        :param ppTComp:
        """
    def GetTypeInfo(self, index: int, ppTI: ITypeInfo) -> Tuple[None, ITypeInfo]:
        """

        :param index:
        :param ppTI:
        """
    def GetTypeInfoCount(self) -> int:
        """

        :return:
        """
    def GetTypeInfoOfGuid(self, guid: Guid, ppTInfo: ITypeInfo) -> Tuple[None, ITypeInfo]:
        """

        :param guid:
        :param ppTInfo:
        """
    def GetTypeInfoType(self, index: int, pTKind: TYPEKIND) -> Tuple[None, TYPEKIND]:
        """

        :param index:
        :param pTKind:
        """
    def IsName(self, szNameBuf: str, lHashVal: int) -> bool:
        """

        :param szNameBuf:
        :param lHashVal:
        :return:
        """
    def ReleaseTLibAttr(self, pTLibAttr: IntPtr) -> None:
        """

        :param pTLibAttr:
        """

class ITypeLib2(ITypeLib):
    """"""

    def FindName(
        self,
        szNameBuf: str,
        lHashVal: int,
        ppTInfo: Array[ITypeInfo],
        rgMemId: Array[int],
        pcFound: int,
    ) -> Tuple[None, Array[ITypeInfo], Array[int]]:
        """

        :param szNameBuf:
        :param lHashVal:
        :param ppTInfo:
        :param rgMemId:
        :param pcFound:
        """
    def GetAllCustData(self, pCustData: IntPtr) -> None:
        """

        :param pCustData:
        """
    def GetCustData(self, guid: Guid, pVarVal: object) -> Tuple[None, object]:
        """

        :param guid:
        :param pVarVal:
        """
    def GetDocumentation(
        self, index: int, strName: str, strDocString: str, dwHelpContext: int, strHelpFile: str
    ) -> Tuple[None, str, str, int, str]:
        """

        :param index:
        :param strName:
        :param strDocString:
        :param dwHelpContext:
        :param strHelpFile:
        """
    def GetDocumentation2(
        self, index: int, pbstrHelpString: str, pdwHelpStringContext: int, pbstrHelpStringDll: str
    ) -> Tuple[None, str, int, str]:
        """

        :param index:
        :param pbstrHelpString:
        :param pdwHelpStringContext:
        :param pbstrHelpStringDll:
        """
    def GetLibAttr(self, ppTLibAttr: IntPtr) -> Tuple[None, IntPtr]:
        """

        :param ppTLibAttr:
        """
    def GetLibStatistics(self, pcUniqueNames: IntPtr, pcchUniqueNames: int) -> Tuple[None, int]:
        """

        :param pcUniqueNames:
        :param pcchUniqueNames:
        """
    def GetTypeComp(self, ppTComp: ITypeComp) -> Tuple[None, ITypeComp]:
        """

        :param ppTComp:
        """
    def GetTypeInfo(self, index: int, ppTI: ITypeInfo) -> Tuple[None, ITypeInfo]:
        """

        :param index:
        :param ppTI:
        """
    def GetTypeInfoCount(self) -> int:
        """

        :return:
        """
    def GetTypeInfoOfGuid(self, guid: Guid, ppTInfo: ITypeInfo) -> Tuple[None, ITypeInfo]:
        """

        :param guid:
        :param ppTInfo:
        """
    def GetTypeInfoType(self, index: int, pTKind: TYPEKIND) -> Tuple[None, TYPEKIND]:
        """

        :param index:
        :param pTKind:
        """
    def IsName(self, szNameBuf: str, lHashVal: int) -> bool:
        """

        :param szNameBuf:
        :param lHashVal:
        :return:
        """
    def ReleaseTLibAttr(self, pTLibAttr: IntPtr) -> None:
        """

        :param pTLibAttr:
        """

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

    lpVarValue: Final[IntPtr] = ...
    """
    
    :return: 
    """
    wParamFlags: Final[PARAMFLAG] = ...
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

    advSink: Final[IAdviseSink] = ...
    """
    
    :return: 
    """
    advf: Final[ADVF] = ...
    """
    
    :return: 
    """
    connection: Final[int] = ...
    """
    
    :return: 
    """
    formatetc: Final[FORMATETC] = ...
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

class STATSTG(ValueType):
    """"""

    atime: Final[FILETIME] = ...
    """
    
    :return: 
    """
    cbSize: Final[int] = ...
    """
    
    :return: 
    """
    clsid: Final[Guid] = ...
    """
    
    :return: 
    """
    ctime: Final[FILETIME] = ...
    """
    
    :return: 
    """
    grfLocksSupported: Final[int] = ...
    """
    
    :return: 
    """
    grfMode: Final[int] = ...
    """
    
    :return: 
    """
    grfStateBits: Final[int] = ...
    """
    
    :return: 
    """
    mtime: Final[FILETIME] = ...
    """
    
    :return: 
    """
    pwcsName: Final[str] = ...
    """
    
    :return: 
    """
    reserved: Final[int] = ...
    """
    
    :return: 
    """
    type: Final[int] = ...
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

class STGMEDIUM(ValueType):
    """"""

    pUnkForRelease: Final[object] = ...
    """
    
    :return: 
    """
    tymed: Final[TYMED] = ...
    """
    
    :return: 
    """
    unionmember: Final[IntPtr] = ...
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

    MEMBER_ID_NIL: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    cFuncs: Final[int] = ...
    """
    
    :return: 
    """
    cImplTypes: Final[int] = ...
    """
    
    :return: 
    """
    cVars: Final[int] = ...
    """
    
    :return: 
    """
    cbAlignment: Final[int] = ...
    """
    
    :return: 
    """
    cbSizeInstance: Final[int] = ...
    """
    
    :return: 
    """
    cbSizeVft: Final[int] = ...
    """
    
    :return: 
    """
    dwReserved: Final[int] = ...
    """
    
    :return: 
    """
    guid: Final[Guid] = ...
    """
    
    :return: 
    """
    idldescType: Final[IDLDESC] = ...
    """
    
    :return: 
    """
    lcid: Final[int] = ...
    """
    
    :return: 
    """
    lpstrSchema: Final[IntPtr] = ...
    """
    
    :return: 
    """
    memidConstructor: Final[int] = ...
    """
    
    :return: 
    """
    memidDestructor: Final[int] = ...
    """
    
    :return: 
    """
    tdescAlias: Final[TYPEDESC] = ...
    """
    
    :return: 
    """
    typekind: Final[TYPEKIND] = ...
    """
    
    :return: 
    """
    wMajorVerNum: Final[int] = ...
    """
    
    :return: 
    """
    wMinorVerNum: Final[int] = ...
    """
    
    :return: 
    """
    wTypeFlags: Final[TYPEFLAGS] = ...
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

class TYPEDESC(ValueType):
    """"""

    lpValue: Final[IntPtr] = ...
    """
    
    :return: 
    """
    vt: Final[int] = ...
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

    guid: Final[Guid] = ...
    """
    
    :return: 
    """
    lcid: Final[int] = ...
    """
    
    :return: 
    """
    syskind: Final[SYSKIND] = ...
    """
    
    :return: 
    """
    wLibFlags: Final[LIBFLAGS] = ...
    """
    
    :return: 
    """
    wMajorVerNum: Final[int] = ...
    """
    
    :return: 
    """
    wMinorVerNum: Final[int] = ...
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

class VARDESC(ValueType):
    """"""

    desc: Final[VARDESC.DESCUNION] = ...
    """
    
    :return: 
    """
    elemdescVar: Final[ELEMDESC] = ...
    """
    
    :return: 
    """
    lpstrSchema: Final[str] = ...
    """
    
    :return: 
    """
    memid: Final[int] = ...
    """
    
    :return: 
    """
    varkind: Final[VARKIND] = ...
    """
    
    :return: 
    """
    wVarFlags: Final[int] = ...
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

    class DESCUNION(ValueType):
        """"""

        lpvarValue: Final[IntPtr] = ...
        """"""
        oInst: Final[int] = ...
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
        def ToString(self) -> str:
            """

            :return:
            """

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
