__all__ = [
    'JsonAttribute',
    'JsonConstructorAttribute',
    'JsonConverter',
    'JsonConverter',
    'JsonConverterAttribute',
    'JsonConverterFactory',
    'JsonExtensionDataAttribute',
    'JsonIgnoreAttribute',
    'JsonIncludeAttribute',
    'JsonNumberHandlingAttribute',
    'JsonPropertyNameAttribute',
    'JsonPropertyOrderAttribute',
    'JsonSerializableAttribute',
    'JsonSerializerContext',
    'JsonSourceGenerationOptionsAttribute',
    'JsonStringEnumConverter',
    'ReferenceHandler',
    'ReferenceHandler',
    'ReferenceResolver',
    'IJsonOnDeserialized',
    'IJsonOnDeserializing',
    'IJsonOnSerialized',
    'IJsonOnSerializing',
    'JsonIgnoreCondition',
    'JsonKnownNamingPolicy',
    'JsonNumberHandling',
    'JsonSourceGenerationMode',
    'JsonUnknownTypeHandling',
]

from typing import TypeVar, Generic

T = TypeVar('T')


# TODO

# ---------- CLASSES ---------- #

class JsonAttribute:
    """Provides the base class for serialization attributes."""


class JsonConstructorAttribute:
    """When placed on a constructor, indicates that the constructor should be used to create instances of the type on deserialization."""


class JsonConverter:
    """Converts an object or value to or from JSON."""


class JsonConverter(Generic[T]):
    """Converts an object or value to or from JSON."""


class JsonConverterAttribute:
    """When placed on a property or type, specifies the converter type to use."""


class JsonConverterFactory:
    """Supports converting several types by using a factory pattern."""


class JsonExtensionDataAttribute:
    """When placed on a property of type IDictionary<TKey,TValue>, any properties that do not have a matching member are added to that dictionary during deserialization and written during serialization."""


class JsonIgnoreAttribute:
    """Prevents a property from being serialized or deserialized."""


class JsonIncludeAttribute:
    """Indicates that the member should be included for serialization and deserialization."""


class JsonNumberHandlingAttribute:
    """When placed on a type, property, or field, indicates what JsonNumberHandling settings should be used when serializing or deserializing numbers."""


class JsonPropertyNameAttribute:
    """Specifies the property name that is present in the JSON when serializing and deserializing. This overrides any naming policy specified by JsonNamingPolicy."""


class JsonPropertyOrderAttribute:
    """Specifies the property order that is present in the JSON when serializing. Lower values are serialized first. If the attribute is not specified, the default value is 0."""


class JsonSerializableAttribute:
    """Instructs the System.Text.Json source generator to generate source code to help optimize performance when serializing and deserializing instances of the specified type and types in its object graph."""


class JsonSerializerContext:
    """Provides metadata about a set of types that is relevant to JSON serialization."""


class JsonSourceGenerationOptionsAttribute:
    """Instructs the System.Text.Json source generator to assume the specified options will be used at run time via JsonSerializerOptions."""


class JsonStringEnumConverter:
    """Converts enumeration values to and from strings."""


class ReferenceHandler:
    """Defines how the JsonSerializer deals with references on serialization and deserialization."""


class ReferenceHandler(Generic[T]):
    """Defines how the JsonSerializer deals with references on serialization and deserialization."""


class ReferenceResolver:
    """Defines how the JsonSerializer deals with references on serialization and deserialization. Defines the core behavior of preserving references on serialization and deserialization."""


# ---------- INTERFACES ---------- #

class IJsonOnDeserialized:
    """Specifies that the JSON type should have its OnDeserialized() method called after deserialization occurs."""


class IJsonOnDeserializing:
    """Specifies that the type should have its OnDeserializing() method called before deserialization occurs."""


class IJsonOnSerialized:
    """Specifies that the type should have its OnSerialized() method called after serialization occurs."""


class IJsonOnSerializing:
    """Specifies that the type should have its OnSerializing() method called before serialization occurs."""


# ---------- ENUMS ---------- #

class JsonIgnoreCondition:
    """Controls how the JsonIgnoreAttribute ignores properties on serialization and deserialization."""


class JsonKnownNamingPolicy:
    """The JsonNamingPolicy to be used at run time."""


class JsonNumberHandling:
    """Determines how JsonSerializer handles numbers when serializing and deserializing."""


class JsonSourceGenerationMode:
    """The generation mode for the System.Text.Json source generator."""


class JsonUnknownTypeHandling:
    """Defines how deserializing a type declared as an Object is handled during deserialization."""
