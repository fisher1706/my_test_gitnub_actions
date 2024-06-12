from pydantic import BaseModel


class AuthorizationPositive(BaseModel):
    exists: bool


class AuthorizationNegative(BaseModel):
    message: str


# TODO: update pydantic validation (email, url ...)
class AuthorizationCodeRegistrationPositive(BaseModel):
    success: bool
    phone: str
    name: str
    surname: str
    email: str
    customer_id: str
    token: str
    redirect: str


class AuthorizationCodeRegistrationNegative(BaseModel):
    success: bool
