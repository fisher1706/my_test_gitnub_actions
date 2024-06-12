import allure
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC

from configuration import Links
from src.base_classes.base_page import BasePage


class CartPage(BasePage):
    QUANTITY_FIELD = ("xpath", "//input[@class='countInput']")
    BTN_MAKE_ORDER = ("xpath", "//button[@class='button-red make-order']")
    BTN_INCREMENT_QUANTITY = ("xpath", "//button[contains(@class, 'plus increment-count')]")
    BTN_DECREMENT_QUANTITY = ("xpath", "(//button[contains(@class, 'btn--minus')])[1]")
    BTN_DELETE = ("xpath", "//button[contains(@class, 'delete-button')]")
    QUANTITY_WARNING = ("xpath", "//header/div[2]/div")
    BTN_QUANTITY_WARNING_OK = ("xpath", "(//button[text() = 'OK'])[1]")

    def __init__(self, driver, settings):
        super().__init__(driver, settings)

    @allure.title("Switch to cart")
    def switch_to_cart(self):
        self.open_page(self.setting.base_url + Links.CART_PAGE)
        self.is_page_opened(self.setting.base_url + Links.CART_PAGE)

    @allure.title("Get quantity ordered product")
    def get_quantity_ordered_product(self):
        return self.wait.until(EC.element_to_be_clickable(self.QUANTITY_FIELD)).get_attribute("value")

    @allure.title("Verify cart page is closed")
    def check_quantity_ordered_product(self, number: str = "1"):
        quantity = self.get_quantity_ordered_product()
        assert quantity == number

    @allure.step("Work with quantity warning")
    def work_with_quantity_warning(self):
        self.click_element(self.BTN_QUANTITY_WARNING_OK)

    @allure.title("Increment quantity ordered product")
    def increment_quantity_ordered_product(self) -> WebElement:
        quantity_before = self.get_quantity_ordered_product()
        self.click_element(self.BTN_INCREMENT_QUANTITY)
        el = self.get_web_element(self.QUANTITY_WARNING)
        if el:
            self.work_with_quantity_warning()
        else:
            quantity_after = self.get_quantity_ordered_product()
            assert int(quantity_before) == int(quantity_after) - 1
        return el

    @allure.title("Decrement quantity ordered product")
    def decrement_quantity_quantity_product(self):
        quantity_before = self.get_quantity_ordered_product()
        if int(quantity_before) == 1:
            el = self.increment_quantity_ordered_product()
            if not el:
                self.click_element(self.BTN_DECREMENT_QUANTITY)
                quantity_after = self.get_quantity_ordered_product()
                assert int(quantity_before) == int(quantity_after) - 1
            else:
                return
        else:
            quantity_after = self.get_quantity_ordered_product()
            assert int(quantity_before) == int(quantity_after) - 1

    @allure.title("Order some product")
    def make_order(self):
        self.click_element(self.BTN_MAKE_ORDER)
        self.is_page_opened(self.setting.base_url + Links.CHECKOUT_PAGE)
