import logging.config
from pathlib import Path

LOG_DIR = Path('logs')
LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / 'stub-generator.log'

DEFAULT_LOGGER_CONFIG = {
    'version':                  1,
    'disable_existing_loggers': True,
    'incremental':              False,
    'formatters':               {
        'simple': {
            'format':   '%(asctime)s [%(thread)d] %(levelname)s - %(name)s - %(message)s',
            'datefmt':  '%Y-%m-%d %I:%M:%S',  # yyyy-MM-dd HH:mm:ss,SSS
            'style':    '%',
            'validate': True,
        }
    },
    'filters':                  {
        'none': {
            'name': '',
        },
    },
    'handlers':                 {
        'console': {
            'class':     'logging.StreamHandler',
            'level':     'INFO',
            'formatter': 'simple',
            'filters':   ['none'],
            # 'stream':    'ext://sys.stdout',
        },
        'file':    {
            'class':       'logging.handlers.RotatingFileHandler',
            'level':       'DEBUG',
            'formatter':   'simple',
            'filters':     ['none'],
            'filename':    str(LOG_FILE.absolute()),
            'maxBytes':    1024 * 1024 * 2,
            'backupCount': 5,
        },
    },
    'loggers':                  {
        '': {
            'level':     'DEBUG',
            'propagate': False,
            'filters':   ['none'],
            'handlers':  ['console', 'file'],
        },
    },
    # 'root':                     {
    #     'class':     '',
    #     'level':     'INFO',
    #     'formatter': 'simple',
    #     'filters':   ['none'],
    # },
}

logging.config.dictConfig(DEFAULT_LOGGER_CONFIG)

logger = logging.getLogger()

__all__ = [
    logger
]
