import sys
from pathlib import Path

from docopt import docopt

from .defaults import ASSEMBLIES, PATHS
from .logger import logger
from .make_stubs import make
from .options import Options
from .util import time_it

__version__ = Options.version()
__doc__ = Options.doc_str()

arguments = docopt(__doc__, version=__version__)

options: Options = Options(
    arguments['<assembly-name>'],
    arguments['--all'],
    Path(arguments['--output']),
    tuple() if arguments['--paths'] is None else tuple(arguments['--paths']),
    not arguments['--no-json'],
    arguments['--overwrite'],
    arguments['--debug'],
)

if options.debug:
    logger.enable_debug()

# Add Paths
sys.path.extend(PATHS)

# Additional Paths from Options
sys.path.extend(options.path_dirs)

logger.debug(sys.path)
logger.debug(arguments)
logger.debug(ASSEMBLIES)

if arguments['make']:
    with time_it('main', log_func=logger.info):
        if not options.all:
            ASSEMBLIES = [options.assembly_name]
        
        for assembly_name in ASSEMBLIES:
            make(assembly_name, options)
