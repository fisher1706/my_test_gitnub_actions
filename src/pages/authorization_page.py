import allure
from selenium.webdriver.support import expected_conditions as EC

from configuration import Links
from src.base_classes.base_page import BasePage


class AuthorizationPage(BasePage):
    ICON_ENTER = ("xpath", "//*[@id='login-enter']")
    PHONE_FIELD = ("xpath", "//*[@id='telephone']")
    BTN_NEXT = ("xpath", "//button[@class='auth_next']")
    CODE_FIELD = ("xpath", "//input[@id='code-auth']")
    AUTHORIZED_USER = ("xpath", "//*[@id='login-enter']/p")
    AUTHORIZATION_WARNING = ("xpath", "(//p[@data-input-error='error_user-exists']/span)[2]")
    AUTHORIZATION_ERROR = ("xpath", "//div[@class='field validate-error-with-message']/p")
    AUTHORIZATION_VERIFICATION_ERROR = ("xpath", "//div[@class='field code-auth validate-error-with-message']/p")

    def __init__(self, driver, settings):
        super().__init__(driver, settings)

    @allure.title("Open authorization form")
    def open_authorization_form(self):
        self.open_page(self.setting.base_url + Links.HOST)
        self.is_page_opened(self.setting.base_url + Links.HOST)

    @allure.title("Fill authorization form")
    def fill_authorization_form(self, user: dict, correct: bool = True):
        self.click_element(self.ICON_ENTER)
        self.fill_field_with_click(self.PHONE_FIELD, user.get("phone")[4:])
        if correct:
            self.click_element(self.BTN_NEXT)

    @allure.title("Confirm authorization form")
    def confirm_authorization_form(self, code: int):
        self.fill_field_with_click(self.CODE_FIELD, code)
        self.click_element(self.BTN_NEXT)

    @allure.title("Verify authorized user")
    def verify_authorized_user(self, user: dict):
        self.driver.refresh()
        user_name = self.wait.until(EC.element_to_be_clickable(self.AUTHORIZED_USER)).text
        assert user_name == user.get("name")

    @allure.title("Verify authorization warning message")
    def verify_authorization_warning(self):
        el = self.get_web_element(self.AUTHORIZATION_WARNING)
        assert el

    @allure.title("Verify authorization error message")
    def verify_authorization_error(self):
        el = self.get_web_element(self.AUTHORIZATION_ERROR)
        assert el

    @allure.title("Verify verification authorization error message")
    def verify_verification_authorization_error(self):
        el = self.get_web_element(self.AUTHORIZATION_VERIFICATION_ERROR)
        assert el
