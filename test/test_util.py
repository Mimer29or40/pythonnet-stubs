"""Tests for stubgen.util.py."""

from __future__ import annotations

from typing import TYPE_CHECKING

import clr  # noqa: F401
import pytest
from conftest import make_params
from System import Array
from System import Int32
from System import Single
from System import String
from System.Collections.Generic import Dictionary
from System.Collections.Generic import List

from stubgen.util import compare_boolean
from stubgen.util import compare_string
from stubgen.util import compare_version
from stubgen.util import from_c_array
from stubgen.util import from_c_dict
from stubgen.util import from_c_list
from stubgen.util import make_python_name
from stubgen.util import merge_mapping
from stubgen.util import merge_sequence
from stubgen.util import merge_string
from stubgen.util import to_c_array
from stubgen.util import to_c_dict
from stubgen.util import to_c_list

if TYPE_CHECKING:  # pragma: no cover
    from collections.abc import Iterable
    from collections.abc import Mapping
    from collections.abc import Sequence

    from stubgen.util import CompareResults


@pytest.mark.parametrize(
    ("namespace", "expected"),
    **make_params(
        [
            ("basic", ("Type", "Type")),
            ("brackets", ("Type[Inner]", "Type")),
            ("`00", ("Type`00", "Type")),
            ("&", ("Type&", "Type")),
            ("[", ("Type[", "Type")),
            ("]", ("Type]", "Type")),
            ("*", ("Type*", "Type")),
            ("<", ("Type<", "Type")),
            (">", ("Type>", "Type")),
            ("$", ("Type$", "Type")),
            ("None", ("None", "_None")),
            ("empty", ("", "_")),
        ]
    ),
)
def test_make_python_name(namespace: str, expected: str) -> None:
    """Test for make_python_name()."""
    actual: str = make_python_name(namespace)

    assert actual == expected


@pytest.mark.parametrize(
    ("x", "y", "expected"),
    **make_params(
        [
            ("True-True", (True, True, 0)),
            ("True-False", (True, False, 1)),
            ("False-True", (False, True, -1)),
            ("False-False", (False, False, 0)),
        ]
    ),
)
def test_compare_boolean(x: bool, y: bool, expected: CompareResults) -> None:
    """Test for _compare_boolean()."""
    actual: CompareResults = compare_boolean(x, y)

    assert actual == expected


@pytest.mark.parametrize(
    ("x", "y", "expected"),
    **make_params(
        [
            ("None-None", (None, None, 0)),
            ("None-B", (None, "B", -1)),
            ("A-None", ("A", None, 1)),
            ("A-A", ("A", "A", 0)),
            ("A-B", ("A", "B", -1)),
            ("B-A", ("B", "A", 1)),
        ]
    ),
)
def test_compare_string(x: str | None, y: str | None, expected: CompareResults) -> None:
    """Test for _compare_string()."""
    actual: CompareResults = compare_string(x, y)

    assert actual == expected


@pytest.mark.parametrize(
    ("x", "y", "expected"),
    **make_params(
        [
            ("0.0.0.0-0.0.0.0", ("0.0.0.0", "0.0.0.0", 0)),
            ("0.0.0.0-0.0.0.1", ("0.0.0.0", "0.0.0.1", -1)),
            ("0.0.0.0-0.0.1.0", ("0.0.0.0", "0.0.1.0", -1)),
            ("0.0.0.0-0.1.0.0", ("0.0.0.0", "0.1.0.0", -1)),
            ("0.0.0.0-1.0.0.0", ("0.0.0.0", "1.0.0.0", -1)),
            ("0.0.0.1-0.0.0.0", ("0.0.0.1", "0.0.0.0", 1)),
            ("0.0.1.0-0.0.0.0", ("0.0.1.0", "0.0.0.0", 1)),
            ("0.1.0.0-0.0.0.0", ("0.1.0.0", "0.0.0.0", 1)),
            ("1.0.0.0-0.0.0.0", ("1.0.0.0", "0.0.0.0", 1)),
        ]
    ),
)
def test_compare_version(x: str, y: str, expected: CompareResults) -> None:
    """Test for _compare_version()."""
    actual: CompareResults = compare_version(x, y)

    assert actual == expected


@pytest.mark.parametrize(
    ("x", "y", "expected"),
    **make_params(
        [
            ("None-None", (None, None, None)),
            ("None-B", (None, "B", "B")),
            ("A-None", ("A", None, "A")),
            ("-", ("", "", "")),
            ("-B", ("", "B", "B")),
            ("A-", ("A", "", "A")),
            ("A-B", ("A", "B", "A\nB")),
        ]
    ),
)
def test_merge_string(x: str | None, y: str | None, expected: str | None) -> None:
    """Test for _merge_string()."""
    actual: str | None = merge_string(x, y)

    assert actual == expected


@pytest.mark.parametrize(
    ("x", "y", "expected"),
    **make_params(
        [
            ("None-None", (None, None, None)),
            ("None-B", (None, ["B"], ["B"])),
            ("A-None", (["A"], None, ["A"])),
            ("A-A", (["A"], ["A"], ["A"])),
            ("A-B", (["A"], ["B"], ["A", "B"])),
        ]
    ),
)
def test_merge_sequence(
    x: Sequence[str] | None, y: Sequence[str] | None, expected: Sequence[str] | None
) -> None:
    """Test for _merge_sequence()."""
    actual: Sequence[str] | None = merge_sequence(x, y, lambda x, _: x)

    assert actual == expected


@pytest.mark.parametrize(
    ("x", "y", "expected"),
    **make_params(
        [
            ("None-None", (None, None, None)),
            ("None-B", (None, {"B": "B"}, {"B": "B"})),
            ("A-None", ({"A": "A"}, None, {"A": "A"})),
            ("A-A", ({"A": "A"}, {"A": "A"}, {"A": "A"})),
            ("A-B", ({"A": "A"}, {"B": "B"}, {"A": "A", "B": "B"})),
        ]
    ),
)
def test_merge_mapping(
    x: Mapping[str, str] | None, y: Mapping[str, str] | None, expected: Mapping[str, str] | None
) -> None:
    """Test for _merge_mapping()."""
    actual: Mapping[str, str] | None = merge_mapping(x, y, lambda x, _: x)

    assert actual == expected


@pytest.mark.parametrize(
    ("cls", "expected"),
    [
        (Int32, [0, 1, 2, 3, 4]),
        (Single, [0.0, 1.0, 2.0, 3.0, 4.0]),
        (String, ["0", "1", "2", "3", "4"]),
    ],
)
def test_array[T](cls: type[T], expected: Iterable[T]) -> None:
    """Test for pyPIAF.to_c_array."""
    obj: Array[T] = to_c_array(cls, expected)

    # noinspection PyTypeHints
    assert isinstance(obj, Array[cls])

    actual: Sequence[T] = from_c_array(obj)
    assert expected == actual


@pytest.mark.parametrize(
    ("cls", "expected"),
    [
        (Int32, [0, 1, 2, 3, 4]),
        (Single, [0.0, 1.0, 2.0, 3.0, 4.0]),
        (String, ["0", "1", "2", "3", "4"]),
    ],
)
def test_list[T](cls: type[T], expected: Iterable[T]) -> None:
    """Test for pyPIAF.to_c_list."""
    obj: List[T] = to_c_list(cls, expected)

    # noinspection PyTypeHints
    assert isinstance(obj, List[cls])

    actual: Sequence[T] = from_c_list(obj)
    assert expected == actual


@pytest.mark.parametrize(
    ("key_cls", "value_cls", "expected"),
    [
        (String, Int32, {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4}),
        (String, Single, {"0": 0.0, "1": 1.0, "2": 2.0, "3": 3.0, "4": 4.0}),
        (String, String, {"0": "0", "1": "1", "2": "2", "3": "3", "4": "4"}),
    ],
)
def test_dict[K, V](key_cls: type[K], value_cls: type[V], expected: Mapping[K, V]) -> None:
    """Test for pyPIAF.to_c_dict."""
    obj: Dictionary[K, V] = to_c_dict(key_cls, value_cls, expected)

    # noinspection PyTypeHints
    assert isinstance(obj, Dictionary[key_cls, value_cls])

    actual: dict[K, V] = from_c_dict(obj)
    assert expected == actual


if __name__ == "__main__":
    pytest.main()
