import pytest
from configuration import Settings


"""
add the "environment" variable to "pytestconfig" with the "pytest_addoption" hook
"""


def pytest_addoption(parser):
    parser.addoption("--environment", action="store", default="dev", help="choose environment", choices=("qa", "dev"))
    parser.addoption("--browser_name", action="store", default="chrome", help="choose browser",
                     choices=("chrome", "firefox"))


"""
form env settings depending on the "environment" variable
"""


@pytest.fixture(scope="session")
def set_env_settings(pytestconfig) -> Settings:
    environment = pytestconfig.getoption("--environment")
    settings = Settings.set_environment(environment)
    return settings
