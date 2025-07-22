"""Tests for stubgen.model.py."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:  # pragma: no cover
    from collections.abc import Mapping
    from collections.abc import Sequence

    type ParamSequence[T] = Sequence[tuple[str, T]]


def make_params[T](o: ParamSequence[T]) -> Mapping[str, ...]:
    """Make pytest.mark.parametrize arguments with a ParamSequence."""
    return {
        "argvalues": [payload for _, payload in o],
        "ids": [identifier for identifier, _ in o],
    }
