__all__ = [
    'XslCompiledTransform',
    'XsltArgumentList',
    'XsltCompileException',
    'XsltContext',
    'XsltException',
    'XsltMessageEncounteredEventArgs',
    'XslTransform',
    'XsltSettings',
    'IXsltContextFunction',
    'IXsltContextVariable',
    'XsltMessageEncounteredEventHandler',
]


# TODO

# ---------- CLASSES ---------- #

class XslCompiledTransform:
    """Transforms XML data using an XSLT style sheet."""


class XsltArgumentList:
    """Contains a variable number of arguments which are either XSLT parameters or extension objects."""


class XsltCompileException:
    """The exception that is thrown by the Load method when an error is found in the XSLT style sheet."""


class XsltContext:
    """Encapsulates the current execution context of the Extensible Stylesheet Language for Transformations (XSLT) processor allowing XML Path Language (XPath) to resolve functions, parameters, and namespaces within XPath expressions."""


class XsltException:
    """The exception that is thrown when an error occurs while processing an XSLT transformation."""


class XsltMessageEncounteredEventArgs:
    """Provides data for the XsltMessageEncountered event."""


class XslTransform:
    """Transforms XML data using an Extensible Stylesheet Language for Transformations (XSLT) style sheet."""


class XsltSettings:
    """Specifies the XSLT features to support during execution of the XSLT style sheet."""


# ---------- INTERFACES ---------- #

class IXsltContextFunction:
    """Provides an interface to a given function defined in the Extensible Stylesheet Language for Transformations (XSLT) style sheet during runtime execution."""


class IXsltContextVariable:
    """Provides an interface to a given variable that is defined in the style sheet during runtime execution."""


# ---------- DELEGATES ---------- #

class XsltMessageEncounteredEventHandler:
    """Represents the method that will handle the XsltMessageEncountered event."""
