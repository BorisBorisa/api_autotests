def assert_delete_response(response: bool):
    """
    Проверяет, что ответ на удаление успешный.

    :param response: Ответ API
    :return: AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert response, "Expected delete response to be True, but got False"
