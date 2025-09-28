from httpx import Response
from pathlib import Path

from clients.api_client import APIClient
from clients.public_http_builder import get_public_http_client
from tools.routes import APIRoutes


class FilesClient(APIClient):
    """
    Клиент для работы с /api/v1/files
    """

    def upload_file_api(self, file_path: Path) -> Response:
        """
        Метод загрузки файла.

        :param file_path: Путь к файлу.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(url=f"{APIRoutes.FILES}/upload", files={"file": file_path.read_bytes()})

    def get_file_api(self, file_name: str) -> Response:
        """
        Метод получения файла.

        :param file_name: Имя файла.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(url=f"{APIRoutes.FILES}/{file_name}")


def get_file_client() -> FilesClient:
    """
    Функция создаёт экземпляр FilesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию FilesClient.
    """
    return FilesClient(client=get_public_http_client())
