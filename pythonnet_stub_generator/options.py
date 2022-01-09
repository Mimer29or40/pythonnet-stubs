from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Optional, Tuple, Any, Dict

__default_path__ = 'stubs'
__version__ = '0.0.1'
__doc__ = f"""
    Stub Generator | {__version__}
    
    Python.NET Stub Generator
    
    Usage:
      stub-generator make (<assembly-name>|--all|--built_in|--core) [options]
      stub-generator minify <folder> [options]
      stub-generator (-h | --help)
      stub-generator (-V | --version)
    
    Examples:
      ipy -m stub-generator make System.Reflection --overwrite
    
    Options:
        <assembly-name>         Name of Dll Assembly to Process
        --all                   Process All Assemblies in defaults.py
        --built_in              Process All Built-In Assemblies in defaults.py
        --core                  Process All Core Assemblies in defaults.py

        --output=<dir>          Name of Output Directory [default: {__default_path__}]
        --paths=<dir>...        Additional Directory to add to Path [default:]
        --overwrite             Force Overwrite if stub already exists [default: False].
        --no-json               Disables Json Log

        -h --help               Show this help
        -V --version            Show version
    
"""


@dataclass
class Options:
    make: bool
    assembly_name: Optional[str]
    all: bool
    built_in: bool
    core: bool
    output_dir: Path
    path_dirs: Tuple[str, ...]
    json: bool
    overwrite: bool
    
    @classmethod
    def version(cls) -> str:
        return __version__
    
    @classmethod
    def doc_str(cls) -> str:
        return __doc__
    
    @classmethod
    def get(cls, arguments: Dict[str, Any]) -> Options:
        return cls(
            arguments['make'],
            arguments['<assembly-name>'],
            arguments['--all'],
            arguments['--built_in'],
            arguments['--core'],
            Path(arguments['--output']),
            tuple() if arguments['--paths'] is None else tuple(arguments['--paths']),
            not arguments['--no-json'],
            arguments['--overwrite'],
        )
