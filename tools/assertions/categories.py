from clients.categories.categories_schema import (
    CreateCategoryRequestSchema,
    CreateCategoryResponseSchema
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
    :param error_messages: Список сообщений ошибок
    :return: AssertionError: Если хотя бы одно поле не совпадает.
    """
    expected = ErrorResponseSchema(
        message=error_messages,
        error="Bad Request",
        status_code=400
    )
    assert_error_response(actual, expected)
