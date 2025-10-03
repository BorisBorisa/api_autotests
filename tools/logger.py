import sys

from loguru import logger
from loguru._logger import Logger

FORMAT = "<w><g>{time:YY-MM-DD HH:mm:ss}</g> | <y>{level:^8}</y> | <m>{extra[name]:^25}</m> | <c>{message}</c></w>"


def logger_init():
    logger.remove()
    logger.add(sys.stderr, format=FORMAT, colorize=True)


def get_logger(name: str) -> Logger:
    return logger.bind(name=name)
