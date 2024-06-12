import allure
import pytest

from data.testing_data import DEFAULT_CODE_REGISTRATION, DEFAULT_CODE_AUTHORIZATION
from data.testing_dataset import RegistrationUserUi
from tests.ui.conftest import BaseTest


class TestRegistrationUser(BaseTest):
    @allure.step("Registration new user AWDEV-T506")
    @pytest.mark.parametrize("user, code", [
        (RegistrationUserUi.user_name_phone_email, DEFAULT_CODE_REGISTRATION)], ids=str)
    def test_registration_new_user_awdev_t506(self, user, code):
        self.registration_page.open_registration_form()
        self.registration_page.fill_registration_form(user=user)
        self.registration_page.confirm_registration_form(code=code)
        self.registration_page.verify_registered_user(user=user)

    @allure.step("Try to registration registered user AWDEV-T506")
    @pytest.mark.parametrize("user", [RegistrationUserUi.registered_user], ids=str)
    def test_try_registration_new_user_awdev_t506(self, user):
        self.registration_page.open_registration_form()
        self.registration_page.fill_registration_form(user=user)
        self.registration_page.verify_phone_warning()
        self.registration_page.verify_email_warning()

    @allure.step("Try to register new user with wrong credentials AWDEV-T506")
    @pytest.mark.parametrize("user", [RegistrationUserUi.new_user_with_wrong_credentials], ids=str)
    def test_registration_user_with_wrong_credentials_awdev_t506(self, user):
        self.registration_page.open_registration_form()
        self.registration_page.fill_registration_form(user=user, click=False)
        self.registration_page.verify_phone_error()
        self.registration_page.verify_email_error()

    @allure.step("Registration new user with wrong code AWDEV-T506")
    @pytest.mark.parametrize("user, code",
                             [(RegistrationUserUi.new_user_name_phone_email, DEFAULT_CODE_AUTHORIZATION)], ids=str)
    def test_registration_user_with_wrong_code_awdev_t506(self, user, code):
        self.registration_page.open_registration_form()
        self.registration_page.fill_registration_form(user=user)
        self.registration_page.confirm_registration_form(code=code, correct=False)
        self.registration_page.verify_code_error()
