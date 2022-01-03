__all__ = [
    'CollectionDataContractAttribute',
    'ContractNamespaceAttribute',
    'DataContractAttribute',
    'DataContractResolver',
    'DataContractSerializer',
    'DataContractSerializerExtensions',
    'DataContractSerializerSettings',
    'DataMemberAttribute',
    'DateTimeFormat',
    'EnumMemberAttribute',
    'ExportOptions',
    'ExtensionDataObject',
    'Formatter',
    'FormatterConverter',
    'FormatterServices',
    'IgnoreDataMemberAttribute',
    'InvalidDataContractException',
    'KnownTypeAttribute',
    'ObjectIDGenerator',
    'ObjectManager',
    'OnDeserializedAttribute',
    'OnDeserializingAttribute',
    'OnSerializedAttribute',
    'OnSerializingAttribute',
    'OptionalFieldAttribute',
    'SafeSerializationEventArgs',
    'SerializationBinder',
    'SerializationException',
    'SerializationInfo',
    'SerializationInfoEnumerator',
    'SerializationObjectManager',
    'SurrogateSelector',
    'XmlObjectSerializer',
    'XmlSerializableServices',
    'XPathQueryGenerator',
    'XsdDataContractExporter',
    'SerializationEntry',
    'StreamingContext',
    'IDeserializationCallback',
    'IExtensibleDataObject',
    'IFormatter',
    'IFormatterConverter',
    'IObjectReference',
    'ISafeSerializationData',
    'ISerializable',
    'ISerializationSurrogate',
    'ISerializationSurrogateProvider',
    'ISurrogateSelector',
    'EmitTypeInformation',
    'StreamingContextStates',
]

# TODO

# class StreamingContext(ValueType):
#     """Describes the source and destination of a given serialized stream,
#     and provides an additional caller-defined context.
#     """
#
#     @overload
#     def __init__(self, state: StreamingContextStates):
#         """Initializes a new instance of the StreamingContext class with a given context state."""
#
#     @overload
#     def __init__(self, state: StreamingContextStates, *additional: Object):
#         """Initializes a new instance of the StreamingContext class with a given context state, and some additional information."""
#
#     def __init__(self, *args, **kwargs): ...
#
#     # Properties
#     # PROPERTIES
#     # Context
#     # Gets context specified as part of the additional context.
#
#     # State
#     # Gets the source or destination of the transmitted data.
#
#     # Methods
#     # METHODS
#     # Equals(Object)
#     # Determines whether two StreamingContext instances contain the same values.
#
#     # GetHashCode()
#     # Returns a hash code of this object.
#
#
# class ISerializable(ABC):
#     """Allows an object to control its own serialization and deserialization."""
#
#     def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
#         """Populates a SerializationInfo with the data needed to serialize the target object."""

# ---------- CLASSES ---------- #
from System import ObjectType, NullableType, VoidType


class CollectionDataContractAttribute:
    """When applied to a collection type, enables custom specification of the collection item elements. This attribute can be applied only to types that are recognized by the DataContractSerializer as valid, serializable collections."""


class ContractNamespaceAttribute:
    """Specifies the CLR namespace and XML namespace of the data contract."""


class DataContractAttribute:
    """Specifies that the type defines or implements a data contract and is serializable by a serializer, such as the DataContractSerializer. To make their type serializable, type authors must define a data contract for their type."""


class DataContractResolver:
    """Provides a mechanism for dynamically mapping types to and from xsi:type representations during serialization and deserialization."""


class DataContractSerializer:
    """Serializes and deserializes an instance of a type into an XML stream or document using a supplied data contract. This class cannot be inherited."""


class DataContractSerializerExtensions:
    """Extends the DataContractSerializer class by providing methods for setting and getting an ISerializationSurrogateProvider."""


class DataContractSerializerSettings:
    """Specifies data contract serializer settings."""


class DataMemberAttribute:
    """When applied to the member of a type, specifies that the member is part of a data contract and is serializable by the DataContractSerializer."""


class DateTimeFormat:
    """Specifies date-time format options."""


class EnumMemberAttribute:
    """Specifies that the field is an enumeration member and should be serialized."""


class ExportOptions:
    """Represents the options that can be set for an XsdDataContractExporter."""


class ExtensionDataObject:
    """Stores data from a versioned data contract that has been extended by adding new members."""


class Formatter:
    """Provides base functionality for the common language runtime serialization formatters."""


class FormatterConverter:
    """Represents a base implementation of the IFormatterConverter interface that uses the Convert class and the IConvertible interface."""


class FormatterServices:
    """Provides static methods to aid with the implementation of a Formatter for serialization. This class cannot be inherited."""


class IgnoreDataMemberAttribute:
    """When applied to the member of a type, specifies that the member is not part of a data contract and is not serialized."""


class InvalidDataContractException:
    """The exception that is thrown when the DataContractSerializer or NetDataContractSerializer encounters an invalid data contract during serialization and deserialization."""


class KnownTypeAttribute:
    """Specifies types that should be recognized by the DataContractSerializer when serializing or deserializing a given type."""


class ObjectIDGenerator:
    """Generates IDs for objects."""


class ObjectManager:
    """Keeps track of objects as they are deserialized."""


class OnDeserializedAttribute:
    """When applied to a method, specifies that the method is called immediately after deserialization of an object in an object graph. The order of deserialization relative to other objects in the graph is non-deterministic."""


class OnDeserializingAttribute:
    """When applied to a method, specifies that the method is called during deserialization of an object in an object graph. The order of deserialization relative to other objects in the graph is non-deterministic."""


class OnSerializedAttribute:
    """When applied to a method, specifies that the method is called after serialization of an object in an object graph. The order of serialization relative to other objects in the graph is non-deterministic."""


class OnSerializingAttribute:
    """When applied to a method, specifies that the method is called during serialization of an object in an object graph. The order of serialization relative to other objects in the graph is non-deterministic."""


class OptionalFieldAttribute:
    """Specifies that a field can be missing from a serialization stream so that the BinaryFormatter and the SoapFormatter does not throw an exception."""


class SafeSerializationEventArgs:
    """Provides data for the SerializeObjectState event."""


class SerializationBinder:
    """Allows users to control class loading and mandate what class to load."""


class SerializationException:
    """The exception thrown when an error occurs during serialization or deserialization."""


class SerializationInfo:
    """Stores all the data needed to serialize or deserialize an object. This class cannot be inherited."""


class SerializationInfoEnumerator:
    """Provides a formatter-friendly mechanism for parsing the data in SerializationInfo. This class cannot be inherited."""


class SerializationObjectManager:
    """Manages serialization processes at run time. This class cannot be inherited."""


class SurrogateSelector:
    """Assists formatters in selection of the serialization surrogate to delegate the serialization or deserialization process to."""


class XmlObjectSerializer:
    """Provides the base class used to serialize objects as XML streams or documents. This class is abstract."""


class XmlSerializableServices:
    """Contains methods for reading and writing XML."""


class XPathQueryGenerator:
    """When given a class representing a data contract, and metadata representing a member of the contract, produces an XPath query for the member."""


class XsdDataContractExporter:
    """Allows the transformation of a set of .NET types that are used in data contracts into an XML schema file (.xsd)."""


# ---------- STRUCTS ---------- #

class SerializationEntry:
    """Holds the value, Type, and name of a serialized object."""


class StreamingContext:
    """Describes the source and destination of a given serialized stream, and provides an additional caller-defined context."""


# ---------- INTERFACES ---------- #

class IDeserializationCallback:
    """Indicates that a class is to be notified when deserialization of the
    entire object graph has been completed. Note that this interface is not
    called when deserializing with the XmlSerializer
    (System.Xml.Serialization.XmlSerializer)."""
    
    def OnDeserialization(self, sender: NullableType[ObjectType]) -> VoidType:
        """Runs when the entire object graph has been deserialized."""


class IExtensibleDataObject:
    """Provides a data structure to store extra data encountered by the XmlObjectSerializer during deserialization of a type marked with the DataContractAttribute attribute."""


class IFormatter:
    """Provides functionality for formatting serialized objects."""


class IFormatterConverter:
    """Provides the connection between an instance of SerializationInfo and the formatter-provided class best suited to parse the data inside the SerializationInfo."""


class IObjectReference:
    """Indicates that the current interface implementer is a reference to another object."""


class ISafeSerializationData:
    """Enables serialization of custom exception data in security-transparent code."""


class ISerializable:
    """Allows an object to control its own serialization and deserialization."""
    
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType:
        """Populates a SerializationInfo with the data needed to serialize the
        target object."""


class ISerializationSurrogate:
    """Implements a serialization surrogate selector that allows one object to perform serialization and deserialization of another."""


class ISerializationSurrogateProvider:
    """Provides the methods needed to construct a serialization surrogate that extends the DataContractSerializer. A serialization surrogate is used during serialization and deserialization to substitute one type for another."""


class ISurrogateSelector:
    """Indicates a serialization surrogate selector class."""


# ---------- ENUMS ---------- #

class EmitTypeInformation:
    """Specifies how often to emit type information."""


class StreamingContextStates:
    """Defines a set of flags that specifies the source or destination context for the stream during serialization."""
