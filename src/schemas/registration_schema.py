from pydantic import BaseModel


class RegistrationPositive(BaseModel):
    email_exists: bool
    phone_exists: bool


class Parameters(BaseModel):
    fieldName: str


class RegistrationNegative(BaseModel):
    message: str
    parameters: Parameters


class RegistrationCodeValid(BaseModel):
    success: bool
    token: str
    redirect: str


class RegistrationCodeInvalid(BaseModel):
    success: bool
    error: str
