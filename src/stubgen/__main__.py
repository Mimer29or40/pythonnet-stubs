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
    parser.add_argument("--verbose", action="store_true", help="Set log level to DEBUG")

    assembly_group = parser.add_mutually_exclusive_group()
    assembly_group.add_argument(
        "-a",
        "--all",
        action="store_true",
        help="Process all assemblies",
    )
    assembly_group.add_argument(
        "-b",
        "--built_in",
        action="store_true",
        help="Process built-in assemblies",
    )
    assembly_group.add_argument(
        "-c",
        "--core",
        action="store_true",
        help="Process core assemblies",
    )

    parser.add_argument(
        "-o",
        "--output",
        action="store",
        type=Path,
        default=Path("stubs"),
        help="Name of Output Directory",
    )
    parser.add_argument(
        "-p",
        "--path",
        action="append",
        type=Path,
        help="Additional directories to add to the path",
    )

    # commands = parser.add_subparsers(dest="command", metavar="command")
    # sub_parser = commands.add_parser("group", help="start the service")

    parser.add_argument(
        "assemblies",
        nargs=ONE_OR_MORE,
        help="Names of dll assemblies to process",
    )

    parsed_args: Namespace = parser.parse_args(args)

    verbose: bool = parsed_args.verbose

    use_all: bool = parsed_args.all
    use_built_in: bool = parsed_args.built_in
    use_core: bool = parsed_args.core

    output: Path = parsed_args.output
    paths: Sequence[Path] = parsed_args.path
    assembly_names: List[str] = list(parsed_args.assemblies)

    if verbose:
        console_handler.setLevel(logging.DEBUG)

    path: Path
    for path in paths:
        path_str: str = str(path.resolve())
        logger.debug("Adding to sys.path: %r", path_str)
        sys.path.append(path_str)

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

    assembly_names = list(dict.fromkeys(assembly_names).keys())

    assembly: str
    for assembly in assembly_names:
        logger.debug(f"Using assembly: %r", assembly)

    output = output.resolve()
    logger.debug("Using output directory: %r", str(output))

    exit_code: Union[int, str]
    try:
        exit_code = make_stubs(assembly_names)
    except Exception as e:
        logger.exception("An unhandled exception occurred:", exc_info=e)
        exit_code = str(e)

    return exit_code


if __name__ == "__main__":
    args: Sequence[str] = sys.argv[1:]

    result: Union[int, str] = main(*args)

    sys.exit(result)
