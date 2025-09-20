from clients.authentication.authentication_schema import LoginResponseSchema
from clients.errors_schema import ErrorResponseSchema

from tools.assertions.errors import assert_error_response
from tools.assertions.base import assert_is_true


def assert_login_response(response: LoginResponseSchema):
    """
    Проверяет корректность ответа при успешной авторизации.

    :param response: Объект ответа с токенами авторизации.
    :raises AssertionError: Если какое-либо из условий не выполняется.
    """
    assert_is_true(response.access_token, "access_token")
    assert_is_true(response.refresh_token, "refresh_token")


def assert_login_invalid_credentials(actual: ErrorResponseSchema):
    """
    Проверяет, что ответ на авторизацию с некорректными данными соответствует ожидаемой ошибке.

    :param actual: Ответ от API с ошибкой, которую необходимо проверить.
    :raises AssertionError: Если фактический ответ не соответствует ожидаемому.
    """
    expected = ErrorResponseSchema(
        message="Unauthorized",
        status_code=401
    )
    assert_error_response(actual, expected)

