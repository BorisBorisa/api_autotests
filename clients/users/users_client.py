import allure

from httpx import Response

from clients.api_client import APIClient
from clients.public_http_builder import get_public_http_client
from clients.users.users_schema import (
    CreateUserResponseSchema,
    CreateUserRequestSchema,
    UpdateUserRequestSchema,
    EmailAvailabilityRequestSchema
)

from tools.routes import APIRoutes


class UserClient(APIClient):
    """
    Клиент для работы с /api/v1/users
    """

    @allure.step("Get users")
    def get_users_api(self) -> Response:
        """
        Метод получения списка всех пользователей.

        :return: Ответ от сервера в виде объекта http.Response.
        """
        return self.get(url=APIRoutes.USERS)

    @allure.step("Get users by id {user_id}")
    def get_user_api(self, user_id: int) -> Response:
        """
        Метод получения пользователя по идентификатору.

        :param user_id: Идентификатор пользователя.
        :return: Ответ от сервера в виде объекта http.Response.
        """
        return self.get(url=f"{APIRoutes.USERS}/{user_id}")

    @allure.step("Create user")
    def create_user_api(self, request: CreateUserRequestSchema) -> Response:
        """
        Метод выполняет создание пользователя.

        :param request: Словарь с name, email, password, avatar.
        :return: Ответ от сервера в виде объекта http.Response.
        """
        return self.client.post(
            url=APIRoutes.USERS,
            json=request.model_dump(by_alias=True)
        )

    @allure.step("Update user by id {user_id}")
    def update_user_api(self, user_id: int, request: UpdateUserRequestSchema) -> Response:
        """
        Метод обновления пользователя по идентификатору.

        :param user_id: Идентификатор пользователя.
        :param request: Словарь с email, lastName, firstName, middleName.
        :return: Ответ от сервера в виде объекта http.Response.
        """
        return self.put(
            url=f"{APIRoutes.USERS}/{user_id}",
            json=request.model_dump(by_alias=True)
        )

    @allure.step("Check email availability")
    def check_email_availability_api(self, request: EmailAvailabilityRequestSchema) -> Response:
        """
        Метод проверки, зарегистрирован ли адрес электронной почты в системе.

        :param request: Словарь с email.
        :return: Ответ от сервера в виде объекта http.Response.
        """
        return self.post(
            url=f"{APIRoutes.USERS}/is-available",
            json=request.model_dump(by_alias=True)
        )

    def create_user(self, request: CreateUserRequestSchema) -> CreateUserResponseSchema:
        response = self.create_user_api(request)
        return CreateUserResponseSchema.model_validate_json(response.text)


def get_user_client() -> UserClient:
    """
    Функция создаёт экземпляр AuthenticationClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию AuthenticationClient.
    """
    return UserClient(client=get_public_http_client())
