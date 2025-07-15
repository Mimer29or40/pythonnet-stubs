from __future__ import annotations

import functools
import keyword
import re
import time
from collections.abc import Callable
from contextlib import contextmanager
from pathlib import Path

from stubgen.log import get_logger

logger = get_logger(__name__)


@contextmanager
def time_it(name: str, log_func: Callable = logger.debug):
    log_func(f"Starting Timer: {name}")
    start_time = time.time()
    try:
        yield
    finally:
        duration = time.time() - start_time
        log_func(f"Timer Finished: {name} - {duration} sec")


def time_function(func=None, *, log_func: Callable = logger.debug):
    def decorator(_func):
        @functools.wraps(_func)
        def wrapper(*args, **kwargs):
            log_func(f"Timing Function: {_func.__name__}")
            start_time = time.time()
            return_value = _func(*args, **kwargs)
            duration = time.time() - start_time
            log_func(f"Function Finished: {_func.__name__} - {duration} sec")
            return return_value

        return wrapper

    return decorator if func is None else decorator(func)


def is_name_valid(name: str) -> bool:
    if "." in name:
        return all(map(is_name_valid, name.split(".")))
    return name.isidentifier() and not keyword.iskeyword(name)


def make_python_name(string: str) -> str:
    if "[" in string:
        string = string[: string.index("[")]
    string = make_python_name.pattern.sub("", string)
    if keyword.iskeyword(string):
        return f"_{string}"
    return string


make_python_name.pattern = re.compile(r"`\d+|&|\[|]|\*|<|>")


def rm_tree(path: Path):
    for child in path.glob("*"):
        if child.is_file():
            child.unlink()
        else:
            rm_tree(child)
    path.rmdir()
