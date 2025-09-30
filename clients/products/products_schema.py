from datetime import datetime
from pydantic import BaseModel, HttpUrl, TypeAdapter, Field, ConfigDict

from clients.categories.categories_schema import CategorySchema
from tools.fakers import fake


class ProductSchema(BaseModel):
    """
    Описание структуры продукта.
    """
    id: int
    title: str
    slug: str
    price: int | float
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
    model_config = ConfigDict(validate_by_name=True)

    title: str = Field(default_factory=fake.phrase)
    price: int | float = Field(default_factory=fake.price)
    description: str = Field(default_factory=fake.sentence)
    category_id: int = Field(alias="categoryId")
    images: list[str] = Field(default_factory=fake.uris_list)


class CreateProductResponseSchema(ProductSchema):
    """
    Описание структуры ответа на создание продукта.
    """


class GetProductResponseSchema(ProductSchema):
    """
    Описание структуры ответа на запрос продукта.
    """


class UpdateProductRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление продукта.
    """
    title: str | None = None
    price: int | float | None = None
    description: str | None = None
    images: list[str] | None = None


class UpdateProductResponseSchema(ProductSchema):
    """
    Описание структуры ответа на обновление продукта.
    """
