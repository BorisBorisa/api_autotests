from clients.api_client import APIClient
from clients.locations.locations_schema import GetLocationsResponseSchema, OriginParams

from tools.routes import APIRoutes


class LocationsClient(APIClient):
    """
    Клиент для работы с /api/v1/locations
    """

    def get_locations_api(self):
        """
        Метод получения списка всех адресов.

        :return: Ответ от сервера в виде объекта httpx.Response.
        """
        return self.get(url=APIRoutes.LOCATIONS)

    def get_locations_by_origin_api(self, origin: OriginParams):
        """
        Метод получения списка адресов отсортированных по расстоянию от указанной исходной точки.

        :param origin: Начальная точка (координаты).
        :return: Ответ от сервера в виде объекта httpx.Response.
        """
        return self.get(url=APIRoutes.LOCATIONS, params={"origin": origin.origin})

    def get_locations_with_a_limit_api(self, limit: int):
        """
        Метод получения списка адресов ограниченное лимитом.

        :param limit: Лимит ответов.
        :return: Ответ от сервера в виде объекта httpx.Response.
        """
        return self.get(url=APIRoutes.LOCATIONS, params={"size": limit})

    def get_locations_within_a_radius(self, origin: OriginParams, radius: int):
        """
        Метод получения списка адресов в указанном радиусе от указанной исходной точки.

        :param origin: Начальная точка (координаты).
        :param radius: Радиус в километрах
        :return: Ответ от сервера в виде объекта httpx.Response.
        """
        return self.get(url=APIRoutes.LOCATIONS, params={"origin": origin.origin, "radius": radius})
