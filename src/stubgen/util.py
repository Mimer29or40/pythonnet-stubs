"""Utility functions for stubgen."""

from __future__ import annotations

import keyword
import re
from typing import TYPE_CHECKING

from packaging.version import Version

from stubgen.log import get_logger

if TYPE_CHECKING:  # pragma: no cover
    from collections.abc import Callable
    from collections.abc import Mapping
    from collections.abc import Sequence
    from logging import Logger
    from typing import Literal

    type CompareResults = Literal[-1, 0, 1]

logger: Logger = get_logger(__name__)


def is_name_valid(name: str) -> bool:
    if "." in name:
        return all(map(is_name_valid, name.split(".")))
    return name.isidentifier() and not keyword.iskeyword(name)


def make_python_name(string: str) -> str:
    if "[" in string:
        string = string[: string.index("[")]
    string = make_python_name.pattern.sub("", string)
    if keyword.iskeyword(string):
        return f"_{string}"
    return string


make_python_name.pattern = re.compile(r"`\d+|&|\[|]|\*|<|>")


def _compare_boolean(x: bool | None, y: bool | None) -> CompareResults:  # pragma: no cover
    match x, y:
        case (None, None):
            return 0
        case (None, bool()):
            return -1
        case (bool(), None):
            return 1
        case (bool(), bool()):
            return 0 if x == y else (-1 if y else 1)
    # This should never be reached, as long as the parameter types are correct
    return 0


def _compare_string(x: str | None, y: str | None) -> CompareResults:  # pragma: no cover
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
    return 0


def _compare_version(x: str | None, y: str | None) -> CompareResults:  # pragma: no cover
    x = Version(x)
    y = Version(y)
    match x, y:
        case (None, None):
            return 0
        case (None, Version()):
            return -1
        case (Version(), None):
            return 1
        case (Version(), Version()):
            return 0 if x == y else (-1 if x < y else 1)
    # This should never be reached, as long as the parameter types are correct
    return 0


def _merge_string(x: str | None, y: str | None) -> str | None:  # pragma: no cover
    return_doc: str | None = None
    if x is not None:
        return_doc = x
        if y is not None:
            if x != "":
                if y != "":
                    return_doc += "\n" + y
            elif y != "":
                return_doc = y
    elif y is not None:
        return_doc = y
    return return_doc


def _merge_sequence[T](
    x: Sequence[T] | None,
    y: Sequence[T] | None,
    merge_func: Callable[[T, T], T],
) -> list[T] | None:  # pragma: no cover
    merged: list[T] | None = None
    if x is not None:
        merged = list(x)
        if y is not None:
            obj1: T
            obj2: T
            for obj2 in y:
                try:
                    index: int = merged.index(obj2)
                    obj1 = merged[index]
                    merged[index] = merge_func(obj1, obj2)
                except ValueError:
                    merged.append(obj2)
    elif y is not None:
        merged = list(y)
    return merged


def _merge_mapping[T](
    x: Mapping[str, T] | None,
    y: Mapping[str, T] | None,
    merge_func: Callable[[T, T], T],
) -> Mapping[str, T] | None:  # pragma: no cover
    merged: dict[str, T] | None = None
    if x is not None:
        merged = dict(x)
        if y is not None:
            name: str
            obj1: T
            obj2: T
            for name, obj2 in y.items():
                if name in x:
                    obj1 = x[name]
                    obj2 = merge_func(obj1, obj2)
                merged[name] = obj2
    elif y is not None:
        merged = dict(y)
    return merged
