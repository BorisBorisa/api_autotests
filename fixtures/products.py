import pytest
from pydantic import BaseModel

from clients.products.products_client import get_product_client, ProductsClient
from clients.products.products_schema import CreateProductRequestSchema, CreateProductResponseSchema
from fixtures.categories import CategoryFixture


class ProductFixture(BaseModel):
    request: CreateProductRequestSchema
    response: CreateProductResponseSchema


@pytest.fixture
def products_client() -> ProductsClient:
    return get_product_client()


@pytest.fixture
def function_product(products_client: ProductsClient, function_category: CategoryFixture) -> ProductFixture:
    """
    Фикстура для создания новой продукта.

    :param products_client: Клиент для работы с роутом /api/v1/products.
    :param function_category: Pydantic схема CategoryFixture c данными новой категории.
    :return: Pydantic схема ProductFixture c данными нового продукта.
    """
    request = CreateProductRequestSchema(category_id=function_category.response.id)
    response = products_client.create_product(request)

    return ProductFixture(request=request, response=response)
