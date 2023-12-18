from __future__ import annotations

from abc import ABC
from typing import Generic
from typing import TypeVar
from typing import Union
from typing import overload

from System import Boolean
from System import Double
from System import Enum
from System import ICloneable
from System import Int32
from System import Object
from System import String
from System import Void
from System.Collections import ArrayList
from System.Collections import ICollection
from System.Collections import IComparer
from System.Collections import IEnumerable
from System.Collections import IEnumerator
from System.Collections import IList
from System.Collections.Generic import ICollection
from System.Collections.Generic import IComparer
from System.Collections.Generic import IEnumerable
from System.Collections.Generic import IList
from System.Collections.Generic import IReadOnlyCollection
from System.Collections.Generic import IReadOnlyList
from System.Collections.Generic import List
from System.Xml import IXmlNamespaceResolver
from System.Xml import XmlNamespaceManager
from System.Xml import XmlNodeOrder
from System.Xml import XmlWriter
from System.Xml.XPath import XmlCaseOrder
from System.Xml.XPath import XmlDataType
from System.Xml.XPath import XmlSortOrder
from System.Xml.XPath import XPathExpression
from System.Xml.XPath import XPathNavigator
from System.Xml.XPath import XPathNodeIterator
from System.Xml.XPath import XPathNodeType
from System.Xml.XPath import XPathResultType
from System.Xml.Xsl import XsltContext

# ---------- Types ---------- #

T = TypeVar("T")

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
        Axis = 0
        Operator = 1
        Filter = 2
        ConstantOperand = 3
        Function = 4
        Group = 5
        Root = 6
        Variable = 7
        Error = 8

class AttributeQuery(BaseAxisQuery, ICloneable, IEnumerable):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(
        self, qyParent: Query, Name: StringType, Prefix: StringType, Type: XPathNodeType
    ): ...

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
    def __init__(
        self,
        axisType: AxisType,
        input: AstNode,
        prefix: StringType,
        name: StringType,
        nodetype: XPathNodeType,
    ): ...
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
        Ancestor = 0
        AncestorOrSelf = 1
        Attribute = 2
        Child = 3
        Descendant = 4
        DescendantOrSelf = 5
        Following = 6
        FollowingSibling = 7
        Namespace = 8
        Parent = 9
        Preceding = 10
        PrecedingSibling = 11
        Self = 12
        # None = 13

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

    def __init__(
        self, qyInput: Query, name: StringType, prefix: StringType, typeTest: XPathNodeType
    ): ...

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

    def __init__(
        self, qyInput: Query, name: StringType, prefix: StringType, type: XPathNodeType
    ): ...

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

class ChildrenQuery(BaseAxisQuery, ICloneable, IEnumerable):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(
        self, qyInput: Query, name: StringType, prefix: StringType, type: XPathNodeType
    ): ...

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

class ClonableStack(
    Generic[T],
    List[T],
    IList[T],
    ICollection[T],
    IEnumerable[T],
    IEnumerable,
    IList,
    ICollection,
    IReadOnlyList[T],
    IReadOnlyCollection[T],
):
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
    def AddSort(
        self,
        expr: ObjectType,
        order: XmlSortOrder,
        caseOrder: XmlCaseOrder,
        lang: StringType,
        dataType: XmlDataType,
    ) -> VoidType: ...
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

class DescendantBaseQuery(ABC, BaseAxisQuery, ICloneable, IEnumerable):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(
        self,
        qyParent: Query,
        Name: StringType,
        Prefix: StringType,
        Type: XPathNodeType,
        matchSelf: BooleanType,
        abbrAxis: BooleanType,
    ): ...
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

    def __init__(
        self,
        qyParent: Query,
        matchSelf: BooleanType,
        name: StringType,
        prefix: StringType,
        typeTest: XPathNodeType,
        abbrAxis: BooleanType,
    ): ...

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

class FollSiblingQuery(BaseAxisQuery, ICloneable, IEnumerable):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(
        self, qyInput: Query, name: StringType, prefix: StringType, type: XPathNodeType
    ): ...

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

    def __init__(
        self, qyInput: Query, name: StringType, prefix: StringType, typeTest: XPathNodeType
    ): ...

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
        FuncLast = 0
        FuncPosition = 1
        FuncCount = 2
        FuncID = 3
        FuncLocalName = 4
        FuncNameSpaceUri = 5
        FuncName = 6
        FuncString = 7
        FuncBoolean = 8
        FuncNumber = 9
        FuncTrue = 10
        FuncFalse = 11
        FuncNot = 12
        FuncConcat = 13
        FuncStartsWith = 14
        FuncContains = 15
        FuncSubstringBefore = 16
        FuncSubstringAfter = 17
        FuncSubstring = 18
        FuncStringLength = 19
        FuncNormalize = 20
        FuncTranslate = 21
        FuncLang = 22
        FuncSum = 23
        FuncFloor = 24
        FuncCeiling = 25
        FuncRound = 26
        FuncUserDefined = 27

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

    def __init__(
        self, qyParent: Query, Name: StringType, Prefix: StringType, Type: XPathNodeType
    ): ...

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
        INVALID = 0
        OR = 1
        AND = 2
        EQ = 3
        NE = 4
        LT = 5
        LE = 6
        GT = 7
        GE = 8
        PLUS = 9
        MINUS = 10
        MUL = 11
        DIV = 12
        MOD = 13
        UNION = 14

class ParentQuery(CacheAxisQuery, ICloneable, IEnumerable):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(
        self, qyInput: Query, Name: StringType, Prefix: StringType, Type: XPathNodeType
    ): ...

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

    def __init__(
        self, qyInput: Query, name: StringType, prefix: StringType, typeTest: XPathNodeType
    ): ...

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

    def __init__(
        self, qyInput: Query, name: StringType, prefix: StringType, typeTest: XPathNodeType
    ): ...

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

class SortKey(ObjectType):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, numKeys: IntType, originalPosition: IntType, node: XPathNavigator): ...

    # ---------- Properties ---------- #

    def __getitem__(self, key: IntType) -> ObjectType: ...
    def __setitem__(self, key: IntType, value: ObjectType) -> None: ...
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
    def __init__(
        self,
        nav: XPathNavigator,
        name: StringType,
        namespaceURI: StringType,
        matchSelf: BooleanType,
    ): ...
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

    def __init__(
        self,
        qyInput: Query,
        name: StringType,
        prefix: StringType,
        typeTest: XPathNodeType,
        matchSelf: BooleanType,
    ): ...

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

class XPathAxisIterator(ABC, XPathNodeIterator, ICloneable, IEnumerable):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self, nav: XPathNavigator, matchSelf: BooleanType): ...
    @overload
    def __init__(self, nav: XPathNavigator, type: XPathNodeType, matchSelf: BooleanType): ...
    @overload
    def __init__(
        self,
        nav: XPathNavigator,
        name: StringType,
        namespaceURI: StringType,
        matchSelf: BooleanType,
    ): ...
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

class XPathComparerHelper(ObjectType, IComparer):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(
        self, order: XmlSortOrder, caseOrder: XmlCaseOrder, lang: StringType, dataType: XmlDataType
    ): ...

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
    def __init__(
        self,
        nav: XPathNavigator,
        name: StringType,
        namespaceURI: StringType,
        matchSelf: BooleanType,
    ): ...
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
        Bang = 33
        Quote = 34
        Dollar = 36
        Apos = 39
        LParens = 40
        RParens = 41
        Star = 42
        Plus = 43
        Comma = 44
        Minus = 45
        Dot = 46
        Slash = 47
        Lt = 60
        Eq = 61
        Gt = 62
        At = 64
        And = 65
        DotDot = 68
        Eof = 69
        Ge = 71
        Le = 76
        Ne = 78
        Or = 79
        SlashSlash = 83
        LBracket = 91
        RBracket = 93
        Axe = 97
        Number = 100
        Name = 110
        String = 115
        Union = 124

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

    def __init__(
        self, qyInput: Query, Name: StringType, Prefix: StringType, Type: XPathNodeType
    ): ...

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
    # None = 0
    Position = 1
    Count = 2
    Cached = 4
    Reverse = 8
    Merge = 16

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
