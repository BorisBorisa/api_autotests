from datetime import datetime

from pydantic import BaseModel, EmailStr, HttpUrl, TypeAdapter, Field, ConfigDict
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


class GetUserResponseSchema(UserSchema):
    """
    Описание структуры ответа на получение пользователя.
    """


GetUsersResponseSchema = TypeAdapter(list[UserSchema])
"""Описание структуры ответа на получение списка пользователей."""


class CreateUserRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание пользователя.
    """
    name: str | None = Field(default_factory=fake.first_name)
    email: str | None = Field(default_factory=fake.email)
    password: str | None = Field(default_factory=fake.password)
    avatar: str | None = Field(default_factory=fake.uri)


class CreateUserResponseSchema(UserSchema):
    """
    Описание структуры ответа на создание пользователя.
    """


class UserProfileResponseSchema(UserSchema):
    """
    Описание структуры ответа на запрос профиля авторизованного пользователя.
    """


class UpdateUserRequestSchema(CreateUserRequestSchema):
    """
    Описание структуры запроса на обновление пользователя.
    """
    role: str | None = Field(default_factory=fake.role)


class UpdateUserResponseSchema(UserSchema):
    """
    Описание структуры ответа на обновление пользователя.
    """


class EmailAvailabilityRequestSchema(BaseModel):
    """
    Описание структуры запроса проверки зарегистрирован ли уже адрес эл. почты.
    """
    email: str = Field(default_factory=fake.email)


class EmailAvailabilityResponseSchema(BaseModel):
    """
    Описание структуры ответа проверки доступности почты.
    """
    is_available: bool = Field(alias="isAvailable")


class UserNotFoundResponseSchema(BaseModel):
    """
    Описание структуры ответа получения пользователя с невалидным id.
    """
    path: str
    timestamp: datetime
    name: str
    message: str
