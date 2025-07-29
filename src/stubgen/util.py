"""Utility functions for stubgen."""

from __future__ import annotations

import keyword
import re
from collections.abc import Mapping
from collections.abc import Sequence
from typing import TYPE_CHECKING

from packaging.version import Version

from stubgen.log import get_logger

if TYPE_CHECKING:  # pragma: no cover
    from collections.abc import Callable
    from logging import Logger
    from re import Pattern
    from typing import Literal

    type CompareResults = Literal[-1, 0, 1]
    type MergeFunc[T] = Callable[[T, T], T]

logger: Logger = get_logger(__name__)


def _is_valid_python_name(name: str) -> bool:  # pragma: no cover
    return name.isidentifier() and not keyword.iskeyword(name)


illegal_chars: Pattern[str] = re.compile(r"`\d+|&|\[|]|\*|<|>")


def make_python_name(string: str) -> str:
    """Remove illegal characters to form a valid Python name."""
    if (idx := string.find("[")) >= 0:
        string = string[:idx]
    string = illegal_chars.sub("", string)
    return string if _is_valid_python_name(string) else f"_{string}"


def _compare_boolean(x: bool, y: bool) -> CompareResults:
    return 0 if x == y else (-1 if y else 1)


def _compare_string(x: str | None, y: str | None) -> CompareResults:
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
    raise NotImplementedError  # pragma: no cover


def _compare_version(x: str, y: str) -> CompareResults:
    return 0 if (v_x := Version(x)) == (v_y := Version(y)) else (-1 if v_x < v_y else 1)


def _merge_string(x: str | None, y: str | None) -> str | None:
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
    raise NotImplementedError  # pragma: no cover


def _merge_sequence[T](
    x: Sequence[T] | None,
    y: Sequence[T] | None,
    merge_func: MergeFunc[T],
) -> list[T] | None:
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
    raise NotImplementedError  # pragma: no cover


def _merge_mapping[T](
    x: Mapping[str, T] | None,
    y: Mapping[str, T] | None,
    merge_func: MergeFunc[T],
) -> Mapping[str, T] | None:
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
    raise NotImplementedError  # pragma: no cover
