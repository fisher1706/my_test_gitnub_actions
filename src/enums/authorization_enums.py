from enum import Enum


class AuthorizationField(Enum):
    IS_EXIST = False


class ErrorMessageAuthorization(Enum):
    ERROR_MESSAGE = 'Request does not match any route.'


class AuthorizationCodeRegistration(Enum):
    VALID_RESPONSE = True
    INVALID_RESPONSE = False
