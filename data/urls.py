from enum import Enum, unique

@unique
class Urls(Enum):
    URL_PROD = "https://release-gs.qa-playground.com/api/v1"
    URL_DEV = "https://dev-gs.qa-playground.com/api/v1"
