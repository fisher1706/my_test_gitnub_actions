import requests
from requests import Response


class ApiClient:

    def __init__(self):
        self.json_headers = {'Content-Type': 'application/json'}

    @staticmethod
    def update_endpoint(endpoint, **kwargs):
        for arg in kwargs:
            endpoint += '/' + str(kwargs[arg])
        return endpoint

    def get(self, url: str, endpoint: str = '', params=None, headers=None) -> Response:
        resp = requests.get(url=url + endpoint, params=params, headers=self.json_headers if not headers else headers)
        return resp

    def post(self, url: str, endpoint: str = '', body=None, headers=None) -> Response:
        resp = requests.post(url=url + endpoint, json=body, headers=self.json_headers if not headers else headers)
        return resp

    def delete(self, url: str, endpoint: str = '', body=None, headers=None) -> Response:
        resp = requests.delete(url=url + endpoint, json=body, headers=self.json_headers if not headers else headers)
        return resp

    def patch(self, url: str, endpoint: str = '', body=None, headers=None) -> Response:
        resp = requests.patch(url=url + endpoint, json=body, headers=self.json_headers if not headers else headers)
        return resp

    def put(self, url: str, endpoint: str = '', body=None, headers=None) -> Response:
        resp = requests.put(url=url + endpoint, json=body, headers=self.json_headers if not headers else headers)
        return resp


if __name__ == '__main__':
    api = ApiClient()

    data = api.update_endpoint(endpoint='test', phone='555-555-555')
    print(data)
