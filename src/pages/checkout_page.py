import allure

from configuration import Links
from data.testing_data import DEFAULT_CODE_AUTHORIZATION, DEFAULT_CITY
from src.base_classes.base_page import BasePage
from utils.utils import Utils


class CheckoutPage(BasePage):
    NEW_CLIENT = ("xpath", "//span[@class='new active-client']")
    REGULAR_CLIENT = ("xpath", "//span[@class='auth']")

    FIELD_LAST_NAME = ("xpath", "//input[@data-input-name='lastname']")
    FIELD_FIRST_NAME = ("xpath", "//input[@data-input-name='firstname']")
    FIELD_PHONE = ("xpath", "//input[@data-input-name='phone']")
    FIELD_EMAIL = ("xpath", "//input[@data-input-name='customerEmail']")
    BTN_NEXT = ("xpath", "//button[@class='form-client__content-btn reg-next']")
    FIELD_DATA_VALIDATION = ("xpath", "//input[@data-validation='code']")
    BTN_ENTER = ("xpath", "//button[@class='form-client__content-btn reg-next']")

    BTN_CONFIRM_ORDER = ("xpath", "//button[@class='button-red confirm-order--button']")
    ICON_EDIT_ORDER = ("xpath", "//div[@class='edit-borderless']")
    BTN_SHOP = ("xpath", "//button[@class='button-red shop-button']")
    BTN_NP = ("xpath", "//button/ul/li")

    BTN_CITY = ("xpath", "//button[@data-popup='location']")
    DEFAULT_CITES = ("xpath", "//*[@id='location']//ul/li")

    CLICK_SEARCH_CITY = ("xpath", "//*[@id='location']//form/span")
    FIELD_SEARCH_CITY = ("xpath", "//*[@id='location']//input")
    REGION_CITY = ("xpath", "//*[@id='location']//form//li")

    SELECT_SHOP = ("xpath", "//*[@id='shipping-method-content-instore']//div/span[2]")
    # SELECT_SHOP = ("xpath", "//*[@id='select_instore_location-1']")
    SELECTOR = ("xpath", "//*[@id='select_instore_location-1']")
    REGION_SHOP = ("xpath", "(//ul)[4]/li/p")

    def __init__(self, driver, settings):
        super().__init__(driver, settings)

    @allure.title("Verify checkout page is opened")
    def verify_checkout_page_is_opened(self):
        self.is_page_opened(self.setting.base_url + Links.CHECKOUT_PAGE)

    @allure.title("Choose user city")
    def choose_user_city(self, if_default: bool = True):
        self.click_element(self.BTN_CITY)
        if if_default:
            self.choose_random_element(self.DEFAULT_CITES)
        else:
            self.click_element(self.CLICK_SEARCH_CITY)
            self.fill_field_with_click(self.FIELD_SEARCH_CITY, DEFAULT_CITY)
            self.choose_random_element(self.REGION_CITY)

    @allure.step("Choose user shop")
    def choose_user_shop(self):
        self.click_element(self.SELECT_SHOP)
        # time.sleep(2)
        # self.choose_random_element(self.REGION_SHOP)
        # time.sleep(10)

    @allure.title("Fill checkout registration form")
    def fill_registration_form(self):
        user = Utils().user_profile()
        self.fill_field_with_click(self.FIELD_FIRST_NAME, user.get("name").split(" ")[0])
        self.fill_field_with_click(self.FIELD_LAST_NAME, user.get("name").split(" ")[1])
        self.fill_field_with_click(self.FIELD_PHONE, user.get("phone_number")[4:])
        self.fill_field_with_click(self.FIELD_EMAIL, user.get("email"))
        self.click_element(self.BTN_NEXT)
        self.fill_field_with_click(self.FIELD_DATA_VALIDATION, DEFAULT_CODE_AUTHORIZATION)
        self.click_element(self.BTN_ENTER)
