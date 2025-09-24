import pytest

from clients.products.products_client import get_product_client, ProductsClient


@pytest.fixture
def products_client() -> ProductsClient:
    return get_product_client()
