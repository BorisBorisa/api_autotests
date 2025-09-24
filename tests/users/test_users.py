from http import HTTPStatus

import pytest

from clients.errors_schema import ErrorResponseSchema
from clients.users.users_client import UserClient
from clients.users.users_schema import (
    GetUsersResponseSchema,
    CreateUserRequestSchema,
    CreateUserResponseSchema,
    GetUserResponseSchema,
    UserNotFoundResponseSchema,
    UpdateUserRequestSchema,
    UpdateUserResponseSchema,
    EmailAvailabilityRequestSchema,
    EmailAvailabilityResponseSchema
)
from fixtures.user import UserFixture

from tools.assertions.base import assert_status_code
from tools.assertions.users import (
    assert_create_user_response,
    assert_create_user_with_wrong_email_response,
    assert_create_user_with_all_empty_fields_response,
    assert_create_user_with_wrong_password_response,
    assert_create_user_with_wrong_avatar_url_response,
    assert_user,
    assert_get_user_with_wrong_id_response,
    assert_update_user_response,
    assert_update_user_with_wrong_data_response,
    assert_email_availability_response
)
from tools.assertions.schema import validate_json_schema

from testdata import test_data


class TestUsers:
    def test_crate_user(self, user_client: UserClient):
        request = CreateUserRequestSchema()
        response = user_client.create_user_api(request)
        response_data = CreateUserResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.CREATED)
        assert_create_user_response(request, response_data)

        validate_json_schema(response.json(), CreateUserResponseSchema.model_json_schema())

    def test_create_user_with_wrong_email(self, user_client: UserClient):
        request = CreateUserRequestSchema(email=test_data.INVALID_EMAIL)
        response = user_client.create_user_api(request)
        response_data = ErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.BAD_REQUEST)
        assert_create_user_with_wrong_email_response(response_data)

        validate_json_schema(response.json(), ErrorResponseSchema.model_json_schema())

    def test_create_user_with_wrong_password(self, user_client: UserClient):
        request = CreateUserRequestSchema(password=test_data.INVALID_PASSWORD)
        response = user_client.create_user_api(request)
        response_data = ErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.BAD_REQUEST)
        assert_create_user_with_wrong_password_response(response_data)

        validate_json_schema(response.json(), ErrorResponseSchema.model_json_schema())

    def test_create_user_with_wrong_avatar_url(self, user_client: UserClient):
        request = CreateUserRequestSchema(avatar=test_data.INVALID_AVATAR_URL)
        response = user_client.create_user_api(request)
        response_data = ErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.BAD_REQUEST)
        assert_create_user_with_wrong_avatar_url_response(response_data)

        validate_json_schema(response.json(), ErrorResponseSchema.model_json_schema())

    def test_create_user_with_all_empty_fields(self, user_client: UserClient):
        request = CreateUserRequestSchema(name="", email="", password="", avatar="")
        response = user_client.create_user_api(request)
        response_data = ErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.BAD_REQUEST)
        assert_create_user_with_all_empty_fields_response(response_data)

        validate_json_schema(response.json(), ErrorResponseSchema.model_json_schema())

    def test_get_user_with_id(self, user_client: UserClient, function_user: UserFixture):
        response = user_client.get_user_api(user_id=function_user.response.id)
        response_data = GetUserResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_user(function_user.response, response_data)

        validate_json_schema(response.json(), GetUserResponseSchema.model_json_schema())

    def test_get_user_with_wrong_id(self, user_client: UserClient):
        response = user_client.get_user_api(user_id=test_data.INVALID_USER_ID)
        response_data = UserNotFoundResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.BAD_REQUEST)
        assert_get_user_with_wrong_id_response(response_data, test_data.INVALID_USER_ID)

        validate_json_schema(response.json(), UserNotFoundResponseSchema.model_json_schema())

    def test_update_user(self, user_client: UserClient, function_user: UserFixture):
        request = UpdateUserRequestSchema()
        response = user_client.update_user_api(user_id=function_user.response.id, request=request)
        response_data = UpdateUserResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_update_user_response(request, response_data)

        validate_json_schema(response.json(), UpdateUserResponseSchema.model_json_schema())

    @pytest.mark.parametrize(
        "payload, message",
        test_data.user_update_invalid_data,
        ids=test_data.user_update_invalid_ids
    )
    def test_update_user_with_invalid_data(self, user_client: UserClient, function_user: UserFixture, payload, message):
        request = UpdateUserRequestSchema(**payload)
        response = user_client.update_user_api(user_id=function_user.response.id, request=request)
        response_data = ErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.BAD_REQUEST)
        assert_update_user_with_wrong_data_response(response_data, message)

        validate_json_schema(response.json(), ErrorResponseSchema.model_json_schema())

    def test_get_users(self, user_client: UserClient):
        response = user_client.get_users_api()
        response_data = GetUsersResponseSchema.validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)

        validate_json_schema(response.json(), GetUsersResponseSchema.json_schema())

    def test_existing_email_availability(self, user_client: UserClient, function_user: UserFixture):
        request = EmailAvailabilityRequestSchema(email=function_user.request.email)
        response = user_client.check_email_availability_api(request)
        response_data = EmailAvailabilityResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.CREATED)
        assert_email_availability_response(response_data, False)

        validate_json_schema(response.json(), EmailAvailabilityResponseSchema.model_json_schema())

    def test_not_existing_email_availability(self, user_client: UserClient, function_user: UserFixture):
        request = EmailAvailabilityRequestSchema()
        response = user_client.check_email_availability_api(request)
        response_data = EmailAvailabilityResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.CREATED)
        assert_email_availability_response(response_data, True)

        validate_json_schema(response.json(), EmailAvailabilityResponseSchema.model_json_schema())
