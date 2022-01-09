from __future__ import annotations

from abc import ABC
from typing import Callable, List, Union, overload

from System import Array, AsyncCallback, Boolean, Enum, Exception, IAsyncResult, ICloneable, Int32, IntPtr, MulticastDelegate, Object, String, TimeSpan, TimeoutException, Void
from System.Collections import ICollection, IEnumerable, IEnumerator
from System.Reflection import AssemblyName
from System.Reflection.Emit import CustomAttributeBuilder
from System.Runtime.InteropServices import _Exception
from System.Runtime.Serialization import ISerializable

# ---------- Types ---------- #

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
IntType = Union[int, Int32]
NIntType = Union[int, IntPtr]
ObjectType = Object
StringType = Union[str, String]
VoidType = Union[None, Void]

# ---------- Classes ---------- #

class CachedCodeEntry(ObjectType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Capture(ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Index(self) -> IntType: ...
    
    @property
    def Length(self) -> IntType: ...
    
    @property
    def Value(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def ToString(self) -> StringType: ...
    
    def get_Index(self) -> IntType: ...
    
    def get_Length(self) -> IntType: ...
    
    def get_Value(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CaptureCollection(ObjectType, ICollection, IEnumerable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def IsReadOnly(self) -> BooleanType: ...
    
    @property
    def IsSynchronized(self) -> BooleanType: ...
    
    @property
    def Item(self) -> Capture: ...
    
    @property
    def SyncRoot(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def CopyTo(self, array: Array, arrayIndex: IntType) -> VoidType: ...
    
    def GetEnumerator(self) -> IEnumerator: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_IsReadOnly(self) -> BooleanType: ...
    
    def get_IsSynchronized(self) -> BooleanType: ...
    
    def get_Item(self, i: IntType) -> Capture: ...
    
    def get_SyncRoot(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CaptureEnumerator(ObjectType, IEnumerator):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Capture(self) -> Capture: ...
    
    @property
    def Current(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def MoveNext(self) -> BooleanType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Capture(self) -> Capture: ...
    
    def get_Current(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CompiledRegexRunner(RegexRunner):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CompiledRegexRunnerFactory(RegexRunnerFactory):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CreateInstanceDelegate(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> RegexRunner: ...
    
    def Invoke(self) -> RegexRunner: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ExclusiveReference(ObjectType):
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


class FindFirstCharDelegate(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, r: RegexRunner, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> BooleanType: ...
    
    def Invoke(self, r: RegexRunner) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Group(Capture):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Captures(self) -> CaptureCollection: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def Success(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def Synchronized(inner: Group) -> Group: ...
    
    def get_Captures(self) -> CaptureCollection: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_Success(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class GroupCollection(ObjectType, ICollection, IEnumerable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def IsReadOnly(self) -> BooleanType: ...
    
    @property
    def IsSynchronized(self) -> BooleanType: ...
    
    @property
    def Item(self) -> Group: ...
    
    @property
    def Item(self) -> Group: ...
    
    @property
    def SyncRoot(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def CopyTo(self, array: Array, arrayIndex: IntType) -> VoidType: ...
    
    def GetEnumerator(self) -> IEnumerator: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_IsReadOnly(self) -> BooleanType: ...
    
    def get_IsSynchronized(self) -> BooleanType: ...
    
    @overload
    def get_Item(self, groupnum: IntType) -> Group: ...
    
    @overload
    def get_Item(self, groupname: StringType) -> Group: ...
    
    def get_SyncRoot(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class GroupEnumerator(ObjectType, IEnumerator):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Capture(self) -> Capture: ...
    
    @property
    def Current(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def MoveNext(self) -> BooleanType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Capture(self) -> Capture: ...
    
    def get_Current(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Match(Group):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def Empty() -> Match: ...
    
    @property
    def Groups(self) -> GroupCollection: ...
    
    # ---------- Methods ---------- #
    
    def NextMatch(self) -> Match: ...
    
    def Result(self, replacement: StringType) -> StringType: ...
    
    @staticmethod
    def Synchronized(inner: Match) -> Match: ...
    
    @staticmethod
    def get_Empty() -> Match: ...
    
    def get_Groups(self) -> GroupCollection: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MatchCollection(ObjectType, ICollection, IEnumerable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def IsReadOnly(self) -> BooleanType: ...
    
    @property
    def IsSynchronized(self) -> BooleanType: ...
    
    @property
    def Item(self) -> Match: ...
    
    @property
    def SyncRoot(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def CopyTo(self, array: Array, arrayIndex: IntType) -> VoidType: ...
    
    def GetEnumerator(self) -> IEnumerator: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_IsReadOnly(self) -> BooleanType: ...
    
    def get_IsSynchronized(self) -> BooleanType: ...
    
    def get_Item(self, i: IntType) -> Match: ...
    
    def get_SyncRoot(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MatchEnumerator(ObjectType, IEnumerator):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Current(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def MoveNext(self) -> BooleanType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Current(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MatchEvaluator(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, match: Match, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> StringType: ...
    
    def Invoke(self, match: Match) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MatchSparse(Match):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Groups(self) -> GroupCollection: ...
    
    # ---------- Methods ---------- #
    
    def get_Groups(self) -> GroupCollection: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class NoParamDelegate(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, r: RegexRunner, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, r: RegexRunner) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Regex(ObjectType, ISerializable):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def InfiniteMatchTimeout() -> TimeSpan: ...
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, pattern: StringType): ...
    
    @overload
    def __init__(self, pattern: StringType, options: RegexOptions): ...
    
    @overload
    def __init__(self, pattern: StringType, options: RegexOptions, matchTimeout: TimeSpan): ...
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def CacheSize() -> IntType: ...
    
    @staticmethod
    @CacheSize.setter
    def CacheSize(value: IntType) -> None: ...
    
    @property
    def MatchTimeout(self) -> TimeSpan: ...
    
    @property
    def Options(self) -> RegexOptions: ...
    
    @property
    def RightToLeft(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    @overload
    def CompileToAssembly(regexinfos: ArrayType[RegexCompilationInfo], assemblyname: AssemblyName) -> VoidType: ...
    
    @staticmethod
    @overload
    def CompileToAssembly(regexinfos: ArrayType[RegexCompilationInfo], assemblyname: AssemblyName, attributes: ArrayType[CustomAttributeBuilder]) -> VoidType: ...
    
    @staticmethod
    @overload
    def CompileToAssembly(regexinfos: ArrayType[RegexCompilationInfo], assemblyname: AssemblyName, attributes: ArrayType[CustomAttributeBuilder], resourceFile: StringType) -> VoidType: ...
    
    @staticmethod
    def Escape(str: StringType) -> StringType: ...
    
    def GetGroupNames(self) -> ArrayType[StringType]: ...
    
    def GetGroupNumbers(self) -> ArrayType[IntType]: ...
    
    def GroupNameFromNumber(self, i: IntType) -> StringType: ...
    
    def GroupNumberFromName(self, name: StringType) -> IntType: ...
    
    @staticmethod
    @overload
    def IsMatch(input: StringType, pattern: StringType, options: RegexOptions, matchTimeout: TimeSpan) -> BooleanType: ...
    
    @overload
    def IsMatch(self, input: StringType) -> BooleanType: ...
    
    @overload
    def IsMatch(self, input: StringType, startat: IntType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def IsMatch(input: StringType, pattern: StringType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def IsMatch(input: StringType, pattern: StringType, options: RegexOptions) -> BooleanType: ...
    
    @staticmethod
    @overload
    def Match(input: StringType, pattern: StringType, options: RegexOptions) -> Match: ...
    
    @staticmethod
    @overload
    def Match(input: StringType, pattern: StringType, options: RegexOptions, matchTimeout: TimeSpan) -> Match: ...
    
    @overload
    def Match(self, input: StringType) -> Match: ...
    
    @overload
    def Match(self, input: StringType, startat: IntType) -> Match: ...
    
    @overload
    def Match(self, input: StringType, beginning: IntType, length: IntType) -> Match: ...
    
    @staticmethod
    @overload
    def Match(input: StringType, pattern: StringType) -> Match: ...
    
    @staticmethod
    @overload
    def Matches(input: StringType, pattern: StringType, options: RegexOptions) -> MatchCollection: ...
    
    @staticmethod
    @overload
    def Matches(input: StringType, pattern: StringType, options: RegexOptions, matchTimeout: TimeSpan) -> MatchCollection: ...
    
    @overload
    def Matches(self, input: StringType) -> MatchCollection: ...
    
    @overload
    def Matches(self, input: StringType, startat: IntType) -> MatchCollection: ...
    
    @staticmethod
    @overload
    def Matches(input: StringType, pattern: StringType) -> MatchCollection: ...
    
    @staticmethod
    @overload
    def Replace(input: StringType, pattern: StringType, replacement: StringType) -> StringType: ...
    
    @staticmethod
    @overload
    def Replace(input: StringType, pattern: StringType, replacement: StringType, options: RegexOptions) -> StringType: ...
    
    @staticmethod
    @overload
    def Replace(input: StringType, pattern: StringType, replacement: StringType, options: RegexOptions, matchTimeout: TimeSpan) -> StringType: ...
    
    @overload
    def Replace(self, input: StringType, replacement: StringType) -> StringType: ...
    
    @overload
    def Replace(self, input: StringType, replacement: StringType, count: IntType) -> StringType: ...
    
    @overload
    def Replace(self, input: StringType, replacement: StringType, count: IntType, startat: IntType) -> StringType: ...
    
    @staticmethod
    @overload
    def Replace(input: StringType, pattern: StringType, evaluator: MatchEvaluator) -> StringType: ...
    
    @staticmethod
    @overload
    def Replace(input: StringType, pattern: StringType, evaluator: MatchEvaluator, options: RegexOptions) -> StringType: ...
    
    @staticmethod
    @overload
    def Replace(input: StringType, pattern: StringType, evaluator: MatchEvaluator, options: RegexOptions, matchTimeout: TimeSpan) -> StringType: ...
    
    @overload
    def Replace(self, input: StringType, evaluator: MatchEvaluator) -> StringType: ...
    
    @overload
    def Replace(self, input: StringType, evaluator: MatchEvaluator, count: IntType) -> StringType: ...
    
    @overload
    def Replace(self, input: StringType, evaluator: MatchEvaluator, count: IntType, startat: IntType) -> StringType: ...
    
    @staticmethod
    @overload
    def Split(input: StringType, pattern: StringType) -> ArrayType[StringType]: ...
    
    @staticmethod
    @overload
    def Split(input: StringType, pattern: StringType, options: RegexOptions) -> ArrayType[StringType]: ...
    
    @staticmethod
    @overload
    def Split(input: StringType, pattern: StringType, options: RegexOptions, matchTimeout: TimeSpan) -> ArrayType[StringType]: ...
    
    @overload
    def Split(self, input: StringType) -> ArrayType[StringType]: ...
    
    @overload
    def Split(self, input: StringType, count: IntType) -> ArrayType[StringType]: ...
    
    @overload
    def Split(self, input: StringType, count: IntType, startat: IntType) -> ArrayType[StringType]: ...
    
    def ToString(self) -> StringType: ...
    
    @staticmethod
    def Unescape(str: StringType) -> StringType: ...
    
    @staticmethod
    def get_CacheSize() -> IntType: ...
    
    def get_MatchTimeout(self) -> TimeSpan: ...
    
    def get_Options(self) -> RegexOptions: ...
    
    def get_RightToLeft(self) -> BooleanType: ...
    
    @staticmethod
    def set_CacheSize(value: IntType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RegexBoyerMoore(ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def ToString(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RegexCharClass(ObjectType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RegexCode(ObjectType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RegexCompilationInfo(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, pattern: StringType, options: RegexOptions, name: StringType, fullnamespace: StringType, ispublic: BooleanType): ...
    
    @overload
    def __init__(self, pattern: StringType, options: RegexOptions, name: StringType, fullnamespace: StringType, ispublic: BooleanType, matchTimeout: TimeSpan): ...
    
    # ---------- Properties ---------- #
    
    @property
    def IsPublic(self) -> BooleanType: ...
    
    @IsPublic.setter
    def IsPublic(self, value: BooleanType) -> None: ...
    
    @property
    def MatchTimeout(self) -> TimeSpan: ...
    
    @MatchTimeout.setter
    def MatchTimeout(self, value: TimeSpan) -> None: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @Name.setter
    def Name(self, value: StringType) -> None: ...
    
    @property
    def Namespace(self) -> StringType: ...
    
    @Namespace.setter
    def Namespace(self, value: StringType) -> None: ...
    
    @property
    def Options(self) -> RegexOptions: ...
    
    @Options.setter
    def Options(self, value: RegexOptions) -> None: ...
    
    @property
    def Pattern(self) -> StringType: ...
    
    @Pattern.setter
    def Pattern(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_IsPublic(self) -> BooleanType: ...
    
    def get_MatchTimeout(self) -> TimeSpan: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_Namespace(self) -> StringType: ...
    
    def get_Options(self) -> RegexOptions: ...
    
    def get_Pattern(self) -> StringType: ...
    
    def set_IsPublic(self, value: BooleanType) -> VoidType: ...
    
    def set_MatchTimeout(self, value: TimeSpan) -> VoidType: ...
    
    def set_Name(self, value: StringType) -> VoidType: ...
    
    def set_Namespace(self, value: StringType) -> VoidType: ...
    
    def set_Options(self, value: RegexOptions) -> VoidType: ...
    
    def set_Pattern(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RegexCompiler(ABC, ObjectType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RegexFC(ObjectType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RegexFCD(ObjectType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RegexInterpreter(RegexRunner):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RegexLWCGCompiler(RegexCompiler):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RegexMatchTimeoutException(TimeoutException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, regexInput: StringType, regexPattern: StringType, matchTimeout: TimeSpan): ...
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, inner: Exception): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Input(self) -> StringType: ...
    
    @property
    def MatchTimeout(self) -> TimeSpan: ...
    
    @property
    def Pattern(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_Input(self) -> StringType: ...
    
    def get_MatchTimeout(self) -> TimeSpan: ...
    
    def get_Pattern(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RegexNode(ObjectType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RegexParser(ObjectType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RegexPrefix(ObjectType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RegexReplacement(ObjectType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RegexRunner(ABC, ObjectType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RegexRunnerFactory(ABC, ObjectType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RegexTree(ObjectType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RegexTypeCompiler(RegexCompiler):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RegexWriter(ObjectType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SharedReference(ObjectType):
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


# No Structs

# No Interfaces

# ---------- Enums ---------- #

class RegexOptions(Enum):
    #None: IntType = 0
    IgnoreCase: IntType = 1
    Multiline: IntType = 2
    ExplicitCapture: IntType = 4
    Compiled: IntType = 8
    Singleline: IntType = 16
    IgnorePatternWhitespace: IntType = 32
    RightToLeft: IntType = 64
    ECMAScript: IntType = 256
    CultureInvariant: IntType = 512


# ---------- Delegates ---------- #

CreateInstanceDelegate = Callable[[], RegexRunner]

FindFirstCharDelegate = Callable[[RegexRunner], BooleanType]

MatchEvaluator = Callable[[Match], StringType]

NoParamDelegate = Callable[[RegexRunner], VoidType]

__all__ = [
    CachedCodeEntry,
    Capture,
    CaptureCollection,
    CaptureEnumerator,
    CompiledRegexRunner,
    CompiledRegexRunnerFactory,
    CreateInstanceDelegate,
    ExclusiveReference,
    FindFirstCharDelegate,
    Group,
    GroupCollection,
    GroupEnumerator,
    Match,
    MatchCollection,
    MatchEnumerator,
    MatchEvaluator,
    MatchSparse,
    NoParamDelegate,
    Regex,
    RegexBoyerMoore,
    RegexCharClass,
    RegexCode,
    RegexCompilationInfo,
    RegexCompiler,
    RegexFC,
    RegexFCD,
    RegexInterpreter,
    RegexLWCGCompiler,
    RegexMatchTimeoutException,
    RegexNode,
    RegexParser,
    RegexPrefix,
    RegexReplacement,
    RegexRunner,
    RegexRunnerFactory,
    RegexTree,
    RegexTypeCompiler,
    RegexWriter,
    SharedReference,
    RegexOptions,
    CreateInstanceDelegate,
    FindFirstCharDelegate,
    MatchEvaluator,
    NoParamDelegate,
]
