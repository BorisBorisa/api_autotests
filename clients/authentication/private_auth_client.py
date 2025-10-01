import allure

from httpx import Response

from clients.api_client import APIClient
from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema

from tools.routes import APIRoutes


class PrivateAuthenticationClient(APIClient):
    """
    Публичный клиент для работы с /api/v1/auth
    """

    @allure.step("Get authenticate user profile")
    def profile_api(self) -> Response:
        """
        Метод возвращает данные авторизованного пользователя.

        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"{APIRoutes.AUTH}/profile")


def get_private_authentication_client(user: AuthenticationUserSchema) -> PrivateAuthenticationClient:
    """
    Функция создаёт экземпляр AuthenticationClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию AuthenticationClient.
    """
    return PrivateAuthenticationClient(client=get_private_http_client(user))
