import allure
import pytest

from configuration import Endpoints
from data.testing_dataset import RegistrationUser
from src.base_classes.api_client import ApiClient
from src.schemas.registration_schema import RegistrationPositive, RegistrationNegative, RegistrationCodeValid, \
    RegistrationCodeInvalid
from src.validate_response.validate_response_registration import ValidateRegistration


class TestRegistration:
    @allure.title("Check positive registration by api")
    @pytest.mark.parametrize("data", [
        RegistrationUser.user_email_phone
    ], ids=str)
    def test_registration_positive(self, set_env_settings, data):
        response = ValidateRegistration(ApiClient().post(
                url=set_env_settings.base_url,
                endpoint=Endpoints.REGISTRATION_ENDPOINT,
                body=data
            )
        )

        response \
            .assert_status_code(200) \
            .validate(RegistrationPositive) \
            .check_response_registration_positive(data)

    @allure.title("Check negative registration by api")
    @pytest.mark.parametrize("data", [
        RegistrationUser.user_phone,
        RegistrationUser.user_email
    ], ids=str)
    def test_registration_negative(self, set_env_settings, data):
        response = ValidateRegistration(ApiClient().post(
                url=set_env_settings.base_url,
                endpoint=Endpoints.REGISTRATION_ENDPOINT,
                body=data
            )
        )

        response \
            .assert_status_code(400) \
            .validate(RegistrationNegative) \
            .check_response_registration_negative()

    @allure.title("Check registration code by api positive")
    @pytest.mark.parametrize("data", [RegistrationUser.user_registration_code_valid], ids=str)
    def test_registration_code_positive(self, set_env_settings, data):
        response = ValidateRegistration(ApiClient().post(
                url=set_env_settings.base_url,
                endpoint=Endpoints.REGISTRATION_CODE_ENDPOINT,
                body=data
            )
        )

        response \
            .assert_status_code(200) \
            .validate(RegistrationCodeValid) \
            .check_response_registration_code_positive()

    @allure.title("Check registration code by api negative")
    @pytest.mark.parametrize("data", [RegistrationUser.created_user_registration_code], ids=str)
    def test_registration_code_negative(self, set_env_settings, data):
        response = ValidateRegistration(ApiClient().post(
                url=set_env_settings.base_url,
                endpoint=Endpoints.REGISTRATION_CODE_ENDPOINT,
                body=data
            )
        )

        response \
            .assert_status_code(200) \
            .validate(RegistrationCodeInvalid) \
            .check_response_registration_code_negative()
