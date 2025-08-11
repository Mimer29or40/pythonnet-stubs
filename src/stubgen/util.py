"""Utility functions for stubgen."""

from __future__ import annotations

import keyword
import re
from collections.abc import Iterable
from collections.abc import Mapping
from collections.abc import Sequence
from typing import TYPE_CHECKING

import clr  # noqa: F401
from packaging.version import Version
from System import Array
from System.Collections.Generic import Dictionary
from System.Collections.Generic import List

from stubgen.log import get_logger

if TYPE_CHECKING:  # pragma: no cover
    from collections.abc import Callable
    from logging import Logger
    from re import Pattern
    from typing import Literal

    from System.Collections.Generic import IDictionary
    from System.Collections.Generic import IList

    type CompareResults = Literal[-1, 0, 1]
    type MergeFunc[T] = Callable[[T, T], T]

logger: Logger = get_logger(__name__)


def _is_valid_python_name(name: str) -> bool:  # pragma: no cover
    return name.isidentifier() and not keyword.iskeyword(name) and name != "cls"


illegal_chars: Pattern[str] = re.compile(r"`\d+|&|\[|]|\*|<|>|\$")


def make_python_name(string: str) -> str:
    """Remove illegal characters to form a valid Python name."""
    if (idx := string.find("[")) >= 0:
        string = string[:idx]
    string = illegal_chars.sub("", string)
    return string if _is_valid_python_name(string) else f"_{string}"


def compare_boolean(x: bool, y: bool) -> CompareResults:
    """Compare two boolean values."""
    return 0 if x == y else (-1 if y else 1)


def compare_string(x: str | None, y: str | None) -> CompareResults:
    """Compare two str values."""
    match x, y:
        case (None, None):
            return 0
        case (None, str()):
            return -1
        case (str(), None):
            return 1
        case (str(), str()):
            return 0 if x == y else (-1 if x < y else 1)
    # This should never be reached, as long as the parameter types are correct
    # noinspection PyUnreachableCode
    raise NotImplementedError  # pragma: no cover


def compare_version(x: str, y: str) -> CompareResults:
    """Compare two str values as Version objects."""
    return 0 if (v_x := Version(x)) == (v_y := Version(y)) else (-1 if v_x < v_y else 1)


def merge_string(x: str | None, y: str | None) -> str | None:
    """Merge two str values into one."""
    match x, y:
        case (None, None):
            return None
        case (None, str()):
            return y
        case (str(), None):
            return x
        case ("", ""):
            return ""
        case ("", str()):
            return y
        case (str(), ""):
            return x
        case (str(), str()):
            return f"{x}\n{y}"
    # This should never be reached, as long as the parameter types are correct
    # noinspection PyUnreachableCode
    raise NotImplementedError  # pragma: no cover


def merge_sequence[T](
    x: Sequence[T] | None,
    y: Sequence[T] | None,
    merge_func: MergeFunc[T],
) -> list[T] | None:
    """Merge two sequences into one."""
    match x, y:
        case (None, None):
            return None
        case (None, Sequence()):
            return y
        case (Sequence(), None):
            return x
        case (Sequence(), Sequence()):
            merged: list[T] = list(x)
            obj1: T
            obj2: T
            for obj2 in y:
                try:
                    index: int = merged.index(obj2)
                    obj1 = merged[index]
                    merged[index] = merge_func(obj1, obj2)
                except ValueError:
                    merged.append(obj2)
            return merged
    # This should never be reached, as long as the parameter types are correct
    # noinspection PyUnreachableCode
    raise NotImplementedError  # pragma: no cover


def merge_mapping[T](
    x: Mapping[str, T] | None,
    y: Mapping[str, T] | None,
    merge_func: MergeFunc[T],
) -> Mapping[str, T] | None:
    """Merge two mappings into one."""
    match x, y:
        case (None, None):
            return None
        case (None, Mapping()):
            return y
        case (Mapping(), None):
            return x
        case (Mapping(), Mapping()):
            merged: dict[str, T] = dict(x)
            name: str
            obj1: T
            obj2: T
            for name, obj2 in y.items():
                if name in x:
                    obj1 = x[name]
                    obj2 = merge_func(obj1, obj2)
                merged[name] = obj2
            return merged
    # This should never be reached, as long as the parameter types are correct
    # noinspection PyUnreachableCode
    raise NotImplementedError  # pragma: no cover


def to_c_array[T](array_type: type[T], iterable: Iterable[T]) -> Array[T]:
    """Convert a python sequence to a C# Array.

    :param array_type: The type of the array.
    :param iterable: The iterable.
    :return: The Array
    """
    return Array[array_type](iterable)


def from_c_array[T](c_array: Array[T]) -> Sequence[T]:
    """Convert a C# Array to a python Sequence."""
    return list(c_array)


def to_c_list[T](list_type: type[T], iterable: Iterable[T]) -> List[T]:
    """Convert a python sequence to a C# List.

    :param list_type: The type of the array.
    :param iterable: The iterable.
    :return: The List
    """
    # noinspection PyTypeHints
    list_obj = List[list_type]()

    for obj in iterable:
        list_obj.Add(obj)

    return list_obj


def from_c_list[T](c_list: IList[T]) -> Sequence[T]:
    """Convert a C# List to a python Sequence."""
    return list(c_list)


def to_c_dict[K, V](
    key_type: type[K],
    value_type: type[V],
    mapping: Mapping[K, V],
) -> Dictionary[K, V]:
    """Convert a python mapping to a C# Dictionary.

    :param key_type: The type of the keys.
    :param value_type: The type of the values.
    :param mapping: The mapping.
    :return: The Dictionary
    """
    # noinspection PyTypeHints
    dict_obj = Dictionary[key_type, value_type]()

    for key, value in mapping.items():
        dict_obj.Add(key, value)

    return dict_obj


def from_c_dict[K, V](c_dict: IDictionary[K, V]) -> dict[K, V]:
    """Convert a C# Dictionary to a python dict."""
    return {kv.Key: kv.Value for kv in c_dict}
