"""Handles creating loggers for the module."""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING

if TYPE_CHECKING:  # pragma: no cover
    from logging import Formatter
    from logging import Handler
    from logging import Logger

root_formatter: Formatter | None = None
root_handler: Handler | None = None
root_logger: Logger | None = None


def _init_root_logger() -> None:
    import sys

    import stubgen

    global root_formatter
    global root_handler
    global root_logger

    root_formatter = logging.Formatter(
        fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %I:%M:%S",
        style="%",
        validate=True,
    )

    root_handler = logging.StreamHandler(stream=sys.stdout)
    root_handler.setFormatter(root_formatter)
    root_handler.setLevel(logging.INFO)

    root_logger = logging.getLogger(stubgen.__name__)
    root_logger.propagate = True
    root_logger.setLevel(logging.DEBUG)
    root_logger.handlers = [root_handler]


def get_logger(name: str) -> Logger:
    """Get a Logger object whose parent is the root logger.

    This is typically called once per file with name being __name__.

    :param name: The name of the logger, usually __name__.
    :return: The Logger object.
    """
    if root_logger is None:
        _init_root_logger()
    logger = logging.getLogger(name)
    if logger is not root_logger:
        logger.parent = root_logger
    return logger
