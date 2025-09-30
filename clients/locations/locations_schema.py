from pydantic import BaseModel, TypeAdapter, Field
from tools.fakers import fake


class LocationSchema(BaseModel):
    """
    Описание структуры местоположения.
    """
    id: int
    name: str
    description: str
    latitude: float
    longitude: float


GetLocationsResponseSchema = TypeAdapter(list[LocationSchema])
"""Описание структуры ответа на получение списка местоположений."""


class OriginParams(BaseModel):
    latitude: float = Field(default_factory=fake.random_latitude)
    longitude: float = Field(default_factory=fake.random_longitude)

    @property
    def origin(self) -> str:
        return f"{self.latitude},{self.longitude}"
