from faker import Faker
from random import choice, randint


class Fake:
    """
    Класс для генерации случайных тестовых данных.
    """

    def __init__(self, faker: Faker):
        """
        :param faker: Экземпляр класса Faker, используемый для генерации данных.
        """
        self.faker = faker

    def first_name(self) -> str:
        """
        Генерирует случайное имя.

        :return: Случайное имя.
        """
        return self.faker.first_name()

    def email(self, domain: str | None = None) -> str:
        """
        Генерирует случайный email.

        :param domain: Домен электронной почты (например, "example.com").
        Если не указан, будет использован случайный домен.
        :return: Случайный email.
        """
        return self.faker.email(domain=domain)

    def password(self) -> str:
        """
        Генерирует случайный пароль.

        :return: Случайный пароль.
        """
        return self.faker.password(special_chars=False)

    def sentence(self) -> str:
        """
        Генерирует случайное предложение.

        :return: Случайное предложение.
        """
        return self.faker.sentence()

    def phrase(self) -> str:
        """
        Генерирует случайное словосочетание.

        :return: Случайное словосочетание.
        """
        return self.faker.sentence(nb_words=3, variable_nb_words=True)[:-1]

    def uri(self) -> str:
        """
        Генерирует случайное URI.

        :return: Случайный URI.
        """
        return self.faker.uri()

    def uris_list(self) -> list[str]:
        """
        Генерирует словарь случайных URI.

        :return: Словарь со случайными URI.
        """
        return [self.uri() for _ in range(randint(1, 4))]

    def price(self) -> float:
        """
        Генерирует случайную цену.

        :return: Случайная цена (float).
        """
        return self.faker.pyfloat(
            right_digits=2,
            min_value=1,
            max_value=10000
        )

    @staticmethod
    def role() -> str:
        """
        Генерирует случайную роль из допустимых.

        :return: Случайная роль из допустимых.
        """
        roles = ("admin", "customer")  # Перенести в конфиг!
        return choice(roles)


fake = Fake(faker=Faker())
