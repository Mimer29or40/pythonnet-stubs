__all__ = [
    'Extensions',
    'XAttribute',
    'XCData',
    'XComment',
    'XContainer',
    'XDeclaration',
    'XDocument',
    'XDocumentType',
    'XElement',
    'XName',
    'XNamespace',
    'XNode',
    'XNodeDocumentOrderComparer',
    'XNodeEqualityComparer',
    'XObject',
    'XObjectChangeEventArgs',
    'XProcessingInstruction',
    'XStreamingElement',
    'XText',
    'LoadOptions',
    'ReaderOptions',
    'SaveOptions',
    'XObjectChange',
]


# TODO

# ---------- CLASSES ---------- #

class Extensions:
    """Contains the LINQ to XML extension methods."""


class XAttribute:
    """Represents an XML attribute."""


class XCData:
    """Represents a text node that contains CDATA."""


class XComment:
    """Represents an XML comment."""


class XContainer:
    """Represents a node that can contain other nodes."""


class XDeclaration:
    """Represents an XML declaration."""


class XDocument:
    """Represents an XML document. For the components and usage of an XDocument object, see XDocument Class Overview."""


class XDocumentType:
    """Represents an XML Document Type Definition (DTD)."""


class XElement:
    """Represents an XML element. See XElement Class Overview and the Remarks section on this page for usage information and examples."""


class XName:
    """Represents a name of an XML element or attribute."""


class XNamespace:
    """Represents an XML namespace. This class cannot be inherited."""


class XNode:
    """Represents the abstract concept of a node (element, comment, document type, processing instruction, or text node) in the XML tree."""


class XNodeDocumentOrderComparer:
    """Contains functionality to compare nodes for their document order. This class cannot be inherited."""


class XNodeEqualityComparer:
    """Compares nodes to determine whether they are equal. This class cannot be inherited."""


class XObject:
    """Represents a node or an attribute in an XML tree."""


class XObjectChangeEventArgs:
    """Provides data for the Changing and Changed events."""


class XProcessingInstruction:
    """Represents an XML processing instruction."""


class XStreamingElement:
    """Represents elements in an XML tree that supports deferred streaming output."""


class XText:
    """Represents a text node."""


# ---------- ENUMS ---------- #

class LoadOptions:
    """Specifies load options when parsing XML."""


class ReaderOptions:
    """Specifies whether to omit duplicate namespaces when loading an XDocument with an XmlReader."""


class SaveOptions:
    """Specifies serialization options."""


class XObjectChange:
    """Specifies the event type when an event is raised for an XObject."""
