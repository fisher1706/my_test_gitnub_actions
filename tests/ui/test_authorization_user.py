import allure
import pytest

from data.testing_data import DEFAULT_CODE_REGISTRATION, DEFAULT_CODE_AUTHORIZATION
from data.testing_dataset import AuthorizationUserUi
from tests.ui.conftest import BaseTest


class TestRegistrationUser(BaseTest):
    @allure.title("Test Authorization authorized user AWDEV-T491")
    @pytest.mark.parametrize("user, code", [(AuthorizationUserUi.authorized_user, DEFAULT_CODE_AUTHORIZATION)], ids=str)
    def test_authorization_user_awdew_t491(self, user, code):
        self.authorization_page.open_authorization_form()
        self.authorization_page.fill_authorization_form(user=user)
        self.authorization_page.confirm_authorization_form(code=code)
        self.authorization_page.verify_authorized_user(user=user)

    @allure.title("Test try authorization new user AWDEV-T491")
    @pytest.mark.parametrize("user", [AuthorizationUserUi.new_user], ids=str)
    def test_try_authorization_new_user_awdew_t491(self, user):
        self.authorization_page.open_authorization_form()
        self.authorization_page.fill_authorization_form(user=user)
        self.authorization_page.verify_authorization_warning()

    @allure.title("Test try authorization user with invalid credentials AWDEV-T491")
    @pytest.mark.parametrize("user", [AuthorizationUserUi.user_with_invalid_credentials], ids=str)
    def test_authorization_user_with_invalid_credentials_awdew_t491(self, user):
        self.authorization_page.open_authorization_form()
        self.authorization_page.fill_authorization_form(user=user, correct=False)
        self.authorization_page.verify_authorization_error()

    @allure.title("Test try authorization with invalid code AWDEV-T491")
    @pytest.mark.parametrize("user, code", [(AuthorizationUserUi.authorized_user, DEFAULT_CODE_REGISTRATION)], ids=str)
    def test_authorization_user_with_invalid_code_awdew_t491(self, user, code):
        self.authorization_page.open_authorization_form()
        self.authorization_page.fill_authorization_form(user=user)
        self.authorization_page.confirm_authorization_form(code=code)
        self.authorization_page.verify_verification_authorization_error()
