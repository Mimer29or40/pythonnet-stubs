import functools
import time
from contextlib import contextmanager
from typing import Callable

from .logger import logger


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
