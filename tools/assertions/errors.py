from clients.errors_schema import ErrorResponseSchema
from tools.assertions.base import assert_equal


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
