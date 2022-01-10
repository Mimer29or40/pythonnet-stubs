from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Optional, Tuple

__version__ = '1.1.0'
__doc__ = f"""
    Stub Generator | {__version__}
    
    Python.NET Stub Generator
    
    Usage:
      pythonnet_stub_generator make (<assembly-name>|--all|--built_in|--core) [options]
      pythonnet_stub_generator group [<assembly-names>...] [--all|--built_in|--core] [options]
      pythonnet_stub_generator minify <folder> [options]
      pythonnet_stub_generator (-h | --help)
      pythonnet_stub_generator (-V | --version)
    
    Examples:
      ipy -m pythonnet_stub_generator make System.Reflection --overwrite
    
    Options:
        <assembly-name>         Name of Dll Assembly to Process
        <assembly-names>...     Names of Dll Assemblies to Process
        
        --all                   Process All Assemblies in defaults.py
        --built_in              Process All Built-In Assemblies in defaults.py
        --core                  Process All Core Assemblies in defaults.py

        --output=<dir>          Name of Output Directory [default: stubs]
        --paths=<dir>...        Additional Directory to add to Path [default:]
        --overwrite             Force Overwrite if stub already exists [default: False].
        --no-json               Disables Json Log

        -h --help               Show this help
        -V --version            Show version
    
"""

from docopt import docopt


@dataclass
class Options:
    make: bool
    group: bool
    
    assembly_name: Optional[str]
    assembly_names: Tuple[str, ...]
    
    all: bool
    built_in: bool
    core: bool
    
    output_dir: Path
    path_dirs: Tuple[str, ...]
    json: bool
    overwrite: bool


arguments = docopt(__doc__, version=__version__)

options = Options(
    arguments['make'],
    arguments['group'],
    arguments['<assembly-name>'],
    tuple() if arguments['<assembly-names>'] is None else tuple(arguments['<assembly-names>']),
    arguments['--all'],
    arguments['--built_in'],
    arguments['--core'],
    Path(arguments['--output']),
    tuple() if arguments['--paths'] is None else tuple(arguments['--paths'].split(sep=',')),
    not arguments['--no-json'],
    arguments['--overwrite'],
)

__all__ = [
    options
]
