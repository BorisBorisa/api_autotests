import sys

from loguru import logger
from loguru._logger import Logger

from config import settings


def logger_init():
    logger.remove()
    logger.add(
        sys.stderr,
        format=settings.logger.format,
        colorize=True
    )
    logger.add(
        settings.logger.path,
        format=settings.logger.format,
        rotation=settings.logger.rotation,
        retention=settings.logger.retention
    )


def get_logger(name: str) -> Logger:
    return logger.bind(name=name)
