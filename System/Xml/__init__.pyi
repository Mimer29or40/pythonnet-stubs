__all__ = [
    'NameTable',
    'UniqueId',
    'XmlAttribute',
    'XmlAttributeCollection',
    'XmlBinaryReaderSession',
    'XmlBinaryWriterSession',
    'XmlCDataSection',
    'XmlCharacterData',
    'XmlComment',
    'XmlConvert',
    'XmlDataDocument',
    'XmlDeclaration',
    'XmlDictionary',
    'XmlDictionaryReader',
    'XmlDictionaryReaderQuotas',
    'XmlDictionaryString',
    'XmlDictionaryWriter',
    'XmlDocument',
    'XmlDocumentFragment',
    'XmlDocumentType',
    'XmlElement',
    'XmlEntity',
    'XmlEntityReference',
    'XmlException',
    'XmlImplementation',
    'XmlLinkedNode',
    'XmlNamedNodeMap',
    'XmlNamespaceManager',
    'XmlNameTable',
    'XmlNode',
    'XmlNodeChangedEventArgs',
    'XmlNodeList',
    'XmlNodeReader',
    'XmlNotation',
    'XmlParserContext',
    'XmlProcessingInstruction',
    'XmlQualifiedName',
    'XmlReader',
    'XmlReaderSettings',
    'XmlResolver',
    'XmlSecureResolver',
    'XmlSignificantWhitespace',
    'XmlText',
    'XmlTextReader',
    'XmlTextWriter',
    'XmlUrlResolver',
    'XmlValidatingReader',
    'XmlWhitespace',
    'XmlWriter',
    'XmlWriterSettings',
    'IApplicationResourceStreamResolver',
    'IFragmentCapableXmlDictionaryWriter',
    'IHasXmlNode',
    'IStreamProvider',
    'IXmlBinaryReaderInitializer',
    'IXmlBinaryWriterInitializer',
    'IXmlDictionary',
    'IXmlLineInfo',
    'IXmlNamespaceResolver',
    'IXmlTextReaderInitializer',
    'IXmlTextWriterInitializer',
    'ConformanceLevel',
    'DtdProcessing',
    'EntityHandling',
    'Formatting',
    'NamespaceHandling',
    'NewLineHandling',
    'ReadState',
    'ValidationType',
    'WhitespaceHandling',
    'WriteState',
    'XmlDateTimeSerializationMode',
    'XmlDictionaryReaderQuotaTypes',
    'XmlNamespaceScope',
    'XmlNodeChangedAction',
    'XmlNodeOrder',
    'XmlNodeType',
    'XmlOutputMethod',
    'XmlSpace',
    'XmlTokenizedType',
    'OnXmlDictionaryReaderClose',
    'XmlNodeChangedEventHandler',
]


# TODO

# ---------- CLASSES ---------- #

class NameTable:
    """Implements a single-threaded XmlNameTable."""


class UniqueId:
    """A unique identifier optimized for Guids."""


class XmlAttribute:
    """Represents an attribute. Valid and default values for the attribute are defined in a document type definition (DTD) or schema."""


class XmlAttributeCollection:
    """Represents a collection of attributes that can be accessed by name or index."""


class XmlBinaryReaderSession:
    """Enables optimized strings to be managed in a dynamic way."""


class XmlBinaryWriterSession:
    """Enables using a dynamic dictionary to compress common strings that appear in a message and maintain state."""


class XmlCDataSection:
    """Represents a CDATA section."""


class XmlCharacterData:
    """Provides text manipulation methods that are used by several classes."""


class XmlComment:
    """Represents the content of an XML comment."""


class XmlConvert:
    """Encodes and decodes XML names, and provides methods for converting between common language runtime types and XML Schema definition language (XSD) types. When converting data types, the values returned are locale-independent."""


class XmlDataDocument:
    """Allows structured data to be stored, retrieved, and manipulated through a relational DataSet."""


class XmlDeclaration:
    """Represents the XML declaration node <?xml version='1.0'...?>."""


class XmlDictionary:
    """Implements a dictionary used to optimize Windows Communication Foundation (WCF)'s XML reader/writer implementations."""


class XmlDictionaryReader:
    """An abstract class that the Windows Communication Foundation (WCF) derives from XmlReader to do serialization and deserialization."""


class XmlDictionaryReaderQuotas:
    """Contains configurable quota values for XmlDictionaryReaders."""


class XmlDictionaryString:
    """Represents an entry stored in a XmlDictionary."""


class XmlDictionaryWriter:
    """Represents an abstract class that Windows Communication Foundation (WCF) derives from XmlWriter to do serialization and deserialization."""


class XmlDocument:
    """Represents an XML document. You can use this class to load, validate, edit, add, and position XML in a document."""


class XmlDocumentFragment:
    """Represents a lightweight object that is useful for tree insert operations."""


class XmlDocumentType:
    """Represents the document type declaration."""


class XmlElement:
    """Represents an element."""


class XmlEntity:
    """Represents an entity declaration, such as <!ENTITY... >."""


class XmlEntityReference:
    """Represents an entity reference node."""


class XmlException:
    """Returns detailed information about the last exception."""


class XmlImplementation:
    """Defines the context for a set of XmlDocument objects."""


class XmlLinkedNode:
    """Gets the node immediately preceding or following this node."""


class XmlNamedNodeMap:
    """Represents a collection of nodes that can be accessed by name or index."""


class XmlNamespaceManager:
    """Resolves, adds, and removes namespaces to a collection and provides scope management for these namespaces."""


class XmlNameTable:
    """Table of atomized string objects."""


class XmlNode:
    """Represents a single node in the XML document."""


class XmlNodeChangedEventArgs:
    """Provides data for the NodeChanged, NodeChanging, NodeInserted, NodeInserting, NodeRemoved and NodeRemoving events."""


class XmlNodeList:
    """Represents an ordered collection of nodes."""


class XmlNodeReader:
    """Represents a reader that provides fast, non-cached forward only access to XML data in an XmlNode."""


class XmlNotation:
    """Represents a notation declaration, such as <!NOTATION... >."""


class XmlParserContext:
    """Provides all the context information required by the XmlReader to parse an XML fragment."""


class XmlProcessingInstruction:
    """Represents a processing instruction, which XML defines to keep processor-specific information in the text of the document."""


class XmlQualifiedName:
    """Represents an XML qualified name."""


class XmlReader:
    """Represents a reader that provides fast, noncached, forward-only access to XML data."""


class XmlReaderSettings:
    """Specifies a set of features to support on the XmlReader object created by the Create method."""


class XmlResolver:
    """Resolves external XML resources named by a Uniform Resource Identifier (URI)."""


class XmlSecureResolver:
    """Helps to secure another implementation of XmlResolver by wrapping the XmlResolver object and restricting the resources that the underlying XmlResolver has access to."""


class XmlSignificantWhitespace:
    """Represents white space between markup in a mixed content node or white space within an xml:space= 'preserve' scope. This is also referred to as significant white space."""


class XmlText:
    """Represents the text content of an element or attribute."""


class XmlTextReader:
    """Represents a reader that provides fast, non-cached, forward-only access to XML data.
    
    Starting with the .NET Framework 2.0, we recommend that you use the XmlReader class instead.
    """


class XmlTextWriter:
    """Represents a writer that provides a fast, non-cached, forward-only way of generating streams or files containing XML data that conforms to the W3C Extensible Markup Language (XML) 1.0 and the Namespaces in XML recommendations.
    
    Starting with the .NET Framework 2.0, we recommend that you use the XmlWriter class instead.
    """


class XmlUrlResolver:
    """Resolves external XML resources named by a Uniform Resource Identifier (URI)."""


class XmlValidatingReader:
    """Represents a reader that provides document type definition (DTD), XML-Data Reduced (XDR) schema, and XML Schema definition language (XSD) validation.
    
    This class is obsolete. Starting with the .NET Framework 2.0, we recommend that you use the XmlReaderSettings class and the Create method to create a validating XML reader.
    """


class XmlWhitespace:
    """Represents white space in element content."""


class XmlWriter:
    """Represents a writer that provides a fast, non-cached, forward-only way to generate streams or files that contain XML data."""


class XmlWriterSettings:
    """Specifies a set of features to support on the XmlWriter object created by the Create method."""


# ---------- INTERFACES ---------- #

class IApplicationResourceStreamResolver:
    """Represents an application resource stream resolver."""


class IFragmentCapableXmlDictionaryWriter:
    """Contains properties and methods that when implemented by a XmlDictionaryWriter, allows processing of XML fragments."""


class IHasXmlNode:
    """Enables a class to return an XmlNode from the current context or position."""


class IStreamProvider:
    """Represents an interface that can be implemented by classes providing streams."""


class IXmlBinaryReaderInitializer:
    """Provides methods for reinitializing a binary reader to read a new document."""


class IXmlBinaryWriterInitializer:
    """Specifies implementation requirements for XML binary writers that derive from this interface."""


class IXmlDictionary:
    """An interface that defines the contract that an Xml dictionary must implement to be used by XmlDictionaryReader and XmlDictionaryWriter implementations."""


class IXmlLineInfo:
    """Provides an interface to enable a class to return line and position information."""


class IXmlNamespaceResolver:
    """Provides read-only access to a set of prefix and namespace mappings."""


class IXmlTextReaderInitializer:
    """Specifies implementation requirements for XML text readers that derive from this interface."""


class IXmlTextWriterInitializer:
    """Specifies implementation requirements for XML text writers that derive from this interface."""


# ---------- ENUMS ---------- #

class ConformanceLevel:
    """Specifies the amount of input or output checking that XmlReader and XmlWriter objects perform."""


class DtdProcessing:
    """Specifies the options for processing DTDs. The DtdProcessing enumeration is used by the XmlReaderSettings class."""


class EntityHandling:
    """Specifies how the XmlTextReader or XmlValidatingReader handle entities."""


class Formatting:
    """Specifies formatting options for the XmlTextWriter."""


class NamespaceHandling:
    """Specifies whether to remove duplicate namespace declarations in the XmlWriter."""


class NewLineHandling:
    """Specifies how to handle line breaks."""


class ReadState:
    """Specifies the state of the reader."""


class ValidationType:
    """Specifies the type of validation to perform."""


class WhitespaceHandling:
    """Specifies how white space is handled."""


class WriteState:
    """Specifies the state of the XmlWriter."""


class XmlDateTimeSerializationMode:
    """Specifies how to treat the time value when converting between string and DateTime."""


class XmlDictionaryReaderQuotaTypes:
    """Enumerates the configurable quota values for XmlDictionaryReaders."""


class XmlNamespaceScope:
    """Defines the namespace scope."""


class XmlNodeChangedAction:
    """Specifies the type of node change."""


class XmlNodeOrder:
    """Describes the document order of a node compared to a second node."""


class XmlNodeType:
    """Specifies the type of node."""


class XmlOutputMethod:
    """Specifies the method used to serialize the XmlWriter output."""


class XmlSpace:
    """Specifies the current xml:space scope."""


class XmlTokenizedType:
    """Represents the XML type for the string. This allows the string to be read as a particular XML type, for example a CDATA section type."""


# ---------- DELEGATES ---------- #

class OnXmlDictionaryReaderClose:
    """delegate for a callback method when closing the reader."""


class XmlNodeChangedEventHandler:
    """Represents the method that handles NodeChanged, NodeChanging, NodeInserted, NodeInserting, NodeRemoved and NodeRemoving events."""
