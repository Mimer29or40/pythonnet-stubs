import logging
import sys

formatter = logging.Formatter(
    fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %I:%M:%S",  # yyyy-MM-dd HH:mm:ss
    style="%",
    validate=True,
)

console_handler = logging.StreamHandler(stream=sys.stdout)
console_handler.setFormatter(formatter)
console_handler.setLevel(logging.INFO)

root_logger = logging.getLogger("stubgen")
root_logger.propagate = True
root_logger.setLevel(logging.DEBUG)
root_logger.handlers = [console_handler]


def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.parent = root_logger
    return logger
