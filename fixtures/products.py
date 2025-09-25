import pytest
from pydantic import BaseModel

from clients.products.products_client import get_product_client, ProductsClient
from clients.products.products_schema import CreateProductRequestSchema, CreateProductResponseSchema


class ProductFixture(BaseModel):
    request: CreateProductRequestSchema
    response: CreateProductResponseSchema


@pytest.fixture
def products_client() -> ProductsClient:
    return get_product_client()


@pytest.fixture
def function_product(products_client: ProductsClient) -> ProductFixture:
    """
    Фикстура для создания новой продукта.

    :param products_client: Клиент для работы с роутом /api/v1/products.
    :return: Pydantic схема CategoryFixture c данными новой категории.
    """
    request = CreateProductRequestSchema()
    response = products_client.create_product(request)

    return ProductFixture(request=request, response=response)
