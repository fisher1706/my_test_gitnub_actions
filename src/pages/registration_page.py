import allure
from selenium.webdriver.support import expected_conditions as EC

from configuration import Links
from src.base_classes.base_page import BasePage


class RegistrationPage(BasePage):
    ICON_ENTER = ("xpath", "//*[@id='login-enter']")
    REGISTRATION_LINK = ("xpath", "//form[1]//a")
    PHONE_FIELD = ("xpath", "//*[@id='telephone']")
    NAME_FIELD = ("xpath", "//input[@data-validation='name']")
    EMAIL_FIELD = ("xpath", "//input[@data-validation='email']")
    BTN_NEXT = ("xpath", "//button[@class='auth_next']")
    CODE_FIELD = ("xpath", "//input[@id='code-auth']")
    BTN_TO_CABINET = ("xpath", "//button[@class='register__success-content-btn']")
    REGISTERED_USER = ("xpath", "//*[@id='login-enter']/p")
    PHONE_WARNING = ("xpath", "//span[@class='error_user-text']")
    EMAIL_WARNING = ("xpath", "//p[@data-input-error='error_email-exists']")
    PHONE_ERROR = ("xpath", "(//div[@class='field validate-error-with-message']/p)[1]")
    EMAIL_ERROR = ("xpath", "(//div[@class='field validate-error-with-message']/p)[4]")
    CODE_ERROR = ("xpath", "(//div[@class='field code-auth validate-error-with-message']/p)[1]")

    def __init__(self, driver, settings):
        super().__init__(driver, settings)

    @allure.title("Open registration form")
    def open_registration_form(self):
        self.open_page(self.setting.base_url + Links.HOST)
        self.is_page_opened(self.setting.base_url + Links.HOST)
        self.click_element(self.ICON_ENTER)
        self.click_element(self.REGISTRATION_LINK)

    @allure.title("Fill registration form")
    def fill_registration_form(self, user: dict, click: bool = True):
        self.fill_field_with_click(self.NAME_FIELD, user.get("name")[0])
        self.fill_field_with_click(self.PHONE_FIELD, user.get("phone")[4:])
        self.fill_field_with_click(self.EMAIL_FIELD, user.get("email"))
        if click:
            self.click_element(self.BTN_NEXT)

    @allure.title("Confirm registration form")
    def confirm_registration_form(self, code: str, correct: bool = True):
        self.fill_field_with_click(self.CODE_FIELD, code)
        self.click_element(self.BTN_NEXT)
        if correct:
            self.click_element(self.BTN_TO_CABINET)

    @allure.title("Verify registered user")
    def verify_registered_user(self, user: dict):
        self.driver.refresh()
        user_name = self.wait.until(EC.element_to_be_clickable(self.REGISTERED_USER)).text
        assert user_name == user.get("name")[0]

    @allure.title("Verify phone warning message")
    def verify_phone_warning(self):
        el = self.get_web_element(self.PHONE_WARNING)
        assert el

    @allure.title("Verify email warning message")
    def verify_email_warning(self):
        el = self.get_web_element(self.EMAIL_WARNING)
        assert el

    @allure.title("Verify phone error message")
    def verify_phone_error(self):
        el = self.get_web_element(self.PHONE_ERROR)
        assert el

    @allure.title("Verify email error message")
    def verify_email_error(self):
        el = self.get_web_element(self.EMAIL_ERROR)
        assert el

    @allure.title("Verify code error message")
    def verify_code_error(self):
        el = self.get_web_element(self.CODE_ERROR)
        assert el
