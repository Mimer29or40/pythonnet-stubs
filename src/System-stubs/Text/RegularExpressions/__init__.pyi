from __future__ import annotations

from abc import ABC
from typing import Callable
from typing import ClassVar
from typing import Final
from typing import Iterator
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

class Capture(Object):
    """"""

    @property
    def Index(self) -> int:
        """

        :return:
        """
    @property
    def Length(self) -> int:
        """

        :return:
        """
    @property
    def Value(self) -> str:
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

class CaptureCollection(Object, ICollection, IEnumerable):
    """"""

    @property
    def Count(self) -> int:
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
    def Item(self) -> Capture:
        """

        :return:
        """
    @property
    def SyncRoot(self) -> object:
        """

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
    def ToString(self) -> str:
        """

        :return:
        """
    def __contains__(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    def __getitem__(self, i: int) -> Capture:
        """

        :param i:
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

class CaptureEnumerator(Object, IEnumerator):
    """"""

    @property
    def Capture(self) -> Capture:
        """

        :return:
        """
    @property
    def Current(self) -> object:
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
    def MoveNext(self) -> bool:
        """

        :return:
        """
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class CompiledRegexRunner(RegexRunner):
    """"""

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

class CompiledRegexRunnerFactory(RegexRunnerFactory):
    """"""

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

CreateInstanceDelegate: Callable[[], RegexRunner] = ...
"""

:return: 
"""

class ExclusiveReference(Object):
    """"""

    def __init__(self):
        """"""
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

FindFirstCharDelegate: Callable[[RegexRunner], bool] = ...
"""

:param r: 
:return: 
"""

class Group(Capture):
    """"""

    @property
    def Captures(self) -> CaptureCollection:
        """

        :return:
        """
    @property
    def Index(self) -> int:
        """

        :return:
        """
    @property
    def Length(self) -> int:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Success(self) -> bool:
        """

        :return:
        """
    @property
    def Value(self) -> str:
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
    @classmethod
    def Synchronized(cls, inner: Group) -> Group:
        """

        :param inner:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class GroupCollection(Object, ICollection, IEnumerable):
    """"""

    @property
    def Count(self) -> int:
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
    def Item(self) -> Group:
        """

        :return:
        """
    @property
    def SyncRoot(self) -> object:
        """

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
    def ToString(self) -> str:
        """

        :return:
        """
    def __contains__(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def __getitem__(self, groupnum: int) -> Group:
        """

        :param groupnum:
        :return:
        """
    @overload
    def __getitem__(self, groupname: str) -> Group:
        """

        :param groupname:
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

class GroupEnumerator(Object, IEnumerator):
    """"""

    @property
    def Capture(self) -> Capture:
        """

        :return:
        """
    @property
    def Current(self) -> object:
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
    def MoveNext(self) -> bool:
        """

        :return:
        """
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class Match(Group):
    """"""

    @property
    def Captures(self) -> CaptureCollection:
        """

        :return:
        """
    @classmethod
    @property
    def Empty(cls) -> Match:
        """

        :return:
        """
    @property
    def Groups(self) -> GroupCollection:
        """

        :return:
        """
    @property
    def Index(self) -> int:
        """

        :return:
        """
    @property
    def Length(self) -> int:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Success(self) -> bool:
        """

        :return:
        """
    @property
    def Value(self) -> str:
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
    def NextMatch(self) -> Match:
        """

        :return:
        """
    def Result(self, replacement: str) -> str:
        """

        :param replacement:
        :return:
        """
    @classmethod
    def Synchronized(cls, inner: Match) -> Match:
        """

        :param inner:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class MatchCollection(Object, ICollection, IEnumerable):
    """"""

    @property
    def Count(self) -> int:
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
    def Item(self) -> Match:
        """

        :return:
        """
    @property
    def SyncRoot(self) -> object:
        """

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
    def ToString(self) -> str:
        """

        :return:
        """
    def __contains__(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    def __getitem__(self, i: int) -> Match:
        """

        :param i:
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

class MatchEnumerator(Object, IEnumerator):
    """"""

    @property
    def Current(self) -> object:
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
    def MoveNext(self) -> bool:
        """

        :return:
        """
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

MatchEvaluator: Callable[[Match], str] = ...
"""

:param match: 
:return: 
"""

class MatchSparse(Match):
    """"""

    @property
    def Captures(self) -> CaptureCollection:
        """

        :return:
        """
    @classmethod
    @property
    def Empty(cls) -> Match:
        """

        :return:
        """
    @property
    def Groups(self) -> GroupCollection:
        """

        :return:
        """
    @property
    def Index(self) -> int:
        """

        :return:
        """
    @property
    def Length(self) -> int:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Success(self) -> bool:
        """

        :return:
        """
    @property
    def Value(self) -> str:
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
    def NextMatch(self) -> Match:
        """

        :return:
        """
    def Result(self, replacement: str) -> str:
        """

        :param replacement:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

NoParamDelegate: Callable[[RegexRunner], None] = ...
"""

:param r: 
"""

class Regex(Object, ISerializable):
    """"""

    InfiniteMatchTimeout: Final[ClassVar[TimeSpan]] = ...
    """
    
    :return: 
    """
    @overload
    def __init__(self, pattern: str):
        """

        :param pattern:
        """
    @overload
    def __init__(self, pattern: str, options: RegexOptions):
        """

        :param pattern:
        :param options:
        """
    @overload
    def __init__(self, pattern: str, options: RegexOptions, matchTimeout: TimeSpan):
        """

        :param pattern:
        :param options:
        :param matchTimeout:
        """
    @classmethod
    @property
    def CacheSize(cls) -> int:
        """

        :return:
        """
    @classmethod
    @CacheSize.setter
    def CacheSize(cls, value: int) -> None: ...
    @property
    def MatchTimeout(self) -> TimeSpan:
        """

        :return:
        """
    @property
    def Options(self) -> RegexOptions:
        """

        :return:
        """
    @property
    def RightToLeft(self) -> bool:
        """

        :return:
        """
    @classmethod
    @overload
    def CompileToAssembly(
        cls, regexinfos: Array[RegexCompilationInfo], assemblyname: AssemblyName
    ) -> None:
        """

        :param regexinfos:
        :param assemblyname:
        """
    @classmethod
    @overload
    def CompileToAssembly(
        cls,
        regexinfos: Array[RegexCompilationInfo],
        assemblyname: AssemblyName,
        attributes: Array[CustomAttributeBuilder],
    ) -> None:
        """

        :param regexinfos:
        :param assemblyname:
        :param attributes:
        """
    @classmethod
    @overload
    def CompileToAssembly(
        cls,
        regexinfos: Array[RegexCompilationInfo],
        assemblyname: AssemblyName,
        attributes: Array[CustomAttributeBuilder],
        resourceFile: str,
    ) -> None:
        """

        :param regexinfos:
        :param assemblyname:
        :param attributes:
        :param resourceFile:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @classmethod
    def Escape(cls, str: str) -> str:
        """

        :param str:
        :return:
        """
    def GetGroupNames(self) -> Array[str]:
        """

        :return:
        """
    def GetGroupNumbers(self) -> Array[int]:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GroupNameFromNumber(self, i: int) -> str:
        """

        :param i:
        :return:
        """
    def GroupNumberFromName(self, name: str) -> int:
        """

        :param name:
        :return:
        """
    @overload
    def IsMatch(self, input: str) -> bool:
        """

        :param input:
        :return:
        """
    @overload
    def IsMatch(self, input: str, startat: int) -> bool:
        """

        :param input:
        :param startat:
        :return:
        """
    @classmethod
    @overload
    def IsMatch(cls, input: str, pattern: str) -> bool:
        """

        :param input:
        :param pattern:
        :return:
        """
    @classmethod
    @overload
    def IsMatch(cls, input: str, pattern: str, options: RegexOptions) -> bool:
        """

        :param input:
        :param pattern:
        :param options:
        :return:
        """
    @classmethod
    @overload
    def IsMatch(
        cls, input: str, pattern: str, options: RegexOptions, matchTimeout: TimeSpan
    ) -> bool:
        """

        :param input:
        :param pattern:
        :param options:
        :param matchTimeout:
        :return:
        """
    @overload
    def Match(self, input: str) -> Match:
        """

        :param input:
        :return:
        """
    @overload
    def Match(self, input: str, startat: int) -> Match:
        """

        :param input:
        :param startat:
        :return:
        """
    @classmethod
    @overload
    def Match(cls, input: str, pattern: str) -> Match:
        """

        :param input:
        :param pattern:
        :return:
        """
    @overload
    def Match(self, input: str, beginning: int, length: int) -> Match:
        """

        :param input:
        :param beginning:
        :param length:
        :return:
        """
    @classmethod
    @overload
    def Match(cls, input: str, pattern: str, options: RegexOptions) -> Match:
        """

        :param input:
        :param pattern:
        :param options:
        :return:
        """
    @classmethod
    @overload
    def Match(
        cls, input: str, pattern: str, options: RegexOptions, matchTimeout: TimeSpan
    ) -> Match:
        """

        :param input:
        :param pattern:
        :param options:
        :param matchTimeout:
        :return:
        """
    @overload
    def Matches(self, input: str) -> MatchCollection:
        """

        :param input:
        :return:
        """
    @overload
    def Matches(self, input: str, startat: int) -> MatchCollection:
        """

        :param input:
        :param startat:
        :return:
        """
    @classmethod
    @overload
    def Matches(cls, input: str, pattern: str) -> MatchCollection:
        """

        :param input:
        :param pattern:
        :return:
        """
    @classmethod
    @overload
    def Matches(cls, input: str, pattern: str, options: RegexOptions) -> MatchCollection:
        """

        :param input:
        :param pattern:
        :param options:
        :return:
        """
    @classmethod
    @overload
    def Matches(
        cls, input: str, pattern: str, options: RegexOptions, matchTimeout: TimeSpan
    ) -> MatchCollection:
        """

        :param input:
        :param pattern:
        :param options:
        :param matchTimeout:
        :return:
        """
    @overload
    def Replace(self, input: str, evaluator: MatchEvaluator) -> str:
        """

        :param input:
        :param evaluator:
        :return:
        """
    @overload
    def Replace(self, input: str, replacement: str) -> str:
        """

        :param input:
        :param replacement:
        :return:
        """
    @overload
    def Replace(self, input: str, evaluator: MatchEvaluator, count: int) -> str:
        """

        :param input:
        :param evaluator:
        :param count:
        :return:
        """
    @classmethod
    @overload
    def Replace(cls, input: str, pattern: str, evaluator: MatchEvaluator) -> str:
        """

        :param input:
        :param pattern:
        :param evaluator:
        :return:
        """
    @overload
    def Replace(self, input: str, replacement: str, count: int) -> str:
        """

        :param input:
        :param replacement:
        :param count:
        :return:
        """
    @classmethod
    @overload
    def Replace(cls, input: str, pattern: str, replacement: str) -> str:
        """

        :param input:
        :param pattern:
        :param replacement:
        :return:
        """
    @overload
    def Replace(self, input: str, evaluator: MatchEvaluator, count: int, startat: int) -> str:
        """

        :param input:
        :param evaluator:
        :param count:
        :param startat:
        :return:
        """
    @classmethod
    @overload
    def Replace(
        cls, input: str, pattern: str, evaluator: MatchEvaluator, options: RegexOptions
    ) -> str:
        """

        :param input:
        :param pattern:
        :param evaluator:
        :param options:
        :return:
        """
    @overload
    def Replace(self, input: str, replacement: str, count: int, startat: int) -> str:
        """

        :param input:
        :param replacement:
        :param count:
        :param startat:
        :return:
        """
    @classmethod
    @overload
    def Replace(cls, input: str, pattern: str, replacement: str, options: RegexOptions) -> str:
        """

        :param input:
        :param pattern:
        :param replacement:
        :param options:
        :return:
        """
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
        """

        :param input:
        :param pattern:
        :param evaluator:
        :param options:
        :param matchTimeout:
        :return:
        """
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
        """

        :param input:
        :param pattern:
        :param replacement:
        :param options:
        :param matchTimeout:
        :return:
        """
    @overload
    def Split(self, input: str) -> Array[str]:
        """

        :param input:
        :return:
        """
    @overload
    def Split(self, input: str, count: int) -> Array[str]:
        """

        :param input:
        :param count:
        :return:
        """
    @classmethod
    @overload
    def Split(cls, input: str, pattern: str) -> Array[str]:
        """

        :param input:
        :param pattern:
        :return:
        """
    @overload
    def Split(self, input: str, count: int, startat: int) -> Array[str]:
        """

        :param input:
        :param count:
        :param startat:
        :return:
        """
    @classmethod
    @overload
    def Split(cls, input: str, pattern: str, options: RegexOptions) -> Array[str]:
        """

        :param input:
        :param pattern:
        :param options:
        :return:
        """
    @classmethod
    @overload
    def Split(
        cls, input: str, pattern: str, options: RegexOptions, matchTimeout: TimeSpan
    ) -> Array[str]:
        """

        :param input:
        :param pattern:
        :param options:
        :param matchTimeout:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @classmethod
    def Unescape(cls, str: str) -> str:
        """

        :param str:
        :return:
        """

class RegexBoyerMoore(Object):
    """"""

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

class RegexCharClass(Object):
    """"""

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

class RegexCode(Object):
    """"""

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

class RegexCompilationInfo(Object):
    """"""

    @overload
    def __init__(
        self, pattern: str, options: RegexOptions, name: str, fullnamespace: str, ispublic: bool
    ):
        """

        :param pattern:
        :param options:
        :param name:
        :param fullnamespace:
        :param ispublic:
        """
    @overload
    def __init__(
        self,
        pattern: str,
        options: RegexOptions,
        name: str,
        fullnamespace: str,
        ispublic: bool,
        matchTimeout: TimeSpan,
    ):
        """

        :param pattern:
        :param options:
        :param name:
        :param fullnamespace:
        :param ispublic:
        :param matchTimeout:
        """
    @property
    def IsPublic(self) -> bool:
        """

        :return:
        """
    @IsPublic.setter
    def IsPublic(self, value: bool) -> None: ...
    @property
    def MatchTimeout(self) -> TimeSpan:
        """

        :return:
        """
    @MatchTimeout.setter
    def MatchTimeout(self, value: TimeSpan) -> None: ...
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def Namespace(self) -> str:
        """

        :return:
        """
    @Namespace.setter
    def Namespace(self, value: str) -> None: ...
    @property
    def Options(self) -> RegexOptions:
        """

        :return:
        """
    @Options.setter
    def Options(self, value: RegexOptions) -> None: ...
    @property
    def Pattern(self) -> str:
        """

        :return:
        """
    @Pattern.setter
    def Pattern(self, value: str) -> None: ...
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

class RegexCompiler(ABC, Object):
    """"""

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

class RegexFC(Object):
    """"""

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

class RegexFCD(Object):
    """"""

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

class RegexInterpreter(RegexRunner):
    """"""

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

class RegexLWCGCompiler(RegexCompiler):
    """"""

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

class RegexMatchTimeoutException(TimeoutException, _Exception, ISerializable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, message: str):
        """

        :param message:
        """
    @overload
    def __init__(self, message: str, inner: Exception):
        """

        :param message:
        :param inner:
        """
    @overload
    def __init__(self, regexInput: str, regexPattern: str, matchTimeout: TimeSpan):
        """

        :param regexInput:
        :param regexPattern:
        :param matchTimeout:
        """
    @property
    def Data(self) -> IDictionary:
        """

        :return:
        """
    @property
    def HResult(self) -> int:
        """

        :return:
        """
    @property
    def HelpLink(self) -> str:
        """

        :return:
        """
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """

        :return:
        """
    @property
    def Input(self) -> str:
        """

        :return:
        """
    @property
    def MatchTimeout(self) -> TimeSpan:
        """

        :return:
        """
    @property
    def Message(self) -> str:
        """

        :return:
        """
    @property
    def Pattern(self) -> str:
        """

        :return:
        """
    @property
    def Source(self) -> str:
        """

        :return:
        """
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """

        :return:
        """
    @property
    def TargetSite(self) -> MethodBase:
        """

        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetBaseException(self) -> Exception:
        """

        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """

class RegexNode(Object):
    """"""

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

class RegexPrefix(Object):
    """"""

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

class RegexReplacement(Object):
    """"""

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

class RegexRunner(ABC, Object):
    """"""

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

class RegexRunnerFactory(ABC, Object):
    """"""

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

class RegexTree(Object):
    """"""

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

class RegexTypeCompiler(RegexCompiler):
    """"""

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

class RegexWriter(Object):
    """"""

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

class SharedReference(Object):
    """"""

    def __init__(self):
        """"""
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
