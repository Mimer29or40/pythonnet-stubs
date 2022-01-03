__all__ = [
    'BIND_OPTS',
    'BINDPTR',
    'CONNECTDATA',
    'DISPPARAMS',
    'ELEMDESC',
    'ELEMDESC',
    'EXCEPINFO',
    'FILETIME',
    'FORMATETC',
    'FUNCDESC',
    'IDLDESC',
    'PARAMDESC',
    'STATDATA',
    'STATSTG',
    'STGMEDIUM',
    'TYPEATTR',
    'TYPEDESC',
    'TYPELIBATTR',
    'VARDESC',
    'VARDESC',
    'IAdviseSink',
    'IBindCtx',
    'IConnectionPoint',
    'IConnectionPointContainer',
    'IDataObject',
    'IEnumConnectionPoints',
    'IEnumConnections',
    'IEnumFORMATETC',
    'IEnumMoniker',
    'IEnumSTATDATA',
    'IEnumString',
    'IEnumVARIANT',
    'IMoniker',
    'IPersistFile',
    'IRunningObjectTable',
    'IStream',
    'ITypeComp',
    'ITypeInfo',
    'ITypeInfo2',
    'ITypeLib',
    'ITypeLib2',
    'ADVF',
    'CALLCONV',
    'DATADIR',
    'DESCKIND',
    'DVASPECT',
    'FUNCFLAGS',
    'FUNCKIND',
    'IDLFLAG',
    'IMPLTYPEFLAGS',
    'INVOKEKIND',
    'LIBFLAGS',
    'PARAMFLAG',
    'SYSKIND',
    'TYMED',
    'TYPEFLAGS',
    'TYPEKIND',
    'VARFLAGS',
    'VARKIND',
]


# TODO

# ---------- STRUCTS ---------- #

class BIND_OPTS:
    """Stores the parameters that are used during a moniker binding operation."""


class BINDPTR:
    """Contains a pointer to a bound-to FUNCDESC structure, VARDESC structure, or an ITypeComp interface."""


class CONNECTDATA:
    """Describes a connection that exists to a given connection point."""


class DISPPARAMS:
    """Contains the arguments passed to a method or property by IDispatch::Invoke."""


class ELEMDESC:
    """Contains the type description and process transfer information for a variable, function, or a function parameter."""
    
    class DESCUNION:
        """Contains information about an element."""


class EXCEPINFO:
    """Describes the exceptions that occur during IDispatch::Invoke."""


class FILETIME:
    """Represents the number of 100-nanosecond intervals since January 1, 1601. This structure is a 64-bit value."""


class FORMATETC:
    """Represents a generalized Clipboard format."""


class FUNCDESC:
    """Defines a function description."""


class IDLDESC:
    """Contains information needed for transferring a structure element, parameter, or function return value between processes."""


class PARAMDESC:
    """Contains information about how to transfer a structure element, parameter, or function return value between processes."""


class STATDATA:
    """Provides the managed definition of the STATDATA structure."""


class STATSTG:
    """Contains statistical information about an open storage, stream, or byte-array object."""


class STGMEDIUM:
    """Provides the managed definition of the STGMEDIUM structure."""


class TYPEATTR:
    """Contains attributes of a UCOMITypeInfo."""


class TYPEDESC:
    """Describes the type of a variable, return type of a function, or the type of a function parameter."""


class TYPELIBATTR:
    """Identifies a particular type library and provides localization support for member names."""


class VARDESC:
    """Describes a variable, constant, or data member."""
    
    class DESCUNION:
        """Contains information about a variable."""


# ---------- INTERFACES ---------- #

class IAdviseSink:
    """Provides a managed definition of the IAdviseSink interface."""


class IBindCtx:
    """Provides the managed definition of the IBindCtx interface."""


class IConnectionPoint:
    """Provides the managed definition of the IConnectionPoint interface."""


class IConnectionPointContainer:
    """Provides the managed definition of the IConnectionPointContainer interface."""


class IDataObject:
    """Provides the managed definition of the IDataObject interface."""


class IEnumConnectionPoints:
    """Manages the definition of the IEnumConnectionPoints interface."""


class IEnumConnections:
    """Manages the definition of the IEnumConnections interface."""


class IEnumFORMATETC:
    """Provides the managed definition of the IEnumFORMATETC interface."""


class IEnumMoniker:
    """Manages the definition of the IEnumMoniker interface."""


class IEnumSTATDATA:
    """Provides the managed definition of the IEnumSTATDATA interface."""


class IEnumString:
    """Manages the definition of the IEnumString interface."""


class IEnumVARIANT:
    """Manages the definition of the IEnumVARIANT interface."""


class IMoniker:
    """Provides the managed definition of the IMoniker interface, with COM functionality from IPersist and IPersistStream."""


class IPersistFile:
    """Provides the managed definition of the IPersistFile interface, with functionality from IPersist."""


class IRunningObjectTable:
    """Provides the managed definition of the IRunningObjectTable interface."""


class IStream:
    """Provides the managed definition of the IStream interface, with ISequentialStream functionality."""


class ITypeComp:
    """Provides the managed definition of the ITypeComp interface."""


class ITypeInfo:
    """Provides the managed definition of the Component Automation ITypeInfo interface."""


class ITypeInfo2:
    """Provides the managed definition of the ITypeInfo2 interface."""


class ITypeLib:
    """Provides the managed definition of the ITypeLib interface."""


class ITypeLib2:
    """Provides a managed definition of the ITypeLib2 interface."""


# ---------- ENUMS ---------- #

class ADVF:
    """Specifies the requested behavior when setting up an advise sink or a caching connection with an object."""


class CALLCONV:
    """Identifies the calling convention used by a method described in a METHODDATA structure."""


class DATADIR:
    """Specifies the direction of the data flow in the dwDirection parameter of the EnumFormatEtc(DATADIR) method. This determines the formats that the resulting enumerator can enumerate."""


class DESCKIND:
    """Identifies the type description being bound to."""


class DVASPECT:
    """Specifies the desired data or view aspect of the object when drawing or getting data."""


class FUNCFLAGS:
    """Identifies the constants that define the properties of a function."""


class FUNCKIND:
    """Defines how to access a function."""


class IDLFLAG:
    """Describes how to transfer a structure element, parameter, or function return value between processes."""


class IMPLTYPEFLAGS:
    """Defines the attributes of an implemented or inherited interface of a type."""


class INVOKEKIND:
    """Specifies how to invoke a function by IDispatch::Invoke."""


class LIBFLAGS:
    """Defines flags that apply to type libraries."""


class PARAMFLAG:
    """Describes how to transfer a structure element, parameter, or function return value between processes."""


class SYSKIND:
    """Identifies the target operating system platform."""


class TYMED:
    """Provides the managed definition of the TYMED structure."""


class TYPEFLAGS:
    """Defines the properties and attributes of a type description."""


class TYPEKIND:
    """Specifies various types of data and functions."""


class VARFLAGS:
    """Identifies the constants that define the properties of a variable."""


class VARKIND:
    """Defines the kind of variable."""
