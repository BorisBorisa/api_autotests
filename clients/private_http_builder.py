from httpx import Client

from clients.event_hooks import curl_event_hook
from config import settings
from pydantic import BaseModel, ConfigDict

from clients.authentication.public_auth_client import get_public_authentication_client
from clients.authentication.authentication_schema import LoginRequestSchema


class AuthenticationUserSchema(BaseModel):
    model_config = ConfigDict(frozen=True)

    email: str
    password: str


def get_private_http_client(user: AuthenticationUserSchema) -> Client:
    """
    Функция создаёт экземпляр http.Client с базовыми настройками.

    :return: Готовый к использованию объект http.Client.
    """
    auth_client = get_public_authentication_client()

    login_request = LoginRequestSchema(email=user.email, password=user.password)
    auth_response = auth_client.login(login_request)

    return Client(
        timeout=settings.http_client.timeout,
        base_url=settings.http_client.client_url,
        headers={"Authorization": f"Bearer {auth_response.access_token}"},
        event_hooks={"request": [curl_event_hook]}
    )
