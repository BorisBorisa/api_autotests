from pydantic import BaseModel, Field, ConfigDict


class ErrorResponseSchema(BaseModel):
    """
    Модель описывающая структуру ответа API с ошибкой
    """
    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)

    message: str
    status_code: int = Field(alias="statusCode")
