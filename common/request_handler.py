import requests
from common.config import Config


class RequestHandler:
    def __init__(self, headers=None, timeout=10):
        self.session = requests.Session()
        self.timeout = timeout
        self.default_headers = Config.auth_headers() if headers is None else headers

    def request(self, method, url, **kwargs):
        headers = kwargs.pop("headers", self.default_headers)

        response = self.session.request(
            method=method,
            url=url,
            headers=headers,
            timeout=self.timeout,
            **kwargs
        )

        print(f"\n[Request] {method.upper()} {url}")
        print(f"[Request Headers] {headers}")

        if "json" in kwargs:
            print(f"[Request JSON] {kwargs['json']}")

        print(f"[Response Status] {response.status_code}")
        print(f"[Response Body] {response.text}")

        return response

    def get(self, url, **kwargs):
        return self.request("get", url, **kwargs)

    def post(self, url, **kwargs):
        return self.request("post", url, **kwargs)

    def patch(self, url, **kwargs):
        return self.request("patch", url, **kwargs)

    def delete(self, url, **kwargs):
        return self.request("delete", url, **kwargs)
    def put(self, url, **kwargs):
        return self.request("put", url, **kwargs)
