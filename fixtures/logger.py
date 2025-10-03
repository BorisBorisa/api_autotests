import sys

import pytest
import allure

from io import StringIO
from loguru import logger

FORMAT = "<w><g>{time:YY-MM-DD HH:mm:ss}</g> | <y>{level:^8}</y> | <m>{extra[name]:^25}</m> | <c>{message}</c></w>"


@pytest.fixture(autouse=True, scope="session")
def setup_global_logger():
    logger.remove()
    logger.add(sys.stderr, format=FORMAT, colorize=True)


@pytest.fixture(autouse=True)
def attach_logs_to_allure():
    log_stream = StringIO()
    handler_id = logger.add(log_stream, format=FORMAT)

    try:
        yield
    finally:
        logger.remove(handler_id)
        allure.attach(log_stream.getvalue(), name="logs", attachment_type=allure.attachment_type.TEXT)
