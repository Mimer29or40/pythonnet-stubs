import sys
from dataclasses import asdict

from .defaults import ASSEMBLIES, BUILT_INS, CORE
from .logging import logger
from .make_stubs import make, group
from .options import options
from .util import time_it

for k, v in asdict(options).items():
    logger.debug(f'Argument: {k}=\'{v}\'')

# Add Paths from Options
sys.path.extend(options.path_dirs)

for p in sys.path:
    logger.debug(f'Path Variable: \'{p}\'')

if options.make:
    assemblies = []
    if options.all:
        assemblies.extend(BUILT_INS)
        assemblies.extend(ASSEMBLIES)
    elif options.built_in:
        assemblies.extend(BUILT_INS)
    elif options.core:
        assemblies.extend(CORE)
    else:
        assemblies.append(options.assembly_name)
    
    for a in assemblies:
        logger.debug(f'Assembly: \'{a}\'')
    
    with time_it('main', log_func=logger.info):
        for assembly_name in assemblies:
            logger.info('=' * 80)
            logger.info(f'Making [{assembly_name}]')
            make(assembly_name)

if options.group:
    assemblies = []
    if options.all:
        assemblies.extend(BUILT_INS)
        assemblies.extend(ASSEMBLIES)
    else:
        if options.built_in:
            assemblies.extend(BUILT_INS)
        elif options.core:
            assemblies.extend(CORE)
    
    assemblies.extend(options.assembly_names)
    
    for a in assemblies:
        logger.debug(f'Assembly: \'{a}\'')
    
    group(assemblies)
