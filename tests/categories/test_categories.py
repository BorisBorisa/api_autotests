from http import HTTPStatus

from clients.categories.categories_client import CategoriesClient

from clients.categories.categories_schema import (
    CreateCategoryRequestSchema,
    CreateCategoryResponseSchema
)
from tools.assertions.base import assert_status_code
from tools.assertions.categories import assert_create_category_response
from tools.assertions.schema import validate_json_schema


class TestCategories:
    def test_create_category(self, categories_client: CategoriesClient):
        request = CreateCategoryRequestSchema()
        response = categories_client.create_category_api(request)
        response_data = CreateCategoryResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.CREATED)
        assert_create_category_response(request, response_data)

        validate_json_schema(response.json(), CreateCategoryResponseSchema.model_json_schema())

    def test_get_category_by_id(self):
        pass

    def test_get_category_by_slug(self):
        pass
