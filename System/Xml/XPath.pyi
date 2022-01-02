__all__ = [
    'Extensions',
    'XDocumentExtensions',
    'XPathDocument',
    'XPathException',
    'XPathExpression',
    'XPathItem',
    'XPathNavigator',
    'XPathNodeIterator',
    'IXPathNavigable',
    'XmlCaseOrder',
    'XmlDataType',
    'XmlSortOrder',
    'XPathNamespaceScope',
    'XPathNodeType',
    'XPathResultType',
]


# TODO

# ---------- CLASSES ---------- #

class Extensions:
    """This class contains the LINQ to XML extension methods that enable you to evaluate XPath expressions."""


class XDocumentExtensions:
    """Extends the XDocument class by providing a method for navigating and editing an XML node."""


class XPathDocument:
    """Provides a fast, read-only, in-memory representation of an XML document by using the XPath data model."""


class XPathException:
    """Provides the exception thrown when an error occurs while processing an XPath expression."""


class XPathExpression:
    """Provides a typed class that represents a compiled XPath expression."""


class XPathItem:
    """Represents an item in the XQuery 1.0 and XPath 2.0 Data Model."""


class XPathNavigator:
    """Provides a cursor model for navigating and editing XML data."""


class XPathNodeIterator:
    """Provides an iterator over a selected set of nodes."""


# ---------- INTERFACES ---------- #

class IXPathNavigable:
    """Provides an accessor to the XPathNavigator class."""


# ---------- ENUMS ---------- #

class XmlCaseOrder:
    """Specifies the sort order for uppercase and lowercase letters."""


class XmlDataType:
    """Specifies the data type used to determine sort order."""


class XmlSortOrder:
    """Specifies the sort order."""


class XPathNamespaceScope:
    """Defines the namespace scope."""


class XPathNodeType:
    """Defines the XPath node types that can be returned from the XPathNavigator class."""


class XPathResultType:
    """Specifies the return type of the XPath expression."""
