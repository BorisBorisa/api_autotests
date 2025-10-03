from http import HTTPStatus

import pytest
import allure

from allure_commons.types import Severity

from clients.categories.categories_client import CategoryClient

from clients.categories.categories_schema import (
    CreateCategoryRequestSchema,
    CreateCategoryResponseSchema,
    GetCategoryResponseSchema,
    UpdateCategoryRequestSchema,
    UpdateCategoryResponseSchema, GetCategoriesResponseSchema
)
from clients.errors_schema import ErrorResponseSchema
from fixtures.categories import CategoryFixture
from testdata import test_data
from tools.assertions.base import assert_status_code
from tools.assertions.categories import (
    assert_create_category_response,
    assert_create_category_with_wrong_data_response,
    assert_get_category_response,
    assert_update_category_response,
    assert_update_category_with_wrong_data_response
)
from tools.assertions.delete import assert_delete_response
from tools.assertions.schema import validate_json_schema

from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeatures
from tools.allure.storys import AllureStory


@pytest.mark.regression
@pytest.mark.categories
@allure.epic(AllureEpic.STORE)
@allure.feature(AllureFeatures.CATEGORIES)
class TestCategories:
    @allure.story(AllureStory.CREATE_ENTITY)
    @allure.title("Create category")
    @allure.severity(Severity.NORMAL)
    def test_create_category(self, category_client: CategoryClient):
        request = CreateCategoryRequestSchema()
        response = category_client.create_category_api(request)
        response_data = CreateCategoryResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.CREATED)
        assert_create_category_response(request, response_data)

        validate_json_schema(response.json(), CreateCategoryResponseSchema.model_json_schema())

    @allure.story(AllureStory.VALIDATE_ENTITY)
    @allure.title("Create category with invalid data fails")
    @allure.severity(Severity.NORMAL)
    @pytest.mark.parametrize(
        "payload, message",
        test_data.category_invalid_data,
        ids=test_data.category_invalid_ids
    )
    def test_create_category_with_wrong_data(self, category_client: CategoryClient, payload, message):
        request = CreateCategoryRequestSchema(**payload)
        response = category_client.create_category_api(request)
        response_data = ErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.BAD_REQUEST)
        assert_create_category_with_wrong_data_response(response_data, message)

        validate_json_schema(response.json(), ErrorResponseSchema.model_json_schema())

    @allure.story(AllureStory.GET_ENTITY)
    @allure.title("Get category by ID")
    @allure.severity(Severity.NORMAL)
    def test_get_category_by_id(self, category_client: CategoryClient, function_category: CategoryFixture):
        response = category_client.get_category_by_id_api(function_category.response.id)
        response_data = GetCategoryResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_category_response(response_data, function_category.response)

        validate_json_schema(response.json(), GetCategoryResponseSchema.model_json_schema())

    @allure.story(AllureStory.GET_ENTITY)
    @allure.title("Get category by slug")
    @allure.severity(Severity.NORMAL)
    def test_get_category_by_slug(self, category_client: CategoryClient, function_category: CategoryFixture):
        response = category_client.get_category_by_slug_api(function_category.response.slug)
        response_data = GetCategoryResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_category_response(response_data, function_category.response)

        validate_json_schema(response.json(), GetCategoryResponseSchema.model_json_schema())

    @allure.story(AllureStory.UPDATE_ENTITY)
    @allure.title("Update category")
    @allure.severity(Severity.NORMAL)
    def test_update_category(self, category_client: CategoryClient, function_category: CategoryFixture):
        request = UpdateCategoryRequestSchema()
        response = category_client.update_category_api(function_category.response.id, request)
        response_data = UpdateCategoryResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_update_category_response(request, response_data)

        validate_json_schema(response.json(), UpdateCategoryResponseSchema.model_json_schema())

    @allure.story(AllureStory.VALIDATE_ENTITY)
    @allure.title("Update category with invalid data fails")
    @allure.severity(Severity.NORMAL)
    @pytest.mark.parametrize(
        "payload, message",
        test_data.category_invalid_data,
        ids=test_data.category_invalid_ids
    )
    def test_update_category_with_wrong_data(
            self,
            category_client: CategoryClient,
            function_category: CategoryFixture,
            payload,
            message
    ):
        request = UpdateCategoryRequestSchema(name=None, image=None).model_copy(update=payload)
        response = category_client.update_category_api(function_category.response.id, request)
        response_data = ErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.BAD_REQUEST)
        assert_update_category_with_wrong_data_response(response_data, message)

        validate_json_schema(response.json(), ErrorResponseSchema.model_json_schema())

    @allure.story(AllureStory.DELETE_ENTITY)
    @allure.title("Delete category")
    @allure.severity(Severity.NORMAL)
    def test_delete_category(self, category_client: CategoryClient, function_category: CategoryFixture):
        response = category_client.delete_category_api(function_category.response.id)
        response_data = response.json()

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_delete_response(response_data)

    @allure.story(AllureStory.GET_ENTITIES)
    @allure.title("Getting categories")
    @allure.severity(Severity.NORMAL)
    def test_get_categories(self, category_client: CategoryClient):
        response = category_client.get_categories_api()

        assert_status_code(response.status_code, HTTPStatus.OK)
        validate_json_schema(response.json(), GetCategoriesResponseSchema.json_schema())
