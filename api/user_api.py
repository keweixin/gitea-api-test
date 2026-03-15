from common.config import Config
from common.request_handler import RequestHandler


class UserApi:
    def __init__(self, request_handler=None):
        self.request_handler = request_handler or RequestHandler()
        self.base_url = Config.BASE_URL.rstrip("/")

    def get_current_user(self):
        url = f"{self.base_url}/user"
        return self.request_handler.get(url)

    def get_current_user_repos(self):
        url = f"{self.base_url}/user/repos"
        return self.request_handler.get(url)

    def get_public_user(self, username):
        url = f"{self.base_url}/users/{username}"
        return self.request_handler.get(url, headers={})

    def get_public_user_repos(self, username):
        url = f"{self.base_url}/users/{username}/repos"
        return self.request_handler.get(url, headers={})
