import allure

from clients.errors_schema import ErrorResponseSchema
from tools.assertions.base import assert_equal


@allure.step("Check error response")
def assert_error_response(
        actual: ErrorResponseSchema,
        expected: ErrorResponseSchema
):
    """
    Проверяет, что объект ответа API с ошибками валидации (`ErrorResponseSchema`)
    соответствует ожидаемому значению.

    :param actual: Фактический ответ API.
    :param expected: Ожидаемый ответ API.
    :raises AssertionError: Если значения полей не совпадают.
    """

    assert_equal(actual.status_code, expected.status_code, "status_code")
    assert_equal(actual.error, expected.error, "error")
    assert_equal(actual.message, expected.message, "message")


@allure.step("Check error response for invalid data request")
def assert_invalid_data_response(actual: ErrorResponseSchema, error_messages: list):
    """
    Проверяет, что объект ответа API с ошибками валидации (`ErrorResponseSchema`)
    при запросе с невалидными данными соответствует ожидаемому значению.

    :param actual: Фактический ответ API.
    :param error_messages: Ожидаемые сообщения об ошибках.
    :raises AssertionError: Если значения полей не совпадают.
    """
    expected = ErrorResponseSchema(
        message=error_messages,
        error="Bad Request",
        status_code=400
    )
    assert_error_response(actual, expected)
