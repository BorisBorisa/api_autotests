from http import HTTPStatus

import pytest

from clients.errors_schema import ErrorResponseSchema
from clients.products.products_client import ProductsClient
from clients.products.products_schema import (
    CreateProductRequestSchema,
    CreateProductResponseSchema
)
from fixtures.categories import CategoryFixture
from tools.assertions.base import assert_status_code
from tools.assertions.products import (
    assert_create_product_response,
    assert_create_product_with_wrong_data_response
)
from tools.assertions.schema import validate_json_schema

from testdata import test_data


class TestProducts:
    def test_create_product(self, products_client: ProductsClient, function_category: CategoryFixture):
        request = CreateProductRequestSchema(category_id=function_category.response.id)
        response = products_client.create_product_api(request)
        response_data = CreateProductResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.CREATED)
        assert_create_product_response(request, response_data)

        validate_json_schema(response.json(), CreateProductResponseSchema.model_json_schema())

    @pytest.mark.parametrize(
        "payload, message",
        test_data.product_invalid_data,
        ids=test_data.product_invalid_ids
    )
    def test_create_product_with_wrong_data(
            self,
            products_client: ProductsClient,
            function_category: CategoryFixture,
            payload,
            message
    ):
        request = CreateProductRequestSchema(category_id=function_category.response.id, **payload)
        response = products_client.create_product_api(request)
        response_data = ErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.BAD_REQUEST)
        assert_create_product_with_wrong_data_response(response_data, message)

        validate_json_schema(response.json(), ErrorResponseSchema.model_json_schema())
