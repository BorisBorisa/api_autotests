import pytest

from clients.authentication.public_auth_client import PublicAuthenticationClient, get_public_authentication_client
from clients.authentication.private_auth_client import PrivateAuthenticationClient, get_private_authentication_client

from fixtures.user import UserFixture


@pytest.fixture
def public_auth_client() -> PublicAuthenticationClient:
    return get_public_authentication_client()


@pytest.fixture
def private_auth_client(function_user: UserFixture) -> PrivateAuthenticationClient:
    return get_private_authentication_client(function_user.authentication_user)
