from pydantic import BaseModel, EmailStr, HttpUrl, TypeAdapter, Field
from typing import Literal

from tools.fakers import fake


class UserSchema(BaseModel):
    """
    Описание структуры пользователя.
    """
    id: int
    name: str
    role: Literal["admin", "customer"]
    email: EmailStr
    password: str
    avatar: HttpUrl


GetUsersResponseSchema = TypeAdapter(list[UserSchema])
"""Описание структуры ответа на получение списка пользователей."""


class CreateUserRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание пользователя.
    """
    name: str = Field(default_factory=fake.first_name)
    email: str = Field(default_factory=fake.email)
    password: str = Field(default_factory=fake.password)
    avatar: str = Field(default_factory=fake.uri)


class CreateUserResponseSchema(UserSchema):
    """
    Описание структуры ответа на создание пользователя.
    """


class UpdateUserRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление пользователя.
    """
    name: str | None = Field(default_factory=fake.first_name)
    role: str | None = Field(default_factory=fake.role)
    email: str | None = Field(default_factory=fake.email)
    password: str | None = Field(default_factory=fake.password)
    avatar: str | None = Field(default="https://picsum.photos/800")


if __name__ == '__main__':
    print(UpdateUserRequestSchema())
