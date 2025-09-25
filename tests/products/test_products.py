from http import HTTPStatus

from clients.products.products_client import ProductsClient
from clients.products.products_schema import (
    CreateProductRequestSchema,
    CreateProductResponseSchema
)
from fixtures.categories import CategoryFixture
from tools.assertions.base import assert_status_code
from tools.assertions.products import assert_create_product_response
from tools.assertions.schema import validate_json_schema


class TestProducts:
    def test_create_product(self, products_client: ProductsClient, function_category: CategoryFixture):
        request = CreateProductRequestSchema(category_id=function_category.response.id)
        response = products_client.create_product_api(request)
        response_data = CreateProductResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.CREATED)
        assert_create_product_response(request, response_data)

        validate_json_schema(response.json(), CreateProductResponseSchema.model_json_schema())
