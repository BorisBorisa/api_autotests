import allure

from clients.locations.locations_schema import GetLocationsResponseSchema


@allure.step("Check get locations response len")
def assert_get_locations_response_len(response: GetLocationsResponseSchema, expected_len: int):
    """
    Проверяет что фактическая длинна ответа соответстввует ожидаемому.

    :param response: Ответ от API при запросе списка адресов.
    :param expected_len: Ожидаемая длинна ответа
    :return:
    """
    assert len(response) == expected_len, (
        f'Incorrect get locations response length. '
        f'Expected length: {expected_len}. '
        f'Actual length: {len(response)}'
    )
