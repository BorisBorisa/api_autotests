from datetime import datetime
from pydantic import BaseModel, HttpUrl, TypeAdapter, Field

from clients.categories.categories_schema import CategorySchema
from tools.fakers import fake


class ProductSchema(BaseModel):
    """
    Описание структуры продукта.
    """
    id: int
    title: str
    slug: str
    price: float
    description: str
    category: CategorySchema
    images: list[HttpUrl]
    creation_at: datetime = Field(alias="creationAt")
    updated_at: datetime = Field(alias="updatedAt")


GetProductsResponseSchema = TypeAdapter(list[ProductSchema])
"""Описание структуры ответа на получение списка продуктов."""


class CreateProductRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание продукта.
    """
    title: str = Field()
    price: int = Field()
    description: str = Field()
    category_id: str = Field(alias="categoryId")
    images: list[str] = Field()


class CreateProductResponseSchema(BaseModel):
    """
    Описание структуры ответа на создание продукта.
    """
    title: str
    slug: str
    price: float
    description: str
    images: list[HttpUrl]
    category: CategorySchema
    id: int
    creation_at: datetime = Field(alias="creationAt")
    updated_at: datetime = Field(alias="updatedAt")


class UpdateProductRequestSchema(BaseModel):
    """
    Описание структуры ответа на создание продукта.
    """
    title: str | None = Field(default_factory=fake.phrase)
    price: float | None = Field(default_factory=fake.price)
    description: str | None = Field(default_factory=fake.sentence)
    category_id: str | None = Field(alias="categoryId")  # необходимо передавать действительно значение
    images: list[HttpUrl] | None = Field(default_factory=fake.uris_list)
