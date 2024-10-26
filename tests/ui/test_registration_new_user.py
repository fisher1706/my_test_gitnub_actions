import allure
import pytest

from data.testing_data import DEFAULT_CODE_REGISTRATION, DEFAULT_CODE_AUTHORIZATION
from data.testing_dataset import RegistrationUserUi
from tests.ui.conftest import BaseTest


class TestRegistrationUser(BaseTest):
    @allure.step("Try to registration registered user AWDEV-T506")
    @pytest.mark.parametrize("user", [RegistrationUserUi.registered_user], ids=str)
    def test_try_registration_new_user_awdev_t506(self, user, set_env_settings):
        env = set_env_settings.env
        print(env)
        self.registration_page.open_registration_form()
        self.registration_page.fill_registration_form(user=user)
        self.registration_page.verify_phone_warning()
        self.registration_page.verify_email_warning()
