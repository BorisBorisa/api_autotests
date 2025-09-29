import pytest
from pydantic import BaseModel

from clients.files.files_client import get_file_client, FileClient
from clients.files.files_schema import UploadFileRequestSchema, UploadFileResponseSchema
from config import settings


class FileFixture(BaseModel):
    request: UploadFileRequestSchema
    response: UploadFileResponseSchema


@pytest.fixture
def file_client() -> FileClient:
    return get_file_client()


@pytest.fixture
def function_file(file_client: FileClient) -> FileFixture:
    """
    Фикстура для загрузки файла.

    :param file_client: Клиент для работы с роутом /api/v1/files.
    :return: Pydantic схема CategoryFixture c данными новой категории.
    """
    request = UploadFileRequestSchema(file_path=settings.test_data.image_png_file)
    response = file_client.upload_file(request)

    return FileFixture(request=request, response=response)
