from common.config import Config
from common.request_handler import RequestHandler


class RepoApi:
    def __init__(self, request_handler=None):
        self.request_handler = request_handler or RequestHandler()
        self.base_url = Config.BASE_URL.rstrip("/")

    def create_repo(self, name, description="", private=False):
        url = f"{self.base_url}/user/repos"
        payload = {
            "name": name,
            "description": description,
            "private": private,
        }
        return self.request_handler.post(url, json=payload)

    def get_repo(self, owner, repo):
        url = f"{self.base_url}/repos/{owner}/{repo}"
        return self.request_handler.get(url)

    def update_repo(self, owner, repo, data):
        url = f"{self.base_url}/repos/{owner}/{repo}"
        return self.request_handler.patch(url, json=data)

    def delete_repo(self, owner, repo):
        url = f"{self.base_url}/repos/{owner}/{repo}"
        return self.request_handler.delete(url)

    def get_repo_languages(self, owner, repo):
        url = f"{self.base_url}/repos/{owner}/{repo}/languages"
        return self.request_handler.get(url)

    def get_collaborators(self, owner, repo):
        url = f"{self.base_url}/repos/{owner}/{repo}/collaborators"
        return self.request_handler.get(url)

    def add_collaborator(self, owner, repo, collaborator):
        url = f"{self.base_url}/repos/{owner}/{repo}/collaborators/{collaborator}"
        return self.request_handler.put(url)

    def delete_collaborator(self, owner, repo, collaborator):
        url = f"{self.base_url}/repos/{owner}/{repo}/collaborators/{collaborator}"
        return self.request_handler.delete(url)
