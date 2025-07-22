"""Utility functions for stubgen."""

from __future__ import annotations

import keyword
import re
from typing import TYPE_CHECKING

from stubgen.log import get_logger

if TYPE_CHECKING:  # pragma: no cover
    from logging import Logger

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
