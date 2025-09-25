from clients.errors_schema import ErrorResponseSchema
from clients.products.products_schema import (
    CreateProductRequestSchema,
    CreateProductResponseSchema
)
from tools.assertions.base import assert_equal
from tools.assertions.errors import assert_invalid_data_response


def assert_create_product_response(request: CreateProductRequestSchema, response: CreateProductResponseSchema):
    """
    Проверяет, что ответ на создание продукта соответствует запросу.

    :param request: Исходный запрос на создание продукта.
    :param response: Ответ API с данными продукта.
    :return: AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(request.title, response.title, "title")
    assert_equal(request.price, response.price, "price")
    assert_equal(request.description, response.description, "description")
    assert_equal(request.category_id, response.category.id, "category id")
    assert_equal(request.images, [str(i) for i in response.images], "images")

def assert_create_product_with_wrong_data_response(actual: ErrorResponseSchema, error_messages: list):
    """
    Проверяет, что ответ на создание продукта с некорректным данными соответствует ожидаемому.

    :param actual: Ответ от API с ошибкой, которую необходимо проверить.
    :param error_messages: Список сообщений ошибок.
    :return: AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_invalid_data_response(actual, error_messages)