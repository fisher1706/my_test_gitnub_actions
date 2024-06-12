import dataclasses
from src.generators.user import User
from src.generators.redwood import RedWood
from data.redwood_data import productItems, balances
from data.testing_data import DEFAULT_EMAIL, DEFAULT_PHONE, DEFAULT_CODE_AUTHORIZATION, DEFAULT_NAME, \
    DEFAULT_CODE_REGISTRATION, DEFAULT_PHONE_SECOND, DEFAULT_NAME_SECOND
from utils.utils import Utils


@dataclasses.dataclass
class RegistrationUser:
    user_email = User().set_user_data(email=Utils().random_email()).build()
    user_phone = User().set_user_data(phone=Utils().random_phone()).build()
    user_email_phone = User().set_user_data(email=Utils().random_email(), phone=Utils().random_phone()).build()
    user_registration_code_valid = User().set_user_data(
        phone=Utils().random_phone(),
        email=Utils().random_email(),
        name=DEFAULT_NAME,
        lastname=DEFAULT_NAME,
        code=DEFAULT_CODE_REGISTRATION
    ).build()
    created_user_registration_code = User().set_user_data(
        phone=DEFAULT_PHONE,
        email=DEFAULT_EMAIL,
        name=DEFAULT_NAME,
        lastname=DEFAULT_NAME,
        code=DEFAULT_CODE_REGISTRATION
    ).build()


@dataclasses.dataclass
class AuthorizationUser:
    user_phone = User().set_user_data(phone=Utils().random_phone()).build()
    user_empty_phone = User().set_user_data(phone="").build()
    user_phone_code = User().set_user_data(phone=Utils().random_phone(), code=Utils().random_code()).build()
    user_default_phone_default_code = User().set_user_data(phone=DEFAULT_PHONE, code=DEFAULT_CODE_AUTHORIZATION).build()


@dataclasses.dataclass
class RedWoodQuery:
    query_product_items = RedWood().generate_redwood_data(productItems)
    query_balances = RedWood().generate_redwood_data(balances)


@dataclasses.dataclass
class RegistrationUserUi:
    user_name_phone_email = Utils().user_profile()
    new_user_name_phone_email = Utils().user_profile()
    registered_user = User().set_user_data(name=DEFAULT_NAME, phone=DEFAULT_PHONE_SECOND, email=DEFAULT_EMAIL).build()
    new_user_with_wrong_credentials = User().set_user_data(
        name=DEFAULT_NAME, phone=Utils.random_data(), email=Utils.random_data()).build()


@dataclasses.dataclass
class AuthorizationUserUi:
    authorized_user = User().set_user_data(name=DEFAULT_NAME_SECOND, phone=DEFAULT_PHONE_SECOND).build()
    new_user = User().set_user_data(phone=Utils().random_phone()).build()
    user_with_invalid_credentials = User().set_user_data(phone=Utils().random_data()).build()


if __name__ == '__main__':
    r = AuthorizationUserUi()
    print(r.user_with_invalid_credentials)

