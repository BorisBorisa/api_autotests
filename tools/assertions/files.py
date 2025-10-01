import allure

from clients.files.files_schema import UploadFileRequestSchema, UploadFileResponseSchema
from tools.assertions.base import assert_equal
from tools.routes import APIRoutes
from config import settings


@allure.step("Check upload file response")
def assert_upload_file_response(request: UploadFileRequestSchema, response: UploadFileResponseSchema):
    """
    Проверяет, что ответ на загрузку файла соответствует запросу.

    :param request: Исходный запрос на загрузку файла.
    :param response: Ответ API с данными загрузки.
    :return: AssertionError: Если хотя бы одно поле не совпадает.
    """

    expected_url = f"{settings.http_client.url}{APIRoutes.FILES}/{response.file_name}"

    assert_equal(response.original_name, request.file_name, "name")
    assert_equal(str(response.location), expected_url, "upload file url")


@allure.step("Check uploaded file content")
def assert_upload_file_content(request_content: bytes, response_content: bytes):
    """
    Проверяет, что содержимое загруженного файла совпадает с исходным.

    :param request_content: Байтовые данные исходного файла.
    :param response_content: Байтовые данные файла из ответа.
    :raises AssertionError: Если содержимое файлов отличается.
    """
    assert_equal(response_content, request_content, "file")
