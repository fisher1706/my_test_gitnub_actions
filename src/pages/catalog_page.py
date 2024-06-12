import allure

from configuration import Links
from src.base_classes.base_page import BasePage


class CatalogPage(BasePage):
    BTN_TO_CART = ("xpath", "(//*[@id='product_form']/button)[1]")
    selected_product = lambda self, number: ("xpath", f"(//a/div/img)[{number}]")

    def __init__(self, driver, settings):
        super().__init__(driver, settings)

    @allure.title("Open catalog page")
    def open_catalog_page(self):
        self.open_page(self.setting.base_url + Links.CATALOG_PAGE)
        self.is_page_opened(self.setting.base_url + Links.CATALOG_PAGE)

    @allure.title("Choose some product from catalog")
    def choose_some_product_from_catalog(self, number: int = 1):
        self.click_element(self.selected_product(number))
        self.click_element(self.BTN_TO_CART)
