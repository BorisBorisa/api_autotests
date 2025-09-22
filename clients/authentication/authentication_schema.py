from pydantic import BaseModel, Field, ConfigDict
from tools.fakers import fake


class TokenSchema(BaseModel):
    """
    Описание структуры аутентификационных токенов.
    """
    access_token: str
    refresh_token: str


class LoginRequestSchema(BaseModel):
    """
    Описание структуры запроса на аутентификацию.
    """
    email: str = Field(default_factory=fake.email)
    password: str = Field(default_factory=fake.password)


class LoginResponseSchema(TokenSchema):
    """
    Описание структуры ответа аутентификации.
    """


class RefreshTokenResponseSchema(TokenSchema):
    """
    Описание структуры ответа при обновлении токенов доступа.
    """


class RefreshTokenRequestSchema(BaseModel):
    """
    Описание структуры запроса для обновления токена.
    """
    model_config = ConfigDict(validate_by_name=True)

    refresh_token: str = Field(alias="refreshToken", default_factory=fake.sentence)
