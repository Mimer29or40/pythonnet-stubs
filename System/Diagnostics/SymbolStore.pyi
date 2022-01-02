__all__ = [
    'SymDocumentType',
    'SymLanguageType',
    'SymLanguageVendor',
    'SymbolToken',
    'ISymbolBinder',
    'ISymbolBinder1',
    'ISymbolDocument',
    'ISymbolDocumentWriter',
    'ISymbolMethod',
    'ISymbolNamespace',
    'ISymbolReader',
    'ISymbolScope',
    'ISymbolVariable',
    'ISymbolWriter',
    'SymAddressKind',
]


# TODO

# ---------- CLASSES ---------- #

class SymDocumentType:
    """Holds the public GUIDs for document types to be used with the symbol store."""


class SymLanguageType:
    """Holds the public GUIDs for language types to be used with the symbol store."""


class SymLanguageVendor:
    """Holds the public GUIDs for language vendors to be used with the symbol store."""


# ---------- STRUCTS ---------- #

class SymbolToken:
    """The SymbolToken structure is an object representation of a token that represents symbolic information."""


# ---------- INTERFACES ---------- #

class ISymbolBinder:
    """Represents a symbol binder for managed code."""


class ISymbolBinder1:
    """Represents a symbol binder for managed code."""


class ISymbolDocument:
    """Represents a document referenced by a symbol store."""


class ISymbolDocumentWriter:
    """Represents a document referenced by a symbol store."""


class ISymbolMethod:
    """Represents a method within a symbol store."""


class ISymbolNamespace:
    """Represents a namespace within a symbol store."""


class ISymbolReader:
    """Represents a symbol reader for managed code."""


class ISymbolScope:
    """Represents a lexical scope within ISymbolMethod, providing access to the start and end offsets of the scope, as well as its child and parent scopes."""


class ISymbolVariable:
    """Represents a variable within a symbol store."""


class ISymbolWriter:
    """Represents a symbol writer for managed code."""


# ---------- ENUMS ---------- #

class SymAddressKind:
    """Specifies address types for local variables, parameters, and fields in the methods DefineLocalVariable(String, FieldAttributes, Byte[], SymAddressKind, Int32, Int32, Int32, Int32, Int32), DefineParameter(String, ParameterAttributes, Int32, SymAddressKind, Int32, Int32, Int32), and DefineField(SymbolToken, String, FieldAttributes, Byte[], SymAddressKind, Int32, Int32, Int32) of the ISymbolWriter interface."""
