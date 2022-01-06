__all__ = [
    'DataContractJsonSerializer',
    'DataContractJsonSerializerSettings',
    'JsonReaderWriterFactory',
    'IXmlJsonReaderInitializer',
    'IXmlJsonWriterInitializer',
]


# TODO

# ---------- CLASSES ---------- #

class DataContractJsonSerializer:
    """Serializes objects to the JavaScript Object Notation (JSON) and deserializes JSON data to objects. This class cannot be inherited."""


class DataContractJsonSerializerSettings:
    """Specifies DataContractJsonSerializer settings."""


class JsonReaderWriterFactory:
    """Produces instances of XmlDictionaryReader that can read data encoded with JavaScript Object Notation (JSON) from a stream or buffer and map it to an XML Infoset and instances of XmlDictionaryWriter that can map an XML Infoset to JSON and write JSON-encoded data to a stream."""


# ---------- INTERFACES ---------- #

class IXmlJsonReaderInitializer:
    """Specifies the interface for initializing a JavaScript Object Notation (JSON) reader when reusing them to read from a particular stream or buffer."""


class IXmlJsonWriterInitializer:
    """Specifies the interface for initializing a JavaScript Object Notation (JSON) writer when reusing them to write to a particular output stream."""
