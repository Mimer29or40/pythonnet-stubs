from __future__ import annotations

from typing import List, Protocol, Tuple, Union, overload

from System import Array, Boolean, Byte, Delegate, Enum, Guid, Int16, Int32, Int64, IntPtr, Object, String, Type, ValueType, Void
from System.Globalization import CultureInfo
from System.Reflection import Binder, BindingFlags, FieldInfo, MemberInfo, MethodInfo, ParameterModifier, PropertyInfo

# ---------- Types ---------- #

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
ByteType = Union[int, Byte]
IntType = Union[int, Int32]
LongType = Union[int, Int64]
NIntType = Union[int, IntPtr]
ObjectType = Object
ShortType = Union[int, Int16]
StringType = Union[str, String]
TypeType = Union[type, Type]
VoidType = Union[None, Void]

# No Classes

# ---------- Structs ---------- #

class BINDPTR(ValueType):
    # ---------- Fields ---------- #
    
    @property
    def lpfuncdesc(self) -> NIntType: ...
    
    @lpfuncdesc.setter
    def lpfuncdesc(self, value: NIntType) -> None: ...
    
    @property
    def lptcomp(self) -> NIntType: ...
    
    @lptcomp.setter
    def lptcomp(self, value: NIntType) -> None: ...
    
    @property
    def lpvardesc(self) -> NIntType: ...
    
    @lpvardesc.setter
    def lpvardesc(self, value: NIntType) -> None: ...
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class BIND_OPTS(ValueType):
    # ---------- Fields ---------- #
    
    @property
    def cbStruct(self) -> IntType: ...
    
    @cbStruct.setter
    def cbStruct(self, value: IntType) -> None: ...
    
    @property
    def dwTickCountDeadline(self) -> IntType: ...
    
    @dwTickCountDeadline.setter
    def dwTickCountDeadline(self, value: IntType) -> None: ...
    
    @property
    def grfFlags(self) -> IntType: ...
    
    @grfFlags.setter
    def grfFlags(self, value: IntType) -> None: ...
    
    @property
    def grfMode(self) -> IntType: ...
    
    @grfMode.setter
    def grfMode(self, value: IntType) -> None: ...
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CONNECTDATA(ValueType):
    # ---------- Fields ---------- #
    
    @property
    def dwCookie(self) -> IntType: ...
    
    @dwCookie.setter
    def dwCookie(self, value: IntType) -> None: ...
    
    @property
    def pUnk(self) -> ObjectType: ...
    
    @pUnk.setter
    def pUnk(self, value: ObjectType) -> None: ...
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DISPPARAMS(ValueType):
    # ---------- Fields ---------- #
    
    @property
    def cArgs(self) -> IntType: ...
    
    @cArgs.setter
    def cArgs(self, value: IntType) -> None: ...
    
    @property
    def cNamedArgs(self) -> IntType: ...
    
    @cNamedArgs.setter
    def cNamedArgs(self, value: IntType) -> None: ...
    
    @property
    def rgdispidNamedArgs(self) -> NIntType: ...
    
    @rgdispidNamedArgs.setter
    def rgdispidNamedArgs(self, value: NIntType) -> None: ...
    
    @property
    def rgvarg(self) -> NIntType: ...
    
    @rgvarg.setter
    def rgvarg(self, value: NIntType) -> None: ...
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ELEMDESC(ValueType):
    # ---------- Fields ---------- #
    
    @property
    def desc(self) -> DESCUNION: ...
    
    @desc.setter
    def desc(self, value: DESCUNION) -> None: ...
    
    @property
    def tdesc(self) -> TYPEDESC: ...
    
    @tdesc.setter
    def tdesc(self, value: TYPEDESC) -> None: ...
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # ---------- Sub Structs ---------- #
    
    class DESCUNION(ValueType):
        # ---------- Fields ---------- #
        
        @property
        def idldesc(self) -> IDLDESC: ...
        
        @idldesc.setter
        def idldesc(self, value: IDLDESC) -> None: ...
        
        @property
        def paramdesc(self) -> PARAMDESC: ...
        
        @paramdesc.setter
        def paramdesc(self, value: PARAMDESC) -> None: ...
        
        # No Constructors
        
        # No Properties
        
        # No Methods
        
        # No Events
        
        # No Sub Classes
        
        # No Sub Structs
        
        # No Sub Interfaces
        
        # No Sub Enums
    
    
    # No Sub Interfaces
    
    # No Sub Enums


class EXCEPINFO(ValueType):
    # ---------- Fields ---------- #
    
    @property
    def bstrDescription(self) -> StringType: ...
    
    @bstrDescription.setter
    def bstrDescription(self, value: StringType) -> None: ...
    
    @property
    def bstrHelpFile(self) -> StringType: ...
    
    @bstrHelpFile.setter
    def bstrHelpFile(self, value: StringType) -> None: ...
    
    @property
    def bstrSource(self) -> StringType: ...
    
    @bstrSource.setter
    def bstrSource(self, value: StringType) -> None: ...
    
    @property
    def dwHelpContext(self) -> IntType: ...
    
    @dwHelpContext.setter
    def dwHelpContext(self, value: IntType) -> None: ...
    
    @property
    def pfnDeferredFillIn(self) -> NIntType: ...
    
    @pfnDeferredFillIn.setter
    def pfnDeferredFillIn(self, value: NIntType) -> None: ...
    
    @property
    def pvReserved(self) -> NIntType: ...
    
    @pvReserved.setter
    def pvReserved(self, value: NIntType) -> None: ...
    
    @property
    def scode(self) -> IntType: ...
    
    @scode.setter
    def scode(self, value: IntType) -> None: ...
    
    @property
    def wCode(self) -> ShortType: ...
    
    @wCode.setter
    def wCode(self, value: ShortType) -> None: ...
    
    @property
    def wReserved(self) -> ShortType: ...
    
    @wReserved.setter
    def wReserved(self, value: ShortType) -> None: ...
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class FILETIME(ValueType):
    # ---------- Fields ---------- #
    
    @property
    def dwHighDateTime(self) -> IntType: ...
    
    @dwHighDateTime.setter
    def dwHighDateTime(self, value: IntType) -> None: ...
    
    @property
    def dwLowDateTime(self) -> IntType: ...
    
    @dwLowDateTime.setter
    def dwLowDateTime(self, value: IntType) -> None: ...
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


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


class FUNCDESC(ValueType):
    # ---------- Fields ---------- #
    
    @property
    def cParams(self) -> ShortType: ...
    
    @cParams.setter
    def cParams(self, value: ShortType) -> None: ...
    
    @property
    def cParamsOpt(self) -> ShortType: ...
    
    @cParamsOpt.setter
    def cParamsOpt(self, value: ShortType) -> None: ...
    
    @property
    def cScodes(self) -> ShortType: ...
    
    @cScodes.setter
    def cScodes(self, value: ShortType) -> None: ...
    
    @property
    def callconv(self) -> CALLCONV: ...
    
    @callconv.setter
    def callconv(self, value: CALLCONV) -> None: ...
    
    @property
    def elemdescFunc(self) -> ELEMDESC: ...
    
    @elemdescFunc.setter
    def elemdescFunc(self, value: ELEMDESC) -> None: ...
    
    @property
    def funckind(self) -> FUNCKIND: ...
    
    @funckind.setter
    def funckind(self, value: FUNCKIND) -> None: ...
    
    @property
    def invkind(self) -> INVOKEKIND: ...
    
    @invkind.setter
    def invkind(self, value: INVOKEKIND) -> None: ...
    
    @property
    def lprgelemdescParam(self) -> NIntType: ...
    
    @lprgelemdescParam.setter
    def lprgelemdescParam(self, value: NIntType) -> None: ...
    
    @property
    def lprgscode(self) -> NIntType: ...
    
    @lprgscode.setter
    def lprgscode(self, value: NIntType) -> None: ...
    
    @property
    def memid(self) -> IntType: ...
    
    @memid.setter
    def memid(self, value: IntType) -> None: ...
    
    @property
    def oVft(self) -> ShortType: ...
    
    @oVft.setter
    def oVft(self, value: ShortType) -> None: ...
    
    @property
    def wFuncFlags(self) -> ShortType: ...
    
    @wFuncFlags.setter
    def wFuncFlags(self, value: ShortType) -> None: ...
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class IDLDESC(ValueType):
    # ---------- Fields ---------- #
    
    @property
    def dwReserved(self) -> NIntType: ...
    
    @dwReserved.setter
    def dwReserved(self, value: NIntType) -> None: ...
    
    @property
    def wIDLFlags(self) -> IDLFLAG: ...
    
    @wIDLFlags.setter
    def wIDLFlags(self, value: IDLFLAG) -> None: ...
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PARAMDESC(ValueType):
    # ---------- Fields ---------- #
    
    @property
    def lpVarValue(self) -> NIntType: ...
    
    @lpVarValue.setter
    def lpVarValue(self, value: NIntType) -> None: ...
    
    @property
    def wParamFlags(self) -> PARAMFLAG: ...
    
    @wParamFlags.setter
    def wParamFlags(self, value: PARAMFLAG) -> None: ...
    
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


class STATSTG(ValueType):
    # ---------- Fields ---------- #
    
    @property
    def atime(self) -> FILETIME: ...
    
    @atime.setter
    def atime(self, value: FILETIME) -> None: ...
    
    @property
    def cbSize(self) -> LongType: ...
    
    @cbSize.setter
    def cbSize(self, value: LongType) -> None: ...
    
    @property
    def clsid(self) -> Guid: ...
    
    @clsid.setter
    def clsid(self, value: Guid) -> None: ...
    
    @property
    def ctime(self) -> FILETIME: ...
    
    @ctime.setter
    def ctime(self, value: FILETIME) -> None: ...
    
    @property
    def grfLocksSupported(self) -> IntType: ...
    
    @grfLocksSupported.setter
    def grfLocksSupported(self, value: IntType) -> None: ...
    
    @property
    def grfMode(self) -> IntType: ...
    
    @grfMode.setter
    def grfMode(self, value: IntType) -> None: ...
    
    @property
    def grfStateBits(self) -> IntType: ...
    
    @grfStateBits.setter
    def grfStateBits(self, value: IntType) -> None: ...
    
    @property
    def mtime(self) -> FILETIME: ...
    
    @mtime.setter
    def mtime(self, value: FILETIME) -> None: ...
    
    @property
    def pwcsName(self) -> StringType: ...
    
    @pwcsName.setter
    def pwcsName(self, value: StringType) -> None: ...
    
    @property
    def reserved(self) -> IntType: ...
    
    @reserved.setter
    def reserved(self, value: IntType) -> None: ...
    
    @property
    def type(self) -> IntType: ...
    
    @type.setter
    def type(self, value: IntType) -> None: ...
    
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


class TYPEATTR(ValueType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def MEMBER_ID_NIL() -> IntType: ...
    
    @property
    def cFuncs(self) -> ShortType: ...
    
    @cFuncs.setter
    def cFuncs(self, value: ShortType) -> None: ...
    
    @property
    def cImplTypes(self) -> ShortType: ...
    
    @cImplTypes.setter
    def cImplTypes(self, value: ShortType) -> None: ...
    
    @property
    def cVars(self) -> ShortType: ...
    
    @cVars.setter
    def cVars(self, value: ShortType) -> None: ...
    
    @property
    def cbAlignment(self) -> ShortType: ...
    
    @cbAlignment.setter
    def cbAlignment(self, value: ShortType) -> None: ...
    
    @property
    def cbSizeInstance(self) -> IntType: ...
    
    @cbSizeInstance.setter
    def cbSizeInstance(self, value: IntType) -> None: ...
    
    @property
    def cbSizeVft(self) -> ShortType: ...
    
    @cbSizeVft.setter
    def cbSizeVft(self, value: ShortType) -> None: ...
    
    @property
    def dwReserved(self) -> IntType: ...
    
    @dwReserved.setter
    def dwReserved(self, value: IntType) -> None: ...
    
    @property
    def guid(self) -> Guid: ...
    
    @guid.setter
    def guid(self, value: Guid) -> None: ...
    
    @property
    def idldescType(self) -> IDLDESC: ...
    
    @idldescType.setter
    def idldescType(self, value: IDLDESC) -> None: ...
    
    @property
    def lcid(self) -> IntType: ...
    
    @lcid.setter
    def lcid(self, value: IntType) -> None: ...
    
    @property
    def lpstrSchema(self) -> NIntType: ...
    
    @lpstrSchema.setter
    def lpstrSchema(self, value: NIntType) -> None: ...
    
    @property
    def memidConstructor(self) -> IntType: ...
    
    @memidConstructor.setter
    def memidConstructor(self, value: IntType) -> None: ...
    
    @property
    def memidDestructor(self) -> IntType: ...
    
    @memidDestructor.setter
    def memidDestructor(self, value: IntType) -> None: ...
    
    @property
    def tdescAlias(self) -> TYPEDESC: ...
    
    @tdescAlias.setter
    def tdescAlias(self, value: TYPEDESC) -> None: ...
    
    @property
    def typekind(self) -> TYPEKIND: ...
    
    @typekind.setter
    def typekind(self, value: TYPEKIND) -> None: ...
    
    @property
    def wMajorVerNum(self) -> ShortType: ...
    
    @wMajorVerNum.setter
    def wMajorVerNum(self, value: ShortType) -> None: ...
    
    @property
    def wMinorVerNum(self) -> ShortType: ...
    
    @wMinorVerNum.setter
    def wMinorVerNum(self, value: ShortType) -> None: ...
    
    @property
    def wTypeFlags(self) -> TYPEFLAGS: ...
    
    @wTypeFlags.setter
    def wTypeFlags(self, value: TYPEFLAGS) -> None: ...
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TYPEDESC(ValueType):
    # ---------- Fields ---------- #
    
    @property
    def lpValue(self) -> NIntType: ...
    
    @lpValue.setter
    def lpValue(self, value: NIntType) -> None: ...
    
    @property
    def vt(self) -> ShortType: ...
    
    @vt.setter
    def vt(self, value: ShortType) -> None: ...
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TYPELIBATTR(ValueType):
    # ---------- Fields ---------- #
    
    @property
    def guid(self) -> Guid: ...
    
    @guid.setter
    def guid(self, value: Guid) -> None: ...
    
    @property
    def lcid(self) -> IntType: ...
    
    @lcid.setter
    def lcid(self, value: IntType) -> None: ...
    
    @property
    def syskind(self) -> SYSKIND: ...
    
    @syskind.setter
    def syskind(self, value: SYSKIND) -> None: ...
    
    @property
    def wLibFlags(self) -> LIBFLAGS: ...
    
    @wLibFlags.setter
    def wLibFlags(self, value: LIBFLAGS) -> None: ...
    
    @property
    def wMajorVerNum(self) -> ShortType: ...
    
    @wMajorVerNum.setter
    def wMajorVerNum(self, value: ShortType) -> None: ...
    
    @property
    def wMinorVerNum(self) -> ShortType: ...
    
    @wMinorVerNum.setter
    def wMinorVerNum(self, value: ShortType) -> None: ...
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class VARDESC(ValueType):
    # ---------- Fields ---------- #
    
    @property
    def desc(self) -> DESCUNION: ...
    
    @desc.setter
    def desc(self, value: DESCUNION) -> None: ...
    
    @property
    def elemdescVar(self) -> ELEMDESC: ...
    
    @elemdescVar.setter
    def elemdescVar(self, value: ELEMDESC) -> None: ...
    
    @property
    def lpstrSchema(self) -> StringType: ...
    
    @lpstrSchema.setter
    def lpstrSchema(self, value: StringType) -> None: ...
    
    @property
    def memid(self) -> IntType: ...
    
    @memid.setter
    def memid(self, value: IntType) -> None: ...
    
    @property
    def varkind(self) -> VARKIND: ...
    
    @varkind.setter
    def varkind(self, value: VARKIND) -> None: ...
    
    @property
    def wVarFlags(self) -> ShortType: ...
    
    @wVarFlags.setter
    def wVarFlags(self, value: ShortType) -> None: ...
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # ---------- Sub Structs ---------- #
    
    class DESCUNION(ValueType):
        # ---------- Fields ---------- #
        
        @property
        def lpvarValue(self) -> NIntType: ...
        
        @lpvarValue.setter
        def lpvarValue(self, value: NIntType) -> None: ...
        
        @property
        def oInst(self) -> IntType: ...
        
        @oInst.setter
        def oInst(self, value: IntType) -> None: ...
        
        # No Constructors
        
        # No Properties
        
        # No Methods
        
        # No Events
        
        # No Sub Classes
        
        # No Sub Structs
        
        # No Sub Interfaces
        
        # No Sub Enums
    
    
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


class IBindCtx(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def EnumObjectParam(self, ppenum: IEnumString) -> Tuple[VoidType, IEnumString]: ...
    
    def GetBindOptions(self, pbindopts: BIND_OPTS) -> Tuple[VoidType, BIND_OPTS]: ...
    
    def GetObjectParam(self, pszKey: StringType, ppunk: ObjectType) -> Tuple[VoidType, ObjectType]: ...
    
    def GetRunningObjectTable(self, pprot: IRunningObjectTable) -> Tuple[VoidType, IRunningObjectTable]: ...
    
    def RegisterObjectBound(self, punk: ObjectType) -> VoidType: ...
    
    def RegisterObjectParam(self, pszKey: StringType, punk: ObjectType) -> VoidType: ...
    
    def ReleaseBoundObjects(self) -> VoidType: ...
    
    def RevokeObjectBound(self, punk: ObjectType) -> VoidType: ...
    
    def RevokeObjectParam(self, pszKey: StringType) -> IntType: ...
    
    def SetBindOptions(self, pbindopts: BIND_OPTS) -> Tuple[VoidType, BIND_OPTS]: ...
    
    # No Events


class IConnectionPoint(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Advise(self, pUnkSink: ObjectType, pdwCookie: IntType) -> Tuple[VoidType, IntType]: ...
    
    def EnumConnections(self, ppEnum: IEnumConnections) -> Tuple[VoidType, IEnumConnections]: ...
    
    def GetConnectionInterface(self, pIID: Guid) -> Tuple[VoidType, Guid]: ...
    
    def GetConnectionPointContainer(self, ppCPC: IConnectionPointContainer) -> Tuple[VoidType, IConnectionPointContainer]: ...
    
    def Unadvise(self, dwCookie: IntType) -> VoidType: ...
    
    # No Events


class IConnectionPointContainer(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def EnumConnectionPoints(self, ppEnum: IEnumConnectionPoints) -> Tuple[VoidType, IEnumConnectionPoints]: ...
    
    def FindConnectionPoint(self, riid: Guid, ppCP: IConnectionPoint) -> Tuple[VoidType, Guid, IConnectionPoint]: ...
    
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


class IEnumConnectionPoints(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Clone(self, ppenum: IEnumConnectionPoints) -> Tuple[VoidType, IEnumConnectionPoints]: ...
    
    def Next(self, celt: IntType, rgelt: ArrayType[IConnectionPoint], pceltFetched: NIntType) -> Tuple[IntType, ArrayType[IConnectionPoint]]: ...
    
    def Reset(self) -> VoidType: ...
    
    def Skip(self, celt: IntType) -> IntType: ...
    
    # No Events


class IEnumConnections(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Clone(self, ppenum: IEnumConnections) -> Tuple[VoidType, IEnumConnections]: ...
    
    def Next(self, celt: IntType, rgelt: ArrayType[CONNECTDATA], pceltFetched: NIntType) -> Tuple[IntType, ArrayType[CONNECTDATA]]: ...
    
    def Reset(self) -> VoidType: ...
    
    def Skip(self, celt: IntType) -> IntType: ...
    
    # No Events


class IEnumFORMATETC(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Clone(self, newEnum: IEnumFORMATETC) -> Tuple[VoidType, IEnumFORMATETC]: ...
    
    def Next(self, celt: IntType, rgelt: ArrayType[FORMATETC], pceltFetched: ArrayType[IntType]) -> Tuple[IntType, ArrayType[FORMATETC], ArrayType[IntType]]: ...
    
    def Reset(self) -> IntType: ...
    
    def Skip(self, celt: IntType) -> IntType: ...
    
    # No Events


class IEnumMoniker(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Clone(self, ppenum: IEnumMoniker) -> Tuple[VoidType, IEnumMoniker]: ...
    
    def Next(self, celt: IntType, rgelt: ArrayType[IMoniker], pceltFetched: NIntType) -> Tuple[IntType, ArrayType[IMoniker]]: ...
    
    def Reset(self) -> VoidType: ...
    
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


class IEnumString(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Clone(self, ppenum: IEnumString) -> Tuple[VoidType, IEnumString]: ...
    
    def Next(self, celt: IntType, rgelt: ArrayType[StringType], pceltFetched: NIntType) -> Tuple[IntType, ArrayType[StringType]]: ...
    
    def Reset(self) -> VoidType: ...
    
    def Skip(self, celt: IntType) -> IntType: ...
    
    # No Events


class IEnumVARIANT(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> IEnumVARIANT: ...
    
    def Next(self, celt: IntType, rgVar: ArrayType[ObjectType], pceltFetched: NIntType) -> Tuple[IntType, ArrayType[ObjectType]]: ...
    
    def Reset(self) -> IntType: ...
    
    def Skip(self, celt: IntType) -> IntType: ...
    
    # No Events


class IEnumerable(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetEnumerator(self) -> IEnumerator: ...
    
    # No Events


class IEnumerator(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def Current(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def MoveNext(self) -> BooleanType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Current(self) -> ObjectType: ...
    
    # No Events


class IExpando(Protocol, IReflect):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def AddField(self, name: StringType) -> FieldInfo: ...
    
    def AddMethod(self, name: StringType, method: Delegate) -> MethodInfo: ...
    
    def AddProperty(self, name: StringType) -> PropertyInfo: ...
    
    def RemoveMember(self, m: MemberInfo) -> VoidType: ...
    
    # No Events


class IMoniker(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BindToObject(self, pbc: IBindCtx, pmkToLeft: IMoniker, riidResult: Guid, ppvResult: ObjectType) -> Tuple[VoidType, Guid, ObjectType]: ...
    
    def BindToStorage(self, pbc: IBindCtx, pmkToLeft: IMoniker, riid: Guid, ppvObj: ObjectType) -> Tuple[VoidType, Guid, ObjectType]: ...
    
    def CommonPrefixWith(self, pmkOther: IMoniker, ppmkPrefix: IMoniker) -> Tuple[VoidType, IMoniker]: ...
    
    def ComposeWith(self, pmkRight: IMoniker, fOnlyIfNotGeneric: BooleanType, ppmkComposite: IMoniker) -> Tuple[VoidType, IMoniker]: ...
    
    def Enum(self, fForward: BooleanType, ppenumMoniker: IEnumMoniker) -> Tuple[VoidType, IEnumMoniker]: ...
    
    def GetClassID(self, pClassID: Guid) -> Tuple[VoidType, Guid]: ...
    
    def GetDisplayName(self, pbc: IBindCtx, pmkToLeft: IMoniker, ppszDisplayName: StringType) -> Tuple[VoidType, StringType]: ...
    
    def GetSizeMax(self, pcbSize: LongType) -> Tuple[VoidType, LongType]: ...
    
    def GetTimeOfLastChange(self, pbc: IBindCtx, pmkToLeft: IMoniker, pFileTime: FILETIME) -> Tuple[VoidType, FILETIME]: ...
    
    def Hash(self, pdwHash: IntType) -> Tuple[VoidType, IntType]: ...
    
    def Inverse(self, ppmk: IMoniker) -> Tuple[VoidType, IMoniker]: ...
    
    def IsDirty(self) -> IntType: ...
    
    def IsEqual(self, pmkOtherMoniker: IMoniker) -> IntType: ...
    
    def IsRunning(self, pbc: IBindCtx, pmkToLeft: IMoniker, pmkNewlyRunning: IMoniker) -> IntType: ...
    
    def IsSystemMoniker(self, pdwMksys: IntType) -> Tuple[IntType, IntType]: ...
    
    def Load(self, pStm: IStream) -> VoidType: ...
    
    def ParseDisplayName(self, pbc: IBindCtx, pmkToLeft: IMoniker, pszDisplayName: StringType, pchEaten: IntType, ppmkOut: IMoniker) -> Tuple[VoidType, IntType, IMoniker]: ...
    
    def Reduce(self, pbc: IBindCtx, dwReduceHowFar: IntType, ppmkToLeft: IMoniker, ppmkReduced: IMoniker) -> Tuple[VoidType, IMoniker, IMoniker]: ...
    
    def RelativePathTo(self, pmkOther: IMoniker, ppmkRelPath: IMoniker) -> Tuple[VoidType, IMoniker]: ...
    
    def Save(self, pStm: IStream, fClearDirty: BooleanType) -> VoidType: ...
    
    # No Events


class IPersistFile(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetClassID(self, pClassID: Guid) -> Tuple[VoidType, Guid]: ...
    
    def GetCurFile(self, ppszFileName: StringType) -> Tuple[VoidType, StringType]: ...
    
    def IsDirty(self) -> IntType: ...
    
    def Load(self, pszFileName: StringType, dwMode: IntType) -> VoidType: ...
    
    def Save(self, pszFileName: StringType, fRemember: BooleanType) -> VoidType: ...
    
    def SaveCompleted(self, pszFileName: StringType) -> VoidType: ...
    
    # No Events


class IReflect(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def UnderlyingSystemType(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def GetField(self, name: StringType, bindingAttr: BindingFlags) -> FieldInfo: ...
    
    def GetFields(self, bindingAttr: BindingFlags) -> ArrayType[FieldInfo]: ...
    
    def GetMember(self, name: StringType, bindingAttr: BindingFlags) -> ArrayType[MemberInfo]: ...
    
    def GetMembers(self, bindingAttr: BindingFlags) -> ArrayType[MemberInfo]: ...
    
    @overload
    def GetMethod(self, name: StringType, bindingAttr: BindingFlags, binder: Binder, types: ArrayType[TypeType], modifiers: ArrayType[ParameterModifier]) -> MethodInfo: ...
    
    @overload
    def GetMethod(self, name: StringType, bindingAttr: BindingFlags) -> MethodInfo: ...
    
    def GetMethods(self, bindingAttr: BindingFlags) -> ArrayType[MethodInfo]: ...
    
    def GetProperties(self, bindingAttr: BindingFlags) -> ArrayType[PropertyInfo]: ...
    
    @overload
    def GetProperty(self, name: StringType, bindingAttr: BindingFlags) -> PropertyInfo: ...
    
    @overload
    def GetProperty(self, name: StringType, bindingAttr: BindingFlags, binder: Binder, returnType: TypeType, types: ArrayType[TypeType], modifiers: ArrayType[ParameterModifier]) -> PropertyInfo: ...
    
    def InvokeMember(self, name: StringType, invokeAttr: BindingFlags, binder: Binder, target: ObjectType, args: ArrayType[ObjectType], modifiers: ArrayType[ParameterModifier], culture: CultureInfo, namedParameters: ArrayType[StringType]) -> ObjectType: ...
    
    def get_UnderlyingSystemType(self) -> TypeType: ...
    
    # No Events


class IRunningObjectTable(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def EnumRunning(self, ppenumMoniker: IEnumMoniker) -> Tuple[VoidType, IEnumMoniker]: ...
    
    def GetObject(self, pmkObjectName: IMoniker, ppunkObject: ObjectType) -> Tuple[IntType, ObjectType]: ...
    
    def GetTimeOfLastChange(self, pmkObjectName: IMoniker, pfiletime: FILETIME) -> Tuple[IntType, FILETIME]: ...
    
    def IsRunning(self, pmkObjectName: IMoniker) -> IntType: ...
    
    def NoteChangeTime(self, dwRegister: IntType, pfiletime: FILETIME) -> Tuple[VoidType, FILETIME]: ...
    
    def Register(self, grfFlags: IntType, punkObject: ObjectType, pmkObjectName: IMoniker) -> IntType: ...
    
    def Revoke(self, dwRegister: IntType) -> VoidType: ...
    
    # No Events


class IStream(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Clone(self, ppstm: IStream) -> Tuple[VoidType, IStream]: ...
    
    def Commit(self, grfCommitFlags: IntType) -> VoidType: ...
    
    def CopyTo(self, pstm: IStream, cb: LongType, pcbRead: NIntType, pcbWritten: NIntType) -> VoidType: ...
    
    def LockRegion(self, libOffset: LongType, cb: LongType, dwLockType: IntType) -> VoidType: ...
    
    def Read(self, pv: ArrayType[ByteType], cb: IntType, pcbRead: NIntType) -> Tuple[VoidType, ArrayType[ByteType]]: ...
    
    def Revert(self) -> VoidType: ...
    
    def Seek(self, dlibMove: LongType, dwOrigin: IntType, plibNewPosition: NIntType) -> VoidType: ...
    
    def SetSize(self, libNewSize: LongType) -> VoidType: ...
    
    def Stat(self, pstatstg: STATSTG, grfStatFlag: IntType) -> Tuple[VoidType, STATSTG]: ...
    
    def UnlockRegion(self, libOffset: LongType, cb: LongType, dwLockType: IntType) -> VoidType: ...
    
    def Write(self, pv: ArrayType[ByteType], cb: IntType, pcbWritten: NIntType) -> VoidType: ...
    
    # No Events


class ITypeComp(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Bind(self, szName: StringType, lHashVal: IntType, wFlags: ShortType, ppTInfo: ITypeInfo, pDescKind: DESCKIND, pBindPtr: BINDPTR) -> Tuple[VoidType, ITypeInfo, DESCKIND, BINDPTR]: ...
    
    def BindType(self, szName: StringType, lHashVal: IntType, ppTInfo: ITypeInfo, ppTComp: ITypeComp) -> Tuple[VoidType, ITypeInfo, ITypeComp]: ...
    
    # No Events


class ITypeInfo(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def AddressOfMember(self, memid: IntType, invKind: INVOKEKIND, ppv: NIntType) -> Tuple[VoidType, NIntType]: ...
    
    def CreateInstance(self, pUnkOuter: ObjectType, riid: Guid, ppvObj: ObjectType) -> Tuple[VoidType, Guid, ObjectType]: ...
    
    def GetContainingTypeLib(self, ppTLB: ITypeLib, pIndex: IntType) -> Tuple[VoidType, ITypeLib, IntType]: ...
    
    def GetDllEntry(self, memid: IntType, invKind: INVOKEKIND, pBstrDllName: NIntType, pBstrName: NIntType, pwOrdinal: NIntType) -> VoidType: ...
    
    def GetDocumentation(self, index: IntType, strName: StringType, strDocString: StringType, dwHelpContext: IntType, strHelpFile: StringType) -> Tuple[VoidType, StringType, StringType, IntType, StringType]: ...
    
    def GetFuncDesc(self, index: IntType, ppFuncDesc: NIntType) -> Tuple[VoidType, NIntType]: ...
    
    def GetIDsOfNames(self, rgszNames: ArrayType[StringType], cNames: IntType, pMemId: ArrayType[IntType]) -> Tuple[VoidType, ArrayType[IntType]]: ...
    
    def GetImplTypeFlags(self, index: IntType, pImplTypeFlags: IMPLTYPEFLAGS) -> Tuple[VoidType, IMPLTYPEFLAGS]: ...
    
    def GetMops(self, memid: IntType, pBstrMops: StringType) -> Tuple[VoidType, StringType]: ...
    
    def GetNames(self, memid: IntType, rgBstrNames: ArrayType[StringType], cMaxNames: IntType, pcNames: IntType) -> Tuple[VoidType, ArrayType[StringType], IntType]: ...
    
    def GetRefTypeInfo(self, hRef: IntType, ppTI: ITypeInfo) -> Tuple[VoidType, ITypeInfo]: ...
    
    def GetRefTypeOfImplType(self, index: IntType, href: IntType) -> Tuple[VoidType, IntType]: ...
    
    def GetTypeAttr(self, ppTypeAttr: NIntType) -> Tuple[VoidType, NIntType]: ...
    
    def GetTypeComp(self, ppTComp: ITypeComp) -> Tuple[VoidType, ITypeComp]: ...
    
    def GetVarDesc(self, index: IntType, ppVarDesc: NIntType) -> Tuple[VoidType, NIntType]: ...
    
    def Invoke(self, pvInstance: ObjectType, memid: IntType, wFlags: ShortType, pDispParams: DISPPARAMS, pVarResult: NIntType, pExcepInfo: NIntType, puArgErr: IntType) -> Tuple[VoidType, DISPPARAMS, IntType]: ...
    
    def ReleaseFuncDesc(self, pFuncDesc: NIntType) -> VoidType: ...
    
    def ReleaseTypeAttr(self, pTypeAttr: NIntType) -> VoidType: ...
    
    def ReleaseVarDesc(self, pVarDesc: NIntType) -> VoidType: ...
    
    # No Events


class ITypeInfo2(Protocol, ITypeInfo):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def AddressOfMember(self, memid: IntType, invKind: INVOKEKIND, ppv: NIntType) -> Tuple[VoidType, NIntType]: ...
    
    def CreateInstance(self, pUnkOuter: ObjectType, riid: Guid, ppvObj: ObjectType) -> Tuple[VoidType, Guid, ObjectType]: ...
    
    def GetAllCustData(self, pCustData: NIntType) -> VoidType: ...
    
    def GetAllFuncCustData(self, index: IntType, pCustData: NIntType) -> VoidType: ...
    
    def GetAllImplTypeCustData(self, index: IntType, pCustData: NIntType) -> VoidType: ...
    
    def GetAllParamCustData(self, indexFunc: IntType, indexParam: IntType, pCustData: NIntType) -> VoidType: ...
    
    def GetAllVarCustData(self, index: IntType, pCustData: NIntType) -> VoidType: ...
    
    def GetContainingTypeLib(self, ppTLB: ITypeLib, pIndex: IntType) -> Tuple[VoidType, ITypeLib, IntType]: ...
    
    def GetCustData(self, guid: Guid, pVarVal: ObjectType) -> Tuple[VoidType, Guid, ObjectType]: ...
    
    def GetDllEntry(self, memid: IntType, invKind: INVOKEKIND, pBstrDllName: NIntType, pBstrName: NIntType, pwOrdinal: NIntType) -> VoidType: ...
    
    def GetDocumentation(self, index: IntType, strName: StringType, strDocString: StringType, dwHelpContext: IntType, strHelpFile: StringType) -> Tuple[VoidType, StringType, StringType, IntType, StringType]: ...
    
    def GetDocumentation2(self, memid: IntType, pbstrHelpString: StringType, pdwHelpStringContext: IntType, pbstrHelpStringDll: StringType) -> Tuple[VoidType, StringType, IntType, StringType]: ...
    
    def GetFuncCustData(self, index: IntType, guid: Guid, pVarVal: ObjectType) -> Tuple[VoidType, Guid, ObjectType]: ...
    
    def GetFuncDesc(self, index: IntType, ppFuncDesc: NIntType) -> Tuple[VoidType, NIntType]: ...
    
    def GetFuncIndexOfMemId(self, memid: IntType, invKind: INVOKEKIND, pFuncIndex: IntType) -> Tuple[VoidType, IntType]: ...
    
    def GetIDsOfNames(self, rgszNames: ArrayType[StringType], cNames: IntType, pMemId: ArrayType[IntType]) -> Tuple[VoidType, ArrayType[IntType]]: ...
    
    def GetImplTypeCustData(self, index: IntType, guid: Guid, pVarVal: ObjectType) -> Tuple[VoidType, Guid, ObjectType]: ...
    
    def GetImplTypeFlags(self, index: IntType, pImplTypeFlags: IMPLTYPEFLAGS) -> Tuple[VoidType, IMPLTYPEFLAGS]: ...
    
    def GetMops(self, memid: IntType, pBstrMops: StringType) -> Tuple[VoidType, StringType]: ...
    
    def GetNames(self, memid: IntType, rgBstrNames: ArrayType[StringType], cMaxNames: IntType, pcNames: IntType) -> Tuple[VoidType, ArrayType[StringType], IntType]: ...
    
    def GetParamCustData(self, indexFunc: IntType, indexParam: IntType, guid: Guid, pVarVal: ObjectType) -> Tuple[VoidType, Guid, ObjectType]: ...
    
    def GetRefTypeInfo(self, hRef: IntType, ppTI: ITypeInfo) -> Tuple[VoidType, ITypeInfo]: ...
    
    def GetRefTypeOfImplType(self, index: IntType, href: IntType) -> Tuple[VoidType, IntType]: ...
    
    def GetTypeAttr(self, ppTypeAttr: NIntType) -> Tuple[VoidType, NIntType]: ...
    
    def GetTypeComp(self, ppTComp: ITypeComp) -> Tuple[VoidType, ITypeComp]: ...
    
    def GetTypeFlags(self, pTypeFlags: IntType) -> Tuple[VoidType, IntType]: ...
    
    def GetTypeKind(self, pTypeKind: TYPEKIND) -> Tuple[VoidType, TYPEKIND]: ...
    
    def GetVarCustData(self, index: IntType, guid: Guid, pVarVal: ObjectType) -> Tuple[VoidType, Guid, ObjectType]: ...
    
    def GetVarDesc(self, index: IntType, ppVarDesc: NIntType) -> Tuple[VoidType, NIntType]: ...
    
    def GetVarIndexOfMemId(self, memid: IntType, pVarIndex: IntType) -> Tuple[VoidType, IntType]: ...
    
    def Invoke(self, pvInstance: ObjectType, memid: IntType, wFlags: ShortType, pDispParams: DISPPARAMS, pVarResult: NIntType, pExcepInfo: NIntType, puArgErr: IntType) -> Tuple[VoidType, DISPPARAMS, IntType]: ...
    
    def ReleaseFuncDesc(self, pFuncDesc: NIntType) -> VoidType: ...
    
    def ReleaseTypeAttr(self, pTypeAttr: NIntType) -> VoidType: ...
    
    def ReleaseVarDesc(self, pVarDesc: NIntType) -> VoidType: ...
    
    # No Events


class ITypeLib(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def FindName(self, szNameBuf: StringType, lHashVal: IntType, ppTInfo: ArrayType[ITypeInfo], rgMemId: ArrayType[IntType], pcFound: ShortType) -> Tuple[VoidType, ArrayType[ITypeInfo], ArrayType[IntType], ShortType]: ...
    
    def GetDocumentation(self, index: IntType, strName: StringType, strDocString: StringType, dwHelpContext: IntType, strHelpFile: StringType) -> Tuple[VoidType, StringType, StringType, IntType, StringType]: ...
    
    def GetLibAttr(self, ppTLibAttr: NIntType) -> Tuple[VoidType, NIntType]: ...
    
    def GetTypeComp(self, ppTComp: ITypeComp) -> Tuple[VoidType, ITypeComp]: ...
    
    def GetTypeInfo(self, index: IntType, ppTI: ITypeInfo) -> Tuple[VoidType, ITypeInfo]: ...
    
    def GetTypeInfoCount(self) -> IntType: ...
    
    def GetTypeInfoOfGuid(self, guid: Guid, ppTInfo: ITypeInfo) -> Tuple[VoidType, Guid, ITypeInfo]: ...
    
    def GetTypeInfoType(self, index: IntType, pTKind: TYPEKIND) -> Tuple[VoidType, TYPEKIND]: ...
    
    def IsName(self, szNameBuf: StringType, lHashVal: IntType) -> BooleanType: ...
    
    def ReleaseTLibAttr(self, pTLibAttr: NIntType) -> VoidType: ...
    
    # No Events


class ITypeLib2(Protocol, ITypeLib):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def FindName(self, szNameBuf: StringType, lHashVal: IntType, ppTInfo: ArrayType[ITypeInfo], rgMemId: ArrayType[IntType], pcFound: ShortType) -> Tuple[VoidType, ArrayType[ITypeInfo], ArrayType[IntType], ShortType]: ...
    
    def GetAllCustData(self, pCustData: NIntType) -> VoidType: ...
    
    def GetCustData(self, guid: Guid, pVarVal: ObjectType) -> Tuple[VoidType, Guid, ObjectType]: ...
    
    def GetDocumentation(self, index: IntType, strName: StringType, strDocString: StringType, dwHelpContext: IntType, strHelpFile: StringType) -> Tuple[VoidType, StringType, StringType, IntType, StringType]: ...
    
    def GetDocumentation2(self, index: IntType, pbstrHelpString: StringType, pdwHelpStringContext: IntType, pbstrHelpStringDll: StringType) -> Tuple[VoidType, StringType, IntType, StringType]: ...
    
    def GetLibAttr(self, ppTLibAttr: NIntType) -> Tuple[VoidType, NIntType]: ...
    
    def GetLibStatistics(self, pcUniqueNames: NIntType, pcchUniqueNames: IntType) -> Tuple[VoidType, IntType]: ...
    
    def GetTypeComp(self, ppTComp: ITypeComp) -> Tuple[VoidType, ITypeComp]: ...
    
    def GetTypeInfo(self, index: IntType, ppTI: ITypeInfo) -> Tuple[VoidType, ITypeInfo]: ...
    
    def GetTypeInfoCount(self) -> IntType: ...
    
    def GetTypeInfoOfGuid(self, guid: Guid, ppTInfo: ITypeInfo) -> Tuple[VoidType, Guid, ITypeInfo]: ...
    
    def GetTypeInfoType(self, index: IntType, pTKind: TYPEKIND) -> Tuple[VoidType, TYPEKIND]: ...
    
    def IsName(self, szNameBuf: StringType, lHashVal: IntType) -> BooleanType: ...
    
    def ReleaseTLibAttr(self, pTLibAttr: NIntType) -> VoidType: ...
    
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


class CALLCONV(Enum):
    CC_CDECL: IntType = 1
    CC_MSCPASCAL: IntType = 2
    CC_PASCAL: IntType = 2
    CC_MACPASCAL: IntType = 3
    CC_STDCALL: IntType = 4
    CC_RESERVED: IntType = 5
    CC_SYSCALL: IntType = 6
    CC_MPWCDECL: IntType = 7
    CC_MPWPASCAL: IntType = 8
    CC_MAX: IntType = 9


class DATADIR(Enum):
    DATADIR_GET: IntType = 1
    DATADIR_SET: IntType = 2


class DESCKIND(Enum):
    DESCKIND_NONE: IntType = 0
    DESCKIND_FUNCDESC: IntType = 1
    DESCKIND_VARDESC: IntType = 2
    DESCKIND_TYPECOMP: IntType = 3
    DESCKIND_IMPLICITAPPOBJ: IntType = 4
    DESCKIND_MAX: IntType = 5


class DVASPECT(Enum):
    DVASPECT_CONTENT: IntType = 1
    DVASPECT_THUMBNAIL: IntType = 2
    DVASPECT_ICON: IntType = 4
    DVASPECT_DOCPRINT: IntType = 8


class FUNCFLAGS(Enum):
    FUNCFLAG_FRESTRICTED: ShortType = 1
    FUNCFLAG_FSOURCE: ShortType = 2
    FUNCFLAG_FBINDABLE: ShortType = 4
    FUNCFLAG_FREQUESTEDIT: ShortType = 8
    FUNCFLAG_FDISPLAYBIND: ShortType = 16
    FUNCFLAG_FDEFAULTBIND: ShortType = 32
    FUNCFLAG_FHIDDEN: ShortType = 64
    FUNCFLAG_FUSESGETLASTERROR: ShortType = 128
    FUNCFLAG_FDEFAULTCOLLELEM: ShortType = 256
    FUNCFLAG_FUIDEFAULT: ShortType = 512
    FUNCFLAG_FNONBROWSABLE: ShortType = 1024
    FUNCFLAG_FREPLACEABLE: ShortType = 2048
    FUNCFLAG_FIMMEDIATEBIND: ShortType = 4096


class FUNCKIND(Enum):
    FUNC_VIRTUAL: IntType = 0
    FUNC_PUREVIRTUAL: IntType = 1
    FUNC_NONVIRTUAL: IntType = 2
    FUNC_STATIC: IntType = 3
    FUNC_DISPATCH: IntType = 4


class IDLFLAG(Enum):
    IDLFLAG_NONE: ShortType = 0
    IDLFLAG_FIN: ShortType = 1
    IDLFLAG_FOUT: ShortType = 2
    IDLFLAG_FLCID: ShortType = 4
    IDLFLAG_FRETVAL: ShortType = 8


class IMPLTYPEFLAGS(Enum):
    IMPLTYPEFLAG_FDEFAULT: IntType = 1
    IMPLTYPEFLAG_FSOURCE: IntType = 2
    IMPLTYPEFLAG_FRESTRICTED: IntType = 4
    IMPLTYPEFLAG_FDEFAULTVTABLE: IntType = 8


class INVOKEKIND(Enum):
    INVOKE_FUNC: IntType = 1
    INVOKE_PROPERTYGET: IntType = 2
    INVOKE_PROPERTYPUT: IntType = 4
    INVOKE_PROPERTYPUTREF: IntType = 8


class LIBFLAGS(Enum):
    LIBFLAG_FRESTRICTED: ShortType = 1
    LIBFLAG_FCONTROL: ShortType = 2
    LIBFLAG_FHIDDEN: ShortType = 4
    LIBFLAG_FHASDISKIMAGE: ShortType = 8


class PARAMFLAG(Enum):
    PARAMFLAG_NONE: ShortType = 0
    PARAMFLAG_FIN: ShortType = 1
    PARAMFLAG_FOUT: ShortType = 2
    PARAMFLAG_FLCID: ShortType = 4
    PARAMFLAG_FRETVAL: ShortType = 8
    PARAMFLAG_FOPT: ShortType = 16
    PARAMFLAG_FHASDEFAULT: ShortType = 32
    PARAMFLAG_FHASCUSTDATA: ShortType = 64


class SYSKIND(Enum):
    SYS_WIN16: IntType = 0
    SYS_WIN32: IntType = 1
    SYS_MAC: IntType = 2
    SYS_WIN64: IntType = 3


class TYMED(Enum):
    TYMED_NULL: IntType = 0
    TYMED_HGLOBAL: IntType = 1
    TYMED_FILE: IntType = 2
    TYMED_ISTREAM: IntType = 4
    TYMED_ISTORAGE: IntType = 8
    TYMED_GDI: IntType = 16
    TYMED_MFPICT: IntType = 32
    TYMED_ENHMF: IntType = 64


class TYPEFLAGS(Enum):
    TYPEFLAG_FAPPOBJECT: ShortType = 1
    TYPEFLAG_FCANCREATE: ShortType = 2
    TYPEFLAG_FLICENSED: ShortType = 4
    TYPEFLAG_FPREDECLID: ShortType = 8
    TYPEFLAG_FHIDDEN: ShortType = 16
    TYPEFLAG_FCONTROL: ShortType = 32
    TYPEFLAG_FDUAL: ShortType = 64
    TYPEFLAG_FNONEXTENSIBLE: ShortType = 128
    TYPEFLAG_FOLEAUTOMATION: ShortType = 256
    TYPEFLAG_FRESTRICTED: ShortType = 512
    TYPEFLAG_FAGGREGATABLE: ShortType = 1024
    TYPEFLAG_FREPLACEABLE: ShortType = 2048
    TYPEFLAG_FDISPATCHABLE: ShortType = 4096
    TYPEFLAG_FREVERSEBIND: ShortType = 8192
    TYPEFLAG_FPROXY: ShortType = 16384


class TYPEKIND(Enum):
    TKIND_ENUM: IntType = 0
    TKIND_RECORD: IntType = 1
    TKIND_MODULE: IntType = 2
    TKIND_INTERFACE: IntType = 3
    TKIND_DISPATCH: IntType = 4
    TKIND_COCLASS: IntType = 5
    TKIND_ALIAS: IntType = 6
    TKIND_UNION: IntType = 7
    TKIND_MAX: IntType = 8


class VARFLAGS(Enum):
    VARFLAG_FREADONLY: ShortType = 1
    VARFLAG_FSOURCE: ShortType = 2
    VARFLAG_FBINDABLE: ShortType = 4
    VARFLAG_FREQUESTEDIT: ShortType = 8
    VARFLAG_FDISPLAYBIND: ShortType = 16
    VARFLAG_FDEFAULTBIND: ShortType = 32
    VARFLAG_FHIDDEN: ShortType = 64
    VARFLAG_FRESTRICTED: ShortType = 128
    VARFLAG_FDEFAULTCOLLELEM: ShortType = 256
    VARFLAG_FUIDEFAULT: ShortType = 512
    VARFLAG_FNONBROWSABLE: ShortType = 1024
    VARFLAG_FREPLACEABLE: ShortType = 2048
    VARFLAG_FIMMEDIATEBIND: ShortType = 4096


class VARKIND(Enum):
    VAR_PERINSTANCE: IntType = 0
    VAR_STATIC: IntType = 1
    VAR_CONST: IntType = 2
    VAR_DISPATCH: IntType = 3


# No Delegates

__all__ = [
    BINDPTR,
    BIND_OPTS,
    CONNECTDATA,
    DISPPARAMS,
    ELEMDESC,
    EXCEPINFO,
    FILETIME,
    FORMATETC,
    FUNCDESC,
    IDLDESC,
    PARAMDESC,
    STATDATA,
    STATSTG,
    STGMEDIUM,
    TYPEATTR,
    TYPEDESC,
    TYPELIBATTR,
    VARDESC,
    IAdviseSink,
    IBindCtx,
    IConnectionPoint,
    IConnectionPointContainer,
    IDataObject,
    IEnumConnectionPoints,
    IEnumConnections,
    IEnumFORMATETC,
    IEnumMoniker,
    IEnumSTATDATA,
    IEnumString,
    IEnumVARIANT,
    IEnumerable,
    IEnumerator,
    IExpando,
    IMoniker,
    IPersistFile,
    IReflect,
    IRunningObjectTable,
    IStream,
    ITypeComp,
    ITypeInfo,
    ITypeInfo2,
    ITypeLib,
    ITypeLib2,
    ADVF,
    CALLCONV,
    DATADIR,
    DESCKIND,
    DVASPECT,
    FUNCFLAGS,
    FUNCKIND,
    IDLFLAG,
    IMPLTYPEFLAGS,
    INVOKEKIND,
    LIBFLAGS,
    PARAMFLAG,
    SYSKIND,
    TYMED,
    TYPEFLAGS,
    TYPEKIND,
    VARFLAGS,
    VARKIND,
]
