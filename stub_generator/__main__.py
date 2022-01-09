import sys

from docopt import docopt

from .defaults import ASSEMBLIES, BUILT_INS
from .logging import logger
from .make_stubs import make
from .options import Options
from .util import time_it

__version__ = Options.version()
__doc__ = Options.doc_str()

arguments = docopt(__doc__, version=__version__)

options: Options = Options.get(arguments)

if options.debug:
    logger.enable_debug()

# Add Paths from Options
sys.path.extend(options.path_dirs)

assemblies = []
if options.all:
    assemblies.extend(ASSEMBLIES)
    assemblies.extend(BUILT_INS)
elif options.built_in:
    assemblies.extend(BUILT_INS)
else:
    assemblies.append(options.assembly_name)

for p in sys.path:
    logger.debug(f'Path Variable: \'{p}\'')
for k, v in arguments.items():
    logger.debug(f'Argument: {k}=\'{v}\'')
for a in assemblies:
    logger.debug(f'Assembly: \'{a}\'')

if options.make:
    with time_it('main', log_func=logger.info):
        for assembly_name in assemblies:
            logger.info('=' * 80)
            logger.info(f'Making [{assembly_name}]')
            make(assembly_name, options)
