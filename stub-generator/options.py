from dataclasses import dataclass
from pathlib import Path
from typing import Optional, Tuple

__default_path__ = 'stubs'
__version__ = '0.0.1'
__doc__ = f"""
    Stub Generator | {__version__}
    
    Python.NET Stub Generator
    
    Usage:
      stub-generator make (<assembly-name>|--all) [options]
      stub-generator minify <folder> [options]
      stub-generator (-h | --help)
      stub-generator (-V | --version)
    
    Examples:
      ipy -m stub-generator System.Reflection --overwrite
    
    Options:
        <assembly-name>         Name of Dll Assembly to load
        --all                   Process all Assemblies in defaults.py

        --output=<dir>          Name of Output Directory [default: {__default_path__}]
        --paths=<dir>...        Additional Directory to add to Path [default:]
        --overwrite             Force Overwrite if stub already exists [default: False].
        --no-json               Disables Json Log
        --debug                 Enables Debug Messages

        -h --help               Show this help
        -V --version            Show version
    
"""


@dataclass
class Options:
    assembly_name: Optional[str]
    all: bool
    output_dir: Path
    path_dirs: Tuple[str]
    json: bool
    overwrite: bool
    debug: bool
    
    @classmethod
    def version(cls) -> str:
        return __version__
    
    @classmethod
    def doc_str(cls) -> str:
        return __doc__
