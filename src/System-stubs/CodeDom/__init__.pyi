"""Automatically generated stubs for C# namespace: System.CodeDom."""

from collections.abc import Iterator
from typing import Self
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

class EventType[T]:
    def __iadd__(self, other: T) -> Self: ...
    def __isub__(self, other: T) -> Self: ...

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CodeArgumentReferenceExpression(CodeExpression):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, parameterName: str) -> None:
        """"""
    @property
    def ParameterName(self) -> str:
        """"""
    @ParameterName.setter
    def ParameterName(self, value: str) -> None: ...
    @property
    def UserData(self) -> IDictionary:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CodeArrayCreateExpression(CodeExpression):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, createType: CodeTypeReference, initializers: Array[CodeExpression]) -> None:
        """"""
    @overload
    def __init__(self, createType: str, initializers: Array[CodeExpression]) -> None:
        """"""
    @overload
    def __init__(self, createType: Type, initializers: Array[CodeExpression]) -> None:
        """"""
    @overload
    def __init__(self, createType: CodeTypeReference, size: int) -> None:
        """"""
    @overload
    def __init__(self, createType: str, size: int) -> None:
        """"""
    @overload
    def __init__(self, createType: Type, size: int) -> None:
        """"""
    @overload
    def __init__(self, createType: CodeTypeReference, size: CodeExpression) -> None:
        """"""
    @overload
    def __init__(self, createType: str, size: CodeExpression) -> None:
        """"""
    @overload
    def __init__(self, createType: Type, size: CodeExpression) -> None:
        """"""
    @property
    def CreateType(self) -> CodeTypeReference:
        """"""
    @CreateType.setter
    def CreateType(self, value: CodeTypeReference) -> None: ...
    @property
    def Initializers(self) -> CodeExpressionCollection:
        """"""
    @property
    def Size(self) -> int:
        """"""
    @Size.setter
    def Size(self, value: int) -> None: ...
    @property
    def SizeExpression(self) -> CodeExpression:
        """"""
    @SizeExpression.setter
    def SizeExpression(self, value: CodeExpression) -> None: ...
    @property
    def UserData(self) -> IDictionary:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CodeArrayIndexerExpression(CodeExpression):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, targetObject: CodeExpression, indices: Array[CodeExpression]) -> None:
        """"""
    @property
    def Indices(self) -> CodeExpressionCollection:
        """"""
    @property
    def TargetObject(self) -> CodeExpression:
        """"""
    @TargetObject.setter
    def TargetObject(self, value: CodeExpression) -> None: ...
    @property
    def UserData(self) -> IDictionary:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CodeAssignStatement(CodeStatement):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, left: CodeExpression, right: CodeExpression) -> None:
        """"""
    @property
    def EndDirectives(self) -> CodeDirectiveCollection:
        """"""
    @property
    def Left(self) -> CodeExpression:
        """"""
    @Left.setter
    def Left(self, value: CodeExpression) -> None: ...
    @property
    def LinePragma(self) -> CodeLinePragma:
        """"""
    @LinePragma.setter
    def LinePragma(self, value: CodeLinePragma) -> None: ...
    @property
    def Right(self) -> CodeExpression:
        """"""
    @Right.setter
    def Right(self, value: CodeExpression) -> None: ...
    @property
    def StartDirectives(self) -> CodeDirectiveCollection:
        """"""
    @property
    def UserData(self) -> IDictionary:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CodeAttachEventStatement(CodeStatement):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, eventRef: CodeEventReferenceExpression, listener: CodeExpression) -> None:
        """"""
    @overload
    def __init__(
        self, targetObject: CodeExpression, eventName: str, listener: CodeExpression
    ) -> None:
        """"""
    @property
    def EndDirectives(self) -> CodeDirectiveCollection:
        """"""
    @property
    def Event(self) -> CodeEventReferenceExpression:
        """"""
    @Event.setter
    def Event(self, value: CodeEventReferenceExpression) -> None: ...
    @property
    def LinePragma(self) -> CodeLinePragma:
        """"""
    @LinePragma.setter
    def LinePragma(self, value: CodeLinePragma) -> None: ...
    @property
    def Listener(self) -> CodeExpression:
        """"""
    @Listener.setter
    def Listener(self, value: CodeExpression) -> None: ...
    @property
    def StartDirectives(self) -> CodeDirectiveCollection:
        """"""
    @property
    def UserData(self) -> IDictionary:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CodeAttributeArgument(Object):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, value: CodeExpression) -> None:
        """"""
    @overload
    def __init__(self, name: str, value: CodeExpression) -> None:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def Value(self) -> CodeExpression:
        """"""
    @Value.setter
    def Value(self, value: CodeExpression) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CodeAttributeArgumentCollection(CollectionBase, ICollection, IEnumerable, IList):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, value: CodeAttributeArgumentCollection) -> None:
        """"""
    @overload
    def __init__(self, value: Array[CodeAttributeArgument]) -> None:
        """"""
    @property
    def Capacity(self) -> int:
        """"""
    @Capacity.setter
    def Capacity(self, value: int) -> None: ...
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsFixedSize(self) -> bool:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def Item(self) -> CodeAttributeArgument:
        """"""
    @Item.setter
    def Item(self, value: CodeAttributeArgument) -> None: ...
    @property
    def SyncRoot(self) -> object:
        """"""
    @overload
    def Add(self, value: CodeAttributeArgument) -> int:
        """"""
    @overload
    def Add(self, value: object) -> int:
        """"""
    @overload
    def AddRange(self, value: CodeAttributeArgumentCollection) -> None:
        """"""
    @overload
    def AddRange(self, value: Array[CodeAttributeArgument]) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    @overload
    def Contains(self, value: CodeAttributeArgument) -> bool:
        """"""
    @overload
    def Contains(self, value: object) -> bool:
        """"""
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array[CodeAttributeArgument], index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IndexOf(self, value: CodeAttributeArgument) -> int:
        """"""
    @overload
    def IndexOf(self, value: object) -> int:
        """"""
    @overload
    def Insert(self, index: int, value: CodeAttributeArgument) -> None:
        """"""
    @overload
    def Insert(self, index: int, value: object) -> None:
        """"""
    @overload
    def Remove(self, value: CodeAttributeArgument) -> None:
        """"""
    @overload
    def Remove(self, value: object) -> None:
        """"""
    def RemoveAt(self, index: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __contains__(self, value: CodeAttributeArgument) -> bool:
        """"""
    @overload
    def __contains__(self, value: object) -> bool:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    @overload
    def __delitem__(self, value: CodeAttributeArgument) -> None:
        """"""
    @overload
    def __delitem__(self, value: object) -> None:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, index: int) -> CodeAttributeArgument:
        """"""
    @overload
    def __setitem__(self, index: int, value: CodeAttributeArgument) -> None:
        """"""
    @overload
    def __setitem__(self, index: int, value: object) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CodeAttributeDeclaration(Object):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, name: str) -> None:
        """"""
    @overload
    def __init__(self, name: str, arguments: Array[CodeAttributeArgument]) -> None:
        """"""
    @overload
    def __init__(self, attributeType: CodeTypeReference) -> None:
        """"""
    @overload
    def __init__(
        self, attributeType: CodeTypeReference, arguments: Array[CodeAttributeArgument]
    ) -> None:
        """"""
    @property
    def Arguments(self) -> CodeAttributeArgumentCollection:
        """"""
    @property
    def AttributeType(self) -> CodeTypeReference:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @Name.setter
    def Name(self, value: str) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CodeAttributeDeclarationCollection(CollectionBase, ICollection, IEnumerable, IList):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, value: CodeAttributeDeclarationCollection) -> None:
        """"""
    @overload
    def __init__(self, value: Array[CodeAttributeDeclaration]) -> None:
        """"""
    @property
    def Capacity(self) -> int:
        """"""
    @Capacity.setter
    def Capacity(self, value: int) -> None: ...
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsFixedSize(self) -> bool:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def Item(self) -> CodeAttributeDeclaration:
        """"""
    @Item.setter
    def Item(self, value: CodeAttributeDeclaration) -> None: ...
    @property
    def SyncRoot(self) -> object:
        """"""
    @overload
    def Add(self, value: CodeAttributeDeclaration) -> int:
        """"""
    @overload
    def Add(self, value: object) -> int:
        """"""
    @overload
    def AddRange(self, value: CodeAttributeDeclarationCollection) -> None:
        """"""
    @overload
    def AddRange(self, value: Array[CodeAttributeDeclaration]) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    @overload
    def Contains(self, value: CodeAttributeDeclaration) -> bool:
        """"""
    @overload
    def Contains(self, value: object) -> bool:
        """"""
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array[CodeAttributeDeclaration], index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IndexOf(self, value: CodeAttributeDeclaration) -> int:
        """"""
    @overload
    def IndexOf(self, value: object) -> int:
        """"""
    @overload
    def Insert(self, index: int, value: CodeAttributeDeclaration) -> None:
        """"""
    @overload
    def Insert(self, index: int, value: object) -> None:
        """"""
    @overload
    def Remove(self, value: CodeAttributeDeclaration) -> None:
        """"""
    @overload
    def Remove(self, value: object) -> None:
        """"""
    def RemoveAt(self, index: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __contains__(self, value: CodeAttributeDeclaration) -> bool:
        """"""
    @overload
    def __contains__(self, value: object) -> bool:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    @overload
    def __delitem__(self, value: CodeAttributeDeclaration) -> None:
        """"""
    @overload
    def __delitem__(self, value: object) -> None:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, index: int) -> CodeAttributeDeclaration:
        """"""
    @overload
    def __setitem__(self, index: int, value: CodeAttributeDeclaration) -> None:
        """"""
    @overload
    def __setitem__(self, index: int, value: object) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CodeBaseReferenceExpression(CodeExpression):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def UserData(self) -> IDictionary:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CodeBinaryOperatorExpression(CodeExpression):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(
        self, left: CodeExpression, op: CodeBinaryOperatorType, right: CodeExpression
    ) -> None:
        """"""
    @property
    def Left(self) -> CodeExpression:
        """"""
    @Left.setter
    def Left(self, value: CodeExpression) -> None: ...
    @property
    def Operator(self) -> CodeBinaryOperatorType:
        """"""
    @Operator.setter
    def Operator(self, value: CodeBinaryOperatorType) -> None: ...
    @property
    def Right(self) -> CodeExpression:
        """"""
    @Right.setter
    def Right(self, value: CodeExpression) -> None: ...
    @property
    def UserData(self) -> IDictionary:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CodeCastExpression(CodeExpression):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, targetType: CodeTypeReference, expression: CodeExpression) -> None:
        """"""
    @overload
    def __init__(self, targetType: str, expression: CodeExpression) -> None:
        """"""
    @overload
    def __init__(self, targetType: Type, expression: CodeExpression) -> None:
        """"""
    @property
    def Expression(self) -> CodeExpression:
        """"""
    @Expression.setter
    def Expression(self, value: CodeExpression) -> None: ...
    @property
    def TargetType(self) -> CodeTypeReference:
        """"""
    @TargetType.setter
    def TargetType(self, value: CodeTypeReference) -> None: ...
    @property
    def UserData(self) -> IDictionary:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CodeCatchClause(Object):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, localName: str) -> None:
        """"""
    @overload
    def __init__(self, localName: str, catchExceptionType: CodeTypeReference) -> None:
        """"""
    @overload
    def __init__(
        self,
        localName: str,
        catchExceptionType: CodeTypeReference,
        statements: Array[CodeStatement],
    ) -> None:
        """"""
    @property
    def CatchExceptionType(self) -> CodeTypeReference:
        """"""
    @CatchExceptionType.setter
    def CatchExceptionType(self, value: CodeTypeReference) -> None: ...
    @property
    def LocalName(self) -> str:
        """"""
    @LocalName.setter
    def LocalName(self, value: str) -> None: ...
    @property
    def Statements(self) -> CodeStatementCollection:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CodeCatchClauseCollection(CollectionBase, ICollection, IEnumerable, IList):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, value: CodeCatchClauseCollection) -> None:
        """"""
    @overload
    def __init__(self, value: Array[CodeCatchClause]) -> None:
        """"""
    @property
    def Capacity(self) -> int:
        """"""
    @Capacity.setter
    def Capacity(self, value: int) -> None: ...
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsFixedSize(self) -> bool:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def Item(self) -> CodeCatchClause:
        """"""
    @Item.setter
    def Item(self, value: CodeCatchClause) -> None: ...
    @property
    def SyncRoot(self) -> object:
        """"""
    @overload
    def Add(self, value: CodeCatchClause) -> int:
        """"""
    @overload
    def Add(self, value: object) -> int:
        """"""
    @overload
    def AddRange(self, value: CodeCatchClauseCollection) -> None:
        """"""
    @overload
    def AddRange(self, value: Array[CodeCatchClause]) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    @overload
    def Contains(self, value: CodeCatchClause) -> bool:
        """"""
    @overload
    def Contains(self, value: object) -> bool:
        """"""
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array[CodeCatchClause], index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IndexOf(self, value: CodeCatchClause) -> int:
        """"""
    @overload
    def IndexOf(self, value: object) -> int:
        """"""
    @overload
    def Insert(self, index: int, value: CodeCatchClause) -> None:
        """"""
    @overload
    def Insert(self, index: int, value: object) -> None:
        """"""
    @overload
    def Remove(self, value: CodeCatchClause) -> None:
        """"""
    @overload
    def Remove(self, value: object) -> None:
        """"""
    def RemoveAt(self, index: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __contains__(self, value: CodeCatchClause) -> bool:
        """"""
    @overload
    def __contains__(self, value: object) -> bool:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    @overload
    def __delitem__(self, value: CodeCatchClause) -> None:
        """"""
    @overload
    def __delitem__(self, value: object) -> None:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, index: int) -> CodeCatchClause:
        """"""
    @overload
    def __setitem__(self, index: int, value: CodeCatchClause) -> None:
        """"""
    @overload
    def __setitem__(self, index: int, value: object) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CodeChecksumPragma(CodeDirective):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, fileName: str, checksumAlgorithmId: Guid, checksumData: Array[int]) -> None:
        """"""
    @property
    def ChecksumAlgorithmId(self) -> Guid:
        """"""
    @ChecksumAlgorithmId.setter
    def ChecksumAlgorithmId(self, value: Guid) -> None: ...
    @property
    def ChecksumData(self) -> Array[int]:
        """"""
    @ChecksumData.setter
    def ChecksumData(self, value: Array[int]) -> None: ...
    @property
    def FileName(self) -> str:
        """"""
    @FileName.setter
    def FileName(self, value: str) -> None: ...
    @property
    def UserData(self) -> IDictionary:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CodeComment(CodeObject):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, text: str) -> None:
        """"""
    @overload
    def __init__(self, text: str, docComment: bool) -> None:
        """"""
    @property
    def DocComment(self) -> bool:
        """"""
    @DocComment.setter
    def DocComment(self, value: bool) -> None: ...
    @property
    def Text(self) -> str:
        """"""
    @Text.setter
    def Text(self, value: str) -> None: ...
    @property
    def UserData(self) -> IDictionary:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CodeCommentStatement(CodeStatement):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, comment: CodeComment) -> None:
        """"""
    @overload
    def __init__(self, text: str) -> None:
        """"""
    @overload
    def __init__(self, text: str, docComment: bool) -> None:
        """"""
    @property
    def Comment(self) -> CodeComment:
        """"""
    @Comment.setter
    def Comment(self, value: CodeComment) -> None: ...
    @property
    def EndDirectives(self) -> CodeDirectiveCollection:
        """"""
    @property
    def LinePragma(self) -> CodeLinePragma:
        """"""
    @LinePragma.setter
    def LinePragma(self, value: CodeLinePragma) -> None: ...
    @property
    def StartDirectives(self) -> CodeDirectiveCollection:
        """"""
    @property
    def UserData(self) -> IDictionary:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CodeCommentStatementCollection(CollectionBase, ICollection, IEnumerable, IList):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, value: CodeCommentStatementCollection) -> None:
        """"""
    @overload
    def __init__(self, value: Array[CodeCommentStatement]) -> None:
        """"""
    @property
    def Capacity(self) -> int:
        """"""
    @Capacity.setter
    def Capacity(self, value: int) -> None: ...
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsFixedSize(self) -> bool:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def Item(self) -> CodeCommentStatement:
        """"""
    @Item.setter
    def Item(self, value: CodeCommentStatement) -> None: ...
    @property
    def SyncRoot(self) -> object:
        """"""
    @overload
    def Add(self, value: CodeCommentStatement) -> int:
        """"""
    @overload
    def Add(self, value: object) -> int:
        """"""
    @overload
    def AddRange(self, value: CodeCommentStatementCollection) -> None:
        """"""
    @overload
    def AddRange(self, value: Array[CodeCommentStatement]) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    @overload
    def Contains(self, value: CodeCommentStatement) -> bool:
        """"""
    @overload
    def Contains(self, value: object) -> bool:
        """"""
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array[CodeCommentStatement], index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IndexOf(self, value: CodeCommentStatement) -> int:
        """"""
    @overload
    def IndexOf(self, value: object) -> int:
        """"""
    @overload
    def Insert(self, index: int, value: CodeCommentStatement) -> None:
        """"""
    @overload
    def Insert(self, index: int, value: object) -> None:
        """"""
    @overload
    def Remove(self, value: CodeCommentStatement) -> None:
        """"""
    @overload
    def Remove(self, value: object) -> None:
        """"""
    def RemoveAt(self, index: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __contains__(self, value: CodeCommentStatement) -> bool:
        """"""
    @overload
    def __contains__(self, value: object) -> bool:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    @overload
    def __delitem__(self, value: CodeCommentStatement) -> None:
        """"""
    @overload
    def __delitem__(self, value: object) -> None:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, index: int) -> CodeCommentStatement:
        """"""
    @overload
    def __setitem__(self, index: int, value: CodeCommentStatement) -> None:
        """"""
    @overload
    def __setitem__(self, index: int, value: object) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CodeCompileUnit(CodeObject):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def AssemblyCustomAttributes(self) -> CodeAttributeDeclarationCollection:
        """"""
    @property
    def EndDirectives(self) -> CodeDirectiveCollection:
        """"""
    @property
    def Namespaces(self) -> CodeNamespaceCollection:
        """"""
    @property
    def ReferencedAssemblies(self) -> StringCollection:
        """"""
    @property
    def StartDirectives(self) -> CodeDirectiveCollection:
        """"""
    @property
    def UserData(self) -> IDictionary:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CodeConditionStatement(CodeStatement):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, condition: CodeExpression, trueStatements: Array[CodeStatement]) -> None:
        """"""
    @overload
    def __init__(
        self,
        condition: CodeExpression,
        trueStatements: Array[CodeStatement],
        falseStatements: Array[CodeStatement],
    ) -> None:
        """"""
    @property
    def Condition(self) -> CodeExpression:
        """"""
    @Condition.setter
    def Condition(self, value: CodeExpression) -> None: ...
    @property
    def EndDirectives(self) -> CodeDirectiveCollection:
        """"""
    @property
    def FalseStatements(self) -> CodeStatementCollection:
        """"""
    @property
    def LinePragma(self) -> CodeLinePragma:
        """"""
    @LinePragma.setter
    def LinePragma(self, value: CodeLinePragma) -> None: ...
    @property
    def StartDirectives(self) -> CodeDirectiveCollection:
        """"""
    @property
    def TrueStatements(self) -> CodeStatementCollection:
        """"""
    @property
    def UserData(self) -> IDictionary:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CodeConstructor(CodeMemberMethod):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Attributes(self) -> MemberAttributes:
        """"""
    @Attributes.setter
    def Attributes(self, value: MemberAttributes) -> None: ...
    @property
    def BaseConstructorArgs(self) -> CodeExpressionCollection:
        """"""
    @property
    def ChainedConstructorArgs(self) -> CodeExpressionCollection:
        """"""
    @property
    def Comments(self) -> CodeCommentStatementCollection:
        """"""
    @property
    def CustomAttributes(self) -> CodeAttributeDeclarationCollection:
        """"""
    @CustomAttributes.setter
    def CustomAttributes(self, value: CodeAttributeDeclarationCollection) -> None: ...
    @property
    def EndDirectives(self) -> CodeDirectiveCollection:
        """"""
    @property
    def ImplementationTypes(self) -> CodeTypeReferenceCollection:
        """"""
    @property
    def LinePragma(self) -> CodeLinePragma:
        """"""
    @LinePragma.setter
    def LinePragma(self, value: CodeLinePragma) -> None: ...
    @property
    def Name(self) -> str:
        """"""
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def Parameters(self) -> CodeParameterDeclarationExpressionCollection:
        """"""
    @property
    def PrivateImplementationType(self) -> CodeTypeReference:
        """"""
    @PrivateImplementationType.setter
    def PrivateImplementationType(self, value: CodeTypeReference) -> None: ...
    @property
    def ReturnType(self) -> CodeTypeReference:
        """"""
    @ReturnType.setter
    def ReturnType(self, value: CodeTypeReference) -> None: ...
    @property
    def ReturnTypeCustomAttributes(self) -> CodeAttributeDeclarationCollection:
        """"""
    @property
    def StartDirectives(self) -> CodeDirectiveCollection:
        """"""
    @property
    def Statements(self) -> CodeStatementCollection:
        """"""
    @property
    def TypeParameters(self) -> CodeTypeParameterCollection:
        """"""
    @property
    def UserData(self) -> IDictionary:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    PopulateImplementationTypes: EventType[EventHandler] = ...
    """"""
    PopulateParameters: EventType[EventHandler] = ...
    """"""
    PopulateStatements: EventType[EventHandler] = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CodeDefaultValueExpression(CodeExpression):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, type: CodeTypeReference) -> None:
        """"""
    @property
    def Type(self) -> CodeTypeReference:
        """"""
    @Type.setter
    def Type(self, value: CodeTypeReference) -> None: ...
    @property
    def UserData(self) -> IDictionary:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CodeDelegateCreateExpression(CodeExpression):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(
        self, delegateType: CodeTypeReference, targetObject: CodeExpression, methodName: str
    ) -> None:
        """"""
    @property
    def DelegateType(self) -> CodeTypeReference:
        """"""
    @DelegateType.setter
    def DelegateType(self, value: CodeTypeReference) -> None: ...
    @property
    def MethodName(self) -> str:
        """"""
    @MethodName.setter
    def MethodName(self, value: str) -> None: ...
    @property
    def TargetObject(self) -> CodeExpression:
        """"""
    @TargetObject.setter
    def TargetObject(self, value: CodeExpression) -> None: ...
    @property
    def UserData(self) -> IDictionary:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CodeDelegateInvokeExpression(CodeExpression):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, targetObject: CodeExpression) -> None:
        """"""
    @overload
    def __init__(self, targetObject: CodeExpression, parameters: Array[CodeExpression]) -> None:
        """"""
    @property
    def Parameters(self) -> CodeExpressionCollection:
        """"""
    @property
    def TargetObject(self) -> CodeExpression:
        """"""
    @TargetObject.setter
    def TargetObject(self, value: CodeExpression) -> None: ...
    @property
    def UserData(self) -> IDictionary:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CodeDirectionExpression(CodeExpression):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, direction: FieldDirection, expression: CodeExpression) -> None:
        """"""
    @property
    def Direction(self) -> FieldDirection:
        """"""
    @Direction.setter
    def Direction(self, value: FieldDirection) -> None: ...
    @property
    def Expression(self) -> CodeExpression:
        """"""
    @Expression.setter
    def Expression(self, value: CodeExpression) -> None: ...
    @property
    def UserData(self) -> IDictionary:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CodeDirective(CodeObject):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def UserData(self) -> IDictionary:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CodeDirectiveCollection(CollectionBase, ICollection, IEnumerable, IList):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, value: CodeDirectiveCollection) -> None:
        """"""
    @overload
    def __init__(self, value: Array[CodeDirective]) -> None:
        """"""
    @property
    def Capacity(self) -> int:
        """"""
    @Capacity.setter
    def Capacity(self, value: int) -> None: ...
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsFixedSize(self) -> bool:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def Item(self) -> CodeDirective:
        """"""
    @Item.setter
    def Item(self, value: CodeDirective) -> None: ...
    @property
    def SyncRoot(self) -> object:
        """"""
    @overload
    def Add(self, value: CodeDirective) -> int:
        """"""
    @overload
    def Add(self, value: object) -> int:
        """"""
    @overload
    def AddRange(self, value: CodeDirectiveCollection) -> None:
        """"""
    @overload
    def AddRange(self, value: Array[CodeDirective]) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    @overload
    def Contains(self, value: CodeDirective) -> bool:
        """"""
    @overload
    def Contains(self, value: object) -> bool:
        """"""
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array[CodeDirective], index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IndexOf(self, value: CodeDirective) -> int:
        """"""
    @overload
    def IndexOf(self, value: object) -> int:
        """"""
    @overload
    def Insert(self, index: int, value: CodeDirective) -> None:
        """"""
    @overload
    def Insert(self, index: int, value: object) -> None:
        """"""
    @overload
    def Remove(self, value: CodeDirective) -> None:
        """"""
    @overload
    def Remove(self, value: object) -> None:
        """"""
    def RemoveAt(self, index: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __contains__(self, value: CodeDirective) -> bool:
        """"""
    @overload
    def __contains__(self, value: object) -> bool:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    @overload
    def __delitem__(self, value: CodeDirective) -> None:
        """"""
    @overload
    def __delitem__(self, value: object) -> None:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, index: int) -> CodeDirective:
        """"""
    @overload
    def __setitem__(self, index: int, value: CodeDirective) -> None:
        """"""
    @overload
    def __setitem__(self, index: int, value: object) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CodeEntryPointMethod(CodeMemberMethod):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Attributes(self) -> MemberAttributes:
        """"""
    @Attributes.setter
    def Attributes(self, value: MemberAttributes) -> None: ...
    @property
    def Comments(self) -> CodeCommentStatementCollection:
        """"""
    @property
    def CustomAttributes(self) -> CodeAttributeDeclarationCollection:
        """"""
    @CustomAttributes.setter
    def CustomAttributes(self, value: CodeAttributeDeclarationCollection) -> None: ...
    @property
    def EndDirectives(self) -> CodeDirectiveCollection:
        """"""
    @property
    def ImplementationTypes(self) -> CodeTypeReferenceCollection:
        """"""
    @property
    def LinePragma(self) -> CodeLinePragma:
        """"""
    @LinePragma.setter
    def LinePragma(self, value: CodeLinePragma) -> None: ...
    @property
    def Name(self) -> str:
        """"""
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def Parameters(self) -> CodeParameterDeclarationExpressionCollection:
        """"""
    @property
    def PrivateImplementationType(self) -> CodeTypeReference:
        """"""
    @PrivateImplementationType.setter
    def PrivateImplementationType(self, value: CodeTypeReference) -> None: ...
    @property
    def ReturnType(self) -> CodeTypeReference:
        """"""
    @ReturnType.setter
    def ReturnType(self, value: CodeTypeReference) -> None: ...
    @property
    def ReturnTypeCustomAttributes(self) -> CodeAttributeDeclarationCollection:
        """"""
    @property
    def StartDirectives(self) -> CodeDirectiveCollection:
        """"""
    @property
    def Statements(self) -> CodeStatementCollection:
        """"""
    @property
    def TypeParameters(self) -> CodeTypeParameterCollection:
        """"""
    @property
    def UserData(self) -> IDictionary:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    PopulateImplementationTypes: EventType[EventHandler] = ...
    """"""
    PopulateParameters: EventType[EventHandler] = ...
    """"""
    PopulateStatements: EventType[EventHandler] = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CodeEventReferenceExpression(CodeExpression):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, targetObject: CodeExpression, eventName: str) -> None:
        """"""
    @property
    def EventName(self) -> str:
        """"""
    @EventName.setter
    def EventName(self, value: str) -> None: ...
    @property
    def TargetObject(self) -> CodeExpression:
        """"""
    @TargetObject.setter
    def TargetObject(self, value: CodeExpression) -> None: ...
    @property
    def UserData(self) -> IDictionary:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CodeExpression(CodeObject):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def UserData(self) -> IDictionary:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CodeExpressionCollection(CollectionBase, ICollection, IEnumerable, IList):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, value: CodeExpressionCollection) -> None:
        """"""
    @overload
    def __init__(self, value: Array[CodeExpression]) -> None:
        """"""
    @property
    def Capacity(self) -> int:
        """"""
    @Capacity.setter
    def Capacity(self, value: int) -> None: ...
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsFixedSize(self) -> bool:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def Item(self) -> CodeExpression:
        """"""
    @Item.setter
    def Item(self, value: CodeExpression) -> None: ...
    @property
    def SyncRoot(self) -> object:
        """"""
    @overload
    def Add(self, value: CodeExpression) -> int:
        """"""
    @overload
    def Add(self, value: object) -> int:
        """"""
    @overload
    def AddRange(self, value: CodeExpressionCollection) -> None:
        """"""
    @overload
    def AddRange(self, value: Array[CodeExpression]) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    @overload
    def Contains(self, value: CodeExpression) -> bool:
        """"""
    @overload
    def Contains(self, value: object) -> bool:
        """"""
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array[CodeExpression], index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IndexOf(self, value: CodeExpression) -> int:
        """"""
    @overload
    def IndexOf(self, value: object) -> int:
        """"""
    @overload
    def Insert(self, index: int, value: CodeExpression) -> None:
        """"""
    @overload
    def Insert(self, index: int, value: object) -> None:
        """"""
    @overload
    def Remove(self, value: CodeExpression) -> None:
        """"""
    @overload
    def Remove(self, value: object) -> None:
        """"""
    def RemoveAt(self, index: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __contains__(self, value: CodeExpression) -> bool:
        """"""
    @overload
    def __contains__(self, value: object) -> bool:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    @overload
    def __delitem__(self, value: CodeExpression) -> None:
        """"""
    @overload
    def __delitem__(self, value: object) -> None:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, index: int) -> CodeExpression:
        """"""
    @overload
    def __setitem__(self, index: int, value: CodeExpression) -> None:
        """"""
    @overload
    def __setitem__(self, index: int, value: object) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CodeExpressionStatement(CodeStatement):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, expression: CodeExpression) -> None:
        """"""
    @property
    def EndDirectives(self) -> CodeDirectiveCollection:
        """"""
    @property
    def Expression(self) -> CodeExpression:
        """"""
    @Expression.setter
    def Expression(self, value: CodeExpression) -> None: ...
    @property
    def LinePragma(self) -> CodeLinePragma:
        """"""
    @LinePragma.setter
    def LinePragma(self, value: CodeLinePragma) -> None: ...
    @property
    def StartDirectives(self) -> CodeDirectiveCollection:
        """"""
    @property
    def UserData(self) -> IDictionary:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CodeFieldReferenceExpression(CodeExpression):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, targetObject: CodeExpression, fieldName: str) -> None:
        """"""
    @property
    def FieldName(self) -> str:
        """"""
    @FieldName.setter
    def FieldName(self, value: str) -> None: ...
    @property
    def TargetObject(self) -> CodeExpression:
        """"""
    @TargetObject.setter
    def TargetObject(self, value: CodeExpression) -> None: ...
    @property
    def UserData(self) -> IDictionary:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CodeGotoStatement(CodeStatement):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, label: str) -> None:
        """"""
    @property
    def EndDirectives(self) -> CodeDirectiveCollection:
        """"""
    @property
    def Label(self) -> str:
        """"""
    @Label.setter
    def Label(self, value: str) -> None: ...
    @property
    def LinePragma(self) -> CodeLinePragma:
        """"""
    @LinePragma.setter
    def LinePragma(self, value: CodeLinePragma) -> None: ...
    @property
    def StartDirectives(self) -> CodeDirectiveCollection:
        """"""
    @property
    def UserData(self) -> IDictionary:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CodeIndexerExpression(CodeExpression):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, targetObject: CodeExpression, indices: Array[CodeExpression]) -> None:
        """"""
    @property
    def Indices(self) -> CodeExpressionCollection:
        """"""
    @property
    def TargetObject(self) -> CodeExpression:
        """"""
    @TargetObject.setter
    def TargetObject(self, value: CodeExpression) -> None: ...
    @property
    def UserData(self) -> IDictionary:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CodeIterationStatement(CodeStatement):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(
        self,
        initStatement: CodeStatement,
        testExpression: CodeExpression,
        incrementStatement: CodeStatement,
        statements: Array[CodeStatement],
    ) -> None:
        """"""
    @property
    def EndDirectives(self) -> CodeDirectiveCollection:
        """"""
    @property
    def IncrementStatement(self) -> CodeStatement:
        """"""
    @IncrementStatement.setter
    def IncrementStatement(self, value: CodeStatement) -> None: ...
    @property
    def InitStatement(self) -> CodeStatement:
        """"""
    @InitStatement.setter
    def InitStatement(self, value: CodeStatement) -> None: ...
    @property
    def LinePragma(self) -> CodeLinePragma:
        """"""
    @LinePragma.setter
    def LinePragma(self, value: CodeLinePragma) -> None: ...
    @property
    def StartDirectives(self) -> CodeDirectiveCollection:
        """"""
    @property
    def Statements(self) -> CodeStatementCollection:
        """"""
    @property
    def TestExpression(self) -> CodeExpression:
        """"""
    @TestExpression.setter
    def TestExpression(self, value: CodeExpression) -> None: ...
    @property
    def UserData(self) -> IDictionary:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CodeLabeledStatement(CodeStatement):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, label: str) -> None:
        """"""
    @overload
    def __init__(self, label: str, statement: CodeStatement) -> None:
        """"""
    @property
    def EndDirectives(self) -> CodeDirectiveCollection:
        """"""
    @property
    def Label(self) -> str:
        """"""
    @Label.setter
    def Label(self, value: str) -> None: ...
    @property
    def LinePragma(self) -> CodeLinePragma:
        """"""
    @LinePragma.setter
    def LinePragma(self, value: CodeLinePragma) -> None: ...
    @property
    def StartDirectives(self) -> CodeDirectiveCollection:
        """"""
    @property
    def Statement(self) -> CodeStatement:
        """"""
    @Statement.setter
    def Statement(self, value: CodeStatement) -> None: ...
    @property
    def UserData(self) -> IDictionary:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CodeLinePragma(Object):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, fileName: str, lineNumber: int) -> None:
        """"""
    @property
    def FileName(self) -> str:
        """"""
    @FileName.setter
    def FileName(self, value: str) -> None: ...
    @property
    def LineNumber(self) -> int:
        """"""
    @LineNumber.setter
    def LineNumber(self, value: int) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CodeMemberEvent(CodeTypeMember):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Attributes(self) -> MemberAttributes:
        """"""
    @Attributes.setter
    def Attributes(self, value: MemberAttributes) -> None: ...
    @property
    def Comments(self) -> CodeCommentStatementCollection:
        """"""
    @property
    def CustomAttributes(self) -> CodeAttributeDeclarationCollection:
        """"""
    @CustomAttributes.setter
    def CustomAttributes(self, value: CodeAttributeDeclarationCollection) -> None: ...
    @property
    def EndDirectives(self) -> CodeDirectiveCollection:
        """"""
    @property
    def ImplementationTypes(self) -> CodeTypeReferenceCollection:
        """"""
    @property
    def LinePragma(self) -> CodeLinePragma:
        """"""
    @LinePragma.setter
    def LinePragma(self, value: CodeLinePragma) -> None: ...
    @property
    def Name(self) -> str:
        """"""
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def PrivateImplementationType(self) -> CodeTypeReference:
        """"""
    @PrivateImplementationType.setter
    def PrivateImplementationType(self, value: CodeTypeReference) -> None: ...
    @property
    def StartDirectives(self) -> CodeDirectiveCollection:
        """"""
    @property
    def Type(self) -> CodeTypeReference:
        """"""
    @Type.setter
    def Type(self, value: CodeTypeReference) -> None: ...
    @property
    def UserData(self) -> IDictionary:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CodeMemberField(CodeTypeMember):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, type: CodeTypeReference, name: str) -> None:
        """"""
    @overload
    def __init__(self, type: str, name: str) -> None:
        """"""
    @overload
    def __init__(self, type: Type, name: str) -> None:
        """"""
    @property
    def Attributes(self) -> MemberAttributes:
        """"""
    @Attributes.setter
    def Attributes(self, value: MemberAttributes) -> None: ...
    @property
    def Comments(self) -> CodeCommentStatementCollection:
        """"""
    @property
    def CustomAttributes(self) -> CodeAttributeDeclarationCollection:
        """"""
    @CustomAttributes.setter
    def CustomAttributes(self, value: CodeAttributeDeclarationCollection) -> None: ...
    @property
    def EndDirectives(self) -> CodeDirectiveCollection:
        """"""
    @property
    def InitExpression(self) -> CodeExpression:
        """"""
    @InitExpression.setter
    def InitExpression(self, value: CodeExpression) -> None: ...
    @property
    def LinePragma(self) -> CodeLinePragma:
        """"""
    @LinePragma.setter
    def LinePragma(self, value: CodeLinePragma) -> None: ...
    @property
    def Name(self) -> str:
        """"""
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def StartDirectives(self) -> CodeDirectiveCollection:
        """"""
    @property
    def Type(self) -> CodeTypeReference:
        """"""
    @Type.setter
    def Type(self, value: CodeTypeReference) -> None: ...
    @property
    def UserData(self) -> IDictionary:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CodeMemberMethod(CodeTypeMember):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Attributes(self) -> MemberAttributes:
        """"""
    @Attributes.setter
    def Attributes(self, value: MemberAttributes) -> None: ...
    @property
    def Comments(self) -> CodeCommentStatementCollection:
        """"""
    @property
    def CustomAttributes(self) -> CodeAttributeDeclarationCollection:
        """"""
    @CustomAttributes.setter
    def CustomAttributes(self, value: CodeAttributeDeclarationCollection) -> None: ...
    @property
    def EndDirectives(self) -> CodeDirectiveCollection:
        """"""
    @property
    def ImplementationTypes(self) -> CodeTypeReferenceCollection:
        """"""
    @property
    def LinePragma(self) -> CodeLinePragma:
        """"""
    @LinePragma.setter
    def LinePragma(self, value: CodeLinePragma) -> None: ...
    @property
    def Name(self) -> str:
        """"""
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def Parameters(self) -> CodeParameterDeclarationExpressionCollection:
        """"""
    @property
    def PrivateImplementationType(self) -> CodeTypeReference:
        """"""
    @PrivateImplementationType.setter
    def PrivateImplementationType(self, value: CodeTypeReference) -> None: ...
    @property
    def ReturnType(self) -> CodeTypeReference:
        """"""
    @ReturnType.setter
    def ReturnType(self, value: CodeTypeReference) -> None: ...
    @property
    def ReturnTypeCustomAttributes(self) -> CodeAttributeDeclarationCollection:
        """"""
    @property
    def StartDirectives(self) -> CodeDirectiveCollection:
        """"""
    @property
    def Statements(self) -> CodeStatementCollection:
        """"""
    @property
    def TypeParameters(self) -> CodeTypeParameterCollection:
        """"""
    @property
    def UserData(self) -> IDictionary:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    PopulateImplementationTypes: EventType[EventHandler] = ...
    """"""
    PopulateParameters: EventType[EventHandler] = ...
    """"""
    PopulateStatements: EventType[EventHandler] = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CodeMemberProperty(CodeTypeMember):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Attributes(self) -> MemberAttributes:
        """"""
    @Attributes.setter
    def Attributes(self, value: MemberAttributes) -> None: ...
    @property
    def Comments(self) -> CodeCommentStatementCollection:
        """"""
    @property
    def CustomAttributes(self) -> CodeAttributeDeclarationCollection:
        """"""
    @CustomAttributes.setter
    def CustomAttributes(self, value: CodeAttributeDeclarationCollection) -> None: ...
    @property
    def EndDirectives(self) -> CodeDirectiveCollection:
        """"""
    @property
    def GetStatements(self) -> CodeStatementCollection:
        """"""
    @property
    def HasGet(self) -> bool:
        """"""
    @HasGet.setter
    def HasGet(self, value: bool) -> None: ...
    @property
    def HasSet(self) -> bool:
        """"""
    @HasSet.setter
    def HasSet(self, value: bool) -> None: ...
    @property
    def ImplementationTypes(self) -> CodeTypeReferenceCollection:
        """"""
    @property
    def LinePragma(self) -> CodeLinePragma:
        """"""
    @LinePragma.setter
    def LinePragma(self, value: CodeLinePragma) -> None: ...
    @property
    def Name(self) -> str:
        """"""
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def Parameters(self) -> CodeParameterDeclarationExpressionCollection:
        """"""
    @property
    def PrivateImplementationType(self) -> CodeTypeReference:
        """"""
    @PrivateImplementationType.setter
    def PrivateImplementationType(self, value: CodeTypeReference) -> None: ...
    @property
    def SetStatements(self) -> CodeStatementCollection:
        """"""
    @property
    def StartDirectives(self) -> CodeDirectiveCollection:
        """"""
    @property
    def Type(self) -> CodeTypeReference:
        """"""
    @Type.setter
    def Type(self, value: CodeTypeReference) -> None: ...
    @property
    def UserData(self) -> IDictionary:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CodeMethodInvokeExpression(CodeExpression):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(
        self, method: CodeMethodReferenceExpression, parameters: Array[CodeExpression]
    ) -> None:
        """"""
    @overload
    def __init__(
        self, targetObject: CodeExpression, methodName: str, parameters: Array[CodeExpression]
    ) -> None:
        """"""
    @property
    def Method(self) -> CodeMethodReferenceExpression:
        """"""
    @Method.setter
    def Method(self, value: CodeMethodReferenceExpression) -> None: ...
    @property
    def Parameters(self) -> CodeExpressionCollection:
        """"""
    @property
    def UserData(self) -> IDictionary:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CodeMethodReferenceExpression(CodeExpression):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, targetObject: CodeExpression, methodName: str) -> None:
        """"""
    @overload
    def __init__(
        self,
        targetObject: CodeExpression,
        methodName: str,
        typeParameters: Array[CodeTypeReference],
    ) -> None:
        """"""
    @property
    def MethodName(self) -> str:
        """"""
    @MethodName.setter
    def MethodName(self, value: str) -> None: ...
    @property
    def TargetObject(self) -> CodeExpression:
        """"""
    @TargetObject.setter
    def TargetObject(self, value: CodeExpression) -> None: ...
    @property
    def TypeArguments(self) -> CodeTypeReferenceCollection:
        """"""
    @property
    def UserData(self) -> IDictionary:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CodeMethodReturnStatement(CodeStatement):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, expression: CodeExpression) -> None:
        """"""
    @property
    def EndDirectives(self) -> CodeDirectiveCollection:
        """"""
    @property
    def Expression(self) -> CodeExpression:
        """"""
    @Expression.setter
    def Expression(self, value: CodeExpression) -> None: ...
    @property
    def LinePragma(self) -> CodeLinePragma:
        """"""
    @LinePragma.setter
    def LinePragma(self, value: CodeLinePragma) -> None: ...
    @property
    def StartDirectives(self) -> CodeDirectiveCollection:
        """"""
    @property
    def UserData(self) -> IDictionary:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CodeNamespace(CodeObject):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, name: str) -> None:
        """"""
    @property
    def Comments(self) -> CodeCommentStatementCollection:
        """"""
    @property
    def Imports(self) -> CodeNamespaceImportCollection:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def Types(self) -> CodeTypeDeclarationCollection:
        """"""
    @property
    def UserData(self) -> IDictionary:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    PopulateComments: EventType[EventHandler] = ...
    """"""
    PopulateImports: EventType[EventHandler] = ...
    """"""
    PopulateTypes: EventType[EventHandler] = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CodeNamespaceCollection(CollectionBase, ICollection, IEnumerable, IList):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, value: CodeNamespaceCollection) -> None:
        """"""
    @overload
    def __init__(self, value: Array[CodeNamespace]) -> None:
        """"""
    @property
    def Capacity(self) -> int:
        """"""
    @Capacity.setter
    def Capacity(self, value: int) -> None: ...
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsFixedSize(self) -> bool:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def Item(self) -> CodeNamespace:
        """"""
    @Item.setter
    def Item(self, value: CodeNamespace) -> None: ...
    @property
    def SyncRoot(self) -> object:
        """"""
    @overload
    def Add(self, value: CodeNamespace) -> int:
        """"""
    @overload
    def Add(self, value: object) -> int:
        """"""
    @overload
    def AddRange(self, value: CodeNamespaceCollection) -> None:
        """"""
    @overload
    def AddRange(self, value: Array[CodeNamespace]) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    @overload
    def Contains(self, value: CodeNamespace) -> bool:
        """"""
    @overload
    def Contains(self, value: object) -> bool:
        """"""
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array[CodeNamespace], index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IndexOf(self, value: CodeNamespace) -> int:
        """"""
    @overload
    def IndexOf(self, value: object) -> int:
        """"""
    @overload
    def Insert(self, index: int, value: CodeNamespace) -> None:
        """"""
    @overload
    def Insert(self, index: int, value: object) -> None:
        """"""
    @overload
    def Remove(self, value: CodeNamespace) -> None:
        """"""
    @overload
    def Remove(self, value: object) -> None:
        """"""
    def RemoveAt(self, index: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __contains__(self, value: CodeNamespace) -> bool:
        """"""
    @overload
    def __contains__(self, value: object) -> bool:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    @overload
    def __delitem__(self, value: CodeNamespace) -> None:
        """"""
    @overload
    def __delitem__(self, value: object) -> None:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, index: int) -> CodeNamespace:
        """"""
    @overload
    def __setitem__(self, index: int, value: CodeNamespace) -> None:
        """"""
    @overload
    def __setitem__(self, index: int, value: object) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CodeNamespaceImport(CodeObject):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, nameSpace: str) -> None:
        """"""
    @property
    def LinePragma(self) -> CodeLinePragma:
        """"""
    @LinePragma.setter
    def LinePragma(self, value: CodeLinePragma) -> None: ...
    @property
    def Namespace(self) -> str:
        """"""
    @Namespace.setter
    def Namespace(self, value: str) -> None: ...
    @property
    def UserData(self) -> IDictionary:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CodeNamespaceImportCollection(Object, ICollection, IEnumerable, IList):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsFixedSize(self) -> bool:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def Item(self) -> CodeNamespaceImport:
        """"""
    @Item.setter
    def Item(self, value: CodeNamespaceImport) -> None: ...
    @property
    def SyncRoot(self) -> object:
        """"""
    @overload
    def Add(self, value: CodeNamespaceImport) -> None:
        """"""
    @overload
    def Add(self, value: object) -> int:
        """"""
    def AddRange(self, value: Array[CodeNamespaceImport]) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    def Contains(self, value: object) -> bool:
        """"""
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def IndexOf(self, value: object) -> int:
        """"""
    def Insert(self, index: int, value: object) -> None:
        """"""
    def Remove(self, value: object) -> None:
        """"""
    def RemoveAt(self, index: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def __contains__(self, value: object) -> bool:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    def __delitem__(self, value: object) -> None:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, index: int) -> CodeNamespaceImport:
        """"""
    @overload
    def __setitem__(self, index: int, value: CodeNamespaceImport) -> None:
        """"""
    @overload
    def __setitem__(self, index: int, value: object) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CodeObject(Object):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def UserData(self) -> IDictionary:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CodeObjectCreateExpression(CodeExpression):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, createType: CodeTypeReference, parameters: Array[CodeExpression]) -> None:
        """"""
    @overload
    def __init__(self, createType: str, parameters: Array[CodeExpression]) -> None:
        """"""
    @overload
    def __init__(self, createType: Type, parameters: Array[CodeExpression]) -> None:
        """"""
    @property
    def CreateType(self) -> CodeTypeReference:
        """"""
    @CreateType.setter
    def CreateType(self, value: CodeTypeReference) -> None: ...
    @property
    def Parameters(self) -> CodeExpressionCollection:
        """"""
    @property
    def UserData(self) -> IDictionary:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CodeParameterDeclarationExpression(CodeExpression):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, type: CodeTypeReference, name: str) -> None:
        """"""
    @overload
    def __init__(self, type: str, name: str) -> None:
        """"""
    @overload
    def __init__(self, type: Type, name: str) -> None:
        """"""
    @property
    def CustomAttributes(self) -> CodeAttributeDeclarationCollection:
        """"""
    @CustomAttributes.setter
    def CustomAttributes(self, value: CodeAttributeDeclarationCollection) -> None: ...
    @property
    def Direction(self) -> FieldDirection:
        """"""
    @Direction.setter
    def Direction(self, value: FieldDirection) -> None: ...
    @property
    def Name(self) -> str:
        """"""
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def Type(self) -> CodeTypeReference:
        """"""
    @Type.setter
    def Type(self, value: CodeTypeReference) -> None: ...
    @property
    def UserData(self) -> IDictionary:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CodeParameterDeclarationExpressionCollection(CollectionBase, ICollection, IEnumerable, IList):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, value: CodeParameterDeclarationExpressionCollection) -> None:
        """"""
    @overload
    def __init__(self, value: Array[CodeParameterDeclarationExpression]) -> None:
        """"""
    @property
    def Capacity(self) -> int:
        """"""
    @Capacity.setter
    def Capacity(self, value: int) -> None: ...
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsFixedSize(self) -> bool:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def Item(self) -> CodeParameterDeclarationExpression:
        """"""
    @Item.setter
    def Item(self, value: CodeParameterDeclarationExpression) -> None: ...
    @property
    def SyncRoot(self) -> object:
        """"""
    @overload
    def Add(self, value: CodeParameterDeclarationExpression) -> int:
        """"""
    @overload
    def Add(self, value: object) -> int:
        """"""
    @overload
    def AddRange(self, value: CodeParameterDeclarationExpressionCollection) -> None:
        """"""
    @overload
    def AddRange(self, value: Array[CodeParameterDeclarationExpression]) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    @overload
    def Contains(self, value: CodeParameterDeclarationExpression) -> bool:
        """"""
    @overload
    def Contains(self, value: object) -> bool:
        """"""
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array[CodeParameterDeclarationExpression], index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IndexOf(self, value: CodeParameterDeclarationExpression) -> int:
        """"""
    @overload
    def IndexOf(self, value: object) -> int:
        """"""
    @overload
    def Insert(self, index: int, value: CodeParameterDeclarationExpression) -> None:
        """"""
    @overload
    def Insert(self, index: int, value: object) -> None:
        """"""
    @overload
    def Remove(self, value: CodeParameterDeclarationExpression) -> None:
        """"""
    @overload
    def Remove(self, value: object) -> None:
        """"""
    def RemoveAt(self, index: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __contains__(self, value: CodeParameterDeclarationExpression) -> bool:
        """"""
    @overload
    def __contains__(self, value: object) -> bool:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    @overload
    def __delitem__(self, value: CodeParameterDeclarationExpression) -> None:
        """"""
    @overload
    def __delitem__(self, value: object) -> None:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, index: int) -> CodeParameterDeclarationExpression:
        """"""
    @overload
    def __setitem__(self, index: int, value: CodeParameterDeclarationExpression) -> None:
        """"""
    @overload
    def __setitem__(self, index: int, value: object) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CodePrimitiveExpression(CodeExpression):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, value: object) -> None:
        """"""
    @property
    def UserData(self) -> IDictionary:
        """"""
    @property
    def Value(self) -> object:
        """"""
    @Value.setter
    def Value(self, value: object) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CodePropertyReferenceExpression(CodeExpression):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, targetObject: CodeExpression, propertyName: str) -> None:
        """"""
    @property
    def PropertyName(self) -> str:
        """"""
    @PropertyName.setter
    def PropertyName(self, value: str) -> None: ...
    @property
    def TargetObject(self) -> CodeExpression:
        """"""
    @TargetObject.setter
    def TargetObject(self, value: CodeExpression) -> None: ...
    @property
    def UserData(self) -> IDictionary:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CodePropertySetValueReferenceExpression(CodeExpression):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def UserData(self) -> IDictionary:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CodeRegionDirective(CodeDirective):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, regionMode: CodeRegionMode, regionText: str) -> None:
        """"""
    @property
    def RegionMode(self) -> CodeRegionMode:
        """"""
    @RegionMode.setter
    def RegionMode(self, value: CodeRegionMode) -> None: ...
    @property
    def RegionText(self) -> str:
        """"""
    @RegionText.setter
    def RegionText(self, value: str) -> None: ...
    @property
    def UserData(self) -> IDictionary:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class CodeRegionMode(Enum):
    """"""

    _None: CodeRegionMode = ...
    """"""
    Start: CodeRegionMode = ...
    """"""
    End: CodeRegionMode = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CodeRemoveEventStatement(CodeStatement):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, eventRef: CodeEventReferenceExpression, listener: CodeExpression) -> None:
        """"""
    @overload
    def __init__(
        self, targetObject: CodeExpression, eventName: str, listener: CodeExpression
    ) -> None:
        """"""
    @property
    def EndDirectives(self) -> CodeDirectiveCollection:
        """"""
    @property
    def Event(self) -> CodeEventReferenceExpression:
        """"""
    @Event.setter
    def Event(self, value: CodeEventReferenceExpression) -> None: ...
    @property
    def LinePragma(self) -> CodeLinePragma:
        """"""
    @LinePragma.setter
    def LinePragma(self, value: CodeLinePragma) -> None: ...
    @property
    def Listener(self) -> CodeExpression:
        """"""
    @Listener.setter
    def Listener(self, value: CodeExpression) -> None: ...
    @property
    def StartDirectives(self) -> CodeDirectiveCollection:
        """"""
    @property
    def UserData(self) -> IDictionary:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CodeSnippetCompileUnit(CodeCompileUnit):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, value: str) -> None:
        """"""
    @property
    def AssemblyCustomAttributes(self) -> CodeAttributeDeclarationCollection:
        """"""
    @property
    def EndDirectives(self) -> CodeDirectiveCollection:
        """"""
    @property
    def LinePragma(self) -> CodeLinePragma:
        """"""
    @LinePragma.setter
    def LinePragma(self, value: CodeLinePragma) -> None: ...
    @property
    def Namespaces(self) -> CodeNamespaceCollection:
        """"""
    @property
    def ReferencedAssemblies(self) -> StringCollection:
        """"""
    @property
    def StartDirectives(self) -> CodeDirectiveCollection:
        """"""
    @property
    def UserData(self) -> IDictionary:
        """"""
    @property
    def Value(self) -> str:
        """"""
    @Value.setter
    def Value(self, value: str) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CodeSnippetExpression(CodeExpression):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, value: str) -> None:
        """"""
    @property
    def UserData(self) -> IDictionary:
        """"""
    @property
    def Value(self) -> str:
        """"""
    @Value.setter
    def Value(self, value: str) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CodeSnippetStatement(CodeStatement):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, value: str) -> None:
        """"""
    @property
    def EndDirectives(self) -> CodeDirectiveCollection:
        """"""
    @property
    def LinePragma(self) -> CodeLinePragma:
        """"""
    @LinePragma.setter
    def LinePragma(self, value: CodeLinePragma) -> None: ...
    @property
    def StartDirectives(self) -> CodeDirectiveCollection:
        """"""
    @property
    def UserData(self) -> IDictionary:
        """"""
    @property
    def Value(self) -> str:
        """"""
    @Value.setter
    def Value(self, value: str) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CodeSnippetTypeMember(CodeTypeMember):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, text: str) -> None:
        """"""
    @property
    def Attributes(self) -> MemberAttributes:
        """"""
    @Attributes.setter
    def Attributes(self, value: MemberAttributes) -> None: ...
    @property
    def Comments(self) -> CodeCommentStatementCollection:
        """"""
    @property
    def CustomAttributes(self) -> CodeAttributeDeclarationCollection:
        """"""
    @CustomAttributes.setter
    def CustomAttributes(self, value: CodeAttributeDeclarationCollection) -> None: ...
    @property
    def EndDirectives(self) -> CodeDirectiveCollection:
        """"""
    @property
    def LinePragma(self) -> CodeLinePragma:
        """"""
    @LinePragma.setter
    def LinePragma(self, value: CodeLinePragma) -> None: ...
    @property
    def Name(self) -> str:
        """"""
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def StartDirectives(self) -> CodeDirectiveCollection:
        """"""
    @property
    def Text(self) -> str:
        """"""
    @Text.setter
    def Text(self, value: str) -> None: ...
    @property
    def UserData(self) -> IDictionary:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CodeStatement(CodeObject):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def EndDirectives(self) -> CodeDirectiveCollection:
        """"""
    @property
    def LinePragma(self) -> CodeLinePragma:
        """"""
    @LinePragma.setter
    def LinePragma(self, value: CodeLinePragma) -> None: ...
    @property
    def StartDirectives(self) -> CodeDirectiveCollection:
        """"""
    @property
    def UserData(self) -> IDictionary:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CodeStatementCollection(CollectionBase, ICollection, IEnumerable, IList):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, value: CodeStatementCollection) -> None:
        """"""
    @overload
    def __init__(self, value: Array[CodeStatement]) -> None:
        """"""
    @property
    def Capacity(self) -> int:
        """"""
    @Capacity.setter
    def Capacity(self, value: int) -> None: ...
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsFixedSize(self) -> bool:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def Item(self) -> CodeStatement:
        """"""
    @Item.setter
    def Item(self, value: CodeStatement) -> None: ...
    @property
    def SyncRoot(self) -> object:
        """"""
    @overload
    def Add(self, value: CodeExpression) -> int:
        """"""
    @overload
    def Add(self, value: CodeStatement) -> int:
        """"""
    @overload
    def Add(self, value: object) -> int:
        """"""
    @overload
    def AddRange(self, value: CodeStatementCollection) -> None:
        """"""
    @overload
    def AddRange(self, value: Array[CodeStatement]) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    @overload
    def Contains(self, value: CodeStatement) -> bool:
        """"""
    @overload
    def Contains(self, value: object) -> bool:
        """"""
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array[CodeStatement], index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IndexOf(self, value: CodeStatement) -> int:
        """"""
    @overload
    def IndexOf(self, value: object) -> int:
        """"""
    @overload
    def Insert(self, index: int, value: CodeStatement) -> None:
        """"""
    @overload
    def Insert(self, index: int, value: object) -> None:
        """"""
    @overload
    def Remove(self, value: CodeStatement) -> None:
        """"""
    @overload
    def Remove(self, value: object) -> None:
        """"""
    def RemoveAt(self, index: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __contains__(self, value: CodeStatement) -> bool:
        """"""
    @overload
    def __contains__(self, value: object) -> bool:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    @overload
    def __delitem__(self, value: CodeStatement) -> None:
        """"""
    @overload
    def __delitem__(self, value: object) -> None:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, index: int) -> CodeStatement:
        """"""
    @overload
    def __setitem__(self, index: int, value: CodeStatement) -> None:
        """"""
    @overload
    def __setitem__(self, index: int, value: object) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CodeThisReferenceExpression(CodeExpression):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def UserData(self) -> IDictionary:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CodeThrowExceptionStatement(CodeStatement):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, toThrow: CodeExpression) -> None:
        """"""
    @property
    def EndDirectives(self) -> CodeDirectiveCollection:
        """"""
    @property
    def LinePragma(self) -> CodeLinePragma:
        """"""
    @LinePragma.setter
    def LinePragma(self, value: CodeLinePragma) -> None: ...
    @property
    def StartDirectives(self) -> CodeDirectiveCollection:
        """"""
    @property
    def ToThrow(self) -> CodeExpression:
        """"""
    @ToThrow.setter
    def ToThrow(self, value: CodeExpression) -> None: ...
    @property
    def UserData(self) -> IDictionary:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CodeTryCatchFinallyStatement(CodeStatement):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(
        self, tryStatements: Array[CodeStatement], catchClauses: Array[CodeCatchClause]
    ) -> None:
        """"""
    @overload
    def __init__(
        self,
        tryStatements: Array[CodeStatement],
        catchClauses: Array[CodeCatchClause],
        finallyStatements: Array[CodeStatement],
    ) -> None:
        """"""
    @property
    def CatchClauses(self) -> CodeCatchClauseCollection:
        """"""
    @property
    def EndDirectives(self) -> CodeDirectiveCollection:
        """"""
    @property
    def FinallyStatements(self) -> CodeStatementCollection:
        """"""
    @property
    def LinePragma(self) -> CodeLinePragma:
        """"""
    @LinePragma.setter
    def LinePragma(self, value: CodeLinePragma) -> None: ...
    @property
    def StartDirectives(self) -> CodeDirectiveCollection:
        """"""
    @property
    def TryStatements(self) -> CodeStatementCollection:
        """"""
    @property
    def UserData(self) -> IDictionary:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CodeTypeConstructor(CodeMemberMethod):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Attributes(self) -> MemberAttributes:
        """"""
    @Attributes.setter
    def Attributes(self, value: MemberAttributes) -> None: ...
    @property
    def Comments(self) -> CodeCommentStatementCollection:
        """"""
    @property
    def CustomAttributes(self) -> CodeAttributeDeclarationCollection:
        """"""
    @CustomAttributes.setter
    def CustomAttributes(self, value: CodeAttributeDeclarationCollection) -> None: ...
    @property
    def EndDirectives(self) -> CodeDirectiveCollection:
        """"""
    @property
    def ImplementationTypes(self) -> CodeTypeReferenceCollection:
        """"""
    @property
    def LinePragma(self) -> CodeLinePragma:
        """"""
    @LinePragma.setter
    def LinePragma(self, value: CodeLinePragma) -> None: ...
    @property
    def Name(self) -> str:
        """"""
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def Parameters(self) -> CodeParameterDeclarationExpressionCollection:
        """"""
    @property
    def PrivateImplementationType(self) -> CodeTypeReference:
        """"""
    @PrivateImplementationType.setter
    def PrivateImplementationType(self, value: CodeTypeReference) -> None: ...
    @property
    def ReturnType(self) -> CodeTypeReference:
        """"""
    @ReturnType.setter
    def ReturnType(self, value: CodeTypeReference) -> None: ...
    @property
    def ReturnTypeCustomAttributes(self) -> CodeAttributeDeclarationCollection:
        """"""
    @property
    def StartDirectives(self) -> CodeDirectiveCollection:
        """"""
    @property
    def Statements(self) -> CodeStatementCollection:
        """"""
    @property
    def TypeParameters(self) -> CodeTypeParameterCollection:
        """"""
    @property
    def UserData(self) -> IDictionary:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    PopulateImplementationTypes: EventType[EventHandler] = ...
    """"""
    PopulateParameters: EventType[EventHandler] = ...
    """"""
    PopulateStatements: EventType[EventHandler] = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CodeTypeDeclaration(CodeTypeMember):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, name: str) -> None:
        """"""
    @property
    def Attributes(self) -> MemberAttributes:
        """"""
    @Attributes.setter
    def Attributes(self, value: MemberAttributes) -> None: ...
    @property
    def BaseTypes(self) -> CodeTypeReferenceCollection:
        """"""
    @property
    def Comments(self) -> CodeCommentStatementCollection:
        """"""
    @property
    def CustomAttributes(self) -> CodeAttributeDeclarationCollection:
        """"""
    @CustomAttributes.setter
    def CustomAttributes(self, value: CodeAttributeDeclarationCollection) -> None: ...
    @property
    def EndDirectives(self) -> CodeDirectiveCollection:
        """"""
    @property
    def IsClass(self) -> bool:
        """"""
    @IsClass.setter
    def IsClass(self, value: bool) -> None: ...
    @property
    def IsEnum(self) -> bool:
        """"""
    @IsEnum.setter
    def IsEnum(self, value: bool) -> None: ...
    @property
    def IsInterface(self) -> bool:
        """"""
    @IsInterface.setter
    def IsInterface(self, value: bool) -> None: ...
    @property
    def IsPartial(self) -> bool:
        """"""
    @IsPartial.setter
    def IsPartial(self, value: bool) -> None: ...
    @property
    def IsStruct(self) -> bool:
        """"""
    @IsStruct.setter
    def IsStruct(self, value: bool) -> None: ...
    @property
    def LinePragma(self) -> CodeLinePragma:
        """"""
    @LinePragma.setter
    def LinePragma(self, value: CodeLinePragma) -> None: ...
    @property
    def Members(self) -> CodeTypeMemberCollection:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def StartDirectives(self) -> CodeDirectiveCollection:
        """"""
    @property
    def TypeAttributes(self) -> TypeAttributes:
        """"""
    @TypeAttributes.setter
    def TypeAttributes(self, value: TypeAttributes) -> None: ...
    @property
    def TypeParameters(self) -> CodeTypeParameterCollection:
        """"""
    @property
    def UserData(self) -> IDictionary:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    PopulateBaseTypes: EventType[EventHandler] = ...
    """"""
    PopulateMembers: EventType[EventHandler] = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CodeTypeDeclarationCollection(CollectionBase, ICollection, IEnumerable, IList):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, value: CodeTypeDeclarationCollection) -> None:
        """"""
    @overload
    def __init__(self, value: Array[CodeTypeDeclaration]) -> None:
        """"""
    @property
    def Capacity(self) -> int:
        """"""
    @Capacity.setter
    def Capacity(self, value: int) -> None: ...
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsFixedSize(self) -> bool:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def Item(self) -> CodeTypeDeclaration:
        """"""
    @Item.setter
    def Item(self, value: CodeTypeDeclaration) -> None: ...
    @property
    def SyncRoot(self) -> object:
        """"""
    @overload
    def Add(self, value: CodeTypeDeclaration) -> int:
        """"""
    @overload
    def Add(self, value: object) -> int:
        """"""
    @overload
    def AddRange(self, value: CodeTypeDeclarationCollection) -> None:
        """"""
    @overload
    def AddRange(self, value: Array[CodeTypeDeclaration]) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    @overload
    def Contains(self, value: CodeTypeDeclaration) -> bool:
        """"""
    @overload
    def Contains(self, value: object) -> bool:
        """"""
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array[CodeTypeDeclaration], index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IndexOf(self, value: CodeTypeDeclaration) -> int:
        """"""
    @overload
    def IndexOf(self, value: object) -> int:
        """"""
    @overload
    def Insert(self, index: int, value: CodeTypeDeclaration) -> None:
        """"""
    @overload
    def Insert(self, index: int, value: object) -> None:
        """"""
    @overload
    def Remove(self, value: CodeTypeDeclaration) -> None:
        """"""
    @overload
    def Remove(self, value: object) -> None:
        """"""
    def RemoveAt(self, index: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __contains__(self, value: CodeTypeDeclaration) -> bool:
        """"""
    @overload
    def __contains__(self, value: object) -> bool:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    @overload
    def __delitem__(self, value: CodeTypeDeclaration) -> None:
        """"""
    @overload
    def __delitem__(self, value: object) -> None:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, index: int) -> CodeTypeDeclaration:
        """"""
    @overload
    def __setitem__(self, index: int, value: CodeTypeDeclaration) -> None:
        """"""
    @overload
    def __setitem__(self, index: int, value: object) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CodeTypeDelegate(CodeTypeDeclaration):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, name: str) -> None:
        """"""
    @property
    def Attributes(self) -> MemberAttributes:
        """"""
    @Attributes.setter
    def Attributes(self, value: MemberAttributes) -> None: ...
    @property
    def BaseTypes(self) -> CodeTypeReferenceCollection:
        """"""
    @property
    def Comments(self) -> CodeCommentStatementCollection:
        """"""
    @property
    def CustomAttributes(self) -> CodeAttributeDeclarationCollection:
        """"""
    @CustomAttributes.setter
    def CustomAttributes(self, value: CodeAttributeDeclarationCollection) -> None: ...
    @property
    def EndDirectives(self) -> CodeDirectiveCollection:
        """"""
    @property
    def IsClass(self) -> bool:
        """"""
    @IsClass.setter
    def IsClass(self, value: bool) -> None: ...
    @property
    def IsEnum(self) -> bool:
        """"""
    @IsEnum.setter
    def IsEnum(self, value: bool) -> None: ...
    @property
    def IsInterface(self) -> bool:
        """"""
    @IsInterface.setter
    def IsInterface(self, value: bool) -> None: ...
    @property
    def IsPartial(self) -> bool:
        """"""
    @IsPartial.setter
    def IsPartial(self, value: bool) -> None: ...
    @property
    def IsStruct(self) -> bool:
        """"""
    @IsStruct.setter
    def IsStruct(self, value: bool) -> None: ...
    @property
    def LinePragma(self) -> CodeLinePragma:
        """"""
    @LinePragma.setter
    def LinePragma(self, value: CodeLinePragma) -> None: ...
    @property
    def Members(self) -> CodeTypeMemberCollection:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def Parameters(self) -> CodeParameterDeclarationExpressionCollection:
        """"""
    @property
    def ReturnType(self) -> CodeTypeReference:
        """"""
    @ReturnType.setter
    def ReturnType(self, value: CodeTypeReference) -> None: ...
    @property
    def StartDirectives(self) -> CodeDirectiveCollection:
        """"""
    @property
    def TypeAttributes(self) -> TypeAttributes:
        """"""
    @TypeAttributes.setter
    def TypeAttributes(self, value: TypeAttributes) -> None: ...
    @property
    def TypeParameters(self) -> CodeTypeParameterCollection:
        """"""
    @property
    def UserData(self) -> IDictionary:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    PopulateBaseTypes: EventType[EventHandler] = ...
    """"""
    PopulateMembers: EventType[EventHandler] = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CodeTypeMember(CodeObject):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Attributes(self) -> MemberAttributes:
        """"""
    @Attributes.setter
    def Attributes(self, value: MemberAttributes) -> None: ...
    @property
    def Comments(self) -> CodeCommentStatementCollection:
        """"""
    @property
    def CustomAttributes(self) -> CodeAttributeDeclarationCollection:
        """"""
    @CustomAttributes.setter
    def CustomAttributes(self, value: CodeAttributeDeclarationCollection) -> None: ...
    @property
    def EndDirectives(self) -> CodeDirectiveCollection:
        """"""
    @property
    def LinePragma(self) -> CodeLinePragma:
        """"""
    @LinePragma.setter
    def LinePragma(self, value: CodeLinePragma) -> None: ...
    @property
    def Name(self) -> str:
        """"""
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def StartDirectives(self) -> CodeDirectiveCollection:
        """"""
    @property
    def UserData(self) -> IDictionary:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CodeTypeMemberCollection(CollectionBase, ICollection, IEnumerable, IList):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, value: CodeTypeMemberCollection) -> None:
        """"""
    @overload
    def __init__(self, value: Array[CodeTypeMember]) -> None:
        """"""
    @property
    def Capacity(self) -> int:
        """"""
    @Capacity.setter
    def Capacity(self, value: int) -> None: ...
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsFixedSize(self) -> bool:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def Item(self) -> CodeTypeMember:
        """"""
    @Item.setter
    def Item(self, value: CodeTypeMember) -> None: ...
    @property
    def SyncRoot(self) -> object:
        """"""
    @overload
    def Add(self, value: CodeTypeMember) -> int:
        """"""
    @overload
    def Add(self, value: object) -> int:
        """"""
    @overload
    def AddRange(self, value: CodeTypeMemberCollection) -> None:
        """"""
    @overload
    def AddRange(self, value: Array[CodeTypeMember]) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    @overload
    def Contains(self, value: CodeTypeMember) -> bool:
        """"""
    @overload
    def Contains(self, value: object) -> bool:
        """"""
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array[CodeTypeMember], index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IndexOf(self, value: CodeTypeMember) -> int:
        """"""
    @overload
    def IndexOf(self, value: object) -> int:
        """"""
    @overload
    def Insert(self, index: int, value: CodeTypeMember) -> None:
        """"""
    @overload
    def Insert(self, index: int, value: object) -> None:
        """"""
    @overload
    def Remove(self, value: CodeTypeMember) -> None:
        """"""
    @overload
    def Remove(self, value: object) -> None:
        """"""
    def RemoveAt(self, index: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __contains__(self, value: CodeTypeMember) -> bool:
        """"""
    @overload
    def __contains__(self, value: object) -> bool:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    @overload
    def __delitem__(self, value: CodeTypeMember) -> None:
        """"""
    @overload
    def __delitem__(self, value: object) -> None:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, index: int) -> CodeTypeMember:
        """"""
    @overload
    def __setitem__(self, index: int, value: CodeTypeMember) -> None:
        """"""
    @overload
    def __setitem__(self, index: int, value: object) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CodeTypeOfExpression(CodeExpression):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, type: CodeTypeReference) -> None:
        """"""
    @overload
    def __init__(self, type: str) -> None:
        """"""
    @overload
    def __init__(self, type: Type) -> None:
        """"""
    @property
    def Type(self) -> CodeTypeReference:
        """"""
    @Type.setter
    def Type(self, value: CodeTypeReference) -> None: ...
    @property
    def UserData(self) -> IDictionary:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CodeTypeParameter(CodeObject):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, name: str) -> None:
        """"""
    @property
    def Constraints(self) -> CodeTypeReferenceCollection:
        """"""
    @property
    def CustomAttributes(self) -> CodeAttributeDeclarationCollection:
        """"""
    @property
    def HasConstructorConstraint(self) -> bool:
        """"""
    @HasConstructorConstraint.setter
    def HasConstructorConstraint(self, value: bool) -> None: ...
    @property
    def Name(self) -> str:
        """"""
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def UserData(self) -> IDictionary:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CodeTypeParameterCollection(CollectionBase, ICollection, IEnumerable, IList):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, value: CodeTypeParameterCollection) -> None:
        """"""
    @overload
    def __init__(self, value: Array[CodeTypeParameter]) -> None:
        """"""
    @property
    def Capacity(self) -> int:
        """"""
    @Capacity.setter
    def Capacity(self, value: int) -> None: ...
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsFixedSize(self) -> bool:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def Item(self) -> CodeTypeParameter:
        """"""
    @Item.setter
    def Item(self, value: CodeTypeParameter) -> None: ...
    @property
    def SyncRoot(self) -> object:
        """"""
    @overload
    def Add(self, value: CodeTypeParameter) -> int:
        """"""
    @overload
    def Add(self, value: object) -> int:
        """"""
    @overload
    def Add(self, value: str) -> None:
        """"""
    @overload
    def AddRange(self, value: CodeTypeParameterCollection) -> None:
        """"""
    @overload
    def AddRange(self, value: Array[CodeTypeParameter]) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    @overload
    def Contains(self, value: CodeTypeParameter) -> bool:
        """"""
    @overload
    def Contains(self, value: object) -> bool:
        """"""
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array[CodeTypeParameter], index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IndexOf(self, value: CodeTypeParameter) -> int:
        """"""
    @overload
    def IndexOf(self, value: object) -> int:
        """"""
    @overload
    def Insert(self, index: int, value: CodeTypeParameter) -> None:
        """"""
    @overload
    def Insert(self, index: int, value: object) -> None:
        """"""
    @overload
    def Remove(self, value: CodeTypeParameter) -> None:
        """"""
    @overload
    def Remove(self, value: object) -> None:
        """"""
    def RemoveAt(self, index: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __contains__(self, value: CodeTypeParameter) -> bool:
        """"""
    @overload
    def __contains__(self, value: object) -> bool:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    @overload
    def __delitem__(self, value: CodeTypeParameter) -> None:
        """"""
    @overload
    def __delitem__(self, value: object) -> None:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, index: int) -> CodeTypeParameter:
        """"""
    @overload
    def __setitem__(self, index: int, value: CodeTypeParameter) -> None:
        """"""
    @overload
    def __setitem__(self, index: int, value: object) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CodeTypeReference(CodeObject):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, type: Type) -> None:
        """"""
    @overload
    def __init__(self, type: Type, codeTypeReferenceOption: CodeTypeReferenceOptions) -> None:
        """"""
    @overload
    def __init__(self, typeName: str, codeTypeReferenceOption: CodeTypeReferenceOptions) -> None:
        """"""
    @overload
    def __init__(self, typeName: str) -> None:
        """"""
    @overload
    def __init__(self, typeName: str, typeArguments: Array[CodeTypeReference]) -> None:
        """"""
    @overload
    def __init__(self, typeParameter: CodeTypeParameter) -> None:
        """"""
    @overload
    def __init__(self, baseType: str, rank: int) -> None:
        """"""
    @overload
    def __init__(self, arrayType: CodeTypeReference, rank: int) -> None:
        """"""
    @property
    def ArrayElementType(self) -> CodeTypeReference:
        """"""
    @ArrayElementType.setter
    def ArrayElementType(self, value: CodeTypeReference) -> None: ...
    @property
    def ArrayRank(self) -> int:
        """"""
    @ArrayRank.setter
    def ArrayRank(self, value: int) -> None: ...
    @property
    def BaseType(self) -> str:
        """"""
    @BaseType.setter
    def BaseType(self, value: str) -> None: ...
    @property
    def Options(self) -> CodeTypeReferenceOptions:
        """"""
    @Options.setter
    def Options(self, value: CodeTypeReferenceOptions) -> None: ...
    @property
    def TypeArguments(self) -> CodeTypeReferenceCollection:
        """"""
    @property
    def UserData(self) -> IDictionary:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CodeTypeReferenceCollection(CollectionBase, ICollection, IEnumerable, IList):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, value: CodeTypeReferenceCollection) -> None:
        """"""
    @overload
    def __init__(self, value: Array[CodeTypeReference]) -> None:
        """"""
    @property
    def Capacity(self) -> int:
        """"""
    @Capacity.setter
    def Capacity(self, value: int) -> None: ...
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsFixedSize(self) -> bool:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def Item(self) -> CodeTypeReference:
        """"""
    @Item.setter
    def Item(self, value: CodeTypeReference) -> None: ...
    @property
    def SyncRoot(self) -> object:
        """"""
    @overload
    def Add(self, value: CodeTypeReference) -> int:
        """"""
    @overload
    def Add(self, value: object) -> int:
        """"""
    @overload
    def Add(self, value: str) -> None:
        """"""
    @overload
    def Add(self, value: Type) -> None:
        """"""
    @overload
    def AddRange(self, value: CodeTypeReferenceCollection) -> None:
        """"""
    @overload
    def AddRange(self, value: Array[CodeTypeReference]) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    @overload
    def Contains(self, value: CodeTypeReference) -> bool:
        """"""
    @overload
    def Contains(self, value: object) -> bool:
        """"""
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array[CodeTypeReference], index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IndexOf(self, value: CodeTypeReference) -> int:
        """"""
    @overload
    def IndexOf(self, value: object) -> int:
        """"""
    @overload
    def Insert(self, index: int, value: CodeTypeReference) -> None:
        """"""
    @overload
    def Insert(self, index: int, value: object) -> None:
        """"""
    @overload
    def Remove(self, value: CodeTypeReference) -> None:
        """"""
    @overload
    def Remove(self, value: object) -> None:
        """"""
    def RemoveAt(self, index: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __contains__(self, value: CodeTypeReference) -> bool:
        """"""
    @overload
    def __contains__(self, value: object) -> bool:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    @overload
    def __delitem__(self, value: CodeTypeReference) -> None:
        """"""
    @overload
    def __delitem__(self, value: object) -> None:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, index: int) -> CodeTypeReference:
        """"""
    @overload
    def __setitem__(self, index: int, value: CodeTypeReference) -> None:
        """"""
    @overload
    def __setitem__(self, index: int, value: object) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CodeTypeReferenceExpression(CodeExpression):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, type: CodeTypeReference) -> None:
        """"""
    @overload
    def __init__(self, type: str) -> None:
        """"""
    @overload
    def __init__(self, type: Type) -> None:
        """"""
    @property
    def Type(self) -> CodeTypeReference:
        """"""
    @Type.setter
    def Type(self, value: CodeTypeReference) -> None: ...
    @property
    def UserData(self) -> IDictionary:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class CodeTypeReferenceOptions(Enum):
    """"""

    GlobalReference: CodeTypeReferenceOptions = ...
    """"""
    GenericTypeParameter: CodeTypeReferenceOptions = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CodeVariableDeclarationStatement(CodeStatement):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, type: CodeTypeReference, name: str) -> None:
        """"""
    @overload
    def __init__(self, type: str, name: str) -> None:
        """"""
    @overload
    def __init__(self, type: Type, name: str) -> None:
        """"""
    @overload
    def __init__(self, type: CodeTypeReference, name: str, initExpression: CodeExpression) -> None:
        """"""
    @overload
    def __init__(self, type: str, name: str, initExpression: CodeExpression) -> None:
        """"""
    @overload
    def __init__(self, type: Type, name: str, initExpression: CodeExpression) -> None:
        """"""
    @property
    def EndDirectives(self) -> CodeDirectiveCollection:
        """"""
    @property
    def InitExpression(self) -> CodeExpression:
        """"""
    @InitExpression.setter
    def InitExpression(self, value: CodeExpression) -> None: ...
    @property
    def LinePragma(self) -> CodeLinePragma:
        """"""
    @LinePragma.setter
    def LinePragma(self, value: CodeLinePragma) -> None: ...
    @property
    def Name(self) -> str:
        """"""
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def StartDirectives(self) -> CodeDirectiveCollection:
        """"""
    @property
    def Type(self) -> CodeTypeReference:
        """"""
    @Type.setter
    def Type(self, value: CodeTypeReference) -> None: ...
    @property
    def UserData(self) -> IDictionary:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CodeVariableReferenceExpression(CodeExpression):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, variableName: str) -> None:
        """"""
    @property
    def UserData(self) -> IDictionary:
        """"""
    @property
    def VariableName(self) -> str:
        """"""
    @VariableName.setter
    def VariableName(self, value: str) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class FieldDirection(Enum):
    """"""

    In: FieldDirection = ...
    """"""
    Out: FieldDirection = ...
    """"""
    Ref: FieldDirection = ...
    """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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
