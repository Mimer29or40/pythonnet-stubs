import logging
import sys
from argparse import ZERO_OR_MORE
from argparse import ArgumentParser
from argparse import Namespace
from pathlib import Path
from typing import Any
from typing import List
from typing import Sequence
from typing import Union

import stubgen
from stubgen.defaults import ASSEMBLIES
from stubgen.defaults import BUILT_INS
from stubgen.defaults import CORE
from stubgen.extract_stubs import extract_assemblies
from stubgen.log import console_handler
from stubgen.log import get_logger

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
    parser.add_argument(
        "-m",
        "--multi-threaded",
        dest="multi_threaded",
        action="store_true",
        help="flag to use multi threading",
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
        "-w",
        "--overwrite",
        action="store_true",
        help="overwrite existing files",
    )
    extract_command.add_argument(
        "assemblies",
        nargs=ZERO_OR_MORE,
        help="names of dll assemblies to process",
    )

    build_command = commands.add_parser("build", help="build stub file tree")
    build_command.add_argument(
        "-l",
        "--line-length",
        type=int,
        default=100,
        help="process core assemblies",
    )
    build_command.add_argument(
        "-f",
        "--format-files",
        action="store_true",
        help="format generated stub files",
    )
    build_command.add_argument(
        "skeletons",
        help="glob to the skeleton files",
    )
    build_command.add_argument(
        "docs",
        help="glob to the doc files",
    )

    parsed_args: Namespace = parser.parse_args(args)

    verbose: bool = parsed_args.verbose
    if verbose:
        console_handler.setLevel(logging.DEBUG)
    logger.debug("Using verbose flag: %s", verbose)

    output_dir: Path = parsed_args.output_dir
    output_dir = output_dir.resolve()
    logger.debug("Using output directory: %r", str(output_dir))

    multi_threaded: bool = parsed_args.multi_threaded
    logger.debug("Using multi threading flag: %s", multi_threaded)

    exit_code: Union[int, str] = 0
    try:
        command: str = parsed_args.command
        logger.debug("Using command: %s", command)
        if command == "extract":
            from stubgen.extract_stubs import extract_assembly

            use_all: bool = parsed_args.all
            use_built_in: bool = parsed_args.built_in
            use_core: bool = parsed_args.core

            skip_failed: bool = parsed_args.skip_failed
            logger.debug("Using skip failed flag: %s", skip_failed)

            paths: Sequence[Path] = parsed_args.path
            if paths is not None:
                path: Path
                for path in paths:
                    path_str: str = str(path.resolve())
                    logger.debug("Adding to sys.path: %r", path_str)
                    sys.path.append(path_str)

            overwrite: bool = parsed_args.overwrite
            logger.debug("Using overwrite flag: %s", skip_failed)

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

            exit_code = extract_assemblies(
                assembly_names=assembly_names,
                output_dir=output_dir,
                overwrite=overwrite,
                skip_failed=skip_failed,
                multi_threaded=multi_threaded,
            )
        elif command == "build":
            from stubgen.build_stubs import build_stubs

            line_length: int = parsed_args.line_length
            logger.debug("Using line length: %s", line_length)

            format_files: bool = parsed_args.format_files
            logger.debug("Using format files flag: %s", format_files)

            skeleton_glob: str = parsed_args.skeletons
            skeleton_files: List[Path] = []
            for file_path in Path().glob(skeleton_glob):
                skeleton_files.append(file_path)
                logger.debug("Using skeleton file: %r", str(file_path))

            doc_glob: str = parsed_args.docs
            doc_files: List[Path] = []
            for file_path in Path().glob(doc_glob):
                doc_files.append(file_path)
                logger.debug("Using doc file: %r", str(file_path))

            exit_code = build_stubs(
                skeleton_files=skeleton_files,
                doc_files=doc_files,
                output_dir=output_dir,
                line_length=line_length,
                multi_threaded=multi_threaded,
                format_files=format_files,
            )

    except Exception as e:
        logger.exception("An unhandled exception occurred:", exc_info=e)
        exit_code = str(e)

    return exit_code


if __name__ == "__main__":
    args: Sequence[str] = sys.argv[1:]

    result: Union[int, str] = main(*args)

    sys.exit(result)
