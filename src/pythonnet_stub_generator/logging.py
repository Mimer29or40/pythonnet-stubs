import logging.config
from pathlib import Path

log_dir = Path('logs')
log_dir.mkdir(exist_ok=True)

log_file = log_dir / 'stub-generator.log'
debug_log_file = log_dir / 'stub-generator-debug.log'

logger_config = {
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
        'console':    {
            'class':     'logging.StreamHandler',
            'level':     'INFO',
            'formatter': 'simple',
            'filters':   ['none'],
            # 'stream':    'ext://sys.stdout',
        },
        'file':       {
            'class':       'logging.handlers.RotatingFileHandler',
            'level':       'INFO',
            'formatter':   'simple',
            'filters':     ['none'],
            'filename':    str(log_file.absolute()),
            'maxBytes':    1024 * 1024 * 2,
            'backupCount': 5,
        },
        'file-debug': {
            'class':       'logging.handlers.RotatingFileHandler',
            'level':       'DEBUG',
            'formatter':   'simple',
            'filters':     ['none'],
            'filename':    str(debug_log_file.absolute()),
            'maxBytes':    1024 * 1024 * 20,
            'backupCount': 5,
        },
    },
    'loggers':                  {
        'stubs': {
            'level':     'DEBUG',
            'propagate': False,
            'filters':   ['none'],
            'handlers':  ['console', 'file', 'file-debug'],
        },
    },
    # 'root':                     {
    #     'class':     '',
    #     'level':     'INFO',
    #     'formatter': 'simple',
    #     'filters':   ['none'],
    # },
}

logging.config.dictConfig(logger_config)

logger = logging.getLogger('stubs')

__all__ = [
    logger
]
