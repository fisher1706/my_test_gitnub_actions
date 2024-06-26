import allure
import pytest

from configuration import Endpoints
from data.testing_dataset import AuthorizationUser
from src.base_classes.api_client import ApiClient
from src.schemas.authorization_schema import AuthorizationPositive, AuthorizationNegative, \
    AuthorizationCodeRegistrationPositive, AuthorizationCodeRegistrationNegative
from src.validate_response.validate_response_authorization import ValidateAuthorization


class TestAuthorization:
    @allure.title("Check positive authentication by api")
    @pytest.mark.parametrize("data", [AuthorizationUser.user_phone], ids=str)
    def test_authorization_positive(self, set_env_settings, data):
        response = ValidateAuthorization(ApiClient().post(
                url=set_env_settings.base_url,
                endpoint=ApiClient().update_endpoint(Endpoints.AUTHORIZATION_ENDPOINT, phone=data.get('phone'))
            )
        )

        response \
            .assert_status_code(200) \
            .validate(AuthorizationPositive) \
            .check_response_authorization_positive()

    @allure.title("Check authentication with out phone by api")
    @pytest.mark.parametrize("data", [AuthorizationUser.user_empty_phone], ids=str)
    def test_authorization_with_out_phone(self, set_env_settings, data):
        response = ValidateAuthorization(ApiClient().post(
                url=set_env_settings.base_url,
                endpoint=ApiClient().update_endpoint(Endpoints.AUTHORIZATION_ENDPOINT, phone=data.get('phone'))
            )
        )

        response \
            .assert_status_code(404) \
            .validate(AuthorizationNegative) \
            .check_response_authorization_negative()

    @allure.title("Validate authorization with valid code by api")
    @pytest.mark.parametrize("data", [AuthorizationUser.user_default_phone_default_code], ids=str)
    def test_validate_authorization_with_valid_code(self, set_env_settings, data):
        response = ValidateAuthorization(ApiClient().post(
                url=set_env_settings.base_url,
                endpoint=ApiClient().update_endpoint(Endpoints.AUTHORIZATION_CODE_REGISTRATION_ENDPOINT,
                                                     phone=data.get('phone'),
                                                     code=data.get('code'))
            )
        )

        response \
            .assert_status_code(200) \
            .validate(AuthorizationCodeRegistrationPositive) \
            .check_response_authorization_code_registration_positive()

    @allure.title("Validate authorization with invalid code by api")
    @pytest.mark.parametrize("data", [AuthorizationUser.user_phone_code], ids=str)
    def test_validate_authorization_with_invalid_code(self, set_env_settings, data):
        response = ValidateAuthorization(ApiClient().post(
                url=set_env_settings.base_url,
                endpoint=ApiClient().update_endpoint(Endpoints.AUTHORIZATION_CODE_REGISTRATION_ENDPOINT,
                                                     phone=data.get('phone'),
                                                     code=data.get('code'))
            )
        )

        response \
            .assert_status_code(200) \
            .validate(AuthorizationCodeRegistrationNegative) \
            .check_response_authorization_code_registration_negative()
