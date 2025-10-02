import pytest
from tools.logger import logger_init


@pytest.fixture(autouse=True, scope="session")
def initialize_logger():
    logger_init()
