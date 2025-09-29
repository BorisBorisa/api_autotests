from pydantic import BaseModel, Field, HttpUrl, FilePath
from tools.fakers import fake

class UploadFileRequestSchema(BaseModel):
    """
    Описание структуры запроса на загрузку файла.
    """
    file_name: str = Field(default_factory=fake.word)
    file_path: FilePath


class UploadFileResponseSchema(BaseModel):
    """
    Описание структуры ответа на загрузку файла.
    """
    original_name: str = Field(alias="originalname")
    file_name: str = Field(alias="filename")
    location: HttpUrl
