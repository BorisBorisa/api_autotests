import allure

from httpx import Response

from clients.api_client import APIClient
from clients.public_http_builder import get_public_http_client
from clients.authentication.authentication_schema import (
    LoginRequestSchema,
    LoginResponseSchema,
    RefreshTokenRequestSchema
)
from tools.routes import APIRoutes


class PublicAuthenticationClient(APIClient):
    """
    Публичный клиент для работы с /api/v1/auth
    """

    @allure.step("Authenticate user")
    def login_api(self, request: LoginRequestSchema) -> Response:
        """
        Метод выполняет аутентификации пользователя.

        :param request: Объект LoginRequestSchema с 'email' и 'password' пользователя.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(
            url=f"{APIRoutes.AUTH}/login",
            json=request.model_dump(by_alias=True)
        )

    @allure.step("Refresh authentication token")
    def refresh_api(self, request: RefreshTokenRequestSchema) -> Response:
        """
        Метод обновляет токен авторизации.

        :param request: Словарь с refreshToken.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(
            url=f"{APIRoutes.AUTH}/refresh-token",
            json=request.model_dump(by_alias=True)
        )

    def login(self, request: LoginRequestSchema) -> LoginResponseSchema:
        response = self.login_api(request)
        return LoginResponseSchema.model_validate_json(response.text)


def get_public_authentication_client() -> PublicAuthenticationClient:
    """
    Функция создаёт экземпляр AuthenticationClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию AuthenticationClient.
    """
    return PublicAuthenticationClient(client=get_public_http_client())
