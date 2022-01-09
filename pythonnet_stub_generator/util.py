import functools
import re
import time
from contextlib import contextmanager
from typing import Callable

from .logging import logger


@contextmanager
def time_it(name: str, log_func: Callable = logger.debug):
    log_func(f'Starting Timer: {name}')
    start_time = time.time()
    try:
        yield
    finally:
        duration = time.time() - start_time
        log_func(f'Timer Finished: {name} - {duration} sec')


def time_function(func=None, *, log_func: Callable = logger.debug):
    def decorator(_func):
        @functools.wraps(_func)
        def wrapper(*args, **kwargs):
            log_func(f'Timing Function: {_func.__name__}')
            start_time = time.time()
            return_value = _func(*args, **kwargs)
            duration = time.time() - start_time
            log_func(f'Function Finished: {_func.__name__} - {duration} sec')
            return return_value
        
        return wrapper
    
    return decorator if func is None else decorator(func)


def make_python_name(string: str) -> str:
    if '[' in string:
        string = string[:string.index('[')]
    string = make_python_name.pattern.sub('', string)
    if string in reserved_python_names:
        return f'_{string}'
    return string


def strip_path_str(string: str) -> str:
    return strip_path_str.pattern.sub('', string)


make_python_name.pattern = re.compile(r'`\d+|&|\[|]|\*')
strip_path_str.pattern = re.compile(r'[<>:"/\\|?*]')
reserved_python_names = [
    'False', 'def', 'if', 'raise',
    'None', 'del', 'import', 'return',
    'True', 'elif', 'in', 'try',
    'and', 'else', 'is', 'while',
    'as', 'except', 'lambda', 'with',
    'assert', 'finally', 'nonlocal', 'yield',
    'break', 'for', 'not', 'class',
    'from', 'or', 'continue', 'global', 'pass',
]
