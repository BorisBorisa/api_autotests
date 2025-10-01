import allure

from httpx import Response

from clients.api_client import APIClient
from clients.files.files_schema import UploadFileRequestSchema, UploadFileResponseSchema
from clients.public_http_builder import get_public_http_client
from tools.routes import APIRoutes


class FileClient(APIClient):
    """
    Клиент для работы с /api/v1/files
    """

    @allure.step("Upload file")
    def upload_file_api(self, request: UploadFileRequestSchema) -> Response:
        """
        Метод загрузки файла.

        :param request: Словарь с file_name, file_path.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(
            url=f"{APIRoutes.FILES}/upload",
            files={"file": (request.file_name, request.file_path.read_bytes())}
        )

    @allure.step("Get file by name {file_name}")
    def get_file_api(self, file_name: str) -> Response:
        """
        Метод получения файла.

        :param file_name: Имя файла.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(url=f"{APIRoutes.FILES}/{file_name}")

    def upload_file(self, request: UploadFileRequestSchema) -> UploadFileResponseSchema:
        response = self.upload_file_api(request)
        return UploadFileResponseSchema.model_validate_json(response.text)


def get_file_client() -> FileClient:
    """
    Функция создаёт экземпляр FilesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию FilesClient.
    """
    return FileClient(client=get_public_http_client())
