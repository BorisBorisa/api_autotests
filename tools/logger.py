from loguru import logger
from loguru._logger import Logger


def get_logger(name: str) -> Logger:
    return logger.bind(name=name)
