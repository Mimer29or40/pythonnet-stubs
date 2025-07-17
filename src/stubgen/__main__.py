"""Entry point for CLI."""

from __future__ import annotations

import logging
import sys
from argparse import ArgumentParser
from argparse import Namespace
from pathlib import Path
from typing import TYPE_CHECKING

from stubgen.build_stubs import BuildArguments
from stubgen.build_stubs import command_build
from stubgen.extract_stubs import ExtractArguments
from stubgen.extract_stubs import command_extract
from stubgen.log import get_logger

if TYPE_CHECKING:  # pragma: no cover
    # noinspection PyProtectedMember
    from argparse import _SubParsersAction
    from collections.abc import Sequence
    from logging import Logger

    from stubgen.command import CommandArguments
    from stubgen.command import CommandResult

logger: Logger = get_logger(__name__)

COMMAND_ARGUMENTS: Sequence[type[CommandArguments]] = [
    ExtractArguments,
    BuildArguments,
]


def _setup_parser() -> ArgumentParser:
    from importlib.metadata import version

    import stubgen

    parser: ArgumentParser = ArgumentParser(prog=stubgen.__name__, description=stubgen.__doc__)

    parser.add_argument("-v", "--version", action="version", version=version("stubgen"))
    parser.add_argument("--verbose", action="store_true", help="set log level to DEBUG")

    parser.add_argument(
        "-o",
        "--output-dir",
        action="store",
        default=Path(),
        type=Path,
        help="path to output directory [default: .]",
        dest="output_dir",
    )
    parser.add_argument(
        "-m",
        "--multi-threaded",
        action="store_true",
        help="flag to use multi threading",
        dest="multi_threaded",
    )

    command_parser: _SubParsersAction[ArgumentParser] = parser.add_subparsers(
        dest="command", metavar="command"
    )

    command_args: type[CommandArguments]
    for command_args in COMMAND_ARGUMENTS:
        command_args.populate_parser(command_parser)

    return parser


def main(*args: str) -> CommandResult:
    """Run stubgen with arguments."""
    exit_code: CommandResult = 0
    try:
        parser: ArgumentParser = _setup_parser()
        parsed_args: Namespace = parser.parse_args(args)

        verbose: bool = parsed_args.verbose
        if verbose:
            from stubgen.log import root_handler

            root_handler.setLevel(logging.DEBUG)

        match parsed_args.commands:
            case "extract":
                command_args: ExtractArguments = ExtractArguments(**parsed_args.__dict__)
                exit_code = command_extract(command_args)
            case "extract":
                command_args: BuildArguments = BuildArguments(**parsed_args.__dict__)
                exit_code = command_build(command_args)
    except Exception as e:
        logger.exception("An unhandled exception occurred:", exc_info=e)
        exit_code = str(e)

    return exit_code


if __name__ == "__main__":
    sys.exit(main(*sys.argv[1:]))
