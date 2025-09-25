from clients.products.products_schema import (
    CreateProductRequestSchema,
    CreateProductResponseSchema
)
from tools.assertions.base import assert_equal


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
