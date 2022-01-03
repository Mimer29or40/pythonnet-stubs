__all__ = [
    'JsonCollectionInfoValues',
    'JsonMetadataServices',
    'JsonObjectInfoValues',
    'JsonParameterInfoValues',
    'JsonPropertyInfo',
    'JsonPropertyInfoValues',
    'JsonTypeInfo',
    'JsonTypeInfo',
]

from typing import TypeVar, Generic

T = TypeVar('T')
TCollection = TypeVar('TCollection')


# TODO

# ---------- CLASSES ---------- #

class JsonCollectionInfoValues(Generic[TCollection]):
    """Provides serialization metadata about a collection type."""


class JsonMetadataServices:
    """Provides helpers to create and initialize metadata for JSON-serializable types."""


class JsonObjectInfoValues(Generic[T]):
    """Provides serialization metadata about an object type with constructors, properties, and fields."""


class JsonParameterInfoValues:
    """Provides information about a constructor parameter required for JSON deserialization."""


class JsonPropertyInfo:
    """Provides JSON serialization-related metadata about a property or field."""


class JsonPropertyInfoValues(Generic[T]):
    """Provides serialization metadata about a property or field."""


class JsonTypeInfo:
    """Provides JSON serialization-related metadata about a type."""


class JsonTypeInfo(Generic[T]):
    """Provides JSON serialization-related metadata about a type."""
