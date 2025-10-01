from enum import Enum


class AllureFeatures(str, Enum):
    AUTHENTICATION = "Authentication"
    CATEGORIES = "Categories"
    FILES = "Files"
    LOCATIONS = "Locations"
    PRODUCTS = "Products"
    USERS = "Users"
