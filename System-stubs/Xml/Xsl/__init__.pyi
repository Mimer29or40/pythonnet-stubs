from __future__ import annotations

from abc import ABC
from typing import Callable, Generic, List, Protocol, TypeVar, Union, overload

from System import Array, AsyncCallback, Boolean, Byte, EventArgs, Exception, IAsyncResult, ICloneable, Int32, IntPtr, MulticastDelegate, Object, String, SystemException, Type, Void
from System.CodeDom.Compiler import CompilerErrorCollection, TempFileCollection
from System.Collections import IEnumerable
from System.IO import Stream, TextWriter
from System.Reflection import MethodInfo
from System.Reflection.Emit import TypeBuilder
from System.Runtime.InteropServices import _Exception
from System.Runtime.Serialization import ISerializable, SerializationInfo, StreamingContext
from System.Security.Policy import Evidence
from System.Xml import IXmlNamespaceResolver, XmlNamespaceManager, XmlReader, XmlResolver, XmlWriter, XmlWriterSettings
from System.Xml.XPath import IXPathNavigable, XPathNavigator, XPathResultType

# ---------- Types ---------- #

T = TypeVar('T')

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
ByteType = Union[int, Byte]
IntType = Union[int, Int32]
NIntType = Union[int, IntPtr]
ObjectType = Object
StringType = Union[str, String]
TypeType = Union[type, Type]
VoidType = Union[None, Void]


class EventType(Generic[T]):
    def __iadd__(self, other: T): ...
    
    def __isub__(self, other: T): ...


# ---------- Classes ---------- #

class XslCompiledTransform(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, enableDebug: BooleanType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def OutputSettings(self) -> XmlWriterSettings: ...
    
    @property
    def TemporaryFiles(self) -> TempFileCollection: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def CompileToType(stylesheet: XmlReader, settings: XsltSettings, stylesheetResolver: XmlResolver, debug: BooleanType, typeBuilder: TypeBuilder, scriptAssemblyPath: StringType) -> CompilerErrorCollection: ...
    
    @overload
    def Load(self, stylesheet: XmlReader, settings: XsltSettings, stylesheetResolver: XmlResolver) -> VoidType: ...
    
    @overload
    def Load(self, stylesheet: IXPathNavigable, settings: XsltSettings, stylesheetResolver: XmlResolver) -> VoidType: ...
    
    @overload
    def Load(self, stylesheetUri: StringType, settings: XsltSettings, stylesheetResolver: XmlResolver) -> VoidType: ...
    
    @overload
    def Load(self, stylesheet: XmlReader) -> VoidType: ...
    
    @overload
    def Load(self, stylesheet: IXPathNavigable) -> VoidType: ...
    
    @overload
    def Load(self, stylesheetUri: StringType) -> VoidType: ...
    
    @overload
    def Load(self, compiledStylesheet: TypeType) -> VoidType: ...
    
    @overload
    def Load(self, executeMethod: MethodInfo, queryData: ArrayType[ByteType], earlyBoundTypes: ArrayType[TypeType]) -> VoidType: ...
    
    @overload
    def Transform(self, input: IXPathNavigable, results: XmlWriter) -> VoidType: ...
    
    @overload
    def Transform(self, input: IXPathNavigable, arguments: XsltArgumentList, results: XmlWriter) -> VoidType: ...
    
    @overload
    def Transform(self, input: IXPathNavigable, arguments: XsltArgumentList, results: TextWriter) -> VoidType: ...
    
    @overload
    def Transform(self, input: IXPathNavigable, arguments: XsltArgumentList, results: Stream) -> VoidType: ...
    
    @overload
    def Transform(self, input: XmlReader, results: XmlWriter) -> VoidType: ...
    
    @overload
    def Transform(self, input: XmlReader, arguments: XsltArgumentList, results: XmlWriter) -> VoidType: ...
    
    @overload
    def Transform(self, input: XmlReader, arguments: XsltArgumentList, results: TextWriter) -> VoidType: ...
    
    @overload
    def Transform(self, input: XmlReader, arguments: XsltArgumentList, results: Stream) -> VoidType: ...
    
    @overload
    def Transform(self, inputUri: StringType, results: XmlWriter) -> VoidType: ...
    
    @overload
    def Transform(self, inputUri: StringType, arguments: XsltArgumentList, results: XmlWriter) -> VoidType: ...
    
    @overload
    def Transform(self, inputUri: StringType, arguments: XsltArgumentList, results: TextWriter) -> VoidType: ...
    
    @overload
    def Transform(self, inputUri: StringType, arguments: XsltArgumentList, results: Stream) -> VoidType: ...
    
    @overload
    def Transform(self, inputUri: StringType, resultsFile: StringType) -> VoidType: ...
    
    @overload
    def Transform(self, input: XmlReader, arguments: XsltArgumentList, results: XmlWriter, documentResolver: XmlResolver) -> VoidType: ...
    
    @overload
    def Transform(self, input: IXPathNavigable, arguments: XsltArgumentList, results: XmlWriter, documentResolver: XmlResolver) -> VoidType: ...
    
    def get_OutputSettings(self) -> XmlWriterSettings: ...
    
    def get_TemporaryFiles(self) -> TempFileCollection: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XslCompiledTransform(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, enableDebug: BooleanType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def OutputSettings(self) -> XmlWriterSettings: ...
    
    @property
    def TemporaryFiles(self) -> TempFileCollection: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def CompileToType(stylesheet: XmlReader, settings: XsltSettings, stylesheetResolver: XmlResolver, debug: BooleanType, typeBuilder: TypeBuilder, scriptAssemblyPath: StringType) -> CompilerErrorCollection: ...
    
    @overload
    def Load(self, stylesheet: XmlReader, settings: XsltSettings, stylesheetResolver: XmlResolver) -> VoidType: ...
    
    @overload
    def Load(self, stylesheet: IXPathNavigable, settings: XsltSettings, stylesheetResolver: XmlResolver) -> VoidType: ...
    
    @overload
    def Load(self, stylesheetUri: StringType, settings: XsltSettings, stylesheetResolver: XmlResolver) -> VoidType: ...
    
    @overload
    def Load(self, stylesheet: XmlReader) -> VoidType: ...
    
    @overload
    def Load(self, stylesheet: IXPathNavigable) -> VoidType: ...
    
    @overload
    def Load(self, stylesheetUri: StringType) -> VoidType: ...
    
    @overload
    def Load(self, compiledStylesheet: TypeType) -> VoidType: ...
    
    @overload
    def Load(self, executeMethod: MethodInfo, queryData: ArrayType[ByteType], earlyBoundTypes: ArrayType[TypeType]) -> VoidType: ...
    
    @overload
    def Transform(self, input: IXPathNavigable, results: XmlWriter) -> VoidType: ...
    
    @overload
    def Transform(self, input: IXPathNavigable, arguments: XsltArgumentList, results: XmlWriter) -> VoidType: ...
    
    @overload
    def Transform(self, input: IXPathNavigable, arguments: XsltArgumentList, results: TextWriter) -> VoidType: ...
    
    @overload
    def Transform(self, input: IXPathNavigable, arguments: XsltArgumentList, results: Stream) -> VoidType: ...
    
    @overload
    def Transform(self, input: XmlReader, results: XmlWriter) -> VoidType: ...
    
    @overload
    def Transform(self, input: XmlReader, arguments: XsltArgumentList, results: XmlWriter) -> VoidType: ...
    
    @overload
    def Transform(self, input: XmlReader, arguments: XsltArgumentList, results: TextWriter) -> VoidType: ...
    
    @overload
    def Transform(self, input: XmlReader, arguments: XsltArgumentList, results: Stream) -> VoidType: ...
    
    @overload
    def Transform(self, inputUri: StringType, results: XmlWriter) -> VoidType: ...
    
    @overload
    def Transform(self, inputUri: StringType, arguments: XsltArgumentList, results: XmlWriter) -> VoidType: ...
    
    @overload
    def Transform(self, inputUri: StringType, arguments: XsltArgumentList, results: TextWriter) -> VoidType: ...
    
    @overload
    def Transform(self, inputUri: StringType, arguments: XsltArgumentList, results: Stream) -> VoidType: ...
    
    @overload
    def Transform(self, inputUri: StringType, resultsFile: StringType) -> VoidType: ...
    
    @overload
    def Transform(self, input: XmlReader, arguments: XsltArgumentList, results: XmlWriter, documentResolver: XmlResolver) -> VoidType: ...
    
    @overload
    def Transform(self, input: IXPathNavigable, arguments: XsltArgumentList, results: XmlWriter, documentResolver: XmlResolver) -> VoidType: ...
    
    def get_OutputSettings(self) -> XmlWriterSettings: ...
    
    def get_TemporaryFiles(self) -> TempFileCollection: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XslTransform(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @XmlResolver.setter
    def XmlResolver(self, value: XmlResolver) -> None: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Load(self, url: StringType) -> VoidType: ...
    
    @overload
    def Load(self, stylesheet: XmlReader, resolver: XmlResolver) -> VoidType: ...
    
    @overload
    def Load(self, stylesheet: IXPathNavigable, resolver: XmlResolver) -> VoidType: ...
    
    @overload
    def Load(self, stylesheet: XPathNavigator, resolver: XmlResolver) -> VoidType: ...
    
    @overload
    def Load(self, stylesheet: IXPathNavigable, resolver: XmlResolver, evidence: Evidence) -> VoidType: ...
    
    @overload
    def Load(self, stylesheet: XmlReader, resolver: XmlResolver, evidence: Evidence) -> VoidType: ...
    
    @overload
    def Load(self, stylesheet: XPathNavigator, resolver: XmlResolver, evidence: Evidence) -> VoidType: ...
    
    @overload
    def Load(self, stylesheet: XmlReader) -> VoidType: ...
    
    @overload
    def Load(self, stylesheet: IXPathNavigable) -> VoidType: ...
    
    @overload
    def Load(self, stylesheet: XPathNavigator) -> VoidType: ...
    
    @overload
    def Load(self, url: StringType, resolver: XmlResolver) -> VoidType: ...
    
    @overload
    def Transform(self, input: XPathNavigator, args: XsltArgumentList, resolver: XmlResolver) -> XmlReader: ...
    
    @overload
    def Transform(self, input: IXPathNavigable, args: XsltArgumentList) -> XmlReader: ...
    
    @overload
    def Transform(self, input: IXPathNavigable, args: XsltArgumentList, resolver: XmlResolver) -> XmlReader: ...
    
    @overload
    def Transform(self, input: IXPathNavigable, args: XsltArgumentList, output: TextWriter, resolver: XmlResolver) -> VoidType: ...
    
    @overload
    def Transform(self, input: IXPathNavigable, args: XsltArgumentList, output: Stream, resolver: XmlResolver) -> VoidType: ...
    
    @overload
    def Transform(self, input: IXPathNavigable, args: XsltArgumentList, output: XmlWriter, resolver: XmlResolver) -> VoidType: ...
    
    @overload
    def Transform(self, inputfile: StringType, outputfile: StringType, resolver: XmlResolver) -> VoidType: ...
    
    @overload
    def Transform(self, input: XPathNavigator, args: XsltArgumentList) -> XmlReader: ...
    
    @overload
    def Transform(self, input: XPathNavigator, args: XsltArgumentList, output: XmlWriter, resolver: XmlResolver) -> VoidType: ...
    
    @overload
    def Transform(self, input: XPathNavigator, args: XsltArgumentList, output: XmlWriter) -> VoidType: ...
    
    @overload
    def Transform(self, input: XPathNavigator, args: XsltArgumentList, output: Stream, resolver: XmlResolver) -> VoidType: ...
    
    @overload
    def Transform(self, input: XPathNavigator, args: XsltArgumentList, output: Stream) -> VoidType: ...
    
    @overload
    def Transform(self, input: XPathNavigator, args: XsltArgumentList, output: TextWriter, resolver: XmlResolver) -> VoidType: ...
    
    @overload
    def Transform(self, input: XPathNavigator, args: XsltArgumentList, output: TextWriter) -> VoidType: ...
    
    @overload
    def Transform(self, input: IXPathNavigable, args: XsltArgumentList, output: TextWriter) -> VoidType: ...
    
    @overload
    def Transform(self, input: IXPathNavigable, args: XsltArgumentList, output: Stream) -> VoidType: ...
    
    @overload
    def Transform(self, input: IXPathNavigable, args: XsltArgumentList, output: XmlWriter) -> VoidType: ...
    
    @overload
    def Transform(self, inputfile: StringType, outputfile: StringType) -> VoidType: ...
    
    def set_XmlResolver(self, value: XmlResolver) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XslTransform(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @XmlResolver.setter
    def XmlResolver(self, value: XmlResolver) -> None: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Load(self, url: StringType) -> VoidType: ...
    
    @overload
    def Load(self, stylesheet: XmlReader, resolver: XmlResolver) -> VoidType: ...
    
    @overload
    def Load(self, stylesheet: IXPathNavigable, resolver: XmlResolver) -> VoidType: ...
    
    @overload
    def Load(self, stylesheet: XPathNavigator, resolver: XmlResolver) -> VoidType: ...
    
    @overload
    def Load(self, stylesheet: IXPathNavigable, resolver: XmlResolver, evidence: Evidence) -> VoidType: ...
    
    @overload
    def Load(self, stylesheet: XmlReader, resolver: XmlResolver, evidence: Evidence) -> VoidType: ...
    
    @overload
    def Load(self, stylesheet: XPathNavigator, resolver: XmlResolver, evidence: Evidence) -> VoidType: ...
    
    @overload
    def Load(self, stylesheet: XmlReader) -> VoidType: ...
    
    @overload
    def Load(self, stylesheet: IXPathNavigable) -> VoidType: ...
    
    @overload
    def Load(self, stylesheet: XPathNavigator) -> VoidType: ...
    
    @overload
    def Load(self, url: StringType, resolver: XmlResolver) -> VoidType: ...
    
    @overload
    def Transform(self, input: XPathNavigator, args: XsltArgumentList, resolver: XmlResolver) -> XmlReader: ...
    
    @overload
    def Transform(self, input: IXPathNavigable, args: XsltArgumentList) -> XmlReader: ...
    
    @overload
    def Transform(self, input: IXPathNavigable, args: XsltArgumentList, resolver: XmlResolver) -> XmlReader: ...
    
    @overload
    def Transform(self, input: IXPathNavigable, args: XsltArgumentList, output: TextWriter, resolver: XmlResolver) -> VoidType: ...
    
    @overload
    def Transform(self, input: IXPathNavigable, args: XsltArgumentList, output: Stream, resolver: XmlResolver) -> VoidType: ...
    
    @overload
    def Transform(self, input: IXPathNavigable, args: XsltArgumentList, output: XmlWriter, resolver: XmlResolver) -> VoidType: ...
    
    @overload
    def Transform(self, inputfile: StringType, outputfile: StringType, resolver: XmlResolver) -> VoidType: ...
    
    @overload
    def Transform(self, input: XPathNavigator, args: XsltArgumentList) -> XmlReader: ...
    
    @overload
    def Transform(self, input: XPathNavigator, args: XsltArgumentList, output: XmlWriter, resolver: XmlResolver) -> VoidType: ...
    
    @overload
    def Transform(self, input: XPathNavigator, args: XsltArgumentList, output: XmlWriter) -> VoidType: ...
    
    @overload
    def Transform(self, input: XPathNavigator, args: XsltArgumentList, output: Stream, resolver: XmlResolver) -> VoidType: ...
    
    @overload
    def Transform(self, input: XPathNavigator, args: XsltArgumentList, output: Stream) -> VoidType: ...
    
    @overload
    def Transform(self, input: XPathNavigator, args: XsltArgumentList, output: TextWriter, resolver: XmlResolver) -> VoidType: ...
    
    @overload
    def Transform(self, input: XPathNavigator, args: XsltArgumentList, output: TextWriter) -> VoidType: ...
    
    @overload
    def Transform(self, input: IXPathNavigable, args: XsltArgumentList, output: TextWriter) -> VoidType: ...
    
    @overload
    def Transform(self, input: IXPathNavigable, args: XsltArgumentList, output: Stream) -> VoidType: ...
    
    @overload
    def Transform(self, input: IXPathNavigable, args: XsltArgumentList, output: XmlWriter) -> VoidType: ...
    
    @overload
    def Transform(self, inputfile: StringType, outputfile: StringType) -> VoidType: ...
    
    def set_XmlResolver(self, value: XmlResolver) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XsltArgumentList(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def AddExtensionObject(self, namespaceUri: StringType, extension: ObjectType) -> VoidType: ...
    
    def AddParam(self, name: StringType, namespaceUri: StringType, parameter: ObjectType) -> VoidType: ...
    
    def Clear(self) -> VoidType: ...
    
    def GetExtensionObject(self, namespaceUri: StringType) -> ObjectType: ...
    
    def GetParam(self, name: StringType, namespaceUri: StringType) -> ObjectType: ...
    
    def RemoveExtensionObject(self, namespaceUri: StringType) -> ObjectType: ...
    
    def RemoveParam(self, name: StringType, namespaceUri: StringType) -> ObjectType: ...
    
    def add_XsltMessageEncountered(self, value: XsltMessageEncounteredEventHandler) -> VoidType: ...
    
    def remove_XsltMessageEncountered(self, value: XsltMessageEncounteredEventHandler) -> VoidType: ...
    
    # ---------- Events ---------- #
    
    XsltMessageEncountered: EventType[XsltMessageEncounteredEventHandler] = ...
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XsltArgumentList(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def AddExtensionObject(self, namespaceUri: StringType, extension: ObjectType) -> VoidType: ...
    
    def AddParam(self, name: StringType, namespaceUri: StringType, parameter: ObjectType) -> VoidType: ...
    
    def Clear(self) -> VoidType: ...
    
    def GetExtensionObject(self, namespaceUri: StringType) -> ObjectType: ...
    
    def GetParam(self, name: StringType, namespaceUri: StringType) -> ObjectType: ...
    
    def RemoveExtensionObject(self, namespaceUri: StringType) -> ObjectType: ...
    
    def RemoveParam(self, name: StringType, namespaceUri: StringType) -> ObjectType: ...
    
    def add_XsltMessageEncountered(self, value: XsltMessageEncounteredEventHandler) -> VoidType: ...
    
    def remove_XsltMessageEncountered(self, value: XsltMessageEncounteredEventHandler) -> VoidType: ...
    
    # ---------- Events ---------- #
    
    XsltMessageEncountered: EventType[XsltMessageEncounteredEventHandler] = ...
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XsltCompileException(XsltException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    @overload
    def __init__(self, inner: Exception, sourceUri: StringType, lineNumber: IntType, linePosition: IntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XsltCompileException(XsltException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    @overload
    def __init__(self, inner: Exception, sourceUri: StringType, lineNumber: IntType, linePosition: IntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XsltContext(ABC, XmlNamespaceManager, IXmlNamespaceResolver, IEnumerable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Whitespace(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def CompareDocument(self, baseUri: StringType, nextbaseUri: StringType) -> IntType: ...
    
    def PreserveWhitespace(self, node: XPathNavigator) -> BooleanType: ...
    
    def ResolveFunction(self, prefix: StringType, name: StringType, ArgTypes: ArrayType[XPathResultType]) -> IXsltContextFunction: ...
    
    def ResolveVariable(self, prefix: StringType, name: StringType) -> IXsltContextVariable: ...
    
    def get_Whitespace(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XsltContext(ABC, XmlNamespaceManager, IXmlNamespaceResolver, IEnumerable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Whitespace(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def CompareDocument(self, baseUri: StringType, nextbaseUri: StringType) -> IntType: ...
    
    def PreserveWhitespace(self, node: XPathNavigator) -> BooleanType: ...
    
    def ResolveFunction(self, prefix: StringType, name: StringType, ArgTypes: ArrayType[XPathResultType]) -> IXsltContextFunction: ...
    
    def ResolveVariable(self, prefix: StringType, name: StringType) -> IXsltContextVariable: ...
    
    def get_Whitespace(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XsltException(SystemException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    # ---------- Properties ---------- #
    
    @property
    def LineNumber(self) -> IntType: ...
    
    @property
    def LinePosition(self) -> IntType: ...
    
    @property
    def Message(self) -> StringType: ...
    
    @property
    def SourceUri(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    
    def get_LineNumber(self) -> IntType: ...
    
    def get_LinePosition(self) -> IntType: ...
    
    def get_Message(self) -> StringType: ...
    
    def get_SourceUri(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XsltException(SystemException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    # ---------- Properties ---------- #
    
    @property
    def LineNumber(self) -> IntType: ...
    
    @property
    def LinePosition(self) -> IntType: ...
    
    @property
    def Message(self) -> StringType: ...
    
    @property
    def SourceUri(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    
    def get_LineNumber(self) -> IntType: ...
    
    def get_LinePosition(self) -> IntType: ...
    
    def get_Message(self) -> StringType: ...
    
    def get_SourceUri(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XsltMessageEncounteredEventArgs(ABC, EventArgs):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Message(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_Message(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XsltMessageEncounteredEventArgs(ABC, EventArgs):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Message(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_Message(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XsltMessageEncounteredEventHandler(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, sender: ObjectType, e: XsltMessageEncounteredEventArgs, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, sender: ObjectType, e: XsltMessageEncounteredEventArgs) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XsltMessageEncounteredEventHandler(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, sender: ObjectType, e: XsltMessageEncounteredEventArgs, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, sender: ObjectType, e: XsltMessageEncounteredEventArgs) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XsltSettings(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, enableDocumentFunction: BooleanType, enableScript: BooleanType): ...
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def Default() -> XsltSettings: ...
    
    @property
    def EnableDocumentFunction(self) -> BooleanType: ...
    
    @EnableDocumentFunction.setter
    def EnableDocumentFunction(self, value: BooleanType) -> None: ...
    
    @property
    def EnableScript(self) -> BooleanType: ...
    
    @EnableScript.setter
    def EnableScript(self, value: BooleanType) -> None: ...
    
    @staticmethod
    @property
    def TrustedXslt() -> XsltSettings: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def get_Default() -> XsltSettings: ...
    
    def get_EnableDocumentFunction(self) -> BooleanType: ...
    
    def get_EnableScript(self) -> BooleanType: ...
    
    @staticmethod
    def get_TrustedXslt() -> XsltSettings: ...
    
    def set_EnableDocumentFunction(self, value: BooleanType) -> VoidType: ...
    
    def set_EnableScript(self, value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XsltSettings(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, enableDocumentFunction: BooleanType, enableScript: BooleanType): ...
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def Default() -> XsltSettings: ...
    
    @property
    def EnableDocumentFunction(self) -> BooleanType: ...
    
    @EnableDocumentFunction.setter
    def EnableDocumentFunction(self, value: BooleanType) -> None: ...
    
    @property
    def EnableScript(self) -> BooleanType: ...
    
    @EnableScript.setter
    def EnableScript(self, value: BooleanType) -> None: ...
    
    @staticmethod
    @property
    def TrustedXslt() -> XsltSettings: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def get_Default() -> XsltSettings: ...
    
    def get_EnableDocumentFunction(self) -> BooleanType: ...
    
    def get_EnableScript(self) -> BooleanType: ...
    
    @staticmethod
    def get_TrustedXslt() -> XsltSettings: ...
    
    def set_EnableDocumentFunction(self, value: BooleanType) -> VoidType: ...
    
    def set_EnableScript(self, value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# No Structs

# ---------- Interfaces ---------- #

class IXsltContextFunction(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def ArgTypes(self) -> ArrayType[XPathResultType]: ...
    
    @property
    def Maxargs(self) -> IntType: ...
    
    @property
    def Minargs(self) -> IntType: ...
    
    @property
    def ReturnType(self) -> XPathResultType: ...
    
    # ---------- Methods ---------- #
    
    def Invoke(self, xsltContext: XsltContext, args: ArrayType[ObjectType], docContext: XPathNavigator) -> ObjectType: ...
    
    def get_ArgTypes(self) -> ArrayType[XPathResultType]: ...
    
    def get_Maxargs(self) -> IntType: ...
    
    def get_Minargs(self) -> IntType: ...
    
    def get_ReturnType(self) -> XPathResultType: ...
    
    # No Events


class IXsltContextFunction(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def ArgTypes(self) -> ArrayType[XPathResultType]: ...
    
    @property
    def Maxargs(self) -> IntType: ...
    
    @property
    def Minargs(self) -> IntType: ...
    
    @property
    def ReturnType(self) -> XPathResultType: ...
    
    # ---------- Methods ---------- #
    
    def Invoke(self, xsltContext: XsltContext, args: ArrayType[ObjectType], docContext: XPathNavigator) -> ObjectType: ...
    
    def get_ArgTypes(self) -> ArrayType[XPathResultType]: ...
    
    def get_Maxargs(self) -> IntType: ...
    
    def get_Minargs(self) -> IntType: ...
    
    def get_ReturnType(self) -> XPathResultType: ...
    
    # No Events


class IXsltContextVariable(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def IsLocal(self) -> BooleanType: ...
    
    @property
    def IsParam(self) -> BooleanType: ...
    
    @property
    def VariableType(self) -> XPathResultType: ...
    
    # ---------- Methods ---------- #
    
    def Evaluate(self, xsltContext: XsltContext) -> ObjectType: ...
    
    def get_IsLocal(self) -> BooleanType: ...
    
    def get_IsParam(self) -> BooleanType: ...
    
    def get_VariableType(self) -> XPathResultType: ...
    
    # No Events


class IXsltContextVariable(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def IsLocal(self) -> BooleanType: ...
    
    @property
    def IsParam(self) -> BooleanType: ...
    
    @property
    def VariableType(self) -> XPathResultType: ...
    
    # ---------- Methods ---------- #
    
    def Evaluate(self, xsltContext: XsltContext) -> ObjectType: ...
    
    def get_IsLocal(self) -> BooleanType: ...
    
    def get_IsParam(self) -> BooleanType: ...
    
    def get_VariableType(self) -> XPathResultType: ...
    
    # No Events


# No Enums

# ---------- Delegates ---------- #

XsltMessageEncounteredEventHandler = Callable[[ObjectType, XsltMessageEncounteredEventArgs], VoidType]

XsltMessageEncounteredEventHandler = Callable[[ObjectType, XsltMessageEncounteredEventArgs], VoidType]

__all__ = [
    XslCompiledTransform,
    XslTransform,
    XsltArgumentList,
    XsltCompileException,
    XsltContext,
    XsltException,
    XsltMessageEncounteredEventArgs,
    XsltMessageEncounteredEventHandler,
    XsltSettings,
    IXsltContextFunction,
    IXsltContextVariable,
    XsltMessageEncounteredEventHandler,
]
