import pytest
from pydantic import BaseModel

from clients.categories.categories_client import get_category_client, CategoryClient
from clients.categories.categories_schema import CreateCategoryRequestSchema, CreateCategoryResponseSchema


class CategoryFixture(BaseModel):
    request: CreateCategoryRequestSchema
    response: CreateCategoryResponseSchema


@pytest.fixture
def category_client() -> CategoryClient:
    return get_category_client()


@pytest.fixture
def function_category(category_client: CategoryClient) -> CategoryFixture:
    """
    Фикстура для создания новой категории.

    :param category_client: Клиент для работы с роутом /api/v1/categories.
    :return: Pydantic схема CategoryFixture c данными новой категории.
    """
    request = CreateCategoryRequestSchema()
    response = category_client.create_category(request)

    return CategoryFixture(request=request, response=response)
