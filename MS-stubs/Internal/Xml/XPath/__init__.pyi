from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar, Union, overload

from System import Boolean, Double, Enum, ICloneable, Int32, Object, String, Void
from System.Collections import ArrayList, ICollection, IComparer, IEnumerable, IEnumerator, IList
from System.Collections.Generic import ICollection, IComparer, IEnumerable, IList, IReadOnlyCollection, IReadOnlyList, List
from System.Xml import IXmlNamespaceResolver, XmlNamespaceManager, XmlNodeOrder, XmlWriter
from System.Xml.XPath import XPathExpression, XPathNavigator, XPathNodeIterator, XPathNodeType, XPathResultType, XmlCaseOrder, XmlDataType, XmlSortOrder
from System.Xml.Xsl import XsltContext

# ---------- Types ---------- #

T = TypeVar('T')

BooleanType = Union[bool, Boolean]
DoubleType = Union[float, Double]
IntType = Union[int, Int32]
ObjectType = Object
StringType = Union[str, String]
VoidType = Union[None, Void]

# ---------- Classes ---------- #

class AbsoluteQuery(ContextQuery, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def Evaluate(self, context: XPathNodeIterator) -> ObjectType: ...
    
    def MatchNode(self, context: XPathNavigator) -> XPathNavigator: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AbsoluteQuery(ContextQuery, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def Evaluate(self, context: XPathNodeIterator) -> ObjectType: ...
    
    def MatchNode(self, context: XPathNavigator) -> XPathNavigator: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AstNode(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def ReturnType(self) -> XPathResultType: ...
    
    @property
    def Type(self) -> AstType: ...
    
    # ---------- Methods ---------- #
    
    def get_ReturnType(self) -> XPathResultType: ...
    
    def get_Type(self) -> AstType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # ---------- Sub Enums ---------- #
    
    class AstType(Enum):
        Axis: IntType = 0
        Operator: IntType = 1
        Filter: IntType = 2
        ConstantOperand: IntType = 3
        Function: IntType = 4
        Group: IntType = 5
        Root: IntType = 6
        Variable: IntType = 7
        Error: IntType = 8
    


class AstNode(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def ReturnType(self) -> XPathResultType: ...
    
    @property
    def Type(self) -> AstType: ...
    
    # ---------- Methods ---------- #
    
    def get_ReturnType(self) -> XPathResultType: ...
    
    def get_Type(self) -> AstType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # ---------- Sub Enums ---------- #
    
    class AstType(Enum):
        Axis: IntType = 0
        Operator: IntType = 1
        Filter: IntType = 2
        ConstantOperand: IntType = 3
        Function: IntType = 4
        Group: IntType = 5
        Root: IntType = 6
        Variable: IntType = 7
        Error: IntType = 8
    


class AttributeQuery(BaseAxisQuery, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, qyParent: Query, Name: StringType, Prefix: StringType, Type: XPathNodeType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Advance(self) -> XPathNavigator: ...
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def MatchNode(self, context: XPathNavigator) -> XPathNavigator: ...
    
    def Reset(self) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AttributeQuery(BaseAxisQuery, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, qyParent: Query, Name: StringType, Prefix: StringType, Type: XPathNodeType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Advance(self) -> XPathNavigator: ...
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def MatchNode(self, context: XPathNavigator) -> XPathNavigator: ...
    
    def Reset(self) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Axis(AstNode):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, axisType: AxisType, input: AstNode, prefix: StringType, name: StringType, nodetype: XPathNodeType): ...
    
    @overload
    def __init__(self, axisType: AxisType, input: AstNode): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AbbrAxis(self) -> BooleanType: ...
    
    @property
    def Input(self) -> AstNode: ...
    
    @Input.setter
    def Input(self, value: AstNode) -> None: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def NodeType(self) -> XPathNodeType: ...
    
    @property
    def Prefix(self) -> StringType: ...
    
    @property
    def ReturnType(self) -> XPathResultType: ...
    
    @property
    def Type(self) -> AstType: ...
    
    @property
    def TypeOfAxis(self) -> AxisType: ...
    
    @property
    def Urn(self) -> StringType: ...
    
    @Urn.setter
    def Urn(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_AbbrAxis(self) -> BooleanType: ...
    
    def get_Input(self) -> AstNode: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_NodeType(self) -> XPathNodeType: ...
    
    def get_Prefix(self) -> StringType: ...
    
    def get_ReturnType(self) -> XPathResultType: ...
    
    def get_Type(self) -> AstType: ...
    
    def get_TypeOfAxis(self) -> AxisType: ...
    
    def get_Urn(self) -> StringType: ...
    
    def set_Input(self, value: AstNode) -> VoidType: ...
    
    def set_Urn(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # ---------- Sub Enums ---------- #
    
    class AxisType(Enum):
        Ancestor: IntType = 0
        AncestorOrSelf: IntType = 1
        Attribute: IntType = 2
        Child: IntType = 3
        Descendant: IntType = 4
        DescendantOrSelf: IntType = 5
        Following: IntType = 6
        FollowingSibling: IntType = 7
        Namespace: IntType = 8
        Parent: IntType = 9
        Preceding: IntType = 10
        PrecedingSibling: IntType = 11
        Self: IntType = 12
        #None: IntType = 13
    


class Axis(AstNode):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, axisType: AxisType, input: AstNode, prefix: StringType, name: StringType, nodetype: XPathNodeType): ...
    
    @overload
    def __init__(self, axisType: AxisType, input: AstNode): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AbbrAxis(self) -> BooleanType: ...
    
    @property
    def Input(self) -> AstNode: ...
    
    @Input.setter
    def Input(self, value: AstNode) -> None: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def NodeType(self) -> XPathNodeType: ...
    
    @property
    def Prefix(self) -> StringType: ...
    
    @property
    def ReturnType(self) -> XPathResultType: ...
    
    @property
    def Type(self) -> AstType: ...
    
    @property
    def TypeOfAxis(self) -> AxisType: ...
    
    @property
    def Urn(self) -> StringType: ...
    
    @Urn.setter
    def Urn(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_AbbrAxis(self) -> BooleanType: ...
    
    def get_Input(self) -> AstNode: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_NodeType(self) -> XPathNodeType: ...
    
    def get_Prefix(self) -> StringType: ...
    
    def get_ReturnType(self) -> XPathResultType: ...
    
    def get_Type(self) -> AstType: ...
    
    def get_TypeOfAxis(self) -> AxisType: ...
    
    def get_Urn(self) -> StringType: ...
    
    def set_Input(self, value: AstNode) -> VoidType: ...
    
    def set_Urn(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # ---------- Sub Enums ---------- #
    
    class AxisType(Enum):
        Ancestor: IntType = 0
        AncestorOrSelf: IntType = 1
        Attribute: IntType = 2
        Child: IntType = 3
        Descendant: IntType = 4
        DescendantOrSelf: IntType = 5
        Following: IntType = 6
        FollowingSibling: IntType = 7
        Namespace: IntType = 8
        Parent: IntType = 9
        Preceding: IntType = 10
        PrecedingSibling: IntType = 11
        Self: IntType = 12
        #None: IntType = 13
    


class BaseAxisQuery(ABC, Query, ICloneable, IEnumerable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Current(self) -> XPathNavigator: ...
    
    @property
    def CurrentPosition(self) -> IntType: ...
    
    @property
    def StaticType(self) -> XPathResultType: ...
    
    @property
    def XsltDefaultPriority(self) -> DoubleType: ...
    
    # ---------- Methods ---------- #
    
    def Evaluate(self, nodeIterator: XPathNodeIterator) -> ObjectType: ...
    
    def PrintQuery(self, w: XmlWriter) -> VoidType: ...
    
    def Reset(self) -> VoidType: ...
    
    def SetXsltContext(self, context: XsltContext) -> VoidType: ...
    
    def get_Current(self) -> XPathNavigator: ...
    
    def get_CurrentPosition(self) -> IntType: ...
    
    def get_StaticType(self) -> XPathResultType: ...
    
    def get_XsltDefaultPriority(self) -> DoubleType: ...
    
    def matches(self, e: XPathNavigator) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class BaseAxisQuery(ABC, Query, ICloneable, IEnumerable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Current(self) -> XPathNavigator: ...
    
    @property
    def CurrentPosition(self) -> IntType: ...
    
    @property
    def StaticType(self) -> XPathResultType: ...
    
    @property
    def XsltDefaultPriority(self) -> DoubleType: ...
    
    # ---------- Methods ---------- #
    
    def Evaluate(self, nodeIterator: XPathNodeIterator) -> ObjectType: ...
    
    def PrintQuery(self, w: XmlWriter) -> VoidType: ...
    
    def Reset(self) -> VoidType: ...
    
    def SetXsltContext(self, context: XsltContext) -> VoidType: ...
    
    def get_Current(self) -> XPathNavigator: ...
    
    def get_CurrentPosition(self) -> IntType: ...
    
    def get_StaticType(self) -> XPathResultType: ...
    
    def get_XsltDefaultPriority(self) -> DoubleType: ...
    
    def matches(self, e: XPathNavigator) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class BooleanExpr(ValueQuery, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, op: Op, opnd1: Query, opnd2: Query): ...
    
    # ---------- Properties ---------- #
    
    @property
    def StaticType(self) -> XPathResultType: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def Evaluate(self, nodeIterator: XPathNodeIterator) -> ObjectType: ...
    
    def PrintQuery(self, w: XmlWriter) -> VoidType: ...
    
    def SetXsltContext(self, context: XsltContext) -> VoidType: ...
    
    def get_StaticType(self) -> XPathResultType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class BooleanExpr(ValueQuery, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, op: Op, opnd1: Query, opnd2: Query): ...
    
    # ---------- Properties ---------- #
    
    @property
    def StaticType(self) -> XPathResultType: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def Evaluate(self, nodeIterator: XPathNodeIterator) -> ObjectType: ...
    
    def PrintQuery(self, w: XmlWriter) -> VoidType: ...
    
    def SetXsltContext(self, context: XsltContext) -> VoidType: ...
    
    def get_StaticType(self) -> XPathResultType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class BooleanFunctions(ValueQuery, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, funcType: FunctionType, arg: Query): ...
    
    # ---------- Properties ---------- #
    
    @property
    def StaticType(self) -> XPathResultType: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def Evaluate(self, nodeIterator: XPathNodeIterator) -> ObjectType: ...
    
    def PrintQuery(self, w: XmlWriter) -> VoidType: ...
    
    def SetXsltContext(self, context: XsltContext) -> VoidType: ...
    
    def get_StaticType(self) -> XPathResultType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class BooleanFunctions(ValueQuery, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, funcType: FunctionType, arg: Query): ...
    
    # ---------- Properties ---------- #
    
    @property
    def StaticType(self) -> XPathResultType: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def Evaluate(self, nodeIterator: XPathNodeIterator) -> ObjectType: ...
    
    def PrintQuery(self, w: XmlWriter) -> VoidType: ...
    
    def SetXsltContext(self, context: XsltContext) -> VoidType: ...
    
    def get_StaticType(self) -> XPathResultType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CacheAxisQuery(ABC, BaseAxisQuery, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, qyInput: Query, name: StringType, prefix: StringType, typeTest: XPathNodeType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def Current(self) -> XPathNavigator: ...
    
    @property
    def CurrentPosition(self) -> IntType: ...
    
    @property
    def Properties(self) -> QueryProps: ...
    
    # ---------- Methods ---------- #
    
    def Advance(self) -> XPathNavigator: ...
    
    def Evaluate(self, context: XPathNodeIterator) -> ObjectType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_Current(self) -> XPathNavigator: ...
    
    def get_CurrentPosition(self) -> IntType: ...
    
    def get_Properties(self) -> QueryProps: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CacheAxisQuery(ABC, BaseAxisQuery, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, qyInput: Query, name: StringType, prefix: StringType, typeTest: XPathNodeType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def Current(self) -> XPathNavigator: ...
    
    @property
    def CurrentPosition(self) -> IntType: ...
    
    @property
    def Properties(self) -> QueryProps: ...
    
    # ---------- Methods ---------- #
    
    def Advance(self) -> XPathNavigator: ...
    
    def Evaluate(self, context: XPathNodeIterator) -> ObjectType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_Current(self) -> XPathNavigator: ...
    
    def get_CurrentPosition(self) -> IntType: ...
    
    def get_Properties(self) -> QueryProps: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CacheChildrenQuery(ChildrenQuery, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, qyInput: Query, name: StringType, prefix: StringType, type: XPathNodeType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Advance(self) -> XPathNavigator: ...
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def Reset(self) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CacheChildrenQuery(ChildrenQuery, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, qyInput: Query, name: StringType, prefix: StringType, type: XPathNodeType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Advance(self) -> XPathNavigator: ...
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def Reset(self) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CacheOutputQuery(ABC, Query, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, input: Query): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def Current(self) -> XPathNavigator: ...
    
    @property
    def CurrentPosition(self) -> IntType: ...
    
    @property
    def Properties(self) -> QueryProps: ...
    
    @property
    def StaticType(self) -> XPathResultType: ...
    
    # ---------- Methods ---------- #
    
    def Advance(self) -> XPathNavigator: ...
    
    def Evaluate(self, context: XPathNodeIterator) -> ObjectType: ...
    
    def PrintQuery(self, w: XmlWriter) -> VoidType: ...
    
    def Reset(self) -> VoidType: ...
    
    def SetXsltContext(self, context: XsltContext) -> VoidType: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_Current(self) -> XPathNavigator: ...
    
    def get_CurrentPosition(self) -> IntType: ...
    
    def get_Properties(self) -> QueryProps: ...
    
    def get_StaticType(self) -> XPathResultType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CacheOutputQuery(ABC, Query, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, input: Query): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def Current(self) -> XPathNavigator: ...
    
    @property
    def CurrentPosition(self) -> IntType: ...
    
    @property
    def Properties(self) -> QueryProps: ...
    
    @property
    def StaticType(self) -> XPathResultType: ...
    
    # ---------- Methods ---------- #
    
    def Advance(self) -> XPathNavigator: ...
    
    def Evaluate(self, context: XPathNodeIterator) -> ObjectType: ...
    
    def PrintQuery(self, w: XmlWriter) -> VoidType: ...
    
    def Reset(self) -> VoidType: ...
    
    def SetXsltContext(self, context: XsltContext) -> VoidType: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_Current(self) -> XPathNavigator: ...
    
    def get_CurrentPosition(self) -> IntType: ...
    
    def get_Properties(self) -> QueryProps: ...
    
    def get_StaticType(self) -> XPathResultType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ChildrenQuery(BaseAxisQuery, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, qyInput: Query, name: StringType, prefix: StringType, type: XPathNodeType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Advance(self) -> XPathNavigator: ...
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def MatchNode(self, context: XPathNavigator) -> XPathNavigator: ...
    
    def Reset(self) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ChildrenQuery(BaseAxisQuery, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, qyInput: Query, name: StringType, prefix: StringType, type: XPathNodeType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Advance(self) -> XPathNavigator: ...
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def MatchNode(self, context: XPathNavigator) -> XPathNavigator: ...
    
    def Reset(self) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ClonableStack(Generic[T], List[T], IList[T], ICollection[T], IEnumerable[T], IEnumerable, IList, ICollection, IReadOnlyList[T], IReadOnlyCollection[T]):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, capacity: IntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> ClonableStack[T]: ...
    
    def Peek(self) -> T: ...
    
    def Pop(self) -> T: ...
    
    def Push(self, value: T) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ClonableStack(Generic[T], List[T], IList[T], ICollection[T], IEnumerable[T], IEnumerable, IList, ICollection, IReadOnlyList[T], IReadOnlyCollection[T]):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, capacity: IntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> ClonableStack[T]: ...
    
    def Peek(self) -> T: ...
    
    def Pop(self) -> T: ...
    
    def Push(self, value: T) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CompiledXpathExpr(XPathExpression):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Expression(self) -> StringType: ...
    
    @property
    def ReturnType(self) -> XPathResultType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def AddSort(self, expr: ObjectType, comparer: IComparer) -> VoidType: ...
    
    @overload
    def AddSort(self, expr: ObjectType, order: XmlSortOrder, caseOrder: XmlCaseOrder, lang: StringType, dataType: XmlDataType) -> VoidType: ...
    
    def CheckErrors(self) -> VoidType: ...
    
    def Clone(self) -> XPathExpression: ...
    
    @overload
    def SetContext(self, nsManager: XmlNamespaceManager) -> VoidType: ...
    
    @overload
    def SetContext(self, nsResolver: IXmlNamespaceResolver) -> VoidType: ...
    
    def get_Expression(self) -> StringType: ...
    
    def get_ReturnType(self) -> XPathResultType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CompiledXpathExpr(XPathExpression):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Expression(self) -> StringType: ...
    
    @property
    def ReturnType(self) -> XPathResultType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def AddSort(self, expr: ObjectType, comparer: IComparer) -> VoidType: ...
    
    @overload
    def AddSort(self, expr: ObjectType, order: XmlSortOrder, caseOrder: XmlCaseOrder, lang: StringType, dataType: XmlDataType) -> VoidType: ...
    
    def CheckErrors(self) -> VoidType: ...
    
    def Clone(self) -> XPathExpression: ...
    
    @overload
    def SetContext(self, nsManager: XmlNamespaceManager) -> VoidType: ...
    
    @overload
    def SetContext(self, nsResolver: IXmlNamespaceResolver) -> VoidType: ...
    
    def get_Expression(self) -> StringType: ...
    
    def get_ReturnType(self) -> XPathResultType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ContextQuery(Query, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def Current(self) -> XPathNavigator: ...
    
    @property
    def CurrentPosition(self) -> IntType: ...
    
    @property
    def Properties(self) -> QueryProps: ...
    
    @property
    def StaticType(self) -> XPathResultType: ...
    
    # ---------- Methods ---------- #
    
    def Advance(self) -> XPathNavigator: ...
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def Evaluate(self, context: XPathNodeIterator) -> ObjectType: ...
    
    def MatchNode(self, current: XPathNavigator) -> XPathNavigator: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_Current(self) -> XPathNavigator: ...
    
    def get_CurrentPosition(self) -> IntType: ...
    
    def get_Properties(self) -> QueryProps: ...
    
    def get_StaticType(self) -> XPathResultType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ContextQuery(Query, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def Current(self) -> XPathNavigator: ...
    
    @property
    def CurrentPosition(self) -> IntType: ...
    
    @property
    def Properties(self) -> QueryProps: ...
    
    @property
    def StaticType(self) -> XPathResultType: ...
    
    # ---------- Methods ---------- #
    
    def Advance(self) -> XPathNavigator: ...
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def Evaluate(self, context: XPathNodeIterator) -> ObjectType: ...
    
    def MatchNode(self, current: XPathNavigator) -> XPathNavigator: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_Current(self) -> XPathNavigator: ...
    
    def get_CurrentPosition(self) -> IntType: ...
    
    def get_Properties(self) -> QueryProps: ...
    
    def get_StaticType(self) -> XPathResultType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DescendantBaseQuery(ABC, BaseAxisQuery, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, qyParent: Query, Name: StringType, Prefix: StringType, Type: XPathNodeType, matchSelf: BooleanType, abbrAxis: BooleanType): ...
    
    @overload
    def __init__(self, other: DescendantBaseQuery): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def MatchNode(self, context: XPathNavigator) -> XPathNavigator: ...
    
    def PrintQuery(self, w: XmlWriter) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DescendantBaseQuery(ABC, BaseAxisQuery, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, qyParent: Query, Name: StringType, Prefix: StringType, Type: XPathNodeType, matchSelf: BooleanType, abbrAxis: BooleanType): ...
    
    @overload
    def __init__(self, other: DescendantBaseQuery): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def MatchNode(self, context: XPathNavigator) -> XPathNavigator: ...
    
    def PrintQuery(self, w: XmlWriter) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DescendantOverDescendantQuery(DescendantBaseQuery, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, qyParent: Query, matchSelf: BooleanType, name: StringType, prefix: StringType, typeTest: XPathNodeType, abbrAxis: BooleanType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Advance(self) -> XPathNavigator: ...
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def Reset(self) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DescendantOverDescendantQuery(DescendantBaseQuery, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, qyParent: Query, matchSelf: BooleanType, name: StringType, prefix: StringType, typeTest: XPathNodeType, abbrAxis: BooleanType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Advance(self) -> XPathNavigator: ...
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def Reset(self) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DescendantQuery(DescendantBaseQuery, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, other: DescendantQuery): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Advance(self) -> XPathNavigator: ...
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def Reset(self) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DescendantQuery(DescendantBaseQuery, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, other: DescendantQuery): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Advance(self) -> XPathNavigator: ...
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def Reset(self) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DocumentOrderQuery(CacheOutputQuery, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, qyParent: Query): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def Evaluate(self, context: XPathNodeIterator) -> ObjectType: ...
    
    def MatchNode(self, context: XPathNavigator) -> XPathNavigator: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DocumentOrderQuery(CacheOutputQuery, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, qyParent: Query): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def Evaluate(self, context: XPathNodeIterator) -> ObjectType: ...
    
    def MatchNode(self, context: XPathNavigator) -> XPathNavigator: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EmptyQuery(Query, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def Current(self) -> XPathNavigator: ...
    
    @property
    def CurrentPosition(self) -> IntType: ...
    
    @property
    def Properties(self) -> QueryProps: ...
    
    @property
    def StaticType(self) -> XPathResultType: ...
    
    # ---------- Methods ---------- #
    
    def Advance(self) -> XPathNavigator: ...
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def Evaluate(self, context: XPathNodeIterator) -> ObjectType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_Current(self) -> XPathNavigator: ...
    
    def get_CurrentPosition(self) -> IntType: ...
    
    def get_Properties(self) -> QueryProps: ...
    
    def get_StaticType(self) -> XPathResultType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EmptyQuery(Query, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def Current(self) -> XPathNavigator: ...
    
    @property
    def CurrentPosition(self) -> IntType: ...
    
    @property
    def Properties(self) -> QueryProps: ...
    
    @property
    def StaticType(self) -> XPathResultType: ...
    
    # ---------- Methods ---------- #
    
    def Advance(self) -> XPathNavigator: ...
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def Evaluate(self, context: XPathNodeIterator) -> ObjectType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_Current(self) -> XPathNavigator: ...
    
    def get_CurrentPosition(self) -> IntType: ...
    
    def get_Properties(self) -> QueryProps: ...
    
    def get_StaticType(self) -> XPathResultType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ExtensionQuery(ABC, Query, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, prefix: StringType, name: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def Current(self) -> XPathNavigator: ...
    
    @property
    def CurrentPosition(self) -> IntType: ...
    
    @property
    def StaticType(self) -> XPathResultType: ...
    
    # ---------- Methods ---------- #
    
    def Advance(self) -> XPathNavigator: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_Current(self) -> XPathNavigator: ...
    
    def get_CurrentPosition(self) -> IntType: ...
    
    def get_StaticType(self) -> XPathResultType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ExtensionQuery(ABC, Query, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, prefix: StringType, name: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def Current(self) -> XPathNavigator: ...
    
    @property
    def CurrentPosition(self) -> IntType: ...
    
    @property
    def StaticType(self) -> XPathResultType: ...
    
    # ---------- Methods ---------- #
    
    def Advance(self) -> XPathNavigator: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_Current(self) -> XPathNavigator: ...
    
    def get_CurrentPosition(self) -> IntType: ...
    
    def get_StaticType(self) -> XPathResultType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Filter(AstNode):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, input: AstNode, condition: AstNode): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Condition(self) -> AstNode: ...
    
    @property
    def Input(self) -> AstNode: ...
    
    @property
    def ReturnType(self) -> XPathResultType: ...
    
    @property
    def Type(self) -> AstType: ...
    
    # ---------- Methods ---------- #
    
    def get_Condition(self) -> AstNode: ...
    
    def get_Input(self) -> AstNode: ...
    
    def get_ReturnType(self) -> XPathResultType: ...
    
    def get_Type(self) -> AstType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Filter(AstNode):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, input: AstNode, condition: AstNode): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Condition(self) -> AstNode: ...
    
    @property
    def Input(self) -> AstNode: ...
    
    @property
    def ReturnType(self) -> XPathResultType: ...
    
    @property
    def Type(self) -> AstType: ...
    
    # ---------- Methods ---------- #
    
    def get_Condition(self) -> AstNode: ...
    
    def get_Input(self) -> AstNode: ...
    
    def get_ReturnType(self) -> XPathResultType: ...
    
    def get_Type(self) -> AstType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class FilterQuery(BaseAxisQuery, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, qyParent: Query, cond: Query, noPosition: BooleanType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Condition(self) -> Query: ...
    
    @property
    def Properties(self) -> QueryProps: ...
    
    # ---------- Methods ---------- #
    
    def Advance(self) -> XPathNavigator: ...
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def MatchNode(self, current: XPathNavigator) -> XPathNavigator: ...
    
    def PrintQuery(self, w: XmlWriter) -> VoidType: ...
    
    def Reset(self) -> VoidType: ...
    
    def SetXsltContext(self, input: XsltContext) -> VoidType: ...
    
    def get_Condition(self) -> Query: ...
    
    def get_Properties(self) -> QueryProps: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class FilterQuery(BaseAxisQuery, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, qyParent: Query, cond: Query, noPosition: BooleanType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Condition(self) -> Query: ...
    
    @property
    def Properties(self) -> QueryProps: ...
    
    # ---------- Methods ---------- #
    
    def Advance(self) -> XPathNavigator: ...
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def MatchNode(self, current: XPathNavigator) -> XPathNavigator: ...
    
    def PrintQuery(self, w: XmlWriter) -> VoidType: ...
    
    def Reset(self) -> VoidType: ...
    
    def SetXsltContext(self, input: XsltContext) -> VoidType: ...
    
    def get_Condition(self) -> Query: ...
    
    def get_Properties(self) -> QueryProps: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class FollSiblingQuery(BaseAxisQuery, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, qyInput: Query, name: StringType, prefix: StringType, type: XPathNodeType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Advance(self) -> XPathNavigator: ...
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def Reset(self) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class FollSiblingQuery(BaseAxisQuery, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, qyInput: Query, name: StringType, prefix: StringType, type: XPathNodeType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Advance(self) -> XPathNavigator: ...
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def Reset(self) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class FollowingQuery(BaseAxisQuery, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, qyInput: Query, name: StringType, prefix: StringType, typeTest: XPathNodeType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Advance(self) -> XPathNavigator: ...
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def Reset(self) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class FollowingQuery(BaseAxisQuery, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, qyInput: Query, name: StringType, prefix: StringType, typeTest: XPathNodeType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Advance(self) -> XPathNavigator: ...
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def Reset(self) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ForwardPositionQuery(CacheOutputQuery, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, input: Query): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def Evaluate(self, context: XPathNodeIterator) -> ObjectType: ...
    
    def MatchNode(self, context: XPathNavigator) -> XPathNavigator: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ForwardPositionQuery(CacheOutputQuery, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, input: Query): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def Evaluate(self, context: XPathNodeIterator) -> ObjectType: ...
    
    def MatchNode(self, context: XPathNavigator) -> XPathNavigator: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Function(AstNode):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, ftype: FunctionType, argumentList: ArrayList): ...
    
    @overload
    def __init__(self, prefix: StringType, name: StringType, argumentList: ArrayList): ...
    
    @overload
    def __init__(self, ftype: FunctionType): ...
    
    @overload
    def __init__(self, ftype: FunctionType, arg: AstNode): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ArgumentList(self) -> ArrayList: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def Prefix(self) -> StringType: ...
    
    @property
    def ReturnType(self) -> XPathResultType: ...
    
    @property
    def Type(self) -> AstType: ...
    
    @property
    def TypeOfFunction(self) -> FunctionType: ...
    
    # ---------- Methods ---------- #
    
    def get_ArgumentList(self) -> ArrayList: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_Prefix(self) -> StringType: ...
    
    def get_ReturnType(self) -> XPathResultType: ...
    
    def get_Type(self) -> AstType: ...
    
    def get_TypeOfFunction(self) -> FunctionType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # ---------- Sub Enums ---------- #
    
    class FunctionType(Enum):
        FuncLast: IntType = 0
        FuncPosition: IntType = 1
        FuncCount: IntType = 2
        FuncID: IntType = 3
        FuncLocalName: IntType = 4
        FuncNameSpaceUri: IntType = 5
        FuncName: IntType = 6
        FuncString: IntType = 7
        FuncBoolean: IntType = 8
        FuncNumber: IntType = 9
        FuncTrue: IntType = 10
        FuncFalse: IntType = 11
        FuncNot: IntType = 12
        FuncConcat: IntType = 13
        FuncStartsWith: IntType = 14
        FuncContains: IntType = 15
        FuncSubstringBefore: IntType = 16
        FuncSubstringAfter: IntType = 17
        FuncSubstring: IntType = 18
        FuncStringLength: IntType = 19
        FuncNormalize: IntType = 20
        FuncTranslate: IntType = 21
        FuncLang: IntType = 22
        FuncSum: IntType = 23
        FuncFloor: IntType = 24
        FuncCeiling: IntType = 25
        FuncRound: IntType = 26
        FuncUserDefined: IntType = 27
    


class Function(AstNode):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, ftype: FunctionType, argumentList: ArrayList): ...
    
    @overload
    def __init__(self, prefix: StringType, name: StringType, argumentList: ArrayList): ...
    
    @overload
    def __init__(self, ftype: FunctionType): ...
    
    @overload
    def __init__(self, ftype: FunctionType, arg: AstNode): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ArgumentList(self) -> ArrayList: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def Prefix(self) -> StringType: ...
    
    @property
    def ReturnType(self) -> XPathResultType: ...
    
    @property
    def Type(self) -> AstType: ...
    
    @property
    def TypeOfFunction(self) -> FunctionType: ...
    
    # ---------- Methods ---------- #
    
    def get_ArgumentList(self) -> ArrayList: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_Prefix(self) -> StringType: ...
    
    def get_ReturnType(self) -> XPathResultType: ...
    
    def get_Type(self) -> AstType: ...
    
    def get_TypeOfFunction(self) -> FunctionType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # ---------- Sub Enums ---------- #
    
    class FunctionType(Enum):
        FuncLast: IntType = 0
        FuncPosition: IntType = 1
        FuncCount: IntType = 2
        FuncID: IntType = 3
        FuncLocalName: IntType = 4
        FuncNameSpaceUri: IntType = 5
        FuncName: IntType = 6
        FuncString: IntType = 7
        FuncBoolean: IntType = 8
        FuncNumber: IntType = 9
        FuncTrue: IntType = 10
        FuncFalse: IntType = 11
        FuncNot: IntType = 12
        FuncConcat: IntType = 13
        FuncStartsWith: IntType = 14
        FuncContains: IntType = 15
        FuncSubstringBefore: IntType = 16
        FuncSubstringAfter: IntType = 17
        FuncSubstring: IntType = 18
        FuncStringLength: IntType = 19
        FuncNormalize: IntType = 20
        FuncTranslate: IntType = 21
        FuncLang: IntType = 22
        FuncSum: IntType = 23
        FuncFloor: IntType = 24
        FuncCeiling: IntType = 25
        FuncRound: IntType = 26
        FuncUserDefined: IntType = 27
    


class FunctionQuery(ExtensionQuery, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, prefix: StringType, name: StringType, args: List[Query]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def StaticType(self) -> XPathResultType: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def Evaluate(self, nodeIterator: XPathNodeIterator) -> ObjectType: ...
    
    def MatchNode(self, navigator: XPathNavigator) -> XPathNavigator: ...
    
    def PrintQuery(self, w: XmlWriter) -> VoidType: ...
    
    def SetXsltContext(self, context: XsltContext) -> VoidType: ...
    
    def get_StaticType(self) -> XPathResultType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class FunctionQuery(ExtensionQuery, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, prefix: StringType, name: StringType, args: List[Query]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def StaticType(self) -> XPathResultType: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def Evaluate(self, nodeIterator: XPathNodeIterator) -> ObjectType: ...
    
    def MatchNode(self, navigator: XPathNavigator) -> XPathNavigator: ...
    
    def PrintQuery(self, w: XmlWriter) -> VoidType: ...
    
    def SetXsltContext(self, context: XsltContext) -> VoidType: ...
    
    def get_StaticType(self) -> XPathResultType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Group(AstNode):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, groupNode: AstNode): ...
    
    # ---------- Properties ---------- #
    
    @property
    def GroupNode(self) -> AstNode: ...
    
    @property
    def ReturnType(self) -> XPathResultType: ...
    
    @property
    def Type(self) -> AstType: ...
    
    # ---------- Methods ---------- #
    
    def get_GroupNode(self) -> AstNode: ...
    
    def get_ReturnType(self) -> XPathResultType: ...
    
    def get_Type(self) -> AstType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Group(AstNode):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, groupNode: AstNode): ...
    
    # ---------- Properties ---------- #
    
    @property
    def GroupNode(self) -> AstNode: ...
    
    @property
    def ReturnType(self) -> XPathResultType: ...
    
    @property
    def Type(self) -> AstType: ...
    
    # ---------- Methods ---------- #
    
    def get_GroupNode(self) -> AstNode: ...
    
    def get_ReturnType(self) -> XPathResultType: ...
    
    def get_Type(self) -> AstType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class GroupQuery(BaseAxisQuery, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, qy: Query): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Properties(self) -> QueryProps: ...
    
    @property
    def StaticType(self) -> XPathResultType: ...
    
    # ---------- Methods ---------- #
    
    def Advance(self) -> XPathNavigator: ...
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def Evaluate(self, nodeIterator: XPathNodeIterator) -> ObjectType: ...
    
    def get_Properties(self) -> QueryProps: ...
    
    def get_StaticType(self) -> XPathResultType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class GroupQuery(BaseAxisQuery, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, qy: Query): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Properties(self) -> QueryProps: ...
    
    @property
    def StaticType(self) -> XPathResultType: ...
    
    # ---------- Methods ---------- #
    
    def Advance(self) -> XPathNavigator: ...
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def Evaluate(self, nodeIterator: XPathNodeIterator) -> ObjectType: ...
    
    def get_Properties(self) -> QueryProps: ...
    
    def get_StaticType(self) -> XPathResultType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class IDQuery(CacheOutputQuery, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, arg: Query): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def Evaluate(self, context: XPathNodeIterator) -> ObjectType: ...
    
    def MatchNode(self, context: XPathNavigator) -> XPathNavigator: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class IDQuery(CacheOutputQuery, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, arg: Query): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def Evaluate(self, context: XPathNodeIterator) -> ObjectType: ...
    
    def MatchNode(self, context: XPathNavigator) -> XPathNavigator: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class IteratorFilter(XPathNodeIterator, ICloneable, IEnumerable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Current(self) -> XPathNavigator: ...
    
    @property
    def CurrentPosition(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def MoveNext(self) -> BooleanType: ...
    
    def get_Current(self) -> XPathNavigator: ...
    
    def get_CurrentPosition(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class IteratorFilter(XPathNodeIterator, ICloneable, IEnumerable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Current(self) -> XPathNavigator: ...
    
    @property
    def CurrentPosition(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def MoveNext(self) -> BooleanType: ...
    
    def get_Current(self) -> XPathNavigator: ...
    
    def get_CurrentPosition(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class LogicalExpr(ValueQuery, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, op: Op, opnd1: Query, opnd2: Query): ...
    
    # ---------- Properties ---------- #
    
    @property
    def StaticType(self) -> XPathResultType: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def Evaluate(self, nodeIterator: XPathNodeIterator) -> ObjectType: ...
    
    def PrintQuery(self, w: XmlWriter) -> VoidType: ...
    
    def SetXsltContext(self, context: XsltContext) -> VoidType: ...
    
    def get_StaticType(self) -> XPathResultType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class LogicalExpr(ValueQuery, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, op: Op, opnd1: Query, opnd2: Query): ...
    
    # ---------- Properties ---------- #
    
    @property
    def StaticType(self) -> XPathResultType: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def Evaluate(self, nodeIterator: XPathNodeIterator) -> ObjectType: ...
    
    def PrintQuery(self, w: XmlWriter) -> VoidType: ...
    
    def SetXsltContext(self, context: XsltContext) -> VoidType: ...
    
    def get_StaticType(self) -> XPathResultType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MergeFilterQuery(CacheOutputQuery, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, input: Query, child: Query): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def Evaluate(self, nodeIterator: XPathNodeIterator) -> ObjectType: ...
    
    def MatchNode(self, current: XPathNavigator) -> XPathNavigator: ...
    
    def PrintQuery(self, w: XmlWriter) -> VoidType: ...
    
    def SetXsltContext(self, xsltContext: XsltContext) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MergeFilterQuery(CacheOutputQuery, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, input: Query, child: Query): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def Evaluate(self, nodeIterator: XPathNodeIterator) -> ObjectType: ...
    
    def MatchNode(self, current: XPathNavigator) -> XPathNavigator: ...
    
    def PrintQuery(self, w: XmlWriter) -> VoidType: ...
    
    def SetXsltContext(self, xsltContext: XsltContext) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class NamespaceQuery(BaseAxisQuery, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, qyParent: Query, Name: StringType, Prefix: StringType, Type: XPathNodeType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Advance(self) -> XPathNavigator: ...
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def Reset(self) -> VoidType: ...
    
    def matches(self, e: XPathNavigator) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class NamespaceQuery(BaseAxisQuery, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, qyParent: Query, Name: StringType, Prefix: StringType, Type: XPathNodeType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Advance(self) -> XPathNavigator: ...
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def Reset(self) -> VoidType: ...
    
    def matches(self, e: XPathNavigator) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class NodeFunctions(ValueQuery, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, funcType: FunctionType, arg: Query): ...
    
    # ---------- Properties ---------- #
    
    @property
    def StaticType(self) -> XPathResultType: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def Evaluate(self, context: XPathNodeIterator) -> ObjectType: ...
    
    def PrintQuery(self, w: XmlWriter) -> VoidType: ...
    
    def SetXsltContext(self, context: XsltContext) -> VoidType: ...
    
    def get_StaticType(self) -> XPathResultType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class NodeFunctions(ValueQuery, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, funcType: FunctionType, arg: Query): ...
    
    # ---------- Properties ---------- #
    
    @property
    def StaticType(self) -> XPathResultType: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def Evaluate(self, context: XPathNodeIterator) -> ObjectType: ...
    
    def PrintQuery(self, w: XmlWriter) -> VoidType: ...
    
    def SetXsltContext(self, context: XsltContext) -> VoidType: ...
    
    def get_StaticType(self) -> XPathResultType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class NumberFunctions(ValueQuery, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, ftype: FunctionType, arg: Query): ...
    
    # ---------- Properties ---------- #
    
    @property
    def StaticType(self) -> XPathResultType: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def Evaluate(self, nodeIterator: XPathNodeIterator) -> ObjectType: ...
    
    def PrintQuery(self, w: XmlWriter) -> VoidType: ...
    
    def SetXsltContext(self, context: XsltContext) -> VoidType: ...
    
    def get_StaticType(self) -> XPathResultType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class NumberFunctions(ValueQuery, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, ftype: FunctionType, arg: Query): ...
    
    # ---------- Properties ---------- #
    
    @property
    def StaticType(self) -> XPathResultType: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def Evaluate(self, nodeIterator: XPathNodeIterator) -> ObjectType: ...
    
    def PrintQuery(self, w: XmlWriter) -> VoidType: ...
    
    def SetXsltContext(self, context: XsltContext) -> VoidType: ...
    
    def get_StaticType(self) -> XPathResultType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class NumericExpr(ValueQuery, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, op: Op, opnd1: Query, opnd2: Query): ...
    
    # ---------- Properties ---------- #
    
    @property
    def StaticType(self) -> XPathResultType: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def Evaluate(self, nodeIterator: XPathNodeIterator) -> ObjectType: ...
    
    def PrintQuery(self, w: XmlWriter) -> VoidType: ...
    
    def SetXsltContext(self, context: XsltContext) -> VoidType: ...
    
    def get_StaticType(self) -> XPathResultType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class NumericExpr(ValueQuery, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, op: Op, opnd1: Query, opnd2: Query): ...
    
    # ---------- Properties ---------- #
    
    @property
    def StaticType(self) -> XPathResultType: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def Evaluate(self, nodeIterator: XPathNodeIterator) -> ObjectType: ...
    
    def PrintQuery(self, w: XmlWriter) -> VoidType: ...
    
    def SetXsltContext(self, context: XsltContext) -> VoidType: ...
    
    def get_StaticType(self) -> XPathResultType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Operand(AstNode):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, val: StringType): ...
    
    @overload
    def __init__(self, val: DoubleType): ...
    
    @overload
    def __init__(self, val: BooleanType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def OperandValue(self) -> ObjectType: ...
    
    @property
    def ReturnType(self) -> XPathResultType: ...
    
    @property
    def Type(self) -> AstType: ...
    
    # ---------- Methods ---------- #
    
    def get_OperandValue(self) -> ObjectType: ...
    
    def get_ReturnType(self) -> XPathResultType: ...
    
    def get_Type(self) -> AstType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Operand(AstNode):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, val: StringType): ...
    
    @overload
    def __init__(self, val: DoubleType): ...
    
    @overload
    def __init__(self, val: BooleanType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def OperandValue(self) -> ObjectType: ...
    
    @property
    def ReturnType(self) -> XPathResultType: ...
    
    @property
    def Type(self) -> AstType: ...
    
    # ---------- Methods ---------- #
    
    def get_OperandValue(self) -> ObjectType: ...
    
    def get_ReturnType(self) -> XPathResultType: ...
    
    def get_Type(self) -> AstType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class OperandQuery(ValueQuery, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, val: ObjectType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def StaticType(self) -> XPathResultType: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def Evaluate(self, nodeIterator: XPathNodeIterator) -> ObjectType: ...
    
    def PrintQuery(self, w: XmlWriter) -> VoidType: ...
    
    def get_StaticType(self) -> XPathResultType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class OperandQuery(ValueQuery, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, val: ObjectType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def StaticType(self) -> XPathResultType: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def Evaluate(self, nodeIterator: XPathNodeIterator) -> ObjectType: ...
    
    def PrintQuery(self, w: XmlWriter) -> VoidType: ...
    
    def get_StaticType(self) -> XPathResultType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Operator(AstNode):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, op: Op, opnd1: AstNode, opnd2: AstNode): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Operand1(self) -> AstNode: ...
    
    @property
    def Operand2(self) -> AstNode: ...
    
    @property
    def OperatorType(self) -> Op: ...
    
    @property
    def ReturnType(self) -> XPathResultType: ...
    
    @property
    def Type(self) -> AstType: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def InvertOperator(op: Op) -> Op: ...
    
    def get_Operand1(self) -> AstNode: ...
    
    def get_Operand2(self) -> AstNode: ...
    
    def get_OperatorType(self) -> Op: ...
    
    def get_ReturnType(self) -> XPathResultType: ...
    
    def get_Type(self) -> AstType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # ---------- Sub Enums ---------- #
    
    class Op(Enum):
        INVALID: IntType = 0
        OR: IntType = 1
        AND: IntType = 2
        EQ: IntType = 3
        NE: IntType = 4
        LT: IntType = 5
        LE: IntType = 6
        GT: IntType = 7
        GE: IntType = 8
        PLUS: IntType = 9
        MINUS: IntType = 10
        MUL: IntType = 11
        DIV: IntType = 12
        MOD: IntType = 13
        UNION: IntType = 14
    


class Operator(AstNode):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, op: Op, opnd1: AstNode, opnd2: AstNode): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Operand1(self) -> AstNode: ...
    
    @property
    def Operand2(self) -> AstNode: ...
    
    @property
    def OperatorType(self) -> Op: ...
    
    @property
    def ReturnType(self) -> XPathResultType: ...
    
    @property
    def Type(self) -> AstType: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def InvertOperator(op: Op) -> Op: ...
    
    def get_Operand1(self) -> AstNode: ...
    
    def get_Operand2(self) -> AstNode: ...
    
    def get_OperatorType(self) -> Op: ...
    
    def get_ReturnType(self) -> XPathResultType: ...
    
    def get_Type(self) -> AstType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # ---------- Sub Enums ---------- #
    
    class Op(Enum):
        INVALID: IntType = 0
        OR: IntType = 1
        AND: IntType = 2
        EQ: IntType = 3
        NE: IntType = 4
        LT: IntType = 5
        LE: IntType = 6
        GT: IntType = 7
        GE: IntType = 8
        PLUS: IntType = 9
        MINUS: IntType = 10
        MUL: IntType = 11
        DIV: IntType = 12
        MOD: IntType = 13
        UNION: IntType = 14
    


class ParentQuery(CacheAxisQuery, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, qyInput: Query, Name: StringType, Prefix: StringType, Type: XPathNodeType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def Evaluate(self, context: XPathNodeIterator) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ParentQuery(CacheAxisQuery, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, qyInput: Query, Name: StringType, Prefix: StringType, Type: XPathNodeType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def Evaluate(self, context: XPathNodeIterator) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PreSiblingQuery(CacheAxisQuery, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, qyInput: Query, name: StringType, prefix: StringType, typeTest: XPathNodeType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Properties(self) -> QueryProps: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def Evaluate(self, context: XPathNodeIterator) -> ObjectType: ...
    
    def get_Properties(self) -> QueryProps: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PreSiblingQuery(CacheAxisQuery, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, qyInput: Query, name: StringType, prefix: StringType, typeTest: XPathNodeType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Properties(self) -> QueryProps: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def Evaluate(self, context: XPathNodeIterator) -> ObjectType: ...
    
    def get_Properties(self) -> QueryProps: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PrecedingQuery(BaseAxisQuery, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, qyInput: Query, name: StringType, prefix: StringType, typeTest: XPathNodeType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Properties(self) -> QueryProps: ...
    
    # ---------- Methods ---------- #
    
    def Advance(self) -> XPathNavigator: ...
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Properties(self) -> QueryProps: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PrecedingQuery(BaseAxisQuery, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, qyInput: Query, name: StringType, prefix: StringType, typeTest: XPathNodeType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Properties(self) -> QueryProps: ...
    
    # ---------- Methods ---------- #
    
    def Advance(self) -> XPathNavigator: ...
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Properties(self) -> QueryProps: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Query(ABC, ResetableIterator, ICloneable, IEnumerable):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def XPathResultType_Navigator() -> XPathResultType: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def Properties(self) -> QueryProps: ...
    
    @property
    def StaticType(self) -> XPathResultType: ...
    
    @property
    def XsltDefaultPriority(self) -> DoubleType: ...
    
    # ---------- Methods ---------- #
    
    def Advance(self) -> XPathNavigator: ...
    
    @staticmethod
    def AssertQuery(query: Query) -> VoidType: ...
    
    @staticmethod
    @overload
    def Clone(input: Query) -> Query: ...
    
    @staticmethod
    def CompareNodes(l: XPathNavigator, r: XPathNavigator) -> XmlNodeOrder: ...
    
    def Evaluate(self, nodeIterator: XPathNodeIterator) -> ObjectType: ...
    
    def Insert(self, buffer: List[XPathNavigator], nav: XPathNavigator) -> BooleanType: ...
    
    def MatchNode(self, current: XPathNavigator) -> XPathNavigator: ...
    
    def MoveNext(self) -> BooleanType: ...
    
    def PrintQuery(self, w: XmlWriter) -> VoidType: ...
    
    def SetXsltContext(self, context: XsltContext) -> VoidType: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_Properties(self) -> QueryProps: ...
    
    def get_StaticType(self) -> XPathResultType: ...
    
    def get_XsltDefaultPriority(self) -> DoubleType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Query(ABC, ResetableIterator, ICloneable, IEnumerable):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def XPathResultType_Navigator() -> XPathResultType: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def Properties(self) -> QueryProps: ...
    
    @property
    def StaticType(self) -> XPathResultType: ...
    
    @property
    def XsltDefaultPriority(self) -> DoubleType: ...
    
    # ---------- Methods ---------- #
    
    def Advance(self) -> XPathNavigator: ...
    
    @staticmethod
    def AssertQuery(query: Query) -> VoidType: ...
    
    @staticmethod
    @overload
    def Clone(input: Query) -> Query: ...
    
    @staticmethod
    def CompareNodes(l: XPathNavigator, r: XPathNavigator) -> XmlNodeOrder: ...
    
    def Evaluate(self, nodeIterator: XPathNodeIterator) -> ObjectType: ...
    
    def Insert(self, buffer: List[XPathNavigator], nav: XPathNavigator) -> BooleanType: ...
    
    def MatchNode(self, current: XPathNavigator) -> XPathNavigator: ...
    
    def MoveNext(self) -> BooleanType: ...
    
    def PrintQuery(self, w: XmlWriter) -> VoidType: ...
    
    def SetXsltContext(self, context: XsltContext) -> VoidType: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_Properties(self) -> QueryProps: ...
    
    def get_StaticType(self) -> XPathResultType: ...
    
    def get_XsltDefaultPriority(self) -> DoubleType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class QueryBuilder(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class QueryBuilder(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ResetableIterator(ABC, XPathNodeIterator, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CurrentPosition(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def MoveToPosition(self, pos: IntType) -> BooleanType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_CurrentPosition(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ResetableIterator(ABC, XPathNodeIterator, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CurrentPosition(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def MoveToPosition(self, pos: IntType) -> BooleanType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_CurrentPosition(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ReversePositionQuery(ForwardPositionQuery, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, input: Query): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CurrentPosition(self) -> IntType: ...
    
    @property
    def Properties(self) -> QueryProps: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def get_CurrentPosition(self) -> IntType: ...
    
    def get_Properties(self) -> QueryProps: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ReversePositionQuery(ForwardPositionQuery, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, input: Query): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CurrentPosition(self) -> IntType: ...
    
    @property
    def Properties(self) -> QueryProps: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def get_CurrentPosition(self) -> IntType: ...
    
    def get_Properties(self) -> QueryProps: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Root(AstNode):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ReturnType(self) -> XPathResultType: ...
    
    @property
    def Type(self) -> AstType: ...
    
    # ---------- Methods ---------- #
    
    def get_ReturnType(self) -> XPathResultType: ...
    
    def get_Type(self) -> AstType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Root(AstNode):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ReturnType(self) -> XPathResultType: ...
    
    @property
    def Type(self) -> AstType: ...
    
    # ---------- Methods ---------- #
    
    def get_ReturnType(self) -> XPathResultType: ...
    
    def get_Type(self) -> AstType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SortKey(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, numKeys: IntType, originalPosition: IntType, node: XPathNavigator): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Item(self) -> ObjectType: ...
    
    @Item.setter
    def Item(self, value: ObjectType) -> None: ...
    
    @property
    def Node(self) -> XPathNavigator: ...
    
    @property
    def NumKeys(self) -> IntType: ...
    
    @property
    def OriginalPosition(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def get_Item(self, index: IntType) -> ObjectType: ...
    
    def get_Node(self) -> XPathNavigator: ...
    
    def get_NumKeys(self) -> IntType: ...
    
    def get_OriginalPosition(self) -> IntType: ...
    
    def set_Item(self, index: IntType, value: ObjectType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SortKey(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, numKeys: IntType, originalPosition: IntType, node: XPathNavigator): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Item(self) -> ObjectType: ...
    
    @Item.setter
    def Item(self, value: ObjectType) -> None: ...
    
    @property
    def Node(self) -> XPathNavigator: ...
    
    @property
    def NumKeys(self) -> IntType: ...
    
    @property
    def OriginalPosition(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def get_Item(self, index: IntType) -> ObjectType: ...
    
    def get_Node(self) -> XPathNavigator: ...
    
    def get_NumKeys(self) -> IntType: ...
    
    def get_OriginalPosition(self) -> IntType: ...
    
    def set_Item(self, index: IntType, value: ObjectType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SortQuery(Query, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, qyInput: Query): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def Current(self) -> XPathNavigator: ...
    
    @property
    def CurrentPosition(self) -> IntType: ...
    
    @property
    def Properties(self) -> QueryProps: ...
    
    @property
    def StaticType(self) -> XPathResultType: ...
    
    # ---------- Methods ---------- #
    
    def Advance(self) -> XPathNavigator: ...
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def Evaluate(self, context: XPathNodeIterator) -> ObjectType: ...
    
    def PrintQuery(self, w: XmlWriter) -> VoidType: ...
    
    def Reset(self) -> VoidType: ...
    
    def SetXsltContext(self, xsltContext: XsltContext) -> VoidType: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_Current(self) -> XPathNavigator: ...
    
    def get_CurrentPosition(self) -> IntType: ...
    
    def get_Properties(self) -> QueryProps: ...
    
    def get_StaticType(self) -> XPathResultType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SortQuery(Query, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, qyInput: Query): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def Current(self) -> XPathNavigator: ...
    
    @property
    def CurrentPosition(self) -> IntType: ...
    
    @property
    def Properties(self) -> QueryProps: ...
    
    @property
    def StaticType(self) -> XPathResultType: ...
    
    # ---------- Methods ---------- #
    
    def Advance(self) -> XPathNavigator: ...
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def Evaluate(self, context: XPathNodeIterator) -> ObjectType: ...
    
    def PrintQuery(self, w: XmlWriter) -> VoidType: ...
    
    def Reset(self) -> VoidType: ...
    
    def SetXsltContext(self, xsltContext: XsltContext) -> VoidType: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_Current(self) -> XPathNavigator: ...
    
    def get_CurrentPosition(self) -> IntType: ...
    
    def get_Properties(self) -> QueryProps: ...
    
    def get_StaticType(self) -> XPathResultType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class StringFunctions(ValueQuery, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, funcType: FunctionType, argList: IList[Query]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def StaticType(self) -> XPathResultType: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def Evaluate(self, nodeIterator: XPathNodeIterator) -> ObjectType: ...
    
    def PrintQuery(self, w: XmlWriter) -> VoidType: ...
    
    def SetXsltContext(self, context: XsltContext) -> VoidType: ...
    
    def get_StaticType(self) -> XPathResultType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class StringFunctions(ValueQuery, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, funcType: FunctionType, argList: IList[Query]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def StaticType(self) -> XPathResultType: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def Evaluate(self, nodeIterator: XPathNodeIterator) -> ObjectType: ...
    
    def PrintQuery(self, w: XmlWriter) -> VoidType: ...
    
    def SetXsltContext(self, context: XsltContext) -> VoidType: ...
    
    def get_StaticType(self) -> XPathResultType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UnionExpr(Query, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, query1: Query, query2: Query): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Current(self) -> XPathNavigator: ...
    
    @property
    def CurrentPosition(self) -> IntType: ...
    
    @property
    def StaticType(self) -> XPathResultType: ...
    
    # ---------- Methods ---------- #
    
    def Advance(self) -> XPathNavigator: ...
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def Evaluate(self, context: XPathNodeIterator) -> ObjectType: ...
    
    def MatchNode(self, xsltContext: XPathNavigator) -> XPathNavigator: ...
    
    def PrintQuery(self, w: XmlWriter) -> VoidType: ...
    
    def Reset(self) -> VoidType: ...
    
    def SetXsltContext(self, xsltContext: XsltContext) -> VoidType: ...
    
    def get_Current(self) -> XPathNavigator: ...
    
    def get_CurrentPosition(self) -> IntType: ...
    
    def get_StaticType(self) -> XPathResultType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UnionExpr(Query, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, query1: Query, query2: Query): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Current(self) -> XPathNavigator: ...
    
    @property
    def CurrentPosition(self) -> IntType: ...
    
    @property
    def StaticType(self) -> XPathResultType: ...
    
    # ---------- Methods ---------- #
    
    def Advance(self) -> XPathNavigator: ...
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def Evaluate(self, context: XPathNodeIterator) -> ObjectType: ...
    
    def MatchNode(self, xsltContext: XPathNavigator) -> XPathNavigator: ...
    
    def PrintQuery(self, w: XmlWriter) -> VoidType: ...
    
    def Reset(self) -> VoidType: ...
    
    def SetXsltContext(self, xsltContext: XsltContext) -> VoidType: ...
    
    def get_Current(self) -> XPathNavigator: ...
    
    def get_CurrentPosition(self) -> IntType: ...
    
    def get_StaticType(self) -> XPathResultType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ValueQuery(ABC, Query, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def Current(self) -> XPathNavigator: ...
    
    @property
    def CurrentPosition(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def Advance(self) -> XPathNavigator: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_Current(self) -> XPathNavigator: ...
    
    def get_CurrentPosition(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ValueQuery(ABC, Query, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def Current(self) -> XPathNavigator: ...
    
    @property
    def CurrentPosition(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def Advance(self) -> XPathNavigator: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_Current(self) -> XPathNavigator: ...
    
    def get_CurrentPosition(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Variable(AstNode):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, name: StringType, prefix: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Localname(self) -> StringType: ...
    
    @property
    def Prefix(self) -> StringType: ...
    
    @property
    def ReturnType(self) -> XPathResultType: ...
    
    @property
    def Type(self) -> AstType: ...
    
    # ---------- Methods ---------- #
    
    def get_Localname(self) -> StringType: ...
    
    def get_Prefix(self) -> StringType: ...
    
    def get_ReturnType(self) -> XPathResultType: ...
    
    def get_Type(self) -> AstType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Variable(AstNode):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, name: StringType, prefix: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Localname(self) -> StringType: ...
    
    @property
    def Prefix(self) -> StringType: ...
    
    @property
    def ReturnType(self) -> XPathResultType: ...
    
    @property
    def Type(self) -> AstType: ...
    
    # ---------- Methods ---------- #
    
    def get_Localname(self) -> StringType: ...
    
    def get_Prefix(self) -> StringType: ...
    
    def get_ReturnType(self) -> XPathResultType: ...
    
    def get_Type(self) -> AstType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class VariableQuery(ExtensionQuery, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, name: StringType, prefix: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def StaticType(self) -> XPathResultType: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def Evaluate(self, nodeIterator: XPathNodeIterator) -> ObjectType: ...
    
    def PrintQuery(self, w: XmlWriter) -> VoidType: ...
    
    def SetXsltContext(self, context: XsltContext) -> VoidType: ...
    
    def get_StaticType(self) -> XPathResultType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class VariableQuery(ExtensionQuery, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, name: StringType, prefix: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def StaticType(self) -> XPathResultType: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def Evaluate(self, nodeIterator: XPathNodeIterator) -> ObjectType: ...
    
    def PrintQuery(self, w: XmlWriter) -> VoidType: ...
    
    def SetXsltContext(self, context: XsltContext) -> VoidType: ...
    
    def get_StaticType(self) -> XPathResultType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XPathAncestorIterator(XPathAxisIterator, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, nav: XPathNavigator, type: XPathNodeType, matchSelf: BooleanType): ...
    
    @overload
    def __init__(self, nav: XPathNavigator, name: StringType, namespaceURI: StringType, matchSelf: BooleanType): ...
    
    @overload
    def __init__(self, other: XPathAncestorIterator): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def MoveNext(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XPathAncestorIterator(XPathAxisIterator, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, nav: XPathNavigator, type: XPathNodeType, matchSelf: BooleanType): ...
    
    @overload
    def __init__(self, nav: XPathNavigator, name: StringType, namespaceURI: StringType, matchSelf: BooleanType): ...
    
    @overload
    def __init__(self, other: XPathAncestorIterator): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def MoveNext(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XPathAncestorQuery(CacheAxisQuery, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, qyInput: Query, name: StringType, prefix: StringType, typeTest: XPathNodeType, matchSelf: BooleanType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CurrentPosition(self) -> IntType: ...
    
    @property
    def Properties(self) -> QueryProps: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def Evaluate(self, context: XPathNodeIterator) -> ObjectType: ...
    
    def PrintQuery(self, w: XmlWriter) -> VoidType: ...
    
    def get_CurrentPosition(self) -> IntType: ...
    
    def get_Properties(self) -> QueryProps: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XPathAncestorQuery(CacheAxisQuery, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, qyInput: Query, name: StringType, prefix: StringType, typeTest: XPathNodeType, matchSelf: BooleanType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CurrentPosition(self) -> IntType: ...
    
    @property
    def Properties(self) -> QueryProps: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def Evaluate(self, context: XPathNodeIterator) -> ObjectType: ...
    
    def PrintQuery(self, w: XmlWriter) -> VoidType: ...
    
    def get_CurrentPosition(self) -> IntType: ...
    
    def get_Properties(self) -> QueryProps: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XPathArrayIterator(ResetableIterator, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, list: IList): ...
    
    @overload
    def __init__(self, it: XPathArrayIterator): ...
    
    @overload
    def __init__(self, nodeIterator: XPathNodeIterator): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AsList(self) -> IList: ...
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def Current(self) -> XPathNavigator: ...
    
    @property
    def CurrentPosition(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def GetEnumerator(self) -> IEnumerator: ...
    
    def MoveNext(self) -> BooleanType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_AsList(self) -> IList: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_Current(self) -> XPathNavigator: ...
    
    def get_CurrentPosition(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XPathArrayIterator(ResetableIterator, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, list: IList): ...
    
    @overload
    def __init__(self, it: XPathArrayIterator): ...
    
    @overload
    def __init__(self, nodeIterator: XPathNodeIterator): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AsList(self) -> IList: ...
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def Current(self) -> XPathNavigator: ...
    
    @property
    def CurrentPosition(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def GetEnumerator(self) -> IEnumerator: ...
    
    def MoveNext(self) -> BooleanType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_AsList(self) -> IList: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_Current(self) -> XPathNavigator: ...
    
    def get_CurrentPosition(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XPathAxisIterator(ABC, XPathNodeIterator, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, nav: XPathNavigator, matchSelf: BooleanType): ...
    
    @overload
    def __init__(self, nav: XPathNavigator, type: XPathNodeType, matchSelf: BooleanType): ...
    
    @overload
    def __init__(self, nav: XPathNavigator, name: StringType, namespaceURI: StringType, matchSelf: BooleanType): ...
    
    @overload
    def __init__(self, it: XPathAxisIterator): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Current(self) -> XPathNavigator: ...
    
    @property
    def CurrentPosition(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def get_Current(self) -> XPathNavigator: ...
    
    def get_CurrentPosition(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XPathAxisIterator(ABC, XPathNodeIterator, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, nav: XPathNavigator, matchSelf: BooleanType): ...
    
    @overload
    def __init__(self, nav: XPathNavigator, type: XPathNodeType, matchSelf: BooleanType): ...
    
    @overload
    def __init__(self, nav: XPathNavigator, name: StringType, namespaceURI: StringType, matchSelf: BooleanType): ...
    
    @overload
    def __init__(self, it: XPathAxisIterator): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Current(self) -> XPathNavigator: ...
    
    @property
    def CurrentPosition(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def get_Current(self) -> XPathNavigator: ...
    
    def get_CurrentPosition(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XPathChildIterator(XPathAxisIterator, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, nav: XPathNavigator, type: XPathNodeType): ...
    
    @overload
    def __init__(self, nav: XPathNavigator, name: StringType, namespaceURI: StringType): ...
    
    @overload
    def __init__(self, it: XPathChildIterator): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def MoveNext(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XPathChildIterator(XPathAxisIterator, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, nav: XPathNavigator, type: XPathNodeType): ...
    
    @overload
    def __init__(self, nav: XPathNavigator, name: StringType, namespaceURI: StringType): ...
    
    @overload
    def __init__(self, it: XPathChildIterator): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def MoveNext(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XPathComparerHelper(ObjectType, IComparer):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, order: XmlSortOrder, caseOrder: XmlCaseOrder, lang: StringType, dataType: XmlDataType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Compare(self, x: ObjectType, y: ObjectType) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XPathComparerHelper(ObjectType, IComparer):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, order: XmlSortOrder, caseOrder: XmlCaseOrder, lang: StringType, dataType: XmlDataType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Compare(self, x: ObjectType, y: ObjectType) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XPathDescendantIterator(XPathAxisIterator, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, nav: XPathNavigator, type: XPathNodeType, matchSelf: BooleanType): ...
    
    @overload
    def __init__(self, nav: XPathNavigator, name: StringType, namespaceURI: StringType, matchSelf: BooleanType): ...
    
    @overload
    def __init__(self, it: XPathDescendantIterator): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def MoveNext(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XPathDescendantIterator(XPathAxisIterator, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, nav: XPathNavigator, type: XPathNodeType, matchSelf: BooleanType): ...
    
    @overload
    def __init__(self, nav: XPathNavigator, name: StringType, namespaceURI: StringType, matchSelf: BooleanType): ...
    
    @overload
    def __init__(self, it: XPathDescendantIterator): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def MoveNext(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XPathEmptyIterator(ResetableIterator, ICloneable, IEnumerable):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Instance() -> XPathEmptyIterator: ...
    
    @staticmethod
    @Instance.setter
    def Instance(value: XPathEmptyIterator) -> None: ...
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def Current(self) -> XPathNavigator: ...
    
    @property
    def CurrentPosition(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def MoveNext(self) -> BooleanType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_Current(self) -> XPathNavigator: ...
    
    def get_CurrentPosition(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XPathEmptyIterator(ResetableIterator, ICloneable, IEnumerable):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Instance() -> XPathEmptyIterator: ...
    
    @staticmethod
    @Instance.setter
    def Instance(value: XPathEmptyIterator) -> None: ...
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def Current(self) -> XPathNavigator: ...
    
    @property
    def CurrentPosition(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def MoveNext(self) -> BooleanType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_Current(self) -> XPathNavigator: ...
    
    def get_CurrentPosition(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XPathMultyIterator(ResetableIterator, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, inputArray: ArrayList): ...
    
    @overload
    def __init__(self, it: XPathMultyIterator): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Current(self) -> XPathNavigator: ...
    
    @property
    def CurrentPosition(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def MoveNext(self) -> BooleanType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Current(self) -> XPathNavigator: ...
    
    def get_CurrentPosition(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XPathMultyIterator(ResetableIterator, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, inputArray: ArrayList): ...
    
    @overload
    def __init__(self, it: XPathMultyIterator): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Current(self) -> XPathNavigator: ...
    
    @property
    def CurrentPosition(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def MoveNext(self) -> BooleanType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Current(self) -> XPathNavigator: ...
    
    def get_CurrentPosition(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XPathParser(ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def ParseXPathExpresion(xpathExpresion: StringType) -> AstNode: ...
    
    @staticmethod
    def ParseXPathPattern(xpathPattern: StringType) -> AstNode: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XPathParser(ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def ParseXPathExpresion(xpathExpresion: StringType) -> AstNode: ...
    
    @staticmethod
    def ParseXPathPattern(xpathPattern: StringType) -> AstNode: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XPathScanner(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, xpathExpr: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CanBeFunction(self) -> BooleanType: ...
    
    @property
    def Kind(self) -> LexKind: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def NumberValue(self) -> DoubleType: ...
    
    @property
    def Prefix(self) -> StringType: ...
    
    @property
    def SourceText(self) -> StringType: ...
    
    @property
    def StringValue(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def NextLex(self) -> BooleanType: ...
    
    def get_CanBeFunction(self) -> BooleanType: ...
    
    def get_Kind(self) -> LexKind: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_NumberValue(self) -> DoubleType: ...
    
    def get_Prefix(self) -> StringType: ...
    
    def get_SourceText(self) -> StringType: ...
    
    def get_StringValue(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # ---------- Sub Enums ---------- #
    
    class LexKind(Enum):
        Bang: IntType = 33
        Quote: IntType = 34
        Dollar: IntType = 36
        Apos: IntType = 39
        LParens: IntType = 40
        RParens: IntType = 41
        Star: IntType = 42
        Plus: IntType = 43
        Comma: IntType = 44
        Minus: IntType = 45
        Dot: IntType = 46
        Slash: IntType = 47
        Lt: IntType = 60
        Eq: IntType = 61
        Gt: IntType = 62
        At: IntType = 64
        And: IntType = 65
        DotDot: IntType = 68
        Eof: IntType = 69
        Ge: IntType = 71
        Le: IntType = 76
        Ne: IntType = 78
        Or: IntType = 79
        SlashSlash: IntType = 83
        LBracket: IntType = 91
        RBracket: IntType = 93
        Axe: IntType = 97
        Number: IntType = 100
        Name: IntType = 110
        String: IntType = 115
        Union: IntType = 124
    


class XPathScanner(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, xpathExpr: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CanBeFunction(self) -> BooleanType: ...
    
    @property
    def Kind(self) -> LexKind: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def NumberValue(self) -> DoubleType: ...
    
    @property
    def Prefix(self) -> StringType: ...
    
    @property
    def SourceText(self) -> StringType: ...
    
    @property
    def StringValue(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def NextLex(self) -> BooleanType: ...
    
    def get_CanBeFunction(self) -> BooleanType: ...
    
    def get_Kind(self) -> LexKind: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_NumberValue(self) -> DoubleType: ...
    
    def get_Prefix(self) -> StringType: ...
    
    def get_SourceText(self) -> StringType: ...
    
    def get_StringValue(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # ---------- Sub Enums ---------- #
    
    class LexKind(Enum):
        Bang: IntType = 33
        Quote: IntType = 34
        Dollar: IntType = 36
        Apos: IntType = 39
        LParens: IntType = 40
        RParens: IntType = 41
        Star: IntType = 42
        Plus: IntType = 43
        Comma: IntType = 44
        Minus: IntType = 45
        Dot: IntType = 46
        Slash: IntType = 47
        Lt: IntType = 60
        Eq: IntType = 61
        Gt: IntType = 62
        At: IntType = 64
        And: IntType = 65
        DotDot: IntType = 68
        Eof: IntType = 69
        Ge: IntType = 71
        Le: IntType = 76
        Ne: IntType = 78
        Or: IntType = 79
        SlashSlash: IntType = 83
        LBracket: IntType = 91
        RBracket: IntType = 93
        Axe: IntType = 97
        Number: IntType = 100
        Name: IntType = 110
        String: IntType = 115
        Union: IntType = 124
    


class XPathSelectionIterator(ResetableIterator, ICloneable, IEnumerable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def Current(self) -> XPathNavigator: ...
    
    @property
    def CurrentPosition(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def MoveNext(self) -> BooleanType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_Current(self) -> XPathNavigator: ...
    
    def get_CurrentPosition(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XPathSelectionIterator(ResetableIterator, ICloneable, IEnumerable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def Current(self) -> XPathNavigator: ...
    
    @property
    def CurrentPosition(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def MoveNext(self) -> BooleanType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_Current(self) -> XPathNavigator: ...
    
    def get_CurrentPosition(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XPathSelfQuery(BaseAxisQuery, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, qyInput: Query, Name: StringType, Prefix: StringType, Type: XPathNodeType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Advance(self) -> XPathNavigator: ...
    
    def Clone(self) -> XPathNodeIterator: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XPathSelfQuery(BaseAxisQuery, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, qyInput: Query, Name: StringType, Prefix: StringType, Type: XPathNodeType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Advance(self) -> XPathNavigator: ...
    
    def Clone(self) -> XPathNodeIterator: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XPathSingletonIterator(ResetableIterator, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, nav: XPathNavigator): ...
    
    @overload
    def __init__(self, nav: XPathNavigator, moved: BooleanType): ...
    
    @overload
    def __init__(self, it: XPathSingletonIterator): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def Current(self) -> XPathNavigator: ...
    
    @property
    def CurrentPosition(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def MoveNext(self) -> BooleanType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_Current(self) -> XPathNavigator: ...
    
    def get_CurrentPosition(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XPathSingletonIterator(ResetableIterator, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, nav: XPathNavigator): ...
    
    @overload
    def __init__(self, nav: XPathNavigator, moved: BooleanType): ...
    
    @overload
    def __init__(self, it: XPathSingletonIterator): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def Current(self) -> XPathNavigator: ...
    
    @property
    def CurrentPosition(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def MoveNext(self) -> BooleanType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_Current(self) -> XPathNavigator: ...
    
    def get_CurrentPosition(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XPathSortComparer(ObjectType, IComparer[SortKey]):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, size: IntType): ...
    
    @overload
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def NumSorts(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def AddSort(self, evalQuery: Query, comparer: IComparer) -> VoidType: ...
    
    def Expression(self, i: IntType) -> Query: ...
    
    def get_NumSorts(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XPathSortComparer(ObjectType, IComparer[SortKey]):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, size: IntType): ...
    
    @overload
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def NumSorts(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def AddSort(self, evalQuery: Query, comparer: IComparer) -> VoidType: ...
    
    def Expression(self, i: IntType) -> Query: ...
    
    def get_NumSorts(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# No Structs

# No Interfaces

# ---------- Enums ---------- #

class QueryProps(Enum):
    #None: IntType = 0
    Position: IntType = 1
    Count: IntType = 2
    Cached: IntType = 4
    Reverse: IntType = 8
    Merge: IntType = 16


class QueryProps(Enum):
    #None: IntType = 0
    Position: IntType = 1
    Count: IntType = 2
    Cached: IntType = 4
    Reverse: IntType = 8
    Merge: IntType = 16


# No Delegates

__all__ = [
    AbsoluteQuery,
    AstNode,
    AttributeQuery,
    Axis,
    BaseAxisQuery,
    BooleanExpr,
    BooleanFunctions,
    CacheAxisQuery,
    CacheChildrenQuery,
    CacheOutputQuery,
    ChildrenQuery,
    ClonableStack,
    CompiledXpathExpr,
    ContextQuery,
    DescendantBaseQuery,
    DescendantOverDescendantQuery,
    DescendantQuery,
    DocumentOrderQuery,
    EmptyQuery,
    ExtensionQuery,
    Filter,
    FilterQuery,
    FollSiblingQuery,
    FollowingQuery,
    ForwardPositionQuery,
    Function,
    FunctionQuery,
    Group,
    GroupQuery,
    IDQuery,
    IteratorFilter,
    LogicalExpr,
    MergeFilterQuery,
    NamespaceQuery,
    NodeFunctions,
    NumberFunctions,
    NumericExpr,
    Operand,
    OperandQuery,
    Operator,
    ParentQuery,
    PreSiblingQuery,
    PrecedingQuery,
    Query,
    QueryBuilder,
    ResetableIterator,
    ReversePositionQuery,
    Root,
    SortKey,
    SortQuery,
    StringFunctions,
    UnionExpr,
    ValueQuery,
    Variable,
    VariableQuery,
    XPathAncestorIterator,
    XPathAncestorQuery,
    XPathArrayIterator,
    XPathAxisIterator,
    XPathChildIterator,
    XPathComparerHelper,
    XPathDescendantIterator,
    XPathEmptyIterator,
    XPathMultyIterator,
    XPathParser,
    XPathScanner,
    XPathSelectionIterator,
    XPathSelfQuery,
    XPathSingletonIterator,
    XPathSortComparer,
    QueryProps,
]
