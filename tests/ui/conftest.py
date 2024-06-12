import chromedriver_autoinstaller
import pytest
from selenium import webdriver

from src.pages.authorization_page import AuthorizationPage
from src.pages.cart_page import CartPage
from src.pages.catalog_page import CatalogPage
from src.pages.checkout_page import CheckoutPage
from src.pages.registration_page import RegistrationPage


@pytest.fixture(autouse=True)
def set_driver(pytestconfig, request):
    driver = None
    browser = pytestconfig.getoption("--browser_name")
    if browser == "chrome":
        chromedriver_autoinstaller.install()
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=options)
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        options.headless = True
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-extensions')
        options.add_argument('--start-maximized')

    request.cls.set_driver = driver
    yield driver
    driver.quit()


class BaseTest:
    authorization_page: AuthorizationPage
    registration_page: RegistrationPage
    catalog_page: CatalogPage
    cart_page: CartPage
    checkout_page: CheckoutPage

    @pytest.fixture(autouse=True)
    def setup(self, request, set_driver, set_env_settings):
        request.cls.authorization_page = AuthorizationPage(set_driver, set_env_settings)
        request.cls.registration_page = RegistrationPage(set_driver, set_env_settings)
        request.cls.catalog_page = CatalogPage(set_driver, set_env_settings)
        request.cls.cart_page = CartPage(set_driver, set_env_settings)
        request.cls.checkout_page = CheckoutPage(set_driver, set_env_settings)
