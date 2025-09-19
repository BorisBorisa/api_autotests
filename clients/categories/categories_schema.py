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
    name: str = Field(default_factory=fake.phrase)
    image: str = Field(default_factory=fake.uri)


class UpdateCategoryRequestSchema(BaseModel):
    """
    Описание запроса на обновление категории.
    """
    name: str = Field(default_factory=fake.phrase)
    image: str = Field(default_factory=fake.uri)
