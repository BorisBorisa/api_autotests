from pydantic import BaseModel, HttpUrl, Field, TypeAdapter
from datetime import datetime
from tools.fakers import fake


class CategorySchema(BaseModel):
    """
    Описание структуры категории.
    """
    id: int
    name: str
    slug: str
    image: HttpUrl
    creation_at: datetime = Field(alias="creationAt")
    updated_at: datetime = Field(alias="updatedAt")


GetCategoriesResponseSchema = TypeAdapter(list[CategorySchema])
"""Описание структуры ответа на получение списка категории."""


class CreateCategoryRequestSchema(BaseModel):
    """
    Описание запроса на создание категории.
    """
    name: str | None = Field(default_factory=fake.phrase)
    image: str | None = Field(default_factory=fake.uri)


class CreateCategoryResponseSchema(CategorySchema):
    """
    Описание структуры ответа на создание категории.
    """


class GetCategoryResponseSchema(CategorySchema):
    """
    Описание структуры ответа на запрос категории.
    """


class UpdateCategoryRequestSchema(CreateCategoryRequestSchema):
    """
    Описание запроса на обновление категории.
    """


class UpdateCategoryResponseSchema(CategorySchema):
    """
    Описание структуры ответа на запрос обновления категории.
    """
