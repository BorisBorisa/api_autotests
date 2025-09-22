from clients.authentication.authentication_schema import LoginResponseSchema, RefreshTokenResponseSchema
from clients.errors_schema import ErrorResponseSchema
from clients.users.users_schema import CreateUserResponseSchema, UserProfileResponseSchema

from tools.assertions.errors import assert_error_response
from tools.assertions.base import assert_is_true
from tools.assertions.users import assert_user


def assert_tokens_present(response):
    """
    Проверяет, что в ответе присутствуют access и refresh токены.

    :param response: Объект ответа, содержащий токены авторизации.
    :raises AssertionError: Если какое-либо из условий не выполняется.
    """
    assert_is_true(response.access_token, "access_token")
    assert_is_true(response.refresh_token, "refresh_token")


def assert_login_response(response: LoginResponseSchema):
    """
    Проверяет корректность ответа при успешной авторизации.

    :param response: Объект ответа с токенами авторизации.
    :raises AssertionError: Если какое-либо из условий не выполняется.
    """
    assert_tokens_present(response)


def assert_refresh_response(response: RefreshTokenResponseSchema):
    """
    Проверяет корректность ответа при обновлении токенов доступа.

    :param response: Объект ответа с токенами авторизации.
    :raises AssertionError: Если какое-либо из условий не выполняется.
    """
    assert_tokens_present(response)


def assert_login_invalid_credentials_response(actual: ErrorResponseSchema):
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


def assert_user_profile_response_matches(
        actual: UserProfileResponseSchema,
        expected: CreateUserResponseSchema
):
    """
    Проверяет, что данные профиля пользователя из ответа API совпадают с ожидаемыми данными созданного пользователя.

    :param actual: Данные профиля из API.
    :param expected: Данные пользователя после создания.
    :return: AssertionError: Если хотя бы одно поле не совпадает.
    :return:
    """
    assert_user(actual, expected)


def assert_refresh_with_invalid_token_response(actual: ErrorResponseSchema):
    """
    Проверяет, что ответ на авторизацию с некорректными данными соответствует ожидаемой ошибке.

    :param actual: Ответ от API с ошибкой, которую необходимо проверить.
    :raises AssertionError: Если фактический ответ не соответствует ожидаемому.
    """
    expected = ErrorResponseSchema(
        message="Invalid",
        error="Unauthorized",
        status_code=401
    )
    assert_error_response(actual, expected)
