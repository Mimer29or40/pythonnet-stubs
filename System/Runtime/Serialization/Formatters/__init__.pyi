__all__ = [
    'IFieldInfo',
    'FormatterAssemblyStyle',
    'FormatterTypeStyle',
    'TypeFilterLevel',
]


# TODO

# ---------- INTERFACES ---------- #

class IFieldInfo:
    """Allows access to field names and field types of objects that support the ISerializable interface."""


# ---------- ENUMS ---------- #

class FormatterAssemblyStyle:
    """Indicates the method that will be used during deserialization for locating and loading assemblies."""


class FormatterTypeStyle:
    """Indicates the format in which type descriptions are laid out in the serialized stream."""


class TypeFilterLevel:
    """Specifies the level of automatic deserialization for .NET Framework remoting."""
