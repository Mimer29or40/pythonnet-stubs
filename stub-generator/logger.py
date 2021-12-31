import logging
from logging.config import dictConfig
from pathlib import Path

log_dir = Path('logs')
log_dir.mkdir(exist_ok=True)

log_file = log_dir / 'log.log'

LOGGER_CONFIG = {
    'version':                  1,
    'disable_existing_loggers': True,
    'handlers':                 {
        'console':      {
            'class':     'logging.StreamHandler',
            'formatter': 'simple',
        },
        'file_handler': {
            'class':     'logging.FileHandler',
            'formatter': 'simple',
            'filename':  log_file,
        },
    },
    'formatters':               {
        'simple': {
            'format':  '%(asctime)s [%(thread)d] %(levelname)s - %(name)s - %(message)s',
            'datefmt': '%Y-%m-%d %I:%M:%S'  # yyyy-MM-dd HH:mm:ss,SSS
        }
    },
    'loggers':                  {
        "": {
            'handlers': ['console', 'file_handler'],
            'level':    'INFO'
        }
    }
}

log_levels = {
    50: 'CRITICAL',
    40: 'ERROR',
    30: 'WARNING',
    20: 'INFO',
    10: 'DEBUG',
    0:  'NOTSET'
}

dictConfig(LOGGER_CONFIG)
logger = logging.getLogger()
logger.debug('** LOG LEVEL: {}'.format(log_levels[logger.getEffectiveLevel()]))


def enable_debug():
    logger.setLevel(logging.DEBUG)


logger.enable_debug = enable_debug
