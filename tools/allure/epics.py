from enum import Enum


class AllureEpic(str, Enum):
    AUTHENTICATION = "Authentication service"
    STORE = "Store service"
    USERS = "Users service"
    FILES = "Files service"
