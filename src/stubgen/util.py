import functools
import re
import time
from contextlib import contextmanager
from pathlib import Path
from typing import Callable

import clr
from System import Nullable
from System import Type
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


def make_ref_type(type: Type) -> Type:
    return clr.Reference[type]


def make_nullable(type: Type) -> "Nullable[Type]":
    return Nullable[type]


def make_python_name(string: str) -> str:
    if "[" in string:
        string = string[: string.index("[")]
    string = make_python_name.pattern.sub("", string)
    if string in reserved_python_names:
        return f"_{string}"
    return string


make_python_name.pattern = re.compile(r"`\d+|&|\[|]|\*")


def strip_path_str(string: str) -> str:
    return strip_path_str.pattern.sub("", string)


strip_path_str.pattern = re.compile(r'[<>:"/\\|?*]')


def rm_tree(path: Path):
    for child in path.glob("*"):
        if child.is_file():
            child.unlink()
        else:
            rm_tree(child)
    path.rmdir()


reserved_python_names = [
    "and",
    "as",
    "assert",
    "break",
    "class",
    "continue",
    "def",
    "del",
    "elif",
    "else",
    "except",
    "False",
    "finally",
    "for",
    "from",
    "global",
    "if",
    "import",
    "in",
    "is",
    "lambda",
    "None",
    "nonlocal",
    "not",
    "or",
    "pass",
    "raise",
    "return",
    "True",
    "try",
    "while",
    "with",
    "yield",
]
