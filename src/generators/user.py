from __future__ import annotations
from src.base_classes.builder import BuilderBaseClass
from src.enums.rest_endpoint_field import RestEndpointField


class User(BuilderBaseClass):
    def __init__(self):
        super().__init__()
        self.result = {}

    def set_user_data(self, **kwargs) -> User:
        self.result.update({key: value for key, value in kwargs.items() if key in RestEndpointField.list()})
        return self


if __name__ == '__main__':
    u = User()
    u.set_user_data(phone=123, code=456)
    print(u.build())
