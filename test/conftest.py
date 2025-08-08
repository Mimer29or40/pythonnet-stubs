"""Tests for stubgen.model.py."""

from __future__ import annotations

import functools
from pathlib import Path
from typing import TYPE_CHECKING

import pytest

from stubgen.model import CType

if TYPE_CHECKING:  # pragma: no cover
    from collections.abc import Mapping
    from collections.abc import Sequence

    type ParamSequence[T] = Sequence[tuple[str, T]]


TEST_LIB: str = "TestLib"
TL_SKELETON: str = f"{TEST_LIB}_1.0.0.0_skeleton.json"
TL_DOC: str = f"{TEST_LIB}_1.0.0.0_doc.json"


def make_params[T](o: ParamSequence[T]) -> Mapping[str, ...]:
    """Make pytest.mark.parametrize arguments with a ParamSequence."""
    return {
        "argvalues": [payload for _, payload in o],
        "ids": [identifier for identifier, _ in o],
    }


@pytest.fixture
def output_dir() -> Path:
    """Output directory fixture."""
    output_dir: Path = Path("output")
    output_dir.mkdir(parents=True, exist_ok=True)
    return output_dir


@functools.cache
def generic(name: str) -> CType:
    """Create a generic type."""
    return CType(name=name, generic=True)
