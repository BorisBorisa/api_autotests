from httpx import Response

from clients.api_client import APIClient
from clients.categories.categories_schema import (
    CreateCategoryRequestSchema,
    UpdateCategoryRequestSchema,
    CreateCategoryResponseSchema
)
from clients.public_http_builder import get_public_http_client

from tools.routes import APIRoutes


class CategoryClient(APIClient):
    """
    Клиент для работы с /api/v1/categories
    """

    def get_categories_api(self) -> Response:
        """
        Метод получения списка всех категорий.

        :return: Ответ от сервера в виде объекта httpx.Response.
        """
        return self.get(url=APIRoutes.CATEGORIES)

    def get_category_by_id_api(self, category_id: int) -> Response:
        """
        Метод получения категории по id.

        :param category_id: Идентификатор категории.
        :return: Ответ от сервера в виде объекта httpx.Response.
        """
        return self.get(url=f"{APIRoutes.CATEGORIES}/{category_id}")

    def get_category_by_slug_api(self, slug: str) -> Response:
        """
        Метод получения категории по текстовому идентификатору.

        :param slug: Текстовый идентификатор категории.
        :return: Ответ от сервера в виде объекта httpx.Response.
        """
        return self.get(url=f"{APIRoutes.CATEGORIES}/slug/{slug}")

    def create_category_api(self, request: CreateCategoryRequestSchema) -> Response:
        """
        Метод выполняет создание категории.

        :param request: Словарь с name, image.
        :return: Ответ от сервера в виде объекта httpx.Response.
        """
        return self.post(
            url=APIRoutes.CATEGORIES,
            json=request.model_dump(by_alias=True)
        )

    def update_category_api(self, category_id: int, request: UpdateCategoryRequestSchema) -> Response:
        """
        Метод обновления категории по идентификатору.

        :param category_id: Идентификатор категории.
        :param request: Словарь с name, image.
        :return: Ответ от сервера в виде объекта httpx.Response.
        """
        return self.put(
            url=f"{APIRoutes.CATEGORIES}/{category_id}",
            json=request.model_dump(by_alias=True)
        )

    def delete_category_api(self, category_id: int) -> Response:
        """
        Метод удаления категории по id.

        :param category_id: Идентификатор категории.
        :return: Ответ от сервера в виде объекта httpx.Response.
        """
        return self.delete(url=f"{APIRoutes.CATEGORIES}/{category_id}")

    def get_products_by_category_id_api(self, category_id: int) -> Response:
        """
        метод получения всех продуктов по id категории.

        :param category_id: Идентификатор категории.
        :return: Ответ от сервера в виде объекта httpx.Response.
        """
        return self.get(url=f"{APIRoutes.CATEGORIES}/{category_id}/products")

    def create_category(self, request: CreateCategoryRequestSchema) -> CreateCategoryResponseSchema:
        response = self.create_category_api(request)
        return CreateCategoryResponseSchema.model_validate_json(response.text)


def get_category_client() -> CategoryClient:
    """
    Функция создаёт экземпляр CategoriesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию CategoriesClient.
    """
    return CategoryClient(client=get_public_http_client())
