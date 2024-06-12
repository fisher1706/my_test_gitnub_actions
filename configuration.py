from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Literal

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    env: Literal["qa", "dev"]
    default_timeout: int = 20
    default_poll_frequency: int = 1
    base_url: str
    redwood_url: str
    redwood_token: dict
    db_url: str
    download_dir: str = str(Path(__file__).parent)

    """
    method to init Settings with values from corresponding .env file
    """
    @classmethod
    def set_environment(cls, env: str) -> Settings:
        path = Path(__file__).parent
        return cls(_env_file=path.joinpath(f".env.{env}"), env=env)


@dataclass
class Endpoints:
    REGISTRATION_ENDPOINT: str = "/rest/V1a/customer/registration/check"
    REGISTRATION_CODE_ENDPOINT: str = "/rest/V1a/customer/registration/check_code"
    AUTHORIZATION_ENDPOINT: str = "/rest/V1a/customer/sms"
    AUTHORIZATION_CODE_REGISTRATION_ENDPOINT: str = "/rest/V1a/customer/login"
    SHIPPING_IN_STORE_ENDPOINT: str = "/:locale/rest/V1a/carts/mine/shipping-information"


@dataclass
class Links:
    HOST: str = "/"
    CATALOG_PAGE: str = "/odjag.html"
    CHECKOUT_PAGE: str = "/checkout/"
    CART_PAGE: str = "/checkout/cart/"


if __name__ == '__main__':
    settings = Settings.set_environment("qa")
    print(repr(settings))
