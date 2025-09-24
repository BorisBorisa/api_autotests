import pytest

from clients.categories.categories_client import get_category_client, CategoriesClient


@pytest.fixture
def category_client() -> CategoryClient:
    return get_category_client()
