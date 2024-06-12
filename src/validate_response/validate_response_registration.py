from __future__ import annotations

from src.base_classes.validade_response_base import ValidateResponseBase
from src.enums.registration_enums import ErrorMessageRegistration, RegistrationCode
from src.enums.rest_endpoint_field import RestEndpointField


class ValidateRegistration(ValidateResponseBase):

    def check_response_registration_positive(self, data: dict) -> ValidateRegistration:
        for key, value in data.items():
            if key and value != "":
                assert not self.response_json.get(f"{key}_exists")
        return self

    def check_response_registration_negative(self) -> ValidateRegistration:
        assert self.response_json.get("message") == ErrorMessageRegistration.REQUIRED_FIELD.value
        assert self.response_json.get("parameters").get("fieldName") in RestEndpointField.list()
        return self

    def check_response_registration_code_positive(self) -> ValidateRegistration:
        assert self.response_json.get("success") == RegistrationCode.VALID_SUCCESS.value
        return self

    def check_response_registration_code_negative(self) -> ValidateRegistration:
        assert self.response_json.get("success") == RegistrationCode.INVALID_SUCCESS.value
        assert self.response_json.get("error") == ErrorMessageRegistration.ERROR_REGISTRATION_CODE.value
        return self
