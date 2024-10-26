from __future__ import annotations
from src.base_classes.builder import BuilderBaseClass
from src.enums.rest_endpoint_field import RestEndpointField
from src.generators.user import User


class Goods(BuilderBaseClass):
    def __init__(self):
        super().__init__()
        self.result = {}

    def create_goods_for_order(self, **kwargs) -> Goods:
        self.result.update({key: value for key, value in kwargs.items() if key in RestEndpointField.list()})
        return self


if __name__ == '__main__':
    u = User()
    u.set_user_data(phone=123, code=456)
    print(u.build())
