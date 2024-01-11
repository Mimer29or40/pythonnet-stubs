import logging
import sys
from argparse import ONE_OR_MORE
from argparse import ArgumentParser
from argparse import Namespace
from pathlib import Path
from typing import Any
from typing import List
from typing import Sequence
from typing import Set
from typing import Union

import stubgen
from stubgen.defaults import ASSEMBLIES
from stubgen.defaults import BUILT_INS
from stubgen.defaults import CORE
from stubgen.extract_stubs import extract_stubs
from stubgen.log import console_handler
from stubgen.log import get_logger
from stubgen.make_stubs import make_stubs

logger = get_logger(__name__)


def main(*args: Any) -> Union[int, str]:
    parser: ArgumentParser = ArgumentParser(
        prog=stubgen.__name__,
        description=stubgen.__description__,
    )

    parser.add_argument("-v", "--version", action="version", version=stubgen.__version__)
    parser.add_argument("--verbose", action="store_true", help="set log level to DEBUG")

    parser.add_argument(
        "-o",
        "--output-dir",
        dest="output_dir",
        action="store",
        type=Path,
        default=Path("."),
        help="path to output directory [default: .]",
    )

    commands = parser.add_subparsers(dest="command", metavar="command")
    extract_command = commands.add_parser("extract", help="extract types from assemblies to json")
    extract_command.add_argument(
        "-s",
        "--skip-failed",
        dest="skip_failed",
        action="store_true",
        help="skips failed assemblies",
    )
    extract_command.add_argument(
        "-p",
        "--path",
        action="append",
        type=Path,
        help="additional directories to add to the path",
    )
    assembly_group = extract_command.add_mutually_exclusive_group()
    assembly_group.add_argument(
        "-a",
        "--all",
        action="store_true",
        help="process all assemblies",
    )
    assembly_group.add_argument(
        "-b",
        "--built_in",
        action="store_true",
        help="process built-in assemblies",
    )
    assembly_group.add_argument(
        "-c",
        "--core",
        action="store_true",
        help="process core assemblies",
    )
    extract_command.add_argument(
        "assemblies",
        nargs=ONE_OR_MORE,
        help="names of dll assemblies to process",
    )

    parsed_args: Namespace = parser.parse_args(args)

    verbose: bool = parsed_args.verbose
    if verbose:
        console_handler.setLevel(logging.DEBUG)

    output_dir: Path = parsed_args.output_dir
    output_dir = output_dir.resolve()
    logger.debug("Using output directory: %r", str(output_dir))

    exit_code: Union[int, str] = 0
    try:
        command: str = parsed_args.command
        if command == "extract":
            use_all: bool = parsed_args.all
            use_built_in: bool = parsed_args.built_in
            use_core: bool = parsed_args.core

            skip_failed: bool = parsed_args.skip_failed

            paths: Sequence[Path] = parsed_args.path
            path: Path
            for path in paths:
                path_str: str = str(path.resolve())
                logger.debug("Adding to sys.path: %r", path_str)
                sys.path.append(path_str)

            assembly_names: List[str] = list()
            if use_all:
                logger.debug("Adding all assemblies")
                assembly_names.extend(ASSEMBLIES)
                assembly_names.extend(BUILT_INS)
                assembly_names.extend(CORE)
            elif use_built_in:
                logger.debug("Adding built-in assemblies")
                assembly_names.extend(BUILT_INS)
            elif use_core:
                logger.debug("Adding core assemblies")
                assembly_names.extend(CORE)
            assemblies: Sequence[str] = parsed_args.assemblies
            assembly_names.extend(assemblies)
            assembly_names = list(dict.fromkeys(assembly_names).keys())

            try:
                assembly: str
                for assembly in assembly_names:
                    exit_code = extract_stubs(assembly, output_dir, True)
                    if exit_code != 0 and not skip_failed:
                        break
            except Exception as e:
                if not skip_failed:
                    raise e from None

    except Exception as e:
        logger.exception("An unhandled exception occurred:", exc_info=e)
        exit_code = str(e)

    return exit_code


if __name__ == "__main__":
    args: Sequence[str] = sys.argv[1:]

    result: Union[int, str] = main(*args)

    sys.exit(result)
