import allure

from httpx import Response

from clients.api_client import APIClient
from clients.products.products_schema import (
    CreateProductRequestSchema,
    UpdateProductRequestSchema,
    CreateProductResponseSchema
)
from clients.public_http_builder import get_public_http_client

from tools.routes import APIRoutes


class ProductsClient(APIClient):
    """
    Клиент для работы с /api/v1/products
    """

    @allure.step("Get products")
    def get_products_api(self) -> Response:
        """
        Метод получения списка всех продуктов.

        :return: Ответ от сервера в виде объекта http.Response.
        """
        return self.get(url=APIRoutes.PRODUCTS)

    @allure.step("Get product by id {product_id}")
    def get_product_by_id_api(self, product_id: int) -> Response:
        """
        Метод получения продуктов по id.

        :param product_id: Идентификатор продукта.
        :return: Ответ от сервера в виде объекта http.Response.
        """
        return self.get(url=f"{APIRoutes.PRODUCTS}/{product_id}")

    @allure.step("Get product by slug {slug}")
    def get_product_by_slug_api(self, slug: str) -> Response:
        """
        Метод получения продуктов по текстовому идентификатору.

        :param slug: Текстовый идентификатор продукта.
        :return: Ответ от сервера в виде объекта http.Response.
        """
        return self.get(url=f"{APIRoutes.PRODUCTS}/slug/{slug}")

    @allure.step("Create product")
    def create_product_api(self, request: CreateProductRequestSchema) -> Response:
        """
        Метод создания продукта.

        :param request: Словарь с title, price, description, category_id, image.
        :return: Ответ от сервера в виде объекта http.Response.
        """
        return self.post(
            url=APIRoutes.PRODUCTS,
            json=request.model_dump(by_alias=True)
        )

    @allure.step("Update product")
    def update_product_api(self, product_id: int, request: UpdateProductRequestSchema) -> Response:
        """
        Метод обновления продукта по идентификатору.

        :param product_id: Идентификатор продукта.
        :param request: Словарь с title, price, description, category_id, image.
        :return: Ответ от сервера в виде объекта http.Response.
        """
        return self.put(
            url=f"{APIRoutes.PRODUCTS}/{product_id}",
            json=request.model_dump(by_alias=True)
        )

    @allure.step("Delete product")
    def delete_product_api(self, product_id: int) -> Response:
        """
        Метод удаления продукта по id.

        :param product_id: Идентификатор продукта.
        :return: Ответ от сервера в виде объекта http.Response.
        """
        return self.delete(url=f"{APIRoutes.PRODUCTS}/{product_id}")

    def create_product(self, request: CreateProductRequestSchema) -> CreateProductResponseSchema:
        response = self.create_product_api(request)
        return CreateProductResponseSchema.model_validate_json(response.text)


def get_product_client() -> ProductsClient:
    """
    Функция создаёт экземпляр ProductsClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию ProductsClient.
    """
    return ProductsClient(client=get_public_http_client())
