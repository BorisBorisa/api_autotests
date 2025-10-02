import allure

from clients.errors_schema import ErrorResponseSchema
from clients.products.products_schema import (
    CreateProductRequestSchema,
    CreateProductResponseSchema,
    ProductSchema,
    GetProductResponseSchema,
    UpdateProductRequestSchema,
    UpdateProductResponseSchema
)
from tools.assertions.base import assert_equal
from tools.assertions.errors import assert_invalid_data_response
from tools.logger import get_logger

logger = get_logger("PRODUCTS_ASSERTIONS")


@allure.step("Check create product response")
def assert_create_product_response(request: CreateProductRequestSchema, response: CreateProductResponseSchema):
    """
    Проверяет, что ответ на создание продукта соответствует запросу.

    :param request: Исходный запрос на создание продукта.
    :param response: Ответ API с данными продукта.
    :return: AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info("Check create product response")

    assert_equal(request.title, response.title, "title")
    assert_equal(request.price, response.price, "price")
    assert_equal(request.description, response.description, "description")
    assert_equal(request.category_id, response.category.id, "category id")
    assert_equal(request.images, [str(i) for i in response.images], "images")


@allure.step("Check product creation response with invalid data")
def assert_create_product_with_wrong_data_response(actual: ErrorResponseSchema, error_messages: list):
    """
    Проверяет, что ответ на создание продукта с некорректным данными соответствует ожидаемому.

    :param actual: Ответ от API с ошибкой, которую необходимо проверить.
    :param error_messages: Список сообщений ошибок.
    :return: AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info("Check product creation response with invalid data")

    assert_invalid_data_response(actual, error_messages)


@allure.step("Check product update response with invalid data")
def assert_update_product_with_wrong_data_response(actual: ErrorResponseSchema, error_messages: list):
    """
    Проверяет, что ответ на обновление продукта с некорректным данными соответствует ожидаемому.

    :param actual: Ответ от API с ошибкой, которую необходимо проверить.
    :param error_messages: Список сообщений ошибок.
    :return: AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info("Check product update response with invalid data")

    assert_invalid_data_response(actual, error_messages)


@allure.step("Check product")
def assert_product(actual: ProductSchema, expected: ProductSchema):
    """
    Проверяет, что фактические данные продукта соответствуют ожидаемым.

    :param actual: Фактические данные продукта.
    :param expected: Ожидаемые данные продукта.
    :return: AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info("Check product")

    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.title, expected.title, "title")
    assert_equal(actual.slug, expected.slug, "slug")
    assert_equal(actual.price, expected.price, "price")
    assert_equal(actual.description, expected.description, "description")
    assert_equal(actual.category, expected.category, "category")
    assert_equal(actual.images, expected.images, "images")
    assert_equal(actual.creation_at, expected.creation_at, "creation_at")
    assert_equal(actual.updated_at, expected.updated_at, "updated_at")


@allure.step("Check get product response")
def assert_get_product_response(actual: GetProductResponseSchema, expected: CreateProductResponseSchema):
    """
    Проверяет, что ответ на запрос продукта совпадает с ответом при её создании

    :param actual: Фактические данные продукта.
    :param expected: Ожидаемые данные продукта.
    :return: AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info("Check get product response")

    assert_product(actual, expected)


@allure.step("Check update product response")
def assert_update_product_response(request: UpdateProductRequestSchema, response: UpdateProductResponseSchema):
    """
    Проверяет, что ответ на обновление продукта соответствует запросу.

    :param request: Исходный запрос на обновление продукта.
    :param response: Ответ API с данными продукта.
    :return: AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info("Check update product response")

    assert_equal(request.title, response.title, "title")
    assert_equal(request.price, response.price, "price")
    assert_equal(request.description, response.description, "description")
    assert_equal(request.category_id, response.category.id, "category id")
    assert_equal(request.images, [str(i) for i in response.images], "images")
