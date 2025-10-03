import pytest
import allure

from io import StringIO
from loguru import logger

from tools.logger import logger_init, FORMAT


@pytest.fixture(autouse=True, scope="session")
def initialize_logger():
    logger_init()

@allure.title("Logs")
@pytest.fixture(autouse=True)
def loguru_to_allure():
    """
    Фикстура, которая автоматически прикрепляет логи loguru к каждому тесту в Allure.
    """
    log_stream = StringIO()
    handler_id = logger.add(log_stream, format=FORMAT, level="DEBUG", colorize=False)

    yield

    allure.attach(
        log_stream.getvalue(),
        name="loguru_logs",
        attachment_type=allure.attachment_type.TEXT
    )

    logger.remove(handler_id)
