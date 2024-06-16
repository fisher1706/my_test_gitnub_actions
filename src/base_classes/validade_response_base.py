from __future__ import annotations

from json import JSONDecodeError

from requests import Response
from utils.utils import Utils


class ValidateResponseBase:
    def __init__(self, response: Response):
        self.response = response
        try:
            self.response_json = response.json()
        except JSONDecodeError as e:
            print(f"Error parsing JSON: {e}")
            self.response_json = {}
        Utils.attach_response(self.response_json)
        self.response_status = response.status_code
        self.response_content = response.content

    def assert_status_code(self, status_code: int | list) -> ValidateResponseBase:
        if isinstance(status_code, list):
            assert self.response_status in status_code, self
        else:
            assert self.response_status == status_code, self
        return self

    def validate(self, schema) -> ValidateResponseBase:
        if isinstance(self.response_json, list):
            for item in self.response_json:
                schema.model_validate(item)
        else:
            schema.model_validate(self.response_json)
        return self

    def get_data_from_response_json(self, *args: str) -> ValidateResponseBase:
        for arg in args:
            self.response_json = self.response_json.get(arg)
        return self

    def __str__(self):
        return \
            f"Status code: {self.response_status}\n" \
            f"Requested url: {self.response.url}\n" \
            f"Response body: {self.response_json}\n" \
            f"Response content: {self.response_content}"
