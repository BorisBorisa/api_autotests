from http import HTTPStatus

import allure
import pytest

from allure_commons.types import Severity

from clients.files.files_client import FileClient
from clients.files.files_schema import UploadFileResponseSchema, UploadFileRequestSchema

from config import settings
from fixtures.files import FileFixture
from tools.assertions.base import assert_status_code
from tools.assertions.files import assert_upload_file_response, assert_upload_file_content
from tools.assertions.schema import validate_json_schema

from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeatures
from tools.allure.storys import AllureStory


@pytest.mark.regression
@pytest.mark.files
@allure.epic(AllureEpic.FILES)
@allure.feature(AllureFeatures.FILES)
class TestFiles:
    @allure.story(AllureStory.UPDATE_ENTITY)
    @allure.title("Upload file")
    @allure.severity(Severity.NORMAL)
    def test_upload_file(self, file_client: FileClient):
        request = UploadFileRequestSchema(file_path=settings.test_data.image_png_file)
        response = file_client.upload_file_api(request)
        response_data = UploadFileResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.CREATED)
        assert_upload_file_response(request, response_data)

        validate_json_schema(response.json(), UploadFileResponseSchema.model_json_schema())

    @allure.story(AllureStory.GET_ENTITY)
    @allure.title("Get file")
    @allure.severity(Severity.NORMAL)
    def test_get_upload_file(self, file_client: FileClient, function_file: FileFixture):
        response = file_client.get_file_api(function_file.response.file_name)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_upload_file_content(function_file.request.file_path.read_bytes(), response.content)
