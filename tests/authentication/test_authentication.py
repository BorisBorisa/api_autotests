from http import HTTPStatus

from clients.authentication.public_auth_client import PublicAuthenticationClient
from clients.authentication.authentication_schema import LoginRequestSchema, LoginResponseSchema
from clients.errors_schema import ErrorResponseSchema

from fixtures.user import UserFixture
from tools.assertions.base import assert_status_code
from tools.assertions.authentication import assert_login_response, assert_login_invalid_credentials
from tools.assertions.schema import validate_json_schema


class TestAuthentication:
    def test_login(self, function_user: UserFixture, public_auth_client: PublicAuthenticationClient):
        request = LoginRequestSchema(email=function_user.email, password=function_user.password)
        response = public_auth_client.login_api(request)
        response_data = LoginResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.CREATED)
        assert_login_response(response_data)

        validate_json_schema(response.json(), LoginResponseSchema.model_json_schema())

    def test_login_invalid_credentials(self, public_auth_client: PublicAuthenticationClient):
        request = LoginRequestSchema()
        response = public_auth_client.login_api(request)
        response_data = ErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.UNAUTHORIZED)
        assert_login_invalid_credentials(response_data)

        validate_json_schema(response.json(), ErrorResponseSchema.model_json_schema())
