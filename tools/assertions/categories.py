from clients.categories.categories_schema import (
    CreateCategoryRequestSchema,
    CreateCategoryResponseSchema
)
from tools.assertions.base import assert_equal


def assert_create_category_response(request: CreateCategoryRequestSchema, response: CreateCategoryResponseSchema):
    """
    Проверяет, что ответ на создание категории соответствует запросу.

    :param request: Исходный запрос на создание категории.
    :param response: Ответ API с данными категории.
    :return: AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(request.name, response.name, "name")
    assert_equal(request.image, str(response.image), "image")
