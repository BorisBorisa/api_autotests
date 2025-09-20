import pytest
from pydantic import BaseModel

from clients.private_http_builder import AuthenticationUserSchema
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema

from clients.users.users_client import UserClient, get_user_client


class UserFixture(BaseModel):
    request: CreateUserRequestSchema
    response: CreateUserResponseSchema

    @property
    def email(self) -> str:
        return self.request.email

    @property
    def password(self) -> str:
        return self.request.password

    @property
    def authentication_user(self) -> AuthenticationUserSchema:
        return AuthenticationUserSchema(
            email=self.email,
            password=self.password
        )


@pytest.fixture
def user_client() -> UserClient:
    return get_user_client()


@pytest.fixture
def function_user(user_client: UserClient) -> UserFixture:
    """
    Фикстура для создания (регистрации) тестового пользователя.

    :param user_client: Клиент для работы с роутом /api/v1/users.
    :return: Pydantic схема UserFixture c данными зарегистрированного пользователя.
    """
    request = CreateUserRequestSchema()
    response = user_client.create_user(request)

    return UserFixture(request=request, response=response)
