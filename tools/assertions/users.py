from clients.users.users_schema import UserSchema
from tools.assertions.base import assert_equal


def assert_user(actual: UserSchema, expected: UserSchema):
    """
    Проверяет корректность данных пользователя.

    :param actual: Фактические данные пользователя.
    :param expected: Ожидаемые данные пользователя.
    :return: AssertionError: Если хотя бы одно поле не совпадает.
    """

    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.name, expected.name, "name")
    assert_equal(actual.role, expected.role, "role")
    assert_equal(actual.email, expected.email, "email")
    assert_equal(actual.password, expected.password, "password")
    assert_equal(actual.avatar, expected.avatar, "avatar")
