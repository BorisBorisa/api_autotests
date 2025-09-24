from clients.categories.categories_schema import (
    CreateCategoryRequestSchema,
    CreateCategoryResponseSchema,
    GetCategoryResponseSchema,
    CategorySchema,
    UpdateCategoryResponseSchema,
    UpdateCategoryRequestSchema
)
from clients.errors_schema import ErrorResponseSchema
from tools.assertions.base import assert_equal
from tools.assertions.errors import assert_error_response


def assert_create_category_response(request: CreateCategoryRequestSchema, response: CreateCategoryResponseSchema):
    """
    Проверяет, что ответ на создание категории соответствует запросу.

    :param request: Исходный запрос на создание категории.
    :param response: Ответ API с данными категории.
    :return: AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(request.name, response.name, "name")
    assert_equal(request.image, str(response.image), "image")


def assert_create_category_with_wrong_data_response(actual: ErrorResponseSchema, error_messages: list):
    """
    Проверяет, что ответ на обновление данных пользователя с некорректным данными соответствует ожидаемому.

    :param actual: Ответ от API с ошибкой, которую необходимо проверить.
    :param error_messages: Список сообщений ошибок.
    :return: AssertionError: Если хотя бы одно поле не совпадает.
    """
    expected = ErrorResponseSchema(
        message=error_messages,
        error="Bad Request",
        status_code=400
    )
    assert_error_response(actual, expected)


def assert_category(actual: CategorySchema, expected: CategorySchema):
    """
    Проверяет, что фактические данные категории соответствуют ожидаемым.

    :param actual: Фактические данные категории.
    :param expected: Ожидаемые данные категории.
    :return: AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.name, expected.name, "name")
    assert_equal(actual.slug, expected.slug, "slug")
    assert_equal(actual.image, expected.image, "image")
    assert_equal(actual.creation_at, expected.creation_at, "creation_at")
    assert_equal(actual.updated_at, expected.updated_at, "updated_at")


def assert_get_category_response(actual: GetCategoryResponseSchema, expected: CreateCategoryResponseSchema):
    """
    Проверяет, что ответ на запрос категории совпадает с ответом при её создании

    :param actual: Фактические данные категории.
    :param expected: Ожидаемые данные категории.
    :return: AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_category(actual, expected)


def assert_update_category_response(request: UpdateCategoryRequestSchema, response: UpdateCategoryResponseSchema):
    """
    Проверяет, что ответ на обновление категории соответствует данным из запроса.

    :param request: Исходный запрос на обновление категории.
    :param response: Ответ API с обновленными данными категории.
    :return: AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(request.name, response.name, "name")
    assert_equal(request.image, str(response.image), "image")
