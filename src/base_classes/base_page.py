import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utils.utils import Utils


class BasePage:

    def __init__(self, driver, setting):
        self.driver = driver
        self.setting = setting
        self.wait = WebDriverWait(
            driver,
            timeout=self.setting.default_timeout,
            poll_frequency=self.setting.default_poll_frequency
        )

    def open_page(self, url: str):
        with allure.step(f"Open '{url}' page"):
            self.driver.get(url)

    def is_page_opened(self, url: str):
        with allure.step(f"Page '{url}' is opened"):
            self.wait.until(EC.url_to_be(url))

    def make_screenshot(self, screenshot_name: str):
        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name=screenshot_name,
            attachment_type=AttachmentType.PNG
        )

    def click_element(self, element_name: [tuple, WebElement]):
        with allure.step(f"Click {element_name}"):
            self.wait.until(EC.element_to_be_clickable(element_name)).click()

    def fill_field(self, field_name: [tuple, WebElement], field_data: [str, int]):
        with allure.step(f"Fill '{field_name}' with data '{field_data}'"):
            self.wait.until(EC.element_to_be_clickable(field_name)).send_keys(field_data)

    def fill_field_with_click(self, field_name: [tuple, WebElement], field_data: [str, int]):
        with allure.step(f"Fill '{field_name}' with data '{field_data}'"):
            self.wait.until(EC.element_to_be_clickable(field_name)).click()
            self.wait.until(EC.element_to_be_clickable(field_name)).send_keys(field_data)

    def get_web_element(self, web_element: [tuple, WebElement]) -> WebElement:
        with allure.step(f"Get WebElement of '{web_element}'"):
            element = self.wait.until(EC.presence_of_element_located(web_element))
            return element

    def get_web_elements(self, web_element: [tuple, WebElement]) -> list:
        with allure.step(f"Get WebElements of '{web_element}'"):
            elements = self.wait.until(EC.visibility_of_all_elements_located(web_element))
            return elements

    def choose_random_element(self, web_element: [tuple, WebElement]):
        with allure.step(f"Choose random WebElements from '{web_element}'"):
            elements = self.get_web_elements(web_element)
            Utils.get_random_data_from_list(elements).click()
