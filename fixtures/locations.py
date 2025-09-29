import pytest

from clients.locations.locations_client import get_location_client, LocationsClient


@pytest.fixture
def locations_client() -> LocationsClient:
    return get_location_client()
