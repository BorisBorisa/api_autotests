from http import HTTPStatus

import pytest

from clients.locations.locations_client import LocationsClient
from clients.locations.locations_schema import GetLocationsResponseSchema, OriginParams
from tools.assertions.base import assert_status_code
from tools.assertions.locations import assert_get_locations_response_len
from tools.assertions.schema import validate_json_schema

from config import settings


@pytest.mark.regression
@pytest.mark.locations
class TestLocations:
    def test_get_locations(self, locations_client: LocationsClient):
        response = locations_client.get_locations_api()

        assert_status_code(response.status_code, HTTPStatus.OK)

        validate_json_schema(response.json(), GetLocationsResponseSchema.json_schema())

    def test_get_locations_by_origin(self, locations_client: LocationsClient):
        param = OriginParams()
        response = locations_client.get_locations_by_origin_api(param)

        assert_status_code(response.status_code, HTTPStatus.OK)

        validate_json_schema(response.json(), GetLocationsResponseSchema.json_schema())

    def test_get_locations_with_limit(self, locations_client: LocationsClient):
        limit = settings.test_data.response_limit
        response = locations_client.get_locations_with_a_limit_api(limit)
        response_data = GetLocationsResponseSchema.validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_locations_response_len(response_data, limit)

        validate_json_schema(response.json(), GetLocationsResponseSchema.json_schema())

    def test_get_locations_with_radius(self, locations_client: LocationsClient):
        radius = settings.test_data.search_radius
        param = OriginParams()
        response = locations_client.get_locations_within_a_radius(param, radius)

        assert_status_code(response.status_code, HTTPStatus.OK)

        validate_json_schema(response.json(), GetLocationsResponseSchema.json_schema())
