import allure

from clients.authentication.authentication_schema import LoginResponseSchema, RefreshTokenResponseSchema
from clients.errors_schema import ErrorResponseSchema
from clients.users.users_schema import CreateUserResponseSchema, UserProfileResponseSchema

from tools.assertions.errors import assert_error_response
from tools.assertions.base import assert_is_true
from tools.assertions.users import assert_user
from tools.logger import get_logger

logger = get_logger("AUTHENTICATION_ASSERTIONS")


@allure.step("Check response contains both access and refresh tokens")
def assert_tokens_present(response):
    """
    Проверяет, что в ответе присутствуют access и refresh токены.

    :param response: Объект ответа, содержащий токены авторизации.
    :raises AssertionError: Если какое-либо из условий не выполняется.
    """
    logger.info("Check response contains both access and refresh tokens")

    assert_is_true(response.access_token, "access_token")
    assert_is_true(response.refresh_token, "refresh_token")


@allure.step("Check login response")
def assert_login_response(response: LoginResponseSchema):
    """
    Проверяет корректность ответа при успешной авторизации.

    :param response: Объект ответа с токенами авторизации.
    :raises AssertionError: Если какое-либо из условий не выполняется.
    """
    logger.info("Check login response")

    assert_tokens_present(response)


@allure.step("Check refresh tokens response")
def assert_refresh_response(response: RefreshTokenResponseSchema):
    """
    Проверяет корректность ответа при обновлении токенов доступа.

    :param response: Объект ответа с токенами авторизации.
    :raises AssertionError: Если какое-либо из условий не выполняется.
    """
    logger.info("Check refresh tokens response")

    assert_tokens_present(response)


@allure.step("Check refresh tokens response")
def assert_login_invalid_credentials_response(actual: ErrorResponseSchema):
    """
    Проверяет, что ответ на авторизацию с некорректными данными соответствует ожидаемой ошибке.

    :param actual: Ответ от API с ошибкой, которую необходимо проверить.
    :raises AssertionError: Если фактический ответ не соответствует ожидаемому.
    """
    logger.info("Check refresh tokens response")

    expected = ErrorResponseSchema(
        message="Unauthorized",
        status_code=401
    )
    assert_error_response(actual, expected)


@allure.step("Check user profile response matches the created user data")
def assert_user_profile_response_matches(
        actual: UserProfileResponseSchema,
        expected: CreateUserResponseSchema
):
    """
    Проверяет, что данные профиля пользователя из ответа API совпадают с ожидаемыми данными созданного пользователя.

    :param actual: Данные профиля из API.
    :param expected: Данные пользователя после создания.
    :raises: AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info("Check user profile response matches the created user data")

    assert_user(actual, expected)


@allure.step("Check refresh response with an invalid token")
def assert_refresh_with_invalid_token_response(actual: ErrorResponseSchema):
    """
    Проверяет, что ответ на авторизацию с некорректными данными соответствует ожидаемой ошибке.

    :param actual: Ответ от API с ошибкой, которую необходимо проверить.
    :raises AssertionError: Если фактический ответ не соответствует ожидаемому.
    """
    logger.info("Check refresh response with an invalid token")

    expected = ErrorResponseSchema(
        message="Invalid",
        error="Unauthorized",
        status_code=401
    )
    assert_error_response(actual, expected)
