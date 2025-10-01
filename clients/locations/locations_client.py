import allure

from httpx import Response

from clients.api_client import APIClient
from clients.locations.locations_schema import OriginParams
from clients.public_http_builder import get_public_http_client

from tools.routes import APIRoutes


class LocationsClient(APIClient):
    """
    Клиент для работы с /api/v1/locations
    """

    @allure.step("Get locations")
    def get_locations_api(self) -> Response:
        """
        Метод получения списка всех адресов.

        :return: Ответ от сервера в виде объекта http.Response.
        """
        return self.get(url=APIRoutes.LOCATIONS)

    @allure.step("Get locations by origin")
    def get_locations_by_origin_api(self, origin_param: OriginParams) -> Response:
        """
        Метод получения списка адресов отсортированных по расстоянию от указанной исходной точки.

        :param origin_param: Начальная точка (координаты).
        :return: Ответ от сервера в виде объекта http.Response.
        """
        return self.get(url=APIRoutes.LOCATIONS, params={"origin": origin_param.origin})

    @allure.step("Get locations with limit")
    def get_locations_with_a_limit_api(self, limit: int) -> Response:
        """
        Метод получения списка адресов ограниченное лимитом.

        :param limit: Лимит ответов.
        :return: Ответ от сервера в виде объекта http.Response.
        """
        return self.get(url=APIRoutes.LOCATIONS, params={"size": limit})

    @allure.step("Get locations within a radius")
    def get_locations_within_a_radius(self, origin_param: OriginParams, radius: int) -> Response:
        """
        Метод получения списка адресов в указанном радиусе от указанной исходной точки.

        :param origin: Начальная точка (координаты).
        :param radius: Радиус в километрах
        :return: Ответ от сервера в виде объекта http.Response.
        """
        return self.get(url=APIRoutes.LOCATIONS, params={"origin": origin_param.origin, "radius": radius})


def get_location_client() -> LocationsClient:
    """
    Функция создаёт экземпляр LocationsClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию LocationsClient.
    """
    return LocationsClient(client=get_public_http_client())
