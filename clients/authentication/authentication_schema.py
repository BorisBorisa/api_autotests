from pydantic import BaseModel, Field
from tools.fakers import fake


class LoginRequestSchema(BaseModel):
    """
    Описание структуры запроса на аутентификацию.
    """
    email: str = Field(default_factory=fake.email)
    password: str = Field(default_factory=fake.password)


class LoginResponseSchema(BaseModel):
    """
    Описание структуры ответа аутентификации.
    """
    access_token: str
    refresh_token: str


class RefreshRequestSchema(BaseModel):
    """
    Описание структуры запроса для обновления токена.
    """
    refresh_token: str = Field(alias="refreshToken", default_factory=fake.sentence)
