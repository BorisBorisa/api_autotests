from pydantic import BaseModel, Field, HttpUrl


class UploadFileResponseSchema(BaseModel):
    """
    Описание структуры ответа на загрузку файла.
    """
    original_name: str = Field(alias="originalname")
    filename: str
    location: HttpUrl
