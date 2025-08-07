"""Automatically generated stubs for C# namespace: System.Text.RegularExpressions."""

from abc import ABC
from collections.abc import Callable
from collections.abc import Iterator
from typing import ClassVar
from typing import overload

from System import Array
from System import Enum
from System import Exception
from System import Object
from System import TimeoutException
from System import TimeSpan
from System import Type
from System.Collections import ICollection
from System.Collections import IDictionary
from System.Collections import IEnumerable
from System.Collections import IEnumerator
from System.Reflection import AssemblyName
from System.Reflection import MethodBase
from System.Reflection.Emit import CustomAttributeBuilder
from System.Runtime.InteropServices import _Exception
from System.Runtime.Serialization import ISerializable
from System.Runtime.Serialization import SerializationInfo
from System.Runtime.Serialization import StreamingContext

class CachedCodeEntry(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class Capture(Object):
    """"""
    @property
    def Index(self) -> int:
        """"""
    @property
    def Length(self) -> int:
        """"""
    @property
    def Value(self) -> str:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class CaptureCollection(Object, ICollection, IEnumerable):
    """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def Item(self) -> Capture:
        """"""
    @property
    def SyncRoot(self) -> object:
        """"""
    def CopyTo(self, array: Array, arrayIndex: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, i: int) -> Capture:
        """"""

class CaptureEnumerator(Object, IEnumerator):
    """"""
    @property
    def Capture(self) -> Capture:
        """"""
    @property
    def Current(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def MoveNext(self) -> bool:
        """"""
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class CompiledRegexRunner(RegexRunner):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class CompiledRegexRunnerFactory(RegexRunnerFactory):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

CreateInstanceDelegate: Callable[[], RegexRunner] = ...
""""""

class ExclusiveReference(Object):
    """"""
    def __init__(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

FindFirstCharDelegate: Callable[[RegexRunner], bool] = ...
""""""

class Group(Capture):
    """"""
    @property
    def Captures(self) -> CaptureCollection:
        """"""
    @property
    def Index(self) -> int:
        """"""
    @property
    def Length(self) -> int:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def Success(self) -> bool:
        """"""
    @property
    def Value(self) -> str:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def Synchronized(cls, inner: Group) -> Group:
        """"""
    def ToString(self) -> str:
        """"""

class GroupCollection(Object, ICollection, IEnumerable):
    """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def Item(self) -> Group:
        """"""
    @property
    def SyncRoot(self) -> object:
        """"""
    def CopyTo(self, array: Array, arrayIndex: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    def __len__(self) -> int:
        """"""
    @overload
    def __getitem__(self, groupnum: int) -> Group:
        """"""
    @overload
    def __getitem__(self, groupname: str) -> Group:
        """"""

class GroupEnumerator(Object, IEnumerator):
    """"""
    @property
    def Capture(self) -> Capture:
        """"""
    @property
    def Current(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def MoveNext(self) -> bool:
        """"""
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class Match(Group):
    """"""
    @property
    def Captures(self) -> CaptureCollection:
        """"""
    @classmethod
    @property
    def Empty(cls) -> Match:
        """"""
    @property
    def Groups(self) -> GroupCollection:
        """"""
    @property
    def Index(self) -> int:
        """"""
    @property
    def Length(self) -> int:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def Success(self) -> bool:
        """"""
    @property
    def Value(self) -> str:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def NextMatch(self) -> Match:
        """"""
    def Result(self, replacement: str) -> str:
        """"""
    @classmethod
    def Synchronized(cls, inner: Match) -> Match:
        """"""
    def ToString(self) -> str:
        """"""

class MatchCollection(Object, ICollection, IEnumerable):
    """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def Item(self) -> Match:
        """"""
    @property
    def SyncRoot(self) -> object:
        """"""
    def CopyTo(self, array: Array, arrayIndex: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, i: int) -> Match:
        """"""

class MatchEnumerator(Object, IEnumerator):
    """"""
    @property
    def Current(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def MoveNext(self) -> bool:
        """"""
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

MatchEvaluator: Callable[[Match], str] = ...
""""""

class MatchSparse(Match):
    """"""
    @property
    def Captures(self) -> CaptureCollection:
        """"""
    @property
    def Groups(self) -> GroupCollection:
        """"""
    @property
    def Index(self) -> int:
        """"""
    @property
    def Length(self) -> int:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def Success(self) -> bool:
        """"""
    @property
    def Value(self) -> str:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def NextMatch(self) -> Match:
        """"""
    def Result(self, replacement: str) -> str:
        """"""
    def ToString(self) -> str:
        """"""

NoParamDelegate: Callable[[RegexRunner], None] = ...
""""""

class Regex(Object, ISerializable):
    """"""

    InfiniteMatchTimeout: ClassVar[TimeSpan]
    """"""
    @overload
    def __init__(self, pattern: str) -> None:
        """"""
    @overload
    def __init__(self, pattern: str, options: RegexOptions) -> None:
        """"""
    @overload
    def __init__(self, pattern: str, options: RegexOptions, matchTimeout: TimeSpan) -> None:
        """"""
    @classmethod
    @property
    def CacheSize(cls) -> int:
        """"""
    @classmethod
    @CacheSize.setter
    def CacheSize(cls, value: int) -> None: ...
    @property
    def MatchTimeout(self) -> TimeSpan:
        """"""
    @property
    def Options(self) -> RegexOptions:
        """"""
    @property
    def RightToLeft(self) -> bool:
        """"""
    @classmethod
    @overload
    def CompileToAssembly(
        cls, regexinfos: Array[RegexCompilationInfo], assemblyname: AssemblyName
    ) -> None:
        """"""
    @classmethod
    @overload
    def CompileToAssembly(
        cls,
        regexinfos: Array[RegexCompilationInfo],
        assemblyname: AssemblyName,
        attributes: Array[CustomAttributeBuilder],
    ) -> None:
        """"""
    @classmethod
    @overload
    def CompileToAssembly(
        cls,
        regexinfos: Array[RegexCompilationInfo],
        assemblyname: AssemblyName,
        attributes: Array[CustomAttributeBuilder],
        resourceFile: str,
    ) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def Escape(cls, str: str) -> str:
        """"""
    def GetGroupNames(self) -> Array[str]:
        """"""
    def GetGroupNumbers(self) -> Array[int]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def GroupNameFromNumber(self, i: int) -> str:
        """"""
    def GroupNumberFromName(self, name: str) -> int:
        """"""
    @overload
    def IsMatch(self, input: str) -> bool:
        """"""
    @overload
    def IsMatch(self, input: str, startat: int) -> bool:
        """"""
    @classmethod
    @overload
    def IsMatch(cls, input: str, pattern: str) -> bool:
        """"""
    @classmethod
    @overload
    def IsMatch(cls, input: str, pattern: str, options: RegexOptions) -> bool:
        """"""
    @classmethod
    @overload
    def IsMatch(
        cls, input: str, pattern: str, options: RegexOptions, matchTimeout: TimeSpan
    ) -> bool:
        """"""
    @overload
    def Match(self, input: str) -> Match:
        """"""
    @overload
    def Match(self, input: str, startat: int) -> Match:
        """"""
    @overload
    def Match(self, input: str, beginning: int, length: int) -> Match:
        """"""
    @classmethod
    @overload
    def Match(cls, input: str, pattern: str) -> Match:
        """"""
    @classmethod
    @overload
    def Match(cls, input: str, pattern: str, options: RegexOptions) -> Match:
        """"""
    @classmethod
    @overload
    def Match(
        cls, input: str, pattern: str, options: RegexOptions, matchTimeout: TimeSpan
    ) -> Match:
        """"""
    @overload
    def Matches(self, input: str) -> MatchCollection:
        """"""
    @overload
    def Matches(self, input: str, startat: int) -> MatchCollection:
        """"""
    @classmethod
    @overload
    def Matches(cls, input: str, pattern: str) -> MatchCollection:
        """"""
    @classmethod
    @overload
    def Matches(cls, input: str, pattern: str, options: RegexOptions) -> MatchCollection:
        """"""
    @classmethod
    @overload
    def Matches(
        cls, input: str, pattern: str, options: RegexOptions, matchTimeout: TimeSpan
    ) -> MatchCollection:
        """"""
    @overload
    def Replace(self, input: str, evaluator: MatchEvaluator) -> str:
        """"""
    @overload
    def Replace(self, input: str, evaluator: MatchEvaluator, count: int) -> str:
        """"""
    @overload
    def Replace(self, input: str, evaluator: MatchEvaluator, count: int, startat: int) -> str:
        """"""
    @overload
    def Replace(self, input: str, replacement: str) -> str:
        """"""
    @classmethod
    @overload
    def Replace(cls, input: str, pattern: str, evaluator: MatchEvaluator) -> str:
        """"""
    @classmethod
    @overload
    def Replace(
        cls, input: str, pattern: str, evaluator: MatchEvaluator, options: RegexOptions
    ) -> str:
        """"""
    @classmethod
    @overload
    def Replace(
        cls,
        input: str,
        pattern: str,
        evaluator: MatchEvaluator,
        options: RegexOptions,
        matchTimeout: TimeSpan,
    ) -> str:
        """"""
    @overload
    def Replace(self, input: str, replacement: str, count: int) -> str:
        """"""
    @overload
    def Replace(self, input: str, replacement: str, count: int, startat: int) -> str:
        """"""
    @classmethod
    @overload
    def Replace(cls, input: str, pattern: str, replacement: str) -> str:
        """"""
    @classmethod
    @overload
    def Replace(cls, input: str, pattern: str, replacement: str, options: RegexOptions) -> str:
        """"""
    @classmethod
    @overload
    def Replace(
        cls,
        input: str,
        pattern: str,
        replacement: str,
        options: RegexOptions,
        matchTimeout: TimeSpan,
    ) -> str:
        """"""
    @overload
    def Split(self, input: str) -> Array[str]:
        """"""
    @overload
    def Split(self, input: str, count: int) -> Array[str]:
        """"""
    @overload
    def Split(self, input: str, count: int, startat: int) -> Array[str]:
        """"""
    @classmethod
    @overload
    def Split(cls, input: str, pattern: str) -> Array[str]:
        """"""
    @classmethod
    @overload
    def Split(cls, input: str, pattern: str, options: RegexOptions) -> Array[str]:
        """"""
    @classmethod
    @overload
    def Split(
        cls, input: str, pattern: str, options: RegexOptions, matchTimeout: TimeSpan
    ) -> Array[str]:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def Unescape(cls, str: str) -> str:
        """"""

class RegexBoyerMoore(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class RegexCharClass(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class RegexCode(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class RegexCompilationInfo(Object):
    """"""
    @overload
    def __init__(
        self, pattern: str, options: RegexOptions, name: str, fullnamespace: str, ispublic: bool
    ) -> None:
        """"""
    @overload
    def __init__(
        self,
        pattern: str,
        options: RegexOptions,
        name: str,
        fullnamespace: str,
        ispublic: bool,
        matchTimeout: TimeSpan,
    ) -> None:
        """"""
    @property
    def IsPublic(self) -> bool:
        """"""
    @IsPublic.setter
    def IsPublic(self, value: bool) -> None: ...
    @property
    def MatchTimeout(self) -> TimeSpan:
        """"""
    @MatchTimeout.setter
    def MatchTimeout(self, value: TimeSpan) -> None: ...
    @property
    def Name(self) -> str:
        """"""
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def Namespace(self) -> str:
        """"""
    @Namespace.setter
    def Namespace(self, value: str) -> None: ...
    @property
    def Options(self) -> RegexOptions:
        """"""
    @Options.setter
    def Options(self, value: RegexOptions) -> None: ...
    @property
    def Pattern(self) -> str:
        """"""
    @Pattern.setter
    def Pattern(self, value: str) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class RegexCompiler(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class RegexFC(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class RegexFCD(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class RegexInterpreter(RegexRunner):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class RegexLWCGCompiler(RegexCompiler):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class RegexMatchTimeoutException(TimeoutException, _Exception, ISerializable):
    """"""
    @overload
    def __init__(self, regexInput: str, regexPattern: str, matchTimeout: TimeSpan) -> None:
        """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, message: str) -> None:
        """"""
    @overload
    def __init__(self, message: str, inner: Exception) -> None:
        """"""
    @property
    def Data(self) -> IDictionary:
        """"""
    @property
    def HResult(self) -> int:
        """"""
    @property
    def HelpLink(self) -> str:
        """"""
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """"""
    @property
    def Input(self) -> str:
        """"""
    @property
    def MatchTimeout(self) -> TimeSpan:
        """"""
    @property
    def Message(self) -> str:
        """"""
    @property
    def Pattern(self) -> str:
        """"""
    @property
    def Source(self) -> str:
        """"""
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """"""
    @property
    def TargetSite(self) -> MethodBase:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetBaseException(self) -> Exception:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class RegexNode(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class RegexOptions(Enum):
    """"""

    _None: RegexOptions = ...
    """"""
    IgnoreCase: RegexOptions = ...
    """"""
    Multiline: RegexOptions = ...
    """"""
    ExplicitCapture: RegexOptions = ...
    """"""
    Compiled: RegexOptions = ...
    """"""
    Singleline: RegexOptions = ...
    """"""
    IgnorePatternWhitespace: RegexOptions = ...
    """"""
    RightToLeft: RegexOptions = ...
    """"""
    ECMAScript: RegexOptions = ...
    """"""
    CultureInvariant: RegexOptions = ...
    """"""

class RegexParser(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class RegexPrefix(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class RegexReplacement(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class RegexRunner(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class RegexRunnerFactory(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class RegexTree(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class RegexTypeCompiler(RegexCompiler):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class RegexWriter(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SharedReference(Object):
    """"""
    def __init__(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
