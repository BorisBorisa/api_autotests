from faker import Faker
from random import choice

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
        return self.faker.password()

    def sentence(self) -> str:
        """
        Генерирует случайное предложение.

        :return: Случайное предложение.
        """
        return self.faker.sentence()

    @staticmethod
    def role() -> str:
        """
        Генерирует случайную роль из допустимых.

        :return: Случайная роль из допустимых.
        """
        roles = ("admin", "customer") # Перенести в конфиг!
        return choice(roles)


fake = Fake(faker=Faker())
