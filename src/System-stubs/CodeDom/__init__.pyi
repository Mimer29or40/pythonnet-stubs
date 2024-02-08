from __future__ import annotations

from typing import Generic
from typing import Iterator
from typing import TypeVar
from typing import overload

from System import Array
from System import Enum
from System import EventHandler
from System import Guid
from System import Object
from System import Type
from System.Collections import CollectionBase
from System.Collections import ICollection
from System.Collections import IDictionary
from System.Collections import IEnumerable
from System.Collections import IEnumerator
from System.Collections import IList
from System.Collections.Specialized import StringCollection
from System.Reflection import TypeAttributes

T = TypeVar("T")

class EventType(Generic[T]):
    def __iadd__(self, other: T): ...
    def __isub__(self, other: T): ...

class CodeArgumentReferenceExpression(CodeExpression):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, parameterName: str):
        """

        :param parameterName:
        """
    @property
    def ParameterName(self) -> str:
        """

        :return:
        """
    @ParameterName.setter
    def ParameterName(self, value: str) -> None: ...
    @property
    def UserData(self) -> IDictionary:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CodeArrayCreateExpression(CodeExpression):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, createType: CodeTypeReference, size: CodeExpression):
        """

        :param createType:
        :param size:
        """
    @overload
    def __init__(self, createType: CodeTypeReference, initializers: Array[CodeExpression]):
        """

        :param createType:
        :param initializers:
        """
    @overload
    def __init__(self, createType: CodeTypeReference, size: int):
        """

        :param createType:
        :param size:
        """
    @overload
    def __init__(self, createType: str, size: CodeExpression):
        """

        :param createType:
        :param size:
        """
    @overload
    def __init__(self, createType: str, initializers: Array[CodeExpression]):
        """

        :param createType:
        :param initializers:
        """
    @overload
    def __init__(self, createType: str, size: int):
        """

        :param createType:
        :param size:
        """
    @overload
    def __init__(self, createType: Type, size: CodeExpression):
        """

        :param createType:
        :param size:
        """
    @overload
    def __init__(self, createType: Type, initializers: Array[CodeExpression]):
        """

        :param createType:
        :param initializers:
        """
    @overload
    def __init__(self, createType: Type, size: int):
        """

        :param createType:
        :param size:
        """
    @property
    def CreateType(self) -> CodeTypeReference:
        """

        :return:
        """
    @CreateType.setter
    def CreateType(self, value: CodeTypeReference) -> None: ...
    @property
    def Initializers(self) -> CodeExpressionCollection:
        """

        :return:
        """
    @property
    def Size(self) -> int:
        """

        :return:
        """
    @Size.setter
    def Size(self, value: int) -> None: ...
    @property
    def SizeExpression(self) -> CodeExpression:
        """

        :return:
        """
    @SizeExpression.setter
    def SizeExpression(self, value: CodeExpression) -> None: ...
    @property
    def UserData(self) -> IDictionary:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CodeArrayIndexerExpression(CodeExpression):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, targetObject: CodeExpression, indices: Array[CodeExpression]):
        """

        :param targetObject:
        :param indices:
        """
    @property
    def Indices(self) -> CodeExpressionCollection:
        """

        :return:
        """
    @property
    def TargetObject(self) -> CodeExpression:
        """

        :return:
        """
    @TargetObject.setter
    def TargetObject(self, value: CodeExpression) -> None: ...
    @property
    def UserData(self) -> IDictionary:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CodeAssignStatement(CodeStatement):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, left: CodeExpression, right: CodeExpression):
        """

        :param left:
        :param right:
        """
    @property
    def EndDirectives(self) -> CodeDirectiveCollection:
        """

        :return:
        """
    @property
    def Left(self) -> CodeExpression:
        """

        :return:
        """
    @Left.setter
    def Left(self, value: CodeExpression) -> None: ...
    @property
    def LinePragma(self) -> CodeLinePragma:
        """

        :return:
        """
    @LinePragma.setter
    def LinePragma(self, value: CodeLinePragma) -> None: ...
    @property
    def Right(self) -> CodeExpression:
        """

        :return:
        """
    @Right.setter
    def Right(self, value: CodeExpression) -> None: ...
    @property
    def StartDirectives(self) -> CodeDirectiveCollection:
        """

        :return:
        """
    @property
    def UserData(self) -> IDictionary:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CodeAttachEventStatement(CodeStatement):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, eventRef: CodeEventReferenceExpression, listener: CodeExpression):
        """

        :param eventRef:
        :param listener:
        """
    @overload
    def __init__(self, targetObject: CodeExpression, eventName: str, listener: CodeExpression):
        """

        :param targetObject:
        :param eventName:
        :param listener:
        """
    @property
    def EndDirectives(self) -> CodeDirectiveCollection:
        """

        :return:
        """
    @property
    def Event(self) -> CodeEventReferenceExpression:
        """

        :return:
        """
    @Event.setter
    def Event(self, value: CodeEventReferenceExpression) -> None: ...
    @property
    def LinePragma(self) -> CodeLinePragma:
        """

        :return:
        """
    @LinePragma.setter
    def LinePragma(self, value: CodeLinePragma) -> None: ...
    @property
    def Listener(self) -> CodeExpression:
        """

        :return:
        """
    @Listener.setter
    def Listener(self, value: CodeExpression) -> None: ...
    @property
    def StartDirectives(self) -> CodeDirectiveCollection:
        """

        :return:
        """
    @property
    def UserData(self) -> IDictionary:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CodeAttributeArgument(Object):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, value: CodeExpression):
        """

        :param value:
        """
    @overload
    def __init__(self, name: str, value: CodeExpression):
        """

        :param name:
        :param value:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def Value(self) -> CodeExpression:
        """

        :return:
        """
    @Value.setter
    def Value(self, value: CodeExpression) -> None: ...
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CodeAttributeArgumentCollection(CollectionBase, ICollection, IEnumerable, IList):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, value: CodeAttributeArgumentCollection):
        """

        :param value:
        """
    @overload
    def __init__(self, value: Array[CodeAttributeArgument]):
        """

        :param value:
        """
    @property
    def Capacity(self) -> int:
        """

        :return:
        """
    @Capacity.setter
    def Capacity(self, value: int) -> None: ...
    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def IsFixedSize(self) -> bool:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def IsSynchronized(self) -> bool:
        """

        :return:
        """
    @property
    def Item(self) -> object:
        """

        :return:
        """
    @Item.setter
    def Item(self, value: object) -> None: ...
    @property
    def SyncRoot(self) -> object:
        """

        :return:
        """
    @overload
    def Add(self, value: CodeAttributeArgument) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def Add(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def AddRange(self, value: CodeAttributeArgumentCollection) -> None:
        """

        :param value:
        """
    @overload
    def AddRange(self, value: Array[CodeAttributeArgument]) -> None:
        """

        :param value:
        """
    def Clear(self) -> None:
        """"""
    @overload
    def Contains(self, value: CodeAttributeArgument) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def Contains(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    @overload
    def CopyTo(self, array: Array[CodeAttributeArgument], index: int) -> None:
        """

        :param array:
        :param index:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def IndexOf(self, value: CodeAttributeArgument) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def IndexOf(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def Insert(self, index: int, value: CodeAttributeArgument) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def Insert(self, index: int, value: object) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def Remove(self, value: CodeAttributeArgument) -> None:
        """

        :param value:
        """
    @overload
    def Remove(self, value: object) -> None:
        """

        :param value:
        """
    def RemoveAt(self, index: int) -> None:
        """

        :param index:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def __contains__(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    def __getitem__(self, index: int) -> object:
        """

        :param index:
        :return:
        """
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    def __len__(self) -> int:
        """

        :return:
        """
    @overload
    def __setitem__(self, index: int, value: CodeAttributeArgument) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def __setitem__(self, index: int, value: object) -> None:
        """

        :param index:
        :param value:
        """

class CodeAttributeDeclaration(Object):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, attributeType: CodeTypeReference):
        """

        :param attributeType:
        """
    @overload
    def __init__(self, name: str):
        """

        :param name:
        """
    @overload
    def __init__(self, attributeType: CodeTypeReference, arguments: Array[CodeAttributeArgument]):
        """

        :param attributeType:
        :param arguments:
        """
    @overload
    def __init__(self, name: str, arguments: Array[CodeAttributeArgument]):
        """

        :param name:
        :param arguments:
        """
    @property
    def Arguments(self) -> CodeAttributeArgumentCollection:
        """

        :return:
        """
    @property
    def AttributeType(self) -> CodeTypeReference:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @Name.setter
    def Name(self, value: str) -> None: ...
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CodeAttributeDeclarationCollection(CollectionBase, ICollection, IEnumerable, IList):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, value: CodeAttributeDeclarationCollection):
        """

        :param value:
        """
    @overload
    def __init__(self, value: Array[CodeAttributeDeclaration]):
        """

        :param value:
        """
    @property
    def Capacity(self) -> int:
        """

        :return:
        """
    @Capacity.setter
    def Capacity(self, value: int) -> None: ...
    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def IsFixedSize(self) -> bool:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def IsSynchronized(self) -> bool:
        """

        :return:
        """
    @property
    def Item(self) -> object:
        """

        :return:
        """
    @Item.setter
    def Item(self, value: object) -> None: ...
    @property
    def SyncRoot(self) -> object:
        """

        :return:
        """
    @overload
    def Add(self, value: CodeAttributeDeclaration) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def Add(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def AddRange(self, value: CodeAttributeDeclarationCollection) -> None:
        """

        :param value:
        """
    @overload
    def AddRange(self, value: Array[CodeAttributeDeclaration]) -> None:
        """

        :param value:
        """
    def Clear(self) -> None:
        """"""
    @overload
    def Contains(self, value: CodeAttributeDeclaration) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def Contains(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    @overload
    def CopyTo(self, array: Array[CodeAttributeDeclaration], index: int) -> None:
        """

        :param array:
        :param index:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def IndexOf(self, value: CodeAttributeDeclaration) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def IndexOf(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def Insert(self, index: int, value: CodeAttributeDeclaration) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def Insert(self, index: int, value: object) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def Remove(self, value: CodeAttributeDeclaration) -> None:
        """

        :param value:
        """
    @overload
    def Remove(self, value: object) -> None:
        """

        :param value:
        """
    def RemoveAt(self, index: int) -> None:
        """

        :param index:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def __contains__(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    def __getitem__(self, index: int) -> object:
        """

        :param index:
        :return:
        """
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    def __len__(self) -> int:
        """

        :return:
        """
    @overload
    def __setitem__(self, index: int, value: CodeAttributeDeclaration) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def __setitem__(self, index: int, value: object) -> None:
        """

        :param index:
        :param value:
        """

class CodeBaseReferenceExpression(CodeExpression):
    """"""

    def __init__(self):
        """"""
    @property
    def UserData(self) -> IDictionary:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CodeBinaryOperatorExpression(CodeExpression):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, left: CodeExpression, op: CodeBinaryOperatorType, right: CodeExpression):
        """

        :param left:
        :param op:
        :param right:
        """
    @property
    def Left(self) -> CodeExpression:
        """

        :return:
        """
    @Left.setter
    def Left(self, value: CodeExpression) -> None: ...
    @property
    def Operator(self) -> CodeBinaryOperatorType:
        """

        :return:
        """
    @Operator.setter
    def Operator(self, value: CodeBinaryOperatorType) -> None: ...
    @property
    def Right(self) -> CodeExpression:
        """

        :return:
        """
    @Right.setter
    def Right(self, value: CodeExpression) -> None: ...
    @property
    def UserData(self) -> IDictionary:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CodeBinaryOperatorType(Enum):
    """"""

    Add: CodeBinaryOperatorType = ...
    """"""
    Subtract: CodeBinaryOperatorType = ...
    """"""
    Multiply: CodeBinaryOperatorType = ...
    """"""
    Divide: CodeBinaryOperatorType = ...
    """"""
    Modulus: CodeBinaryOperatorType = ...
    """"""
    Assign: CodeBinaryOperatorType = ...
    """"""
    IdentityInequality: CodeBinaryOperatorType = ...
    """"""
    IdentityEquality: CodeBinaryOperatorType = ...
    """"""
    ValueEquality: CodeBinaryOperatorType = ...
    """"""
    BitwiseOr: CodeBinaryOperatorType = ...
    """"""
    BitwiseAnd: CodeBinaryOperatorType = ...
    """"""
    BooleanOr: CodeBinaryOperatorType = ...
    """"""
    BooleanAnd: CodeBinaryOperatorType = ...
    """"""
    LessThan: CodeBinaryOperatorType = ...
    """"""
    LessThanOrEqual: CodeBinaryOperatorType = ...
    """"""
    GreaterThan: CodeBinaryOperatorType = ...
    """"""
    GreaterThanOrEqual: CodeBinaryOperatorType = ...
    """"""

class CodeCastExpression(CodeExpression):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, targetType: CodeTypeReference, expression: CodeExpression):
        """

        :param targetType:
        :param expression:
        """
    @overload
    def __init__(self, targetType: str, expression: CodeExpression):
        """

        :param targetType:
        :param expression:
        """
    @overload
    def __init__(self, targetType: Type, expression: CodeExpression):
        """

        :param targetType:
        :param expression:
        """
    @property
    def Expression(self) -> CodeExpression:
        """

        :return:
        """
    @Expression.setter
    def Expression(self, value: CodeExpression) -> None: ...
    @property
    def TargetType(self) -> CodeTypeReference:
        """

        :return:
        """
    @TargetType.setter
    def TargetType(self, value: CodeTypeReference) -> None: ...
    @property
    def UserData(self) -> IDictionary:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CodeCatchClause(Object):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, localName: str):
        """

        :param localName:
        """
    @overload
    def __init__(self, localName: str, catchExceptionType: CodeTypeReference):
        """

        :param localName:
        :param catchExceptionType:
        """
    @overload
    def __init__(
        self,
        localName: str,
        catchExceptionType: CodeTypeReference,
        statements: Array[CodeStatement],
    ):
        """

        :param localName:
        :param catchExceptionType:
        :param statements:
        """
    @property
    def CatchExceptionType(self) -> CodeTypeReference:
        """

        :return:
        """
    @CatchExceptionType.setter
    def CatchExceptionType(self, value: CodeTypeReference) -> None: ...
    @property
    def LocalName(self) -> str:
        """

        :return:
        """
    @LocalName.setter
    def LocalName(self, value: str) -> None: ...
    @property
    def Statements(self) -> CodeStatementCollection:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CodeCatchClauseCollection(CollectionBase, ICollection, IEnumerable, IList):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, value: CodeCatchClauseCollection):
        """

        :param value:
        """
    @overload
    def __init__(self, value: Array[CodeCatchClause]):
        """

        :param value:
        """
    @property
    def Capacity(self) -> int:
        """

        :return:
        """
    @Capacity.setter
    def Capacity(self, value: int) -> None: ...
    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def IsFixedSize(self) -> bool:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def IsSynchronized(self) -> bool:
        """

        :return:
        """
    @property
    def Item(self) -> object:
        """

        :return:
        """
    @Item.setter
    def Item(self, value: object) -> None: ...
    @property
    def SyncRoot(self) -> object:
        """

        :return:
        """
    @overload
    def Add(self, value: CodeCatchClause) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def Add(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def AddRange(self, value: CodeCatchClauseCollection) -> None:
        """

        :param value:
        """
    @overload
    def AddRange(self, value: Array[CodeCatchClause]) -> None:
        """

        :param value:
        """
    def Clear(self) -> None:
        """"""
    @overload
    def Contains(self, value: CodeCatchClause) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def Contains(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    @overload
    def CopyTo(self, array: Array[CodeCatchClause], index: int) -> None:
        """

        :param array:
        :param index:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def IndexOf(self, value: CodeCatchClause) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def IndexOf(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def Insert(self, index: int, value: CodeCatchClause) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def Insert(self, index: int, value: object) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def Remove(self, value: CodeCatchClause) -> None:
        """

        :param value:
        """
    @overload
    def Remove(self, value: object) -> None:
        """

        :param value:
        """
    def RemoveAt(self, index: int) -> None:
        """

        :param index:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def __contains__(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    def __getitem__(self, index: int) -> object:
        """

        :param index:
        :return:
        """
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    def __len__(self) -> int:
        """

        :return:
        """
    @overload
    def __setitem__(self, index: int, value: CodeCatchClause) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def __setitem__(self, index: int, value: object) -> None:
        """

        :param index:
        :param value:
        """

class CodeChecksumPragma(CodeDirective):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, fileName: str, checksumAlgorithmId: Guid, checksumData: Array[int]):
        """

        :param fileName:
        :param checksumAlgorithmId:
        :param checksumData:
        """
    @property
    def ChecksumAlgorithmId(self) -> Guid:
        """

        :return:
        """
    @ChecksumAlgorithmId.setter
    def ChecksumAlgorithmId(self, value: Guid) -> None: ...
    @property
    def ChecksumData(self) -> Array[int]:
        """

        :return:
        """
    @ChecksumData.setter
    def ChecksumData(self, value: Array[int]) -> None: ...
    @property
    def FileName(self) -> str:
        """

        :return:
        """
    @FileName.setter
    def FileName(self, value: str) -> None: ...
    @property
    def UserData(self) -> IDictionary:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CodeComment(CodeObject):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, text: str):
        """

        :param text:
        """
    @overload
    def __init__(self, text: str, docComment: bool):
        """

        :param text:
        :param docComment:
        """
    @property
    def DocComment(self) -> bool:
        """

        :return:
        """
    @DocComment.setter
    def DocComment(self, value: bool) -> None: ...
    @property
    def Text(self) -> str:
        """

        :return:
        """
    @Text.setter
    def Text(self, value: str) -> None: ...
    @property
    def UserData(self) -> IDictionary:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CodeCommentStatement(CodeStatement):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, comment: CodeComment):
        """

        :param comment:
        """
    @overload
    def __init__(self, text: str):
        """

        :param text:
        """
    @overload
    def __init__(self, text: str, docComment: bool):
        """

        :param text:
        :param docComment:
        """
    @property
    def Comment(self) -> CodeComment:
        """

        :return:
        """
    @Comment.setter
    def Comment(self, value: CodeComment) -> None: ...
    @property
    def EndDirectives(self) -> CodeDirectiveCollection:
        """

        :return:
        """
    @property
    def LinePragma(self) -> CodeLinePragma:
        """

        :return:
        """
    @LinePragma.setter
    def LinePragma(self, value: CodeLinePragma) -> None: ...
    @property
    def StartDirectives(self) -> CodeDirectiveCollection:
        """

        :return:
        """
    @property
    def UserData(self) -> IDictionary:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CodeCommentStatementCollection(CollectionBase, ICollection, IEnumerable, IList):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, value: CodeCommentStatementCollection):
        """

        :param value:
        """
    @overload
    def __init__(self, value: Array[CodeCommentStatement]):
        """

        :param value:
        """
    @property
    def Capacity(self) -> int:
        """

        :return:
        """
    @Capacity.setter
    def Capacity(self, value: int) -> None: ...
    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def IsFixedSize(self) -> bool:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def IsSynchronized(self) -> bool:
        """

        :return:
        """
    @property
    def Item(self) -> object:
        """

        :return:
        """
    @Item.setter
    def Item(self, value: object) -> None: ...
    @property
    def SyncRoot(self) -> object:
        """

        :return:
        """
    @overload
    def Add(self, value: CodeCommentStatement) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def Add(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def AddRange(self, value: CodeCommentStatementCollection) -> None:
        """

        :param value:
        """
    @overload
    def AddRange(self, value: Array[CodeCommentStatement]) -> None:
        """

        :param value:
        """
    def Clear(self) -> None:
        """"""
    @overload
    def Contains(self, value: CodeCommentStatement) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def Contains(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    @overload
    def CopyTo(self, array: Array[CodeCommentStatement], index: int) -> None:
        """

        :param array:
        :param index:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def IndexOf(self, value: CodeCommentStatement) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def IndexOf(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def Insert(self, index: int, value: CodeCommentStatement) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def Insert(self, index: int, value: object) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def Remove(self, value: CodeCommentStatement) -> None:
        """

        :param value:
        """
    @overload
    def Remove(self, value: object) -> None:
        """

        :param value:
        """
    def RemoveAt(self, index: int) -> None:
        """

        :param index:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def __contains__(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    def __getitem__(self, index: int) -> object:
        """

        :param index:
        :return:
        """
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    def __len__(self) -> int:
        """

        :return:
        """
    @overload
    def __setitem__(self, index: int, value: CodeCommentStatement) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def __setitem__(self, index: int, value: object) -> None:
        """

        :param index:
        :param value:
        """

class CodeCompileUnit(CodeObject):
    """"""

    def __init__(self):
        """"""
    @property
    def AssemblyCustomAttributes(self) -> CodeAttributeDeclarationCollection:
        """

        :return:
        """
    @property
    def EndDirectives(self) -> CodeDirectiveCollection:
        """

        :return:
        """
    @property
    def Namespaces(self) -> CodeNamespaceCollection:
        """

        :return:
        """
    @property
    def ReferencedAssemblies(self) -> StringCollection:
        """

        :return:
        """
    @property
    def StartDirectives(self) -> CodeDirectiveCollection:
        """

        :return:
        """
    @property
    def UserData(self) -> IDictionary:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CodeConditionStatement(CodeStatement):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, condition: CodeExpression, trueStatements: Array[CodeStatement]):
        """

        :param condition:
        :param trueStatements:
        """
    @overload
    def __init__(
        self,
        condition: CodeExpression,
        trueStatements: Array[CodeStatement],
        falseStatements: Array[CodeStatement],
    ):
        """

        :param condition:
        :param trueStatements:
        :param falseStatements:
        """
    @property
    def Condition(self) -> CodeExpression:
        """

        :return:
        """
    @Condition.setter
    def Condition(self, value: CodeExpression) -> None: ...
    @property
    def EndDirectives(self) -> CodeDirectiveCollection:
        """

        :return:
        """
    @property
    def FalseStatements(self) -> CodeStatementCollection:
        """

        :return:
        """
    @property
    def LinePragma(self) -> CodeLinePragma:
        """

        :return:
        """
    @LinePragma.setter
    def LinePragma(self, value: CodeLinePragma) -> None: ...
    @property
    def StartDirectives(self) -> CodeDirectiveCollection:
        """

        :return:
        """
    @property
    def TrueStatements(self) -> CodeStatementCollection:
        """

        :return:
        """
    @property
    def UserData(self) -> IDictionary:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CodeConstructor(CodeMemberMethod):
    """"""

    def __init__(self):
        """"""
    @property
    def Attributes(self) -> MemberAttributes:
        """

        :return:
        """
    @Attributes.setter
    def Attributes(self, value: MemberAttributes) -> None: ...
    @property
    def BaseConstructorArgs(self) -> CodeExpressionCollection:
        """

        :return:
        """
    @property
    def ChainedConstructorArgs(self) -> CodeExpressionCollection:
        """

        :return:
        """
    @property
    def Comments(self) -> CodeCommentStatementCollection:
        """

        :return:
        """
    @property
    def CustomAttributes(self) -> CodeAttributeDeclarationCollection:
        """

        :return:
        """
    @CustomAttributes.setter
    def CustomAttributes(self, value: CodeAttributeDeclarationCollection) -> None: ...
    @property
    def EndDirectives(self) -> CodeDirectiveCollection:
        """

        :return:
        """
    @property
    def ImplementationTypes(self) -> CodeTypeReferenceCollection:
        """

        :return:
        """
    @property
    def LinePragma(self) -> CodeLinePragma:
        """

        :return:
        """
    @LinePragma.setter
    def LinePragma(self, value: CodeLinePragma) -> None: ...
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def Parameters(self) -> CodeParameterDeclarationExpressionCollection:
        """

        :return:
        """
    @property
    def PrivateImplementationType(self) -> CodeTypeReference:
        """

        :return:
        """
    @PrivateImplementationType.setter
    def PrivateImplementationType(self, value: CodeTypeReference) -> None: ...
    @property
    def ReturnType(self) -> CodeTypeReference:
        """

        :return:
        """
    @ReturnType.setter
    def ReturnType(self, value: CodeTypeReference) -> None: ...
    @property
    def ReturnTypeCustomAttributes(self) -> CodeAttributeDeclarationCollection:
        """

        :return:
        """
    @property
    def StartDirectives(self) -> CodeDirectiveCollection:
        """

        :return:
        """
    @property
    def Statements(self) -> CodeStatementCollection:
        """

        :return:
        """
    @property
    def TypeParameters(self) -> CodeTypeParameterCollection:
        """

        :return:
        """
    @property
    def UserData(self) -> IDictionary:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    PopulateImplementationTypes: EventType[EventHandler] = ...
    """"""
    PopulateParameters: EventType[EventHandler] = ...
    """"""
    PopulateStatements: EventType[EventHandler] = ...
    """"""

class CodeDefaultValueExpression(CodeExpression):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, type: CodeTypeReference):
        """

        :param type:
        """
    @property
    def Type(self) -> CodeTypeReference:
        """

        :return:
        """
    @Type.setter
    def Type(self, value: CodeTypeReference) -> None: ...
    @property
    def UserData(self) -> IDictionary:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CodeDelegateCreateExpression(CodeExpression):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(
        self, delegateType: CodeTypeReference, targetObject: CodeExpression, methodName: str
    ):
        """

        :param delegateType:
        :param targetObject:
        :param methodName:
        """
    @property
    def DelegateType(self) -> CodeTypeReference:
        """

        :return:
        """
    @DelegateType.setter
    def DelegateType(self, value: CodeTypeReference) -> None: ...
    @property
    def MethodName(self) -> str:
        """

        :return:
        """
    @MethodName.setter
    def MethodName(self, value: str) -> None: ...
    @property
    def TargetObject(self) -> CodeExpression:
        """

        :return:
        """
    @TargetObject.setter
    def TargetObject(self, value: CodeExpression) -> None: ...
    @property
    def UserData(self) -> IDictionary:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CodeDelegateInvokeExpression(CodeExpression):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, targetObject: CodeExpression):
        """

        :param targetObject:
        """
    @overload
    def __init__(self, targetObject: CodeExpression, parameters: Array[CodeExpression]):
        """

        :param targetObject:
        :param parameters:
        """
    @property
    def Parameters(self) -> CodeExpressionCollection:
        """

        :return:
        """
    @property
    def TargetObject(self) -> CodeExpression:
        """

        :return:
        """
    @TargetObject.setter
    def TargetObject(self, value: CodeExpression) -> None: ...
    @property
    def UserData(self) -> IDictionary:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CodeDirectionExpression(CodeExpression):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, direction: FieldDirection, expression: CodeExpression):
        """

        :param direction:
        :param expression:
        """
    @property
    def Direction(self) -> FieldDirection:
        """

        :return:
        """
    @Direction.setter
    def Direction(self, value: FieldDirection) -> None: ...
    @property
    def Expression(self) -> CodeExpression:
        """

        :return:
        """
    @Expression.setter
    def Expression(self, value: CodeExpression) -> None: ...
    @property
    def UserData(self) -> IDictionary:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CodeDirective(CodeObject):
    """"""

    def __init__(self):
        """"""
    @property
    def UserData(self) -> IDictionary:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CodeDirectiveCollection(CollectionBase, ICollection, IEnumerable, IList):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, value: CodeDirectiveCollection):
        """

        :param value:
        """
    @overload
    def __init__(self, value: Array[CodeDirective]):
        """

        :param value:
        """
    @property
    def Capacity(self) -> int:
        """

        :return:
        """
    @Capacity.setter
    def Capacity(self, value: int) -> None: ...
    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def IsFixedSize(self) -> bool:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def IsSynchronized(self) -> bool:
        """

        :return:
        """
    @property
    def Item(self) -> object:
        """

        :return:
        """
    @Item.setter
    def Item(self, value: object) -> None: ...
    @property
    def SyncRoot(self) -> object:
        """

        :return:
        """
    @overload
    def Add(self, value: CodeDirective) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def Add(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def AddRange(self, value: CodeDirectiveCollection) -> None:
        """

        :param value:
        """
    @overload
    def AddRange(self, value: Array[CodeDirective]) -> None:
        """

        :param value:
        """
    def Clear(self) -> None:
        """"""
    @overload
    def Contains(self, value: CodeDirective) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def Contains(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    @overload
    def CopyTo(self, array: Array[CodeDirective], index: int) -> None:
        """

        :param array:
        :param index:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def IndexOf(self, value: CodeDirective) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def IndexOf(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def Insert(self, index: int, value: CodeDirective) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def Insert(self, index: int, value: object) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def Remove(self, value: CodeDirective) -> None:
        """

        :param value:
        """
    @overload
    def Remove(self, value: object) -> None:
        """

        :param value:
        """
    def RemoveAt(self, index: int) -> None:
        """

        :param index:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def __contains__(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    def __getitem__(self, index: int) -> object:
        """

        :param index:
        :return:
        """
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    def __len__(self) -> int:
        """

        :return:
        """
    @overload
    def __setitem__(self, index: int, value: CodeDirective) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def __setitem__(self, index: int, value: object) -> None:
        """

        :param index:
        :param value:
        """

class CodeEntryPointMethod(CodeMemberMethod):
    """"""

    def __init__(self):
        """"""
    @property
    def Attributes(self) -> MemberAttributes:
        """

        :return:
        """
    @Attributes.setter
    def Attributes(self, value: MemberAttributes) -> None: ...
    @property
    def Comments(self) -> CodeCommentStatementCollection:
        """

        :return:
        """
    @property
    def CustomAttributes(self) -> CodeAttributeDeclarationCollection:
        """

        :return:
        """
    @CustomAttributes.setter
    def CustomAttributes(self, value: CodeAttributeDeclarationCollection) -> None: ...
    @property
    def EndDirectives(self) -> CodeDirectiveCollection:
        """

        :return:
        """
    @property
    def ImplementationTypes(self) -> CodeTypeReferenceCollection:
        """

        :return:
        """
    @property
    def LinePragma(self) -> CodeLinePragma:
        """

        :return:
        """
    @LinePragma.setter
    def LinePragma(self, value: CodeLinePragma) -> None: ...
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def Parameters(self) -> CodeParameterDeclarationExpressionCollection:
        """

        :return:
        """
    @property
    def PrivateImplementationType(self) -> CodeTypeReference:
        """

        :return:
        """
    @PrivateImplementationType.setter
    def PrivateImplementationType(self, value: CodeTypeReference) -> None: ...
    @property
    def ReturnType(self) -> CodeTypeReference:
        """

        :return:
        """
    @ReturnType.setter
    def ReturnType(self, value: CodeTypeReference) -> None: ...
    @property
    def ReturnTypeCustomAttributes(self) -> CodeAttributeDeclarationCollection:
        """

        :return:
        """
    @property
    def StartDirectives(self) -> CodeDirectiveCollection:
        """

        :return:
        """
    @property
    def Statements(self) -> CodeStatementCollection:
        """

        :return:
        """
    @property
    def TypeParameters(self) -> CodeTypeParameterCollection:
        """

        :return:
        """
    @property
    def UserData(self) -> IDictionary:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    PopulateImplementationTypes: EventType[EventHandler] = ...
    """"""
    PopulateParameters: EventType[EventHandler] = ...
    """"""
    PopulateStatements: EventType[EventHandler] = ...
    """"""

class CodeEventReferenceExpression(CodeExpression):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, targetObject: CodeExpression, eventName: str):
        """

        :param targetObject:
        :param eventName:
        """
    @property
    def EventName(self) -> str:
        """

        :return:
        """
    @EventName.setter
    def EventName(self, value: str) -> None: ...
    @property
    def TargetObject(self) -> CodeExpression:
        """

        :return:
        """
    @TargetObject.setter
    def TargetObject(self, value: CodeExpression) -> None: ...
    @property
    def UserData(self) -> IDictionary:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CodeExpression(CodeObject):
    """"""

    def __init__(self):
        """"""
    @property
    def UserData(self) -> IDictionary:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CodeExpressionCollection(CollectionBase, ICollection, IEnumerable, IList):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, value: CodeExpressionCollection):
        """

        :param value:
        """
    @overload
    def __init__(self, value: Array[CodeExpression]):
        """

        :param value:
        """
    @property
    def Capacity(self) -> int:
        """

        :return:
        """
    @Capacity.setter
    def Capacity(self, value: int) -> None: ...
    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def IsFixedSize(self) -> bool:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def IsSynchronized(self) -> bool:
        """

        :return:
        """
    @property
    def Item(self) -> object:
        """

        :return:
        """
    @Item.setter
    def Item(self, value: object) -> None: ...
    @property
    def SyncRoot(self) -> object:
        """

        :return:
        """
    @overload
    def Add(self, value: CodeExpression) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def Add(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def AddRange(self, value: CodeExpressionCollection) -> None:
        """

        :param value:
        """
    @overload
    def AddRange(self, value: Array[CodeExpression]) -> None:
        """

        :param value:
        """
    def Clear(self) -> None:
        """"""
    @overload
    def Contains(self, value: CodeExpression) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def Contains(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    @overload
    def CopyTo(self, array: Array[CodeExpression], index: int) -> None:
        """

        :param array:
        :param index:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def IndexOf(self, value: CodeExpression) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def IndexOf(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def Insert(self, index: int, value: CodeExpression) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def Insert(self, index: int, value: object) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def Remove(self, value: CodeExpression) -> None:
        """

        :param value:
        """
    @overload
    def Remove(self, value: object) -> None:
        """

        :param value:
        """
    def RemoveAt(self, index: int) -> None:
        """

        :param index:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def __contains__(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    def __getitem__(self, index: int) -> object:
        """

        :param index:
        :return:
        """
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    def __len__(self) -> int:
        """

        :return:
        """
    @overload
    def __setitem__(self, index: int, value: CodeExpression) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def __setitem__(self, index: int, value: object) -> None:
        """

        :param index:
        :param value:
        """

class CodeExpressionStatement(CodeStatement):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, expression: CodeExpression):
        """

        :param expression:
        """
    @property
    def EndDirectives(self) -> CodeDirectiveCollection:
        """

        :return:
        """
    @property
    def Expression(self) -> CodeExpression:
        """

        :return:
        """
    @Expression.setter
    def Expression(self, value: CodeExpression) -> None: ...
    @property
    def LinePragma(self) -> CodeLinePragma:
        """

        :return:
        """
    @LinePragma.setter
    def LinePragma(self, value: CodeLinePragma) -> None: ...
    @property
    def StartDirectives(self) -> CodeDirectiveCollection:
        """

        :return:
        """
    @property
    def UserData(self) -> IDictionary:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CodeFieldReferenceExpression(CodeExpression):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, targetObject: CodeExpression, fieldName: str):
        """

        :param targetObject:
        :param fieldName:
        """
    @property
    def FieldName(self) -> str:
        """

        :return:
        """
    @FieldName.setter
    def FieldName(self, value: str) -> None: ...
    @property
    def TargetObject(self) -> CodeExpression:
        """

        :return:
        """
    @TargetObject.setter
    def TargetObject(self, value: CodeExpression) -> None: ...
    @property
    def UserData(self) -> IDictionary:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CodeGotoStatement(CodeStatement):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, label: str):
        """

        :param label:
        """
    @property
    def EndDirectives(self) -> CodeDirectiveCollection:
        """

        :return:
        """
    @property
    def Label(self) -> str:
        """

        :return:
        """
    @Label.setter
    def Label(self, value: str) -> None: ...
    @property
    def LinePragma(self) -> CodeLinePragma:
        """

        :return:
        """
    @LinePragma.setter
    def LinePragma(self, value: CodeLinePragma) -> None: ...
    @property
    def StartDirectives(self) -> CodeDirectiveCollection:
        """

        :return:
        """
    @property
    def UserData(self) -> IDictionary:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CodeIndexerExpression(CodeExpression):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, targetObject: CodeExpression, indices: Array[CodeExpression]):
        """

        :param targetObject:
        :param indices:
        """
    @property
    def Indices(self) -> CodeExpressionCollection:
        """

        :return:
        """
    @property
    def TargetObject(self) -> CodeExpression:
        """

        :return:
        """
    @TargetObject.setter
    def TargetObject(self, value: CodeExpression) -> None: ...
    @property
    def UserData(self) -> IDictionary:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CodeIterationStatement(CodeStatement):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(
        self,
        initStatement: CodeStatement,
        testExpression: CodeExpression,
        incrementStatement: CodeStatement,
        statements: Array[CodeStatement],
    ):
        """

        :param initStatement:
        :param testExpression:
        :param incrementStatement:
        :param statements:
        """
    @property
    def EndDirectives(self) -> CodeDirectiveCollection:
        """

        :return:
        """
    @property
    def IncrementStatement(self) -> CodeStatement:
        """

        :return:
        """
    @IncrementStatement.setter
    def IncrementStatement(self, value: CodeStatement) -> None: ...
    @property
    def InitStatement(self) -> CodeStatement:
        """

        :return:
        """
    @InitStatement.setter
    def InitStatement(self, value: CodeStatement) -> None: ...
    @property
    def LinePragma(self) -> CodeLinePragma:
        """

        :return:
        """
    @LinePragma.setter
    def LinePragma(self, value: CodeLinePragma) -> None: ...
    @property
    def StartDirectives(self) -> CodeDirectiveCollection:
        """

        :return:
        """
    @property
    def Statements(self) -> CodeStatementCollection:
        """

        :return:
        """
    @property
    def TestExpression(self) -> CodeExpression:
        """

        :return:
        """
    @TestExpression.setter
    def TestExpression(self, value: CodeExpression) -> None: ...
    @property
    def UserData(self) -> IDictionary:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CodeLabeledStatement(CodeStatement):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, label: str):
        """

        :param label:
        """
    @overload
    def __init__(self, label: str, statement: CodeStatement):
        """

        :param label:
        :param statement:
        """
    @property
    def EndDirectives(self) -> CodeDirectiveCollection:
        """

        :return:
        """
    @property
    def Label(self) -> str:
        """

        :return:
        """
    @Label.setter
    def Label(self, value: str) -> None: ...
    @property
    def LinePragma(self) -> CodeLinePragma:
        """

        :return:
        """
    @LinePragma.setter
    def LinePragma(self, value: CodeLinePragma) -> None: ...
    @property
    def StartDirectives(self) -> CodeDirectiveCollection:
        """

        :return:
        """
    @property
    def Statement(self) -> CodeStatement:
        """

        :return:
        """
    @Statement.setter
    def Statement(self, value: CodeStatement) -> None: ...
    @property
    def UserData(self) -> IDictionary:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CodeLinePragma(Object):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, fileName: str, lineNumber: int):
        """

        :param fileName:
        :param lineNumber:
        """
    @property
    def FileName(self) -> str:
        """

        :return:
        """
    @FileName.setter
    def FileName(self, value: str) -> None: ...
    @property
    def LineNumber(self) -> int:
        """

        :return:
        """
    @LineNumber.setter
    def LineNumber(self, value: int) -> None: ...
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CodeMemberEvent(CodeTypeMember):
    """"""

    def __init__(self):
        """"""
    @property
    def Attributes(self) -> MemberAttributes:
        """

        :return:
        """
    @Attributes.setter
    def Attributes(self, value: MemberAttributes) -> None: ...
    @property
    def Comments(self) -> CodeCommentStatementCollection:
        """

        :return:
        """
    @property
    def CustomAttributes(self) -> CodeAttributeDeclarationCollection:
        """

        :return:
        """
    @CustomAttributes.setter
    def CustomAttributes(self, value: CodeAttributeDeclarationCollection) -> None: ...
    @property
    def EndDirectives(self) -> CodeDirectiveCollection:
        """

        :return:
        """
    @property
    def ImplementationTypes(self) -> CodeTypeReferenceCollection:
        """

        :return:
        """
    @property
    def LinePragma(self) -> CodeLinePragma:
        """

        :return:
        """
    @LinePragma.setter
    def LinePragma(self, value: CodeLinePragma) -> None: ...
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def PrivateImplementationType(self) -> CodeTypeReference:
        """

        :return:
        """
    @PrivateImplementationType.setter
    def PrivateImplementationType(self, value: CodeTypeReference) -> None: ...
    @property
    def StartDirectives(self) -> CodeDirectiveCollection:
        """

        :return:
        """
    @property
    def Type(self) -> CodeTypeReference:
        """

        :return:
        """
    @Type.setter
    def Type(self, value: CodeTypeReference) -> None: ...
    @property
    def UserData(self) -> IDictionary:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CodeMemberField(CodeTypeMember):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, type: CodeTypeReference, name: str):
        """

        :param type:
        :param name:
        """
    @overload
    def __init__(self, type: str, name: str):
        """

        :param type:
        :param name:
        """
    @overload
    def __init__(self, type: Type, name: str):
        """

        :param type:
        :param name:
        """
    @property
    def Attributes(self) -> MemberAttributes:
        """

        :return:
        """
    @Attributes.setter
    def Attributes(self, value: MemberAttributes) -> None: ...
    @property
    def Comments(self) -> CodeCommentStatementCollection:
        """

        :return:
        """
    @property
    def CustomAttributes(self) -> CodeAttributeDeclarationCollection:
        """

        :return:
        """
    @CustomAttributes.setter
    def CustomAttributes(self, value: CodeAttributeDeclarationCollection) -> None: ...
    @property
    def EndDirectives(self) -> CodeDirectiveCollection:
        """

        :return:
        """
    @property
    def InitExpression(self) -> CodeExpression:
        """

        :return:
        """
    @InitExpression.setter
    def InitExpression(self, value: CodeExpression) -> None: ...
    @property
    def LinePragma(self) -> CodeLinePragma:
        """

        :return:
        """
    @LinePragma.setter
    def LinePragma(self, value: CodeLinePragma) -> None: ...
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def StartDirectives(self) -> CodeDirectiveCollection:
        """

        :return:
        """
    @property
    def Type(self) -> CodeTypeReference:
        """

        :return:
        """
    @Type.setter
    def Type(self, value: CodeTypeReference) -> None: ...
    @property
    def UserData(self) -> IDictionary:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CodeMemberMethod(CodeTypeMember):
    """"""

    def __init__(self):
        """"""
    @property
    def Attributes(self) -> MemberAttributes:
        """

        :return:
        """
    @Attributes.setter
    def Attributes(self, value: MemberAttributes) -> None: ...
    @property
    def Comments(self) -> CodeCommentStatementCollection:
        """

        :return:
        """
    @property
    def CustomAttributes(self) -> CodeAttributeDeclarationCollection:
        """

        :return:
        """
    @CustomAttributes.setter
    def CustomAttributes(self, value: CodeAttributeDeclarationCollection) -> None: ...
    @property
    def EndDirectives(self) -> CodeDirectiveCollection:
        """

        :return:
        """
    @property
    def ImplementationTypes(self) -> CodeTypeReferenceCollection:
        """

        :return:
        """
    @property
    def LinePragma(self) -> CodeLinePragma:
        """

        :return:
        """
    @LinePragma.setter
    def LinePragma(self, value: CodeLinePragma) -> None: ...
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def Parameters(self) -> CodeParameterDeclarationExpressionCollection:
        """

        :return:
        """
    @property
    def PrivateImplementationType(self) -> CodeTypeReference:
        """

        :return:
        """
    @PrivateImplementationType.setter
    def PrivateImplementationType(self, value: CodeTypeReference) -> None: ...
    @property
    def ReturnType(self) -> CodeTypeReference:
        """

        :return:
        """
    @ReturnType.setter
    def ReturnType(self, value: CodeTypeReference) -> None: ...
    @property
    def ReturnTypeCustomAttributes(self) -> CodeAttributeDeclarationCollection:
        """

        :return:
        """
    @property
    def StartDirectives(self) -> CodeDirectiveCollection:
        """

        :return:
        """
    @property
    def Statements(self) -> CodeStatementCollection:
        """

        :return:
        """
    @property
    def TypeParameters(self) -> CodeTypeParameterCollection:
        """

        :return:
        """
    @property
    def UserData(self) -> IDictionary:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    PopulateImplementationTypes: EventType[EventHandler] = ...
    """"""
    PopulateParameters: EventType[EventHandler] = ...
    """"""
    PopulateStatements: EventType[EventHandler] = ...
    """"""

class CodeMemberProperty(CodeTypeMember):
    """"""

    def __init__(self):
        """"""
    @property
    def Attributes(self) -> MemberAttributes:
        """

        :return:
        """
    @Attributes.setter
    def Attributes(self, value: MemberAttributes) -> None: ...
    @property
    def Comments(self) -> CodeCommentStatementCollection:
        """

        :return:
        """
    @property
    def CustomAttributes(self) -> CodeAttributeDeclarationCollection:
        """

        :return:
        """
    @CustomAttributes.setter
    def CustomAttributes(self, value: CodeAttributeDeclarationCollection) -> None: ...
    @property
    def EndDirectives(self) -> CodeDirectiveCollection:
        """

        :return:
        """
    @property
    def GetStatements(self) -> CodeStatementCollection:
        """

        :return:
        """
    @property
    def HasGet(self) -> bool:
        """

        :return:
        """
    @HasGet.setter
    def HasGet(self, value: bool) -> None: ...
    @property
    def HasSet(self) -> bool:
        """

        :return:
        """
    @HasSet.setter
    def HasSet(self, value: bool) -> None: ...
    @property
    def ImplementationTypes(self) -> CodeTypeReferenceCollection:
        """

        :return:
        """
    @property
    def LinePragma(self) -> CodeLinePragma:
        """

        :return:
        """
    @LinePragma.setter
    def LinePragma(self, value: CodeLinePragma) -> None: ...
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def Parameters(self) -> CodeParameterDeclarationExpressionCollection:
        """

        :return:
        """
    @property
    def PrivateImplementationType(self) -> CodeTypeReference:
        """

        :return:
        """
    @PrivateImplementationType.setter
    def PrivateImplementationType(self, value: CodeTypeReference) -> None: ...
    @property
    def SetStatements(self) -> CodeStatementCollection:
        """

        :return:
        """
    @property
    def StartDirectives(self) -> CodeDirectiveCollection:
        """

        :return:
        """
    @property
    def Type(self) -> CodeTypeReference:
        """

        :return:
        """
    @Type.setter
    def Type(self, value: CodeTypeReference) -> None: ...
    @property
    def UserData(self) -> IDictionary:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CodeMethodInvokeExpression(CodeExpression):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, method: CodeMethodReferenceExpression, parameters: Array[CodeExpression]):
        """

        :param method:
        :param parameters:
        """
    @overload
    def __init__(
        self, targetObject: CodeExpression, methodName: str, parameters: Array[CodeExpression]
    ):
        """

        :param targetObject:
        :param methodName:
        :param parameters:
        """
    @property
    def Method(self) -> CodeMethodReferenceExpression:
        """

        :return:
        """
    @Method.setter
    def Method(self, value: CodeMethodReferenceExpression) -> None: ...
    @property
    def Parameters(self) -> CodeExpressionCollection:
        """

        :return:
        """
    @property
    def UserData(self) -> IDictionary:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CodeMethodReferenceExpression(CodeExpression):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, targetObject: CodeExpression, methodName: str):
        """

        :param targetObject:
        :param methodName:
        """
    @overload
    def __init__(
        self,
        targetObject: CodeExpression,
        methodName: str,
        typeParameters: Array[CodeTypeReference],
    ):
        """

        :param targetObject:
        :param methodName:
        :param typeParameters:
        """
    @property
    def MethodName(self) -> str:
        """

        :return:
        """
    @MethodName.setter
    def MethodName(self, value: str) -> None: ...
    @property
    def TargetObject(self) -> CodeExpression:
        """

        :return:
        """
    @TargetObject.setter
    def TargetObject(self, value: CodeExpression) -> None: ...
    @property
    def TypeArguments(self) -> CodeTypeReferenceCollection:
        """

        :return:
        """
    @property
    def UserData(self) -> IDictionary:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CodeMethodReturnStatement(CodeStatement):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, expression: CodeExpression):
        """

        :param expression:
        """
    @property
    def EndDirectives(self) -> CodeDirectiveCollection:
        """

        :return:
        """
    @property
    def Expression(self) -> CodeExpression:
        """

        :return:
        """
    @Expression.setter
    def Expression(self, value: CodeExpression) -> None: ...
    @property
    def LinePragma(self) -> CodeLinePragma:
        """

        :return:
        """
    @LinePragma.setter
    def LinePragma(self, value: CodeLinePragma) -> None: ...
    @property
    def StartDirectives(self) -> CodeDirectiveCollection:
        """

        :return:
        """
    @property
    def UserData(self) -> IDictionary:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CodeNamespace(CodeObject):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, name: str):
        """

        :param name:
        """
    @property
    def Comments(self) -> CodeCommentStatementCollection:
        """

        :return:
        """
    @property
    def Imports(self) -> CodeNamespaceImportCollection:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def Types(self) -> CodeTypeDeclarationCollection:
        """

        :return:
        """
    @property
    def UserData(self) -> IDictionary:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    PopulateComments: EventType[EventHandler] = ...
    """"""
    PopulateImports: EventType[EventHandler] = ...
    """"""
    PopulateTypes: EventType[EventHandler] = ...
    """"""

class CodeNamespaceCollection(CollectionBase, ICollection, IEnumerable, IList):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, value: CodeNamespaceCollection):
        """

        :param value:
        """
    @overload
    def __init__(self, value: Array[CodeNamespace]):
        """

        :param value:
        """
    @property
    def Capacity(self) -> int:
        """

        :return:
        """
    @Capacity.setter
    def Capacity(self, value: int) -> None: ...
    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def IsFixedSize(self) -> bool:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def IsSynchronized(self) -> bool:
        """

        :return:
        """
    @property
    def Item(self) -> object:
        """

        :return:
        """
    @Item.setter
    def Item(self, value: object) -> None: ...
    @property
    def SyncRoot(self) -> object:
        """

        :return:
        """
    @overload
    def Add(self, value: CodeNamespace) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def Add(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def AddRange(self, value: CodeNamespaceCollection) -> None:
        """

        :param value:
        """
    @overload
    def AddRange(self, value: Array[CodeNamespace]) -> None:
        """

        :param value:
        """
    def Clear(self) -> None:
        """"""
    @overload
    def Contains(self, value: CodeNamespace) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def Contains(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    @overload
    def CopyTo(self, array: Array[CodeNamespace], index: int) -> None:
        """

        :param array:
        :param index:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def IndexOf(self, value: CodeNamespace) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def IndexOf(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def Insert(self, index: int, value: CodeNamespace) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def Insert(self, index: int, value: object) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def Remove(self, value: CodeNamespace) -> None:
        """

        :param value:
        """
    @overload
    def Remove(self, value: object) -> None:
        """

        :param value:
        """
    def RemoveAt(self, index: int) -> None:
        """

        :param index:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def __contains__(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    def __getitem__(self, index: int) -> object:
        """

        :param index:
        :return:
        """
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    def __len__(self) -> int:
        """

        :return:
        """
    @overload
    def __setitem__(self, index: int, value: CodeNamespace) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def __setitem__(self, index: int, value: object) -> None:
        """

        :param index:
        :param value:
        """

class CodeNamespaceImport(CodeObject):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, nameSpace: str):
        """

        :param nameSpace:
        """
    @property
    def LinePragma(self) -> CodeLinePragma:
        """

        :return:
        """
    @LinePragma.setter
    def LinePragma(self, value: CodeLinePragma) -> None: ...
    @property
    def Namespace(self) -> str:
        """

        :return:
        """
    @Namespace.setter
    def Namespace(self, value: str) -> None: ...
    @property
    def UserData(self) -> IDictionary:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CodeNamespaceImportCollection(Object, ICollection, IEnumerable, IList):
    """"""

    def __init__(self):
        """"""
    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def IsFixedSize(self) -> bool:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def IsSynchronized(self) -> bool:
        """

        :return:
        """
    @property
    def Item(self) -> object:
        """

        :return:
        """
    @Item.setter
    def Item(self, value: object) -> None: ...
    @property
    def SyncRoot(self) -> object:
        """

        :return:
        """
    @overload
    def Add(self, value: CodeNamespaceImport) -> None:
        """

        :param value:
        """
    @overload
    def Add(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    def AddRange(self, value: Array[CodeNamespaceImport]) -> None:
        """

        :param value:
        """
    def Clear(self) -> None:
        """"""
    def Contains(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def IndexOf(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    def Insert(self, index: int, value: object) -> None:
        """

        :param index:
        :param value:
        """
    def Remove(self, value: object) -> None:
        """

        :param value:
        """
    def RemoveAt(self, index: int) -> None:
        """

        :param index:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def __contains__(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    def __getitem__(self, index: int) -> object:
        """

        :param index:
        :return:
        """
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    def __len__(self) -> int:
        """

        :return:
        """
    @overload
    def __setitem__(self, index: int, value: CodeNamespaceImport) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def __setitem__(self, index: int, value: object) -> None:
        """

        :param index:
        :param value:
        """

class CodeObject(Object):
    """"""

    def __init__(self):
        """"""
    @property
    def UserData(self) -> IDictionary:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CodeObjectCreateExpression(CodeExpression):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, createType: CodeTypeReference, parameters: Array[CodeExpression]):
        """

        :param createType:
        :param parameters:
        """
    @overload
    def __init__(self, createType: str, parameters: Array[CodeExpression]):
        """

        :param createType:
        :param parameters:
        """
    @overload
    def __init__(self, createType: Type, parameters: Array[CodeExpression]):
        """

        :param createType:
        :param parameters:
        """
    @property
    def CreateType(self) -> CodeTypeReference:
        """

        :return:
        """
    @CreateType.setter
    def CreateType(self, value: CodeTypeReference) -> None: ...
    @property
    def Parameters(self) -> CodeExpressionCollection:
        """

        :return:
        """
    @property
    def UserData(self) -> IDictionary:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CodeParameterDeclarationExpression(CodeExpression):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, type: CodeTypeReference, name: str):
        """

        :param type:
        :param name:
        """
    @overload
    def __init__(self, type: str, name: str):
        """

        :param type:
        :param name:
        """
    @overload
    def __init__(self, type: Type, name: str):
        """

        :param type:
        :param name:
        """
    @property
    def CustomAttributes(self) -> CodeAttributeDeclarationCollection:
        """

        :return:
        """
    @CustomAttributes.setter
    def CustomAttributes(self, value: CodeAttributeDeclarationCollection) -> None: ...
    @property
    def Direction(self) -> FieldDirection:
        """

        :return:
        """
    @Direction.setter
    def Direction(self, value: FieldDirection) -> None: ...
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def Type(self) -> CodeTypeReference:
        """

        :return:
        """
    @Type.setter
    def Type(self, value: CodeTypeReference) -> None: ...
    @property
    def UserData(self) -> IDictionary:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CodeParameterDeclarationExpressionCollection(CollectionBase, ICollection, IEnumerable, IList):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, value: CodeParameterDeclarationExpressionCollection):
        """

        :param value:
        """
    @overload
    def __init__(self, value: Array[CodeParameterDeclarationExpression]):
        """

        :param value:
        """
    @property
    def Capacity(self) -> int:
        """

        :return:
        """
    @Capacity.setter
    def Capacity(self, value: int) -> None: ...
    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def IsFixedSize(self) -> bool:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def IsSynchronized(self) -> bool:
        """

        :return:
        """
    @property
    def Item(self) -> object:
        """

        :return:
        """
    @Item.setter
    def Item(self, value: object) -> None: ...
    @property
    def SyncRoot(self) -> object:
        """

        :return:
        """
    @overload
    def Add(self, value: CodeParameterDeclarationExpression) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def Add(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def AddRange(self, value: CodeParameterDeclarationExpressionCollection) -> None:
        """

        :param value:
        """
    @overload
    def AddRange(self, value: Array[CodeParameterDeclarationExpression]) -> None:
        """

        :param value:
        """
    def Clear(self) -> None:
        """"""
    @overload
    def Contains(self, value: CodeParameterDeclarationExpression) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def Contains(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    @overload
    def CopyTo(self, array: Array[CodeParameterDeclarationExpression], index: int) -> None:
        """

        :param array:
        :param index:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def IndexOf(self, value: CodeParameterDeclarationExpression) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def IndexOf(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def Insert(self, index: int, value: CodeParameterDeclarationExpression) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def Insert(self, index: int, value: object) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def Remove(self, value: CodeParameterDeclarationExpression) -> None:
        """

        :param value:
        """
    @overload
    def Remove(self, value: object) -> None:
        """

        :param value:
        """
    def RemoveAt(self, index: int) -> None:
        """

        :param index:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def __contains__(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    def __getitem__(self, index: int) -> object:
        """

        :param index:
        :return:
        """
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    def __len__(self) -> int:
        """

        :return:
        """
    @overload
    def __setitem__(self, index: int, value: CodeParameterDeclarationExpression) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def __setitem__(self, index: int, value: object) -> None:
        """

        :param index:
        :param value:
        """

class CodePrimitiveExpression(CodeExpression):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, value: object):
        """

        :param value:
        """
    @property
    def UserData(self) -> IDictionary:
        """

        :return:
        """
    @property
    def Value(self) -> object:
        """

        :return:
        """
    @Value.setter
    def Value(self, value: object) -> None: ...
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CodePropertyReferenceExpression(CodeExpression):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, targetObject: CodeExpression, propertyName: str):
        """

        :param targetObject:
        :param propertyName:
        """
    @property
    def PropertyName(self) -> str:
        """

        :return:
        """
    @PropertyName.setter
    def PropertyName(self, value: str) -> None: ...
    @property
    def TargetObject(self) -> CodeExpression:
        """

        :return:
        """
    @TargetObject.setter
    def TargetObject(self, value: CodeExpression) -> None: ...
    @property
    def UserData(self) -> IDictionary:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CodePropertySetValueReferenceExpression(CodeExpression):
    """"""

    def __init__(self):
        """"""
    @property
    def UserData(self) -> IDictionary:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CodeRegionDirective(CodeDirective):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, regionMode: CodeRegionMode, regionText: str):
        """

        :param regionMode:
        :param regionText:
        """
    @property
    def RegionMode(self) -> CodeRegionMode:
        """

        :return:
        """
    @RegionMode.setter
    def RegionMode(self, value: CodeRegionMode) -> None: ...
    @property
    def RegionText(self) -> str:
        """

        :return:
        """
    @RegionText.setter
    def RegionText(self, value: str) -> None: ...
    @property
    def UserData(self) -> IDictionary:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CodeRegionMode(Enum):
    """"""

    _None: CodeRegionMode = ...
    """"""
    Start: CodeRegionMode = ...
    """"""
    End: CodeRegionMode = ...
    """"""

class CodeRemoveEventStatement(CodeStatement):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, eventRef: CodeEventReferenceExpression, listener: CodeExpression):
        """

        :param eventRef:
        :param listener:
        """
    @overload
    def __init__(self, targetObject: CodeExpression, eventName: str, listener: CodeExpression):
        """

        :param targetObject:
        :param eventName:
        :param listener:
        """
    @property
    def EndDirectives(self) -> CodeDirectiveCollection:
        """

        :return:
        """
    @property
    def Event(self) -> CodeEventReferenceExpression:
        """

        :return:
        """
    @Event.setter
    def Event(self, value: CodeEventReferenceExpression) -> None: ...
    @property
    def LinePragma(self) -> CodeLinePragma:
        """

        :return:
        """
    @LinePragma.setter
    def LinePragma(self, value: CodeLinePragma) -> None: ...
    @property
    def Listener(self) -> CodeExpression:
        """

        :return:
        """
    @Listener.setter
    def Listener(self, value: CodeExpression) -> None: ...
    @property
    def StartDirectives(self) -> CodeDirectiveCollection:
        """

        :return:
        """
    @property
    def UserData(self) -> IDictionary:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CodeSnippetCompileUnit(CodeCompileUnit):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, value: str):
        """

        :param value:
        """
    @property
    def AssemblyCustomAttributes(self) -> CodeAttributeDeclarationCollection:
        """

        :return:
        """
    @property
    def EndDirectives(self) -> CodeDirectiveCollection:
        """

        :return:
        """
    @property
    def LinePragma(self) -> CodeLinePragma:
        """

        :return:
        """
    @LinePragma.setter
    def LinePragma(self, value: CodeLinePragma) -> None: ...
    @property
    def Namespaces(self) -> CodeNamespaceCollection:
        """

        :return:
        """
    @property
    def ReferencedAssemblies(self) -> StringCollection:
        """

        :return:
        """
    @property
    def StartDirectives(self) -> CodeDirectiveCollection:
        """

        :return:
        """
    @property
    def UserData(self) -> IDictionary:
        """

        :return:
        """
    @property
    def Value(self) -> str:
        """

        :return:
        """
    @Value.setter
    def Value(self, value: str) -> None: ...
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CodeSnippetExpression(CodeExpression):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, value: str):
        """

        :param value:
        """
    @property
    def UserData(self) -> IDictionary:
        """

        :return:
        """
    @property
    def Value(self) -> str:
        """

        :return:
        """
    @Value.setter
    def Value(self, value: str) -> None: ...
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CodeSnippetStatement(CodeStatement):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, value: str):
        """

        :param value:
        """
    @property
    def EndDirectives(self) -> CodeDirectiveCollection:
        """

        :return:
        """
    @property
    def LinePragma(self) -> CodeLinePragma:
        """

        :return:
        """
    @LinePragma.setter
    def LinePragma(self, value: CodeLinePragma) -> None: ...
    @property
    def StartDirectives(self) -> CodeDirectiveCollection:
        """

        :return:
        """
    @property
    def UserData(self) -> IDictionary:
        """

        :return:
        """
    @property
    def Value(self) -> str:
        """

        :return:
        """
    @Value.setter
    def Value(self, value: str) -> None: ...
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CodeSnippetTypeMember(CodeTypeMember):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, text: str):
        """

        :param text:
        """
    @property
    def Attributes(self) -> MemberAttributes:
        """

        :return:
        """
    @Attributes.setter
    def Attributes(self, value: MemberAttributes) -> None: ...
    @property
    def Comments(self) -> CodeCommentStatementCollection:
        """

        :return:
        """
    @property
    def CustomAttributes(self) -> CodeAttributeDeclarationCollection:
        """

        :return:
        """
    @CustomAttributes.setter
    def CustomAttributes(self, value: CodeAttributeDeclarationCollection) -> None: ...
    @property
    def EndDirectives(self) -> CodeDirectiveCollection:
        """

        :return:
        """
    @property
    def LinePragma(self) -> CodeLinePragma:
        """

        :return:
        """
    @LinePragma.setter
    def LinePragma(self, value: CodeLinePragma) -> None: ...
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def StartDirectives(self) -> CodeDirectiveCollection:
        """

        :return:
        """
    @property
    def Text(self) -> str:
        """

        :return:
        """
    @Text.setter
    def Text(self, value: str) -> None: ...
    @property
    def UserData(self) -> IDictionary:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CodeStatement(CodeObject):
    """"""

    def __init__(self):
        """"""
    @property
    def EndDirectives(self) -> CodeDirectiveCollection:
        """

        :return:
        """
    @property
    def LinePragma(self) -> CodeLinePragma:
        """

        :return:
        """
    @LinePragma.setter
    def LinePragma(self, value: CodeLinePragma) -> None: ...
    @property
    def StartDirectives(self) -> CodeDirectiveCollection:
        """

        :return:
        """
    @property
    def UserData(self) -> IDictionary:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CodeStatementCollection(CollectionBase, ICollection, IEnumerable, IList):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, value: CodeStatementCollection):
        """

        :param value:
        """
    @overload
    def __init__(self, value: Array[CodeStatement]):
        """

        :param value:
        """
    @property
    def Capacity(self) -> int:
        """

        :return:
        """
    @Capacity.setter
    def Capacity(self, value: int) -> None: ...
    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def IsFixedSize(self) -> bool:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def IsSynchronized(self) -> bool:
        """

        :return:
        """
    @property
    def Item(self) -> object:
        """

        :return:
        """
    @Item.setter
    def Item(self, value: object) -> None: ...
    @property
    def SyncRoot(self) -> object:
        """

        :return:
        """
    @overload
    def Add(self, value: CodeExpression) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def Add(self, value: CodeStatement) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def Add(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def AddRange(self, value: CodeStatementCollection) -> None:
        """

        :param value:
        """
    @overload
    def AddRange(self, value: Array[CodeStatement]) -> None:
        """

        :param value:
        """
    def Clear(self) -> None:
        """"""
    @overload
    def Contains(self, value: CodeStatement) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def Contains(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    @overload
    def CopyTo(self, array: Array[CodeStatement], index: int) -> None:
        """

        :param array:
        :param index:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def IndexOf(self, value: CodeStatement) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def IndexOf(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def Insert(self, index: int, value: CodeStatement) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def Insert(self, index: int, value: object) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def Remove(self, value: CodeStatement) -> None:
        """

        :param value:
        """
    @overload
    def Remove(self, value: object) -> None:
        """

        :param value:
        """
    def RemoveAt(self, index: int) -> None:
        """

        :param index:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def __contains__(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    def __getitem__(self, index: int) -> object:
        """

        :param index:
        :return:
        """
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    def __len__(self) -> int:
        """

        :return:
        """
    @overload
    def __setitem__(self, index: int, value: CodeStatement) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def __setitem__(self, index: int, value: object) -> None:
        """

        :param index:
        :param value:
        """

class CodeThisReferenceExpression(CodeExpression):
    """"""

    def __init__(self):
        """"""
    @property
    def UserData(self) -> IDictionary:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CodeThrowExceptionStatement(CodeStatement):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, toThrow: CodeExpression):
        """

        :param toThrow:
        """
    @property
    def EndDirectives(self) -> CodeDirectiveCollection:
        """

        :return:
        """
    @property
    def LinePragma(self) -> CodeLinePragma:
        """

        :return:
        """
    @LinePragma.setter
    def LinePragma(self, value: CodeLinePragma) -> None: ...
    @property
    def StartDirectives(self) -> CodeDirectiveCollection:
        """

        :return:
        """
    @property
    def ToThrow(self) -> CodeExpression:
        """

        :return:
        """
    @ToThrow.setter
    def ToThrow(self, value: CodeExpression) -> None: ...
    @property
    def UserData(self) -> IDictionary:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CodeTryCatchFinallyStatement(CodeStatement):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, tryStatements: Array[CodeStatement], catchClauses: Array[CodeCatchClause]):
        """

        :param tryStatements:
        :param catchClauses:
        """
    @overload
    def __init__(
        self,
        tryStatements: Array[CodeStatement],
        catchClauses: Array[CodeCatchClause],
        finallyStatements: Array[CodeStatement],
    ):
        """

        :param tryStatements:
        :param catchClauses:
        :param finallyStatements:
        """
    @property
    def CatchClauses(self) -> CodeCatchClauseCollection:
        """

        :return:
        """
    @property
    def EndDirectives(self) -> CodeDirectiveCollection:
        """

        :return:
        """
    @property
    def FinallyStatements(self) -> CodeStatementCollection:
        """

        :return:
        """
    @property
    def LinePragma(self) -> CodeLinePragma:
        """

        :return:
        """
    @LinePragma.setter
    def LinePragma(self, value: CodeLinePragma) -> None: ...
    @property
    def StartDirectives(self) -> CodeDirectiveCollection:
        """

        :return:
        """
    @property
    def TryStatements(self) -> CodeStatementCollection:
        """

        :return:
        """
    @property
    def UserData(self) -> IDictionary:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CodeTypeConstructor(CodeMemberMethod):
    """"""

    def __init__(self):
        """"""
    @property
    def Attributes(self) -> MemberAttributes:
        """

        :return:
        """
    @Attributes.setter
    def Attributes(self, value: MemberAttributes) -> None: ...
    @property
    def Comments(self) -> CodeCommentStatementCollection:
        """

        :return:
        """
    @property
    def CustomAttributes(self) -> CodeAttributeDeclarationCollection:
        """

        :return:
        """
    @CustomAttributes.setter
    def CustomAttributes(self, value: CodeAttributeDeclarationCollection) -> None: ...
    @property
    def EndDirectives(self) -> CodeDirectiveCollection:
        """

        :return:
        """
    @property
    def ImplementationTypes(self) -> CodeTypeReferenceCollection:
        """

        :return:
        """
    @property
    def LinePragma(self) -> CodeLinePragma:
        """

        :return:
        """
    @LinePragma.setter
    def LinePragma(self, value: CodeLinePragma) -> None: ...
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def Parameters(self) -> CodeParameterDeclarationExpressionCollection:
        """

        :return:
        """
    @property
    def PrivateImplementationType(self) -> CodeTypeReference:
        """

        :return:
        """
    @PrivateImplementationType.setter
    def PrivateImplementationType(self, value: CodeTypeReference) -> None: ...
    @property
    def ReturnType(self) -> CodeTypeReference:
        """

        :return:
        """
    @ReturnType.setter
    def ReturnType(self, value: CodeTypeReference) -> None: ...
    @property
    def ReturnTypeCustomAttributes(self) -> CodeAttributeDeclarationCollection:
        """

        :return:
        """
    @property
    def StartDirectives(self) -> CodeDirectiveCollection:
        """

        :return:
        """
    @property
    def Statements(self) -> CodeStatementCollection:
        """

        :return:
        """
    @property
    def TypeParameters(self) -> CodeTypeParameterCollection:
        """

        :return:
        """
    @property
    def UserData(self) -> IDictionary:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    PopulateImplementationTypes: EventType[EventHandler] = ...
    """"""
    PopulateParameters: EventType[EventHandler] = ...
    """"""
    PopulateStatements: EventType[EventHandler] = ...
    """"""

class CodeTypeDeclaration(CodeTypeMember):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, name: str):
        """

        :param name:
        """
    @property
    def Attributes(self) -> MemberAttributes:
        """

        :return:
        """
    @Attributes.setter
    def Attributes(self, value: MemberAttributes) -> None: ...
    @property
    def BaseTypes(self) -> CodeTypeReferenceCollection:
        """

        :return:
        """
    @property
    def Comments(self) -> CodeCommentStatementCollection:
        """

        :return:
        """
    @property
    def CustomAttributes(self) -> CodeAttributeDeclarationCollection:
        """

        :return:
        """
    @CustomAttributes.setter
    def CustomAttributes(self, value: CodeAttributeDeclarationCollection) -> None: ...
    @property
    def EndDirectives(self) -> CodeDirectiveCollection:
        """

        :return:
        """
    @property
    def IsClass(self) -> bool:
        """

        :return:
        """
    @IsClass.setter
    def IsClass(self, value: bool) -> None: ...
    @property
    def IsEnum(self) -> bool:
        """

        :return:
        """
    @IsEnum.setter
    def IsEnum(self, value: bool) -> None: ...
    @property
    def IsInterface(self) -> bool:
        """

        :return:
        """
    @IsInterface.setter
    def IsInterface(self, value: bool) -> None: ...
    @property
    def IsPartial(self) -> bool:
        """

        :return:
        """
    @IsPartial.setter
    def IsPartial(self, value: bool) -> None: ...
    @property
    def IsStruct(self) -> bool:
        """

        :return:
        """
    @IsStruct.setter
    def IsStruct(self, value: bool) -> None: ...
    @property
    def LinePragma(self) -> CodeLinePragma:
        """

        :return:
        """
    @LinePragma.setter
    def LinePragma(self, value: CodeLinePragma) -> None: ...
    @property
    def Members(self) -> CodeTypeMemberCollection:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def StartDirectives(self) -> CodeDirectiveCollection:
        """

        :return:
        """
    @property
    def TypeAttributes(self) -> TypeAttributes:
        """

        :return:
        """
    @TypeAttributes.setter
    def TypeAttributes(self, value: TypeAttributes) -> None: ...
    @property
    def TypeParameters(self) -> CodeTypeParameterCollection:
        """

        :return:
        """
    @property
    def UserData(self) -> IDictionary:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    PopulateBaseTypes: EventType[EventHandler] = ...
    """"""
    PopulateMembers: EventType[EventHandler] = ...
    """"""

class CodeTypeDeclarationCollection(CollectionBase, ICollection, IEnumerable, IList):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, value: CodeTypeDeclarationCollection):
        """

        :param value:
        """
    @overload
    def __init__(self, value: Array[CodeTypeDeclaration]):
        """

        :param value:
        """
    @property
    def Capacity(self) -> int:
        """

        :return:
        """
    @Capacity.setter
    def Capacity(self, value: int) -> None: ...
    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def IsFixedSize(self) -> bool:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def IsSynchronized(self) -> bool:
        """

        :return:
        """
    @property
    def Item(self) -> object:
        """

        :return:
        """
    @Item.setter
    def Item(self, value: object) -> None: ...
    @property
    def SyncRoot(self) -> object:
        """

        :return:
        """
    @overload
    def Add(self, value: CodeTypeDeclaration) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def Add(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def AddRange(self, value: CodeTypeDeclarationCollection) -> None:
        """

        :param value:
        """
    @overload
    def AddRange(self, value: Array[CodeTypeDeclaration]) -> None:
        """

        :param value:
        """
    def Clear(self) -> None:
        """"""
    @overload
    def Contains(self, value: CodeTypeDeclaration) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def Contains(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    @overload
    def CopyTo(self, array: Array[CodeTypeDeclaration], index: int) -> None:
        """

        :param array:
        :param index:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def IndexOf(self, value: CodeTypeDeclaration) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def IndexOf(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def Insert(self, index: int, value: CodeTypeDeclaration) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def Insert(self, index: int, value: object) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def Remove(self, value: CodeTypeDeclaration) -> None:
        """

        :param value:
        """
    @overload
    def Remove(self, value: object) -> None:
        """

        :param value:
        """
    def RemoveAt(self, index: int) -> None:
        """

        :param index:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def __contains__(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    def __getitem__(self, index: int) -> object:
        """

        :param index:
        :return:
        """
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    def __len__(self) -> int:
        """

        :return:
        """
    @overload
    def __setitem__(self, index: int, value: CodeTypeDeclaration) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def __setitem__(self, index: int, value: object) -> None:
        """

        :param index:
        :param value:
        """

class CodeTypeDelegate(CodeTypeDeclaration):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, name: str):
        """

        :param name:
        """
    @property
    def Attributes(self) -> MemberAttributes:
        """

        :return:
        """
    @Attributes.setter
    def Attributes(self, value: MemberAttributes) -> None: ...
    @property
    def BaseTypes(self) -> CodeTypeReferenceCollection:
        """

        :return:
        """
    @property
    def Comments(self) -> CodeCommentStatementCollection:
        """

        :return:
        """
    @property
    def CustomAttributes(self) -> CodeAttributeDeclarationCollection:
        """

        :return:
        """
    @CustomAttributes.setter
    def CustomAttributes(self, value: CodeAttributeDeclarationCollection) -> None: ...
    @property
    def EndDirectives(self) -> CodeDirectiveCollection:
        """

        :return:
        """
    @property
    def IsClass(self) -> bool:
        """

        :return:
        """
    @IsClass.setter
    def IsClass(self, value: bool) -> None: ...
    @property
    def IsEnum(self) -> bool:
        """

        :return:
        """
    @IsEnum.setter
    def IsEnum(self, value: bool) -> None: ...
    @property
    def IsInterface(self) -> bool:
        """

        :return:
        """
    @IsInterface.setter
    def IsInterface(self, value: bool) -> None: ...
    @property
    def IsPartial(self) -> bool:
        """

        :return:
        """
    @IsPartial.setter
    def IsPartial(self, value: bool) -> None: ...
    @property
    def IsStruct(self) -> bool:
        """

        :return:
        """
    @IsStruct.setter
    def IsStruct(self, value: bool) -> None: ...
    @property
    def LinePragma(self) -> CodeLinePragma:
        """

        :return:
        """
    @LinePragma.setter
    def LinePragma(self, value: CodeLinePragma) -> None: ...
    @property
    def Members(self) -> CodeTypeMemberCollection:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def Parameters(self) -> CodeParameterDeclarationExpressionCollection:
        """

        :return:
        """
    @property
    def ReturnType(self) -> CodeTypeReference:
        """

        :return:
        """
    @ReturnType.setter
    def ReturnType(self, value: CodeTypeReference) -> None: ...
    @property
    def StartDirectives(self) -> CodeDirectiveCollection:
        """

        :return:
        """
    @property
    def TypeAttributes(self) -> TypeAttributes:
        """

        :return:
        """
    @TypeAttributes.setter
    def TypeAttributes(self, value: TypeAttributes) -> None: ...
    @property
    def TypeParameters(self) -> CodeTypeParameterCollection:
        """

        :return:
        """
    @property
    def UserData(self) -> IDictionary:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    PopulateBaseTypes: EventType[EventHandler] = ...
    """"""
    PopulateMembers: EventType[EventHandler] = ...
    """"""

class CodeTypeMember(CodeObject):
    """"""

    def __init__(self):
        """"""
    @property
    def Attributes(self) -> MemberAttributes:
        """

        :return:
        """
    @Attributes.setter
    def Attributes(self, value: MemberAttributes) -> None: ...
    @property
    def Comments(self) -> CodeCommentStatementCollection:
        """

        :return:
        """
    @property
    def CustomAttributes(self) -> CodeAttributeDeclarationCollection:
        """

        :return:
        """
    @CustomAttributes.setter
    def CustomAttributes(self, value: CodeAttributeDeclarationCollection) -> None: ...
    @property
    def EndDirectives(self) -> CodeDirectiveCollection:
        """

        :return:
        """
    @property
    def LinePragma(self) -> CodeLinePragma:
        """

        :return:
        """
    @LinePragma.setter
    def LinePragma(self, value: CodeLinePragma) -> None: ...
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def StartDirectives(self) -> CodeDirectiveCollection:
        """

        :return:
        """
    @property
    def UserData(self) -> IDictionary:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CodeTypeMemberCollection(CollectionBase, ICollection, IEnumerable, IList):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, value: CodeTypeMemberCollection):
        """

        :param value:
        """
    @overload
    def __init__(self, value: Array[CodeTypeMember]):
        """

        :param value:
        """
    @property
    def Capacity(self) -> int:
        """

        :return:
        """
    @Capacity.setter
    def Capacity(self, value: int) -> None: ...
    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def IsFixedSize(self) -> bool:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def IsSynchronized(self) -> bool:
        """

        :return:
        """
    @property
    def Item(self) -> object:
        """

        :return:
        """
    @Item.setter
    def Item(self, value: object) -> None: ...
    @property
    def SyncRoot(self) -> object:
        """

        :return:
        """
    @overload
    def Add(self, value: CodeTypeMember) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def Add(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def AddRange(self, value: CodeTypeMemberCollection) -> None:
        """

        :param value:
        """
    @overload
    def AddRange(self, value: Array[CodeTypeMember]) -> None:
        """

        :param value:
        """
    def Clear(self) -> None:
        """"""
    @overload
    def Contains(self, value: CodeTypeMember) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def Contains(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    @overload
    def CopyTo(self, array: Array[CodeTypeMember], index: int) -> None:
        """

        :param array:
        :param index:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def IndexOf(self, value: CodeTypeMember) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def IndexOf(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def Insert(self, index: int, value: CodeTypeMember) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def Insert(self, index: int, value: object) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def Remove(self, value: CodeTypeMember) -> None:
        """

        :param value:
        """
    @overload
    def Remove(self, value: object) -> None:
        """

        :param value:
        """
    def RemoveAt(self, index: int) -> None:
        """

        :param index:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def __contains__(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    def __getitem__(self, index: int) -> object:
        """

        :param index:
        :return:
        """
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    def __len__(self) -> int:
        """

        :return:
        """
    @overload
    def __setitem__(self, index: int, value: CodeTypeMember) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def __setitem__(self, index: int, value: object) -> None:
        """

        :param index:
        :param value:
        """

class CodeTypeOfExpression(CodeExpression):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, type: CodeTypeReference):
        """

        :param type:
        """
    @overload
    def __init__(self, type: str):
        """

        :param type:
        """
    @overload
    def __init__(self, type: Type):
        """

        :param type:
        """
    @property
    def Type(self) -> CodeTypeReference:
        """

        :return:
        """
    @Type.setter
    def Type(self, value: CodeTypeReference) -> None: ...
    @property
    def UserData(self) -> IDictionary:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CodeTypeParameter(CodeObject):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, name: str):
        """

        :param name:
        """
    @property
    def Constraints(self) -> CodeTypeReferenceCollection:
        """

        :return:
        """
    @property
    def CustomAttributes(self) -> CodeAttributeDeclarationCollection:
        """

        :return:
        """
    @property
    def HasConstructorConstraint(self) -> bool:
        """

        :return:
        """
    @HasConstructorConstraint.setter
    def HasConstructorConstraint(self, value: bool) -> None: ...
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def UserData(self) -> IDictionary:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CodeTypeParameterCollection(CollectionBase, ICollection, IEnumerable, IList):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, value: CodeTypeParameterCollection):
        """

        :param value:
        """
    @overload
    def __init__(self, value: Array[CodeTypeParameter]):
        """

        :param value:
        """
    @property
    def Capacity(self) -> int:
        """

        :return:
        """
    @Capacity.setter
    def Capacity(self, value: int) -> None: ...
    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def IsFixedSize(self) -> bool:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def IsSynchronized(self) -> bool:
        """

        :return:
        """
    @property
    def Item(self) -> object:
        """

        :return:
        """
    @Item.setter
    def Item(self, value: object) -> None: ...
    @property
    def SyncRoot(self) -> object:
        """

        :return:
        """
    @overload
    def Add(self, value: CodeTypeParameter) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def Add(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def Add(self, value: str) -> None:
        """

        :param value:
        """
    @overload
    def AddRange(self, value: CodeTypeParameterCollection) -> None:
        """

        :param value:
        """
    @overload
    def AddRange(self, value: Array[CodeTypeParameter]) -> None:
        """

        :param value:
        """
    def Clear(self) -> None:
        """"""
    @overload
    def Contains(self, value: CodeTypeParameter) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def Contains(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    @overload
    def CopyTo(self, array: Array[CodeTypeParameter], index: int) -> None:
        """

        :param array:
        :param index:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def IndexOf(self, value: CodeTypeParameter) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def IndexOf(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def Insert(self, index: int, value: CodeTypeParameter) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def Insert(self, index: int, value: object) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def Remove(self, value: CodeTypeParameter) -> None:
        """

        :param value:
        """
    @overload
    def Remove(self, value: object) -> None:
        """

        :param value:
        """
    def RemoveAt(self, index: int) -> None:
        """

        :param index:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def __contains__(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    def __getitem__(self, index: int) -> object:
        """

        :param index:
        :return:
        """
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    def __len__(self) -> int:
        """

        :return:
        """
    @overload
    def __setitem__(self, index: int, value: CodeTypeParameter) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def __setitem__(self, index: int, value: object) -> None:
        """

        :param index:
        :param value:
        """

class CodeTypeReference(CodeObject):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, typeParameter: CodeTypeParameter):
        """

        :param typeParameter:
        """
    @overload
    def __init__(self, typeName: str):
        """

        :param typeName:
        """
    @overload
    def __init__(self, type: Type):
        """

        :param type:
        """
    @overload
    def __init__(self, arrayType: CodeTypeReference, rank: int):
        """

        :param arrayType:
        :param rank:
        """
    @overload
    def __init__(self, typeName: str, codeTypeReferenceOption: CodeTypeReferenceOptions):
        """

        :param typeName:
        :param codeTypeReferenceOption:
        """
    @overload
    def __init__(self, typeName: str, typeArguments: Array[CodeTypeReference]):
        """

        :param typeName:
        :param typeArguments:
        """
    @overload
    def __init__(self, baseType: str, rank: int):
        """

        :param baseType:
        :param rank:
        """
    @overload
    def __init__(self, type: Type, codeTypeReferenceOption: CodeTypeReferenceOptions):
        """

        :param type:
        :param codeTypeReferenceOption:
        """
    @property
    def ArrayElementType(self) -> CodeTypeReference:
        """

        :return:
        """
    @ArrayElementType.setter
    def ArrayElementType(self, value: CodeTypeReference) -> None: ...
    @property
    def ArrayRank(self) -> int:
        """

        :return:
        """
    @ArrayRank.setter
    def ArrayRank(self, value: int) -> None: ...
    @property
    def BaseType(self) -> str:
        """

        :return:
        """
    @BaseType.setter
    def BaseType(self, value: str) -> None: ...
    @property
    def Options(self) -> CodeTypeReferenceOptions:
        """

        :return:
        """
    @Options.setter
    def Options(self, value: CodeTypeReferenceOptions) -> None: ...
    @property
    def TypeArguments(self) -> CodeTypeReferenceCollection:
        """

        :return:
        """
    @property
    def UserData(self) -> IDictionary:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CodeTypeReferenceCollection(CollectionBase, ICollection, IEnumerable, IList):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, value: CodeTypeReferenceCollection):
        """

        :param value:
        """
    @overload
    def __init__(self, value: Array[CodeTypeReference]):
        """

        :param value:
        """
    @property
    def Capacity(self) -> int:
        """

        :return:
        """
    @Capacity.setter
    def Capacity(self, value: int) -> None: ...
    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def IsFixedSize(self) -> bool:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def IsSynchronized(self) -> bool:
        """

        :return:
        """
    @property
    def Item(self) -> object:
        """

        :return:
        """
    @Item.setter
    def Item(self, value: object) -> None: ...
    @property
    def SyncRoot(self) -> object:
        """

        :return:
        """
    @overload
    def Add(self, value: CodeTypeReference) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def Add(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def Add(self, value: str) -> None:
        """

        :param value:
        """
    @overload
    def Add(self, value: Type) -> None:
        """

        :param value:
        """
    @overload
    def AddRange(self, value: CodeTypeReferenceCollection) -> None:
        """

        :param value:
        """
    @overload
    def AddRange(self, value: Array[CodeTypeReference]) -> None:
        """

        :param value:
        """
    def Clear(self) -> None:
        """"""
    @overload
    def Contains(self, value: CodeTypeReference) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def Contains(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    @overload
    def CopyTo(self, array: Array[CodeTypeReference], index: int) -> None:
        """

        :param array:
        :param index:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def IndexOf(self, value: CodeTypeReference) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def IndexOf(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def Insert(self, index: int, value: CodeTypeReference) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def Insert(self, index: int, value: object) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def Remove(self, value: CodeTypeReference) -> None:
        """

        :param value:
        """
    @overload
    def Remove(self, value: object) -> None:
        """

        :param value:
        """
    def RemoveAt(self, index: int) -> None:
        """

        :param index:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def __contains__(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    def __getitem__(self, index: int) -> object:
        """

        :param index:
        :return:
        """
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    def __len__(self) -> int:
        """

        :return:
        """
    @overload
    def __setitem__(self, index: int, value: CodeTypeReference) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def __setitem__(self, index: int, value: object) -> None:
        """

        :param index:
        :param value:
        """

class CodeTypeReferenceExpression(CodeExpression):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, type: CodeTypeReference):
        """

        :param type:
        """
    @overload
    def __init__(self, type: str):
        """

        :param type:
        """
    @overload
    def __init__(self, type: Type):
        """

        :param type:
        """
    @property
    def Type(self) -> CodeTypeReference:
        """

        :return:
        """
    @Type.setter
    def Type(self, value: CodeTypeReference) -> None: ...
    @property
    def UserData(self) -> IDictionary:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CodeTypeReferenceOptions(Enum):
    """"""

    GlobalReference: CodeTypeReferenceOptions = ...
    """"""
    GenericTypeParameter: CodeTypeReferenceOptions = ...
    """"""

class CodeVariableDeclarationStatement(CodeStatement):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, type: CodeTypeReference, name: str):
        """

        :param type:
        :param name:
        """
    @overload
    def __init__(self, type: str, name: str):
        """

        :param type:
        :param name:
        """
    @overload
    def __init__(self, type: Type, name: str):
        """

        :param type:
        :param name:
        """
    @overload
    def __init__(self, type: CodeTypeReference, name: str, initExpression: CodeExpression):
        """

        :param type:
        :param name:
        :param initExpression:
        """
    @overload
    def __init__(self, type: str, name: str, initExpression: CodeExpression):
        """

        :param type:
        :param name:
        :param initExpression:
        """
    @overload
    def __init__(self, type: Type, name: str, initExpression: CodeExpression):
        """

        :param type:
        :param name:
        :param initExpression:
        """
    @property
    def EndDirectives(self) -> CodeDirectiveCollection:
        """

        :return:
        """
    @property
    def InitExpression(self) -> CodeExpression:
        """

        :return:
        """
    @InitExpression.setter
    def InitExpression(self, value: CodeExpression) -> None: ...
    @property
    def LinePragma(self) -> CodeLinePragma:
        """

        :return:
        """
    @LinePragma.setter
    def LinePragma(self, value: CodeLinePragma) -> None: ...
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def StartDirectives(self) -> CodeDirectiveCollection:
        """

        :return:
        """
    @property
    def Type(self) -> CodeTypeReference:
        """

        :return:
        """
    @Type.setter
    def Type(self, value: CodeTypeReference) -> None: ...
    @property
    def UserData(self) -> IDictionary:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CodeVariableReferenceExpression(CodeExpression):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, variableName: str):
        """

        :param variableName:
        """
    @property
    def UserData(self) -> IDictionary:
        """

        :return:
        """
    @property
    def VariableName(self) -> str:
        """

        :return:
        """
    @VariableName.setter
    def VariableName(self, value: str) -> None: ...
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class FieldDirection(Enum):
    """"""

    In: FieldDirection = ...
    """"""
    Out: FieldDirection = ...
    """"""
    Ref: FieldDirection = ...
    """"""

class MemberAttributes(Enum):
    """"""

    Abstract: MemberAttributes = ...
    """"""
    Final: MemberAttributes = ...
    """"""
    Static: MemberAttributes = ...
    """"""
    Override: MemberAttributes = ...
    """"""
    Const: MemberAttributes = ...
    """"""
    ScopeMask: MemberAttributes = ...
    """"""
    New: MemberAttributes = ...
    """"""
    VTableMask: MemberAttributes = ...
    """"""
    Overloaded: MemberAttributes = ...
    """"""
    Assembly: MemberAttributes = ...
    """"""
    FamilyAndAssembly: MemberAttributes = ...
    """"""
    Family: MemberAttributes = ...
    """"""
    FamilyOrAssembly: MemberAttributes = ...
    """"""
    Private: MemberAttributes = ...
    """"""
    Public: MemberAttributes = ...
    """"""
    AccessMask: MemberAttributes = ...
    """"""
