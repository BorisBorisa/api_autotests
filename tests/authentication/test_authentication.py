from http import HTTPStatus

import allure
import pytest

from clients.authentication.private_auth_client import PrivateAuthenticationClient
from clients.authentication.public_auth_client import PublicAuthenticationClient
from clients.authentication.authentication_schema import (
    LoginRequestSchema,
    LoginResponseSchema,
    RefreshTokenRequestSchema,
    RefreshTokenResponseSchema
)
from clients.errors_schema import ErrorResponseSchema
from clients.users.users_schema import UserProfileResponseSchema

from fixtures.user import UserFixture

from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema
from tools.assertions.authentication import (
    assert_login_response,
    assert_refresh_response,
    assert_login_invalid_credentials_response,
    assert_user_profile_response_matches, assert_refresh_with_invalid_token_response
)
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeatures
from tools.allure.storys import AllureStory


@pytest.mark.regression
@pytest.mark.authentication
@allure.epic(AllureEpic.AUTHENTICATION)
@allure.feature(AllureFeatures.AUTHENTICATION)
class TestAuthentication:
    @allure.story(AllureStory.LOGIN)
    @allure.title("Login with correct credentials")
    def test_login(self, function_user: UserFixture, public_auth_client: PublicAuthenticationClient):
        request = LoginRequestSchema(email=function_user.email, password=function_user.password)
        response = public_auth_client.login_api(request)
        response_data = LoginResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.CREATED)
        assert_login_response(response_data)

        validate_json_schema(response.json(), LoginResponseSchema.model_json_schema())

    @allure.story(AllureStory.VALIDATE_ENTITY)
    @allure.title("Login with invalid credentials")
    def test_login_invalid_credentials(self, public_auth_client: PublicAuthenticationClient):
        request = LoginRequestSchema()
        response = public_auth_client.login_api(request)
        response_data = ErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.UNAUTHORIZED)
        assert_login_invalid_credentials_response(response_data)

        validate_json_schema(response.json(), ErrorResponseSchema.model_json_schema())

    @allure.story(AllureStory.GET_ENTITY)
    @allure.title("Retrieving an authenticated user’s profile")
    def test_authenticated_user_can_retrieve_profile(
            self,
            function_user: UserFixture,
            private_auth_client: PrivateAuthenticationClient
    ):
        response = private_auth_client.profile_api()
        response_data = UserProfileResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_user_profile_response_matches(response_data, function_user.response)

        validate_json_schema(response.json(), UserProfileResponseSchema.model_json_schema())

    @allure.story(AllureStory.GET_ENTITY)
    @allure.title("Refreshing tokens with a valid token returns a new token pair")
    def test_refresh_token_returns_new_token_pair(
            self,
            function_user: UserFixture,
            public_auth_client: PublicAuthenticationClient,
    ):
        login_request = LoginRequestSchema(email=function_user.email, password=function_user.password)
        login_response = public_auth_client.login_api(login_request)
        login_response_data = LoginResponseSchema.model_validate_json(login_response.text)

        refresh_request = RefreshTokenRequestSchema(refresh_token=login_response_data.refresh_token)
        refresh_response = public_auth_client.refresh_api(refresh_request)
        response_data = RefreshTokenResponseSchema.model_validate_json(refresh_response.text)

        assert_status_code(refresh_response.status_code, HTTPStatus.CREATED)
        assert_refresh_response(response_data)

        validate_json_schema(refresh_response.json(), RefreshTokenResponseSchema.model_json_schema())

    @allure.story(AllureStory.VALIDATE_ENTITY)
    @allure.title("Refreshing tokens with an invalid token returns an error")
    def test_refresh_token_with_invalid_token(self, public_auth_client: PublicAuthenticationClient):
        request = RefreshTokenRequestSchema()
        response = public_auth_client.refresh_api(request)
        response_data = ErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.UNAUTHORIZED)
        assert_refresh_with_invalid_token_response(response_data)

        validate_json_schema(response.json(), ErrorResponseSchema.model_json_schema())
