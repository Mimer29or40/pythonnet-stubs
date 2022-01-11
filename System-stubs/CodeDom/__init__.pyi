from __future__ import annotations

from typing import Generic, List, TypeVar, Union, overload

from System import Array, Boolean, Byte, Enum, EventHandler, Guid, Int32, Object, String, Type, Void
from System.Collections import CollectionBase, ICollection, IDictionary, IEnumerable, IEnumerator, IList
from System.Collections.Specialized import StringCollection
from System.Reflection import TypeAttributes

# ---------- Types ---------- #

T = TypeVar('T')

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
ByteType = Union[int, Byte]
IntType = Union[int, Int32]
ObjectType = Object
StringType = Union[str, String]
TypeType = Union[type, Type]
VoidType = Union[None, Void]


class EventType(Generic[T]):
    def __iadd__(self, other: T): ...
    
    def __isub__(self, other: T): ...



# ---------- Classes ---------- #

class CodeArgumentReferenceExpression(CodeExpression):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, parameterName: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ParameterName(self) -> StringType: ...
    
    @ParameterName.setter
    def ParameterName(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_ParameterName(self) -> StringType: ...
    
    def set_ParameterName(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeArrayCreateExpression(CodeExpression):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, createType: CodeTypeReference, initializers: ArrayType[CodeExpression]): ...
    
    @overload
    def __init__(self, createType: StringType, initializers: ArrayType[CodeExpression]): ...
    
    @overload
    def __init__(self, createType: TypeType, initializers: ArrayType[CodeExpression]): ...
    
    @overload
    def __init__(self, createType: CodeTypeReference, size: IntType): ...
    
    @overload
    def __init__(self, createType: StringType, size: IntType): ...
    
    @overload
    def __init__(self, createType: TypeType, size: IntType): ...
    
    @overload
    def __init__(self, createType: CodeTypeReference, size: CodeExpression): ...
    
    @overload
    def __init__(self, createType: StringType, size: CodeExpression): ...
    
    @overload
    def __init__(self, createType: TypeType, size: CodeExpression): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CreateType(self) -> CodeTypeReference: ...
    
    @CreateType.setter
    def CreateType(self, value: CodeTypeReference) -> None: ...
    
    @property
    def Initializers(self) -> CodeExpressionCollection: ...
    
    @property
    def Size(self) -> IntType: ...
    
    @Size.setter
    def Size(self, value: IntType) -> None: ...
    
    @property
    def SizeExpression(self) -> CodeExpression: ...
    
    @SizeExpression.setter
    def SizeExpression(self, value: CodeExpression) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_CreateType(self) -> CodeTypeReference: ...
    
    def get_Initializers(self) -> CodeExpressionCollection: ...
    
    def get_Size(self) -> IntType: ...
    
    def get_SizeExpression(self) -> CodeExpression: ...
    
    def set_CreateType(self, value: CodeTypeReference) -> VoidType: ...
    
    def set_Size(self, value: IntType) -> VoidType: ...
    
    def set_SizeExpression(self, value: CodeExpression) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeArrayIndexerExpression(CodeExpression):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, targetObject: CodeExpression, indices: ArrayType[CodeExpression]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Indices(self) -> CodeExpressionCollection: ...
    
    @property
    def TargetObject(self) -> CodeExpression: ...
    
    @TargetObject.setter
    def TargetObject(self, value: CodeExpression) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Indices(self) -> CodeExpressionCollection: ...
    
    def get_TargetObject(self) -> CodeExpression: ...
    
    def set_TargetObject(self, value: CodeExpression) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeAssignStatement(CodeStatement):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, left: CodeExpression, right: CodeExpression): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Left(self) -> CodeExpression: ...
    
    @Left.setter
    def Left(self, value: CodeExpression) -> None: ...
    
    @property
    def Right(self) -> CodeExpression: ...
    
    @Right.setter
    def Right(self, value: CodeExpression) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Left(self) -> CodeExpression: ...
    
    def get_Right(self) -> CodeExpression: ...
    
    def set_Left(self, value: CodeExpression) -> VoidType: ...
    
    def set_Right(self, value: CodeExpression) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeAttachEventStatement(CodeStatement):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, eventRef: CodeEventReferenceExpression, listener: CodeExpression): ...
    
    @overload
    def __init__(self, targetObject: CodeExpression, eventName: StringType, listener: CodeExpression): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Event(self) -> CodeEventReferenceExpression: ...
    
    @Event.setter
    def Event(self, value: CodeEventReferenceExpression) -> None: ...
    
    @property
    def Listener(self) -> CodeExpression: ...
    
    @Listener.setter
    def Listener(self, value: CodeExpression) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Event(self) -> CodeEventReferenceExpression: ...
    
    def get_Listener(self) -> CodeExpression: ...
    
    def set_Event(self, value: CodeEventReferenceExpression) -> VoidType: ...
    
    def set_Listener(self, value: CodeExpression) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeAttributeArgument(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: CodeExpression): ...
    
    @overload
    def __init__(self, name: StringType, value: CodeExpression): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Name(self) -> StringType: ...
    
    @Name.setter
    def Name(self, value: StringType) -> None: ...
    
    @property
    def Value(self) -> CodeExpression: ...
    
    @Value.setter
    def Value(self, value: CodeExpression) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Name(self) -> StringType: ...
    
    def get_Value(self) -> CodeExpression: ...
    
    def set_Name(self, value: StringType) -> VoidType: ...
    
    def set_Value(self, value: CodeExpression) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeAttributeArgumentCollection(CollectionBase, IList, ICollection, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: CodeAttributeArgumentCollection): ...
    
    @overload
    def __init__(self, value: ArrayType[CodeAttributeArgument]): ...
    
    # ---------- Properties ---------- #
    
    def __getitem__(self, key: IntType) -> CodeAttributeArgument: ...
    
    def __setitem__(self, key: IntType, value: CodeAttributeArgument) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Add(self, value: CodeAttributeArgument) -> IntType: ...
    
    @overload
    def AddRange(self, value: ArrayType[CodeAttributeArgument]) -> VoidType: ...
    
    @overload
    def AddRange(self, value: CodeAttributeArgumentCollection) -> VoidType: ...
    
    def Contains(self, value: CodeAttributeArgument) -> BooleanType: ...
    
    def CopyTo(self, array: ArrayType[CodeAttributeArgument], index: IntType) -> VoidType: ...
    
    def IndexOf(self, value: CodeAttributeArgument) -> IntType: ...
    
    def Insert(self, index: IntType, value: CodeAttributeArgument) -> VoidType: ...
    
    def Remove(self, value: CodeAttributeArgument) -> VoidType: ...
    
    def get_Item(self, index: IntType) -> CodeAttributeArgument: ...
    
    def set_Item(self, index: IntType, value: CodeAttributeArgument) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeAttributeDeclaration(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, name: StringType): ...
    
    @overload
    def __init__(self, name: StringType, arguments: ArrayType[CodeAttributeArgument]): ...
    
    @overload
    def __init__(self, attributeType: CodeTypeReference): ...
    
    @overload
    def __init__(self, attributeType: CodeTypeReference, arguments: ArrayType[CodeAttributeArgument]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Arguments(self) -> CodeAttributeArgumentCollection: ...
    
    @property
    def AttributeType(self) -> CodeTypeReference: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @Name.setter
    def Name(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Arguments(self) -> CodeAttributeArgumentCollection: ...
    
    def get_AttributeType(self) -> CodeTypeReference: ...
    
    def get_Name(self) -> StringType: ...
    
    def set_Name(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeAttributeDeclarationCollection(CollectionBase, IList, ICollection, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: CodeAttributeDeclarationCollection): ...
    
    @overload
    def __init__(self, value: ArrayType[CodeAttributeDeclaration]): ...
    
    # ---------- Properties ---------- #
    
    def __getitem__(self, key: IntType) -> CodeAttributeDeclaration: ...
    
    def __setitem__(self, key: IntType, value: CodeAttributeDeclaration) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Add(self, value: CodeAttributeDeclaration) -> IntType: ...
    
    @overload
    def AddRange(self, value: ArrayType[CodeAttributeDeclaration]) -> VoidType: ...
    
    @overload
    def AddRange(self, value: CodeAttributeDeclarationCollection) -> VoidType: ...
    
    def Contains(self, value: CodeAttributeDeclaration) -> BooleanType: ...
    
    def CopyTo(self, array: ArrayType[CodeAttributeDeclaration], index: IntType) -> VoidType: ...
    
    def IndexOf(self, value: CodeAttributeDeclaration) -> IntType: ...
    
    def Insert(self, index: IntType, value: CodeAttributeDeclaration) -> VoidType: ...
    
    def Remove(self, value: CodeAttributeDeclaration) -> VoidType: ...
    
    def get_Item(self, index: IntType) -> CodeAttributeDeclaration: ...
    
    def set_Item(self, index: IntType, value: CodeAttributeDeclaration) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeBaseReferenceExpression(CodeExpression):
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


class CodeBinaryOperatorExpression(CodeExpression):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, left: CodeExpression, op: CodeBinaryOperatorType, right: CodeExpression): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Left(self) -> CodeExpression: ...
    
    @Left.setter
    def Left(self, value: CodeExpression) -> None: ...
    
    @property
    def Operator(self) -> CodeBinaryOperatorType: ...
    
    @Operator.setter
    def Operator(self, value: CodeBinaryOperatorType) -> None: ...
    
    @property
    def Right(self) -> CodeExpression: ...
    
    @Right.setter
    def Right(self, value: CodeExpression) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Left(self) -> CodeExpression: ...
    
    def get_Operator(self) -> CodeBinaryOperatorType: ...
    
    def get_Right(self) -> CodeExpression: ...
    
    def set_Left(self, value: CodeExpression) -> VoidType: ...
    
    def set_Operator(self, value: CodeBinaryOperatorType) -> VoidType: ...
    
    def set_Right(self, value: CodeExpression) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeCastExpression(CodeExpression):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, targetType: CodeTypeReference, expression: CodeExpression): ...
    
    @overload
    def __init__(self, targetType: StringType, expression: CodeExpression): ...
    
    @overload
    def __init__(self, targetType: TypeType, expression: CodeExpression): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Expression(self) -> CodeExpression: ...
    
    @Expression.setter
    def Expression(self, value: CodeExpression) -> None: ...
    
    @property
    def TargetType(self) -> CodeTypeReference: ...
    
    @TargetType.setter
    def TargetType(self, value: CodeTypeReference) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Expression(self) -> CodeExpression: ...
    
    def get_TargetType(self) -> CodeTypeReference: ...
    
    def set_Expression(self, value: CodeExpression) -> VoidType: ...
    
    def set_TargetType(self, value: CodeTypeReference) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeCatchClause(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, localName: StringType): ...
    
    @overload
    def __init__(self, localName: StringType, catchExceptionType: CodeTypeReference): ...
    
    @overload
    def __init__(self, localName: StringType, catchExceptionType: CodeTypeReference, statements: ArrayType[CodeStatement]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CatchExceptionType(self) -> CodeTypeReference: ...
    
    @CatchExceptionType.setter
    def CatchExceptionType(self, value: CodeTypeReference) -> None: ...
    
    @property
    def LocalName(self) -> StringType: ...
    
    @LocalName.setter
    def LocalName(self, value: StringType) -> None: ...
    
    @property
    def Statements(self) -> CodeStatementCollection: ...
    
    # ---------- Methods ---------- #
    
    def get_CatchExceptionType(self) -> CodeTypeReference: ...
    
    def get_LocalName(self) -> StringType: ...
    
    def get_Statements(self) -> CodeStatementCollection: ...
    
    def set_CatchExceptionType(self, value: CodeTypeReference) -> VoidType: ...
    
    def set_LocalName(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeCatchClauseCollection(CollectionBase, IList, ICollection, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: CodeCatchClauseCollection): ...
    
    @overload
    def __init__(self, value: ArrayType[CodeCatchClause]): ...
    
    # ---------- Properties ---------- #
    
    def __getitem__(self, key: IntType) -> CodeCatchClause: ...
    
    def __setitem__(self, key: IntType, value: CodeCatchClause) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Add(self, value: CodeCatchClause) -> IntType: ...
    
    @overload
    def AddRange(self, value: ArrayType[CodeCatchClause]) -> VoidType: ...
    
    @overload
    def AddRange(self, value: CodeCatchClauseCollection) -> VoidType: ...
    
    def Contains(self, value: CodeCatchClause) -> BooleanType: ...
    
    def CopyTo(self, array: ArrayType[CodeCatchClause], index: IntType) -> VoidType: ...
    
    def IndexOf(self, value: CodeCatchClause) -> IntType: ...
    
    def Insert(self, index: IntType, value: CodeCatchClause) -> VoidType: ...
    
    def Remove(self, value: CodeCatchClause) -> VoidType: ...
    
    def get_Item(self, index: IntType) -> CodeCatchClause: ...
    
    def set_Item(self, index: IntType, value: CodeCatchClause) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeChecksumPragma(CodeDirective):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, fileName: StringType, checksumAlgorithmId: Guid, checksumData: ArrayType[ByteType]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ChecksumAlgorithmId(self) -> Guid: ...
    
    @ChecksumAlgorithmId.setter
    def ChecksumAlgorithmId(self, value: Guid) -> None: ...
    
    @property
    def ChecksumData(self) -> ArrayType[ByteType]: ...
    
    @ChecksumData.setter
    def ChecksumData(self, value: ArrayType[ByteType]) -> None: ...
    
    @property
    def FileName(self) -> StringType: ...
    
    @FileName.setter
    def FileName(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_ChecksumAlgorithmId(self) -> Guid: ...
    
    def get_ChecksumData(self) -> ArrayType[ByteType]: ...
    
    def get_FileName(self) -> StringType: ...
    
    def set_ChecksumAlgorithmId(self, value: Guid) -> VoidType: ...
    
    def set_ChecksumData(self, value: ArrayType[ByteType]) -> VoidType: ...
    
    def set_FileName(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeComment(CodeObject):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, text: StringType): ...
    
    @overload
    def __init__(self, text: StringType, docComment: BooleanType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def DocComment(self) -> BooleanType: ...
    
    @DocComment.setter
    def DocComment(self, value: BooleanType) -> None: ...
    
    @property
    def Text(self) -> StringType: ...
    
    @Text.setter
    def Text(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_DocComment(self) -> BooleanType: ...
    
    def get_Text(self) -> StringType: ...
    
    def set_DocComment(self, value: BooleanType) -> VoidType: ...
    
    def set_Text(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeCommentStatement(CodeStatement):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, comment: CodeComment): ...
    
    @overload
    def __init__(self, text: StringType): ...
    
    @overload
    def __init__(self, text: StringType, docComment: BooleanType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Comment(self) -> CodeComment: ...
    
    @Comment.setter
    def Comment(self, value: CodeComment) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Comment(self) -> CodeComment: ...
    
    def set_Comment(self, value: CodeComment) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeCommentStatementCollection(CollectionBase, IList, ICollection, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: CodeCommentStatementCollection): ...
    
    @overload
    def __init__(self, value: ArrayType[CodeCommentStatement]): ...
    
    # ---------- Properties ---------- #
    
    def __getitem__(self, key: IntType) -> CodeCommentStatement: ...
    
    def __setitem__(self, key: IntType, value: CodeCommentStatement) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Add(self, value: CodeCommentStatement) -> IntType: ...
    
    @overload
    def AddRange(self, value: ArrayType[CodeCommentStatement]) -> VoidType: ...
    
    @overload
    def AddRange(self, value: CodeCommentStatementCollection) -> VoidType: ...
    
    def Contains(self, value: CodeCommentStatement) -> BooleanType: ...
    
    def CopyTo(self, array: ArrayType[CodeCommentStatement], index: IntType) -> VoidType: ...
    
    def IndexOf(self, value: CodeCommentStatement) -> IntType: ...
    
    def Insert(self, index: IntType, value: CodeCommentStatement) -> VoidType: ...
    
    def Remove(self, value: CodeCommentStatement) -> VoidType: ...
    
    def get_Item(self, index: IntType) -> CodeCommentStatement: ...
    
    def set_Item(self, index: IntType, value: CodeCommentStatement) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeCompileUnit(CodeObject):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AssemblyCustomAttributes(self) -> CodeAttributeDeclarationCollection: ...
    
    @property
    def EndDirectives(self) -> CodeDirectiveCollection: ...
    
    @property
    def Namespaces(self) -> CodeNamespaceCollection: ...
    
    @property
    def ReferencedAssemblies(self) -> StringCollection: ...
    
    @property
    def StartDirectives(self) -> CodeDirectiveCollection: ...
    
    # ---------- Methods ---------- #
    
    def get_AssemblyCustomAttributes(self) -> CodeAttributeDeclarationCollection: ...
    
    def get_EndDirectives(self) -> CodeDirectiveCollection: ...
    
    def get_Namespaces(self) -> CodeNamespaceCollection: ...
    
    def get_ReferencedAssemblies(self) -> StringCollection: ...
    
    def get_StartDirectives(self) -> CodeDirectiveCollection: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeConditionStatement(CodeStatement):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, condition: CodeExpression, trueStatements: ArrayType[CodeStatement]): ...
    
    @overload
    def __init__(self, condition: CodeExpression, trueStatements: ArrayType[CodeStatement], falseStatements: ArrayType[CodeStatement]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Condition(self) -> CodeExpression: ...
    
    @Condition.setter
    def Condition(self, value: CodeExpression) -> None: ...
    
    @property
    def FalseStatements(self) -> CodeStatementCollection: ...
    
    @property
    def TrueStatements(self) -> CodeStatementCollection: ...
    
    # ---------- Methods ---------- #
    
    def get_Condition(self) -> CodeExpression: ...
    
    def get_FalseStatements(self) -> CodeStatementCollection: ...
    
    def get_TrueStatements(self) -> CodeStatementCollection: ...
    
    def set_Condition(self, value: CodeExpression) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeConstructor(CodeMemberMethod):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def BaseConstructorArgs(self) -> CodeExpressionCollection: ...
    
    @property
    def ChainedConstructorArgs(self) -> CodeExpressionCollection: ...
    
    # ---------- Methods ---------- #
    
    def get_BaseConstructorArgs(self) -> CodeExpressionCollection: ...
    
    def get_ChainedConstructorArgs(self) -> CodeExpressionCollection: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeDefaultValueExpression(CodeExpression):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, type: CodeTypeReference): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Type(self) -> CodeTypeReference: ...
    
    @Type.setter
    def Type(self, value: CodeTypeReference) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Type(self) -> CodeTypeReference: ...
    
    def set_Type(self, value: CodeTypeReference) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeDelegateCreateExpression(CodeExpression):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, delegateType: CodeTypeReference, targetObject: CodeExpression, methodName: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def DelegateType(self) -> CodeTypeReference: ...
    
    @DelegateType.setter
    def DelegateType(self, value: CodeTypeReference) -> None: ...
    
    @property
    def MethodName(self) -> StringType: ...
    
    @MethodName.setter
    def MethodName(self, value: StringType) -> None: ...
    
    @property
    def TargetObject(self) -> CodeExpression: ...
    
    @TargetObject.setter
    def TargetObject(self, value: CodeExpression) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_DelegateType(self) -> CodeTypeReference: ...
    
    def get_MethodName(self) -> StringType: ...
    
    def get_TargetObject(self) -> CodeExpression: ...
    
    def set_DelegateType(self, value: CodeTypeReference) -> VoidType: ...
    
    def set_MethodName(self, value: StringType) -> VoidType: ...
    
    def set_TargetObject(self, value: CodeExpression) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeDelegateInvokeExpression(CodeExpression):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, targetObject: CodeExpression): ...
    
    @overload
    def __init__(self, targetObject: CodeExpression, parameters: ArrayType[CodeExpression]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Parameters(self) -> CodeExpressionCollection: ...
    
    @property
    def TargetObject(self) -> CodeExpression: ...
    
    @TargetObject.setter
    def TargetObject(self, value: CodeExpression) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Parameters(self) -> CodeExpressionCollection: ...
    
    def get_TargetObject(self) -> CodeExpression: ...
    
    def set_TargetObject(self, value: CodeExpression) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeDirectionExpression(CodeExpression):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, direction: FieldDirection, expression: CodeExpression): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Direction(self) -> FieldDirection: ...
    
    @Direction.setter
    def Direction(self, value: FieldDirection) -> None: ...
    
    @property
    def Expression(self) -> CodeExpression: ...
    
    @Expression.setter
    def Expression(self, value: CodeExpression) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Direction(self) -> FieldDirection: ...
    
    def get_Expression(self) -> CodeExpression: ...
    
    def set_Direction(self, value: FieldDirection) -> VoidType: ...
    
    def set_Expression(self, value: CodeExpression) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeDirective(CodeObject):
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


class CodeDirectiveCollection(CollectionBase, IList, ICollection, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: CodeDirectiveCollection): ...
    
    @overload
    def __init__(self, value: ArrayType[CodeDirective]): ...
    
    # ---------- Properties ---------- #
    
    def __getitem__(self, key: IntType) -> CodeDirective: ...
    
    def __setitem__(self, key: IntType, value: CodeDirective) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Add(self, value: CodeDirective) -> IntType: ...
    
    @overload
    def AddRange(self, value: ArrayType[CodeDirective]) -> VoidType: ...
    
    @overload
    def AddRange(self, value: CodeDirectiveCollection) -> VoidType: ...
    
    def Contains(self, value: CodeDirective) -> BooleanType: ...
    
    def CopyTo(self, array: ArrayType[CodeDirective], index: IntType) -> VoidType: ...
    
    def IndexOf(self, value: CodeDirective) -> IntType: ...
    
    def Insert(self, index: IntType, value: CodeDirective) -> VoidType: ...
    
    def Remove(self, value: CodeDirective) -> VoidType: ...
    
    def get_Item(self, index: IntType) -> CodeDirective: ...
    
    def set_Item(self, index: IntType, value: CodeDirective) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeEntryPointMethod(CodeMemberMethod):
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


class CodeEventReferenceExpression(CodeExpression):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, targetObject: CodeExpression, eventName: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def EventName(self) -> StringType: ...
    
    @EventName.setter
    def EventName(self, value: StringType) -> None: ...
    
    @property
    def TargetObject(self) -> CodeExpression: ...
    
    @TargetObject.setter
    def TargetObject(self, value: CodeExpression) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_EventName(self) -> StringType: ...
    
    def get_TargetObject(self) -> CodeExpression: ...
    
    def set_EventName(self, value: StringType) -> VoidType: ...
    
    def set_TargetObject(self, value: CodeExpression) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeExpression(CodeObject):
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


class CodeExpressionCollection(CollectionBase, IList, ICollection, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: CodeExpressionCollection): ...
    
    @overload
    def __init__(self, value: ArrayType[CodeExpression]): ...
    
    # ---------- Properties ---------- #
    
    def __getitem__(self, key: IntType) -> CodeExpression: ...
    
    def __setitem__(self, key: IntType, value: CodeExpression) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Add(self, value: CodeExpression) -> IntType: ...
    
    @overload
    def AddRange(self, value: ArrayType[CodeExpression]) -> VoidType: ...
    
    @overload
    def AddRange(self, value: CodeExpressionCollection) -> VoidType: ...
    
    def Contains(self, value: CodeExpression) -> BooleanType: ...
    
    def CopyTo(self, array: ArrayType[CodeExpression], index: IntType) -> VoidType: ...
    
    def IndexOf(self, value: CodeExpression) -> IntType: ...
    
    def Insert(self, index: IntType, value: CodeExpression) -> VoidType: ...
    
    def Remove(self, value: CodeExpression) -> VoidType: ...
    
    def get_Item(self, index: IntType) -> CodeExpression: ...
    
    def set_Item(self, index: IntType, value: CodeExpression) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeExpressionStatement(CodeStatement):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, expression: CodeExpression): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Expression(self) -> CodeExpression: ...
    
    @Expression.setter
    def Expression(self, value: CodeExpression) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Expression(self) -> CodeExpression: ...
    
    def set_Expression(self, value: CodeExpression) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeFieldReferenceExpression(CodeExpression):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, targetObject: CodeExpression, fieldName: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def FieldName(self) -> StringType: ...
    
    @FieldName.setter
    def FieldName(self, value: StringType) -> None: ...
    
    @property
    def TargetObject(self) -> CodeExpression: ...
    
    @TargetObject.setter
    def TargetObject(self, value: CodeExpression) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_FieldName(self) -> StringType: ...
    
    def get_TargetObject(self) -> CodeExpression: ...
    
    def set_FieldName(self, value: StringType) -> VoidType: ...
    
    def set_TargetObject(self, value: CodeExpression) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeGotoStatement(CodeStatement):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, label: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Label(self) -> StringType: ...
    
    @Label.setter
    def Label(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Label(self) -> StringType: ...
    
    def set_Label(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeIndexerExpression(CodeExpression):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, targetObject: CodeExpression, indices: ArrayType[CodeExpression]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Indices(self) -> CodeExpressionCollection: ...
    
    @property
    def TargetObject(self) -> CodeExpression: ...
    
    @TargetObject.setter
    def TargetObject(self, value: CodeExpression) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Indices(self) -> CodeExpressionCollection: ...
    
    def get_TargetObject(self) -> CodeExpression: ...
    
    def set_TargetObject(self, value: CodeExpression) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeIterationStatement(CodeStatement):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, initStatement: CodeStatement, testExpression: CodeExpression, incrementStatement: CodeStatement, statements: ArrayType[CodeStatement]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def IncrementStatement(self) -> CodeStatement: ...
    
    @IncrementStatement.setter
    def IncrementStatement(self, value: CodeStatement) -> None: ...
    
    @property
    def InitStatement(self) -> CodeStatement: ...
    
    @InitStatement.setter
    def InitStatement(self, value: CodeStatement) -> None: ...
    
    @property
    def Statements(self) -> CodeStatementCollection: ...
    
    @property
    def TestExpression(self) -> CodeExpression: ...
    
    @TestExpression.setter
    def TestExpression(self, value: CodeExpression) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_IncrementStatement(self) -> CodeStatement: ...
    
    def get_InitStatement(self) -> CodeStatement: ...
    
    def get_Statements(self) -> CodeStatementCollection: ...
    
    def get_TestExpression(self) -> CodeExpression: ...
    
    def set_IncrementStatement(self, value: CodeStatement) -> VoidType: ...
    
    def set_InitStatement(self, value: CodeStatement) -> VoidType: ...
    
    def set_TestExpression(self, value: CodeExpression) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeLabeledStatement(CodeStatement):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, label: StringType): ...
    
    @overload
    def __init__(self, label: StringType, statement: CodeStatement): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Label(self) -> StringType: ...
    
    @Label.setter
    def Label(self, value: StringType) -> None: ...
    
    @property
    def Statement(self) -> CodeStatement: ...
    
    @Statement.setter
    def Statement(self, value: CodeStatement) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Label(self) -> StringType: ...
    
    def get_Statement(self) -> CodeStatement: ...
    
    def set_Label(self, value: StringType) -> VoidType: ...
    
    def set_Statement(self, value: CodeStatement) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeLinePragma(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, fileName: StringType, lineNumber: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def FileName(self) -> StringType: ...
    
    @FileName.setter
    def FileName(self, value: StringType) -> None: ...
    
    @property
    def LineNumber(self) -> IntType: ...
    
    @LineNumber.setter
    def LineNumber(self, value: IntType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_FileName(self) -> StringType: ...
    
    def get_LineNumber(self) -> IntType: ...
    
    def set_FileName(self, value: StringType) -> VoidType: ...
    
    def set_LineNumber(self, value: IntType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeMemberEvent(CodeTypeMember):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ImplementationTypes(self) -> CodeTypeReferenceCollection: ...
    
    @property
    def PrivateImplementationType(self) -> CodeTypeReference: ...
    
    @PrivateImplementationType.setter
    def PrivateImplementationType(self, value: CodeTypeReference) -> None: ...
    
    @property
    def Type(self) -> CodeTypeReference: ...
    
    @Type.setter
    def Type(self, value: CodeTypeReference) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_ImplementationTypes(self) -> CodeTypeReferenceCollection: ...
    
    def get_PrivateImplementationType(self) -> CodeTypeReference: ...
    
    def get_Type(self) -> CodeTypeReference: ...
    
    def set_PrivateImplementationType(self, value: CodeTypeReference) -> VoidType: ...
    
    def set_Type(self, value: CodeTypeReference) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeMemberField(CodeTypeMember):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, type: CodeTypeReference, name: StringType): ...
    
    @overload
    def __init__(self, type: StringType, name: StringType): ...
    
    @overload
    def __init__(self, type: TypeType, name: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def InitExpression(self) -> CodeExpression: ...
    
    @InitExpression.setter
    def InitExpression(self, value: CodeExpression) -> None: ...
    
    @property
    def Type(self) -> CodeTypeReference: ...
    
    @Type.setter
    def Type(self, value: CodeTypeReference) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_InitExpression(self) -> CodeExpression: ...
    
    def get_Type(self) -> CodeTypeReference: ...
    
    def set_InitExpression(self, value: CodeExpression) -> VoidType: ...
    
    def set_Type(self, value: CodeTypeReference) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeMemberMethod(CodeTypeMember):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ImplementationTypes(self) -> CodeTypeReferenceCollection: ...
    
    @property
    def Parameters(self) -> CodeParameterDeclarationExpressionCollection: ...
    
    @property
    def PrivateImplementationType(self) -> CodeTypeReference: ...
    
    @PrivateImplementationType.setter
    def PrivateImplementationType(self, value: CodeTypeReference) -> None: ...
    
    @property
    def ReturnType(self) -> CodeTypeReference: ...
    
    @ReturnType.setter
    def ReturnType(self, value: CodeTypeReference) -> None: ...
    
    @property
    def ReturnTypeCustomAttributes(self) -> CodeAttributeDeclarationCollection: ...
    
    @property
    def Statements(self) -> CodeStatementCollection: ...
    
    @property
    def TypeParameters(self) -> CodeTypeParameterCollection: ...
    
    # ---------- Methods ---------- #
    
    def add_PopulateImplementationTypes(self, value: EventHandler) -> VoidType: ...
    
    def add_PopulateParameters(self, value: EventHandler) -> VoidType: ...
    
    def add_PopulateStatements(self, value: EventHandler) -> VoidType: ...
    
    def get_ImplementationTypes(self) -> CodeTypeReferenceCollection: ...
    
    def get_Parameters(self) -> CodeParameterDeclarationExpressionCollection: ...
    
    def get_PrivateImplementationType(self) -> CodeTypeReference: ...
    
    def get_ReturnType(self) -> CodeTypeReference: ...
    
    def get_ReturnTypeCustomAttributes(self) -> CodeAttributeDeclarationCollection: ...
    
    def get_Statements(self) -> CodeStatementCollection: ...
    
    def get_TypeParameters(self) -> CodeTypeParameterCollection: ...
    
    def remove_PopulateImplementationTypes(self, value: EventHandler) -> VoidType: ...
    
    def remove_PopulateParameters(self, value: EventHandler) -> VoidType: ...
    
    def remove_PopulateStatements(self, value: EventHandler) -> VoidType: ...
    
    def set_PrivateImplementationType(self, value: CodeTypeReference) -> VoidType: ...
    
    def set_ReturnType(self, value: CodeTypeReference) -> VoidType: ...
    
    # ---------- Events ---------- #
    
    PopulateImplementationTypes: EventType[EventHandler] = ...
    
    PopulateParameters: EventType[EventHandler] = ...
    
    PopulateStatements: EventType[EventHandler] = ...
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeMemberProperty(CodeTypeMember):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def GetStatements(self) -> CodeStatementCollection: ...
    
    @property
    def HasGet(self) -> BooleanType: ...
    
    @HasGet.setter
    def HasGet(self, value: BooleanType) -> None: ...
    
    @property
    def HasSet(self) -> BooleanType: ...
    
    @HasSet.setter
    def HasSet(self, value: BooleanType) -> None: ...
    
    @property
    def ImplementationTypes(self) -> CodeTypeReferenceCollection: ...
    
    @property
    def Parameters(self) -> CodeParameterDeclarationExpressionCollection: ...
    
    @property
    def PrivateImplementationType(self) -> CodeTypeReference: ...
    
    @PrivateImplementationType.setter
    def PrivateImplementationType(self, value: CodeTypeReference) -> None: ...
    
    @property
    def SetStatements(self) -> CodeStatementCollection: ...
    
    @property
    def Type(self) -> CodeTypeReference: ...
    
    @Type.setter
    def Type(self, value: CodeTypeReference) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_GetStatements(self) -> CodeStatementCollection: ...
    
    def get_HasGet(self) -> BooleanType: ...
    
    def get_HasSet(self) -> BooleanType: ...
    
    def get_ImplementationTypes(self) -> CodeTypeReferenceCollection: ...
    
    def get_Parameters(self) -> CodeParameterDeclarationExpressionCollection: ...
    
    def get_PrivateImplementationType(self) -> CodeTypeReference: ...
    
    def get_SetStatements(self) -> CodeStatementCollection: ...
    
    def get_Type(self) -> CodeTypeReference: ...
    
    def set_HasGet(self, value: BooleanType) -> VoidType: ...
    
    def set_HasSet(self, value: BooleanType) -> VoidType: ...
    
    def set_PrivateImplementationType(self, value: CodeTypeReference) -> VoidType: ...
    
    def set_Type(self, value: CodeTypeReference) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeMethodInvokeExpression(CodeExpression):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, method: CodeMethodReferenceExpression, parameters: ArrayType[CodeExpression]): ...
    
    @overload
    def __init__(self, targetObject: CodeExpression, methodName: StringType, parameters: ArrayType[CodeExpression]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Method(self) -> CodeMethodReferenceExpression: ...
    
    @Method.setter
    def Method(self, value: CodeMethodReferenceExpression) -> None: ...
    
    @property
    def Parameters(self) -> CodeExpressionCollection: ...
    
    # ---------- Methods ---------- #
    
    def get_Method(self) -> CodeMethodReferenceExpression: ...
    
    def get_Parameters(self) -> CodeExpressionCollection: ...
    
    def set_Method(self, value: CodeMethodReferenceExpression) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeMethodReferenceExpression(CodeExpression):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, targetObject: CodeExpression, methodName: StringType): ...
    
    @overload
    def __init__(self, targetObject: CodeExpression, methodName: StringType, typeParameters: ArrayType[CodeTypeReference]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def MethodName(self) -> StringType: ...
    
    @MethodName.setter
    def MethodName(self, value: StringType) -> None: ...
    
    @property
    def TargetObject(self) -> CodeExpression: ...
    
    @TargetObject.setter
    def TargetObject(self, value: CodeExpression) -> None: ...
    
    @property
    def TypeArguments(self) -> CodeTypeReferenceCollection: ...
    
    # ---------- Methods ---------- #
    
    def get_MethodName(self) -> StringType: ...
    
    def get_TargetObject(self) -> CodeExpression: ...
    
    def get_TypeArguments(self) -> CodeTypeReferenceCollection: ...
    
    def set_MethodName(self, value: StringType) -> VoidType: ...
    
    def set_TargetObject(self, value: CodeExpression) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeMethodReturnStatement(CodeStatement):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, expression: CodeExpression): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Expression(self) -> CodeExpression: ...
    
    @Expression.setter
    def Expression(self, value: CodeExpression) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Expression(self) -> CodeExpression: ...
    
    def set_Expression(self, value: CodeExpression) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeNamespace(CodeObject):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, name: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Comments(self) -> CodeCommentStatementCollection: ...
    
    @property
    def Imports(self) -> CodeNamespaceImportCollection: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @Name.setter
    def Name(self, value: StringType) -> None: ...
    
    @property
    def Types(self) -> CodeTypeDeclarationCollection: ...
    
    # ---------- Methods ---------- #
    
    def add_PopulateComments(self, value: EventHandler) -> VoidType: ...
    
    def add_PopulateImports(self, value: EventHandler) -> VoidType: ...
    
    def add_PopulateTypes(self, value: EventHandler) -> VoidType: ...
    
    def get_Comments(self) -> CodeCommentStatementCollection: ...
    
    def get_Imports(self) -> CodeNamespaceImportCollection: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_Types(self) -> CodeTypeDeclarationCollection: ...
    
    def remove_PopulateComments(self, value: EventHandler) -> VoidType: ...
    
    def remove_PopulateImports(self, value: EventHandler) -> VoidType: ...
    
    def remove_PopulateTypes(self, value: EventHandler) -> VoidType: ...
    
    def set_Name(self, value: StringType) -> VoidType: ...
    
    # ---------- Events ---------- #
    
    PopulateComments: EventType[EventHandler] = ...
    
    PopulateImports: EventType[EventHandler] = ...
    
    PopulateTypes: EventType[EventHandler] = ...
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeNamespaceCollection(CollectionBase, IList, ICollection, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: CodeNamespaceCollection): ...
    
    @overload
    def __init__(self, value: ArrayType[CodeNamespace]): ...
    
    # ---------- Properties ---------- #
    
    def __getitem__(self, key: IntType) -> CodeNamespace: ...
    
    def __setitem__(self, key: IntType, value: CodeNamespace) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Add(self, value: CodeNamespace) -> IntType: ...
    
    @overload
    def AddRange(self, value: ArrayType[CodeNamespace]) -> VoidType: ...
    
    @overload
    def AddRange(self, value: CodeNamespaceCollection) -> VoidType: ...
    
    def Contains(self, value: CodeNamespace) -> BooleanType: ...
    
    def CopyTo(self, array: ArrayType[CodeNamespace], index: IntType) -> VoidType: ...
    
    def IndexOf(self, value: CodeNamespace) -> IntType: ...
    
    def Insert(self, index: IntType, value: CodeNamespace) -> VoidType: ...
    
    def Remove(self, value: CodeNamespace) -> VoidType: ...
    
    def get_Item(self, index: IntType) -> CodeNamespace: ...
    
    def set_Item(self, index: IntType, value: CodeNamespace) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeNamespaceImport(CodeObject):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, nameSpace: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def LinePragma(self) -> CodeLinePragma: ...
    
    @LinePragma.setter
    def LinePragma(self, value: CodeLinePragma) -> None: ...
    
    @property
    def Namespace(self) -> StringType: ...
    
    @Namespace.setter
    def Namespace(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_LinePragma(self) -> CodeLinePragma: ...
    
    def get_Namespace(self) -> StringType: ...
    
    def set_LinePragma(self, value: CodeLinePragma) -> VoidType: ...
    
    def set_Namespace(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeNamespaceImportCollection(ObjectType, IList, ICollection, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    def __getitem__(self, key: IntType) -> CodeNamespaceImport: ...
    
    def __setitem__(self, key: IntType, value: CodeNamespaceImport) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Add(self, value: CodeNamespaceImport) -> VoidType: ...
    
    def AddRange(self, value: ArrayType[CodeNamespaceImport]) -> VoidType: ...
    
    def Clear(self) -> VoidType: ...
    
    def GetEnumerator(self) -> IEnumerator: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_Item(self, index: IntType) -> CodeNamespaceImport: ...
    
    def set_Item(self, index: IntType, value: CodeNamespaceImport) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeObject(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def UserData(self) -> IDictionary: ...
    
    # ---------- Methods ---------- #
    
    def get_UserData(self) -> IDictionary: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeObjectCreateExpression(CodeExpression):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, createType: CodeTypeReference, parameters: ArrayType[CodeExpression]): ...
    
    @overload
    def __init__(self, createType: StringType, parameters: ArrayType[CodeExpression]): ...
    
    @overload
    def __init__(self, createType: TypeType, parameters: ArrayType[CodeExpression]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CreateType(self) -> CodeTypeReference: ...
    
    @CreateType.setter
    def CreateType(self, value: CodeTypeReference) -> None: ...
    
    @property
    def Parameters(self) -> CodeExpressionCollection: ...
    
    # ---------- Methods ---------- #
    
    def get_CreateType(self) -> CodeTypeReference: ...
    
    def get_Parameters(self) -> CodeExpressionCollection: ...
    
    def set_CreateType(self, value: CodeTypeReference) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeParameterDeclarationExpression(CodeExpression):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, type: CodeTypeReference, name: StringType): ...
    
    @overload
    def __init__(self, type: StringType, name: StringType): ...
    
    @overload
    def __init__(self, type: TypeType, name: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CustomAttributes(self) -> CodeAttributeDeclarationCollection: ...
    
    @CustomAttributes.setter
    def CustomAttributes(self, value: CodeAttributeDeclarationCollection) -> None: ...
    
    @property
    def Direction(self) -> FieldDirection: ...
    
    @Direction.setter
    def Direction(self, value: FieldDirection) -> None: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @Name.setter
    def Name(self, value: StringType) -> None: ...
    
    @property
    def Type(self) -> CodeTypeReference: ...
    
    @Type.setter
    def Type(self, value: CodeTypeReference) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_CustomAttributes(self) -> CodeAttributeDeclarationCollection: ...
    
    def get_Direction(self) -> FieldDirection: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_Type(self) -> CodeTypeReference: ...
    
    def set_CustomAttributes(self, value: CodeAttributeDeclarationCollection) -> VoidType: ...
    
    def set_Direction(self, value: FieldDirection) -> VoidType: ...
    
    def set_Name(self, value: StringType) -> VoidType: ...
    
    def set_Type(self, value: CodeTypeReference) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeParameterDeclarationExpressionCollection(CollectionBase, IList, ICollection, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: CodeParameterDeclarationExpressionCollection): ...
    
    @overload
    def __init__(self, value: ArrayType[CodeParameterDeclarationExpression]): ...
    
    # ---------- Properties ---------- #
    
    def __getitem__(self, key: IntType) -> CodeParameterDeclarationExpression: ...
    
    def __setitem__(self, key: IntType, value: CodeParameterDeclarationExpression) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Add(self, value: CodeParameterDeclarationExpression) -> IntType: ...
    
    @overload
    def AddRange(self, value: ArrayType[CodeParameterDeclarationExpression]) -> VoidType: ...
    
    @overload
    def AddRange(self, value: CodeParameterDeclarationExpressionCollection) -> VoidType: ...
    
    def Contains(self, value: CodeParameterDeclarationExpression) -> BooleanType: ...
    
    def CopyTo(self, array: ArrayType[CodeParameterDeclarationExpression], index: IntType) -> VoidType: ...
    
    def IndexOf(self, value: CodeParameterDeclarationExpression) -> IntType: ...
    
    def Insert(self, index: IntType, value: CodeParameterDeclarationExpression) -> VoidType: ...
    
    def Remove(self, value: CodeParameterDeclarationExpression) -> VoidType: ...
    
    def get_Item(self, index: IntType) -> CodeParameterDeclarationExpression: ...
    
    def set_Item(self, index: IntType, value: CodeParameterDeclarationExpression) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodePrimitiveExpression(CodeExpression):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: ObjectType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> ObjectType: ...
    
    @Value.setter
    def Value(self, value: ObjectType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Value(self) -> ObjectType: ...
    
    def set_Value(self, value: ObjectType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodePropertyReferenceExpression(CodeExpression):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, targetObject: CodeExpression, propertyName: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def PropertyName(self) -> StringType: ...
    
    @PropertyName.setter
    def PropertyName(self, value: StringType) -> None: ...
    
    @property
    def TargetObject(self) -> CodeExpression: ...
    
    @TargetObject.setter
    def TargetObject(self, value: CodeExpression) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_PropertyName(self) -> StringType: ...
    
    def get_TargetObject(self) -> CodeExpression: ...
    
    def set_PropertyName(self, value: StringType) -> VoidType: ...
    
    def set_TargetObject(self, value: CodeExpression) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodePropertySetValueReferenceExpression(CodeExpression):
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


class CodeRegionDirective(CodeDirective):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, regionMode: CodeRegionMode, regionText: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def RegionMode(self) -> CodeRegionMode: ...
    
    @RegionMode.setter
    def RegionMode(self, value: CodeRegionMode) -> None: ...
    
    @property
    def RegionText(self) -> StringType: ...
    
    @RegionText.setter
    def RegionText(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_RegionMode(self) -> CodeRegionMode: ...
    
    def get_RegionText(self) -> StringType: ...
    
    def set_RegionMode(self, value: CodeRegionMode) -> VoidType: ...
    
    def set_RegionText(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeRemoveEventStatement(CodeStatement):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, eventRef: CodeEventReferenceExpression, listener: CodeExpression): ...
    
    @overload
    def __init__(self, targetObject: CodeExpression, eventName: StringType, listener: CodeExpression): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Event(self) -> CodeEventReferenceExpression: ...
    
    @Event.setter
    def Event(self, value: CodeEventReferenceExpression) -> None: ...
    
    @property
    def Listener(self) -> CodeExpression: ...
    
    @Listener.setter
    def Listener(self, value: CodeExpression) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Event(self) -> CodeEventReferenceExpression: ...
    
    def get_Listener(self) -> CodeExpression: ...
    
    def set_Event(self, value: CodeEventReferenceExpression) -> VoidType: ...
    
    def set_Listener(self, value: CodeExpression) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeSnippetCompileUnit(CodeCompileUnit):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def LinePragma(self) -> CodeLinePragma: ...
    
    @LinePragma.setter
    def LinePragma(self, value: CodeLinePragma) -> None: ...
    
    @property
    def Value(self) -> StringType: ...
    
    @Value.setter
    def Value(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_LinePragma(self) -> CodeLinePragma: ...
    
    def get_Value(self) -> StringType: ...
    
    def set_LinePragma(self, value: CodeLinePragma) -> VoidType: ...
    
    def set_Value(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeSnippetExpression(CodeExpression):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> StringType: ...
    
    @Value.setter
    def Value(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Value(self) -> StringType: ...
    
    def set_Value(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeSnippetStatement(CodeStatement):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> StringType: ...
    
    @Value.setter
    def Value(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Value(self) -> StringType: ...
    
    def set_Value(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeSnippetTypeMember(CodeTypeMember):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, text: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Text(self) -> StringType: ...
    
    @Text.setter
    def Text(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Text(self) -> StringType: ...
    
    def set_Text(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeStatement(CodeObject):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def EndDirectives(self) -> CodeDirectiveCollection: ...
    
    @property
    def LinePragma(self) -> CodeLinePragma: ...
    
    @LinePragma.setter
    def LinePragma(self, value: CodeLinePragma) -> None: ...
    
    @property
    def StartDirectives(self) -> CodeDirectiveCollection: ...
    
    # ---------- Methods ---------- #
    
    def get_EndDirectives(self) -> CodeDirectiveCollection: ...
    
    def get_LinePragma(self) -> CodeLinePragma: ...
    
    def get_StartDirectives(self) -> CodeDirectiveCollection: ...
    
    def set_LinePragma(self, value: CodeLinePragma) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeStatementCollection(CollectionBase, IList, ICollection, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: CodeStatementCollection): ...
    
    @overload
    def __init__(self, value: ArrayType[CodeStatement]): ...
    
    # ---------- Properties ---------- #
    
    def __getitem__(self, key: IntType) -> CodeStatement: ...
    
    def __setitem__(self, key: IntType, value: CodeStatement) -> None: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Add(self, value: CodeStatement) -> IntType: ...
    
    @overload
    def Add(self, value: CodeExpression) -> IntType: ...
    
    @overload
    def AddRange(self, value: ArrayType[CodeStatement]) -> VoidType: ...
    
    @overload
    def AddRange(self, value: CodeStatementCollection) -> VoidType: ...
    
    def Contains(self, value: CodeStatement) -> BooleanType: ...
    
    def CopyTo(self, array: ArrayType[CodeStatement], index: IntType) -> VoidType: ...
    
    def IndexOf(self, value: CodeStatement) -> IntType: ...
    
    def Insert(self, index: IntType, value: CodeStatement) -> VoidType: ...
    
    def Remove(self, value: CodeStatement) -> VoidType: ...
    
    def get_Item(self, index: IntType) -> CodeStatement: ...
    
    def set_Item(self, index: IntType, value: CodeStatement) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeThisReferenceExpression(CodeExpression):
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


class CodeThrowExceptionStatement(CodeStatement):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, toThrow: CodeExpression): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ToThrow(self) -> CodeExpression: ...
    
    @ToThrow.setter
    def ToThrow(self, value: CodeExpression) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_ToThrow(self) -> CodeExpression: ...
    
    def set_ToThrow(self, value: CodeExpression) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeTryCatchFinallyStatement(CodeStatement):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, tryStatements: ArrayType[CodeStatement], catchClauses: ArrayType[CodeCatchClause]): ...
    
    @overload
    def __init__(self, tryStatements: ArrayType[CodeStatement], catchClauses: ArrayType[CodeCatchClause], finallyStatements: ArrayType[CodeStatement]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CatchClauses(self) -> CodeCatchClauseCollection: ...
    
    @property
    def FinallyStatements(self) -> CodeStatementCollection: ...
    
    @property
    def TryStatements(self) -> CodeStatementCollection: ...
    
    # ---------- Methods ---------- #
    
    def get_CatchClauses(self) -> CodeCatchClauseCollection: ...
    
    def get_FinallyStatements(self) -> CodeStatementCollection: ...
    
    def get_TryStatements(self) -> CodeStatementCollection: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeTypeConstructor(CodeMemberMethod):
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


class CodeTypeDeclaration(CodeTypeMember):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, name: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def BaseTypes(self) -> CodeTypeReferenceCollection: ...
    
    @property
    def IsClass(self) -> BooleanType: ...
    
    @IsClass.setter
    def IsClass(self, value: BooleanType) -> None: ...
    
    @property
    def IsEnum(self) -> BooleanType: ...
    
    @IsEnum.setter
    def IsEnum(self, value: BooleanType) -> None: ...
    
    @property
    def IsInterface(self) -> BooleanType: ...
    
    @IsInterface.setter
    def IsInterface(self, value: BooleanType) -> None: ...
    
    @property
    def IsPartial(self) -> BooleanType: ...
    
    @IsPartial.setter
    def IsPartial(self, value: BooleanType) -> None: ...
    
    @property
    def IsStruct(self) -> BooleanType: ...
    
    @IsStruct.setter
    def IsStruct(self, value: BooleanType) -> None: ...
    
    @property
    def Members(self) -> CodeTypeMemberCollection: ...
    
    @property
    def TypeAttributes(self) -> TypeAttributes: ...
    
    @TypeAttributes.setter
    def TypeAttributes(self, value: TypeAttributes) -> None: ...
    
    @property
    def TypeParameters(self) -> CodeTypeParameterCollection: ...
    
    # ---------- Methods ---------- #
    
    def add_PopulateBaseTypes(self, value: EventHandler) -> VoidType: ...
    
    def add_PopulateMembers(self, value: EventHandler) -> VoidType: ...
    
    def get_BaseTypes(self) -> CodeTypeReferenceCollection: ...
    
    def get_IsClass(self) -> BooleanType: ...
    
    def get_IsEnum(self) -> BooleanType: ...
    
    def get_IsInterface(self) -> BooleanType: ...
    
    def get_IsPartial(self) -> BooleanType: ...
    
    def get_IsStruct(self) -> BooleanType: ...
    
    def get_Members(self) -> CodeTypeMemberCollection: ...
    
    def get_TypeAttributes(self) -> TypeAttributes: ...
    
    def get_TypeParameters(self) -> CodeTypeParameterCollection: ...
    
    def remove_PopulateBaseTypes(self, value: EventHandler) -> VoidType: ...
    
    def remove_PopulateMembers(self, value: EventHandler) -> VoidType: ...
    
    def set_IsClass(self, value: BooleanType) -> VoidType: ...
    
    def set_IsEnum(self, value: BooleanType) -> VoidType: ...
    
    def set_IsInterface(self, value: BooleanType) -> VoidType: ...
    
    def set_IsPartial(self, value: BooleanType) -> VoidType: ...
    
    def set_IsStruct(self, value: BooleanType) -> VoidType: ...
    
    def set_TypeAttributes(self, value: TypeAttributes) -> VoidType: ...
    
    # ---------- Events ---------- #
    
    PopulateBaseTypes: EventType[EventHandler] = ...
    
    PopulateMembers: EventType[EventHandler] = ...
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeTypeDeclarationCollection(CollectionBase, IList, ICollection, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: CodeTypeDeclarationCollection): ...
    
    @overload
    def __init__(self, value: ArrayType[CodeTypeDeclaration]): ...
    
    # ---------- Properties ---------- #
    
    def __getitem__(self, key: IntType) -> CodeTypeDeclaration: ...
    
    def __setitem__(self, key: IntType, value: CodeTypeDeclaration) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Add(self, value: CodeTypeDeclaration) -> IntType: ...
    
    @overload
    def AddRange(self, value: ArrayType[CodeTypeDeclaration]) -> VoidType: ...
    
    @overload
    def AddRange(self, value: CodeTypeDeclarationCollection) -> VoidType: ...
    
    def Contains(self, value: CodeTypeDeclaration) -> BooleanType: ...
    
    def CopyTo(self, array: ArrayType[CodeTypeDeclaration], index: IntType) -> VoidType: ...
    
    def IndexOf(self, value: CodeTypeDeclaration) -> IntType: ...
    
    def Insert(self, index: IntType, value: CodeTypeDeclaration) -> VoidType: ...
    
    def Remove(self, value: CodeTypeDeclaration) -> VoidType: ...
    
    def get_Item(self, index: IntType) -> CodeTypeDeclaration: ...
    
    def set_Item(self, index: IntType, value: CodeTypeDeclaration) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeTypeDelegate(CodeTypeDeclaration):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, name: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Parameters(self) -> CodeParameterDeclarationExpressionCollection: ...
    
    @property
    def ReturnType(self) -> CodeTypeReference: ...
    
    @ReturnType.setter
    def ReturnType(self, value: CodeTypeReference) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Parameters(self) -> CodeParameterDeclarationExpressionCollection: ...
    
    def get_ReturnType(self) -> CodeTypeReference: ...
    
    def set_ReturnType(self, value: CodeTypeReference) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeTypeMember(CodeObject):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Attributes(self) -> MemberAttributes: ...
    
    @Attributes.setter
    def Attributes(self, value: MemberAttributes) -> None: ...
    
    @property
    def Comments(self) -> CodeCommentStatementCollection: ...
    
    @property
    def CustomAttributes(self) -> CodeAttributeDeclarationCollection: ...
    
    @CustomAttributes.setter
    def CustomAttributes(self, value: CodeAttributeDeclarationCollection) -> None: ...
    
    @property
    def EndDirectives(self) -> CodeDirectiveCollection: ...
    
    @property
    def LinePragma(self) -> CodeLinePragma: ...
    
    @LinePragma.setter
    def LinePragma(self, value: CodeLinePragma) -> None: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @Name.setter
    def Name(self, value: StringType) -> None: ...
    
    @property
    def StartDirectives(self) -> CodeDirectiveCollection: ...
    
    # ---------- Methods ---------- #
    
    def get_Attributes(self) -> MemberAttributes: ...
    
    def get_Comments(self) -> CodeCommentStatementCollection: ...
    
    def get_CustomAttributes(self) -> CodeAttributeDeclarationCollection: ...
    
    def get_EndDirectives(self) -> CodeDirectiveCollection: ...
    
    def get_LinePragma(self) -> CodeLinePragma: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_StartDirectives(self) -> CodeDirectiveCollection: ...
    
    def set_Attributes(self, value: MemberAttributes) -> VoidType: ...
    
    def set_CustomAttributes(self, value: CodeAttributeDeclarationCollection) -> VoidType: ...
    
    def set_LinePragma(self, value: CodeLinePragma) -> VoidType: ...
    
    def set_Name(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeTypeMemberCollection(CollectionBase, IList, ICollection, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: CodeTypeMemberCollection): ...
    
    @overload
    def __init__(self, value: ArrayType[CodeTypeMember]): ...
    
    # ---------- Properties ---------- #
    
    def __getitem__(self, key: IntType) -> CodeTypeMember: ...
    
    def __setitem__(self, key: IntType, value: CodeTypeMember) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Add(self, value: CodeTypeMember) -> IntType: ...
    
    @overload
    def AddRange(self, value: ArrayType[CodeTypeMember]) -> VoidType: ...
    
    @overload
    def AddRange(self, value: CodeTypeMemberCollection) -> VoidType: ...
    
    def Contains(self, value: CodeTypeMember) -> BooleanType: ...
    
    def CopyTo(self, array: ArrayType[CodeTypeMember], index: IntType) -> VoidType: ...
    
    def IndexOf(self, value: CodeTypeMember) -> IntType: ...
    
    def Insert(self, index: IntType, value: CodeTypeMember) -> VoidType: ...
    
    def Remove(self, value: CodeTypeMember) -> VoidType: ...
    
    def get_Item(self, index: IntType) -> CodeTypeMember: ...
    
    def set_Item(self, index: IntType, value: CodeTypeMember) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeTypeOfExpression(CodeExpression):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, type: CodeTypeReference): ...
    
    @overload
    def __init__(self, type: StringType): ...
    
    @overload
    def __init__(self, type: TypeType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Type(self) -> CodeTypeReference: ...
    
    @Type.setter
    def Type(self, value: CodeTypeReference) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Type(self) -> CodeTypeReference: ...
    
    def set_Type(self, value: CodeTypeReference) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeTypeParameter(CodeObject):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, name: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Constraints(self) -> CodeTypeReferenceCollection: ...
    
    @property
    def CustomAttributes(self) -> CodeAttributeDeclarationCollection: ...
    
    @property
    def HasConstructorConstraint(self) -> BooleanType: ...
    
    @HasConstructorConstraint.setter
    def HasConstructorConstraint(self, value: BooleanType) -> None: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @Name.setter
    def Name(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Constraints(self) -> CodeTypeReferenceCollection: ...
    
    def get_CustomAttributes(self) -> CodeAttributeDeclarationCollection: ...
    
    def get_HasConstructorConstraint(self) -> BooleanType: ...
    
    def get_Name(self) -> StringType: ...
    
    def set_HasConstructorConstraint(self, value: BooleanType) -> VoidType: ...
    
    def set_Name(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeTypeParameterCollection(CollectionBase, IList, ICollection, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: CodeTypeParameterCollection): ...
    
    @overload
    def __init__(self, value: ArrayType[CodeTypeParameter]): ...
    
    # ---------- Properties ---------- #
    
    def __getitem__(self, key: IntType) -> CodeTypeParameter: ...
    
    def __setitem__(self, key: IntType, value: CodeTypeParameter) -> None: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Add(self, value: CodeTypeParameter) -> IntType: ...
    
    @overload
    def Add(self, value: StringType) -> VoidType: ...
    
    @overload
    def AddRange(self, value: ArrayType[CodeTypeParameter]) -> VoidType: ...
    
    @overload
    def AddRange(self, value: CodeTypeParameterCollection) -> VoidType: ...
    
    def Contains(self, value: CodeTypeParameter) -> BooleanType: ...
    
    def CopyTo(self, array: ArrayType[CodeTypeParameter], index: IntType) -> VoidType: ...
    
    def IndexOf(self, value: CodeTypeParameter) -> IntType: ...
    
    def Insert(self, index: IntType, value: CodeTypeParameter) -> VoidType: ...
    
    def Remove(self, value: CodeTypeParameter) -> VoidType: ...
    
    def get_Item(self, index: IntType) -> CodeTypeParameter: ...
    
    def set_Item(self, index: IntType, value: CodeTypeParameter) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeTypeReference(CodeObject):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, type: TypeType): ...
    
    @overload
    def __init__(self, type: TypeType, codeTypeReferenceOption: CodeTypeReferenceOptions): ...
    
    @overload
    def __init__(self, typeName: StringType, codeTypeReferenceOption: CodeTypeReferenceOptions): ...
    
    @overload
    def __init__(self, typeName: StringType): ...
    
    @overload
    def __init__(self, typeName: StringType, typeArguments: ArrayType[CodeTypeReference]): ...
    
    @overload
    def __init__(self, typeParameter: CodeTypeParameter): ...
    
    @overload
    def __init__(self, baseType: StringType, rank: IntType): ...
    
    @overload
    def __init__(self, arrayType: CodeTypeReference, rank: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ArrayElementType(self) -> CodeTypeReference: ...
    
    @ArrayElementType.setter
    def ArrayElementType(self, value: CodeTypeReference) -> None: ...
    
    @property
    def ArrayRank(self) -> IntType: ...
    
    @ArrayRank.setter
    def ArrayRank(self, value: IntType) -> None: ...
    
    @property
    def BaseType(self) -> StringType: ...
    
    @BaseType.setter
    def BaseType(self, value: StringType) -> None: ...
    
    @property
    def Options(self) -> CodeTypeReferenceOptions: ...
    
    @Options.setter
    def Options(self, value: CodeTypeReferenceOptions) -> None: ...
    
    @property
    def TypeArguments(self) -> CodeTypeReferenceCollection: ...
    
    # ---------- Methods ---------- #
    
    def get_ArrayElementType(self) -> CodeTypeReference: ...
    
    def get_ArrayRank(self) -> IntType: ...
    
    def get_BaseType(self) -> StringType: ...
    
    def get_Options(self) -> CodeTypeReferenceOptions: ...
    
    def get_TypeArguments(self) -> CodeTypeReferenceCollection: ...
    
    def set_ArrayElementType(self, value: CodeTypeReference) -> VoidType: ...
    
    def set_ArrayRank(self, value: IntType) -> VoidType: ...
    
    def set_BaseType(self, value: StringType) -> VoidType: ...
    
    def set_Options(self, value: CodeTypeReferenceOptions) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeTypeReferenceCollection(CollectionBase, IList, ICollection, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: CodeTypeReferenceCollection): ...
    
    @overload
    def __init__(self, value: ArrayType[CodeTypeReference]): ...
    
    # ---------- Properties ---------- #
    
    def __getitem__(self, key: IntType) -> CodeTypeReference: ...
    
    def __setitem__(self, key: IntType, value: CodeTypeReference) -> None: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Add(self, value: CodeTypeReference) -> IntType: ...
    
    @overload
    def Add(self, value: StringType) -> VoidType: ...
    
    @overload
    def Add(self, value: TypeType) -> VoidType: ...
    
    @overload
    def AddRange(self, value: ArrayType[CodeTypeReference]) -> VoidType: ...
    
    @overload
    def AddRange(self, value: CodeTypeReferenceCollection) -> VoidType: ...
    
    def Contains(self, value: CodeTypeReference) -> BooleanType: ...
    
    def CopyTo(self, array: ArrayType[CodeTypeReference], index: IntType) -> VoidType: ...
    
    def IndexOf(self, value: CodeTypeReference) -> IntType: ...
    
    def Insert(self, index: IntType, value: CodeTypeReference) -> VoidType: ...
    
    def Remove(self, value: CodeTypeReference) -> VoidType: ...
    
    def get_Item(self, index: IntType) -> CodeTypeReference: ...
    
    def set_Item(self, index: IntType, value: CodeTypeReference) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeTypeReferenceExpression(CodeExpression):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, type: CodeTypeReference): ...
    
    @overload
    def __init__(self, type: StringType): ...
    
    @overload
    def __init__(self, type: TypeType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Type(self) -> CodeTypeReference: ...
    
    @Type.setter
    def Type(self, value: CodeTypeReference) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Type(self) -> CodeTypeReference: ...
    
    def set_Type(self, value: CodeTypeReference) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeVariableDeclarationStatement(CodeStatement):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, type: CodeTypeReference, name: StringType): ...
    
    @overload
    def __init__(self, type: StringType, name: StringType): ...
    
    @overload
    def __init__(self, type: TypeType, name: StringType): ...
    
    @overload
    def __init__(self, type: CodeTypeReference, name: StringType, initExpression: CodeExpression): ...
    
    @overload
    def __init__(self, type: StringType, name: StringType, initExpression: CodeExpression): ...
    
    @overload
    def __init__(self, type: TypeType, name: StringType, initExpression: CodeExpression): ...
    
    # ---------- Properties ---------- #
    
    @property
    def InitExpression(self) -> CodeExpression: ...
    
    @InitExpression.setter
    def InitExpression(self, value: CodeExpression) -> None: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @Name.setter
    def Name(self, value: StringType) -> None: ...
    
    @property
    def Type(self) -> CodeTypeReference: ...
    
    @Type.setter
    def Type(self, value: CodeTypeReference) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_InitExpression(self) -> CodeExpression: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_Type(self) -> CodeTypeReference: ...
    
    def set_InitExpression(self, value: CodeExpression) -> VoidType: ...
    
    def set_Name(self, value: StringType) -> VoidType: ...
    
    def set_Type(self, value: CodeTypeReference) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeVariableReferenceExpression(CodeExpression):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, variableName: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def VariableName(self) -> StringType: ...
    
    @VariableName.setter
    def VariableName(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_VariableName(self) -> StringType: ...
    
    def set_VariableName(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# No Structs

# No Interfaces

# ---------- Enums ---------- #

class CodeBinaryOperatorType(Enum):
    Add: IntType = 0
    Subtract: IntType = 1
    Multiply: IntType = 2
    Divide: IntType = 3
    Modulus: IntType = 4
    Assign: IntType = 5
    IdentityInequality: IntType = 6
    IdentityEquality: IntType = 7
    ValueEquality: IntType = 8
    BitwiseOr: IntType = 9
    BitwiseAnd: IntType = 10
    BooleanOr: IntType = 11
    BooleanAnd: IntType = 12
    LessThan: IntType = 13
    LessThanOrEqual: IntType = 14
    GreaterThan: IntType = 15
    GreaterThanOrEqual: IntType = 16


class CodeRegionMode(Enum):
    #None: IntType = 0
    Start: IntType = 1
    End: IntType = 2


class CodeTypeReferenceOptions(Enum):
    GlobalReference: IntType = 1
    GenericTypeParameter: IntType = 2


class FieldDirection(Enum):
    In: IntType = 0
    Out: IntType = 1
    Ref: IntType = 2


class MemberAttributes(Enum):
    Abstract: IntType = 1
    Final: IntType = 2
    Static: IntType = 3
    Override: IntType = 4
    Const: IntType = 5
    ScopeMask: IntType = 15
    New: IntType = 16
    VTableMask: IntType = 240
    Overloaded: IntType = 256
    Assembly: IntType = 4096
    FamilyAndAssembly: IntType = 8192
    Family: IntType = 12288
    FamilyOrAssembly: IntType = 16384
    Private: IntType = 20480
    Public: IntType = 24576
    AccessMask: IntType = 61440


# No Delegates

__all__ = [
    CodeArgumentReferenceExpression,
    CodeArrayCreateExpression,
    CodeArrayIndexerExpression,
    CodeAssignStatement,
    CodeAttachEventStatement,
    CodeAttributeArgument,
    CodeAttributeArgumentCollection,
    CodeAttributeDeclaration,
    CodeAttributeDeclarationCollection,
    CodeBaseReferenceExpression,
    CodeBinaryOperatorExpression,
    CodeCastExpression,
    CodeCatchClause,
    CodeCatchClauseCollection,
    CodeChecksumPragma,
    CodeComment,
    CodeCommentStatement,
    CodeCommentStatementCollection,
    CodeCompileUnit,
    CodeConditionStatement,
    CodeConstructor,
    CodeDefaultValueExpression,
    CodeDelegateCreateExpression,
    CodeDelegateInvokeExpression,
    CodeDirectionExpression,
    CodeDirective,
    CodeDirectiveCollection,
    CodeEntryPointMethod,
    CodeEventReferenceExpression,
    CodeExpression,
    CodeExpressionCollection,
    CodeExpressionStatement,
    CodeFieldReferenceExpression,
    CodeGotoStatement,
    CodeIndexerExpression,
    CodeIterationStatement,
    CodeLabeledStatement,
    CodeLinePragma,
    CodeMemberEvent,
    CodeMemberField,
    CodeMemberMethod,
    CodeMemberProperty,
    CodeMethodInvokeExpression,
    CodeMethodReferenceExpression,
    CodeMethodReturnStatement,
    CodeNamespace,
    CodeNamespaceCollection,
    CodeNamespaceImport,
    CodeNamespaceImportCollection,
    CodeObject,
    CodeObjectCreateExpression,
    CodeParameterDeclarationExpression,
    CodeParameterDeclarationExpressionCollection,
    CodePrimitiveExpression,
    CodePropertyReferenceExpression,
    CodePropertySetValueReferenceExpression,
    CodeRegionDirective,
    CodeRemoveEventStatement,
    CodeSnippetCompileUnit,
    CodeSnippetExpression,
    CodeSnippetStatement,
    CodeSnippetTypeMember,
    CodeStatement,
    CodeStatementCollection,
    CodeThisReferenceExpression,
    CodeThrowExceptionStatement,
    CodeTryCatchFinallyStatement,
    CodeTypeConstructor,
    CodeTypeDeclaration,
    CodeTypeDeclarationCollection,
    CodeTypeDelegate,
    CodeTypeMember,
    CodeTypeMemberCollection,
    CodeTypeOfExpression,
    CodeTypeParameter,
    CodeTypeParameterCollection,
    CodeTypeReference,
    CodeTypeReferenceCollection,
    CodeTypeReferenceExpression,
    CodeVariableDeclarationStatement,
    CodeVariableReferenceExpression,
    CodeBinaryOperatorType,
    CodeRegionMode,
    CodeTypeReferenceOptions,
    FieldDirection,
    MemberAttributes,
]
