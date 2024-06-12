from __future__ import annotations

from data.testing_data import DEFAULT_PHONE, DEFAULT_NAME, DEFAULT_EMAIL
from src.base_classes.validade_response_base import ValidateResponseBase
from src.enums.authorization_enums import AuthorizationField, ErrorMessageAuthorization, AuthorizationCodeRegistration


class ValidateAuthorization(ValidateResponseBase):
    def check_response_authorization_positive(self) -> ValidateAuthorization:
        assert self.response_json.get("exists") == AuthorizationField.IS_EXIST.value
        return self

    def check_response_authorization_negative(self) -> ValidateAuthorization:
        assert self.response_json.get("message") == ErrorMessageAuthorization.ERROR_MESSAGE.value
        return self

    def check_response_authorization_code_registration_positive(self) -> ValidateAuthorization:
        assert self.response_json.get("success") == AuthorizationCodeRegistration.VALID_RESPONSE.value
        assert self.response_json.get("phone") == DEFAULT_PHONE
        assert self.response_json.get("name") == DEFAULT_NAME
        assert self.response_json.get("surname") == DEFAULT_NAME
        assert self.response_json.get("email") == DEFAULT_EMAIL
        return self

    def check_response_authorization_code_registration_negative(self) -> ValidateAuthorization:
        assert self.response_json.get("success") == AuthorizationCodeRegistration.INVALID_RESPONSE.value
        return self
