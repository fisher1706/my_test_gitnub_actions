from enum import Enum


class ErrorMessageRegistration(Enum):
    REQUIRED_FIELD = '"%fieldName" is required. Enter and try again.'
    ERROR_REGISTRATION_CODE = 'A customer with the same email address already exists in an associated website.'


class RegistrationCode(Enum):
    VALID_SUCCESS = True
    INVALID_SUCCESS = False


if __name__ == '__main__':
    print(ErrorMessageRegistration.REQUIRED_FIELD.value)
