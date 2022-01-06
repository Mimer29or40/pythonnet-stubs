__all__ = [
    'JsonDocument',
    'JsonException',
    'JsonNamingPolicy',
    'JsonSerializer',
    'JsonSerializerOptions',
    'Utf8JsonWriter',
    'JsonDocumentOptions',
    'JsonElement',
    'JsonEncodedText',
    'JsonProperty',
    'JsonReaderOptions',
    'JsonReaderState',
    'JsonWriterOptions',
    'Utf8JsonReader',
    'JsonCommentHandling',
    'JsonSerializerDefaults',
    'JsonTokenType',
    'JsonValueKind',
]


# TODO

# ---------- CLASSES ---------- #

class JsonDocument:
    """Provides a mechanism for examining the structural content of a JSON value without automatically instantiating data values."""


class JsonException:
    """Defines a custom exception object that is thrown when invalid JSON text is encountered, the defined maximum depth is passed, or the JSON text is not compatible with the type of a property on an object."""


class JsonNamingPolicy:
    """Determines the naming policy used to convert a string-based name to another format, such as a camel-casing format."""


class JsonSerializer:
    """Provides functionality to serialize objects or value types to JSON and to deserialize JSON into objects or value types."""


class JsonSerializerOptions:
    """Provides options to be used with JsonSerializer."""


class Utf8JsonWriter:
    """Provides a high-performance API for forward-only, non-cached writing of UTF-8 encoded JSON text."""


# ---------- STRUCTS ---------- #

class JsonDocumentOptions:
    """Provides the ability for the user to define custom behavior when parsing JSON to create a JsonDocument."""


class JsonElement:
    """Represents a specific JSON value within a JsonDocument."""
    
    class ArrayEnumerator:
        """Represents an enumerator for the contents of a JSON array."""
    
    class ObjectEnumerator:
        """Represents an enumerator for the properties of a JSON object."""


class JsonEncodedText:
    """Provides methods to transform UTF-8 or UTF-16 encoded text into a form that is suitable for JSON."""


class JsonProperty:
    """Represents a single property for a JSON object."""


class JsonReaderOptions:
    """Provides the ability for the user to define custom behavior when reading JSON."""


class JsonReaderState:
    """Defines an opaque type that holds and saves all the relevant state information, which must be provided to the Utf8JsonReader to continue reading after processing incomplete data."""


class JsonWriterOptions:
    """Allows the user to define custom behavior when writing JSON using the Utf8JsonWriter."""


class Utf8JsonReader:
    """Provides a high-performance API for forward-only, read-only access to UTF-8 encoded JSON text."""


# ---------- ENUMS ---------- #

class JsonCommentHandling:
    """Defines how the Utf8JsonReader struct handles comments."""


class JsonSerializerDefaults:
    """Specifies scenario-based default serialization options that can be used to construct a JsonSerializerOptions instance."""


class JsonTokenType:
    """Defines the various JSON tokens that make up a JSON text."""


class JsonValueKind:
    """Specifies the data type of a JSON value."""
