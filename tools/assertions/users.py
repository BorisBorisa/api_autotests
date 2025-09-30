from clients.errors_schema import ErrorResponseSchema
from clients.users.users_schema import (
    UserSchema,
    CreateUserRequestSchema,
    CreateUserResponseSchema,
    UserNotFoundResponseSchema,
    UpdateUserRequestSchema,
    UpdateUserResponseSchema,
    EmailAvailabilityResponseSchema
)
from tools.assertions.base import assert_equal
from tools.assertions.errors import assert_error_response

from tools.routes import APIRoutes


def assert_user(actual: UserSchema, expected: UserSchema):
    """
    Проверяет корректность данных пользователя.

    :param actual: Фактические данные пользователя.
    :param expected: Ожидаемые данные пользователя.
    :return: AssertionError: Если хотя бы одно поле не совпадает.
    """

    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.name, expected.name, "name")
    assert_equal(actual.role, expected.role, "role")
    assert_equal(actual.email, expected.email, "email")
    assert_equal(actual.password, expected.password, "password")
    assert_equal(actual.avatar, expected.avatar, "avatar")


def assert_create_user_response(request: CreateUserRequestSchema, response: CreateUserResponseSchema):
    """
    Проверяет, что ответ на создание пользователя соответствует запросу.

    :param request: Исходный запрос на создание пользователя.
    :param response: Ответ API с данными пользователя.
    :return: AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(request.name, response.name, "name")
    assert_equal(request.email, response.email, "email")
    assert_equal(request.password, response.password, "password")
    assert_equal(request.avatar, str(response.avatar), "avatar")


def assert_create_user_with_wrong_data_response(actual: ErrorResponseSchema, error_messages: list):
    """
    Проверяет, что ответ на регистрацию пользователя с некорректным данными соответствует ожидаемому.

    :param actual: Ответ от API с ошибкой, которую необходимо проверить.
    :param error_messages: Список сообщений ошибок.
    :raises AssertionError: Если фактический ответ не соответствует ожидаемому.
    """
    expected = ErrorResponseSchema(
        message=error_messages,
        error="Bad Request",
        status_code=400
    )
    assert_error_response(actual, expected)


def assert_get_user_with_wrong_id_response(actual: UserNotFoundResponseSchema, user_id: int):
    """
    Проверяет, что ответ на получение пользователя с некорректным user_id соответствует ожидаемому.

    :param actual: Ответ от API с ошибкой, которую необходимо проверить.
    :param user_id: Идентификатор пользователя.
    :return: AssertionError: Если фактический ответ не соответствует ожидаемому.
    """
    assert_equal(actual.path, f"/{APIRoutes.USERS}/{user_id}", "path")
    assert_equal(actual.name, "EntityNotFoundError", "error name")
    assert_equal(
        actual.message,
        f"Could not find any entity of type \"User\" matching: {{\n    \"id\": {user_id}\n}}",
        "message"
    )


def assert_update_user_response(request: UpdateUserRequestSchema, response: UpdateUserResponseSchema):
    """
    Проверяет, что ответ на обновление данных пользователя соответствует запросу.

    :param request: Исходные данные обновления пользователя.
    :param response: Ответ API с данными пользователя.
    :return: AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(request.name, response.name, "name")
    assert_equal(request.role, response.role, "role")
    assert_equal(request.email, response.email, "email")
    assert_equal(request.password, response.password, "password")
    assert_equal(request.avatar, str(response.avatar), "avatar")


def assert_update_user_with_wrong_data_response(actual: ErrorResponseSchema, error_messages: list):
    """
    Проверяет, что ответ на обновление данных пользователя с некорректным данными соответствует ожидаемому.

    :param actual: Ответ от API с ошибкой, которую необходимо проверить.
    :param error_messages: Список сообщений ошибок
    :return: AssertionError: Если хотя бы одно поле не совпадает.
    """
    expected = ErrorResponseSchema(
        message=error_messages,
        error="Bad Request",
        status_code=400
    )
    assert_error_response(actual, expected)


def assert_email_availability_response(request: EmailAvailabilityResponseSchema, expected: bool):
    """
    Проверка, что ответ доступности адреса электронной почты соответствует ожидаемому.

    :param request: Фактические значение доступности.
    :param expected: Ожидаемое значение доступности.
    :return: AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(request.is_available, expected, "email availability")
