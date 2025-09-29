from enum import Enum


class APIRoutes(str, Enum):
    PRODUCTS = "api/v1/products"
    USERS = "api/v1/users"
    AUTH = "api/v1/auth"
    CATEGORIES = "api/v1/categories"
    FILES = "api/v1/files"
    LOCATIONS = "api/v1/locations"

    def __str__(self):
        return self.value
