import sys
from typing import Optional, List

from docopt import docopt

from .defaults import ASSEMBLIES, DEFAULT_OUTPUT_PATH, PATHS
from .logger import logger
from .make_stubs import dump_json_log, make
from .util import time_it

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
      ipy -m stub-generator RhinoCommon --overwrite
    
    Options:
        <assembly-name>         Name of Dll Assembly to load
        --all                   Process all Assemblies in defaults.py

        --output=<dir>          Name of Output Directory [default: {DEFAULT_OUTPUT_PATH}]
        --paths=<dir>...        Additional Directory to add to Path [default:]
        --overwrite             Force Overwrite if stub already exists [default: False].
        --no-json               Disables Json Log
        --debug                 Enables Debug Messages

        -h --help               Show this help
        -V --version            Show version
    
"""

arguments = docopt(__doc__, version=__version__)

# OPTIONS
option_assembly_name: Optional[str] = arguments['<assembly-name>']
option_all: bool = arguments['--all']

option_output_dir: str = arguments['--output']
option_path_dirs: Optional[List[str]] = arguments['--paths']
option_json: bool = not arguments['--no-json']
option_overwrite: bool = arguments['--overwrite']
option_debug: bool = arguments['--debug']

print(f'option_assembly_name={option_assembly_name}')
print(f'option_all={option_all}')

print(f'option_output_dir={option_output_dir}')
print(f'option_path_dirs={option_path_dirs}')
print(f'option_json={option_json}')
print(f'option_overwrite={option_overwrite}')
print(f'option_debug={option_debug}')

if option_debug:
    logger.enable_debug()

# PROJECT_DIR = os.getcwd()  # Must execute from project dir
# PKG_DIR = os.path.dirname(__file__)
# PROJECT_DIR = os.path.dirname(PKG_DIR)
# release_dir = os.path.join(PROJECT_DIR, 'release', option_output_dir)
# os.chdir(PROJECT_DIR)

# Add Paths
sys.path.extend(PATHS)

# Additional Paths from Options
if option_path_dirs is not None:
    sys.path.extend(option_path_dirs)

logger.debug(sys.path)
logger.debug(arguments)
logger.debug(ASSEMBLIES)

if arguments['make']:
    with time_it('main', log_func=logger.info):
        if not option_all:
            ASSEMBLIES = [option_assembly_name]
        
        for assembly_name in ASSEMBLIES:
            print(assembly_name)
            assembly_dict = make(option_output_dir, assembly_name, overwrite=option_overwrite, quiet=option_all)
            if option_json:
                dump_json_log(assembly_dict)
