from pydantic import BaseModel, TypeAdapter


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
    latitude: float
    longitude: float

    @property
    def origin(self) -> str:
        return f"{self.latitude},{self.longitude}"
