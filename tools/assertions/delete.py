import allure

from tools.logger import get_logger

logger = get_logger("DELETE_ASSERTIONS")


@allure.step("Check delete response")
def assert_delete_response(response: bool):
    """
    Проверяет, что ответ на удаление успешный.

    :param response: Ответ API
    :return: AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info("Check delete response")

    assert response, "Expected delete response to be True, but got False"
