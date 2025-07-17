"""Functions and class related to the CLI."""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:  # pragma: no cover
    from argparse import ArgumentParser

    # noinspection PyProtectedMember
    from argparse import _SubParsersAction

    type CommandResult = int | str


@dataclass(frozen=True, kw_only=True)
class CommandArguments(ABC):
    """Base class for command-line arguments."""

    command: str
    verbose: bool = False
    output_dir: Path = Path()
    multi_threaded: bool = False

    @classmethod
    @abstractmethod
    def populate_parser(cls, sub_parser: _SubParsersAction[ArgumentParser]) -> None:
        """Populate parser with arguments for the command."""
