import pytest

from clients.categories.categories_client import get_category_client, CategoriesClient


@pytest.fixture
def categories_client() -> CategoriesClient:
    return get_category_client()
